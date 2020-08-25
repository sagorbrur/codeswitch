import codecs
import setuptools


setuptools.setup(
    name="codeswitch",
    version="1.1",
    author="Sagor Sarker",
    author_email="sagorhem3532@gmail.com",
    description="Code Switch is a NLP tool can use for language identification, pos tagging, name entity recognition, sentiment analysis of code mixed data.",
    long_description=codecs.open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sagorbrur/codeswitch",
    license="MIT",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    install_requires=[
        "transformers",
    ],
)
