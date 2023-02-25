"""
https://packaging.python.org/tutorials/packaging-projects/
Markdown guide: https://www.markdownguide.org/cheat-sheet/
"""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="latestearthquake-indonesia v.1",
    version="0.9",
    author="Nur Arif",
    author_email="nurarif0151@gmail.com",
    description="This package will get the latest earthquake from BMKG | Meteorological, Climatological, and "
                "Geophysical Agency",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nurarif151/latest-indonesia-earthquake",
    project_urls={
        "Website": "https://teollo.id",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable"
    ],
    # package_dir={"": "src"},
    # packages=setuptools.find_packages(where="src"),
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)