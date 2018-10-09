import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='RaiderFetch',
    version='1.0',
    description='A python3 library for getting information about the team',
    url='https://github.com/frc5024/RaiderFetch',
    author='Evan Pratten',
    author_email='ewpratten@gmail.com',
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=['requests', 'feedparser'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
    ),
)