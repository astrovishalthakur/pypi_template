import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

__version__ = "0.0.0"

REPO_NAME = "IPYNBRENDERER"
AUTHOR_NAME = "astrovishalthakur"
SRC_REPO = "IPYNBRENDERER"
AUTHOR_EMAIL = "astrovishalthakur@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small package to render ipynb files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{SRC_REPO}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{SRC_REPO}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)