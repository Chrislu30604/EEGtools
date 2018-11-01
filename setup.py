from setuptools import setup

require = ['numpy', 'scikit-learn']

setup(
    name='SSVEPbox',
    version='1.0',
    description='This is SSVEP for many algorithm',
    url='https://github.com/Chrislu30604/ssvepbox.git',
    author='chrislu30604',
    author_email='chrislu30604@gmail.com',
    include_package_data=True,
    install_requires=require
)
# install_requires=[] sklearn