"""
Core SmartTQDM implementation with intelligent progress tracking
"""

import time
import sys
import threading
from typing import Dict, Any, Optional, Callable, Union, List
from contextlib import contextmanager
import numpy as np
from tqdm import tqdm

from .themes import Theme, DefaultTheme
from .animations import FluidAnimation, WaveAnimation
from .metrics import MetricsTracker, PerformanceAnalyzer


class FluidTQDM(tqdm):
    """Custom tqdm subclass that supports fluid animations"""
    
    def __init__(self, *args, animation=None, **kwargs):
        # Remove animation from kwargs before passing to parent
        kwargs_copy = kwargs.copy()
        if 'animation' in kwargs_copy:
            kwargs_copy.pop('animation')
        
        super().__init__(*args, **kwargs_copy)
        self.animation = animation
        self.animation_frame = 0
    
    def format_meter(self, n, total, elapsed, ncols=None, prefix='', ascii=False, unit='it',
                     unit_scale=False, rate=None, bar_format=None, postfix=None,
                     unit_divisor=1000, initial=0, colour=None, **extra_kwargs):
        """Override format_meter to use fluid animation"""
        if self.animation and hasattr(self.animation, 'get_bar'):
            # Use custom fluid animation
            progress = n / total if total else 0
            custom_bar = self.animation.get_bar(progress, self.animation_frame)
            
            # Get the original format but replace the bar
            original = super().format_meter(n, total, elapsed, ncols, prefix, ascii, unit,
                                          unit_scale, rate, bar_format, postfix,
                                          unit_divisor, initial, colour, **extra_kwargs)
            
            # Replace the standard bar with our fluid bar
            if '|' in original:
                parts = original.split('|')
                if len(parts) >= 3:
                    # Replace middle part (the bar) with our custom fluid bar
                    parts[1] = custom_bar
                    return '|'.join(parts)
            
            return original
        else:
            # Fallback to standard tqdm
            return super().format_meter(n, total, elapsed, ncols, prefix, ascii, unit,
                                      unit_scale, rate, bar_format, postfix,
                                      unit_divisor, initial, colour, **extra_kwargs)


