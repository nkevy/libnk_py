from setuptools import setup

setup(
	dependency_links=['https://github.com/nkevy/libnk_py.git#egg=package-1.0']
	version = '1.0',
	name='libnk_py',
	description='library of python modudles',
	url='https://github.com/nkevy/libnk_py.git',
	author='noah kevy',
	license='nk',
	author_email='yvek.com@gmail.com',
	packages = ['Econ'],
	install_requires=['os'],
	zip_safe=False)
