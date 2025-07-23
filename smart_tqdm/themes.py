"""
Theme system for SmartTQDM with emoji-based feedback
"""

from typing import Dict, Any, Optional
from enum import Enum
import random


class PerformanceStatus(Enum):
    """Performance status for emoji selection"""
    IMPROVING = "improving"
    PLATEAU = "plateau"
    UNSTABLE = "unstable"
    NEW_BEST = "new_best"
    SLOW = "slow"
    EXCELLENT = "excellent"
    WARNING = "warning"
    MILESTONE = "milestone"


class Theme:
    """Base theme class for emoji-based feedback"""
    
    def __init__(self):
        self.performance_emojis = {
            PerformanceStatus.IMPROVING: "🔥",
            PerformanceStatus.PLATEAU: "🐢",
            PerformanceStatus.UNSTABLE: "😅",
            PerformanceStatus.NEW_BEST: "🥳",
            PerformanceStatus.SLOW: "🐌",
            PerformanceStatus.EXCELLENT: "⭐",
            PerformanceStatus.WARNING: "⚠️",
            PerformanceStatus.MILESTONE: "🎯"
        }
        
        self.milestone_emojis = {
            0.25: "🎯",
            0.5: "🎯",
            0.75: "🎯",
            0.9: "🎯"
        }
    
    def get_emoji(self, status: PerformanceStatus) -> str:
        """Get emoji for performance status"""
        return self.performance_emojis.get(status, "📊")
    
    def get_milestone_emoji(self, progress: float) -> str:
        """Get emoji for milestone progress"""
        # Find closest milestone
        milestones = [0.25, 0.5, 0.75, 0.9]
        closest = min(milestones, key=lambda x: abs(x - progress))
        return self.milestone_emojis.get(closest, "🎯")
    
    def get_random_emoji(self) -> str:
        """Get a random emoji from the theme"""
        return random.choice(list(self.performance_emojis.values()))


class DefaultTheme(Theme):
    """Default theme with standard emojis"""
    
    def __init__(self):
        super().__init__()
        self.performance_emojis = {
            PerformanceStatus.IMPROVING: "🔥",
            PerformanceStatus.PLATEAU: "🐢",
            PerformanceStatus.UNSTABLE: "😅",
            PerformanceStatus.NEW_BEST: "🥳",
            PerformanceStatus.SLOW: "🐌",
            PerformanceStatus.EXCELLENT: "⭐",
            PerformanceStatus.WARNING: "⚠️",
            PerformanceStatus.MILESTONE: "🎯"
        }
        
        self.milestone_emojis = {
            0.25: "🎯",
            0.5: "🎯",
            0.75: "🎯",
            0.9: "🎯"
        }


class CatTheme(Theme):
    """Cat-themed emojis for feline lovers"""
    
    def __init__(self):
        super().__init__()
        self.performance_emojis = {
            PerformanceStatus.IMPROVING: "😸",
            PerformanceStatus.PLATEAU: "😺",
            PerformanceStatus.UNSTABLE: "😿",
            PerformanceStatus.NEW_BEST: "😻",
            PerformanceStatus.SLOW: "😹",
            PerformanceStatus.EXCELLENT: "😽",
            PerformanceStatus.WARNING: "🙀",
            PerformanceStatus.MILESTONE: "🐱"
        }
        
        self.milestone_emojis = {
            0.25: "🐱",
            0.5: "🐱",
            0.75: "🐱",
            0.9: "🐱"
        }


class RocketTheme(Theme):
    """Rocket-themed emojis for space enthusiasts"""
    
    def __init__(self):
        super().__init__()
        self.performance_emojis = {
            PerformanceStatus.IMPROVING: "🚀",
            PerformanceStatus.PLATEAU: "🛸",
            PerformanceStatus.UNSTABLE: "💫",
            PerformanceStatus.NEW_BEST: "⭐",
            PerformanceStatus.SLOW: "🌙",
            PerformanceStatus.EXCELLENT: "🌟",
            PerformanceStatus.WARNING: "☄️",
            PerformanceStatus.MILESTONE: "🎯"
        }
        
        self.milestone_emojis = {
            0.25: "🛰️",
            0.5: "🛰️",
            0.75: "🛰️",
            0.9: "🛰️"
        }


