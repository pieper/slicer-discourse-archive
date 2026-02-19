---
topic_id: 8441
title: "Problem Installing Module For Compiled Slicer Version"
date: 2019-09-16
url: https://discourse.slicer.org/t/8441
---

# Problem installing module for compiled slicer version

**Topic ID**: 8441
**Date**: 2019-09-16
**URL**: https://discourse.slicer.org/t/problem-installing-module-for-compiled-slicer-version/8441

---

## Post #1 by @rbahegne (2019-09-16 10:01 UTC)

<p>Hello, i am a currently developing  a loadable module. I need some functionalities of other no native module (currently sequence module). I am encountering issue with the extension manager in the compiled (with my module) slicer version, i can’t see any module to install. But that’s not the real issue because i manage to install it from files quite easily but after installing it when i run slicer i get :</p>
<blockquote>
<p>Error(s):<br>
Cannot load library /home/raphaelbahegne/.config/NA-MIC/Extensions-f421157/Sequences/lib/Slicer-4.11/qt-loadable-modules/libqSlicerMetafileImporterModule.so: (libITKColormap-5.1.so.1: cannot open shared object file: No such file or directory)<br>
Error(s):<br>
Cannot load library /home/raphaelbahegne/.config/NA-MIC/Extensions-f421157/Sequences/lib/Slicer-4.11/qt-loadable-modules/libqSlicerSequenceBrowserModule.so: (libITKColormap-5.1.so.1: cannot open shared object file: No such file or directory)<br>
Error(s):<br>
Cannot load library /home/raphaelbahegne/.config/NA-MIC/Extensions-f421157/Sequences/lib/Slicer-4.11/qt-loadable-modules/libqSlicerSequencesModule.so: (libITKColormap-5.1.so.1: cannot open shared object file: No such file or directory)<br>
libITKDeprecated-5.1.so.1: cannot open shared object file: No such file or directory<br>
libITKColormap-5.1.so.1: cannot open shared object file: No such file or directory<br>
libITKColormap-5.1.so.1: cannot open shared object file: No such file or directory<br>
libITKColormap-5.1.so.1: cannot open shared object file: No such file or directory<br>
libITKColormap-5.1.so.1: cannot open shared object file: No such file or directory<br>
libITKColormap-5.1.so.1: cannot open shared object file: No such file or directory</p>
</blockquote>
<p>The “libqSlicer***” files exists and are at the right place so i thought i missed libITKColormap-5.1 or something and i tried to reinstall some ITK libs but it did’nt changed anything.</p>
<p>In the end only the Crop Volume Sequence is available. Too bad i needed the sequence browser <img src="https://emoji.discourse-cdn.com/twitter/expressionless.png?v=12" title=":expressionless:" class="emoji" alt=":expressionless:" loading="lazy" width="20" height="20"></p>
<p>Any hints ?<br>
Thank you</p>

---

## Post #2 by @lassoan (2019-09-17 00:34 UTC)

<aside class="quote no-group" data-username="rbahegne" data-post="1" data-topic="8441">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbahegne/48/4837_2.png" class="avatar"> rbahegne:</div>
<blockquote>
<p>I am encountering issue with the extension manager in the compiled (with my module) slicer version</p>
</blockquote>
</aside>
<p>If you build Slicer then you need to build all the extensions, too. In general, you cannot mix executables and shared objects built on different computers.</p>
<aside class="quote no-group" data-username="rbahegne" data-post="1" data-topic="8441">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbahegne/48/4837_2.png" class="avatar"> rbahegne:</div>
<blockquote>
<p>i missed libITKColormap-5.1 or something and i tried to reinstall some ITK libs</p>
</blockquote>
</aside>
<p>ITK is built by Slicer. You should not try to get some random ITK libraries and copy them into the Slicer build tree. If ITK libraries are missing then maybe your Slicer build has not completed successfully. Start again your Slicer build and check that there are no build errors.</p>

---

## Post #3 by @rbahegne (2019-09-17 09:54 UTC)

<p>OK, i see. I need to package any wanted extension in my custom build.</p>
<p>Thank you</p>

---

## Post #4 by @lassoan (2019-09-17 13:02 UTC)

<p>Yes. You can list extensions in CMake when you configure your Slicer build that you want to bundle in the install package.</p>

---
