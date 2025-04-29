from setuptools import setup, find_packages

setup(
    name="voidtrack",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "colorama",
        "scapy",
        "prettytable"
    ],
    entry_points={
        "console_scripts": [
            "voidtrack=voidtrack.cli:main"
        ]
    }
)