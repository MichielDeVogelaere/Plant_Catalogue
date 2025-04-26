from setuptools import setup, find_packages

setup(
    name="plant_catalogue",
    version="0.1.0",
    description="A command-line application to manage your plant collection",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'qrcode>=7.3.1',
        'opencv-python>=4.8.0',
        'pillow>=10.0.0',
        'tabulate>=0.9.0',
        'python-dateutil>=2.8.2',
        'numpy>=1.24.0',
        'configparser>=5.3.0',
    ],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'plant-catalogue=main:main',
        ],
    },
) 