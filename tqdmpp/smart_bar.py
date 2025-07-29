"""
SmartBar - Intelligent Stateful Progress Bar with Emoji Feedback

Main SmartBar class that coordinates all modular components.
"""
import time
from typing import Dict, Any, Optional, Callable

from .metrics import MetricTracker
from .display import TerminalRenderer
from .emoji_selectors import EmojiSelector, accuracy_based_selector, loss_based_selector
from .config import ProgressBarConfig, EmojiConfig


class SmartBar:
    """
    Intelligent progress bar with emoji feedback and trend analysis
    
    Features:
    - Metric history tracking and trend detection
    - Intelligent emoji selection based on performance patterns
    - Color gradient progress bars
    - Real-time metrics display
    - Terminal width adaptation
    """
    
    def __init__(self, total: int, desc: str = "", width: Optional[int] = None, 
                 show_emoji: bool = True, show_metrics: bool = True, 
                 emoji_selector: Optional[Callable] = None):
        """
        Initialize SmartBar with modular components
        
        Args:
            total: Total number of iterations
            desc: Description text for the progress bar
            width: Fixed width (None for auto-calculation)
            show_emoji: Whether to show emoji indicators
            show_metrics: Whether to show metrics display
            emoji_selector: Custom emoji selection function
        """
        # Basic configuration
        self.total = total
        self.desc = desc
        self.width = width
        self.show_emoji = show_emoji
        self.show_metrics = show_metrics
        self.emoji_selector = emoji_selector
        
        # Progress tracking
        self.start_time = time.time()
        self.n = 0
        self.emoji = ""
        self.metrics: Dict[str, Any] = {}
        
        # Initialize modular components
        self.metric_tracker = MetricTracker(ProgressBarConfig.DEFAULT_HISTORY_SIZE)
        self.renderer = TerminalRenderer()
        self.emoji_selector_instance = EmojiSelector()

    def set_emoji_selector(self, selector_func: Callable) -> None:
        """Set custom emoji selector function"""
        self.emoji_selector = selector_func

    def set_metrics(self, **kwargs) -> None:
        """Set metrics and update history for trend analysis"""
        self.metrics.update(kwargs)
        
        # Update metric tracker with current progress
        self.metric_tracker.update_metrics(self.n, self.start_time, **kwargs)

    def _select_emoji(self) -> str:
        """Select emoji using the configured selector"""
        trend_data = self.metric_tracker.get_trend_data()
        
        return self.emoji_selector(
            self.n, self.total, self.metrics, self.start_time,
            trend_data['metric_history'], trend_data['best_accuracy'],
            trend_data['best_loss'], trend_data['accuracy_trend'],
            trend_data['loss_trend']
        )

    def _print_bar(self) -> None:
        """Internal method to print the progress bar"""
        # Use intelligent default emoji selection based on trends and progress
        trend_data = self.metric_tracker.get_trend_data()
        self.emoji = self.emoji_selector_instance.intelligent_default_selector(
            self.n, self.total, self.metrics,
            trend_data['best_accuracy'], trend_data['best_loss'],
            trend_data['accuracy_trend'], trend_data['loss_trend']
        )

        # Update emoji based on custom selector if configured
        if self.show_emoji and self.emoji_selector:
            self.emoji = self._select_emoji()
        
        # Render and print the progress bar
        bar_str = self.renderer.render_progress_bar(
            self.n, self.total, self.desc, self.emoji, self.metrics, 
            self.start_time, self.show_emoji, self.show_metrics
        )
        self.renderer.print_bar(bar_str)
    
    def __iter__(self):
        """Make SmartBar iterable"""
        return self
    
    def __next__(self):
        """Iterator protocol for automatic progress updates"""
        if self.n >= self.total:
            self.renderer.finish()  # New line when done
            raise StopIteration
        self.n += 1
        self._print_bar()
        return self.n - 1  # Return previous iteration number 