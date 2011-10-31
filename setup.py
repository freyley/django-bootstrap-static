from setuptools import setup
import subprocess
import os.path

long_description = (open('README.rst').read() + 
                    open('CHANGES.rst').read() +
                    open('TODO.rst').read())

setup(
    name='django-boostrap-static',
    version='0.0.1',
    description='Boostrap django projects with twitter-bootstrap, requirejs, resig microtemplating, etc',
    author='LoFi Art',
    author_email='chris@lofiart.com',
    long_description=long_description,
    url='',
    packages=['bootstrap_static'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
    #test_suite='tests.runtests.runtests',
    package_data={
        'boostrap_static': [
            'static/js/*.js',
            'static/css/*.css',
            '__init__.py',
        ]
    },
)
