#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import (
    setup,
    find_packages,
)

extras_require = {
    "test": [
        "hypothesis>=4.18.0,<5",
        "pytest>=6.2.5,<7",
        "pytest-xdist",
        "coverage",
        "tox==3.25.0",
    ],
    "lint": [
        "flake8==3.7.9",
        "isort>=4.2.15,<5",
        "mypy==0.910",
        "pydocstyle>=5.0.0,<6",
        "black>=22,<23",
    ],
    "doc": [
        "sphinx>=5.0.0",
        "sphinx_rtd_theme>=1.0.0",
        "towncrier>=21,<22",
    ],
    "dev": [
        "bumpversion>=0.5.3,<1",
        "pytest-watch>=4.1.0,<5",
        "wheel",
        "twine",
        "ipython",
    ],
}

extras_require["dev"] = (
    extras_require["dev"]
    + extras_require["test"]
    + extras_require["lint"]
    + extras_require["doc"]
)


with open("./README.md") as readme:
    long_description = readme.read()


setup(
    name="eth-account",
    # *IMPORTANT*: Don't manually change the version here. Use `make bump`, as described in readme
    version="0.8.0",
    description="""eth-account: Sign Ethereum transactions and messages with local private keys""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="The Ethereum Foundation",
    author_email="snakecharmers@ethereum.org",
    url="https://github.com/ethereum/eth-account",
    include_package_data=True,
    package_data={
        "eth_account": [
            "py.typed",
            "hdaccount/wordlist/*.txt",
        ]
    },
    install_requires=[
        "bitarray>=2.4.0,<3",
        "eth-abi>=4.0.0-b.2",
        "eth-keyfile>=0.6.0,<0.7.0",
        "eth-keys>=0.4.0,<0.5",
        "eth-rlp>=0.3.0,<1",
        "eth-utils>=2.0.0,<3",
        "hexbytes>=0.1.0,<1",
        "rlp>=1.0.0,<4",
    ],
    python_requires=">=3.6, <4",
    extras_require=extras_require,
    py_modules=["eth_account"],
    license="MIT",
    zip_safe=False,
    keywords="ethereum",
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
