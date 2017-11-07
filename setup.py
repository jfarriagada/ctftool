from setuptools import find_packages, setup

setup(
    name='ctf-tool',
    version='0.0.1',
    author='Jose Francisco Arriagada A',
    author_email='jfarriagada91@gmail.com',
    description=('A simple capture the flag tool.'),
    long_description='',
    license='BSD',
    keywords='ctc capture the flag tool',
    url='',
    packages=find_packages(),
    package_data={
        'ctf-tool': ['*.txt']
    },
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.x',
        'Topic :: Utilities'
    ]
)
