# coding=utf-8
"""
Setup for scikit-surgeryvideoutils
"""

from setuptools import setup, find_packages
import versioneer

# Get the long description
with open('README.rst') as f:
    long_description = f.read()

setup(
    name='scikit-surgeryvideoutils',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='scikit-surgeryvideoutils - Tests/demos utilities, based around opencv-contrib and PySide2',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareRepositories/SNAPPY/scikit-surgeryvideoutils',
    author='Matt Clarkson',
    author_email='m.clarkson@ucl.ac.uk',
    license='BSD-3 license',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',


        'License :: OSI Approved :: BSD License',


        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',

        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
    ],

    keywords='medical imaging',

    packages=find_packages(
        exclude=[
            'doc',
            'tests',
        ]
    ),

    install_requires=[
        'six>=1.10',
        'numpy>=1.11',
        'opencv-contrib-python>=3.4.4',
        'PySide2>=5.12.0',
        'scikit-surgeryimage>=0.1.1',
    ],

    entry_points={
        'console_scripts': [
            'sksurgeryvideolag=sksurgeryvideoutils.ui.sksurgeryvideolag_command_line:main',
            'sksurgerycharucotest=sksurgeryvideoutils.ui.sksurgerycharucotest_command_line:main',
        ],
    },
)