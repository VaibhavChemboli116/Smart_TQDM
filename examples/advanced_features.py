#!/usr/bin/env python3
"""
Advanced features example for SmartTQDM
Demonstrates GIF export, custom themes, comprehensive reporting, and more
"""

import time
import random
import numpy as np
import os
from smart_tqdm import (
    smart_tqdm, 
    CustomTheme, 
    PerformanceStatus,
    GIFExporter,
    ReportGenerator,
    SmartMetrics,
    WaveAnimation,
    ParticleAnimation
)

def create_custom_theme():
    """Create a custom theme with unique emojis"""
    print("🎨 Creating Custom Theme")
    print("=" * 40)
    
    # Define custom emoji mappings for a "space" theme
    space_emojis = {
        PerformanceStatus.IMPROVING: "🚀",
        PerformanceStatus.PLATEAU: "🛸",
        PerformanceStatus.UNSTABLE: "💫",
        PerformanceStatus.NEW_BEST: "⭐",
        PerformanceStatus.SLOW: "🌙",
        PerformanceStatus.EXCELLENT: "🌟",
        PerformanceStatus.WARNING: "☄️",
        PerformanceStatus.MILESTONE: "🛰️"
    }
    
    # Custom milestone emojis
    milestone_emojis = {
        0.25: "🛰️",
        0.5: "🛰️",
        0.75: "🛰️",
        0.9: "🛰️"
    }
    
    return CustomTheme(space_emojis, milestone_emojis)

def demonstrate_gif_export():
    """Demonstrate GIF export functionality"""
    print("\n🎬 GIF Export Demonstration")
    print("=" * 40)
    
    # Create GIF exporter
    gif_exporter = GIFExporter(fps=15, dpi=150)
    
    # Create output directory
    os.makedirs("exports", exist_ok=True)
    
    # Simulate training with frame capture
    for epoch in smart_tqdm(
        range(50), 
        desc="Training for GIF",
        theme=create_custom_theme(),
        animation=WaveAnimation(wave_speed=2.5)
    ):
        # Simulate realistic training metrics
        if epoch < 20:
            loss = 2.0 - epoch * 0.08 + random.uniform(-0.05, 0.05)
            accuracy = 0.3 + epoch * 0.025 + random.uniform(-0.02, 0.02)
        elif epoch < 35:
            loss = 0.4 + random.uniform(-0.03, 0.03)
            accuracy = 0.8 + random.uniform(-0.015, 0.015)
        else:
            loss = 0.3 - (epoch - 35) * 0.003 + random.uniform(-0.01, 0.01)
            accuracy = 0.85 + (epoch - 35) * 0.002 + random.uniform(-0.005, 0.005)
        
        # Capture frame for GIF
        gif_exporter.capture_frame(pbar, {"loss": loss, "accuracy": accuracy})
        
        pbar.set_postfix(loss=f"{loss:.4f}", accuracy=f"{accuracy:.4f}")
        time.sleep(0.1)
    
    # Export GIF
    gif_path = "exports/training_animation.gif"
    gif_exporter.export(pbar, gif_path, duration=4.0)
    print(f"✅ GIF exported to: {gif_path}")

