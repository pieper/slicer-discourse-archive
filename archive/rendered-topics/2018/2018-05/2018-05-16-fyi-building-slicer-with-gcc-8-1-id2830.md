# FYI : building Slicer with GCC 8.1

**Topic ID**: 2830
**Date**: 2018-05-16
**URL**: https://discourse.slicer.org/t/fyi-building-slicer-with-gcc-8-1/2830

---

## Post #1 by @chir.set (2018-05-16 20:06 UTC)

<p>Building Slicer with GCC 8.1.0 on Arch Linux succeeds with these three patches.</p>
<ol>
<li>Use Python 2.7.15. Versions 2.7.{13,14} do not compile.</li>
</ol>
<blockquote>
<pre><code>diff --git a/CMake/CTestCustom.cmake.in b/CMake/CTestCustom.cmake.in
index 96dde4b99..0b5f65ce7 100644
--- a/CMake/CTestCustom.cmake.in
+++ b/CMake/CTestCustom.cmake.in
@@ -172,8 +172,8 @@ set(CTEST_CUSTOM_WARNING_EXCEPTION
   "warning: the use of .tmpnam_r. is dangerous, better use .mkstemp."
 
   # Python - Windows
-  "(P|p)ython-2.7.13.(M|m)odules"
-  "(P|p)ython-2.7.13.PC"
+  "(P|p)ython-2.7.15.(M|m)odules"
+  "(P|p)ython-2.7.15.PC"
   "Include\\um\\winsock2.h.*warning C4005: 'INVALID_SOCKET': macro redefinition"
   # Python - Linux
   "Objects.unicodeobject.c.*warning:.*differ in signedness"
diff --git a/SuperBuild/External_python.cmake b/SuperBuild/External_python.cmake
index 98d92a5be..1b7fc5928 100644
--- a/SuperBuild/External_python.cmake
+++ b/SuperBuild/External_python.cmake
@@ -53,11 +53,11 @@ if((NOT DEFINED PYTHON_INCLUDE_DIR
    OR NOT DEFINED PYTHON_LIBRARY
    OR NOT DEFINED PYTHON_EXECUTABLE) AND NOT ${CMAKE_PROJECT_NAME}_USE_SYSTEM_${proj})
 
-  set(python_SOURCE_DIR "${CMAKE_BINARY_DIR}/Python-2.7.13")
+  set(python_SOURCE_DIR "${CMAKE_BINARY_DIR}/Python-2.7.15")
 
   ExternalProject_Add(python-source
-    URL "https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tgz"
-    URL_MD5 "17add4bf0ad0ec2f08e0cae6d205c700"
+    URL "https://www.python.org/ftp/python/2.7.15/Python-2.7.15.tgz"
+    URL_MD5 "045fb3440219a1f6923fefdabde63342"
     DOWNLOAD_DIR ${CMAKE_BINARY_DIR}
     SOURCE_DIR ${python_SOURCE_DIR}
     CONFIGURE_COMMAND ""
</code></pre>
</blockquote>
<ol start="2">
<li>Declare gcc 8 for ITKv4. The declared constants for GCC 7 do not seem to be used in the code (using grep to find out)</li>
</ol>
<blockquote>
<pre><code>diff --git a/Modules/ThirdParty/VNL/src/vxl/vcl/vcl_compiler.h b/Modules/ThirdParty/VNL/src/vxl/vcl/vcl_compiler.h
index 3f1bb01144..db3e7a6091 100644
--- a/Modules/ThirdParty/VNL/src/vxl/vcl/vcl_compiler.h
+++ b/Modules/ThirdParty/VNL/src/vxl/vcl/vcl_compiler.h
@@ -75,7 +75,7 @@
 #  else
 #   define VCL_GCC_60
 #  endif
-# elif (__GNUC__==7)
+# elif (__GNUC__==7) 
 #  define VCL_GCC_7
 #  if (__GNUC_MINOR__ &gt; 2 )
 #   define VCL_GCC_73
@@ -86,6 +86,13 @@
 #  else
 #   define VCL_GCC_70
 #  endif
+# elif (__GNUC__==8)
+#  define VCL_GCC_8
+#  if (__GNUC_MINOR__ &gt; 0 )
+#   define VCL_GCC_81
+#  else
+#   define VCL_GCC_80
+#  endif
 # else
 #  error "Dunno about this gcc"
 # endif
</code></pre>
</blockquote>
<ol start="3">
<li>Avoid this error while compiling VTKv9 : H5detect.c:1363:1: error: attributes should be specified before the declarator in a function definition</li>
</ol>
<blockquote>
<pre><code>diff --git a/ThirdParty/hdf5/vtkhdf5/src/H5detect.c b/ThirdParty/hdf5/vtkhdf5/src/H5detect.c
index b2c958e5c4..bb32265b18 100644
--- a/ThirdParty/hdf5/vtkhdf5/src/H5detect.c
+++ b/ThirdParty/hdf5/vtkhdf5/src/H5detect.c
@@ -1361,7 +1361,7 @@ bit.\n";
  *-------------------------------------------------------------------------
  */
 static void
-detect_C89_integers(void) HDF_NO_UBSAN
+HDF_NO_UBSAN detect_C89_integers(void) 
 {
     DETECT_BYTE(signed char,	  SCHAR,        d_g[nd_g]); nd_g++;
     DETECT_BYTE(unsigned char,	  UCHAR,        d_g[nd_g]); nd_g++;
@@ -1389,7 +1389,7 @@ detect_C89_integers(void) HDF_NO_UBSAN
  *-------------------------------------------------------------------------
  */
 static void
-detect_C89_floats(void) HDF_NO_UBSAN
+HDF_NO_UBSAN detect_C89_floats(void)
 {
     DETECT_F(float,     FLOAT,      d_g[nd_g]); nd_g++;
     DETECT_F(double,    DOUBLE,     d_g[nd_g]); nd_g++;
@@ -1411,7 +1411,7 @@ detect_C89_floats(void) HDF_NO_UBSAN
  *-------------------------------------------------------------------------
  */
 static void
-detect_C99_integers8(void) HDF_NO_UBSAN
+HDF_NO_UBSAN detect_C99_integers8(void) 
 {
 #if H5_SIZEOF_INT8_T&gt;0
   #if H5_SIZEOF_INT8_T==1
@@ -1473,7 +1473,7 @@ detect_C99_integers8(void) HDF_NO_UBSAN
  *-------------------------------------------------------------------------
  */
 static void
-detect_C99_integers16(void) HDF_NO_UBSAN
+HDF_NO_UBSAN detect_C99_integers16(void) 
 {
 #if H5_SIZEOF_INT16_T&gt;0
     DETECT_I(int16_t, 		  INT16,        d_g[nd_g]); nd_g++;
@@ -1511,7 +1511,7 @@ detect_C99_integers16(void) HDF_NO_UBSAN
  *-------------------------------------------------------------------------
  */
 static void
-detect_C99_integers32(void) HDF_NO_UBSAN
+HDF_NO_UBSAN detect_C99_integers32(void) 
 {
 #if H5_SIZEOF_INT32_T&gt;0
     DETECT_I(int32_t, 		  INT32,        d_g[nd_g]); nd_g++;
@@ -1549,7 +1549,7 @@ detect_C99_integers32(void) HDF_NO_UBSAN
  *-------------------------------------------------------------------------
  */
 static void
-detect_C99_integers64(void) HDF_NO_UBSAN
+HDF_NO_UBSAN detect_C99_integers64(void) 
 {
 #if H5_SIZEOF_INT64_T&gt;0
     DETECT_I(int64_t, 		  INT64,        d_g[nd_g]); nd_g++;
@@ -1600,7 +1600,7 @@ detect_C99_integers64(void) HDF_NO_UBSAN
  *-------------------------------------------------------------------------
  */
 static void
-detect_C99_integers(void) HDF_NO_UBSAN
+HDF_NO_UBSAN detect_C99_integers(void) 
 {
     /* break it down to more subroutines so that each module subroutine */
     /* is smaller and takes less time to compile with optimization on.  */
@@ -1626,7 +1626,7 @@ detect_C99_integers(void) HDF_NO_UBSAN
  *-------------------------------------------------------------------------
  */
 static void
-detect_C99_floats(void) HDF_NO_UBSAN
+HDF_NO_UBSAN detect_C99_floats(void) 
 {
 #if H5_SIZEOF_DOUBLE == H5_SIZEOF_LONG_DOUBLE
     /*
@@ -1657,7 +1657,7 @@ detect_C99_floats(void) HDF_NO_UBSAN
  *-------------------------------------------------------------------------
  */
 static void
-detect_alignments(void) HDF_NO_UBSAN
+HDF_NO_UBSAN detect_alignments(void) 
 {
     /* Detect structure alignment for pointers, hvl_t, hobj_ref_t, hdset_reg_ref_t */
     DETECT_M(void *,              POINTER,      m_g[na_g]); na_g++;
@@ -1745,7 +1745,7 @@ static int verify_signal_handlers(int signum, void (*handler)(int))
  *-------------------------------------------------------------------------
  */
 int
-main(void) HDF_NO_UBSAN
+HDF_NO_UBSAN main(void) 
 {
 
 #if defined(H5_HAVE_SETSYSINFO) &amp;&amp; defined(SSI_NVPAIRS)
</code></pre>
</blockquote>
<p>Just for informational purposes.</p>

---

## Post #2 by @phcerdan (2018-05-16 20:54 UTC)

<p>This is great <a class="mention" href="/u/chir.set">@chir.set</a>, thanks for reporting it. I hitted the same issues this morning using arch <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=12" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20"></p>
<aside class="quote no-group" data-username="chir.set" data-post="1" data-topic="2830">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<ol>
<li>Use Python 2.7.15. Versions 2.7.{13,14} do not compile.</li>
</ol>
</blockquote>
</aside>
<p><a class="mention" href="/u/jcfr">@jcfr</a> might have a say on this one. Thanks for the suggested solution!</p>
<aside class="quote no-group" data-username="chir.set" data-post="1" data-topic="2830">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>Avoid this error while compiling VTKv9 : H5detect.c:1363:1: error: attributes should be specified before the declarator in a function definition</p>
</blockquote>
</aside>
<p>VXL has been fixed already (and merged) : <a href="https://github.com/vxl/vxl/commit/2662860491ff44a16e01581a6b3727d53997fee8" class="inline-onebox" rel="noopener nofollow ugc">COMP: Add gcc8 support to vcl_compiler. · vxl/vxl@2662860 · GitHub</a></p>
<p>And the update for ITK to use the updated VXL is in review: <a href="http://review.source.kitware.com/#/c/23437/1" rel="noopener nofollow ugc">http://review.source.kitware.com/#/c/23437/1</a></p>
<aside class="quote no-group" data-username="chir.set" data-post="1" data-topic="2830">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<ol start="3">
<li>Avoid this error while compiling VTKv9 : H5detect.c:1363:1: error: attributes should be specified before the declarator in a function definition</li>
</ol>
</blockquote>
</aside>
<p>Reported to VTK with your patch suggestion: <a href="https://gitlab.kitware.com/vtk/vtk/issues/17316" class="inline-onebox" rel="noopener nofollow ugc">Errors in H5detect (#17316) · Issues · VTK / VTK · GitLab</a></p>

---

## Post #3 by @jcfr (2018-05-16 21:08 UTC)

<p><a class="mention" href="/u/chir.set">@chir.set</a> <a class="mention" href="/u/phcerdan">@phcerdan</a> Thanks for your help with this.</p>
<blockquote>
<p>Python 2.7.13 → Python 2.7.15</p>
</blockquote>
<p>Makes sense. We will update the version used in Slicer.</p>
<blockquote>
<p>error while compiling VTKv9</p>
</blockquote>
<p>I added a comment <a href="https://gitlab.kitware.com/vtk/vtk/issues/17316" class="inline-onebox">Errors in H5detect (#17316) · Issues · VTK / VTK · GitLab</a> referencing the HDF5 upstream fix that could be backported to the VTK fork of hdf5</p>

---

## Post #4 by @phcerdan (2018-10-25 00:09 UTC)

<p>For completion in this thread, I have been using <code>USE_SYSTEM_python:BOOL=ON</code> in Archlinux to overcome the following bug in <a href="https://github.com/python-cmake-buildsystem/python-cmake-buildsystem/issues/224" rel="nofollow noopener">python-cmake-buildsystem</a> about missing the header <code>rpc.h</code>. This happens to me with <code>python-2.7.15</code> too.</p>

---
