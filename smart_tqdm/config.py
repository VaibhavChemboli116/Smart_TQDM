"""
Configuration constants and settings for SmartBar
"""

# Progress bar configuration
class ProgressBarConfig:
    """Configuration constants for progress bar display"""
    SLIM_CHAR = '━'  # Character used for filled bar sections
    MIN_BAR_WIDTH = 10  # Minimum width for progress bar
    MIN_TERM_WIDTH = 40  # Minimum terminal width
    DEFAULT_HISTORY_SIZE = 5  # Default metric history size for trend analysis
    
    # Trend detection thresholds
    ACCURACY_THRESHOLD = 0.005  # Sensitivity for accuracy trend detection
    LOSS_THRESHOLD = 0.005  # Sensitivity for loss trend detection
    
    # Best metric tolerance (for floating point comparisons)
    BEST_METRIC_TOLERANCE = 0.001


# Emoji mapping for different states
class EmojiConfig:
    """Emoji constants for different progress states"""
    
    # Achievement emojis
    NEW_BEST = "🥳"
    COMPLETE = "🏆"
    
    # Improvement emojis
    IMPROVING_FAST = "🚀"
    IMPROVING = "🔥"
    IMPROVING_STEADY = "⚡"
    IMPROVING_TREND = "📈"
    LOSS_IMPROVING = "📉"
    
    # Stable performance emojis
    STABLE_GOOD = "⚡"
    STABLE_EARLY = "🎯"
    STABLE_EXCELLENT = "🏆"
    STABLE_AVERAGE = "🎯"
    STABLE_LOW = "📊"
    
    # Declining performance emojis
    DECLINING = "😅"
    DECLINING_DECENT = "😐"
    DECLINING_LOW = "😰"
    
    # Progress-based emojis
    STARTING = "🔍"
    GETTING_THERE = "🎯"
    HALFWAY = "🔥"
    GOOD_PROGRESS = "⚡"
    ALMOST_DONE = "🚀"
    
    # Speed-based emojis
    VERY_FAST = "🚀"
    FAST = "⚡"
    NORMAL = "🔥"
    SLOW = "🐌"


# Color configuration for gradient bars
class ColorConfig:
    """Color configuration for gradient progress bars"""
    
    # RGB color values for gradient
    RED = (255, 0, 0)      # Start color (0% progress)
    YELLOW = (255, 255, 0)  # Middle color (50% progress)
    GREEN = (0, 255, 0)     # End color (100% progress)


# Default configuration values
class DefaultConfig:
    """Default configuration values for SmartBar"""
    
    SHOW_EMOJI = True
    SHOW_METRICS = True
    HEAD_EMOJI = "👉"
    DESCRIPTION = ""
    WIDTH = None  # Auto-calculate based on terminal width
    
    # Performance thresholds for emoji selection
    ACCURACY_EXCELLENT = 0.95
    ACCURACY_GOOD = 0.90
    ACCURACY_DECENT = 0.80
    ACCURACY_AVERAGE = 0.70
    
    LOSS_VERY_LOW = 0.1
    LOSS_LOW = 0.3
    LOSS_MODERATE = 0.5
    LOSS_HIGH = 1.0
    
    # Speed thresholds (items per second)
    SPEED_VERY_FAST = 50
    SPEED_FAST = 20
    SPEED_NORMAL = 10