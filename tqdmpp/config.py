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
    LOSS_THRESHOLD = 0.01  # Sensitivity for loss trend detection
    
    # Best metric tolerance (for floating point comparisons)
    BEST_METRIC_TOLERANCE = 0.001


# Emoji mapping for different states
class EmojiConfig:
    """Emoji constants for trend-based progress states"""
    
    # Achievement emojis
    NEW_BEST = "🥳"
    
    # Trend-based emojis
    IMPROVING = "🚀"      # For accuracy_trend = 1 or loss_trend = 1
    STABLE = "🎯"         # For accuracy_trend = 0 and loss_trend = 0
    DECLINING = "😅"      # For accuracy_trend = -1 or loss_trend = -1
    DECLINING_SEVERE = "😰"  # For severe declining performance


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
    
    # Performance thresholds for emoji selection (only the ones actually used)
    ACCURACY_AVERAGE = 0.70  # Used in emoji_selectors.py for severe declining check
    LOSS_HIGH = 1.0          # Used in emoji_selectors.py for severe declining check