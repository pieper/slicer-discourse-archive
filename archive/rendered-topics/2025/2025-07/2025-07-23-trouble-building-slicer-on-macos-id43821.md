# Trouble Building Slicer on macOS

**Topic ID**: 43821
**Date**: 2025-07-23
**URL**: https://discourse.slicer.org/t/trouble-building-slicer-on-macos/43821

---

## Post #1 by @alientex (2025-07-23 08:57 UTC)

<p>Hello,</p>
<p>I’ve been trying to build Slicer on my Mac for months now, but still haven’t found a reliable way to do it without running into errors—even after following the documentation carefully.</p>
<p>One of the main blockers is the Qt requirement. The documentation points to a DMG <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/macos.html#prerequisites" rel="noopener nofollow ugc">here</a>, but it doesn’t include Qt 5.15.2. Since that version is no longer maintained, I’m not sure where to get it, and I’m stuck.</p>
<p>Honestly, I just want to build Slicer on my Mac and get started without all the friction. It’s frustrating that there isn’t a simpler, more end-user-friendly way to do this.</p>
<p>Can anyone please guide me through a working setup or a less painful process?</p>
<p>Thanks in advance!</p>

---

## Post #3 by @tas47 (2025-07-26 16:05 UTC)

<p>I know this is cliche but you need to  read this in and out:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/macos.html">
  <header class="source">

      <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/macos.html" target="_blank" rel="noopener nofollow ugc">slicer.readthedocs.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/macos.html" target="_blank" rel="noopener nofollow ugc">macOS — 3D Slicer  documentation</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I also  spend hours trying to build  slicer from sourceand it was very hard. My first recommendation is that if you can avoid installing in your mac, and instead in a new VM, it  will make the build much easier.</p>
