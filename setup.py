from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="fig2pen",
    version="0.4.0",
    author="Nicolas Kruchten",
    packages=["fig2pen"],
    license="MIT",
    project_urls={"Github": "https://github.com/nicolaskruchten/fig2pen"},
    description="A utility to make CodePens out of Plotly.py figures",
    long_description=readme(),
    long_description_content_type="text/markdown",
    install_requires=[],
)
