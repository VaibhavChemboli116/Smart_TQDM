#!/usr/bin/env python3
"""
Test script for SmartTQDM functionality
"""

import time
import random
import sys
import os

# Add the smart_tqdm package to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_basic_functionality():
    """Test basic SmartTQDM functionality"""
    print("🧪 Testing Basic Functionality")
    print("=" * 40)
    
    try:
        from smart_tqdm import smart_tqdm
        
        # Test basic iteration
        for i in smart_tqdm(range(10), desc="Basic Test"):
            time.sleep(0.1)
        
        print("✅ Basic functionality test passed")
        return True
    except Exception as e:
        print(f"❌ Basic functionality test failed: {e}")
        return False

def test_themes():
    """Test different themes"""
    print("\n🎨 Testing Themes")
    print("=" * 40)
    
    try:
        from smart_tqdm import smart_tqdm, CatTheme, RocketTheme, GamingTheme
        
        themes = [
            ("Default", None),
            ("Cat", CatTheme()),
            ("Rocket", RocketTheme()),
            ("Gaming", GamingTheme())
        ]
        
        for theme_name, theme in themes:
            print(f"Testing {theme_name} theme...")
            for i in smart_tqdm(range(5), desc=f"{theme_name} Theme", theme=theme):
                time.sleep(0.1)
        
        print("✅ Themes test passed")
        return True
    except Exception as e:
        print(f"❌ Themes test failed: {e}")
        return False

def test_animations():
    """Test different animations"""
    print("\n🌊 Testing Animations")
    print("=" * 40)
    
    try:
        from smart_tqdm import smart_tqdm, WaveAnimation, RippleAnimation, PulseAnimation
        
        animations = [
            ("Wave", WaveAnimation()),
            ("Ripple", RippleAnimation()),
            ("Pulse", PulseAnimation())
        ]
        
        for anim_name, animation in animations:
            print(f"Testing {anim_name} animation...")
            for i in smart_tqdm(range(5), desc=f"{anim_name} Animation", animation=animation):
                time.sleep(0.1)
        
        print("✅ Animations test passed")
        return True
    except Exception as e:
        print(f"❌ Animations test failed: {e}")
        return False

def test_metrics():
    """Test metrics tracking"""
    print("\n📊 Testing Metrics")
    print("=" * 40)
    
    try:
        from smart_tqdm import smart_tqdm, SmartMetrics, PerformanceStatus
        
        # Create smart metrics
        smart_metrics = SmartMetrics()
        
        # Test metrics update
        for i in smart_tqdm(range(10), desc="Metrics Test"):
            loss = random.uniform(0.1, 1.0)
            accuracy = random.uniform(0.5, 0.9)
            
            # Update metrics
            status = smart_metrics.update(
                {"loss": loss, "accuracy": accuracy},
                progress=i/10
            )
            
            # Update progress bar
            pbar.set_postfix(loss=f"{loss:.3f}", accuracy=f"{accuracy:.3f}")
            time.sleep(0.1)
        
        # Get performance report
        report = smart_metrics.get_performance_report()
        print(f"✅ Metrics test passed - Generated report with {len(report['summary'])} metrics")
        return True
    except Exception as e:
        print(f"❌ Metrics test failed: {e}")
        return False

def test_custom_theme():
    """Test custom theme creation"""
    print("\n🎨 Testing Custom Theme")
    print("=" * 40)
    
    try:
        from smart_tqdm import smart_tqdm, CustomTheme, PerformanceStatus
        
        # Create custom emoji mappings
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
        
        # Test custom theme
        for i in smart_tqdm(range(5), desc="Custom Theme Test", theme=custom_theme):
            loss = random.uniform(0.1, 1.0)
            accuracy = random.uniform(0.5, 0.9)
            pbar.set_postfix(loss=f"{loss:.3f}", accuracy=f"{accuracy:.3f}")
            time.sleep(0.1)
        
        print("✅ Custom theme test passed")
        return True
    except Exception as e:
        print(f"❌ Custom theme test failed: {e}")
        return False

def test_context_manager():
    """Test context manager usage"""
    print("\n🔧 Testing Context Manager")
    print("=" * 40)
    
    try:
        from smart_tqdm import smart_progress, CatTheme, WaveAnimation
        
        with smart_progress(
            range(5), 
            desc="Context Manager Test",
            theme=CatTheme(),
            animation=WaveAnimation()
        ) as pbar:
            for i in pbar:
                loss = random.uniform(0.1, 1.0)
                accuracy = random.uniform(0.5, 0.9)
                pbar.set_postfix(loss=f"{loss:.3f}", accuracy=f"{accuracy:.3f}")
                time.sleep(0.1)
        
        print("✅ Context manager test passed")
        return True
    except Exception as e:
        print(f"❌ Context manager test failed: {e}")
        return False

def test_exporters():
    """Test export functionality"""
    print("\n📈 Testing Exporters")
    print("=" * 40)
    
    try:
        from smart_tqdm import smart_tqdm, ReportGenerator
        
        # Create report generator
        report_gen = ReportGenerator(output_dir="test_reports")
        
        # Simulate training
        for i in smart_tqdm(range(10), desc="Export Test"):
            loss = random.uniform(0.1, 1.0)
            accuracy = random.uniform(0.5, 0.9)
            pbar.set_postfix(loss=f"{loss:.3f}", accuracy=f"{accuracy:.3f}")
            time.sleep(0.1)
        
        # Generate report
        report_path = report_gen.generate_report(pbar)
        print(f"✅ Export test passed - Report generated: {report_path}")
        return True
    except Exception as e:
        print(f"❌ Export test failed: {e}")
        return False

def run_all_tests():
    """Run all tests"""
    print("🚀 SmartTQDM Test Suite")
    print("=" * 60)
    
    tests = [
        test_basic_functionality,
        test_themes,
        test_animations,
        test_metrics,
        test_custom_theme,
        test_context_manager,
        test_exporters
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print(f"\n📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! SmartTQDM is working correctly.")
        return True
    else:
        print("⚠️  Some tests failed. Please check the implementation.")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1) 