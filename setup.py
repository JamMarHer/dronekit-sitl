#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='dronekit_sitl',
      version='2.0.0',
      description='Runs SITL as part of DroneKit.',
      author='Tim Ryan',
      author_email='tim@3drobotics.com',
      url='https://github.com/tcr3dr/dronekit-sitl-runner/',
      entry_points={
          'console_scripts': [
              'dronekit-sitl = dronekit.sitl.__init__:main'
          ]
      },
      packages = ['dronekit', 'dronekit.sitl'],
      namespace_packages = ['dronekit']
      )
