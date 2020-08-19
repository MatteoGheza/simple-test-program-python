import setuptools
import simpletestprogram

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=simpletestprogram.__productname__,
    version=simpletestprogram.__version__,
    author=simpletestprogram.__author__,
    author_email=simpletestprogram.__author_email__,
    description=simpletestprogram.__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=simpletestprogram.__homepage__,
    packages=setuptools.find_packages(),
    install_requires=[line.strip() for line in open("requirements.txt").readlines()],
    scripts = ['bin/simpletestprogram', 'bin/simpletestprogram.bat'],
    package_data={
        "simpletestprogram": ["res/*.*"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL3 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.3',
)