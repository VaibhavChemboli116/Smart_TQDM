"""
Emoji selection logic for SmartBar progress indicators
"""
from typing import Dict, Any, Optional
from collections import deque

from .config import ProgressBarConfig, EmojiConfig, DefaultConfig


class EmojiSelector:
    """Base class for emoji selection logic"""
    
    @staticmethod
    def intelligent_default_selector(n: int, total: int, metrics: Dict[str, Any], 
                                   best_accuracy: float, best_loss: float,
                                   accuracy_trend: int, loss_trend: int) -> str:
        """Intelligent default emoji selection using pure trend analysis"""
        
        # Check for new best accuracy (with tolerance)
        if 'acc' in metrics:
            current_acc = float(metrics['acc'])
            if current_acc >= best_accuracy - ProgressBarConfig.BEST_METRIC_TOLERANCE:
                return EmojiConfig.NEW_BEST  # New best!
        
        # Check for new best loss (with tolerance)
        if 'loss' in metrics:
            current_loss = float(metrics['loss'])
            if current_loss <= best_loss + ProgressBarConfig.BEST_METRIC_TOLERANCE:
                return EmojiConfig.NEW_BEST  # New best!
        
        # Pure trend-based selection
        if accuracy_trend == 1 or loss_trend == 1:
            return EmojiConfig.IMPROVING  # Improving trend
        elif accuracy_trend == -1 or loss_trend == -1:
            return EmojiConfig.DECLINING  # Declining trend
        else:
            return EmojiConfig.STABLE  # Stable trend


def accuracy_based_selector(n: int, total: int, metrics: Dict[str, Any], start_time: float, 
                           metric_history: Optional[deque] = None, best_accuracy: float = 0.0, 
                           best_loss: float = float('inf'), accuracy_trend: int = 0, 
                           loss_trend: int = 0) -> str:
    """Intelligent emoji selector based on accuracy trends"""
    if 'acc' not in metrics:
        return EmojiConfig.STABLE
    
    accuracy = float(metrics['acc'])
    
    # Check for new best accuracy (with tolerance)
    if accuracy >= best_accuracy - ProgressBarConfig.BEST_METRIC_TOLERANCE:
        return EmojiConfig.NEW_BEST  # New best accuracy!
    
    # Pure trend-based selection
    if accuracy_trend == 1:
        return EmojiConfig.IMPROVING  # Improving
    elif accuracy_trend == -1:
        if accuracy < DefaultConfig.ACCURACY_AVERAGE:
            return EmojiConfig.DECLINING_SEVERE  # Low accuracy and declining
        else:
            return EmojiConfig.DECLINING  # Declining
    else:
        return EmojiConfig.STABLE  # Stable


def loss_based_selector(n: int, total: int, metrics: Dict[str, Any], start_time: float, 
                       metric_history: Optional[deque] = None, best_accuracy: float = 0.0, 
                       best_loss: float = float('inf'), accuracy_trend: int = 0, 
                       loss_trend: int = 0) -> str:
    """Intelligent emoji selector based on loss trends"""
    if 'loss' not in metrics:
        return EmojiConfig.STABLE
    
    loss = float(metrics['loss'])
    
    # Check for new best loss (with tolerance)
    if loss <= best_loss + ProgressBarConfig.BEST_METRIC_TOLERANCE:
        return EmojiConfig.NEW_BEST  # New best loss!
    
    # Pure trend-based selection
    if loss_trend == 1:
        return EmojiConfig.IMPROVING  # Improving (loss decreasing)
    elif loss_trend == -1:
        if loss > DefaultConfig.LOSS_HIGH:
            return EmojiConfig.DECLINING_SEVERE  # High loss and increasing
        else:
            return EmojiConfig.DECLINING  # Declining (loss increasing)
    else:
        return EmojiConfig.STABLE  # Stable