---
topic_id: 1129
title: "Building From Source On Ubuntu 16 04 Openssl"
date: 2017-09-26
url: https://discourse.slicer.org/t/1129
---

# Building From Source on Ubuntu 16.04 - OpenSSL

**Topic ID**: 1129
**Date**: 2017-09-26
**URL**: https://discourse.slicer.org/t/building-from-source-on-ubuntu-16-04-openssl/1129

---

## Post #1 by @codey (2017-09-26 23:59 UTC)

<p>I can build Slicer with the option</p>
<p>Slicer_USE_PYTHONQT_WITH_OPENS</p>
<p>off</p>
<p>When I try to build with this on I get</p>
<pre><code class="lang-auto">[ 11%] Completed 'bzip2'
[ 12%] Built target bzip2
[ 12%] No configure step for 'OpenSSL'
/usr/bin/cmake: libssl.so.1.0.0: no version information available (required by /usr/lib/x86_64-linux-gnu/libcurl.so.4)
/usr/bin/cmake: libssl.so.1.0.0: no version information available (required by /usr/lib/x86_64-linux-gnu/libcurl.so.4)
/usr/bin/cmake: libssl.so.1.0.0: no version information available (required by /usr/lib/x86_64-linux-gnu/libcurl.so.4)
/usr/bin/cmake: libcrypto.so.1.0.0: no version information available (required by /usr/lib/x86_64-linux-gnu/libcurl.so.4)
/usr/bin/cmake: relocation error: /usr/lib/x86_64-linux-gnu/libcurl.so.4: symbol SSL_CTX_set_alpn_protos, version OPENSSL_1.0.2 not defined in file libssl.so.1.0.0 with link time reference
CMakeFiles/OpenSSL.dir/build.make:109: recipe for target 'OpenSSL-prefix/src/OpenSSL-stamp/OpenSSL-configure' failed
make[2]: *** [OpenSSL-prefix/src/OpenSSL-stamp/OpenSSL-configure] Error 127
CMakeFiles/Makefile2:1267: recipe for target 'CMakeFiles/OpenSSL.dir/all' failed
make[1]: *** [CMakeFiles/OpenSSL.dir/all] Error 2
Makefile:94: recipe for target 'all' failed
make: *** [all] Error 2
</code></pre>

---

## Post #2 by @lassoan (2017-09-27 00:04 UTC)

<p>As described in Slicer build instructors, you need to build Qt with OpenSSL support, or build Slicer with OpenSSL disabled.</p>

---

## Post #3 by @codey (2017-09-28 08:43 UTC)

<p>I can build with Slicer disabled no problem. I want to use pip so I need SSL.</p>
<p>I tried using</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">
      <a href="https://github.com/jcfr/qt-easy-build" target="_blank" rel="nofollow noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars1.githubusercontent.com/u/219043?s=400&amp;v=4" class="thumbnail onebox-avatar" width="400" height="400">

<h3><a href="https://github.com/jcfr/qt-easy-build" target="_blank" rel="nofollow noopener">jcfr/qt-easy-build</a></h3>

<p>Scripts allowing to easily build Qt with OpenSSL support on Linux, macOS or Windows - jcfr/qt-easy-build</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>and pointing CMake to the qmake of the resulting build with openssl but I get the same error</p>

---

## Post #4 by @lassoan (2017-09-28 23:53 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> Is qt-easy-build supposed to work on Ubuntu 16.04?</p>
<p><a class="mention" href="/u/codey">@codey</a>, which Qt version did you try to build? On the <a href="https://github.com/jcfr/qt-easy-build">dashboard</a> Qt 5.9.1 shows up in green for Linux.</p>

---

## Post #5 by @codey (2017-09-29 09:43 UTC)

<p>I am using version 4.8.7</p>

---

## Post #6 by @lassoan (2017-09-29 13:03 UTC)

<p>Maybe while waiting for <a class="mention" href="/u/jcfr">@jcfr</a> to get back to us, you can try building with Qt5 and VTK8.</p>

---

## Post #7 by @jcfr (2017-09-29 16:03 UTC)

<p>I haven’t tried to build using Ubuntu 16.04 … that said I will soon update my workstation to use it.</p>
<blockquote>
<p>qt-easy-build dashboard</p>
</blockquote>
<p>The testing for Qt 4.8.7 needs some work, I will look into it.</p>

---

## Post #8 by @codey (2017-09-30 13:13 UTC)

