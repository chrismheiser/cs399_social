from setuptools import setup, find_packages


setup(
    name='cs399_Social',
    version='0.1.0',
    description='CS399 Social',
    long_description=open('README.rst').read(),
    keywords=[
        'class',
        'django',
        'nau'
    ],
    author='Group',
    url='https://github.com/cmh553/cs399_social',
    packages=find_packages(),
    license='UNLICENSE',
    install_requires=open('requirements.txt').readlines(),
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)
