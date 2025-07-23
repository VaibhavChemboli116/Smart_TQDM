"""
Smart TQDM - Intelligent Progress Bar with Emoji Feedback and Fluid Visualization

A drop-in replacement for tqdm with smart features:
- Emoji-based performance feedback
- Fluid progress bar visualization
- Smart metrics awareness
- Custom themes and animations
- Jupyter notebook support
- GIF export capabilities

Author: IEEE Research Project
Version: 1.0.0
"""

from .smart_tqdm import SmartTQDM, smart_tqdm, smart_progress
from .themes import Theme, DefaultTheme, CatTheme, RocketTheme, CustomTheme
from .animations import FluidAnimation, WaveAnimation, RippleAnimation
from .metrics import MetricsTracker, PerformanceAnalyzer
from .exporters import GIFExporter, ReportGenerator

__version__ = "1.0.0"
__author__ = "IEEE Research Project"

__all__ = [
    "SmartTQDM",
    "smart_tqdm",
    "smart_progress", 
    "Theme",
    "DefaultTheme",
    "CatTheme", 
    "RocketTheme",
    "CustomTheme",
    "FluidAnimation",
    "WaveAnimation",
    "RippleAnimation",
    "MetricsTracker",
    "PerformanceAnalyzer",
    "GIFExporter",
    "ReportGenerator"
] 