import os

from setuptools import setup


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

setup(
    name='imgur-uploader',
    version='0.1.0',
    description='A simple command line client for uploading files to Imgur.',
    long_description=read('README.md'),
    url='https://github.com/atbaker/imgur-uploader',
    license='MIT',
    author='Andrew Tork Baker',
    author_email='andrew@atbaker.me',
    py_modules=['imgur_uploader'],
    include_package_data=True,
    install_requires=[
        'click',
        'imgurpython'
    ],
    entry_points='''
        [console_scripts]
        imgur-uploader=imgur_uploader:upload_gif
    ''',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Utilities',
    ]
)
