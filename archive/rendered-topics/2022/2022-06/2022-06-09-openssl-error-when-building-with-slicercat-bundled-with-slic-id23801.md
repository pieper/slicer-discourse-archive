---
topic_id: 23801
title: "Openssl Error When Building With Slicercat Bundled With Slic"
date: 2022-06-09
url: https://discourse.slicer.org/t/23801
---

# OpenSSL error when building with SlicerCAT bundled with SlicerJupyter on Windows

**Topic ID**: 23801
**Date**: 2022-06-09
**URL**: https://discourse.slicer.org/t/openssl-error-when-building-with-slicercat-bundled-with-slicerjupyter-on-windows/23801

---

## Post #1 by @keri (2022-06-09 19:47 UTC)

<p>Hi,</p>
<p>During <code>xeus</code> configure step I get the following error:</p>
<pre><code class="lang-auto">  -- Detecting CXX compile features
  -- Detecting CXX compile features - done
  -- xeus version: v2.3.1
  -- xeus binary version: v7.1.1
  -- XEUS_DISABLE_ARCH_NATIVE:        OFF
  -- XEUS_BUILD_SHARED_LIBS:          ON
  -- XEUS_BUILD_STATIC_LIBS:          ON
  -- XEUS_STATIC_DEPENDENCIES:        OFF
  -- XEUS_EMSCRIPTEN_WASM_BUILD:      OFF
  -- XEUS_BUILD_TESTS:                OFF
  -- XEUS_EMSCRIPTEN_WASM_TEST_BUILD: OFF
  -- Found nlohmann_json: C:/C/r/nlohmann_json-build/nlohmann_jsonConfig.cmake (found suitable version "3.8.0", minimum
   required is "3.2.0")
  -- Found OpenSSL: optimized;C:/C/r/OpenSSL-install/Release/lib/libcrypto.lib;debug;C:/C/r/OpenSSL-install/Debug/lib/l
  ibcrypto.lib
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
<p>That happens because <code>$(Configuration)</code> is unwrapped only at buildtime (or at generation time I don’t remember).<br>
Thus with multiconfig generators OpenSSL includes non-existent path at configure time.<br>
<code>xeus</code> tries to link to OpenSSL` and gives me this error.</p>
<p>I sligghtly modified <a href="https://github.com/Slicer/Slicer/pull/6414/files" rel="noopener nofollow ugc">External_OpenSSL.cmake</a> in a way that if the developper explicitely pass <code>-DCMAKE_BUILD_TYPE=smth</code> then the mentioned error doesn’t arise anymore.</p>
<p>I know that somebody already tried to bundle SlicerJupyter with SlicerCAT. If somebody encountered the same problem please give some hints.</p>

---
