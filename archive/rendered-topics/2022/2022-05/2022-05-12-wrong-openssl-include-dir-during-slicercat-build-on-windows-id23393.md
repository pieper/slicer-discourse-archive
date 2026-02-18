# Wrong OPENSSL_INCLUDE_DIR during SlicerCAT build on WIndows

**Topic ID**: 23393
**Date**: 2022-05-12
**URL**: https://discourse.slicer.org/t/wrong-openssl-include-dir-during-slicercat-build-on-windows/23393

---

## Post #1 by @keri (2022-05-12 18:23 UTC)

<p>Hi,</p>
<p>I’m trying to build SlicerCAT with SlicerJupyter bundled using clean build on WIndows with VS 2022.<br>
Thus <code>xeus</code> depends on <code>OpenSSL</code>:</p>
<pre><code class="lang-auto">ExternalProject_Add_Dependencies(xeus
  DEPENDS
    OpenSSL
  )
</code></pre>
<p>But during <code>xeus</code> configuration I get:</p>
<pre><code class="lang-auto">  Performing configure step for 'xeus'
  loading initial cache file C:/C/r/slicersources-build/xeus-prefix/tmp/xeus-cache-Release.cmake
  -- Selecting Windows SDK version 10.0.19041.0 to target Windows 10.0.22000.
  -- xeus version: v2.3.1
  -- xeus binary version: v7.1.1
  -- XEUS_DISABLE_ARCH_NATIVE:        OFF
  -- XEUS_BUILD_SHARED_LIBS:          ON
  -- XEUS_BUILD_STATIC_LIBS:          ON
  -- XEUS_STATIC_DEPENDENCIES:        OFF
  -- XEUS_EMSCRIPTEN_WASM_BUILD:      OFF
  -- XEUS_BUILD_TESTS:                OFF
  -- XEUS_EMSCRIPTEN_WASM_TEST_BUILD: OFF
  -- tests disabled
  -- Configuring done
  CMake Error in CMakeLists.txt:
    Imported target "OpenSSL::Crypto" includes non-existent path

      "C:/C/r/OpenSSL-install/$(Configuration)/include"

    in its INTERFACE_INCLUDE_DIRECTORIES.  Possible reasons include:

    * The path was deleted, renamed, or moved to another location.

    * An install or uninstall procedure did not complete successfully.

    * The installation package was faulty and references files it does not
    provide.
</code></pre>
<p>In <code>xeus</code> cmakecache <code>OPENSSL_INCLUDE_DIR</code> is set to <code>C:/C/r/OpenSSL-install/$(Configuration)/include</code>.</p>
<p>I’m looking at <code>External_OpenSSL.cmake</code> but still don’t understand why there is rounded brakets in <code>$(Configuration)</code><br>
It seems it goes from <code>SlicerBlockAdditionalLauncherSettings.cmake</code> but can’t understand why this is hapenning.</p>

---

## Post #2 by @keri (2022-05-12 18:46 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/602ec55f2d0d6ec1d1b13ba5619adb29d712778b.jpeg" data-download-href="/uploads/short-url/dIS2Hlaw6UCl8NF73ZWhf2Tadhp.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/602ec55f2d0d6ec1d1b13ba5619adb29d712778b_2_690x301.jpeg" alt="image" data-base62-sha1="dIS2Hlaw6UCl8NF73ZWhf2Tadhp" width="690" height="301" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/602ec55f2d0d6ec1d1b13ba5619adb29d712778b_2_690x301.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/602ec55f2d0d6ec1d1b13ba5619adb29d712778b_2_1035x451.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/602ec55f2d0d6ec1d1b13ba5619adb29d712778b.jpeg 2x" data-dominant-color="1F1E1E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1100×481 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @keri (2022-05-12 19:17 UTC)

<p>I see now</p>
<p>Slicer’s External_OpenSSL uses <a href="https://cmake.org/cmake/help/latest/variable/CMAKE_CFG_INTDIR.html" rel="noopener nofollow ugc">CMAKE_CFG_INTDIR</a> that is expanded to <code>$(Configuration)</code> at configuration time and to <code>Release</code> or <code>Debug</code> etc during build time.</p>
<p>Probably <code>xeus</code> tries to check whether the path exist during config time and that is why I get error</p>

---
