import setuptools

setuptools.setup(
    name='wsdd',
    version='1.1',
    author='Steffen Christgau',
    description="Web Service Discovery host daemon",
    packages=setuptools.find_packages(),
    scripts=["src/wsdd.py"],
    license='MIT',
    platforms="any",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: No Input/Output (Daemon)",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
    ],
    url='https://github.com/freenas/wsdd'
)
