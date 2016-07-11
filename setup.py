from setuptools import setup

setup(
        name='redraspi',
        version='0.0.1',
        packages=['redraspi'],
        entry_points={
            'console_scripts': [
                'redraspi = redraspi.__main__:main'
            ]
        },
        )

