# tqdm++ 🚀

**Enhanced Progress Bar with Intelligent Emoji Feedback & Performance Tracking**

A modern, intelligent progress bar library specifically designed for neural network training workflows. tqdm++ provides contextual emoji feedback based on your model's actual performance trends, making training monitoring both informative and engaging.

## ✨ Key Features

- **🧠 Intelligent Emoji Feedback**: Emojis change dynamically based on real performance metrics (accuracy/loss trends)
- **📊 Stateful Metric Tracking**: Maintains performance history and best scores across training iterations
- **📈 Trend Detection**: Automatically detects improvement, plateau, or decline patterns in your metrics
- **🎨 Beautiful Color Gradients**: Smooth red→yellow→green progress visualization with emoji positioning
- **⚡ Zero Dependencies**: Uses only Python standard library - no external dependencies required
- **🔧 Highly Configurable**: Multiple emoji selection strategies and full customization support
- **🎯 ML-Focused**: Specifically designed for neural networks

## 🚀 Quick Start

### Installation

```bash
# From PyPI (coming soon)
pip install tqdmpp

# From source
git clone https://github.com/VaibhavChemboli116/Smart_TQDM.git
cd Smart_TQDM
pip install -e .
```

### Basic Usage

```python
from tqdmpp import SmartBar

# Simple progress tracking with automatic emoji feedback
bar = SmartBar(total=100, desc="Training Neural Network")

for epoch in range(100):
    # Simulate training
    accuracy = train_one_epoch()  # Your training function
    loss = calculate_loss()       # Your loss calculation
    
    # Update metrics - emojis automatically change based on trends!
    bar.set_metrics(acc=accuracy, loss=loss)
    bar.n = epoch + 1
    bar._print_bar()
```

### Advanced Usage with Custom Selectors

```python
from tqdmpp import SmartBar, accuracy_based_selector, loss_based_selector

# Use accuracy-focused emoji selection
bar = SmartBar(
    total=epochs,
    desc="Training VGG16",
    emoji_selector=accuracy_based_selector
)

for epoch in bar:
    # Your training loop here
    acc, loss = train_epoch()
    bar.set_metrics(acc=acc, loss=loss)
```

## 🎯 Emoji System

tqdm++ uses a simple, intelligent emoji system based on performance trends:

### The 5 Core Emojis
- **🥳** = New best performance achieved!
- **🚀** = Performance is improving (positive trend)
- **🎯** = Performance is stable (no significant change)  
- **😅** = Performance is declining (negative trend)
- **😰** = Severe performance decline

### How It Works
1. **New Best Check**: If current accuracy/loss beats previous best → 🥳
2. **Trend Analysis**: Based on last few iterations:
   - Improving trend → 🚀
   - Stable trend → 🎯  
   - Declining trend → 😅 (or 😰 for severe cases)

## 📊 Real-World Example

Here's how tqdm++ looks in a real neural network training scenario:

```python
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from tqdmpp import SmartBar, accuracy_based_selector

# Setup your model
model = YourNeuralNetwork()
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Create tqdm++ bar
epochs = 50
bar = SmartBar(
    total=epochs, 
    desc="Training ResNet-18",
    emoji_selector=accuracy_based_selector
)

for epoch in bar:
    model.train()
    total_loss = 0
    correct = 0
    total = 0
    
    for batch_idx, (data, target) in enumerate(train_loader):
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
        
        total_loss += loss.item()
        pred = output.argmax(dim=1, keepdim=True)
        correct += pred.eq(target.view_as(pred)).sum().item()
        total += target.size(0)
    
    # tqdm++ automatically analyzes trends and selects appropriate emojis
    epoch_loss = total_loss / len(train_loader)
    epoch_acc = correct / total
    bar.set_metrics(loss=f"{epoch_loss:.4f}", acc=f"{epoch_acc:.4f}")

# Output example:
# Training ResNet-18 ┃██████████████(gradient bar)🚀              ┃ 35/50 70.0% [ 45.2s] [loss:0.2341 acc:0.8934]
```

## 🎨 Customization

### Creating Custom Emoji Selectors

