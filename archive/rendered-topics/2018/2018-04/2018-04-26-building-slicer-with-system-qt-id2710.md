---
topic_id: 2710
title: "Building Slicer With System Qt"
date: 2018-04-26
url: https://discourse.slicer.org/t/2710
---

# Building slicer with system QT

**Topic ID**: 2710
**Date**: 2018-04-26
**URL**: https://discourse.slicer.org/t/building-slicer-with-system-qt/2710

---

## Post #1 by @vegoria (2018-04-26 18:05 UTC)

<p>Hi,<br>
I’m trying to compile slicer for the first time - but when I try to compile QT webkit I get an error: conflicting declaration ‘typedef int32_t UChar32’<br>
In manual I found information that I can use qt from system package, but when i try to compile it using:<br>
$CMAKE_BIN -DCMAKE_BUILD_TYPE:STRING=Release -DQT_QMAKE_EXECUTABLE:FILEPATH=/usr/bin/qmake-qt4 …/Slicer-Source/Slicer<br>
I got an “missing QTOPENGL” error.<br>
I was searching in the Internet but I wasn’t able to find solution. Could anybody give me any advise/clue? Its third day and I made no progress in compilig it…</p>

---

## Post #2 by @tavaughan (2018-04-26 18:21 UTC)

<p>Hi Sylwia,</p>
<p>You’re using Linux? I had issues in Ubuntu/Pop_OS. You could try following the steps that I took and see if they help:</p>
<aside class="quote quote-modified" data-post="21" data-topic="2576">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tavaughan/48/1475_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/compile-errors-pop-os-ubuntu-with-qt-5-10/2576/21">Compile errors Pop!_OS/Ubuntu with Qt 5.10</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    I now have Slicer building and running without fiddling with LD_LIBRARY_PATH. I think the issue was with the Build-qt.sh script. 
Steps: 

