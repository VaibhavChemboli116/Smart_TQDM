#!/usr/bin/env python3
"""
Quick demo of SmartTQDM features
Run this script to see SmartTQDM in action!
"""

import time
import random
import numpy as np

def main():
    print("🚀 SmartTQDM Demo")
    print("=" * 50)
    print("This demo showcases the key features of SmartTQDM")
    print("Watch the emojis change based on performance!")
    print()
    
    try:
        from smart_tqdm import smart_tqdm, CatTheme, WaveAnimation
        
        # Demo 1: Basic usage with performance simulation
        print("🔥 Demo 1: Basic SmartTQDM with Performance Feedback")
        print("-" * 50)
        
        pbar = smart_tqdm(range(50), desc="Training Model")
        for epoch in pbar:
            # Simulate realistic training patterns
            if epoch < 15:
                # Initial rapid improvement
                loss = 2.0 - epoch * 0.1 + random.uniform(-0.05, 0.05)
                accuracy = 0.3 + epoch * 0.03 + random.uniform(-0.02, 0.02)
            elif epoch < 35:
                # Plateau phase
                loss = 0.5 + random.uniform(-0.03, 0.03)
                accuracy = 0.75 + random.uniform(-0.02, 0.02)
            else:
                # Final improvement
                loss = 0.3 - (epoch - 35) * 0.005 + random.uniform(-0.01, 0.01)
                accuracy = 0.85 + (epoch - 35) * 0.002 + random.uniform(-0.005, 0.005)
            
            # Update progress bar - emojis will change based on performance!
            pbar.set_postfix(loss=f"{loss:.4f}", accuracy=f"{accuracy:.4f}")
            time.sleep(0.1)
        
        print("\n✅ Demo 1 completed!")
        
        # Demo 2: Custom theme
        print("\n🐱 Demo 2: Cat Theme with Wave Animation")
        print("-" * 50)
        
        pbar = smart_tqdm(
            range(30), 
            desc="Cat Training",
            theme=CatTheme(),
            animation=WaveAnimation(wave_speed=2.0)
        )
        for epoch in pbar:
            loss = random.uniform(0.1, 1.0)
            accuracy = random.uniform(0.5, 0.9)
            pbar.set_postfix(loss=f"{loss:.3f}", accuracy=f"{accuracy:.3f}")
            time.sleep(0.1)
        
        print("\n✅ Demo 2 completed!")
        
        # Demo 3: Context manager
        print("\n🔧 Demo 3: Context Manager Usage")
        print("-" * 50)
        
        from smart_tqdm import smart_progress
        
        with smart_progress(
            range(20), 
            desc="Context Demo",
            theme=CatTheme(),
            animation=WaveAnimation()
        ) as pbar:
            for epoch in pbar:
                loss = random.uniform(0.1, 1.0)
                accuracy = random.uniform(0.5, 0.9)
                pbar.set_postfix(loss=f"{loss:.3f}", accuracy=f"{accuracy:.3f}")
                time.sleep(0.1)
        
        print("\n✅ Demo 3 completed!")
        
        print("\n🎉 All demos completed successfully!")
        print("\n💡 Key Features Demonstrated:")
        print("   • Emoji-based performance feedback")
        print("   • Fluid progress bar animations")
        print("   • Custom themes (Cat theme)")
        print("   • Context manager usage")
        print("   • Smart metrics awareness")
        
        print("\n🚀 SmartTQDM is ready for your IEEE research!")
        print("Check out examples/ directory for more advanced features.")
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Make sure you have installed the required dependencies:")
        print("pip install tqdm numpy matplotlib pillow")
    except Exception as e:
        print(f"❌ Demo failed: {e}")
        print("Please check the SmartTQDM installation.")

if __name__ == "__main__":
    main() 