"""
Setup script for tqdm++ package
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "tqdm++ - Enhanced Progress Bar with Intelligent Emoji Feedback"

setup(
    name="tqdmpp",
    version="2.0.0",
    author="IEEE Research Project",
    author_email="research@ieee.org",
    description="Enhanced progress bar with intelligent emoji feedback for neural network training",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/ieee-research/tqdmpp",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Monitoring",
    ],
    python_requires=">=3.7",
    install_requires=[
        # No external dependencies - uses only Python standard library
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "pytest-cov>=2.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "mypy>=0.950",
        ],
    },
    keywords=[
        "progress-bar",
        "emoji",
        "neural-network",
        "machine-learning",
        "deep-learning",
        "training",
        "monitoring",
        "metrics",
        "accuracy",
        "loss",
        "trend-detection",
        "intelligent-feedback",
        "stateful",
        "ieee",
        "research"
    ],
    project_urls={
        "Bug Reports": "https://github.com/ieee-research/tqdmpp/issues",
        "Source": "https://github.com/ieee-research/tqdmpp",
        "Documentation": "https://github.com/ieee-research/tqdmpp/blob/main/README.md",
    },
    include_package_data=True,
    zip_safe=False,
) 