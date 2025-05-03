from setuptools import setup, find_packages

setup(
    name="CurrBotmxvbe",
    version="0.1.0",
    description="Телеграм-бот для курса валют на aiogram",
    author="Mikhail",
    author_email="mitrasher.negativ@gmail.com",
    packages=find_packages(),
    python_requires=">=3.7, <3.12",
    install_requires=[
        "requests",
        "aiogram==2.23.1"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