def demonstrate_comprehensive_reporting():
    """Demonstrate comprehensive reporting features"""
    print("\n📊 Comprehensive Reporting Demo")
    print("=" * 40)
    
    # Create report generator
    report_gen = ReportGenerator(output_dir="reports")
    
    # Create smart metrics for detailed analysis
    smart_metrics = SmartMetrics()
    
    # Simulate complex training with multiple metrics
    metrics_data = {
        'train_loss': [],
        'val_loss': [],
        'train_acc': [],
        'val_acc': [],
        'learning_rate': []
    }
    
    for epoch in smart_tqdm(range(80), desc="Training for Report"):
        # Simulate realistic training patterns
        if epoch < 25:
            # Initial training phase
            train_loss = 2.0 - epoch * 0.06 + random.uniform(-0.03, 0.03)
            val_loss = train_loss + 0.2 + random.uniform(-0.05, 0.05)
            train_acc = 0.3 + epoch * 0.02 + random.uniform(-0.01, 0.01)
            val_acc = train_acc - 0.1 + random.uniform(-0.02, 0.02)
            lr = 0.001
        elif epoch < 50:
            # Plateau phase
            train_loss = 0.4 + random.uniform(-0.02, 0.02)
            val_loss = 0.6 + random.uniform(-0.03, 0.03)
            train_acc = 0.85 + random.uniform(-0.01, 0.01)
            val_acc = 0.8 + random.uniform(-0.015, 0.015)
            lr = 0.0005
        else:
            # Fine-tuning phase
            train_loss = 0.3 - (epoch - 50) * 0.002 + random.uniform(-0.01, 0.01)
            val_loss = 0.5 - (epoch - 50) * 0.003 + random.uniform(-0.015, 0.015)
            train_acc = 0.9 + (epoch - 50) * 0.001 + random.uniform(-0.005, 0.005)
            val_acc = 0.85 + (epoch - 50) * 0.0015 + random.uniform(-0.008, 0.008)
            lr = 0.0001
        
        # Store metrics
        metrics_data['train_loss'].append(train_loss)
        metrics_data['val_loss'].append(val_loss)
        metrics_data['train_acc'].append(train_acc)
        metrics_data['val_acc'].append(val_acc)
        metrics_data['learning_rate'].append(lr)
        
        # Update smart metrics
        current_metrics = {
            'train_loss': train_loss,
            'val_loss': val_loss,
            'train_acc': train_acc,
            'val_acc': val_acc,
            'lr': lr
        }
        
        smart_metrics.update(current_metrics, progress=epoch/80)
        pbar.set_postfix(
            train_loss=f"{train_loss:.4f}",
            val_loss=f"{val_loss:.4f}",
            train_acc=f"{train_acc:.4f}",
            val_acc=f"{val_acc:.4f}"
        )
        time.sleep(0.05)
    
    # Generate comprehensive report
    report_path = report_gen.generate_report(pbar)
    print(f"✅ HTML Report generated: {report_path}")
    
    # Export data in different formats
    json_path = report_gen.export_json(pbar)
    csv_path = report_gen.export_csv(pbar)
    print(f"✅ JSON data exported: {json_path}")
    print(f"✅ CSV data exported: {csv_path}")
    
    # Display performance summary
    report = smart_metrics.get_performance_report()
    print(f"\n📈 Final Performance Summary:")
    for metric, stats in report['summary'].items():
        print(f"  {metric}:")
        print(f"    Current: {stats['current']:.4f}")
        print(f"    Mean: {stats['mean']:.4f}")
        print(f"    Trend: {stats['trend']:.6f}")
        print(f"    Volatility: {stats['volatility']:.4f}")

def demonstrate_custom_animations():
    """Demonstrate custom animation parameters"""
    print("\n🌊 Custom Animation Demo")
    print("=" * 40)
    
    # Create custom animations with different parameters
    animations = [
        ("Fast Wave", WaveAnimation(width=60, wave_speed=4.0)),
        ("Slow Ripple", ParticleAnimation(width=50, particle_count=8)),
        ("Intense Pulse", WaveAnimation(width=70, wave_speed=1.5))
    ]
    
    for anim_name, animation in animations:
        print(f"\n{anim_name}:")
        for epoch in smart_tqdm(
            range(25), 
            desc=f"{anim_name} Demo",
            animation=animation,
            theme=create_custom_theme()
        ):
            loss = random.uniform(0.1, 1.0)
            accuracy = random.uniform(0.5, 0.9)
            pbar.set_postfix(loss=f"{loss:.3f}", accuracy=f"{accuracy:.3f}")
            time.sleep(0.08)

