from setuptools import setup, find_packages

setup(
    name="soundswallower",
    license="MIT",
    version="0.2",
    description="An even smaller speech recognizer",
    author="David Huggins-Daines",
    author_email="dhdaines@gmail.com",
    url="https://github.com/ReadAlongs/SoundSwallower",
    packages=["soundswallower"],
    requires=["numpy"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "soundswallower = soundswallower.cli:main",
        ],
    },
)
