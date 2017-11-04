from setuptools import setup

setup(name='edge_ai',
      version='0.1.0',
      description='EdgeAI API Client',
      url='https://github.com/deep-horizon/edge_ai',
      author='Ben Whittle',
      author_email='benwhittle31@gmail.com',
      license='MIT',
      packages=['edge_ai'],
      install_requires=['requests'],
      zip_safe=False)