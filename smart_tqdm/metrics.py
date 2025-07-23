"""
Smart metrics tracking and performance analysis for SmartTQDM
"""

import numpy as np
from typing import Dict, List, Any, Optional, Tuple
from collections import defaultdict, deque
from .themes import PerformanceStatus


class MetricsTracker:
    """Track and store metrics history"""
    
    def __init__(self, max_history: int = 100):
        self.max_history = max_history
        self.history = defaultdict(lambda: deque(maxlen=max_history))
        self.best_values = {}
        self.worst_values = {}
    
    def update(self, metrics: Dict[str, Any]):
        """Update metrics history"""
        for key, value in metrics.items():
            if isinstance(value, (int, float)):
                self.history[key].append(value)
                
                # Update best/worst values
                if key not in self.best_values or value > self.best_values[key]:
                    self.best_values[key] = value
                if key not in self.worst_values or value < self.worst_values[key]:
                    self.worst_values[key] = value
    
    def get_latest(self, metric: str) -> Optional[float]:
        """Get the latest value for a metric"""
        if metric in self.history and self.history[metric]:
            return self.history[metric][-1]
        return None
    
    def get_trend(self, metric: str, window: int = 5) -> Optional[float]:
        """Calculate trend for a metric over a window"""
        if metric not in self.history or len(self.history[metric]) < window:
            return None
        
        values = list(self.history[metric])[-window:]
        if len(values) < 2:
            return None
        
        # Linear regression slope
        x = np.arange(len(values))
        y = np.array(values)
        slope = np.polyfit(x, y, 1)[0]
        return slope
    
    def get_moving_average(self, metric: str, window: int = 5) -> Optional[float]:
        """Calculate moving average for a metric"""
        if metric not in self.history or len(self.history[metric]) < window:
            return None
        
        values = list(self.history[metric])[-window:]
        return np.mean(values)
    
    def get_volatility(self, metric: str, window: int = 10) -> Optional[float]:
        """Calculate volatility (standard deviation) for a metric"""
        if metric not in self.history or len(self.history[metric]) < window:
            return None
        
        values = list(self.history[metric])[-window:]
        return np.std(values)
    
    def reset(self):
        """Reset all tracked metrics"""
        self.history.clear()
        self.best_values.clear()
        self.worst_values.clear()
    
    def get_summary(self) -> Dict[str, Dict[str, float]]:
        """Get summary statistics for all metrics"""
        summary = {}
        for metric in self.history:
            values = list(self.history[metric])
            if values:
                summary[metric] = {
                    'current': values[-1],
                    'mean': np.mean(values),
                    'std': np.std(values),
                    'min': np.min(values),
                    'max': np.max(values),
                    'trend': self.get_trend(metric),
                    'volatility': self.get_volatility(metric)
                }
        return summary


class PerformanceAnalyzer:
    """Analyze performance and determine status for emoji selection"""
    
    def __init__(self, 
                 improvement_threshold: float = 0.001,
                 plateau_threshold: float = 0.0001,
                 volatility_threshold: float = 0.01,
                 window_size: int = 5):
        self.improvement_threshold = improvement_threshold
        self.plateau_threshold = plateau_threshold
        self.volatility_threshold = volatility_threshold
        self.window_size = window_size
    
    def analyze(self, current_metrics: Dict[str, Any], 
                history: Dict[str, deque]) -> PerformanceStatus:
        """Analyze current performance and return status"""
        
        if not current_metrics or not history:
            return PerformanceStatus.IMPROVING
        
        # Analyze each metric
        statuses = []
        for metric, current_value in current_metrics.items():
            if not isinstance(current_value, (int, float)):
                continue
            
            if metric not in history or len(history[metric]) < self.window_size:
                statuses.append(PerformanceStatus.IMPROVING)
                continue
            
            status = self._analyze_metric(metric, current_value, history[metric])
            statuses.append(status)
        
        # Return the most significant status
        return self._prioritize_status(statuses)
    
    def _analyze_metric(self, metric: str, current_value: float, 
                       history: deque) -> PerformanceStatus:
        """Analyze a single metric with special handling for accuracy"""
        
        values = list(history)[-self.window_size:]
        if len(values) < 2:
            return PerformanceStatus.IMPROVING
        
        # Calculate trend
        trend = self._calculate_trend(values)
        
        # Calculate volatility
        volatility = np.std(values)
        
        # Special handling for accuracy metrics
        if 'acc' in metric.lower() or 'accuracy' in metric.lower():
            # For accuracy, higher is better
            if current_value > max(values[:-1]):
                return PerformanceStatus.NEW_BEST
            if current_value > 0.95:  # Excellent accuracy
                return PerformanceStatus.EXCELLENT
            if trend > self.improvement_threshold * 2:  # More sensitive for accuracy
                return PerformanceStatus.IMPROVING
            if abs(trend) < self.plateau_threshold:
                return PerformanceStatus.PLATEAU
            if trend < -self.improvement_threshold:
                return PerformanceStatus.SLOW
        
        # Special handling for loss metrics
        elif 'loss' in metric.lower():
            # For loss, lower is better (invert the logic)
            if current_value < min(values[:-1]):
                return PerformanceStatus.NEW_BEST
            if trend < -self.improvement_threshold:  # Decreasing loss is good
                return PerformanceStatus.IMPROVING
            if trend > self.improvement_threshold:  # Increasing loss is bad
                return PerformanceStatus.SLOW
            if abs(trend) < self.plateau_threshold:
                return PerformanceStatus.PLATEAU
        
        # General metric handling
        else:
            # Check for new best
            if current_value > max(values[:-1]):
                return PerformanceStatus.NEW_BEST
            
            # Check for improvement
            if trend > self.improvement_threshold:
                return PerformanceStatus.IMPROVING
            
            # Check for plateau
            if abs(trend) < self.plateau_threshold:
                return PerformanceStatus.PLATEAU
            
            # Check for slow progress
            if trend < -self.improvement_threshold:
                return PerformanceStatus.SLOW
        
        # Check for instability (applies to all metrics)
        if volatility > self.volatility_threshold:
            return PerformanceStatus.UNSTABLE
        
        return PerformanceStatus.IMPROVING
    
    def _calculate_trend(self, values: List[float]) -> float:
        """Calculate trend using linear regression"""
        if len(values) < 2:
            return 0.0
        
        x = np.arange(len(values))
        y = np.array(values)
        slope = np.polyfit(x, y, 1)[0]
        return slope
    
    def _prioritize_status(self, statuses: List[PerformanceStatus]) -> PerformanceStatus:
        """Prioritize statuses based on importance"""
        priority_order = [
            PerformanceStatus.NEW_BEST,
            PerformanceStatus.WARNING,
            PerformanceStatus.UNSTABLE,
            PerformanceStatus.SLOW,
            PerformanceStatus.PLATEAU,
            PerformanceStatus.IMPROVING,
            PerformanceStatus.EXCELLENT
        ]
        
        for status in priority_order:
            if status in statuses:
                return status
        
        return PerformanceStatus.IMPROVING