<p>I’ve tried installing QT5.9.1 from the Qt’s runfile with VTK8 but I get<br>
an error when building Slicer</p>
<pre><code class="lang-auto">/Data-work/BuildDirs/Slicer/Modules/Loadable/Tables/Widgets/Testing/Cxx/qSlicerTableColumnPropertiesWidgetTest1.cxx: 
In function ‘int qSlicerTableColumnPropertiesWidgetTest1(int, char**)’:
/Data-work/BuildDirs/Slicer/Modules/Loadable/Tables/Widgets/Testing/Cxx/qSlicerTableColumnPropertiesWidgetTest1.cxx:46:3: 
error: ‘QSurfaceFormat’ was not declared in this scope
    QSurfaceFormat format = QVTKOpenGLWidget::defaultFormat();
</code></pre>
<p>I didn’t think you could build it with QT5 from reading the build<br>
instructions. I’ll try using QT4 with the runfile installation.</p>

---

## Post #9 by @ihnorton (2017-09-30 13:26 UTC)

<p>Note that you can use Qt 4.8.7 from the system package manager:</p>
<p><code>sudo apt-get install qt4-dev-tools libqt4-dev libqt4-core libqt4-gui libqtwebkit-dev</code></p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Qt" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Qt</a></p>

---

## Post #10 by @codey (2017-09-30 18:57 UTC)

<p>I’ve got a successful build with this. Thanks</p>

---

## Post #11 by @codey (2017-10-09 14:12 UTC)

<p>I am not sure how I managed to get Slicer built. I am trying to build on<br>
another Ubuntu 16.04 and I have run into the same issues.</p>
<pre><code class="lang-auto">/usr/bin/cmake: relocation error: 
/usr/lib/x86_64-linux-gnu/libcurl.so.4: symbol SSL_CTX_set_alpn_protos, 
version OPENSSL_1.0.2 not defined in file libssl.so.1.0.0 with link time 
reference
CMakeFiles/OpenSSL.dir/build.make:109: recipe for target 
'OpenSSL-prefix/src/OpenSSL-stamp/OpenSSL-configure' failed
make[2]: *** [OpenSSL-prefix/src/OpenSSL-stamp/OpenSSL-configure] Error 127
CMakeFiles/Makefile2:1267: recipe for target 
'CMakeFiles/OpenSSL.dir/all' failed
make[1]: *** [CMakeFiles/OpenSSL.dir/all] Error 2
Makefile:94: recipe for target 'all' failed
make: *** [all] Error 2
</code></pre>
<p>The choices of openssl are set in the cmake file</p>
<p>set_property(CACHE OPENSSL_DOWNLOAD_VERSION PROPERTY STRINGS “1.0.1e”<br>
“1.0.1l”)</p>
<p>I think they might not be compatible with the openssl I have installed.<br>
I posted this on AskUbuntu here</p>
<aside class="onebox stackexchange">
  <header class="source">
      <a href="https://askubuntu.com/questions/963299/building-3d-slicer-from-source-openssl-error" target="_blank" rel="nofollow noopener">askubuntu.com</a>
  </header>
  <article class="onebox-body">
      <a href="https://askubuntu.com/users/56192/codey-mccodeface" target="_blank" rel="nofollow noopener">
    <img alt="Codey McCodeface" src="https://www.gravatar.com/avatar/e63b988c8e9ca7e0e335b326bbbe94d4?s=128&amp;d=identicon&amp;r=PG" class="thumbnail onebox-avatar" width="128" height="128">
  </a>
<h4>
  <a href="https://askubuntu.com/questions/963299/building-3d-slicer-from-source-openssl-error" target="_blank" rel="nofollow noopener">Building 3D Slicer from source: openssl error</a>
</h4>

<div class="tags">
  <strong>openssl</strong>
</div>

<div class="date">
  asked by
  
  <a href="https://askubuntu.com/users/56192/codey-mccodeface" target="_blank" rel="nofollow noopener">
    Codey McCodeface
  </a>
  on <a href="https://askubuntu.com/questions/963299/building-3d-slicer-from-source-openssl-error" target="_blank" rel="nofollow noopener">10:56AM - 09 Oct 17 UTC</a>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>One comment says,</p>
<p>OpenSSL 1.0.x built from source does not include versioned symbols.<br>
However the Ubuntu supplied OpenSSL has a patch which does include<br>
versioned symbols. The error message above mentions a symbol version<br>
(OPENSSL_1.0.2) so there is some confusion between the two OpenSSL<br>
versions (i.e. the system installed version and the one downloaded and<br>
built from source)</p>

---
