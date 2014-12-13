import setuptools

setuptools.setup(
    name="plainstream",
    version="0.1.0",
    url="https://github.com/jimmycallin/plainstream",

    author="Jimmy Callin",
    author_email="jimmy.callin@gmail.com",

    description="Do you need a lot of text for whatever reason? Plainstream provides you with a plain text stream coming directly from Wikipedia in any of its supporting languages.",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],

    scripts=['bin/plainstream']
)
