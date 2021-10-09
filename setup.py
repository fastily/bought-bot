import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bought_bot",
    version="0.0.1",
    author="Fastily",
    author_email="fastily@users.noreply.github.com",
    description="A bot for automatically buying things on websites",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fastily/bought-bot",
    project_urls={
        "Bug Tracker": "https://github.com/fastily/bought-bot/issues",
    },
    include_package_data=True,
    packages=setuptools.find_packages(include=["bought_bot"]),
    install_requires=["selenium"],
    entry_points={
        'console_scripts': [
            'bought_bot = bought_bot.__main__:_main'
        ]
    },
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9"
)
