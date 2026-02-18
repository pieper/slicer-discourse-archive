# [help!] Error while linking in SlicerOpenCV

**Topic ID**: 22700
**Date**: 2022-03-26
**URL**: https://discourse.slicer.org/t/help-error-while-linking-in-sliceropencv/22700

---

## Post #1 by @adamrankin (2022-03-26 14:19 UTC)

<p>I’m working on the linux build of SlicerOpenCV.</p>
<p>All of the dependencies build fine, and I get the following error when linking the extension</p>
<pre><code class="lang-auto">[ 92%] Linking CXX executable ../../../bin/qSlicerOpenCVModuleCxxTests
/usr/bin/ld: ../../../bin/qSlicerOpenCVModuleCxxTests: hidden symbol `deflate' in /home/ROBARTS/arankin/SCVR/OpenCV-install/lib/opencv4/3rdparty/libzlib.a(deflate.c.o) is referenced by DSO
/usr/bin/ld: final link failed: bad value
collect2: error: ld returned 1 exit status
</code></pre>
<p>Preliminary google searches indicate that this is an error in static and dynamic linking, with a dynamic library (the extension) trying to link to a static library (libzlib) with a hidden symbol.</p>
<p>Should I configure CMake to tell opencv to link against the VTK zlib library? Any other ideas?</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>

---
