---
topic_id: 4572
title: "Build Slicer 4 10 With Qt5 And Vtk 8 On Windows 10 Using Vs2"
date: 2018-10-29
url: https://discourse.slicer.org/t/4572
---

# Build Slicer 4.10 with Qt5 and VTK 8 on WIndows 10 using VS2015

**Topic ID**: 4572
**Date**: 2018-10-29
**URL**: https://discourse.slicer.org/t/build-slicer-4-10-with-qt5-and-vtk-8-on-windows-10-using-vs2015/4572

---

## Post #1 by @brhoom (2018-10-29 16:09 UTC)

<p>It seems the instruction page and the qt easy build need an update. I could not find a working-script to build Qt5 with ssl support. Does anyone build Slicer with the above configuration successfully?</p>

---

## Post #2 by @jamesobutler (2018-10-29 16:56 UTC)

<p>There isn’t a qt-easy-build script for Qt5w/openssl on Windows.  I issued a PR <a href="https://github.com/jcfr/qt-easy-build/pull/45" rel="nofollow noopener">https://github.com/jcfr/qt-easy-build/pull/45</a> awhile back that attempted to add the support.  Though I’ve been building Slicer on Windows by using the regular pre-built Qt5 binaries downloaded from the web. You can see <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions/Prerequisites/Qt5" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions/Prerequisites/Qt5</a> for instructions related to that.</p>

---

## Post #3 by @brhoom (2018-10-29 16:59 UTC)

<p>Thanks for your quick reply. I will try this.</p>

---

## Post #4 by @lassoan (2018-10-29 17:06 UTC)

<p>Where did you find instructions that told you need Qt5 with OpenSSL for building nightly versions?</p>
<p>The <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Common_Prerequisites_2">instructions that I’ve found</a> state that you need to use reqular Qt installer:</p>
<blockquote>
<p>Qt5 <strong>recommended and officially supported</strong> . Download <a href="https://download.qt.io/official_releases/online_installers/qt-unified-windows-x86-online.exe">qt-unified-windows-x86-online.exe</a> and install Qt along with qtscript and qtwebengine components. For building with VS2015, Qt version 5.10.x or older is required. For more details, read <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions/Prerequisites/Qt5">step-by-step</a> guide.</p>
</blockquote>

---

## Post #5 by @brhoom (2018-10-29 17:21 UTC)

<blockquote>
<p>Where did you find instructions that told you need Qt5 with OpenSSL for building nightly versions?</p>
</blockquote>
<p>I thought it is the same as qt4. I thought the page is not updated because of the part after this line</p>
<pre><code> svn co http://svn.slicer.org/Slicer4/&lt;MARKER&gt; Slicer-r&lt;SVNREVISION&gt; -r &lt;SVNREVISION&gt;
</code></pre>
<p>It does not include 4.10</p>

---

## Post #6 by @jamesobutler (2018-10-29 17:30 UTC)

<p>The default configuration in CMakeLists.txt specifies <a href="https://github.com/Slicer/Slicer/blob/master/CMakeLists.txt#L270" rel="nofollow noopener">enable PythonQt with openssl</a>. Maybe this should be set to “Off” if it isn’t truly the preferred configuration, otherwise you’ll end up with those QSslSocket error messages when starting Slicer. Or maybe update qt-easy-build to work for other platforms. Looks like right now it only passes on Mac for Qt 5.10.0.</p>

---

## Post #7 by @jcfr (2018-10-29 18:05 UTC)

<aside class="quote no-group quote-modified" data-username="jamesobutler" data-post="2" data-topic="4572">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>I issued a PR <a href="https://github.com/jcfr/qt-easy-build/pull/45" class="inline-onebox">Add Windows support for Qt 5.10.0 by jamesobutler · Pull Request #45 · jcfr/qt-easy-build · GitHub</a> awhile back that attempted to add the support.</p>
</blockquote>
</aside>
<p>Just to let you know your contribution wasn’t forgotten and will be integrated. The time being, building against he official Qt installer should work.</p>
<blockquote>
<p>otherwise you’ll end up with those QSslSocket error messages when starting Slicer</p>
</blockquote>
<p>Out of curiosity, is this already tracked by a Slicer issue ?</p>

---

## Post #8 by @jamesobutler (2018-10-29 19:14 UTC)

<p>No problem about the PR. It hasn’t been a top priority.</p>
<p>I actually forget to uncheck the PythonQt with openssl cmake entry when using the regular Qt5 downloaded from the official installer.  I get the following errors when starting Slicer:</p>
<pre><code class="lang-auto">qt.network.ssl: QSslSocket: cannot resolve SSL_set_alpn_protos
qt.network.ssl: QSslSocket: cannot resolve SSL_CTX_set_alpn_select_cb
qt.network.ssl: QSslSocket: cannot resolve SSL_get0_alpn_selected
</code></pre>
<p>I figured this was similar to one of the “Common Errors” in the Slicer build instructions. See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#.27QSslSocket.27_:_is_not_a_class_or_namespace_name" rel="nofollow noopener">here</a>. I don’t see any issue for that in the issue tracker, but I wouldn’t really call it a bug since it’s just an error with how I configured the build.</p>

---

## Post #9 by @brhoom (2018-10-30 18:28 UTC)

<p>The build works. Thanks everyone!</p>

---
