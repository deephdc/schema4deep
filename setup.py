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
    zip_safe=False,
    entry_points ={
        'console_scripts': ['deep-app-schema-validator=schema4deep.main:validate']
    }
)
