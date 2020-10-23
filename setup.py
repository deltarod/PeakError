import setuptools
import numpy

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PeakError",
    version="0.0.1",
    author="Tristan Miller",
    author_email="Tristan.Miller@nau.edu",
    description="A Python binding for PeakError",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/deltarod/PeakError/",
    install_requires=['numpy', 'pandas'],
    packages=['PeakError'],
    extras_require={
        'test': ['pytest']
    },
    ext_modules=[setuptools.Extension('PeakError/PeakErrorInterface',
                                      ['src/interface.c', 'src/PeakError.c'],
                                      include_dirs=[numpy.get_include()])],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: C",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    python_requires='>=3.6',
)
