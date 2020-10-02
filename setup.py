import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jobkey",
    version="0.1",
    author="Matt Mays",
    author_email="matt@cosmodrome.com",
    description="Performs some basic Natural Language Processing to pull keywords from Job Descriptions that can be used in a resume.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mattmays/jobkey/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)