class SmartTQDM:
    """
    Smart TQDM with emoji feedback, fluid visualization, and intelligent metrics tracking
    """
    
    def __init__(
        self,
        iterable=None,
        desc=None,
        total=None,
        leave=True,
        file=None,
        ncols=None,
        mininterval=0.1,
        maxinterval=10.0,
        miniters=None,
        ascii=False,
        disable=False,
        unit='it',
        unit_scale=False,
        dynamic_ncols=False,
        smoothing=0.3,
        bar_format=None,
        initial=0,
        position=None,
        postfix=None,
        unit_divisor=1000,
        write_bytes=None,
        lock_args=None,
        nrows=None,
        colour=None,
        delay=0,
        gui=False,
        **kwargs
    ):
        # Standard tqdm parameters
        self.iterable = iterable
        self.desc = desc
        self.total = total
        self.leave = leave
        self.file = file or sys.stderr
        self.ncols = ncols
        self.mininterval = mininterval
        self.maxinterval = maxinterval
        self.miniters = miniters
        self.ascii = ascii
        self.disable = disable
        self.unit = unit
        self.unit_scale = unit_scale
        self.dynamic_ncols = dynamic_ncols
        self.smoothing = smoothing
        self.bar_format = bar_format
        self.initial = initial
        self.position = position
        self.postfix = postfix
        self.unit_divisor = unit_divisor
        self.write_bytes = write_bytes
        self.lock_args = lock_args
        self.nrows = nrows
        self.colour = colour
        self.delay = delay
        self.gui = gui
        
        # Smart features
        self.theme = kwargs.get('theme', DefaultTheme())
        self.animation = kwargs.get('animation', WaveAnimation())
        self.metrics = kwargs.get('metrics', {})
        self.metrics_tracker = MetricsTracker()
        self.performance_analyzer = PerformanceAnalyzer()
        
        # Animation state
        self.animation_frame = 0
        self.last_update = time.time()
        self.animation_thread = None
        self.animation_running = False
        
        # Performance tracking
        self.current_metrics = {}
        self.best_metrics = {}
        self.milestone_reached = False
        
        # Initialize tqdm
        self._tqdm = None
        self._setup_tqdm()
    
    def _setup_tqdm(self):
        """Initialize the underlying tqdm instance"""
        if self.iterable is not None:
            self._tqdm = tqdm(
                iterable=self.iterable,
                desc=self.desc,
                total=self.total,
                leave=self.leave,
                file=self.file,
                ncols=self.ncols,
                mininterval=self.mininterval,
                maxinterval=self.maxinterval,
                miniters=self.miniters,
                ascii=self.ascii,
                disable=self.disable,
                unit=self.unit,
                unit_scale=self.unit_scale,
                dynamic_ncols=self.dynamic_ncols,
                smoothing=self.smoothing,
                bar_format=self._get_smart_bar_format(),
                initial=self.initial,
                position=self.position,
                postfix=self.postfix,
                unit_divisor=self.unit_divisor,
                write_bytes=self.write_bytes,
                lock_args=self.lock_args,
                nrows=self.nrows,
                colour=self.colour,
                delay=self.delay,
                gui=self.gui
            )
            # Store original description for emoji updates
            self._original_desc = self.desc or "Progress"
    
    def _get_smart_bar_format(self) -> str:
        """Generate smart bar format with emoji and fluid visualization"""
        if self.bar_format:
            return self.bar_format
        
        # Standard format without emoji in format string (we'll add emoji dynamically)
        return (
            "{desc}: {percentage:3.0f}%|{bar}| "
            "{n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]"
        )
    
    def update_metrics(self, metrics: Dict[str, Any]):
        """Update current metrics and analyze performance"""
        self.current_metrics.update(metrics)
        self.metrics_tracker.update(metrics)
        
        # Analyze performance for emoji selection
        performance_status = self.performance_analyzer.analyze(
            self.current_metrics, 
            self.metrics_tracker.history
        )
        
        # Update emoji based on performance
        emoji = self.theme.get_emoji(performance_status)
        
        # Check for milestones
        if self._tqdm and self._tqdm.n > 0:
            progress = self._tqdm.n / self._tqdm.total
            if self._check_milestone(progress):
                self.milestone_reached = True
                emoji = self.theme.get_milestone_emoji(progress)
        
        # Update the progress bar description with the new emoji
        if self._tqdm:
            # Add emoji to the description
            if hasattr(self, '_original_desc'):
                new_desc = f"{emoji} {self._original_desc}"
            else:
                self._original_desc = self.desc or "Progress"
                new_desc = f"{emoji} {self._original_desc}"
            self._tqdm.set_description(new_desc)
        
        # Update postfix with metrics only (emoji is now in the bar format)
        self._update_postfix_metrics_only(metrics)
    
    def _check_milestone(self, progress: float) -> bool:
        """Check if a milestone has been reached"""
        milestones = [0.25, 0.5, 0.75, 0.9]
        for milestone in milestones:
            if abs(progress - milestone) < 0.01:
                return True
        return False
    
    def _update_postfix_metrics_only(self, metrics: Dict[str, Any]):
        """Update the postfix with formatted metrics only"""
        if not self._tqdm:
            return
        
        # Format metrics for display
        formatted_metrics = []
        for key, value in metrics.items():
            if isinstance(value, float):
                formatted_metrics.append(f"{key}: {value:.4f}")
            else:
                formatted_metrics.append(f"{key}: {value}")
        
        # Create postfix with metrics only (emoji is shown in the bar)
        if formatted_metrics:
            postfix = ' | '.join(formatted_metrics)
            self._tqdm.set_postfix_str(postfix)
    
    def _get_fluid_bar(self) -> str:
        """Generate fluid progress bar with animation"""
        if not self._tqdm:
            return ""
        
        progress = self._tqdm.n / self._tqdm.total if self._tqdm.total else 0
        return self.animation.get_bar(progress, self.animation_frame)
    
    def start_animation(self):
        """Start the fluid animation thread"""
        if self.animation_running:
            return
        
        self.animation_running = True
        self.animation_thread = threading.Thread(target=self._animation_loop)
        self.animation_thread.daemon = True
        self.animation_thread.start()
    
    def stop_animation(self):
        """Stop the fluid animation thread"""
        self.animation_running = False
        if self.animation_thread:
            self.animation_thread.join()
    
    def _animation_loop(self):
        """Animation loop for fluid effects"""
        while self.animation_running:
            self.animation_frame += 1
            if self._tqdm:
                # Update the animation frame in the tqdm instance
                self._tqdm.animation_frame = self.animation_frame
                self._tqdm.refresh()
            time.sleep(0.1)
    
    def __iter__(self):
        """Make SmartTQDM iterable"""
        if self._tqdm:
            self.start_animation()
            try:
                for item in self._tqdm:
                    yield item
            finally:
                self.stop_animation()
        else:
            yield from self.iterable
    
    def __enter__(self):
        """Context manager entry"""
        if self._tqdm:
            self.start_animation()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        self.stop_animation()
        if self._tqdm:
            self._tqdm.close()
    
    def update(self, n=1):
        """Update progress by n steps"""
        if self._tqdm:
            self._tqdm.update(n)
    
    def close(self):
        """Close the progress bar"""
        self.stop_animation()
        if self._tqdm:
            self._tqdm.close()
    
    def set_description(self, desc):
        """Set the description"""
        if self._tqdm:
            self._tqdm.set_description(desc)
    
    def set_postfix(self, **kwargs):
        """Set postfix with metrics"""
        self.update_metrics(kwargs)
    
    def reset(self, total=None):
        """Reset the progress bar"""
        if self._tqdm:
            self._tqdm.reset(total)
        self.metrics_tracker.reset()
        self.current_metrics.clear()
    
    def get_metrics_history(self) -> Dict[str, List[float]]:
        """Get the history of all tracked metrics"""
        return self.metrics_tracker.history
    
    def export_gif(self, filename: str, duration: float = 2.0):
        """Export animated progress bar as GIF"""
        from .exporters import GIFExporter
        exporter = GIFExporter()
        exporter.export(self, filename, duration)


def smart_tqdm(*args, **kwargs):
    """
    Convenience function for creating SmartTQDM instances
    
    Usage:
        for epoch in smart_tqdm(range(epochs), metrics=metrics_dict):
            # training code
            pass
    """
    return SmartTQDM(*args, **kwargs)


# Context manager for easy usage
@contextmanager
def smart_progress(iterable, **kwargs):
    """
    Context manager for smart progress tracking
    
    Usage:
        with smart_progress(range(epochs), metrics=metrics_dict) as pbar:
            for epoch in pbar:
                # training code
                pbar.set_postfix(loss=loss, accuracy=acc)
    """
    pbar = SmartTQDM(iterable, **kwargs)
    try:
        yield pbar
    finally:
        pbar.close() 