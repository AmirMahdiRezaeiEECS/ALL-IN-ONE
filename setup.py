from setuptools import setup, find_packages

setup(
    name="all_in_one_ai",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "torch",
        "numpy",
        "pandas",
    ],
)
