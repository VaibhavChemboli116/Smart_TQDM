"""
Emoji selection logic for SmartBar progress indicators
"""
import time
from typing import Dict, Any, Callable, Optional
from collections import deque


class EmojiSelector:
    """Base class for emoji selection logic"""
    
    @staticmethod
    def intelligent_default_selector(n: int, total: int, metrics: Dict[str, Any], 
                                   best_accuracy: float, best_loss: float,
                                   accuracy_trend: int, loss_trend: int) -> str:
        """Intelligent default emoji selection using trend analysis"""
        progress = n / total
        
        # Check for new best accuracy (with small tolerance)
        if 'acc' in metrics:
            current_acc = float(metrics['acc'])
            if current_acc >= best_accuracy - 0.001:  # Small tolerance for floating point
                return "🥳"  # New best!
        
        # Check for significant improvement trends
        if accuracy_trend == 1:
            return "🚀"  # Improving fast
        elif loss_trend == 1:
            return "🔥"  # Loss decreasing fast
        
        # Check for plateau/stable performance
        if accuracy_trend == 0 and loss_trend == 0:
            if progress > 0.5:
                return "⚡"  # Stable but good progress
            else:
                return "🎯"  # Stable, still early
        
        # Check for declining performance
        if accuracy_trend == -1 or loss_trend == -1:
            return "😅"  # Uh oh, declining
        
        # Progress-based fallback
        if progress >= 1.0:
            return "🏆"  # Complete
        elif progress >= 0.8:
            return "🚀"  # Almost done
        elif progress >= 0.6:
            return "⚡"  # Good progress
        elif progress >= 0.4:
            return "🔥"  # Halfway
        elif progress >= 0.2:
            return "🎯"  # Getting there
        else:
            return "🔍"  # Starting


def accuracy_based_selector(n: int, total: int, metrics: Dict[str, Any], start_time: float, 
                           metric_history: Optional[deque] = None, best_accuracy: float = 0.0, 
                           best_loss: float = float('inf'), accuracy_trend: int = 0, 
                           loss_trend: int = 0) -> str:
    """Intelligent emoji selector based on accuracy trends and improvements"""
    if 'acc' not in metrics:
        return "🎯"
    
    accuracy = float(metrics['acc'])
    
    # Check for new best accuracy (with tolerance)
    if accuracy >= best_accuracy - 0.001:
        return "🥳"  # New best accuracy!
    
    # Check for significant improvement trend
    if accuracy_trend == 1:
        if accuracy > 0.95:
            return "🚀"  # Excellent and improving
        elif accuracy > 0.90:
            return "🔥"  # Good and improving
        elif accuracy > 0.80:
            return "⚡"  # Decent and improving
        else:
            return "📈"  # Improving steadily
    
    # Check for plateau
    if accuracy_trend == 0:
        if accuracy > 0.95:
            return "🏆"  # Excellent but stable
        elif accuracy > 0.90:
            return "🔥"  # Good but stable
        elif accuracy > 0.80:
            return "⚡"  # Decent but stable
        elif accuracy > 0.70:
            return "🎯"  # Average but stable
        else:
            return "📊"  # Low but stable
    
    # Check for decline
    if accuracy_trend == -1:
        if accuracy > 0.90:
            return "😅"  # High but declining
        elif accuracy > 0.80:
            return "😐"  # Decent but declining
        else:
            return "😰"  # Low and declining
    
    # Fallback to absolute values
    if accuracy > 0.95:
        return "🥳"  # Excellent accuracy
    elif accuracy > 0.90:
        return "🔥"  # Good accuracy
    elif accuracy > 0.80:
        return "⚡"  # Decent accuracy
    elif accuracy > 0.70:
        return "🎯"  # Average accuracy
    else:
        return "😅"  # Low accuracy


def loss_based_selector(n: int, total: int, metrics: Dict[str, Any], start_time: float,
                       metric_history: Optional[deque] = None, best_accuracy: float = 0.0, 
                       best_loss: float = float('inf'), accuracy_trend: int = 0, 
                       loss_trend: int = 0) -> str:
    """Intelligent emoji selector based on loss trends and improvements"""
    if 'loss' not in metrics:
        return "🎯"
    
    loss = float(metrics['loss'])
    
    # Check for new best loss (with tolerance)
    if loss <= best_loss + 0.001:
        return "🥳"  # New best loss!
    
    # Check for significant improvement trend
    if loss_trend == 1:
        if loss < 0.1:
            return "🚀"  # Very low and improving
        elif loss < 0.3:
            return "🔥"  # Low and improving
        elif loss < 0.5:
            return "⚡"  # Moderate and improving
        else:
            return "📉"  # High but improving
    
    # Check for plateau
    if loss_trend == 0:
        if loss < 0.1:
            return "🏆"  # Very low but stable
        elif loss < 0.3:
            return "🔥"  # Low but stable
        elif loss < 0.5:
            return "⚡"  # Moderate but stable
        elif loss < 1.0:
            return "🎯"  # High but stable
        else:
            return "📊"  # Very high but stable
    
    # Check for increase
    if loss_trend == -1:
        if loss < 0.5:
            return "😅"  # Low but increasing
        elif loss < 1.0:
            return "😐"  # Moderate but increasing
        else:
            return "😰"  # High and increasing
    
    # Fallback to absolute values
    if loss < 0.1:
        return "🥳"  # Very low loss
    elif loss < 0.3:
        return "🔥"  # Low loss
    elif loss < 0.5:
        return "⚡"  # Moderate loss
    elif loss < 1.0:
        return "🎯"  # High loss
    else:
        return "😅"  # Very high loss


def speed_based_selector(n: int, total: int, metrics: Dict[str, Any], start_time: float) -> str:
    """Emoji selector based on processing speed"""
    if n == 0:
        return "🔍"
    
    elapsed = time.time() - start_time
    speed = n / elapsed if elapsed > 0 else 0
    
    if speed > 50:
        return "🚀"  # Very fast
    elif speed > 20:
        return "⚡"  # Fast
    elif speed > 10:
        return "🔥"  # Normal
    else:
        return "🐌"  # Slow


# Type alias for emoji selector functions
EmojiSelectorFunc = Callable[[int, int, Dict[str, Any], float, Optional[deque], float, float, int, int], str]