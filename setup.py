import setuptools
import coincall
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-coincall",
    version=coincall.__version__,
    author="coincall_api",
    author_email="api@coincall.com",
    description="Python SDK for Coincall",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://docs.coincall.com",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "importlib-metadata",
        "httpx[http2]",
        "keyring",
        "requests",
        "Twisted",
        "pyOpenSSL"
    ]
)