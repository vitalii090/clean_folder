from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1.0',
    description='Sort and clean folders',
    author='Vitalii',
    url='https://github.com/vitalii090/clean_folder.git',
    packages=find_namespace_packages(),
    entry_points={
        'console_scripts': [
            'clean-folder = clean_folder.clean:main'
        ]
    }
)
