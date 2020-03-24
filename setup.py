from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='nnir',
    version='1.0.0',
    description='User-friendly machine learning tool for image classification',
    long_description=long_description,
    author='Nesac128',
    author_email='ml.learner.8359@gmail.com',
    long_description_content_type="text/markdown",
    url="https://github.com/Nesac128/NNIR",
    install_requires=['tensorflow==1.9.0', 'Pillow==6.2.0', 'scikit-learn==0.19.1',
                      'numpy==1.14.5', 'opencv-python==3.4.0.12', 'pandas==0.22.0',
                      'click==6.7', 'scipy'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL-2.0 License",
        "Operating System :: POSIX",
        "Programming Language :: Python"
    )
)
