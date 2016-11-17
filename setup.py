from setuptools import setup
setup(
    name='polyssifier',
    packages=['polyssifier'],
    version='0.1.8',
    install_requires=[
        'mlp==0.6',
        'pandas==0.18.1',
        'scikit-learn==0.18',
        'numpy==1.11.1'],
    description='Data exploration tool for assessing optimal classification methods',
    author='Alvaro Ulloa',
    author_email='alvarouc@gmail.com',
    url='https://github.com/alvarouc/polyssifier',
    download_url='https://github.com/alvarouc/polyssifier/tarball/0.1.8',
    keywords=['classification', 'machine learning', 'data science'],
    classifiers=[],
)
