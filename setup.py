from setuptools import setup, find_packages
from codecs import open
from os import path

from jupyter_packaging import (
    create_cmdclass, install_npm, ensure_targets,
    combine_commands, ensure_python, get_version
)

pjoin = path.join

ensure_python(('2.7', '>=3.3'))

name = 'jupyterlab_iframe'
here = path.abspath(path.dirname(__file__))
version = get_version(pjoin(here, name, '_version.py'))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    requires = f.read().split()


data_spec = [
    # Lab extension installed by default:
    ('share/jupyter/lab/extensions',
     'lab-dist',
     'jupyterlab_iframe-*.tgz'),
    # Config to enable server extension by default:
    ('etc/jupyter',
     'jupyter-config',
     '**/*.json'),
]


cmdclass = create_cmdclass('js', data_files_spec=data_spec)
cmdclass['js'] = combine_commands(
    install_npm(here, build_cmd='build:all'),
    ensure_targets([
        pjoin(here, 'lib', 'index.js'),
        pjoin(here, 'style', 'index.css')
    ]),
)


setup(
    name=name,
    version=version,
    description='IFrame widgets for JupyterLab',
    long_description=long_description,
    url='https://github.com/timkpaine/jupyterlab_iframe',
    author='Tim Paine',
    author_email='t.paine154@gmail.com',
    license='Apache 2.0',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Framework :: Jupyter',
    ],

    cmdclass=cmdclass,

    keywords='jupyter jupyterlab',
    packages=find_packages(exclude=['tests', ]),
    install_requires=requires,
    extras_require={
        'dev': ['pytest', 'pytest-cov', 'pylint', 'flake8', 'bumpversion', 'autopep8', 'mock']
    },
    include_package_data=True,
    zip_safe=False,

)
