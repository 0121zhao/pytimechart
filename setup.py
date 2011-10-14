#!/usr/bin/env python
# Installs pyTimechart using setuptools
# Run:
#     python setup.py install
# to install the package from the source archive.

import os, sys
from setuptools import setup, find_packages

# get version from source code
version = [
    (line.split('=')[1]).strip().strip('"').strip("'")
    for line in open(os.path.join('timechart', 'window.py'))
    if line.startswith( '__version__' )
][0]

# get descriptions from documentation
DOCLINES = {"":[]}
current_part = ""
for line in open(os.path.join('docs',os.path.join('sources', 'index.rst'))):
    if line.startswith(".. DESC"):
        current_part = line[7:].strip()
        DOCLINES[current_part] = []
    else:
        DOCLINES[current_part].append(line.strip())


if __name__ == "__main__":
    # docs are only supposed to be generated by a few, so dont make it a hard dependancy
    if "build_sphinx" in sys.argv or "upload_sphinx" in sys.argv:
        extraArguments = {'setup_requires' : 'sphinx-pypi-upload>=0.2'}
    else:
        extraArguments = {}
    ### Now the actual set up call
    setup (
        name = DOCLINES["title"][1],
        classifiers = [ c.strip() for c in """\
                License :: OSI Approved :: BSD License
                Programming Language :: Python
                Topic :: Software Development :: Libraries :: Python Modules
        	Operating System :: Microsoft :: Windows
        	Operating System :: OS Independent
        	Operating System :: POSIX
        	Operating System :: Unix
                Intended Audience :: Developers
		""".splitlines() if len(c.strip()) > 0],
        keywords = 'gui,ftrace,perf,trace-event',
        version = version,
        url = "http://gitorious.org/pytimechart",
        download_url = "http://gitorious.org/pytimechart",
        description = DOCLINES["shortdesc"][1],
        long_description = '\n'.join(DOCLINES["longdesc"][1:]),
        author = "Pierre Tardy",
        author_email = "tardyp@gmail.com",
        install_requires = [
            'Chaco >= 3.0', # you should install that via distro rather than pypi..
            # 'pyliblzma >= 0.5' # not really mandatory
        ],
        license = "BSD",
        platforms = ["Windows", "Linux", "Mac OS-X", # actually did not manage to make it work on osx because of Traits..
                     "Unix", "Solaris"],
        namespace_packages = [
        'timechart',
        'timechart.plugins',
        'timechart.backends',
        ],
        packages = find_packages(exclude = [
        'examples',
        ]),
        package_data = {
            '': ['images/*'],
            },

        include_package_data = True,
        options = {
            'sdist':{
                'force_manifest':1,
                'formats':['gztar','zip'],},
        },
        zip_safe=False,
        entry_points = {
            'gui_scripts': [
                'pytimechart=timechart.timechart:main',
            ],
        },
        **extraArguments
    )

