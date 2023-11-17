from setuptools import setup, find_packages

setup(
    name='Sorbet',
    version='0.1.0',
    packages=find_packages(),
    author='Himeji',
    author_email='himeji@proton.me',
    description='Improved logging for Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/HimejiDev/Sorbet',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT',
        'Programming Language :: Python :: 3',
        # Add more classifiers as needed
    ],
    install_requires=[
        # List dependencies here
    ],
)