import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.LLAW33012021S2ALRM1',
      version='',
      description=(''),
      long_description="### Civil Internal Referral System<br>\r\n---\r\n<p>This application was created to consolidate the process of client referral<br>\r\ninto a a single, more efficient process. The application will ask the user for<br>\r\ntheir clients' age, gender, region, general location and what areas they<br>\r\nrequire support in. The application will then produce a list of applicable<br>\r\nsupport services tailored to the clients needs. This list can be downloaded,<br>\r\nprinted and emailed as necessary to provide the greatest ease of use to the<br>\r\nclient.</p>\r\n\r\n<p>The Civil Internal Referral System was created for, and in collaboration with,<br>\r\nthe Aboriginal Legal Rights Movement. ALRM is a public not-for-profit<br>\r\norganisation focused on protecting the interests and rights of Aboriginal and<br>\r\nTorres Srait Islander (ATSI) people.</p>\r\n\r\n<p><strong>ABN</strong>: 32 942 723 464</p>\r\n\r\n#### Authors:\r\n---\r\nAmy Blight<br>\r\nAmani Obaida<br>\r\nBradely Hawkes<br>\r\nBrayden Tansell<br>\r\nEliza Page",
      long_description_content_type='text/markdown',
      author='Brayden Tansell',
      author_email='tans0013@flinders.edu.au',
      license='',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/LLAW33012021S2ALRM1/', package='docassemble.LLAW33012021S2ALRM1'),
     )

