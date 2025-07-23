"""
Fluid animation system for SmartTQDM progress bars
"""

import math
import time
from typing import List, Optional
import random


class FluidAnimation:
    """Base class for fluid progress bar animations"""
    
    def __init__(self, width: int = 50, characters: List[str] = None):
        self.width = width
        self.characters = characters or ["░", "▒", "▓", "█"]
        self.frame = 0
    
    def get_bar(self, progress: float, frame: int = 0) -> str:
        """Generate fluid progress bar"""
        self.frame = frame
        filled_width = int(progress * self.width)
        empty_width = self.width - filled_width
        
        filled_part = self._get_filled_part(filled_width)
        empty_part = self._get_empty_part(empty_width)
        
        return filled_part + empty_part
    
    def _get_filled_part(self, width: int) -> str:
        """Get the filled part of the progress bar"""
        return "█" * width
    
    def _get_empty_part(self, width: int) -> str:
        """Get the empty part of the progress bar"""
        return "░" * width


class WaveAnimation(FluidAnimation):
    """Fluid water-like wave animation with blue color"""
    
    def __init__(self, width: int = 50, wave_speed: float = 2.0):
        super().__init__(width)
        self.wave_speed = wave_speed
        # Blue water-like characters for filled part
        self.water_chars = ["░", "▒", "▓", "█"]
        # Enhanced ANSI color codes for beautiful blue water effect
        self.blue_water = [
            "\033[44m \033[0m",   # Blue background space (water droplet)
            "\033[46m░\033[0m",   # Cyan background with light char
            "\033[96m▒\033[0m",   # Bright cyan text
            "\033[94m▓\033[0m",   # Blue text
            "\033[104m█\033[0m",  # Bright blue background
            "\033[36m█\033[0m"    # Cyan text
        ]
        self.empty_char = " "
    
    def get_bar(self, progress: float, frame: int = 0) -> str:
        """Generate beautiful flowing blue water progress bar"""
        self.frame = frame
        bar_width = self.width
        filled_width = int(progress * bar_width)
        
        # Create the flowing water effect
        result = []
        
        for i in range(bar_width):
            if i < filled_width:
                # Filled part with flowing blue water
                wave1 = math.sin((i + self.frame * self.wave_speed) * 0.5) * 0.5 + 0.5
                wave2 = math.sin((i * 0.3 + self.frame * self.wave_speed * 0.7)) * 0.3
                turbulence = math.sin((i * 1.2 + self.frame * self.wave_speed * 0.4)) * 0.2
                
                # Combine waves for realistic water movement
                final_intensity = max(0, min(1, wave1 + wave2 + turbulence))
                
                # Map intensity to blue water characters
                char_index = int(final_intensity * (len(self.blue_water) - 1))
                result.append(self.blue_water[char_index])
                
            else:
                # Empty part with subtle flow hints
                wave = math.sin((i + self.frame * self.wave_speed * 0.1) * 0.2) * 0.1 + 0.9
                if wave > 0.98:
                    result.append("\033[100m \033[0m")  # Dark gray hint of water
                else:
                    result.append(" ")
        
        return "".join(result)
    
    def _get_filled_part(self, width: int) -> str:
        """Generate fluid water-like filled part"""
        # This method is now handled by get_bar() for better integration
        return "█" * width
    
    def _get_empty_part(self, width: int) -> str:
        """Generate empty part with subtle flow effect"""
        # This method is now handled by get_bar() for better integration  
        return " " * width


class RippleAnimation(FluidAnimation):
    """Ripple effect animation"""
    
    def __init__(self, width: int = 50, ripple_speed: float = 1.5):
        super().__init__(width)
        self.ripple_speed = ripple_speed
        self.characters = ["░", "▒", "▓", "█"]
    
    def _get_filled_part(self, width: int) -> str:
        """Generate ripple-filled part"""
        if width == 0:
            return ""
        
        result = []
        for i in range(width):
            # Create ripple effect from center
            center = width / 2
            distance = abs(i - center)
            ripple = math.sin((distance - self.frame * self.ripple_speed) * 0.5) * 0.5 + 0.5
            char_index = int(ripple * (len(self.characters) - 1))
            result.append(self.characters[char_index])
        
        return "".join(result)


class PulseAnimation(FluidAnimation):
    """Pulsing animation effect"""
    
    def __init__(self, width: int = 50, pulse_speed: float = 3.0):
        super().__init__(width)
        self.pulse_speed = pulse_speed
        self.characters = ["░", "▒", "▓", "█"]
    
    def _get_filled_part(self, width: int) -> str:
        """Generate pulsing filled part"""
        if width == 0:
            return ""
        
        # Global pulse effect
        pulse = math.sin(self.frame * self.pulse_speed * 0.1) * 0.3 + 0.7
        
        result = []
        for i in range(width):
            # Combine global pulse with local variation
            local_var = math.sin(i * 0.2) * 0.2 + 0.8
            intensity = pulse * local_var
            char_index = int(intensity * (len(self.characters) - 1))
            result.append(self.characters[char_index])
        
        return "".join(result)


