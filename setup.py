from setuptools import setup, find_packages


def readme():
    with open("README.md", 'r') as f:
        return f.read()


setup(
    name="separationSheetGenerator",
    description="Generates separation sheets " +
    "for use during the accessioning process " +
    "at the University of Chicago Special Collections Research Center.",
    version="0.0.1",
    long_description=readme(),
    author="Brian Balsamo",
    author_email="balsamo@uchicago.edu",
    packages=find_packages(
        exclude=[
        ]
    ),
    include_package_data=True,
    install_requires=[
        'Pillow',
        'Jinja2',
        'pyBarcode'
    ]
)
