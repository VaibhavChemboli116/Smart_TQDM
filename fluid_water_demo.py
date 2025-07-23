#!/usr/bin/env python3
"""
Fluid Water Animation Demo with Real-time Emoji Feedback
Shows the beautiful fluid blue water effect and smart emoji changes
"""

import time
import random
import math

def fluid_water_training_demo():
    """Demo focused on showing the fluid water animation clearly"""
    print("🌊 Fluid Water Animation Demo")
    print("=" * 50)
    print("Watch the BLUE WATER flow through the progress bar!")
    print("Emojis change based on accuracy in real-time:")
    print("🔥 = Improving | 🥳 = New Best | 🐢 = Plateau | ⭐ = Excellent")
    print()
    
    try:
        from smart_tqdm import smart_tqdm, WaveAnimation
        
        # Create progress bar with enhanced fluid water animation
        epochs = 50
        
        pbar = smart_tqdm(
            range(epochs), 
            desc="Training Model",
            animation=WaveAnimation(wave_speed=4.0),  # Fast flowing water
            mininterval=0.1  # More frequent updates for smooth animation
        )
        
        # Simulate different training phases with realistic accuracy patterns
        for epoch in pbar:
            # Different training phases
            if epoch < 10:
                # Initial rapid improvement - should show 🔥
                accuracy = 0.3 + (epoch / 10) * 0.4 + random.uniform(-0.01, 0.02)
                loss = 2.0 - (epoch / 10) * 1.2 + random.uniform(-0.05, 0.05)
                phase = "Rapid Learning"
                
            elif epoch < 20:
                # Continued improvement - should show 🔥 or 🥳 for new bests
                base_acc = 0.7 + ((epoch - 10) / 10) * 0.15
                accuracy = base_acc + random.uniform(-0.005, 0.025)
                loss = 0.8 - ((epoch - 10) / 10) * 0.3 + random.uniform(-0.03, 0.03)
                phase = "Steady Progress"
                
            elif epoch < 30:
                # Plateau phase - should show 🐢
                accuracy = 0.85 + random.uniform(-0.005, 0.005)
                loss = 0.5 + random.uniform(-0.02, 0.02)
                phase = "Plateau"
                
            elif epoch < 40:
                # Breakthrough phase - should show 🥳 for new bests
                base_acc = 0.85 + ((epoch - 30) / 10) * 0.08
                accuracy = base_acc + random.uniform(0.0, 0.02)  # Only positive improvements
                loss = 0.45 - ((epoch - 30) / 10) * 0.1 + random.uniform(-0.01, 0.01)
                phase = "Breakthrough"
                
            else:
                # Excellent performance - should show ⭐
                accuracy = 0.93 + ((epoch - 40) / 10) * 0.05 + random.uniform(-0.002, 0.005)
                loss = 0.35 - ((epoch - 40) / 10) * 0.05 + random.uniform(-0.005, 0.005)
                phase = "Excellence"
            
            # Ensure bounds
            accuracy = max(0.0, min(1.0, accuracy))
            loss = max(0.0, loss)
            
            # Update progress bar with metrics
            pbar.set_postfix(
                accuracy=f"{accuracy:.4f}",
                loss=f"{loss:.4f}",
                phase=phase
            )
            
            # This is the key - update metrics to trigger emoji changes!
            pbar.update_metrics({
                'accuracy': accuracy,
                'loss': loss
            })
            
            # Slower sleep to better see the fluid animation
            time.sleep(0.15)
        
        print(f"\n🎉 Training Complete!")
        print("Did you see the fluid blue water animation? 🌊")
        print("And how the emojis changed based on accuracy trends? 😊")
        
    except Exception as e:
        print(f"❌ Error: {e}")

def accuracy_focused_demo():
    """Demo that focuses on accuracy-based emoji changes"""
    print("\n🎯 Accuracy-Focused Emoji Demo")
    print("=" * 50)
    print("Watch emojis change as accuracy improves:")
    
    try:
        from smart_tqdm import smart_tqdm, WaveAnimation
        
        # Simulate different accuracy scenarios
        scenarios = [
            ("Low Accuracy (Random)", [0.3 + random.uniform(-0.1, 0.1) for _ in range(10)]),
            ("Improving", [0.4 + i*0.05 + random.uniform(-0.01, 0.01) for i in range(10)]),
            ("Plateau", [0.8 + random.uniform(-0.01, 0.01) for _ in range(10)]),
            ("New Bests", [0.7 + i*0.02 + random.uniform(0.0, 0.01) for i in range(10)]),
            ("Excellent", [0.95 + random.uniform(-0.005, 0.005) for _ in range(10)])
        ]
        
        for scenario_name, accuracies in scenarios:
            print(f"\n{scenario_name}:")
            
            pbar = smart_tqdm(
                range(len(accuracies)), 
                desc=scenario_name,
                animation=WaveAnimation(wave_speed=3.0)
            )
            
            for i, accuracy in enumerate(pbar):
                pbar.set_postfix(accuracy=f"{accuracies[i]:.4f}")
                pbar.update_metrics({'accuracy': accuracies[i]})
                time.sleep(0.2)
            
            time.sleep(0.5)  # Pause between scenarios
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    fluid_water_training_demo()
    accuracy_focused_demo()
    
    print("\n🌟 What you just saw:")
    print("   🌊 Fluid blue water animation flowing through progress bar")
    print("   🔥 Real-time emoji changes based on accuracy trends")
    print("   📊 Smart performance analysis in action")
    print("   💧 Beautiful visual feedback for neural network training")
    
    print("\n🚀 Your SmartTQDM is ready for IEEE research!")
    print("   Just use: pbar.update_metrics({'accuracy': acc_value})")
    print("   And watch the magic happen! ✨") 