import setuptools

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
    package_dir={'': 'Python'},
    py_modules=['PeakError', 'check'],
    ext_modules=[setuptools.Extension('PeakErrorInterface', ['src/interface.c', 'src/PeakError.c'])],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)