from setuptools import setup

setup(name='print_progress',
      version='0.1',
      description='Print a progress bar for iterations and loops',
      url='http://github.com/KevSed/features_from_phs',
      author='Kevin Sedlaczek',
      author_email='kevin.sedlaczek@tu-dortmund.de',
      license='GNU',
      packages=['print_progress'],
      install_requires=[
              'sys'],
      zip_safe=False)