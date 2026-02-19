---
topic_id: 3215
title: "Building Failure On Ubuntu"
date: 2018-06-18
url: https://discourse.slicer.org/t/3215
---

# Building failure on Ubuntu

**Topic ID**: 3215
**Date**: 2018-06-18
**URL**: https://discourse.slicer.org/t/building-failure-on-ubuntu/3215

---

## Post #1 by @Edern_Haumont (2018-06-18 15:50 UTC)

<p>Hi everyone,<br>
I am currently trying ti build Slicer on Ubuntu 18.<br>
The superbuild fails on compiling libarchive :</p>
<pre><code>In function ‘pack_native’:
/home/edern/Projects/Slicer-build/LibArchive/libarchive/archive_pack_dev.c:111:13: error: In the GNU C Library, "makedev" is defined
 by &lt;sys/sysmacros.h&gt;. For historical compatibility, it is
 currently defined by &lt;sys/types.h&gt; as well, but we plan to
 remove this soon. To use "makedev", include &lt;sys/sysmacros.h&gt;
 directly. If you did not intend to use a system-defined macro
 "makedev", you should undefine it after including &lt;sys/types.h&gt;. [-Werror]
   dev = apd_makedev(numbers[0], numbers[1]);
</code></pre>
<p>I have the same error with “major” and “minor”. I am using gcc 7.3.</p>
<p>Any pointer on why that could happen ? Maybe it has nothing to to with Slicer’s configuration …</p>

---

## Post #2 by @brhoom (2018-06-18 16:23 UTC)

<p>Hi and welcome to Slicer,</p>
<p>I just built  Slicer  8.4.1 in Ubuntu 18.04. Here are the steps:</p>
<p>First install required tools and Qt:</p>
<pre><code> sudo apt -y update &amp;&amp; sudo apt -y upgrade  &amp;&amp; sudo apt install unzip wget subversion git-core git-svn make gcc g++ libx11-dev libxt-dev libgl1-mesa-dev libglu1-mesa-dev libfontconfig-dev libxrender-dev libncurses5-dev curl libssl-dev  cmake

 sudo apt -y install qt4-dev-tools libqt4-dev libqtcore4 libqtgui4 libqtwebkit-dev
</code></pre>
<p>Get the sorce</p>
<pre><code> svn co http://svn.slicer.org/Slicer4/branches/Slicer-4-8  Destination_source_folder -r 26813   
</code></pre>
<p>Configure and build Slicer</p>
<pre><code> cmake -DCMAKE_BUILD_TYPE=Release   Destination_build_folder   &amp;&amp; make 
</code></pre>
<p>I only had a problem building DCMTK so I had to changed the   Slicer_Source/CmakeLists.txt File at line 18 and add:</p>
<pre><code>         set (CMAKE_CXX_STANDARD 11) 
         set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
</code></pre>
<p>Good luck!</p>

---

## Post #3 by @ihnorton (2018-06-18 17:06 UTC)

