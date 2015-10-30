from distutils.core import setup

with open("README.md") as readme:
    README_TEXT = readme.read()

setup(
    name="tnsmaster",
    version="0.1.0",
    description="Toolset for mastering tnsnames",
    long_description=README_TEXT,
    author="Dirk Fuchs",
    author_email="somewhere@over-the-rain.bow",
    url="https://github.com/difu/tnsmaster",
    packages=["tnsnames"],
    data_files=[("tests", ["__init__.py", "test_serviceFinder.py",
                           "testFiles/tnsnames.ora"])],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Topic :: Database",
        "Topic :: Utilities"
    ],
    license="MIT"
)
