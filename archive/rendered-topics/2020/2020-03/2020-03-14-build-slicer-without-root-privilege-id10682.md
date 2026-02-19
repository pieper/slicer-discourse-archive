---
topic_id: 10682
title: "Build Slicer Without Root Privilege"
date: 2020-03-14
url: https://discourse.slicer.org/t/10682
---

# Build slicer without root privilege?

**Topic ID**: 10682
**Date**: 2020-03-14
**URL**: https://discourse.slicer.org/t/build-slicer-without-root-privilege/10682

---

## Post #1 by @ButuiHu (2020-03-14 06:44 UTC)

<p>Hi, it seems that during the building to slicer, it attempts to install something to the root partition? Here is the cmake options I used:</p>
<pre><code class="lang-auto">		-DCMAKE_INSTALL_LIBDIR:PATH=lib
		-DCMAKE_INSTALL_PREFIX:PATH="build-dist"
		-DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON
		-DSlicer_USE_CTKAPPLAUNCHER=0
		-DSlicer_USE_SYSTEM_bzip2=1
		-DSlicer_USE_SYSTEM_curl=1
		-DSlicer_USE_SYSTEM_LibArchive=1
		-DSlicer_USE_SYSTEM_OpenSSL=1
		-DSlicer_USE_SYSTEM_python=1
		-DSlicer_USE_SYSTEM_QT=1
		-DSlicer_USE_SYSTEM_RapidJSON=1
		-DSlicer_USE_SYSTEM_sqlite=1
		-DSlicer_USE_SYSTEM_tbb=1
		-DSlicer_USE_SYSTEM_tcl=1
		-DSlicer_USE_SYSTEM_tk=1
		-DSlicer_USE_SYSTEM_VTK=1
		-DSlicer_USE_SYSTEM_zlib=1
</code></pre>
<p>Though <code>CMAKE_INSTALL_PREFIX</code> is set to a dir the current user has rw permission, some external project is built and installed to root partition, eg. SimpleITK. Is there any related variable to setup? Did I miss something?</p>

---

## Post #2 by @pieper (2020-03-14 15:29 UTC)

<p>The <code>Slicer_USE_SYSTEM</code> family of options probably don’t get much testing.  Maybe you can do a series of builds and see which ones have issues?  Whatever the issue is it’s probably very fixable.</p>

---
