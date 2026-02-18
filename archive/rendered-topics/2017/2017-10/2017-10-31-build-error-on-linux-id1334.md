# Build error on linux

**Topic ID**: 1334
**Date**: 2017-10-31
**URL**: https://discourse.slicer.org/t/build-error-on-linux/1334

---

## Post #1 by @gcsharp (2017-10-31 16:11 UTC)

<p>Hi, I have a build failure on linux (debian stable, gcc 6.3.0).<br>
Fresh build directory, DCMTK fails.  Excerpts below.  Any idea?<br>
-Greg</p>
<p>[ 48%] Performing configure step for ‘DCMTK’<br>
<br>
– Info: C++11 features disabled<br>
<br>
[  0%] Building CXX object<br>
ofstd/libsrc/CMakeFiles/ofstd.dir/ofchrenc.cc.o<br>
In file included from /usr/include/c++/6/cstdint:35:0,<br>
from /home/gcs6/build/slicer-4/Slicer-<br>
build/DCMTK/ofstd/include/dcmtk/ofstd/ofstdinc.h:279,<br>
from /home/gcs6/build/slicer-4/Slicer-<br>
build/DCMTK/ofstd/include/dcmtk/ofstd/oftypes.h:74,<br>
from /home/gcs6/build/slicer-4/Slicer-<br>
build/DCMTK/ofstd/include/dcmtk/ofstd/ofcond.h:28,<br>
from /home/gcs6/build/slicer-4/Slicer-<br>
build/DCMTK/ofstd/include/dcmtk/ofstd/ofchrenc.h:28,<br>
from /home/gcs6/build/slicer-4/Slicer-<br>
build/DCMTK/ofstd/libsrc/ofchrenc.cc:25:<br>
/usr/include/c++/6/bits/c++0x_warning.h:32:2: error: <a class="hashtag" href="http://discourse.slicer.org/tags/error">#<span>error</span></a> This file<br>
requires compiler and library support for the ISO C++ 2011 standard.<br>
This support must be enabled with the -std=c++11 or -std=gnu++11<br>
compiler options.</p>
<p>The information in this e-mail is intended only for the person to whom it is<br>
addressed. If you believe this e-mail was sent to you in error and the e-mail<br>
contains patient information, please contact the Partners Compliance HelpLine at<br>
<a href="http://www.partners.org/complianceline" rel="nofollow noopener">http://www.partners.org/complianceline</a> . If the e-mail was sent to you in error<br>
but does not contain patient information, please contact the sender and properly<br>
dispose of the e-mail.</p>

---

## Post #2 by @jcfr (2017-10-31 16:43 UTC)

<p>How do you configure Slicer ?</p>

---

## Post #3 by @gcsharp (2017-10-31 17:01 UTC)

<p>After reading CMakeLists.txt, I learned that I could tell Slicer to use<br>
c++11 by changing the VTK version.</p>
<p>I would propose changing that logic to the below, so that one could<br>
choose on the command line to enable c++11 even with VTK 7.</p>
<p>If you like I can give a pull request.</p>

---

## Post #4 by @jcfr (2017-10-31 17:18 UTC)

<p>Since we will soon transition to C++11, Qt5 and VTK8 as the default. I am sure it is worth the effort.</p>
<p>If c++ 11 is required, I suggest you configure Slicer (from a clean build tree) with</p>
<pre><code class="lang-auto">cmake  -DQt5_DIR:PATH=/path/to/lib/cmake/Qt5 ../Slicer
</code></pre>

---

## Post #5 by @chir.set (2017-10-31 17:40 UTC)

<aside class="quote no-group" data-username="gcsharp" data-post="3" data-topic="1334">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gcsharp/48/863_2.png" class="avatar"> gcsharp:</div>
<blockquote>
<p>even with VTK 7</p>
</blockquote>
</aside>
<p>The performance gain I have seen with Volume Rendering using VTK8 is a game changer. I don’t think it’s worthwhile to spend resources with VTK7.</p>

---
