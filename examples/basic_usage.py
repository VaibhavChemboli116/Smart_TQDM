#!/usr/bin/env python3
"""
Basic usage example for SmartTQDM
Demonstrates core features: emoji feedback, fluid animation, and smart metrics
"""

import time
import random
import numpy as np
from smart_tqdm import smart_tqdm, smart_progress

def simulate_training():
    """Simulate a training process with varying performance"""
    epochs = 100
    
    # Initialize metrics with some realistic patterns
    base_loss = 2.0
    base_accuracy = 0.3
    
    print("🚀 Starting SmartTQDM Demo")
    print("=" * 50)
    
    # Basic usage - drop-in replacement for tqdm
    for epoch in smart_tqdm(range(epochs), desc="Training Model"):
        # Simulate realistic training patterns
        if epoch < 20:
            # Initial rapid improvement
            loss = base_loss * np.exp(-epoch * 0.1) + random.uniform(-0.1, 0.1)
            accuracy = base_accuracy + (0.6 - base_accuracy) * (epoch / 20) + random.uniform(-0.05, 0.05)
        elif epoch < 60:
            # Plateau phase
            loss = 0.3 + random.uniform(-0.05, 0.05)
            accuracy = 0.85 + random.uniform(-0.02, 0.02)
        elif epoch < 80:
            # Another improvement phase
            loss = 0.3 - (epoch - 60) * 0.005 + random.uniform(-0.02, 0.02)
            accuracy = 0.85 + (epoch - 60) * 0.002 + random.uniform(-0.01, 0.01)
        else:
            # Final convergence
            loss = 0.2 + random.uniform(-0.01, 0.01)
            accuracy = 0.92 + random.uniform(-0.005, 0.005)
        
        # Update progress bar with metrics
        # SmartTQDM will automatically show appropriate emojis based on performance
        pbar.set_postfix(loss=f"{loss:.4f}", accuracy=f"{accuracy:.4f}")
        
        # Simulate training time
        time.sleep(0.05)
    
    print("\n✅ Training completed!")

def demonstrate_themes():
    """Demonstrate different themes"""
    print("\n🎨 Theme Demonstrations")
    print("=" * 50)
    
    from smart_tqdm import CatTheme, RocketTheme, GamingTheme, NatureTheme
    
    themes = [
        ("Default", None),
        ("Cat", CatTheme()),
        ("Rocket", RocketTheme()),
        ("Gaming", GamingTheme()),
        ("Nature", NatureTheme())
    ]
    
    for theme_name, theme in themes:
        print(f"\n{theme_name} Theme:")
        for i in smart_tqdm(range(20), desc=f"{theme_name} Demo", theme=theme):
            loss = random.uniform(0.1, 1.0)
            accuracy = random.uniform(0.5, 0.9)
            pbar.set_postfix(loss=f"{loss:.3f}", accuracy=f"{accuracy:.3f}")
            time.sleep(0.1)

def demonstrate_animations():
    """Demonstrate different animations"""
    print("\n🌊 Animation Demonstrations")
    print("=" * 50)
    
    from smart_tqdm import WaveAnimation, RippleAnimation, PulseAnimation, ParticleAnimation
    
    animations = [
        ("Wave", WaveAnimation(wave_speed=2.0)),
        ("Ripple", RippleAnimation(ripple_speed=1.5)),
        ("Pulse", PulseAnimation(pulse_speed=3.0)),
        ("Particle", ParticleAnimation(particle_count=5))
    ]
    
    for anim_name, animation in animations:
        print(f"\n{anim_name} Animation:")
        for i in smart_tqdm(range(30), desc=f"{anim_name} Demo", animation=animation):
            loss = random.uniform(0.1, 1.0)
            accuracy = random.uniform(0.5, 0.9)
            pbar.set_postfix(loss=f"{loss:.3f}", accuracy=f"{accuracy:.3f}")
            time.sleep(0.1)

def demonstrate_context_manager():
    """Demonstrate context manager usage"""
    print("\n🔧 Context Manager Demo")
    print("=" * 50)
    
    from smart_tqdm import CatTheme, WaveAnimation
    
    with smart_progress(
        range(25), 
        desc="Context Manager Demo",
        theme=CatTheme(),
        animation=WaveAnimation()
    ) as pbar:
        for epoch in pbar:
            loss = random.uniform(0.1, 1.0)
            accuracy = random.uniform(0.5, 0.9)
            pbar.set_postfix(loss=f"{loss:.3f}", accuracy=f"{accuracy:.3f}")
            time.sleep(0.1)

def demonstrate_metrics_analysis():
    """Demonstrate smart metrics analysis"""
    print("\n📊 Smart Metrics Analysis Demo")
    print("=" * 50)
    
    from smart_tqdm import SmartMetrics, PerformanceStatus
    
    # Create smart metrics tracker
    smart_metrics = SmartMetrics()
    
    # Add alert callback
    def performance_alert(status, metrics):
        if status == PerformanceStatus.WARNING:
            print(f"\n⚠️  Performance warning detected: {metrics}")
        elif status == PerformanceStatus.NEW_BEST:
            print(f"\n🥳 New best performance: {metrics}")
    
    smart_metrics.add_alert_callback(performance_alert)
    
    # Simulate training with smart analysis
    for epoch in smart_tqdm(range(50), desc="Smart Analysis"):
        # Simulate different performance phases
        if epoch < 15:
            loss = 2.0 - epoch * 0.1 + random.uniform(-0.05, 0.05)
            accuracy = 0.3 + epoch * 0.03 + random.uniform(-0.02, 0.02)
        elif epoch < 30:
            loss = 0.5 + random.uniform(-0.1, 0.1)
            accuracy = 0.75 + random.uniform(-0.05, 0.05)
        else:
            loss = 0.3 - (epoch - 30) * 0.005 + random.uniform(-0.02, 0.02)
            accuracy = 0.85 + (epoch - 30) * 0.003 + random.uniform(-0.01, 0.01)
        
        # Update smart metrics
        status = smart_metrics.update(
            {"loss": loss, "accuracy": accuracy},
            progress=epoch/50
        )
        
        pbar.set_postfix(loss=f"{loss:.4f}", accuracy=f"{accuracy:.4f}")
        time.sleep(0.1)
    
    # Generate performance report
    report = smart_metrics.get_performance_report()
    print(f"\n📈 Performance Summary:")
    for metric, stats in report['summary'].items():
        print(f"  {metric}:")
        print(f"    Current: {stats['current']:.4f}")
        print(f"    Trend: {stats['trend']:.4f}")
        print(f"    Volatility: {stats['volatility']:.4f}")
    
    print(f"\n🎯 Recommendations:")
    for rec in report['recommendations']:
        print(f"  {rec}")

if __name__ == "__main__":
    print("SmartTQDM Basic Usage Examples")
    print("=" * 60)
    
    # Run demonstrations
    simulate_training()
    demonstrate_themes()
    demonstrate_animations()
    demonstrate_context_manager()
    demonstrate_metrics_analysis()
    
    print("\n🎉 All demonstrations completed!")
    print("Check out the examples directory for more advanced usage.") 