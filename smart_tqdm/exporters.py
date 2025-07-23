"""
Export and reporting capabilities for SmartTQDM
"""

import os
import json
import time
from typing import Dict, Any, List, Optional
from datetime import datetime
try:
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    from matplotlib.patches import Rectangle
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False
import numpy as np


class GIFExporter:
    """Export animated progress bars as GIFs"""
    
    def __init__(self, fps: int = 10, dpi: int = 100):
        self.fps = fps
        self.dpi = dpi
        self.frames = []
        self.metrics_history = []
    
    def capture_frame(self, progress_bar, metrics: Dict[str, Any] = None):
        """Capture a frame of the progress bar"""
        frame_data = {
            'timestamp': time.time(),
            'progress': progress_bar._tqdm.n / progress_bar._tqdm.total if progress_bar._tqdm else 0,
            'metrics': metrics or {},
            'emoji': progress_bar.theme.get_emoji(progress_bar.performance_analyzer.analyze(
                metrics or {}, progress_bar.metrics_tracker.history
            )) if metrics else "📊"
        }
        self.frames.append(frame_data)
    
    def export(self, progress_bar, filename: str, duration: float = 2.0):
        """Export progress bar animation as GIF"""
        if not MATPLOTLIB_AVAILABLE:
            print("Matplotlib is required for GIF export. Install with: pip install matplotlib")
            return
            
        if not self.frames:
            print("No frames captured. Use capture_frame() first.")
            return
        
        # Create matplotlib figure
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
        fig.suptitle('SmartTQDM Progress Animation', fontsize=16)
        
        # Progress bar subplot
        ax1.set_xlim(0, 1)
        ax1.set_ylim(0, 1)
        ax1.set_title('Progress Bar')
        ax1.set_xlabel('Progress')
        ax1.set_ylabel('Status')
        
        # Metrics subplot
        ax2.set_title('Metrics Over Time')
        ax2.set_xlabel('Time')
        ax2.set_ylabel('Value')
        
        # Animation function
        def animate(frame_idx):
            ax1.clear()
            ax2.clear()
            
            frame = self.frames[frame_idx]
            progress = frame['progress']
            emoji = frame['emoji']
            metrics = frame['metrics']
            
            # Draw progress bar
            bar = Rectangle((0, 0.3), progress, 0.4, facecolor='lightblue', edgecolor='black')
            ax1.add_patch(bar)
            ax1.set_xlim(0, 1)
            ax1.set_ylim(0, 1)
            ax1.text(0.5, 0.5, f'{emoji} {progress:.1%}', 
                    ha='center', va='center', fontsize=20)
            ax1.set_title(f'Progress: {progress:.1%}')
            
            # Plot metrics
            if metrics:
                times = [f['timestamp'] - self.frames[0]['timestamp'] 
                        for f in self.frames[:frame_idx + 1]]
                for metric, value in metrics.items():
                    if isinstance(value, (int, float)):
                        values = [f['metrics'].get(metric, 0) 
                                for f in self.frames[:frame_idx + 1]]
                        ax2.plot(times, values, label=metric, marker='o')
                
                ax2.legend()
                ax2.set_title('Metrics Over Time')
                ax2.set_xlabel('Time (seconds)')
                ax2.set_ylabel('Value')
        
        # Create animation
        anim = animation.FuncAnimation(
            fig, animate, frames=len(self.frames), 
            interval=duration * 1000 / len(self.frames), 
            repeat=True, blit=False
        )
        
        # Save as GIF
        anim.save(filename, writer='pillow', fps=self.fps, dpi=self.dpi)
        plt.close()
        
        print(f"GIF exported to: {filename}")
    
    def export_metrics_gif(self, metrics_history: Dict[str, List[float]], 
                          filename: str, duration: float = 3.0):
        """Export metrics animation as GIF"""
        if not MATPLOTLIB_AVAILABLE:
            print("Matplotlib is required for GIF export. Install with: pip install matplotlib")
            return
            
        if not metrics_history:
            print("No metrics history provided.")
            return
        
        # Create figure
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.set_title('Metrics Animation')
        ax.set_xlabel('Time Steps')
        ax.set_ylabel('Value')
        
        # Prepare data
        max_length = max(len(values) for values in metrics_history.values())
        x_data = list(range(max_length))
        
        # Animation function
        def animate(frame):
            ax.clear()
            ax.set_title('Metrics Animation')
            ax.set_xlabel('Time Steps')
            ax.set_ylabel('Value')
            
            for metric, values in metrics_history.items():
                if frame < len(values):
                    ax.plot(x_data[:frame + 1], values[:frame + 1], 
                           label=metric, marker='o')
            
            ax.legend()
            ax.grid(True, alpha=0.3)
        
        # Create animation
        anim = animation.FuncAnimation(
            fig, animate, frames=max_length,
            interval=duration * 1000 / max_length,
            repeat=True, blit=False
        )
        
        # Save as GIF
        anim.save(filename, writer='pillow', fps=self.fps, dpi=self.dpi)
        plt.close()
        
        print(f"Metrics GIF exported to: {filename}")