class SmartMetrics:
    """Enhanced metrics with smart features"""
    
    def __init__(self, tracker: MetricsTracker = None, analyzer: PerformanceAnalyzer = None):
        self.tracker = tracker or MetricsTracker()
        self.analyzer = analyzer or PerformanceAnalyzer()
        self.alert_callbacks = []
        self.milestone_callbacks = []
    
    def add_alert_callback(self, callback: callable):
        """Add callback for performance alerts"""
        self.alert_callbacks.append(callback)
    
    def add_milestone_callback(self, callback: callable):
        """Add callback for milestone achievements"""
        self.milestone_callbacks.append(callback)
    
    def update(self, metrics: Dict[str, Any], progress: float = None):
        """Update metrics and trigger callbacks"""
        self.tracker.update(metrics)
        
        # Analyze performance
        status = self.analyzer.analyze(metrics, self.tracker.history)
        
        # Check for alerts
        if status in [PerformanceStatus.WARNING, PerformanceStatus.UNSTABLE]:
            self._trigger_alerts(status, metrics)
        
        # Check for milestones
        if progress is not None:
            self._check_milestones(progress, metrics)
        
        return status
    
    def _trigger_alerts(self, status: PerformanceStatus, metrics: Dict[str, Any]):
        """Trigger alert callbacks"""
        for callback in self.alert_callbacks:
            try:
                callback(status, metrics)
            except Exception as e:
                print(f"Alert callback error: {e}")
    
    def _check_milestones(self, progress: float, metrics: Dict[str, Any]):
        """Check for milestone achievements"""
        milestones = [0.25, 0.5, 0.75, 0.9]
        for milestone in milestones:
            if abs(progress - milestone) < 0.01:
                for callback in self.milestone_callbacks:
                    try:
                        callback(milestone, metrics)
                    except Exception as e:
                        print(f"Milestone callback error: {e}")
    
    def get_performance_report(self) -> Dict[str, Any]:
        """Generate comprehensive performance report"""
        summary = self.tracker.get_summary()
        
        report = {
            'summary': summary,
            'best_values': self.tracker.best_values,
            'worst_values': self.tracker.worst_values,
            'recommendations': self._generate_recommendations(summary)
        }
        
        return report
    
    def _generate_recommendations(self, summary: Dict[str, Dict[str, float]]) -> List[str]:
        """Generate recommendations based on performance"""
        recommendations = []
        
        for metric, stats in summary.items():
            trend = stats.get('trend', 0)
            volatility = stats.get('volatility', 0)
            
            if trend < -0.01:
                recommendations.append(f"⚠️ {metric} is declining rapidly")
            elif volatility > 0.1:
                recommendations.append(f"📊 {metric} is very unstable")
            elif abs(trend) < 0.001:
                recommendations.append(f"🐢 {metric} has plateaued")
            elif trend > 0.01:
                recommendations.append(f"🔥 {metric} is improving well")
        
        return recommendations


class MetricsVisualizer:
    """Visualize metrics in real-time"""
    
    def __init__(self, metrics: SmartMetrics):
        self.metrics = metrics
        self.plot_data = defaultdict(list)
    
    def update_plot(self, metrics: Dict[str, Any], step: int):
        """Update plot data"""
        for key, value in metrics.items():
            if isinstance(value, (int, float)):
                self.plot_data[key].append((step, value))
    
    def get_ascii_plot(self, metric: str, width: int = 50, height: int = 10) -> str:
        """Generate ASCII plot for a metric"""
        if metric not in self.plot_data or len(self.plot_data[metric]) < 2:
            return "No data available"
        
        data = self.plot_data[metric]
        if len(data) < 2:
            return "Insufficient data"
        
        # Extract values
        values = [point[1] for point in data]
        min_val, max_val = min(values), max(values)
        
        if max_val == min_val:
            return "No variation in data"
        
        # Create ASCII plot
        plot_lines = []
        for i in range(height):
            y = max_val - (i * (max_val - min_val) / (height - 1))
            line = f"{y:8.3f} |"
            
            for j, value in enumerate(values):
                if j >= width:
                    break
                if abs(value - y) < (max_val - min_val) / (height * 2):
                    line += "●"
                else:
                    line += " "
            
            plot_lines.append(line)
        
        # Add x-axis
        x_axis = "         +" + "-" * width
        plot_lines.append(x_axis)
        
        return "\n".join(plot_lines) 