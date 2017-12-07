from setuptools import setup


setup(
    name='print_progress',
    author='Kevin Sedlaczek',
    author_email='kevin.sedlaczek@tu-dortmund.de',
    description='Print a progress bar for iterations and loops',
    license='MIT',
    version='0.0.1',
    packages=['print_progress'],
    # install_requires=['sys'],
    entry_points={
                'console_scripts': [
                    'print_progress=print_progress.__main__:main'
                ]
    }
)
