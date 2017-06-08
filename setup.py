from setuptools import setup, find_packages

setup(name='ekphrasis',
      version='0.1.1',
      description='Text processing tool, geared towards text from social networks, such as Twitter or Facebook. Ekphrasis performs tokenization, word normalization, word segmentation (for splitting hashtags) and spell correction.',
      url='https://github.com/cbaziotis/ekphrasis',
      author='Christos Baziotis',
      author_email='christos.baziotis@gmail.com',
      license='MIT',
      packages=find_packages(exclude=['docs', 'tests*', 'analysis']),
      install_requires=["matplotlib", "numpy", "pandas", "termcolor", "textacy", "tqdm", "colorama"],
      include_package_data=True
      )