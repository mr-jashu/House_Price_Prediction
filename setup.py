from setuptools import setup, find_packages

setup(
    name='HousePricePrediction',
    version='0.0.1',
    author='Your Name',
    author_email='your@email.com',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'xgboost',
        'matplotlib',
        'seaborn',
        'streamlit'
    ]
)