class GradientAnimation(FluidAnimation):
    """Gradient-based animation"""
    
    def __init__(self, width: int = 50, gradient_speed: float = 1.0):
        super().__init__(width)
        self.gradient_speed = gradient_speed
        self.characters = ["░", "▒", "▓", "█"]
    
    def _get_filled_part(self, width: int) -> str:
        """Generate gradient-filled part"""
        if width == 0:
            return ""
        
        result = []
        for i in range(width):
            # Create moving gradient
            gradient_pos = (i + self.frame * self.gradient_speed) / width
            gradient_pos = gradient_pos % 1.0
            char_index = int(gradient_pos * (len(self.characters) - 1))
            result.append(self.characters[char_index])
        
        return "".join(result)


class ParticleAnimation(FluidAnimation):
    """Particle-based animation with floating elements"""
    
    def __init__(self, width: int = 50, particle_count: int = 5):
        super().__init__(width)
        self.particle_count = particle_count
        self.characters = ["░", "▒", "▓", "█", "●", "○", "◐", "◑"]
        self.particles = self._init_particles()
    
    def _init_particles(self) -> List[dict]:
        """Initialize particle positions and velocities"""
        particles = []
        for _ in range(self.particle_count):
            particles.append({
                'x': random.uniform(0, self.width),
                'vx': random.uniform(-0.5, 0.5),
                'life': random.uniform(0, 1)
            })
        return particles
    
    def _update_particles(self):
        """Update particle positions and life"""
        for particle in self.particles:
            particle['x'] += particle['vx']
            particle['life'] += 0.02
            
            # Wrap around edges
            if particle['x'] < 0:
                particle['x'] = self.width
            elif particle['x'] > self.width:
                particle['x'] = 0
            
            # Reset particle when life expires
            if particle['life'] > 1:
                particle['x'] = random.uniform(0, self.width)
                particle['vx'] = random.uniform(-0.5, 0.5)
                particle['life'] = 0
    
    def _get_filled_part(self, width: int) -> str:
        """Generate particle-filled part"""
        self._update_particles()
        
        if width == 0:
            return ""
        
        result = ["░"] * width
        
        # Add particles
        for particle in self.particles:
            if particle['x'] < width:
                x = int(particle['x'])
                if 0 <= x < width:
                    # Use particle life to determine character
                    char_index = int(particle['life'] * (len(self.characters) - 1))
                    result[x] = self.characters[char_index]
        
        return "".join(result)


class MatrixAnimation(FluidAnimation):
    """Matrix-style digital rain animation"""
    
    def __init__(self, width: int = 50, rain_speed: float = 2.0):
        super().__init__(width)
        self.rain_speed = rain_speed
        self.characters = ["░", "▒", "▓", "█", "▌", "▐", "▄", "▀"]
        self.drops = self._init_drops()
    
    def _init_drops(self) -> List[dict]:
        """Initialize digital rain drops"""
        drops = []
        for i in range(self.width):
            drops.append({
                'y': random.uniform(-10, 0),
                'speed': random.uniform(0.5, 2.0),
                'length': random.randint(3, 8)
            })
        return drops
    
    def _update_drops(self):
        """Update drop positions"""
        for drop in self.drops:
            drop['y'] += drop['speed']
            if drop['y'] > self.width + 10:
                drop['y'] = random.uniform(-10, 0)
    
    def _get_filled_part(self, width: int) -> str:
        """Generate matrix-style filled part"""
        self._update_drops()
        
        if width == 0:
            return ""
        
        result = ["░"] * width
        
        # Add digital rain
        for i, drop in enumerate(self.drops):
            if i >= width:
                break
            
            y = int(drop['y'])
            if 0 <= y < width:
                # Create trail effect
                for j in range(min(int(drop['length']), width - y)):
                    if y + j < width:
                        intensity = 1.0 - (j / drop['length'])
                        char_index = int(intensity * (len(self.characters) - 1))
                        result[y + j] = self.characters[char_index]
        
        return "".join(result)


class RainbowAnimation(FluidAnimation):
    """Rainbow color cycling animation (for terminals that support color)"""
    
    def __init__(self, width: int = 50, cycle_speed: float = 1.0):
        super().__init__(width)
        self.cycle_speed = cycle_speed
        self.characters = ["█"]
        self.colors = [
            "\033[91m",  # Red
            "\033[93m",  # Yellow
            "\033[92m",  # Green
            "\033[96m",  # Cyan
            "\033[94m",  # Blue
            "\033[95m",  # Magenta
        ]
        self.reset_color = "\033[0m"
    
    def _get_filled_part(self, width: int) -> str:
        """Generate rainbow-filled part"""
        if width == 0:
            return ""
        
        result = []
        for i in range(width):
            color_index = int((i + self.frame * self.cycle_speed) % len(self.colors))
            color = self.colors[color_index]
            result.append(f"{color}█{self.reset_color}")
        
        return "".join(result)


# Animation factory for easy selection
class AnimationFactory:
    """Factory for creating animations"""
    
    @staticmethod
    def create_animation(animation_name: str, **kwargs) -> FluidAnimation:
        """Create an animation by name"""
        animations = {
            "fluid": FluidAnimation,
            "wave": WaveAnimation,
            "ripple": RippleAnimation,
            "pulse": PulseAnimation,
            "gradient": GradientAnimation,
            "particle": ParticleAnimation,
            "matrix": MatrixAnimation,
            "rainbow": RainbowAnimation
        }
        
        animation_class = animations.get(animation_name.lower(), WaveAnimation)
        return animation_class(**kwargs)
    
    @staticmethod
    def list_animations() -> list:
        """List all available animations"""
        return ["fluid", "wave", "ripple", "pulse", "gradient", "particle", "matrix", "rainbow"] 