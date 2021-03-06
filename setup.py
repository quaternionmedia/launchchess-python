import setuptools
from launchchess._version import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

INSTALL_REQUIRES = [
    'python-chess',
    'python-rtmidi',
]
setuptools.setup(
    name="launchchess",
    packages=['launchchess'],
    version=__version__,
    author="Quaternion Media",
    author_email="info@quaternion.media",
    license='MIT',
    description="Play chess on a Launchpad",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/quaternionmedia/launchchess-python",
    install_requires=INSTALL_REQUIRES,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        "console_scripts": [
            "launchchess=launchchess.launchchess:main",
        ]
    },
)
