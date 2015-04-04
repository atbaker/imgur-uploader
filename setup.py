from setuptools import setup

setup(
    name='imgur-uploader',
    version='0.1',
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
)