class ReportGenerator:
    """Generate comprehensive reports from SmartTQDM data"""
    
    def __init__(self, output_dir: str = "reports"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
    
    def generate_report(self, progress_bar, filename: str = None) -> str:
        """Generate comprehensive report"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"smart_tqdm_report_{timestamp}.html"
        
        filepath = os.path.join(self.output_dir, filename)
        
        # Generate report content
        report_content = self._create_html_report(progress_bar)
        
        # Save report
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(report_content)
        
        print(f"Report generated: {filepath}")
        return filepath
    
    def _create_html_report(self, progress_bar) -> str:
        """Create HTML report content"""
        metrics_history = progress_bar.get_metrics_history()
        summary = progress_bar.metrics_tracker.get_summary()
        
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>SmartTQDM Report</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                         color: white; padding: 20px; border-radius: 10px; }}
                .section {{ margin: 20px 0; padding: 20px; border: 1px solid #ddd; border-radius: 5px; }}
                .metric-card {{ display: inline-block; margin: 10px; padding: 15px; 
                              background: #f8f9fa; border-radius: 5px; min-width: 200px; }}
                .emoji {{ font-size: 24px; }}
                .chart {{ width: 100%; height: 400px; margin: 20px 0; }}
                .recommendation {{ background: #e3f2fd; padding: 10px; margin: 5px 0; border-radius: 5px; }}
            </style>
            <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
        </head>
        <body>
            <div class="header">
                <h1>🚀 SmartTQDM Performance Report</h1>
                <p>Generated on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
            </div>
            
            <div class="section">
                <h2>📊 Metrics Summary</h2>
                {self._generate_metrics_summary(summary)}
            </div>
            
            <div class="section">
                <h2>📈 Performance Charts</h2>
                {self._generate_charts(metrics_history)}
            </div>
            
            <div class="section">
                <h2>🎯 Recommendations</h2>
                {self._generate_recommendations(summary)}
            </div>
            
            <div class="section">
                <h2>⚙️ Configuration</h2>
                {self._generate_config_section(progress_bar)}
            </div>
        </body>
        </html>
        """
        
        return html_content
    
    def _generate_metrics_summary(self, summary: Dict[str, Dict[str, float]]) -> str:
        """Generate metrics summary HTML"""
        if not summary:
            return "<p>No metrics data available.</p>"
        
        html = ""
        for metric, stats in summary.items():
            emoji = "📊"
            if stats.get('trend', 0) > 0.01:
                emoji = "🔥"
            elif stats.get('trend', 0) < -0.01:
                emoji = "📉"
            elif stats.get('volatility', 0) > 0.1:
                emoji = "⚠️"
            
            html += f"""
            <div class="metric-card">
                <div class="emoji">{emoji}</div>
                <h3>{metric}</h3>
                <p><strong>Current:</strong> {stats.get('current', 'N/A'):.4f}</p>
                <p><strong>Mean:</strong> {stats.get('mean', 'N/A'):.4f}</p>
                <p><strong>Trend:</strong> {stats.get('trend', 'N/A'):.4f}</p>
                <p><strong>Volatility:</strong> {stats.get('volatility', 'N/A'):.4f}</p>
            </div>
            """
        
        return html
    
    def _generate_charts(self, metrics_history: Dict[str, List[float]]) -> str:
        """Generate interactive charts HTML"""
        if not metrics_history:
            return "<p>No metrics history available.</p>"
        
        charts_html = ""
        for metric, values in metrics_history.items():
            if len(values) < 2:
                continue
            
            x_data = list(range(len(values)))
            charts_html += f"""
            <div class="chart">
                <h3>{metric} Over Time</h3>
                <div id="chart_{metric.replace(' ', '_')}"></div>
                <script>
                    var data = [{{
                        x: {x_data},
                        y: {values},
                        type: 'scatter',
                        mode: 'lines+markers',
                        name: '{metric}',
                        line: {{color: '#667eea'}}
                    }}];
                    
                    var layout = {{
                        title: '{metric} Progress',
                        xaxis: {{title: 'Time Steps'}},
                        yaxis: {{title: 'Value'}},
                        height: 300
                    }};
                    
                    Plotly.newPlot('chart_{metric.replace(' ', '_')}', data, layout);
                </script>
            </div>
            """
        
        return charts_html
    
    def _generate_recommendations(self, summary: Dict[str, Dict[str, float]]) -> str:
        """Generate recommendations HTML"""
        recommendations = []
        
        for metric, stats in summary.items():
            trend = stats.get('trend', 0)
            volatility = stats.get('volatility', 0)
            
            if trend < -0.01:
                recommendations.append(f"⚠️ {metric} is declining rapidly - consider adjusting learning rate or model architecture")
            elif volatility > 0.1:
                recommendations.append(f"📊 {metric} is very unstable - consider using gradient clipping or reducing batch size")
            elif abs(trend) < 0.001:
                recommendations.append(f"🐢 {metric} has plateaued - consider early stopping or learning rate scheduling")
            elif trend > 0.01:
                recommendations.append(f"🔥 {metric} is improving well - continue current approach")
        
        if not recommendations:
            recommendations.append("🎉 All metrics are performing well!")
        
        html = ""
        for rec in recommendations:
            html += f'<div class="recommendation">{rec}</div>'
        
        return html
    
    def _generate_config_section(self, progress_bar) -> str:
        """Generate configuration section HTML"""
        config = {
            "Theme": progress_bar.theme.__class__.__name__,
            "Animation": progress_bar.animation.__class__.__name__,
            "Total Steps": progress_bar._tqdm.total if progress_bar._tqdm else "N/A",
            "Current Step": progress_bar._tqdm.n if progress_bar._tqdm else "N/A"
        }
        
        html = "<div class='metric-card'>"
        for key, value in config.items():
            html += f"<p><strong>{key}:</strong> {value}</p>"
        html += "</div>"
        
        return html
    
    def export_json(self, progress_bar, filename: str = None) -> str:
        """Export data as JSON"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"smart_tqdm_data_{timestamp}.json"
        
        filepath = os.path.join(self.output_dir, filename)
        
        data = {
            "timestamp": datetime.now().isoformat(),
            "metrics_history": progress_bar.get_metrics_history(),
            "summary": progress_bar.metrics_tracker.get_summary(),
            "best_values": progress_bar.metrics_tracker.best_values,
            "worst_values": progress_bar.metrics_tracker.worst_values
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, default=str)
        
        print(f"JSON data exported: {filepath}")
        return filepath
    
    def export_csv(self, progress_bar, filename: str = None) -> str:
        """Export metrics as CSV"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"smart_tqdm_metrics_{timestamp}.csv"
        
        filepath = os.path.join(self.output_dir, filename)
        metrics_history = progress_bar.get_metrics_history()
        
        if not metrics_history:
            print("No metrics data to export.")
            return ""
        
        # Find the maximum length
        max_length = max(len(values) for values in metrics_history.values())
        
        with open(filepath, 'w', encoding='utf-8') as f:
            # Write header
            f.write("step," + ",".join(metrics_history.keys()) + "\n")
            
            # Write data
            for step in range(max_length):
                row = [str(step)]
                for metric in metrics_history.keys():
                    values = metrics_history[metric]
                    value = values[step] if step < len(values) else ""
                    row.append(str(value))
                f.write(",".join(row) + "\n")
        
        print(f"CSV data exported: {filepath}")
        return filepath 