def demonstrate_alert_system():
    """Demonstrate the alert and callback system"""
    print("\n🚨 Alert System Demo")
    print("=" * 40)
    
    from smart_tqdm import PerformanceStatus
    
    # Create smart metrics with alert callbacks
    smart_metrics = SmartMetrics()
    
    # Define alert callbacks
    def warning_alert(status, metrics):
        if status == PerformanceStatus.WARNING:
            print(f"\n⚠️  WARNING: Performance degradation detected!")
            print(f"   Metrics: {metrics}")
    
    def milestone_alert(milestone, metrics):
        print(f"\n🎯 MILESTONE: {milestone*100:.0f}% progress reached!")
        print(f"   Current metrics: {metrics}")
    
    def new_best_alert(status, metrics):
        if status == PerformanceStatus.NEW_BEST:
            print(f"\n🥳 NEW BEST: Outstanding performance achieved!")
            print(f"   Metrics: {metrics}")
    
    # Add callbacks
    smart_metrics.add_alert_callback(warning_alert)
    smart_metrics.add_alert_callback(new_best_alert)
    smart_metrics.add_milestone_callback(milestone_alert)
    
    # Simulate training with various performance patterns
    for epoch in smart_tqdm(range(60), desc="Alert System Test"):
        # Simulate different scenarios
        if epoch < 20:
            # Normal improvement
            loss = 2.0 - epoch * 0.08 + random.uniform(-0.02, 0.02)
            accuracy = 0.3 + epoch * 0.025 + random.uniform(-0.01, 0.01)
        elif epoch < 30:
            # Sudden degradation (should trigger warning)
            loss = 0.4 + random.uniform(0.1, 0.3)
            accuracy = 0.8 - random.uniform(0.05, 0.15)
        elif epoch < 45:
            # Recovery and new best
            loss = 0.2 - random.uniform(0.01, 0.05)
            accuracy = 0.95 + random.uniform(0.01, 0.03)
        else:
            # Stable performance
            loss = 0.15 + random.uniform(-0.01, 0.01)
            accuracy = 0.97 + random.uniform(-0.005, 0.005)
        
        # Update metrics
        smart_metrics.update(
            {"loss": loss, "accuracy": accuracy},
            progress=epoch/60
        )
        
        pbar.set_postfix(loss=f"{loss:.4f}", accuracy=f"{accuracy:.4f}")
        time.sleep(0.1)

def demonstrate_jupyter_support():
    """Demonstrate Jupyter notebook support"""
    print("\n📓 Jupyter Support Demo")
    print("=" * 40)
    print("This demo shows how SmartTQDM works in Jupyter notebooks.")
    print("Run this in a Jupyter notebook for the full experience.")
    
    # Simulate Jupyter-like environment
    for epoch in smart_tqdm(
        range(30), 
        desc="Jupyter Demo",
        theme=create_custom_theme(),
        animation=ParticleAnimation(particle_count=6)
    ):
        loss = random.uniform(0.1, 1.0)
        accuracy = random.uniform(0.5, 0.9)
        pbar.set_postfix(loss=f"{loss:.3f}", accuracy=f"{accuracy:.3f}")
        time.sleep(0.1)
    
    print("\n💡 In Jupyter, you can use:")
    print("   from IPython.display import clear_output")
    print("   clear_output(wait=True)  # For smooth animations")

if __name__ == "__main__":
    print("SmartTQDM Advanced Features Demo")
    print("=" * 60)
    
    # Run advanced demonstrations
    demonstrate_gif_export()
    demonstrate_comprehensive_reporting()
    demonstrate_custom_animations()
    demonstrate_alert_system()
    demonstrate_jupyter_support()
    
    print("\n🎉 Advanced features demonstration completed!")
    print("\n📁 Generated files:")
    print("  - exports/training_animation.gif")
    print("  - reports/smart_tqdm_report_*.html")
    print("  - reports/smart_tqdm_data_*.json")
    print("  - reports/smart_tqdm_metrics_*.csv")
    
    print("\n🚀 SmartTQDM is ready for your IEEE research!") 