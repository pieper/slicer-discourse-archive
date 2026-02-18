# Build Error PythonQt Visual Studio 2015 Qt 5.9.2

**Topic ID**: 1411
**Date**: 2017-11-08
**URL**: https://discourse.slicer.org/t/build-error-pythonqt-visual-studio-2015-qt-5-9-2/1411

---

## Post #1 by @danielbr (2017-11-08 21:40 UTC)

<p>Trying to build slicer 4.8.0 with Qt 5.9.2.  I get really close to a full complete build, but PythonQt in CTK fails everytime with a laundry list of errors.  I am using Visual Studio 2015 I turned off Slicer_USE_PYTHONQT_WITH_OPENSSL.  I also tried turning off Slicer_USE_PYTHONQT_WITH_TCL and had the exact same result.  I have attached my build output, but the problem seems to be with QOpenGLTimeMonitor.  Anyone have any suggestions?</p>
<p>For reference I built Qt with the following configure (configure -prefix D:/Qt/5926415R -release -opensource -confirm-license -platform win32-msvc2015 -nomake examples -nomake tests -openssl -I D:/OpenSSL/OpenSSL-64VS15/include -L D:/OpenSSL/OpenSSL-64VS15)</p>
<p>Build output here:</p>
<p><a href="https://pastebin.com/wQEREi25" rel="nofollow noopener">Build Output</a></p>
<p>I should note that I also tried the latest commit of slicer 4.9.0 as of today and got the same error.</p>

---

## Post #2 by @ihnorton (2017-11-08 22:16 UTC)

<p>Did you follow the instructions here?: <a href="https://www.slicer.org/wiki/Documentation/Labs/Qt5-and-VTK8#Status">https://www.slicer.org/wiki/Documentation/Labs/Qt5-and-VTK8#Status</a></p>
<p>I did that a few weeks ago, with no other changes, and successfully built against Qt 5.9.2 (VS2015 lib) installed with the Qt installer. 28 tests fail, but I think most of them are known issues.</p>

---

## Post #3 by @danielbr (2017-11-08 22:26 UTC)

<p>Yep I changed the Slicer_REQUIRED_QT_VERSION to 5.9.2 which made the QT5_DIR come up and then I set that to my qtdirectory/lib/cmake/Qt5.</p>

---

## Post #4 by @jcfr (2017-11-08 22:46 UTC)

<p>From an empty directory, if you configure using:</p>
<pre><code class="lang-auto">cmake -DQt5_DIR:PATH=... 
</code></pre>
<p>There is no need to manually set <code>Slicer_REQUIRED_QT_VERSION</code>.</p>
<p>If you are using cmake-gui or ccmake, just make sure you are <strong>NOT</strong> configuring a first time and then setting the <code>Qt5_DIR</code> variable.</p>
<p>You need to set the <code>Qt5_DIR</code> variable the first time you configure. That way all default values are properly initialized.</p>

---

## Post #5 by @jcfr (2017-11-08 22:49 UTC)

<aside class="quote no-group" data-username="danielbr" data-post="1" data-topic="1411">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/c2a13f/48.png" class="avatar"> danielbr:</div>
<blockquote>
<p>I built Qt with the following configure</p>
</blockquote>
</aside>
<p>Waiting we test and finalize updates associated with building Qt from source, there is no problem downloading existing binaries. It just mean that if you do a debug build, you will not be able to use the QtDesigner or QtCreator and make use of the custom designer/QtCreator plugins offered by CTK and Slicer to design UI</p>

---

## Post #6 by @danielbr (2017-11-08 23:04 UTC)

<p>ok I will try this in a new directory.  I will let it build overnight and see if that solves the issue.  I will report back.  Thanks!</p>

---

## Post #7 by @danielbr (2017-11-09 13:32 UTC)

<p>Still not building pythonQt.  So I am using the cmake gui.  I created a new directory opened the cmake gui and set Qt5_DIR and QT_QMAKE_EXECUTABLE before configuring.  Configured generated and opened the project.  Started the build.  Again most everything built but it is still failing to build pythonQt.  The first error occurs at recognizing QOpenGLTimeMonitor…  Any other suggestions to get this working?</p>

---

## Post #8 by @lassoan (2017-11-09 14:13 UTC)

<p>I usually create a .bat file that configures CMake using -D parameters. It is less work and more reproducible than setting CMake variables manually each time I need a clean rebuild.</p>

---

## Post #9 by @ihnorton (2017-11-09 14:17 UTC)

