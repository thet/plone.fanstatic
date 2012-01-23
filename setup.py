from setuptools import setup
from setuptools import find_packages

version = '0.1'

setup(
    name='plone.fanstatic',
    version=version,
    description="Fanstatic integration into Zope2/Plone",
    long_description=open("README.rst").read(),
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
    keywords='plone fanstatic resources css javascript',
    author='Plone Foundation',
    author_email='plone-developers@lists.sourceforge.net',
    url='https://github.com/plone/plone.fanstatic',
    license='BSD',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['plone'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'fanstatic',
        'plone.transformchain',
        ],
    extras_require={'test': ['plone.app.testing']},
    entry_points={
        'z3c.autoinclude.plugin': [
            'target = plone',
            ],
        'fanstatic.libraries': [
            'plone_example = plone.fanstatic:plone_example',
            ],
        },
    )
