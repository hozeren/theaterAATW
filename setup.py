from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="theateraatw",
    version="0.0.1",
    author="Hüsamettin Deniz Özeren",
    author_email="denizozeren614@gmail.com",
    description="Twitterbot for TheaterAATW",
    url="https://github.com/hozeren/theaterAATW",
    project_urls={
        "Bug Tracker": "https://github.com/hozeren/theaterAATW/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3.0",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'twython',
        'pandas',
        'nltk'
    ],
    packages=find_packages(include=['theaterAATW', 'theaterAATW.*']),
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'theateraatw = theaterAATW.main:main'],
            },
    tests_require=['pytest'],
    setup_requires=['pytest-runner', 'flake8'],
    test_suite='theaterAATW.tests',
)