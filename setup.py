import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(name='multibarplot',
      version='0.1',
      description='Helper function to plot multiple barplots using Matplotlib',
      long_description=long_description,
      long_description_content_type='text/markdown',
      keywords=['machine learning', 'plotting', 'visualization', 'matplotlib'],
      author='Matthias Jakobs',
      author_email='matthias.jakobs@tu-dortmund.de',
      url='https://github.com/MatthiasJakobs/multibarplot',
      license='GNU GPLv3',
      package_dir={"": "src"},
      packages=setuptools.find_packages(),
      python_requires='>=3.5',)
