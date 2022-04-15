from setuptools import setup
import datamuse_cli.__main__ as m

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as file:
    requires = [line.strip() for line in file.readlines()]

VERSION = m.__version__
DESCRIPTION = "A command line interface that displays results from the Datamuse API"

setup(
    name="datamuse-cli",
    version=VERSION,
    url="https://github.com/agmmnn/datamuse-cli",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="agmmnn",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Utilities",
    ],
    packages=["datamuse_cli"],
    install_requires=requires,
    include_package_data=True,
    package_data={"datamuse_cli": ["datamuse_cli/*"]},
    python_requires=">=3.6.3",
    entry_points={"console_scripts": ["datamuse = datamuse_cli.__main__:main"]},
)