class GamingTheme(Theme):
    """Gaming-themed emojis for gamers"""
    
    def __init__(self):
        super().__init__()
        self.performance_emojis = {
            PerformanceStatus.IMPROVING: "🎮",
            PerformanceStatus.PLATEAU: "🎲",
            PerformanceStatus.UNSTABLE: "🎯",
            PerformanceStatus.NEW_BEST: "🏆",
            PerformanceStatus.SLOW: "⏰",
            PerformanceStatus.EXCELLENT: "💎",
            PerformanceStatus.WARNING: "⚠️",
            PerformanceStatus.MILESTONE: "🎯"
        }
        
        self.milestone_emojis = {
            0.25: "🎯",
            0.5: "🎯",
            0.75: "🎯",
            0.9: "🎯"
        }


class NatureTheme(Theme):
    """Nature-themed emojis for environmentalists"""
    
    def __init__(self):
        super().__init__()
        self.performance_emojis = {
            PerformanceStatus.IMPROVING: "🌱",
            PerformanceStatus.PLATEAU: "🌿",
            PerformanceStatus.UNSTABLE: "🍃",
            PerformanceStatus.NEW_BEST: "🌸",
            PerformanceStatus.SLOW: "🌲",
            PerformanceStatus.EXCELLENT: "🌺",
            PerformanceStatus.WARNING: "🍂",
            PerformanceStatus.MILESTONE: "🌳"
        }
        
        self.milestone_emojis = {
            0.25: "🌳",
            0.5: "🌳",
            0.75: "🌳",
            0.9: "🌳"
        }


class CustomTheme(Theme):
    """Custom theme with user-defined emoji mappings"""
    
    def __init__(self, emoji_mapping: Dict[PerformanceStatus, str], milestone_mapping: Dict[float, str] = None):
        super().__init__()
        self.performance_emojis = emoji_mapping
        
        if milestone_mapping:
            self.milestone_emojis = milestone_mapping
        else:
            # Default milestone emojis
            self.milestone_emojis = {
                0.25: "🎯",
                0.5: "🎯",
                0.75: "🎯",
                0.9: "🎯"
            }


class AnimatedTheme(Theme):
    """Theme with animated emojis that cycle through variations"""
    
    def __init__(self, base_theme: Theme = None):
        super().__init__()
        self.base_theme = base_theme or DefaultTheme()
        self.animation_frame = 0
        
        # Animated emoji variations
        self.animated_emojis = {
            PerformanceStatus.IMPROVING: ["🔥", "🔥", "🔥", "🔥"],
            PerformanceStatus.PLATEAU: ["🐢", "🐢", "🐢", "🐢"],
            PerformanceStatus.UNSTABLE: ["😅", "😅", "😅", "😅"],
            PerformanceStatus.NEW_BEST: ["🥳", "🥳", "🥳", "🥳"],
            PerformanceStatus.SLOW: ["🐌", "🐌", "🐌", "🐌"],
            PerformanceStatus.EXCELLENT: ["⭐", "⭐", "⭐", "⭐"],
            PerformanceStatus.WARNING: ["⚠️", "⚠️", "⚠️", "⚠️"],
            PerformanceStatus.MILESTONE: ["🎯", "🎯", "🎯", "🎯"]
        }
    
    def get_emoji(self, status: PerformanceStatus) -> str:
        """Get animated emoji for performance status"""
        emojis = self.animated_emojis.get(status, ["📊"])
        return emojis[self.animation_frame % len(emojis)]
    
    def update_animation(self):
        """Update animation frame"""
        self.animation_frame += 1


# Theme factory for easy theme selection
class ThemeFactory:
    """Factory for creating themes"""
    
    @staticmethod
    def create_theme(theme_name: str, **kwargs) -> Theme:
        """Create a theme by name"""
        themes = {
            "default": DefaultTheme,
            "cat": CatTheme,
            "rocket": RocketTheme,
            "gaming": GamingTheme,
            "nature": NatureTheme,
            "animated": AnimatedTheme,
            "custom": CustomTheme
        }
        
        theme_class = themes.get(theme_name.lower(), DefaultTheme)
        return theme_class(**kwargs)
    
    @staticmethod
    def list_themes() -> list:
        """List all available themes"""
        return ["default", "cat", "rocket", "gaming", "nature", "animated", "custom"] 