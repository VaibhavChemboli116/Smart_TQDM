"""
Smart TQDM - Intelligent Stateful Progress Bar with Emoji Feedback

A smart progress bar library with:
- Intelligent emoji-based performance feedback
- Stateful metric history tracking
- Trend detection (improvement/plateau/decline)
- Configurable emoji selection (accuracy vs loss vs default)
- Color gradient progress bars
- Smart metrics awareness
- Neural network training focused

Author: IEEE Research Project
Version: 2.0.0
"""

# Import main components from modular structure
from .smart_bar import SmartBar
from .emoji_selectors import (
    accuracy_based_selector, 
    loss_based_selector, 
    speed_based_selector,
    EmojiSelector
)
from .metrics import MetricTracker
from .display import TerminalRenderer
from .config import (
    ProgressBarConfig, 
    EmojiConfig, 
    ColorConfig, 
    DefaultConfig
)

__version__ = "2.0.0"
__author__ = "IEEE Research Project"

# Maintain backward compatibility with existing API
__all__ = [
    # Main progress bar class
    "SmartBar",
    
    # Predefined emoji selectors
    "accuracy_based_selector",
    "loss_based_selector", 
    "speed_based_selector",
    
    # Advanced components (for custom usage)
    "EmojiSelector",
    "MetricTracker",
    "TerminalRenderer",
    
    # Configuration classes
    "ProgressBarConfig",
    "EmojiConfig", 
    "ColorConfig",
    "DefaultConfig"
] 