<p>For mac:<br>
The most important thing it that you have to make sure you have a version  qt 15 and a version of cmake that is not higher than 4x.</p>
<p>make sure you check those first and where they are in your path. Most people install them with brew so try<br>
﻿﻿﻿ ```<br>
brew list --formula | grep make</p>
<pre><code class="lang-auto">brew list --formula | grep qt
</code></pre>
<p>i installed qt with brew and it worked, and if you have the wrong versions delete those too.</p>
<pre><code class="lang-auto">brew install qt@5
</code></pre>
<p>you can also check using <code>which</code> command</p>
<p>-Fix those first, and make sure they are in your path env and have xcode installed.</p>
<p>-Next just like the documentation says make sure you make a directory in the /opt : this will be very helpful</p>
<pre><code class="lang-auto">mkdir /opt/s/
</code></pre>
<pre><code class="lang-auto">cd /opt/s
cmake \
  -DCMAKE_OSX_DEPLOYMENT_TARGET:STRING=13.0 \
  -DCMAKE_BUILD_TYPE:STRING=Debug \
  -DQt5_DIR:PATH="PUT YOUR QT PATH"
</code></pre>
<p>Then execute this:</p>
<pre data-code-wrap="cd"><code class="lang-cd">make -j4
</code></pre>
<p>also i recommend using cursor you debug the logs</p>

---

## Post #4 by @alientex (2025-07-29 11:39 UTC)

<p>Hi <a class="mention" href="/u/tas47">@tas47</a> ,</p>
<p>I followed your provided instructions, but encountered the following errors during the build:</p>
<pre><code class="lang-auto">[ 65%] Building CXX object CMakeFiles/PythonQt.dir/generated_cpp_515/com_trolltech_qt_network/com_trolltech_qt_network0.cpp.o
In file included from /opt/s/CTK-build/PythonQt/generated_cpp_515/com_trolltech_qt_network/com_trolltech_qt_network0.cpp:1:
In file included from /opt/s/CTK-build/PythonQt/generated_cpp_515/com_trolltech_qt_network/com_trolltech_qt_network0.h:14:
/opt/homebrew/opt/qt@5/lib/QtNetwork.framework/Headers/qdtls.h:52:1: error: static_assert failed due to requirement 'bool(-1 == 1)' "Required feature dtls for file /opt/homebrew/opt/qt@5/lib/QtNetwork.framework/Headers/qdtls.h not available."
QT_REQUIRE_CONFIG(dtls);
^~~~~~~~~~~~~~~~~~~~~~~
/opt/homebrew/opt/qt@5/include/QtCore/qglobal.h:87:36: note: expanded from macro 'QT_REQUIRE_CONFIG'
#define QT_REQUIRE_CONFIG(feature) Q_STATIC_ASSERT_X(QT_FEATURE_##feature == 1, "Required feature " #feature " for file " __FILE__ " not available.")

138 warnings and 1 error generated.
make[8]: *** [CMakeFiles/PythonQt.dir/generated_cpp_515/com_trolltech_qt_network/com_trolltech_qt_network0.cpp.o] Error 1
make[7]: *** [CMakeFiles/PythonQt.dir/all] Error 2
make[6]: *** [all] Error 2
make[5]: *** [PythonQt-cmake/src/PythonQt-stamp/PythonQt-install] Error 2
make[4]: *** [CMakeFiles/PythonQt.dir/all] Error 2
make[3]: *** [all] Error 2
make[2]: *** [CTK-prefix/src/CTK-stamp/CTK-build] Error 2
make[1]: *** [CMakeFiles/CTK.dir/all] Error 2
</code></pre>
<p>Below is the configuration command:<br>
<code>cmake \ </code><br>
<code>-DCMAKE_OSX_DEPLOYMENT_TARGET:STRING=13.0 </code><br>
<code>-DCMAKE_BUILD_TYPE:STRING=Debug </code><br>
<code>-DCMAKE_PREFIX_PATH:PATH=/opt/homebrew/qt@5/lib/cmake </code><br>
<code>-DSlicer_VTK_SMP_IMPLEMENTATION_TYPE:STRING=Sequential </code><br>
<code>~/Desktop/Slicer</code></p>

---

## Post #5 by @tas47 (2025-07-30 17:30 UTC)

<p>I hear your frustration, and honestly i dont really have a solution. Since every computer and configuration feels different. I read alot of post here and it seems alot of people having build trouble with arm.</p>
<p>First try to get the QT path ahead of your slicer build path in your .bash or .zsh file first</p>
<p>-update xcode</p>
<p>my qt version is this<br>
<strong>Qt 5.15.16 from Homebrew so install this</strong></p>
<p>which qt: to get bath and add it to your path variable,<br>
export Qt5_DIR=/opt/homebrew/opt/qt@5/lib/cmake/Qt5</p>
<p>and then make sure you clean up your slicer and build from source:</p>
<p>my configuration:</p>
<p>based on my cache and path cmake used it looks like this (dont copy this  but it can maybe help u diagnose)</p>
<pre><code class="lang-auto">cmake \
  -DADDITIONAL_CXX_FLAGS:STRING="" \
  -DADDITIONAL_C_FLAGS:STRING="" \
  -DBUILD_TESTING:BOOL=ON \
  -DCMAKE_BUILD_TYPE:STRING=Debug \
  -DCMAKE_OSX_SYSROOT:PATH=/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.2.sdk \
  -DQt5_DIR:PATH=/opt/homebrew/opt/qt@5/lib/cmake/Qt5 \
  -DSlicer_BUILD_APPLICATIONUPDATE_SUPPORT:BOOL=ON \
  -DSlicer_BUILD_BRAINSTOOLS:BOOL=ON \
  -DSlicer_BUILD_CLI:BOOL=ON \
  -DSlicer_BUILD_DICOM_SUPPORT:BOOL=ON \
  -DSlicer_BUILD_DIFFUSION_SUPPORT:BOOL=ON \
  -DSlicer_BUILD_EXTENSIONMANAGER_SUPPORT:BOOL=ON \
  -DSlicer_BUILD_MULTIMEDIA_SUPPORT:BOOL=ON \
  -DSlicer_BUILD_MULTIVOLUME_SUPPORT:BOOL=ON \
  -DSlicer_BUILD_PYTHONQT:BOOL=ON \
  -DSlicer_BUILD_QTLOADABLEMODULES:BOOL=ON \
  -DSlicer_BUILD_QTSCRIPTEDMODULES:BOOL=ON \
  -DSlicer_BUILD_WEBENGINE_SUPPORT:BOOL=ON \
  -DSlicer_DEFAULT_FAVORITE_MODULES:STRING="Data,Volumes,Models,Transforms,Markups,SegmentEditor" \
  -DSlicer_DEFAULT_HOME_MODULE:STRING="Welcome" \
  -DSlicer_ORGANIZATION_DOMAIN:STRING=slicer.org \
  -DSlicer_ORGANIZATION_NAME:STRING=slicer.org \
  -DSlicer_RELEASE_TYPE:STRING=Experimental \
  -DSlicer_REQUIRED_QT_VERSION:STRING=5.15 \
  -DSlicer_SUPERBUILD:BOOL=ON \
  -DSlicer_USE_CTKAPPLAUNCHER:BOOL=ON \
  -DSlicer_USE_NUMPY:BOOL=ON \
  -DSlicer_USE_PYTHONQT:BOOL=ON \
  -DSlicer_USE_PYTHONQT_WITH_OPENSSL:BOOL=ON \
  -DSlicer_USE_QtTesting:BOOL=ON \
  -DSlicer_USE_SCIPY:BOOL=ON \
  -DSlicer_USE_SimpleITK:BOOL=ON \
  -DSlicer_USE_SimpleITK_SHARED:BOOL=ON \
  -DSlicer_VTK_SMP_IMPLEMENTATION_TYPE:STRING=STDThread \
  -DSlicer_VTK_VERSION_MAJOR:STRING=9 \
  -DSlicer_VTK_VERSION_MINOR:STRING=4 \
  ~/Slicer-source
</code></pre>
<p>Try to follow  these links:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5944">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5944" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5944" target="_blank" rel="noopener nofollow ugc">Unable to build from source on Apple silicon</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-10-12" data-time="17:46:43" data-timezone="UTC">05:46PM - 12 Oct 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/kliron" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/626811?v=4" class="onebox-avatar-inline" width="20" height="20">
          kliron
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Type: Bug
        </span>
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Domain: build-system
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Steps to reproduce

I followed all the instructions from the [docs](https:/<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">/slicer.readthedocs.io/en/latest/developer_guide/build_instructions/macos.html#prerequisites) to build slicer from source. 

Build halts with the following error while trying to build DCMTK:

```
make[2]: *** [DCMTK-prefix/src/DCMTK-stamp/DCMTK-configure] Error 1
make[1]: *** [CMakeFiles/DCMTK.dir/all] Error 2
-- OpenSSL: Errors detected - See below.

