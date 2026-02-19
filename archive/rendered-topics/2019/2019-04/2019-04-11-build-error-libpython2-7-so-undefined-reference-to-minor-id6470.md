---
topic_id: 6470
title: "Build Error Libpython2 7 So Undefined Reference To Minor"
date: 2019-04-11
url: https://discourse.slicer.org/t/6470
---

# Build Error:libpython2.7.so: undefined reference to `minor

**Topic ID**: 6470
**Date**: 2019-04-11
**URL**: https://discourse.slicer.org/t/build-error-libpython2-7-so-undefined-reference-to-minor/6470

---

## Post #1 by @Ranglage (2019-04-11 14:01 UTC)

<p>When I build the latest Slicer source from Github<br>
I got these errors:<br>
[ 43%] Linking C shared library …/…/…/lib/python2.7/lib-dynload/_hashlib.so<br>
[ 44%] Built target extension_hashlib<br>
[ 44%] Linking C shared library …/…/…/lib/python2.7/lib-dynload/_ssl.so<br>
[ 45%] Built target extension_ssl<br>
[ 45%] Built target extension_zlib<br>
[ 91%] Built target libpython-shared<br>
[ 97%] Built target pgen<br>
[ 97%] Linking C executable …/…/bin/python<br>
Creating ‘bin/./Modules/Setup.local’<br>
/usr/bin/ld: …/…/lib/libpython2.7.so: undefined reference to <code>minor' /usr/bin/ld: ../../lib/libpython2.7.so: undefined reference to</code>major’<br>
/usr/bin/ld: …/…/lib/libpython2.7.so: undefined reference to `makedev’<br>
collect2: error: ld returned 1 exit status<br>
make[5]: *** [CMakeBuild/python/CMakeFiles/python.dir/build.make:92: bin/python] Error 1<br>
make[4]: *** [CMakeFiles/Makefile2:4311: CMakeBuild/python/CMakeFiles/python.dir/all] Error 2<br>
make[3]: *** [Makefile:141: all] Error 2<br>
make[2]: *** [CMakeFiles/python.dir/build.make:119: python-prefix/src/python-stamp/python-build] Error 2<br>
make[1]: *** [CMakeFiles/Makefile2:1431: CMakeFiles/python.dir/all] Error 2<br>
make: *** [Makefile:95: all] Error 2</p>
<p>OS:Ubuntu18.10<br>
QT:5.12.2<br>
Cmake:3.14.1</p>

---

## Post #2 by @jcfr (2019-04-11 14:38 UTC)

<p>Thanks for reporting the problem.</p>
<p>Two approaches to move forward:</p>
<p>(1) build <a href="https://github.com/python-cmake-buildsystem/python-cmake-buildsystem" rel="nofollow noopener">https://github.com/python-cmake-buildsystem/python-cmake-buildsystem</a> specifying options <code>-DPYTHON_VERSION:STRING=2.7.15</code> and <code>-DBUILD_LIBPYTHON_SHARED:BOOL=1</code> and report issue in the associated tracker.</p>
<p>(2) Waiting this is addressed, you could also try building the branch <code>python3-support</code> ? See <a href="https://github.com/Slicer/Slicer/pull/1118" rel="nofollow noopener">https://github.com/Slicer/Slicer/pull/1118</a></p>
<p>Since we will very soon switch to Python3 (most likely today), testing this would also be  helpful.</p>

---
