"""
Metric tracking and trend analysis for SmartBar
"""
import time
from collections import deque
from typing import Dict, Any, Optional

try:
    from typing import Deque
except ImportError:
    # For Python < 3.9, use typing_extensions or fallback
    try:
        from typing_extensions import Deque
    except ImportError:
        from typing import Any as Deque


class MetricTracker:
    """Handles metric history tracking and trend analysis"""
    
    def __init__(self, history_size: int = 5):
        self.history_size = history_size
        self.metric_history: Deque[Dict[str, Any]] = deque(maxlen=history_size)
        self.best_accuracy = 0.0
        self.best_loss = float('inf')
        self.accuracy_trend = 0  # -1: decreasing, 0: stable, 1: increasing
        self.loss_trend = 0      # -1: decreasing, 0: stable, 1: increasing
    
    def update_metrics(self, n: int, start_time: float, **kwargs) -> None:
        """Update metrics and store in history"""
        current_metrics = {
            'n': n,
            'time': time.time() - start_time,
            **kwargs
        }
        self.metric_history.append(current_metrics)
        
        # Update best values
        if 'acc' in kwargs:
            acc = float(kwargs['acc'])
            if acc > self.best_accuracy:
                self.best_accuracy = acc
        
        if 'loss' in kwargs:
            loss = float(kwargs['loss'])
            if loss < self.best_loss:
                self.best_loss = loss
        
        # Calculate trends if we have enough history
        self._update_trends()
    
    def _update_trends(self) -> None:
        """Update accuracy and loss trends based on recent history"""
        if len(self.metric_history) < 3:
            return
        
        # Get last 3 entries for trend calculation
        recent = list(self.metric_history)[-3:]
        
        # Calculate accuracy trend with more sensitive thresholds
        if all('acc' in entry for entry in recent):
            acc_values = [float(entry['acc']) for entry in recent]
            # More sensitive threshold for accuracy changes
            threshold = 0.005  # Reduced from 0.01
            if acc_values[-1] > acc_values[0] + threshold:  # Significant improvement
                self.accuracy_trend = 1
            elif acc_values[-1] < acc_values[0] - threshold:  # Significant decrease
                self.accuracy_trend = -1
            else:
                self.accuracy_trend = 0  # Stable
        
        # Calculate loss trend with more sensitive thresholds
        if all('loss' in entry for entry in recent):
            loss_values = [float(entry['loss']) for entry in recent]
            # More sensitive threshold for loss changes
            threshold = 0.005  # Reduced from 0.01
            if loss_values[-1] < loss_values[0] - threshold:  # Significant improvement
                self.loss_trend = 1
            elif loss_values[-1] > loss_values[0] + threshold:  # Significant increase
                self.loss_trend = -1
            else:
                self.loss_trend = 0  # Stable
    
    def get_trend_data(self) -> Dict[str, Any]:
        """Get current trend analysis data"""
        return {
            'metric_history': self.metric_history,
            'best_accuracy': self.best_accuracy,
            'best_loss': self.best_loss,
            'accuracy_trend': self.accuracy_trend,
            'loss_trend': self.loss_trend
        }