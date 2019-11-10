from setuptools import setup

setup(
    name='detrapezer',
    version='0.0.1',
    packages=['app'],
    entry_points={
        'console_scripts': [
            'detrapezer = app.main:main'
        ]
    }
)
