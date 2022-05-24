import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="eightbitdo_zero2",
    version="0.1.3",
    author="KawamataRyo",
    author_email="ba068082@gmail.com",
    license="MIT",
    description="Python code to use thev 8bitdo zero2 controller with a Raspberry Pi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kawamataryo/8bitdo_zero2",
    keywords=["8bitdo", "raspberry Pi"],
    project_urls={
        "Homepage": "https://github.com/kawamataryo/8bitdo_zero2",
        "Bug Tracker": "https://github.com/kawamataryo/8bitdo_zero2/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['eightbitdo_zero2'],
    python_requires=">=3.6",
)