<p>I believe the following simple patch will fix this, but I don’t have a way to test right now:</p>
<pre><code class="lang-auto">diff --git a/libarchive/archive_entry.c b/libarchive/archive_entry.c
index 30fb4566..50f3a04f 100644
--- a/libarchive/archive_entry.c
+++ b/libarchive/archive_entry.c
@@ -30,9 +30,6 @@ __FBSDID("$FreeBSD: head/lib/libarchive/archive_entry.c 201096 2009-12-28 02:41:
 #ifdef HAVE_SYS_STAT_H
 #include &lt;sys/stat.h&gt;
 #endif
-#ifdef HAVE_SYS_TYPES_H
-#include &lt;sys/types.h&gt;
-#endif
 #if MAJOR_IN_MKDEV
 #include &lt;sys/mkdev.h&gt;
 #define HAVE_MAJOR
@@ -40,6 +37,9 @@ __FBSDID("$FreeBSD: head/lib/libarchive/archive_entry.c 201096 2009-12-28 02:41:
 #include &lt;sys/sysmacros.h&gt;
 #define HAVE_MAJOR
 #endif
+#ifdef HAVE_SYS_TYPES_H
+#include &lt;sys/types.h&gt;
+#endif
 #ifdef HAVE_ERRNO_H
 #include &lt;errno.h&gt;
 #endif
@@ -204,7 +204,7 @@ archive_entry_clone(struct archive_entry *entry)

        /* Copy encryption status */
        entry2-&gt;encryption = entry-&gt;encryption;
-
+
        /* Copy ACL data over. */
        archive_acl_copy(&amp;entry2-&gt;acl, &amp;entry-&gt;acl);

diff --git a/libarchive/archive_pack_dev.c b/libarchive/archive_pack_dev.c
index 238cb85a..90ed5117 100644
--- a/libarchive/archive_pack_dev.c
+++ b/libarchive/archive_pack_dev.c
@@ -51,9 +51,6 @@ __RCSID("$NetBSD$");
 #ifdef HAVE_STRING_H
 #include &lt;string.h&gt;
 #endif
-#ifdef HAVE_SYS_TYPES_H
-#include &lt;sys/types.h&gt;
-#endif
 #if MAJOR_IN_MKDEV
 #include &lt;sys/mkdev.h&gt;
 #define HAVE_MAJOR
@@ -61,6 +58,9 @@ __RCSID("$NetBSD$");
 #include &lt;sys/sysmacros.h&gt;
 #define HAVE_MAJOR
 #endif
+#ifdef HAVE_SYS_TYPES_H
+#include &lt;sys/types.h&gt;
+#endif
 #ifdef HAVE_SYS_STAT_H
 #include &lt;sys/stat.h&gt;
 #endif
</code></pre>

---

## Post #4 by @Edern_Haumont (2018-06-19 07:34 UTC)

<p>I am following nearly these steps except the first time I was following this recommendation :<a href="https://www.slicer.org/wiki/Documentation/Labs/Qt5-and-VTK8" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Labs/Qt5-and-VTK8</a><br>
on top of the “default” ones : <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions</a></p>
<p>Also I was building with ninja and for Debug. I started over again, this time with make. I will tell you how it goes.</p>
<p>Thanks !</p>

---

## Post #5 by @Edern_Haumont (2018-06-19 07:39 UTC)

<p>Yep I am confirming still the same error. I will try the fix of <a class="mention" href="/u/ihnorton">@ihnorton</a></p>
<p>Update : Got the same problem building ITK alone. Fixed it by switching from gcc 7.3 to 6.4.</p>

---

## Post #6 by @tavaughan (2018-07-09 20:13 UTC)

<p>I’m getting the above problem. I tried both <a class="mention" href="/u/ihnorton">@ihnorton</a>’s fix above and switching from gcc 7.3 to gcc 6.4, but neither of these worked for me. The command I’m running is:</p>
<pre><code class="lang-auto">cd S4D
cmake \
  -G "Unix Makefiles" \
  -DCMAKE_C_COMPILER=gcc-6 \
  -DQt5_DIR=/media/vaughan/workspace/lnx/devel/Support/qt-everywhere-build-5.10.0/lib/cmake/Qt5 \
  -DCMAKE_BUILD_TYPE:STRING=Debug \
  -DCMAKE_PREFIX_PATH:PATH=/media/vaughan/workspace/lnx/devel/Support/qt-everywhere-build-5.10.0/bin/ \
  -DSlicer_USE_PYTHONQT_WITH_TCL:BOOL=OFF \
  -DSlicer_USE_SimpleITK:BOOL=OFF \
  -DSlicer_USE_QtTesting:BOOL=OFF \
  -DSlicer_VTK_VERSION_MAJOR:STRING=9 \
  -DSlicer_VTK_RENDERING_BACKEND:STRING=OpenGL2 \
  -DSlicer_BUILD_DataStore:BOOL=OFF \
  ../S4
make -j7
</code></pre>
<p>I’m on Ubuntu 18.04 and I’m trying to build the master branch</p>

---

## Post #7 by @tavaughan (2018-07-09 20:42 UTC)

<p>Well I got it to compile past that point by following the instruction in the error message, but I’m not convinced this is the <em>right</em> way to deal with the issue.</p>
<pre><code>diff --git a/libarchive/archive_entry.c b/libarchive/archive_entry.c
index 30fb4566..9e74a331 100644
--- a/libarchive/archive_entry.c
+++ b/libarchive/archive_entry.c
@@ -32,6 +32,9 @@ __FBSDID("$FreeBSD: head/lib/libarchive/archive_entry.c 201096 2009-12-28 02:41:
 #endif
 #ifdef HAVE_SYS_TYPES_H
 #include &lt;sys/types.h&gt;
+#undef makedev
+#undef major
+#undef minor
 #endif
 #if MAJOR_IN_MKDEV
 #include &lt;sys/mkdev.h&gt;
diff --git a/libarchive/archive_pack_dev.c b/libarchive/archive_pack_dev.c
index 098881b6..55937f70 100644
--- a/libarchive/archive_pack_dev.c
+++ b/libarchive/archive_pack_dev.c
@@ -53,6 +53,9 @@ __RCSID("$NetBSD$");
 #endif
 #ifdef HAVE_SYS_TYPES_H
 #include &lt;sys/types.h&gt;
+#undef makedev
+#undef major
+#undef minor
 #endif
 #ifdef HAVE_SYS_STAT_H
 #include &lt;sys/stat.h&gt;</code></pre>

---

## Post #8 by @Meghan_Stuart (2018-10-01 14:48 UTC)

<p>I am running into the same problem. <a class="mention" href="/u/tavaughan">@tavaughan</a>’s solution does seem to work for me, but are there any updates on a “proper” fix?</p>

---

## Post #9 by @jcfr (2018-10-01 15:13 UTC)

<p><a class="mention" href="/u/phcerdan">@phcerdan</a> Since you are building using a recent gcc, would you have any suggestions ?</p>

---

## Post #10 by @phcerdan (2018-10-01 15:38 UTC)

<p>There is an open issue in libarchive about this: <a href="https://github.com/libarchive/libarchive/issues/974" rel="nofollow noopener">https://github.com/libarchive/libarchive/issues/974</a></p>
<p>The fix would be to add the header in <code>libarchive/archive_pack_dev.c</code>.</p>
<pre><code class="lang-cpp">#include &lt;sys/sysmacros.h&gt;
</code></pre>
<p>I am not hitting the warning with gcc 8 in archlinux though.</p>

---

## Post #11 by @pieper (2019-08-22 20:43 UTC)

<p>Building Slicer on ubuntu 18.04 and hit the same error.  Updating to v3.4.0 from the upstream libarchive fixes the problem there (the <a href="https://github.com/libarchive/libarchive/issues/974" rel="nofollow noopener">issue</a> mentioned by <a class="mention" href="/u/phcerdan">@phcerdan</a> has been <a href="https://github.com/libarchive/libarchive/commit/4925fd0ba817764f30b3d6837820351c3bd556d4" rel="nofollow noopener">fixed</a>).</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> do you want to rebase any slicer-specific patches on top of the latest libarchive release?  Or we could cherrypick this fix into our fork, which might be safer in the short run.</p>

---
