from setuptools import setup

setup(
    name='schema4deep',
    version='0.0.1',
    description='DEEP applications metadata validator',
    url='https://github.com/deephdc/json-schema4deep',
    author='Pablo Orviz',
    author_email='orviz@ifca.unican.es',
    license='Apache 2.0',
    packages=['schema4deep'],
    install_requires=[
        'jsonschema>=3.0.0b3',
        'rfc3987>=1.3.8',
        'simplejson>=3.16.0'
    ],
    zip_safe=False,
    entry_points ={
        'console_scripts': ['deep-app-schema-validator=schema4deep.main:validate']
    }
)
