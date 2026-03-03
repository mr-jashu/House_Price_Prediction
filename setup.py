from setuptools import setup, find_packages

setup(
    name='HousePricePrediction',
    version='0.0.1',
    author='Jaswanth',
    author_email='peddadajaswanth123@email.com',
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