from setuptools import setup, find_packages

version = "1.2.3"


setup(
    name="dlchord",
    version=version,
    description="chord library",
    install_requires=["numpy"],
    author="anime-song",
    url="https://github.com/anime-song/DL-Chord",
    keywords='music chord',
    license="MIT",
    packages=find_packages(exclude=['test']),
    include_package_data=True,
    test_suite='./test',
)
