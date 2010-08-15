from setuptools import setup, find_packages

setup(
    name='sphinx_sourcecode',
    author='Tommi Virtanen',
    author_email='tv@eagain.net',
    description='Explicit sourcecode directive for Sphinx.',
    version='0.1',
    install_requires=[
        'setuptools',
        'Sphinx >=0.6.1',
        'Pygments >=1.3.1',
        ],
    packages=find_packages(exclude=['ez_setup']),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Documentation',
        'Topic :: Documentation',
        'Topic :: System :: Installation/Setup',
        'License :: OSI Approved :: BSD License',
        ]
    )
