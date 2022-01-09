import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pynq_cdma",
    version="0.1.0",
    author="NCJ",
    author_email="me@ncj.wiki",
    description="PYNQ Driver for Xilinx Central Direct Memory Access IP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iamNCJ/PYNQ-CDMA-Driver",
    packages=setuptools.find_packages(),
    install_requires=[
       'pynq>=2.6'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.6',
)
