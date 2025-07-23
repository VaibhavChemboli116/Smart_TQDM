# SmartTQDM 🚀

**Intelligent Progress Bar with Emoji Feedback and Fluid Visualization**

A drop-in replacement for tqdm with smart features including emoji-based performance feedback, fluid progress bar animations, intelligent metrics awareness, and comprehensive reporting capabilities.

## 🌟 Features

### 🎯 Emoji-Based Feedback
- **Smart Performance Detection**: Automatically displays emojis based on training performance
- **Multiple Themes**: Default, Cat, Rocket, Gaming, Nature, and Custom themes
- **Milestone Recognition**: Special emojis for 25%, 50%, 75%, and 90% progress milestones
- **Performance Status**: 🔥 Improving, 🐢 Plateau, 😅 Unstable, 🥳 New Best, 🐌 Slow, ⭐ Excellent

### 🌊 Fluid Progress Bar Visualization
- **Wave Animation**: Smooth wave-like progress bar
- **Ripple Effect**: Ripple animation from center
- **Pulse Animation**: Pulsing effect with global and local variations
- **Gradient Animation**: Moving gradient across the progress bar
- **Particle Animation**: Floating particles with life cycles
- **Matrix Animation**: Digital rain effect
- **Rainbow Animation**: Color cycling (for color terminals)

### 📊 Smart Metrics Awareness
- **Real-time Analysis**: Tracks trends, volatility, and performance patterns
- **Intelligent Alerts**: Automatic detection of performance issues
- **Moving Averages**: Smooth trend analysis
- **Performance Recommendations**: AI-powered suggestions for improvement

### 🎨 Customization & Themes
- **Plug-and-Play API**: Drop-in replacement for tqdm
- **Custom Emoji Mappings**: Define your own emoji-performance relationships
- **Animated Themes**: Themes with cycling emoji variations
- **Jupyter Support**: Full compatibility with Jupyter notebooks

### 📈 Export & Reporting
- **GIF Export**: Save animated progress bars as GIFs
- **HTML Reports**: Comprehensive performance reports with interactive charts
- **JSON/CSV Export**: Data export for further analysis
- **Real-time Visualization**: ASCII plots and performance charts

## 🚀 Quick Start

### Installation

```bash
pip install smart-tqdm
```

### Basic Usage

```python
from smart_tqdm import smart_tqdm
import time
import random

# Simple usage - drop-in replacement for tqdm
for epoch in smart_tqdm(range(100), desc="Training"):
    # Simulate training
    loss = random.uniform(0.1, 2.0)
    accuracy = random.uniform(0.5, 0.95)
    
    # Update metrics - emojis will automatically appear based on performance
    pbar.set_postfix(loss=loss, accuracy=accuracy)
    time.sleep(0.1)
```

### Advanced Usage with Custom Theme

```python
from smart_tqdm import smart_tqdm, CatTheme, WaveAnimation

# Custom theme and animation
for epoch in smart_tqdm(
    range(100), 
    desc="Training",
    theme=CatTheme(),
    animation=WaveAnimation(wave_speed=2.0)
):
    loss = random.uniform(0.1, 2.0)
    accuracy = random.uniform(0.5, 0.95)
    
    pbar.set_postfix(loss=loss, accuracy=accuracy)
    time.sleep(0.1)
```

## 🎨 Themes

### Available Themes

```python
from smart_tqdm import ThemeFactory

# List all available themes
print(ThemeFactory.list_themes())
# ['default', 'cat', 'rocket', 'gaming', 'nature', 'animated', 'custom']

# Create themes
default_theme = ThemeFactory.create_theme("default")
cat_theme = ThemeFactory.create_theme("cat")
rocket_theme = ThemeFactory.create_theme("rocket")
gaming_theme = ThemeFactory.create_theme("gaming")
nature_theme = ThemeFactory.create_theme("nature")
animated_theme = ThemeFactory.create_theme("animated")
```

### Custom Theme

```python
from smart_tqdm import CustomTheme, PerformanceStatus

# Define custom emoji mappings
custom_emojis = {
    PerformanceStatus.IMPROVING: "🚀",
    PerformanceStatus.PLATEAU: "⏸️",
    PerformanceStatus.UNSTABLE: "🌪️",
    PerformanceStatus.NEW_BEST: "🏆",
    PerformanceStatus.SLOW: "🐌",
    PerformanceStatus.EXCELLENT: "💎",
    PerformanceStatus.WARNING: "⚠️",
    PerformanceStatus.MILESTONE: "🎯"
}

custom_theme = CustomTheme(custom_emojis)

for epoch in smart_tqdm(range(100), theme=custom_theme):
    # Your training code here
    pass
```

## 🌊 Animations

### Available Animations

```python
from smart_tqdm import AnimationFactory

# List all available animations
print(AnimationFactory.list_animations())
# ['fluid', 'wave', 'ripple', 'pulse', 'gradient', 'particle', 'matrix', 'rainbow']

# Create animations with custom parameters
wave_anim = AnimationFactory.create_animation("wave", wave_speed=3.0)
ripple_anim = AnimationFactory.create_animation("ripple", ripple_speed=2.0)
pulse_anim = AnimationFactory.create_animation("pulse", pulse_speed=4.0)
particle_anim = AnimationFactory.create_animation("particle", particle_count=8)
```