<p>FWIW, here’s the selections I used with the Qt online installer. I would also suggest to build from top-of-trunk because there are continuous improvements, and targeting 4.8 because it’s a “release” is meaningless for a non-default configuration.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89ecb534331a6837c039da82f783fd35473e8562.jpeg" data-download-href="/uploads/short-url/jG8yzxGNZeTOR5TqMpdiaGGeqLE.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/89ecb534331a6837c039da82f783fd35473e8562_2_690x352.jpg" alt="image" data-base62-sha1="jG8yzxGNZeTOR5TqMpdiaGGeqLE" width="690" height="352" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/89ecb534331a6837c039da82f783fd35473e8562_2_690x352.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/89ecb534331a6837c039da82f783fd35473e8562_2_1035x528.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89ecb534331a6837c039da82f783fd35473e8562.jpeg 2x" data-dominant-color="F0F1F2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1280×654 361 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #10 by @danielbr (2017-11-09 21:44 UTC)

<p>Ok I installed Qt using the Qt installer with the options you suggested.  Everything built this time except for python.  Python says “unresolved external symbol _Py_silent_invalid_parameter_handler referenced in function new_threadstate” in the libpython-shared project.  I am used the top of the trunk for this build.  Any ideas to solve this last problem?</p>

---

## Post #11 by @ihnorton (2017-11-09 23:14 UTC)

<p>Remove the <code>superbuild/[Python-2.7.13, python-build, python-prefix]</code> directories and build again. Should be fixed by the following, but I don’t know if the commit was bumped in slicer yet:</p>
<p><a href="https://github.com/python-cmake-buildsystem/python-cmake-buildsystem/pull/195" class="onebox" target="_blank">https://github.com/python-cmake-buildsystem/python-cmake-buildsystem/pull/195</a></p>

---

## Post #12 by @jcfr (2017-11-09 23:33 UTC)

<aside class="quote no-group" data-username="danielbr" data-post="7" data-topic="1411">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/c2a13f/48.png" class="avatar"> danielbr:</div>
<blockquote>
<p>I created a new directory opened the cmake gui and set Qt5_DIR and QT_QMAKE_EXECUTABLE before configuring</p>
</blockquote>
</aside>
<p>Only <code>Qt5_DIR</code> should be set. <code>QT_QMAKE_EXECUTABLE</code> was specific to Qt4 configuration.</p>

---

## Post #13 by @jcfr (2017-11-09 23:34 UTC)

<aside class="quote no-group" data-username="ihnorton" data-post="11" data-topic="1411">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p>Should be fixed by the following, but I don’t know if the commit was bumped in slicer</p>
</blockquote>
</aside>
<p><s>Not yet. It will be done shortly.</s> <strong>Done</strong> - See <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26559">r26559</a></p>

---

## Post #14 by @danielbr (2017-11-09 23:56 UTC)

<p>Gonna try not setting QT_QMAKE_EXECUTABLE and rebuild fresh.  Will let it run overnight.  Will report back if I have success.  Thanks for all of the help.  One of these times it is going to build!</p>

---

## Post #15 by @jcfr (2017-11-10 00:04 UTC)

<p>You are welcome.</p>
<p>It should really be a seamless experience. We will try to improve things.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/ihnorton">@ihnorton</a> For some time  I have been thinking about creating a “SlicerDevelopmentEnvironment” project on GitHub where we would keep:</p>
<p>This would ne lightweight and allow to store:</p>
<ul>
<li>batch/shell script to build Slicer</li>
<li>and other misc scripts</li>
</ul>
<p>Or we could commit batch script directly to Slicer repo.</p>
<p>Here is what was done for ITK: <a href="https://github.com/InsightSoftwareConsortium/ITKDevelopmentEnvironment">https://github.com/InsightSoftwareConsortium/ITKDevelopmentEnvironment</a></p>

---

## Post #16 by @ihnorton (2017-11-10 12:45 UTC)

<p>A post was split to a new topic: <a href="/t/windows-build-scripts-and-simplification/1431">Windows build scripts and simplification</a></p>

---

## Post #17 by @ihnorton (2017-11-10 12:46 UTC)

<p>(I moved my response to a new topic because it is not directly related to the original post)</p>

---

## Post #18 by @danielbr (2017-11-10 15:14 UTC)

<p>Ok it worked!  I was able to build it finally.  Now I have one last issue that I need to solve.  When I open slicer it complains that the OpenGL Core Profile was requested but it is not supported on my current platform…  I assumed this must me a graphics card driver issue.  I have the NVIDIA NVS 315 which is supposed to support OpenGL.  I tried updating the drivers to the latest, but slicer still complains and says it is not supported.  Any ideas of how to remedy this?</p>

---

## Post #19 by @ihnorton (2017-11-10 15:46 UTC)

<aside class="quote no-group" data-username="danielbr" data-post="18" data-topic="1411">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/c2a13f/48.png" class="avatar"> danielbr:</div>
<blockquote>
<p>OpenGL Core Profile was requested but it is not supported on my current platform</p>
</blockquote>
</aside>
<p>This comes from QWebEngine, and I believe it is a known issue with the initialization. GL/VTK stuff in Slicer proper should work fine.</p>

---
