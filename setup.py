from setuptools import find_packages, setup

setup(
    name="module-tracker",
    version="0.0.1",
    description="a tool that tracks dependencies in project",
    install_requires=[],
    url="https://github.com/jeongukjae/module-tracker.py",
    author="Jeong Ukjae",
    author_email="jeongukjae@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(exclude=["tests"]),
)