Install Qt dependencies (for QtWebEngine-specific dependencies I referred to this page <a href="https://wiki.qt.io/QtWebEngine/How_to_Try" rel="noopener nofollow ugc">https://wiki.qt.io/QtWebEngine/How_to_Try</a> )
Download the Qt-build script as per <a href="https://github.com/jcfr/qt-easy-build/tree/5.10.0#readme" rel="noopener nofollow ugc">https://github.com/jcfr/qt-easy-build/tree/5.10.0#readme</a>

Open the script in a text editor. Scroll to the configure step near the end of the file (line 365 at time of writing). Change the -no-rp…
  </blockquote>
</aside>

<p>Note that I built Qt5 using the qt-easy-build scripts, I did not try to use a system install of Qt.</p>
<p>Thomas</p>

---

## Post #3 by @chir.set (2018-04-26 19:46 UTC)

<p>Slicer developers <a href="https://discourse.slicer.org/t/slicer-nightly-does-not-build-with-qt4-vtk7/2631/4">recommend</a> building against Qt5.</p>
<p>On my host running Arch Linux, the following configuration builds nicely :</p>
<blockquote>
<p>cmake -DSlicer_VTK_VERSION_MAJOR:INT=9 -DQt5_DIR:PATH=/usr/lib/cmake/Qt5 -DSlicer_USE_PYTHONQT_WITH_OPENSSL:BOOL=0 -DBUILD_TESTING:BOOL=0 -DCMAKE_BUILD_TYPE:STRING=Release …/Slicer</p>
</blockquote>
<p>You should adapt Qt5_DIR parameter to your distribution.</p>
<p>If you really want Qt4, I guess you’ll be having a hard time and few help. In any case, Qt4 support is scheduled to be deprecated, as far as I understood.</p>

---

## Post #4 by @vegoria (2018-04-26 20:03 UTC)

<p>Ok, thanks <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"> I’ll try to build it with Qt5 <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #5 by @vegoria (2018-05-01 14:04 UTC)

<p>Ok, I tried to compile slicer with Qt5. (I’m using linux mint).<br>
Configuration that I’m using to compile Slicer:</p>
<blockquote>
<p>$CMAKE_BIN -DQT_QMAKE_EXECUTABLE:FILEPATH=/home/software/medical/slicer/Slicer-Build-Support/qt-everywhere-build-5.10.0/bin/qmake -DQt5_DIR=/home/software/medical/slicer/Slicer-Build-Support/qt-everywhere-build-5.10.0/lib/cmake/Qt5 -DCMAKE_BUILD_TYPE:STRING=Release -DCMAKE_PREFIX_PATH:PATH=/home/software/medical/slicer/Slicer-Build-Support/qt-everywhere-build-5.10.0/bin/ -DSlicer_USE_PYTHONQT_WITH_TCL:BOOL=OFF -DSlicer_USE_SimpleITK:BOOL=OFF -DSlicer_USE_QtTesting:BOOL=OFF -DSlicer_VTK_VERSION_MAJOR:STRING=9 -DSlicer_VTK_RENDERING_BACKEND:STRING=OpenGL2 -DSlicer_BUILD_DataStore:BOOL=OFF …/Slicer-Source/Slicer/</p>
</blockquote>
<p>But I get an error:</p>
<blockquote>
<p>Call Stack (most recent call first):<br>
CMake/SlicerBlockFindQtAndCheckVersion.cmake:36 (find_package)<br>
CMake/SlicerBlockFindQtAndCheckVersion.cmake:110 (__SlicerBlockFindQtAndCheckVersion_find_qt)<br>
CMakeLists.txt:607 (include)</p>
<p>CMake Warning at CMake/SlicerBlockFindQtAndCheckVersion.cmake:36 (find_package):<br>
Found package configuration file:</p>
<pre><code>/home/software/medical/slicer/Slicer-Build-Support/qt-everywhere-build-5.10.0/lib/cmake/Qt5/Qt5Config.cmake
</code></pre>
<p>but it set Qt5_FOUND to FALSE so package “Qt5” is considered to be NOT<br>
FOUND.  Reason given by package:</p>
<p>Failed to find Qt5 component “WebEngine” config file at<br>
“/home/software/medical/slicer/Slicer-Build-Support/qt-everywhere-build-5.10.0/lib/cmake/Qt5WebEngine/Qt5WebEngineConfig.cmake”</p>
<p>Failed to find Qt5 component “WebEngineWidgets” config file at<br>
“/home/software/medical/slicer/Slicer-Build-Support/qt-everywhere-build-5.10.0/lib/cmake/Qt5WebEngineWidgets/Qt5WebEngineWidgetsConfig.cmake”</p>
</blockquote>

---

## Post #6 by @ihnorton (2018-05-01 19:53 UTC)

<p>Try installing <code>libqt5webengine5</code> and probably <code>qt5webengine-dev</code>. I think Slicer requires at least Qt 5.7 (note the qt-easy-build script mentioned by tavaughan may be easier if the distribution version is too old).</p>

---

## Post #7 by @vegoria (2018-05-10 08:55 UTC)

<p>How? By apt-get? Those packages does not exist.<br>
I’m installing qt5 using easy-build, but it does not compile web engine</p>

---

## Post #8 by @ihnorton (2018-05-10 13:28 UTC)

<p>You need to install all of the dependencies <a href="https://wiki.qt.io/QtWebEngine/How_to_Try#Installing_dependencies_on_Ubuntu">listed here</a>. I built Qt 5.10 recently on Ubuntu 16.04 starting from those instructions. I don’t remember if they were complete, but <a href="https://gist.github.com/ihnorton/bdce68c56344610f2ab071374e9b7908">here are all the packages I installed to be able to compile</a>.</p>
<p>Unfortunately WebEngine is rather tricky to compile because the build system is layered in such a way that it does not give very good feedback during configuration about <a href="http://lists.qt-project.org/pipermail/interest/2018-April/029850.html">why webengine was skipped</a>.</p>

---

## Post #9 by @vegoria (2018-10-07 15:27 UTC)

<p>Ok, I’m returning to this old topic… Previously I managed to install Slicer with older version of Qt, but as I reinstalled my system and had to install Slicer again I decided to make it with Qt5.<br>
I’ve stuck again in this webengine installation… But when I tried to complie webkit separatelly I have a message:</p>
<p>“A suitable version of dbus could not be found.<br>
QtWebEngine will not be built.”</p>
<p>Anyone know which is this ‘suitable version’ of dbus and how to install it?<br>
When I’m makind apt-get dbus I receive message that dbus is already installed<br>
System: linux mint 19 Tara,<br>
Qt: using easy build script, so it is 5.10.0</p>

---

## Post #10 by @lassoan (2018-10-07 16:05 UTC)

<p>You should still be able to build Slicer with Qt4. We’ll probably remove Slicer’s QtWebEngine dependency shortly after releasing Slicer-4.10.</p>
<p>So, a solution can be to keep using Qt4 for now and switch to Qt5 when QtWebEngine is not needed for Slicer anymore (probably within a few months).</p>

---

## Post #11 by @vegoria (2018-10-07 16:38 UTC)

<p>Well I’m kind of stubborn person, and I’m irritated when I don’t know how to do something, so I would prefer to manage compile Slicer with Qt5 <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=6" title=":wink:" class="emoji" alt=":wink:"></p>

---

## Post #12 by @jcfr (2018-10-07 21:47 UTC)

<p>If you build against Qt5, do not pass QT_QMAKE_EXECUTABLE, only Qt5_DIR.</p>

---

## Post #13 by @vegoria (2018-10-08 04:40 UTC)

<p>Yes, but first I have to compile this version of Qt. When I try to compile qt4 on new linux distribution I get compilation errors. And when I try to compile qt5 I cannot compile webengine - some missing dependency probably, but I don’t know which dependency <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=6" title=":frowning:" class="emoji" alt=":frowning:"></p>

---

## Post #14 by @jcfr (2018-10-08 12:04 UTC)

<p>To clarify, in you first message, you indicated that the command:</p>
<aside class="quote no-group" data-username="vegoria" data-post="5" data-topic="2710">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/v/85f322/48.png" class="avatar"> vegoria:</div>
<blockquote>
<p>$CMAKE_BIN <br>
-DQT_QMAKE_EXECUTABLE:FILEPATH=/home/software/medical/slicer/Slicer-Build-Support/qt-everywhere-build-5.10.0/bin/qmake <br>
-DQt5_DIR=/home/software/medical/slicer/Slicer-Build-Support/qt-everywhere-build-5.10.0/lib/cmake/Qt5   <br>
-DCMAKE_BUILD_TYPE:STRING=Release <br>
-DCMAKE_PREFIX_PATH:PATH=/home/software/medical/slicer/Slicer-Build-Support/qt-everywhere-build-5.10.0/bin/ <br>
-DSlicer_USE_PYTHONQT_WITH_TCL:BOOL=OFF <br>
-DSlicer_USE_SimpleITK:BOOL=OFF <br>
-DSlicer_USE_QtTesting:BOOL=OFF <br>
-DSlicer_VTK_VERSION_MAJOR:STRING=9 <br>
-DSlicer_VTK_RENDERING_BACKEND:STRING=OpenGL2 <br>
-DSlicer_BUILD_DataStore:BOOL=OFF <br>
…/Slicer-Source/Slicer/</p>
</blockquote>
</aside>
<p>failed with</p>
<blockquote>
<p>Failed to find Qt5 component “WebEngine” config file at<br>
“/home/software/medical/slicer/Slicer-Build-Support/qt-everywhere-build-5.10.0/lib/cmake/Qt5WebEngine/Qt5WebEngineConfig.cmake”</p>
<p>Failed to find Qt5 component “WebEngineWidgets” config file at<br>
“/home/software/medical/slicer/Slicer-Build-Support/qt-everywhere-build-5.10.0/lib/cmake/Qt5WebEngineWidgets/Qt5WebEngineWidgetsConfig.cmake”</p>
</blockquote>
<p>could  you instead try the following:</p>
<pre><code class="lang-auto">$CMAKE_BIN \
  -DQt5_DIR=/home/software/medical/slicer/Slicer-Build-Support/qt-everywhere-build-5.10.0/lib/cmake/Qt5   \
  -DCMAKE_BUILD_TYPE:STRING=Release \
  -DSlicer_USE_PYTHONQT_WITH_TCL:BOOL=OFF \
  -DSlicer_USE_SimpleITK:BOOL=OFF \
  -DSlicer_USE_QtTesting:BOOL=OFF \
  -DSlicer_BUILD_DataStore:BOOL=OFF \
  ../Slicer-Source/Slicer/
</code></pre>
<ul>
<li>The argument <code>QT_QMAKE_EXECUTABLE</code> should NOT be specified along with <code>Qt5_DIR</code></li>
<li>The argument <code>CMAKE_PREFIX_PATH</code> is not needed, the recommended way are to pass <code>Qt5_DIR</code> or <code>QT_QMAKE_EXECUTABLE</code></li>
<li>Passing <code>Slicer_VTK_RENDERING_BACKEND</code> or <code>Slicer_VTK_VERSION_MAJOR</code> are not needed, these will be automatically set based on <code>Qt5_DIR</code> or <code>QT_QMAKE_EXECUTABLE</code></li>
<li>Finally, make sure to run the configure command in a clean build directory</li>
</ul>
<p>Last, could you also check that <code>Qt5WebEngineConfig.cmake</code> exists in your install of Qt5, if not make sure you select the corresponding component during installation. For example, see selected components <a href="https://github.com/Slicer/SlicerBuildEnvironment/blob/1de3dc02b8ce96f9f132b0d7e45b95f17a646b2c/Docker/qt5-centos7/qt-installer-noninteractive.qs#L51-L54">here</a>.</p>

---
