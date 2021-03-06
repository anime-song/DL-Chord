from setuptools import setup, find_packages
import sys
sys.path.append("./test/")
version = "1.4.5"


setup(
    name="dlchord",
    version=version,
    description="chord library",
    install_requires=["numpy"],
    author="anime-song",
    url="https://github.com/anime-song/DL-Chord",
    keywords='music chord',
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    test_suite='test',
)
