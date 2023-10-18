from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in resturant/__init__.py
from resturant import __version__ as version

setup(
	name="resturant",
	version=version,
	description="related to resturant",
	author="NexTash",
	author_email="support@nextash.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
