"""
Terminal display and rendering functionality for SmartBar
"""
import sys
import shutil
import time
from typing import Dict, Any, Optional


class TerminalRenderer:
    """Handles terminal rendering and display formatting"""
    
    # Display constants
    SLIM_CHAR = '━'  # Changed from '─' to '━' for thicker bar
    MIN_BAR_WIDTH = 10
    MIN_TERM_WIDTH = 40
    
    def __init__(self):
        self.last_print_len = 0
        self.warned_narrow = False
    
    def get_terminal_width(self) -> int:
        """Get current terminal width"""
        try:
            return shutil.get_terminal_size().columns
        except Exception:
            return 80
    
    def create_color_gradient_bar(self, filled_width: int) -> str:
        """Create a color gradient filled bar segment"""
        if filled_width <= 0:
            return ""
        
        colored_filled = ""
        for i in range(filled_width):
            # Calculate gradient position (0=start, 1=end)
            pos = i / max(1, filled_width - 1)
            # Interpolate colors: red (0) -> yellow (0.5) -> green (1)
            if pos <= 0.5:
                # Red to yellow
                ratio = pos * 2
                r = 255
                g = int(255 * ratio)
                b = 0
            else:
                # Yellow to green
                ratio = (pos - 0.5) * 2
                r = int(255 * (1 - ratio))
                g = 255
                b = 0
            colored_filled += f"\033[38;2;{r};{g};{b}m{self.SLIM_CHAR}\033[0m"
        
        return colored_filled
    
    def calculate_layout(self, desc: str, emoji: str, metrics: Dict[str, Any], 
                        n: int, total: int, start_time: float, 
                        show_emoji: bool, show_metrics: bool) -> Dict[str, Any]:
        """Calculate layout dimensions and components"""
        term_width = self.get_terminal_width()
        
        # Calculate space needed for other elements
        desc_len = len(desc) if desc else 0
        emoji_len = len(emoji) if show_emoji and emoji else 0
        
        # Format metrics string
        metrics_str = ""
        if show_metrics and metrics:
            metrics_str = " [" + " ".join([f"{k}:{v}" for k, v in metrics.items()]) + "]"
        metrics_len = len(metrics_str)
        
        # Calculate progress info
        progress_str = f" {n}/{total} {((n / total) * 100):.1f}%"
        elapsed = time.time() - start_time
        time_str = f" [ {elapsed:.1f}s]"
        
        # Calculate total space needed
        total_needed = (desc_len + emoji_len + 2 +  # desc + emoji + spaces
                       2 + 2 +  # bar brackets
                       len(progress_str) + len(time_str) + metrics_len + 10)  # progress + time + metrics + padding
        
        # Calculate available bar width
        available_width = term_width - total_needed
        if available_width < self.MIN_BAR_WIDTH:
            if not self.warned_narrow:
                print(f"\n⚠️  Terminal too narrow ({term_width} chars). Bar will be minimal.")
                self.warned_narrow = True
            available_width = self.MIN_BAR_WIDTH
        
        # Truncate description if needed
        desc_display = desc
        if desc_len > 20:
            desc_display = desc[:17] + "..."
        
        return {
            'term_width': term_width,
            'available_width': available_width,
            'desc_display': desc_display,
            'metrics_str': metrics_str,
            'progress_str': progress_str,
            'time_str': time_str
        }
    
    def render_progress_bar(self, n: int, total: int, desc: str, emoji: str, 
                           metrics: Dict[str, Any], start_time: float,
                           show_emoji: bool = True, show_metrics: bool = True) -> str:
        """Render the complete progress bar string"""
        layout = self.calculate_layout(desc, emoji, metrics, n, total, start_time, 
                                     show_emoji, show_metrics)
        
        # Build the bar
        filled_width = int((n / total) * layout['available_width'])
        empty_width = layout['available_width'] - filled_width
        
        filled_part = self.create_color_gradient_bar(filled_width)
        empty_part = " " * empty_width
        
        # Build the complete bar string with emoji as slider head
        bar_str = f"{layout['desc_display']}"
        if show_emoji and emoji:
            bar_str += f" ┃{filled_part}"
            
            # Position the emoji at the current progress point
            if filled_width < layout['available_width']:
                bar_str += f"{emoji}{empty_part}"
            else:
                # If bar is full, emoji goes at the end
                bar_str += f"{emoji}"
        else:
            bar_str += f" ┃{filled_part}{empty_part}"
            
        bar_str += f"┃{layout['progress_str']}{layout['time_str']}{layout['metrics_str']}"
        
        return bar_str
    
    def print_bar(self, bar_str: str) -> None:
        """Print the progress bar with terminal handling"""
        try:
            # Use carriage return to go to beginning of line
            sys.stdout.write('\r')
            # Clear the line
            sys.stdout.write('\033[K')
            # Write the new bar
            sys.stdout.write(bar_str)
            sys.stdout.flush()
            self.last_print_len = len(bar_str)
        except Exception:
            # Fallback for terminals that don't support ANSI escape codes
            sys.stdout.write('\r' + ' ' * self.last_print_len + '\r')
            sys.stdout.write(bar_str)
            sys.stdout.flush()
            self.last_print_len = len(bar_str)
    
    def finish(self) -> None:
        """Print final newline when progress is complete"""
        print()  # Ensure new line at end