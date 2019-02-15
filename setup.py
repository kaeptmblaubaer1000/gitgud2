# -*- encoding: utf-8 -*-

try:
    chr = unichr
except NameError:
    pass

from io import open
from setuptools import setup, Extension, find_packages

fp = open("README.md", "rt", encoding="utf-8")
long_description = fp.read()
fp.close()

setup(name='gitgud2',
      version='2.0',
      author='Kaeptm Blaubaer',
      author_email=__import__('base64').b64decode(''.join(map(lambda c1, c2: chr(c1 ^ c2), *zip((17611, 17578), (8271, 8317), (33432, 33502), (15455, 15411), (64937, 64970), (58915, 58987), (61898, 61848), (49756, 49704), (27519, 27430), (12302, 12387), (63944, 63920), (3715, 3819), (51093, 51185), (56723, 56772), (276, 350), (58377, 58465), (34908, 34822), (29984, 30072), (13399, 13342), (41606, 41726), (4009, 4068), (2925, 2857), (3335, 3398), (1206, 1217), (49965, 50044), (28390, 28321), (55327, 55419), (3806, 3754), (29057, 29144), (57394, 57445), (64987, 64951), (30550, 30501), (45311, 45235), (30260, 30297), (28676, 28746), (60241, 60199), (37982, 37948), (2816, 2897), (54549, 54568), (13107, 13070))))).decode("utf-8"),
      description="Git Gud - a utility for when you are told to 'get good'",
      long_description=long_description,
      long_description_content_type="text/markdown",
      license="Public domain",
      url="https://github.com/kaeptmblaubaer1000/gitgud2",
      package_dir={'': 'src'},
      packages=['gitgud'],
      provides=['gitgud'],
      entry_points={
          "console_scripts": [
              "git-gud=gitgud.gitgud:git.gud",
              "git-job=gitgud.gitgud:git.job",
              "git-rekt=gitgud.gitgud:git.rekt",
              "git-spooked=gitgud.gitgud:git.spooked",
              "git-money=gitgud.gitgud:git.money",
          ],
      },

      install_requires=['argparse', 'pyfiglet'],
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Environment :: Console",
          "Intended Audience :: Developers",
          "License :: Public Domain",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 3",
          # TODO: Test supported versions and add them as classifiers
      ],
      zip_safe=True,
      )
