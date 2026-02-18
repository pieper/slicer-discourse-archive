# Build fails on Ubuntu 14.04

**Topic ID**: 3330
**Date**: 2018-06-28
**URL**: https://discourse.slicer.org/t/build-fails-on-ubuntu-14-04/3330

---

## Post #1 by @Lorensen (2018-06-28 17:19 UTC)

<p>%] Built target python-appdirs<br>
[ 20%] No configure step for ‘python-pyparsing’<br>
[ 20%] No build step for ‘python-pyparsing’<br>
[ 21%] Performing install step for ‘python-pyparsing’<br>
Traceback (most recent call last):<br>
File “setup.py”, line 15, in <br>
from pyparsing import <strong>version</strong> as pyparsing_version<br>
File “/home/lorensen/ProjectsGIT/Slicer-Superbuild/python-pyparsing/pyparsing.py”,<br>
line 78, in <br>
from datetime import datetime<br>
ImportError: No module named datetime<br>
make[2]: *** [python-pyparsing-prefix/src/python-pyparsing-stamp/python-pyparsing-install]<br>
Error 1<br>
make[1]: *** [CMakeFiles/python-pyparsing.dir/all] Error 2</p>

---

## Post #2 by @pieper (2018-07-02 15:19 UTC)

<p>Hi Bill - Not sure what’s up there.  I did a fresh build on ubuntu 16.04 and didn’t run into this.</p>
<p>-Steve</p>

---

## Post #3 by @brhoom (2018-07-02 15:42 UTC)

<p>I just want to note that sometimes using <strong>make -j</strong> makes a problem as some stuff depends on other stuff. I usually use <strong>make</strong>  for a few minutes until the error pass then I go back to <strong>make -j</strong></p>

---

## Post #4 by @Lorensen (2018-07-02 15:48 UTC)

<p>I updated my cmake to 10.3.1 and it builds now.</p>

---

## Post #5 by @lassoan (2018-07-02 17:13 UTC)

<p>What CMake version did you try to use before?</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Linux">Build instructions</a> require CMake 3.7-rc2 as a minimum but minimum version in the code is just set to CMake 3.5.</p>

---

## Post #6 by @Lorensen (2018-07-02 18:03 UTC)

<p>I think it was 3.7rc2. I’m pretty sure. I did try a clean build with that cmake but it also failed.</p>

---
