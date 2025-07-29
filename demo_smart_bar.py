import time
import random
import sys
from smart_tqdm.smart_bar import SmartBar, accuracy_based_selector, loss_based_selector

def main():
    print("🚀 SmartBar Demo (Intelligent Stateful Emoji Selection)")
    print("=" * 60)
    print("Watch how emojis change based on real training trends!")
    print("The SmartBar now tracks metric history and detects patterns.")
    print()

    # Demo 1: Accuracy-based Selector with Intelligent Trends
    print("📊 Demo 1: Intelligent Accuracy-based Emoji Selection")
    print("-" * 55)
    print("Emojis will change based on accuracy trends and improvements!")

    total_epochs = 50
    bar = SmartBar(total_epochs, desc="Training Neural Network", show_emoji=True, emoji_selector=accuracy_based_selector)

    # Simulate realistic training with ups and downs
    base_accuracy = 0.5
    for i in bar:
        # Simulate neural network training with realistic patterns
        if i < 10:
            # Early training - slow improvement
            accuracy = base_accuracy + i * 0.02 + random.uniform(-0.01, 0.01)
        elif i < 25:
            # Mid training - faster improvement
            accuracy = base_accuracy + 0.2 + (i-10) * 0.03 + random.uniform(-0.02, 0.02)
        elif i < 40:
            # Late training - plateau with occasional spikes
            accuracy = base_accuracy + 0.65 + random.uniform(-0.05, 0.05)
        else:
            # Final epochs - slight improvement
            accuracy = base_accuracy + 0.7 + (i-40) * 0.01 + random.uniform(-0.01, 0.01)
        
        # Ensure accuracy stays in reasonable bounds
        accuracy = max(0.1, min(0.99, accuracy))
        
        # Simulate corresponding loss
        loss = 2.0 - accuracy * 1.5 + random.uniform(-0.1, 0.1)
        loss = max(0.01, min(2.0, loss))

        # Update metrics
        bar.set_metrics(loss=f"{loss:.3f}", acc=f"{accuracy:.3f}")
        time.sleep(0.08)

    print("✅ Demo 1 completed!")

    # Demo 2: Loss-based Selector with Intelligent Trends
    print("\n📊 Demo 2: Intelligent Loss-based Emoji Selection")
    print("-" * 50)
    print("Emojis will change based on loss trends and improvements!")

    bar = SmartBar(total_epochs, desc="Training Neural Network", show_emoji=True, emoji_selector=loss_based_selector)

    # Simulate different loss pattern
    base_loss = 2.0
    for i in bar:
        # Simulate loss reduction with realistic patterns
        if i < 15:
            # Early training - rapid loss reduction
            loss = base_loss - i * 0.08 + random.uniform(-0.05, 0.05)
        elif i < 30:
            # Mid training - slower reduction
            loss = base_loss - 1.2 - (i-15) * 0.03 + random.uniform(-0.03, 0.03)
        elif i < 45:
            # Late training - plateau
            loss = base_loss - 1.65 + random.uniform(-0.02, 0.02)
        else:
            # Final epochs - slight improvement
            loss = base_loss - 1.7 - (i-45) * 0.01 + random.uniform(-0.01, 0.01)
        
        # Ensure loss stays in reasonable bounds
        loss = max(0.01, min(2.0, loss))
        
        # Simulate corresponding accuracy
        accuracy = 0.5 + (2.0 - loss) * 0.25 + random.uniform(-0.02, 0.02)
        accuracy = max(0.1, min(0.99, accuracy))

        # Update metrics
        bar.set_metrics(loss=f"{loss:.3f}", acc=f"{accuracy:.3f}")
        time.sleep(0.08)

    print("✅ Demo 2 completed!")

    # Demo 3: Default Intelligent Selector (No custom selector)
    print("\n📊 Demo 3: Default Intelligent Emoji Selection")
    print("-" * 45)
    print("SmartBar automatically detects trends without custom selector!")

    bar = SmartBar(total_epochs, desc="Training Neural Network", show_emoji=True)

    # Simulate training with mixed patterns
    base_accuracy = 0.4
    for i in bar:
        # Create interesting pattern: improvement -> plateau -> decline -> recovery
        if i < 12:
            # Improvement phase
            accuracy = base_accuracy + i * 0.04 + random.uniform(-0.01, 0.01)
        elif i < 25:
            # Plateau phase
            accuracy = base_accuracy + 0.48 + random.uniform(-0.02, 0.02)
        elif i < 35:
            # Decline phase
            accuracy = base_accuracy + 0.48 - (i-25) * 0.02 + random.uniform(-0.01, 0.01)
        else:
            # Recovery phase
            accuracy = base_accuracy + 0.28 + (i-35) * 0.03 + random.uniform(-0.01, 0.01)
        
        accuracy = max(0.1, min(0.99, accuracy))
        loss = 2.0 - accuracy * 1.5 + random.uniform(-0.1, 0.1)
        loss = max(0.01, min(2.0, loss))

        bar.set_metrics(loss=f"{loss:.3f}", acc=f"{accuracy:.3f}")
        time.sleep(0.08)

    print("✅ Demo 3 completed!")

    print("\n🎉🎉🎉 All Intelligent Demos Completed! 🎉🎉🎉")
    print("\n💡 New SmartBar Features:")
    print("   • 📈 Tracks metric history (last 5 epochs)")
    print("   • 🎯 Detects improvement/plateau/decline trends")
    print("   • 🏆 Recognizes new best accuracy/loss")
    print("   • 🚀 Shows different emojis for different patterns")
    print("   • 🧠 Intelligent default selection without custom selectors")
    print("\n📝 Usage Examples:")
    print("   # Accuracy-based with trend detection")
    print("   bar = SmartBar(100, emoji_selector=accuracy_based_selector)")
    print("   ")
    print("   # Loss-based with trend detection")
    print("   bar = SmartBar(100, emoji_selector=loss_based_selector)")
    print("   ")
    print("   # Automatic intelligent selection")
    print("   bar = SmartBar(100)  # No selector needed!")

if __name__ == "__main__":
    main() 