# Slicer FTBFS Debian testing

**Topic ID**: 2058
**Date**: 2018-02-10
**URL**: https://discourse.slicer.org/t/slicer-ftbfs-debian-testing/2058

---

## Post #1 by @gcsharp (2018-02-10 05:38 UTC)

<p>Hello slicers,<br>
Slicer FTBFS debian testing with default options.  Default settings need updating?<br>
Thanks!<br>
Greg</p>
<p>[ 46%] Performing build step for ‘DCMTK’<br>
[  0%] Building CXX object ofstd/libsrc/CMakeFiles/ofstd.dir/ofchrenc.cc.o<br>
In file included from /usr/include/c++/7/cstdint:35:0,<br>
from /home/gsharp/build/slicer-4/Slicer-build/DCMTK/ofstd/include/dcmtk/ofstd/ofstdinc.h:279,<br>
from /home/gsharp/build/slicer-4/Slicer-build/DCMTK/ofstd/include/dcmtk/ofstd/oftypes.h:74,<br>
from /home/gsharp/build/slicer-4/Slicer-build/DCMTK/ofstd/include/dcmtk/ofstd/ofcond.h:28,<br>
from /home/gsharp/build/slicer-4/Slicer-build/DCMTK/ofstd/include/dcmtk/ofstd/ofchrenc.h:28,<br>
from /home/gsharp/build/slicer-4/Slicer-build/DCMTK/ofstd/libsrc/ofchrenc.cc:25:<br>
/usr/include/c++/7/bits/c++0x_warning.h:32:2: error: <a class="hashtag" href="http://discourse.slicer.org/tags/error">#<span>error</span></a> This file requires compiler and library support for the ISO C++ 2011 standard. This support must be enabled with the -std=c++11 or -std=gnu++11 compiler options.<br>
<a class="hashtag" href="http://discourse.slicer.org/tags/error">#<span>error</span></a> This file requires compiler and library support <br>
^~~~~</p>

---

## Post #2 by @gcsharp (2018-02-10 05:40 UTC)

<p>PS: This is the double-edged sword of requiring slicer-specific versions instead of using debian-supplied.  FWIW.</p>

---

## Post #3 by @ihnorton (2018-02-10 11:56 UTC)

<p>The <a href="https://github.com/Slicer/Slicer/blob/master/CMakeLists.txt#L8-L17">defaults</a> have not been changed yet, so you probably still need to pass <code>Qt5_DIR</code> to get the C++11 build configuration. See:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Labs/Qt5-and-VTK8#Status" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Labs/Qt5-and-VTK8#Status</a></p>

---

## Post #4 by @gcsharp (2018-02-11 03:53 UTC)

<p>As always Isaiah, you are correct.  Thanks!!</p>
<p>Please forgive my grumpiness; but I am passionate that packages should build from source without setting options.</p>

---

## Post #5 by @jcfr (2018-02-11 06:38 UTC)

<aside class="quote no-group" data-username="gcsharp" data-post="4" data-topic="2058">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gcsharp/48/863_2.png" class="avatar"> gcsharp:</div>
<blockquote>
<p>should build from source without setting options</p>
</blockquote>
</aside>
<p>That will be the case in few days <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
