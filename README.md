# SmartBar 🚀

**Intelligent Stateful Progress Bar with Emoji Feedback for Neural Network Training**

A smart progress bar library that provides intelligent, stateful feedback during neural network training with dynamic emoji selection based on real-time performance trends.

## 🌟 Features

### 🧠 Intelligent Stateful Design
- **Metric History Tracking**: Automatically tracks last 5 epochs of training metrics
- **Trend Detection**: Detects improvement, plateau, and decline patterns
- **Best Performance Recognition**: Automatically identifies new best accuracy/loss
- **Memory Efficient**: Only keeps recent history for trend analysis

### 🎯 Smart Emoji Selection
- **Accuracy-based Selector**: Emojis based on accuracy trends and improvements
- **Loss-based Selector**: Emojis based on loss reduction patterns
- **Default Intelligent**: Automatic trend detection without custom selectors
- **Dynamic Updates**: Emojis change in real-time as training progresses

### 🎨 Visual Features
- **Color Gradient**: Red → Yellow → Green progress indication
- **Emoji Slider**: Emoji moves along progress bar as slider head
- **Single-line Output**: Clean terminal display like tqdm
- **Dynamic Width**: Automatically adjusts to terminal size

### 📊 Real-time Metrics
- **Loss & Accuracy**: Real-time tracking and display
- **Time Elapsed**: Training duration display
- **Progress Percentage**: Clear progress indication
- **Trend Analysis**: Visual feedback on training patterns

## 🚀 Quick Start

### Installation

```bash
pip install smart-tqdm
```

### Basic Usage

```python
from smart_tqdm import SmartBar, accuracy_based_selector, loss_based_selector
import time
import random

# Simple usage with default intelligent selection
bar = SmartBar(100, desc="Training Model", show_emoji=True)

for epoch in bar:
    # Simulate training
    loss = random.uniform(0.1, 2.0)
    accuracy = random.uniform(0.5, 0.95)
    
    # Update metrics - emojis will automatically change based on trends
    bar.set_metrics(loss=f"{loss:.3f}", acc=f"{accuracy:.3f}")
    time.sleep(0.1)
```

### Advanced Usage with Custom Selectors

```python
# Accuracy-based emoji selection
bar = SmartBar(100, desc="Training", emoji_selector=accuracy_based_selector)

for epoch in bar:
    loss = random.uniform(0.1, 2.0)
    accuracy = random.uniform(0.5, 0.95)
    bar.set_metrics(loss=f"{loss:.3f}", acc=f"{accuracy:.3f}")

# Loss-based emoji selection
bar = SmartBar(100, desc="Training", emoji_selector=loss_based_selector)

for epoch in bar:
    loss = random.uniform(0.1, 2.0)
    accuracy = random.uniform(0.5, 0.95)
    bar.set_metrics(loss=f"{loss:.3f}", acc=f"{accuracy:.3f}")
```

## 🎯 Emoji Meanings

### Accuracy-based Selector
- 🥳 = New best accuracy!
- 🚀 = Excellent and improving
- 🔥 = Good and improving
- ⚡ = Decent and improving
- 📈 = Improving steadily
- 🏆 = Excellent but stable
- 🎯 = Average but stable
- 📊 = Low but stable
- 😅 = High but declining
- 😐 = Decent but declining
- 😰 = Low and declining

### Loss-based Selector
- 🥳 = New best loss!
- 🚀 = Very low and improving
- 🔥 = Low and improving
- ⚡ = Moderate and improving
- 📉 = High but improving
- 🏆 = Very low but stable
- 🎯 = High but stable
- 📊 = Very high but stable
- 😅 = Low but increasing
- 😐 = Moderate but increasing
- 😰 = High and increasing

## 📊 Real Training Example

```python
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from smart_tqdm import SmartBar, accuracy_based_selector

# Define your model
model = YourNeuralNetwork()
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters())

# Create SmartBar
bar = SmartBar(epochs, desc="Training", emoji_selector=accuracy_based_selector)

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
    
    # Update SmartBar with real metrics
    avg_loss = total_loss / len(train_loader)
    accuracy = correct / total
    bar.set_metrics(loss=f"{avg_loss:.3f}", acc=f"{accuracy:.3f}")
```

## 🎨 Customization

### Custom Emoji Selector

```python
def custom_selector(n, total, metrics, start_time, metric_history, best_accuracy, best_loss, accuracy_trend, loss_trend):
    """Custom emoji selection logic"""
    if 'custom_metric' in metrics:
        value = float(metrics['custom_metric'])
        if value > 0.9:
            return "🌟"
        elif value > 0.7:
            return "✨"
        else:
            return "💫"
    return "🎯"

# Use custom selector
bar = SmartBar(100, desc="Training", emoji_selector=custom_selector)
```

## 📦 Package Structure

```
smart_tqdm/
├── smart_tqdm/
│   ├── __init__.py
│   └── smart_bar.py
├── setup.py
├── README.md
├── requirements.txt
├── demo_smart_bar.py
└── real_training_test.py
```

## 🚀 Installation

### From Source

```bash
git clone https://github.com/your-repo/smart-tqdm.git
cd smart-tqdm
pip install -e .
```

### Dependencies

- Python >= 3.7
- No external dependencies (uses only Python standard library)

## 📝 Examples

### Demo Scripts

- `demo_smart_bar.py` - Simple demonstration of SmartBar features
- `real_training_test.py` - Real neural network training with Iris/Wine datasets

### Running Examples

```bash
# Simple demo
python demo_smart_bar.py

# Real training demo
python real_training_test.py
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Inspired by tqdm progress bar library
- Designed for neural network training workflows
- Built with ❤️ for the machine learning community

---

**SmartBar** - Making neural network training more engaging and informative! 🚀 