```python
def custom_selector(n, total, metrics, start_time, metric_history, 
                   best_accuracy, best_loss, accuracy_trend, loss_trend):
    """
    Custom emoji selection logic based on your specific needs
    
    Args:
        n: Current iteration
        total: Total iterations
        metrics: Current metrics dict
        start_time: Training start time
        metric_history: Historical metrics
        best_accuracy: Best accuracy so far
        best_loss: Best loss so far
        accuracy_trend: -1 (declining), 0 (stable), 1 (improving)
        loss_trend: -1 (increasing), 0 (stable), 1 (decreasing)
    """
    if 'custom_metric' in metrics:
        value = float(metrics['custom_metric'])
        if value > 0.95:
            return "🌟"  # Excellent
        elif value > 0.85:
            return "⭐"  # Good
        elif value > 0.70:
            return "✨"  # Decent
        else:
            return "💫"  # Needs improvement
    
    # Fallback to trend-based selection
    if accuracy_trend == 1 or loss_trend == 1:
        return "🚀"
    elif accuracy_trend == -1 or loss_trend == -1:
        return "😅"
    else:
        return "🎯"

# Use your custom selector
bar = SmartBar(total=100, desc="Custom Training", emoji_selector=custom_selector)
```

### Configuration Options

```python
from tqdmpp import SmartBar
from tqdmpp.config import ProgressBarConfig

# Customize trend detection sensitivity
ProgressBarConfig.ACCURACY_THRESHOLD = 0.01  # Default: 0.005
ProgressBarConfig.LOSS_THRESHOLD = 0.02       # Default: 0.01

# Create bar with custom settings
bar = SmartBar(
    total=epochs,
    desc="Fine-tuned Training",
    show_emoji=True,      # Show emoji feedback
    show_metrics=True,    # Show metrics in bar
    width=None           # Auto-detect terminal width
)
```

## 📦 Project Structure

```
Smart_TQDM/
├── tqdmpp/                     # Main package
│   ├── __init__.py            # Package exports
│   ├── smart_bar.py           # Main SmartBar class
│   ├── config.py              # Configuration constants
│   ├── display.py             # Terminal rendering
│   ├── emoji_selectors.py     # Emoji selection logic
│   └── metrics.py             # Metric tracking & trend analysis
├── classification_tqdmpp_demo.ipynb  # Jupyter demo with VGG16
├── pyproject.toml             # Modern Python packaging
├── setup.py                   # Installation script
├── requirements.txt           # Dependencies (none for core!)
└── README.md                  # This file
```

## 📚 Examples & Demos

### 1. Jupyter Notebook Demo
The `classification_tqdmpp_demo.ipynb` notebook contains a complete example:
- VGG16 image classification training
- Real-time emoji feedback
- Performance comparison with standard tqdm


## 🔧 Technical Details

### Requirements
- **Python**: 3.7 or higher
- **Dependencies**: None (uses only Python standard library)
- **Optional**: PyTorch, scikit-learn (for running the examples)

### Performance
- **Lightweight**: Minimal overhead during training
- **Efficient**: Optimized for frequent updates
- **Memory**: Small footprint with configurable history size

### Compatibility
- ✅ Linux, macOS, Windows
- ✅ Jupyter Notebooks
- ✅ Terminal/Command Line

## 🤝 Contributing

We welcome contributions and issues! 

### Development Setup

```bash
git clone https://github.com/VaibhavChemboli116/Smart_TQDM.git
cd Smart_TQDM
pip install -e ".[dev]"  # Install with development dependencies
```

## 👥 Authors

- **Vaibhav Chemboli** - *Lead Developer* - [vaibhav.chemboli@gmail.com](mailto:vaibhav.chemboli@gmail.com)
- **Keerthi Sana** - *Co-Developer* - [keerthisana.sk@gmail.com](mailto:keerthisana.sk@gmail.com)

## 🙏 Acknowledgments

- Inspired by the excellent [tqdm](https://github.com/tqdm/tqdm) progress bar library
- Designed specifically for the deep learning community
- Built with ❤️ for making neural network training more engaging and informative

## 🚀 Why tqdm++?

Traditional progress bars only show completion percentage. tqdm++ goes beyond that by:

1. **Understanding Your Training**: Analyzes your actual metrics, not just progress
2. **Providing Context**: Emojis give instant visual feedback about performance trends
3. **Saving Mental Energy**: No need to constantly monitor loss curves - the emoji tells you instantly
4. **Making Training Fun**: Engaging visual feedback makes long training sessions more enjoyable
5. **Zero Overhead**: Lightweight design that won't slow down your training

---

**tqdm++** - Because your progress bar should be as intelligent as your model! 🚀✨
