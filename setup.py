# """
# Flask-Remodel
# ----------------

# Adds Remodel support to Flask.

# """

from setuptools import setup, find_packages


setup(
    name='Flask-Remodel',
    version='0.1',
    url='http://github.com/linkyndy/flask-remodel',
    license='MIT',
    author='Andrei Horak',
    author_email='linkyndy@yahoo.com',
    description='Adds Remodel support to Flask',
    long_description=__doc__,
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'flask >= 0.9',
        'rethinkdb',
        'remodel',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
