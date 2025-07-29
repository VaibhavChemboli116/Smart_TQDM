"""
Real training simulation script for testing SmartBar with actual ML workflow
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import time
import numpy as np
from sklearn.datasets import load_iris, load_wine, load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import random
import math

from tqdmpp import SmartBar, accuracy_based_selector, loss_based_selector

# Set device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"🚀 Using device: {device}")

# Define neural networks for different datasets
class SimpleNN(nn.Module):
    def __init__(self, input_size, hidden_size=32, num_classes=3):
        super(SimpleNN, self).__init__()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(hidden_size, hidden_size // 2),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(hidden_size // 2, num_classes)
        )

    def forward(self, x):
        logits = self.linear_relu_stack(x)
        return logits

def load_iris_dataset():
    """Load the real Iris dataset"""
    print("🌸 Loading Iris dataset...")
    
    # Load Iris dataset
    iris = load_iris()
    X, y = iris.data, iris.target
    
    # Split into train and test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Scale the features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    # Convert to PyTorch tensors
    X_train = torch.FloatTensor(X_train)
    y_train = torch.LongTensor(y_train)
    X_test = torch.FloatTensor(X_test)
    y_test = torch.LongTensor(y_test)
    
    print(f"📊 Iris dataset loaded:")
    print(f"   • Training samples: {len(X_train)}")
    print(f"   • Test samples: {len(X_test)}")
    print(f"   • Features: {X_train.shape[1]}")
    print(f"   • Classes: {len(np.unique(y))}")
    
    return X_train, y_train, X_test, y_test

def load_wine_dataset():
    """Load the real Wine dataset"""
    print("🍷 Loading Wine dataset...")
    
    # Load Wine dataset
    wine = load_wine()
    X, y = wine.data, wine.target
    
    # Split into train and test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Scale the features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    # Convert to PyTorch tensors
    X_train = torch.FloatTensor(X_train)
    y_train = torch.LongTensor(y_train)
    X_test = torch.FloatTensor(X_test)
    y_test = torch.LongTensor(y_test)
    
    print(f"📊 Wine dataset loaded:")
    print(f"   • Training samples: {len(X_train)}")
    print(f"   • Test samples: {len(X_test)}")
    print(f"   • Features: {X_train.shape[1]}")
    print(f"   • Classes: {len(np.unique(y))}")
    
    return X_train, y_train, X_test, y_test

def train_model(dataset_name="iris"):
    """Train a real neural network with SmartBar progress tracking"""
    print(f"🎯 Real Neural Network Training with {dataset_name.upper()} Dataset")
    print("=" * 65)

    # Load real dataset
    if dataset_name.lower() == "wine":
        X_train, y_train, X_test, y_test = load_wine_dataset()
        input_size = 13
        num_classes = 3
    else:
        X_train, y_train, X_test, y_test = load_iris_dataset()
        input_size = 4
        num_classes = 3
    
    # Create data loaders
    train_dataset = TensorDataset(X_train, y_train)
    test_dataset = TensorDataset(X_test, y_test)
    
    train_loader = DataLoader(train_dataset, batch_size=4, shuffle=True)  # Smaller batch size
    test_loader = DataLoader(test_dataset, batch_size=4, shuffle=False)   # Smaller batch size

    # Model setup
    model = SimpleNN(input_size=input_size, num_classes=num_classes).to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    print(f"📈 Model parameters: {sum(p.numel() for p in model.parameters()):,}")
    print()

    # Training parameters
    epochs = 50  # Increased from 20 to 50 for more visible progress
    best_accuracy = 0.0

    # Test 1: Accuracy-based emojis with intelligent trends
    print("🎯 Test 1: Intelligent Accuracy-based Emoji Selection")
    print("-" * 55)

    bar = SmartBar(epochs, desc="Training Model", show_emoji=True, emoji_selector=accuracy_based_selector)

    for epoch in bar:
        model.train()
        total_loss = 0
        correct = 0
        total = 0

        for batch_idx, (data, target) in enumerate(train_loader):
            data, target = data.to(device), target.to(device)

            optimizer.zero_grad()
            output = model(data)
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()

            total_loss += loss.item()
            pred = output.argmax(dim=1, keepdim=True)
            correct += pred.eq(target.view_as(pred)).sum().item()
            total += target.size(0)

        # Calculate epoch metrics
        avg_loss = total_loss / len(train_loader)
        accuracy = correct / total

        # Update SmartBar with intelligent trend detection
        bar.set_metrics(loss=f"{avg_loss:.3f}", acc=f"{accuracy:.3f}")
        
        # Add delay to see emoji changes
        time.sleep(0.3)  # 300ms delay between epochs

        # Track best accuracy
        if accuracy > best_accuracy:
            best_accuracy = accuracy

    print(f"✅ Best Training Accuracy: {best_accuracy:.3f}")

    # Evaluate on test set
    model.eval()
    test_loss = 0
    correct = 0
    total = 0

    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            test_loss += criterion(output, target).item()
            pred = output.argmax(dim=1, keepdim=True)
            correct += pred.eq(target.view_as(pred)).sum().item()
            total += target.size(0)

    test_accuracy = correct / total
    print(f"🧪 Test Accuracy: {test_accuracy:.3f}")

    # Test 2: Loss-based emojis with intelligent trends
    print("\n📉 Test 2: Intelligent Loss-based Emoji Selection")
    print("-" * 50)

    # Reset model for second test
    model = SimpleNN(input_size=input_size, num_classes=num_classes).to(device)
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    bar = SmartBar(epochs, desc="Training Model", show_emoji=True, emoji_selector=loss_based_selector)

    for epoch in bar:
        model.train()
        total_loss = 0
        correct = 0
        total = 0

        for batch_idx, (data, target) in enumerate(train_loader):
            data, target = data.to(device), target.to(device)

            optimizer.zero_grad()
            output = model(data)
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()

            total_loss += loss.item()
            pred = output.argmax(dim=1, keepdim=True)
            correct += pred.eq(target.view_as(pred)).sum().item()
            total += target.size(0)

        # Calculate epoch metrics
        avg_loss = total_loss / len(train_loader)
        accuracy = correct / total

        # Update SmartBar with intelligent trend detection
        bar.set_metrics(loss=f"{avg_loss:.3f}", acc=f"{accuracy:.3f}")
        
        # Add delay to see emoji changes
        time.sleep(0.3)  # 300ms delay between epochs

    print(f"✅ Final Training Loss: {avg_loss:.3f}")
    print(f"✅ Final Training Accuracy: {accuracy:.3f}")

    # Test 3: Default intelligent selection (no custom selector)
    print("\n🧠 Test 3: Default Intelligent Emoji Selection")
    print("-" * 45)
    print("SmartBar automatically detects trends without custom selector!")

    # Reset model for third test
    model = SimpleNN(input_size=input_size, num_classes=num_classes).to(device)
    optimizer = optim.Adam(model.parameters(), lr=0.00005)

    bar = SmartBar(epochs, desc="Training Model", show_emoji=True)

    for epoch in bar:
        model.train()
        total_loss = 0
        correct = 0
        total = 0

        for batch_idx, (data, target) in enumerate(train_loader):
            data, target = data.to(device), target.to(device)

            optimizer.zero_grad()
            output = model(data)
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()

            total_loss += loss.item()
            pred = output.argmax(dim=1, keepdim=True)
            correct += pred.eq(target.view_as(pred)).sum().item()
            total += target.size(0)

        # Calculate epoch metrics
        avg_loss = total_loss / len(train_loader)
        accuracy = correct / total

        # Update SmartBar with intelligent trend detection
        bar.set_metrics(loss=f"{avg_loss:.3f}", acc=f"{accuracy:.3f}")
        
        # Add delay to see emoji changes
        time.sleep(0.3)  # 300ms delay between epochs

    print(f"✅ Final Training Loss: {avg_loss:.3f}")
    print(f"✅ Final Training Accuracy: {accuracy:.3f}")

    print(f"\n🎉🎉🎉 Real Training with {dataset_name.upper()} Dataset Completed! 🎉🎉🎉")
    print("\n💡 SmartBar Features Demonstrated:")
    print(f"   • 📈 Real neural network training with {dataset_name.upper()} dataset")
    print("   • 🎯 Emoji moves along progress bar as slider head")
    print("   • 🌈 Color gradient from red → yellow → green")
    print("   • 📊 Real-time loss and accuracy metrics")
    print("   • 🧠 Intelligent trend detection (improvement/plateau/decline)")
    print("   • 🏆 New best accuracy/loss recognition")
    print("   • 🎨 Configurable emoji selection (accuracy vs loss vs default)")
    print("   • 📱 Single-line terminal output")
    print("\n🚀 Ready for production use!")

if __name__ == "__main__":
    # Use Wine dataset by default (more features = slower training = better emoji visibility)
    print("🍷 Using Wine dataset for slower, more visible training...")
    train_model("wine")
    
    # Uncomment to try Iris dataset instead (faster)
    # print("🌸 Using Iris dataset...")
    # train_model("iris") 