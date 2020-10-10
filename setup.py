import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Koshur-Recog-murtaza",  # Replace with your own username
    version="0.0.1",
    author="Murtaza, Wajid",
    author_email="myemail@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KoshurNizam/KoshurRecognition",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License ::  GPL-3.0 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)