ld: warning: double slash removed from -install_name (/Users/kliron/opt/slicer/OpenSSL//libcrypto.1.1.dylib)
ld: warning: The i386 architecture is deprecated for macOS (remove from the Xcode build setting: ARCHS)
ld: warning: ignoring file /Users/kliron/opt/slicer/zlib-install/lib/libz.a, building for macOS-i386 but attempting to link with file built for macOS-arm64
ld: warning: ignoring file /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX11.3.sdk/usr/lib/libSystem.tbd, missing required architecture i386 in file /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX11.3.sdk/usr/lib/libSystem.tbd (3 slices)

Undefined symbols for architecture i386:

"__DefaultRuneLocale", referenced from:
      _CONF_parse_list in conf_mod.o
  "___bzero", referenced from:
      _ASN1_BIT_STRING_set_bit in a_bitstr.o
      _asn1_item_embed_new in tasn_new.o
      _addr_strings in b_addr.o
      _mem_ctrl in bss_mem.o
      _BLAKE2b_Final in blake2b.o
      _BLAKE2s_Final in blake2s.o
      _bn_div_fixed_top in bn_div.o
      ...

[...an extensive output of a lot more missing symbols...]

ld: symbol(s) not found for architecture i386
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make[4]: *** [libcrypto.dylib] Error 1
make[3]: *** [build_libs] Error 2

CMake Error at /Users/kliron/Projects/slicer/CMake/ExternalProjectForNonCMakeProject.cmake:104 (message):
  OpenSSL: build step failed with exit code '2'.
```

## Expected behavior

A successful build.

## Environment
- Slicer version: latest source tree
- Operating system: MacOS Big Sur 11.6

Has anyone been able to compile slicer from source on a M1 Mac? How do I bypass the missing i386 openssl library?</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>“I confirm that the last Slicer version successfully compiles on apple m1 only with OpenSSL built outside of Slicer (configured for darwin x86_64) and SimpleITK disabled.</p>
<p>These should be the relevant flags:</p>
<p><code>-DCMAKE_OSX_ARCHITECTURES:STRING=x86_64</code><br>
<code>-DSlicer_USE_SYSTEM_OpenSSL:BOOL=ON</code><br>
<code>-DSlicer_USE_SimpleITK:BOOL=OFF</code></p>
<p>I think the issue is the configuration step of the default slicer openssl build, which allows various dependencies of OpenSSL to be compiled in 32 bit mode, which I believe is not supported in M1 chips.</p>
<p>In fact, OpenSSL on its own (1.1.1g in this example) builds very nicely with a very simple <code>./Configure darwin64-x86_64-cc shared</code>"</p>
<p>Another post:</p>
<aside class="quote quote-modified" data-post="1" data-topic="39549">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/park/48/5717_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/build-slicer-in-apple-silicon-error-arm64/39549">Build Slicer in apple silicon - error "arm64"</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    Hi all, 
During the build process as per Steve’s advice, <a href="https://github.com/Slicer/Slicer/issues/5944" rel="noopener nofollow ugc">#5944</a> 
I encountered the following issue. Has anyone resolved this? 
Computer Specifications: 

CPU: M1 Pro
OS: macOS Ventura
Xcode: 13.0

Process: 

Installed Qt5 and CMake using Homebrew.

brew install qt@5
brew install cmake


Build OpenSSL:

git clone https://github.com/openssl/openssl.git openssl-git
cd openssl-git
./Configure darwin64-arm64-cc --prefix="/tmp/openssl-arm" no-asm
make &amp;&amp; make install
mv OpenSSL-install OpenSSL-install-…
  </blockquote>
</aside>

<p><a href="https://discourse.slicer.org/t/build-slicer-in-apple-silicon-error-arm64/39549/2">“I haven’t tried building on mac arm in a long time, so more recent changes in the dependencies may have broken things.</a></p>
<p><a href="https://discourse.slicer.org/t/build-slicer-in-apple-silicon-error-arm64/39549/2">One idea is to turn off this flag:”</a></p>
<p>I also just want to preface that although my build was successful,  it didn’t pass all the tests, I also used a lot of ai to help me  so I am not too savvy with cmake at all. I mainly build slicer so i could extract lsp and get a configuration.json file to get access to autocomplete.</p>

---