### Custom Animation Parameters

```python
from smart_tqdm import WaveAnimation, ParticleAnimation

# Wave animation with custom speed
wave_anim = WaveAnimation(width=60, wave_speed=2.5)

# Particle animation with more particles
particle_anim = ParticleAnimation(width=50, particle_count=10)

for epoch in smart_tqdm(range(100), animation=wave_anim):
    # Your training code here
    pass
```

## 📊 Smart Metrics

### Performance Analysis

```python
from smart_tqdm import smart_tqdm, SmartMetrics

# Create smart metrics tracker
smart_metrics = SmartMetrics()

# Add alert callbacks
def performance_alert(status, metrics):
    if status == PerformanceStatus.WARNING:
        print(f"⚠️ Performance warning: {metrics}")

smart_metrics.add_alert_callback(performance_alert)

# Use in training loop
for epoch in smart_tqdm(range(100)):
    loss = random.uniform(0.1, 2.0)
    accuracy = random.uniform(0.5, 0.95)
    
    # Update metrics with smart analysis
    status = smart_metrics.update(
        {"loss": loss, "accuracy": accuracy}, 
        progress=epoch/100
    )
    
    pbar.set_postfix(loss=loss, accuracy=accuracy)
```

### Get Performance Report

```python
# Generate comprehensive performance report
report = smart_metrics.get_performance_report()
print("Performance Summary:", report['summary'])
print("Recommendations:", report['recommendations'])
```

## 📈 Export & Reporting

### GIF Export

```python
from smart_tqdm import smart_tqdm, GIFExporter

# Create GIF exporter
gif_exporter = GIFExporter(fps=10)

for epoch in smart_tqdm(range(100)):
    loss = random.uniform(0.1, 2.0)
    accuracy = random.uniform(0.5, 0.95)
    
    # Capture frame for GIF
    gif_exporter.capture_frame(pbar, {"loss": loss, "accuracy": accuracy})
    
    pbar.set_postfix(loss=loss, accuracy=accuracy)

# Export GIF
gif_exporter.export(pbar, "training_progress.gif", duration=3.0)
```

### HTML Report Generation

```python
from smart_tqdm import smart_tqdm, ReportGenerator

# Create report generator
report_gen = ReportGenerator(output_dir="reports")

for epoch in smart_tqdm(range(100)):
    loss = random.uniform(0.1, 2.0)
    accuracy = random.uniform(0.5, 0.95)
    
    pbar.set_postfix(loss=loss, accuracy=accuracy)

# Generate comprehensive HTML report
report_path = report_gen.generate_report(pbar)
print(f"Report generated: {report_path}")

# Export data in different formats
json_path = report_gen.export_json(pbar)
csv_path = report_gen.export_csv(pbar)
```

## 🔧 Advanced Configuration

### Context Manager Usage

```python
from smart_tqdm import smart_progress

with smart_progress(range(100), theme=CatTheme(), animation=WaveAnimation()) as pbar:
    for epoch in pbar:
        loss = random.uniform(0.1, 2.0)
        accuracy = random.uniform(0.5, 0.95)
        
        pbar.set_postfix(loss=loss, accuracy=accuracy)
```

### Jupyter Notebook Support

```python
# In Jupyter notebook
from smart_tqdm import smart_tqdm
from IPython.display import display, clear_output

for epoch in smart_tqdm(range(100), desc="Training"):
    loss = random.uniform(0.1, 2.0)
    accuracy = random.uniform(0.5, 0.95)
    
    pbar.set_postfix(loss=loss, accuracy=accuracy)
    
    # Clear output for smooth animation in Jupyter
    if epoch % 10 == 0:
        clear_output(wait=True)
```

## 🎯 Performance Status Detection

SmartTQDM automatically detects performance patterns:

- **🔥 Improving**: Positive trend detected
- **🐢 Plateau**: No significant change in metrics
- **😅 Unstable**: High volatility in metrics
- **🥳 New Best**: New best value achieved
- **🐌 Slow**: Declining performance
- **⭐ Excellent**: Outstanding performance
- **⚠️ Warning**: Performance issues detected
- **🎯 Milestone**: Progress milestone reached

## 📋 Requirements

- Python 3.7+
- tqdm >= 4.64.0
- numpy >= 1.21.0
- matplotlib >= 3.5.0
- pillow >= 8.0.0

### Optional Dependencies

```bash
# For development
pip install smart-tqdm[dev]

# For Jupyter support
pip install smart-tqdm[jupyter]

# For full features
pip install smart-tqdm[full]
```

## 🤝 Contributing

This is an IEEE research project. Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📚 Citation

If you use SmartTQDM in your research, please cite:

```bibtex
@software{smart_tqdm,
  title={SmartTQDM: Intelligent Progress Bar with Emoji Feedback and Fluid Visualization},
  author={IEEE Research Project},
  year={2024},
  url={https://github.com/ieee-research/smart-tqdm}
}
```

## 🚀 Roadmap

- [ ] Real-time performance optimization suggestions
- [ ] Integration with popular ML frameworks (PyTorch, TensorFlow)
- [ ] Web-based dashboard
- [ ] Mobile app for remote monitoring
- [ ] Advanced statistical analysis
- [ ] Custom animation builder
- [ ] Plugin system for custom themes and animations

---

**Made with ❤️ for the IEEE Research Community** 