# tqdm++ 🚀

**Enhanced Progress Bar with Intelligent Emoji Feedback**

An intelligent, stateful progress bar library specifically designed for neural network training and machine learning workflows. Unlike traditional progress bars, tqdm++ provides contextual emoji feedback based on your model's performance trends.

## ✨ Key Features

- **🧠 Intelligent Emoji Feedback**: Emojis change based on actual performance (accuracy/loss trends)
- **📊 Stateful Metric Tracking**: Remembers performance history across iterations
- **📈 Trend Detection**: Automatically detects improvement, plateau, or decline patterns  
- **🎨 Beautiful Color Gradients**: Smooth red→yellow→green progress visualization
- **⚡ Zero Dependencies**: Uses only Python standard library
- **🔧 Highly Configurable**: Multiple emoji selection strategies and customization options

## 🚀 Quick Start

### Installation

```bash
pip install tqdmpp
```

### Basic Usage

```python
from tqdmpp import SmartBar

# Simple progress tracking
bar = SmartBar(1000, desc="Training Neural Network")
for epoch in bar:
    # Your training code here
    accuracy = train_one_epoch()  # Your function
    loss = calculate_loss()       # Your function
    
    # Update metrics - emojis automatically change based on trends!
    bar.set_metrics(acc=accuracy, loss=loss)
```

### Smart Emoji Selection

```python
from tqdmpp import SmartBar, accuracy_based_selector, loss_based_selector
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
tqdmpp/
├── tqdmpp/
│   ├── __init__.py
│   ├── smart_bar.py
│   ├── config.py
│   ├── display.py
│   ├── emoji_selectors.py
│   └── metrics.py
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