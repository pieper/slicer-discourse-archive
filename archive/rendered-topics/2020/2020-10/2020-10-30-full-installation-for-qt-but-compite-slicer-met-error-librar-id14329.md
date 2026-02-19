---
topic_id: 14329
title: "Full Installation For Qt But Compite Slicer Met Error Librar"
date: 2020-10-30
url: https://discourse.slicer.org/t/14329
---

# Full installation for Qt, but compite Slicer met error: "Library not found: Qt5Cored"

**Topic ID**: 14329
**Date**: 2020-10-30
**URL**: https://discourse.slicer.org/t/full-installation-for-qt-but-compite-slicer-met-error-library-not-found-qt5cored/14329

---

## Post #1 by @chenyx (2020-10-30 14:03 UTC)

<p>I use Cmake Gui to compile Slicer Source code download. The develop tools are:<br>
1.vs 2015<br>
2.Qt 5.13.1<br>
3. CMake &gt;3.15.1<br>
4.Git &gt;1.7.10</p>
<p>I add Qt5_DIR variable pointing to Qt5 folder : D:\Qt\Qt5.13.1\5.13.1\msvc2015_64\lib\cmake\Qt5<br>
and<br>
select my compiler:  Visual Studio 14 2015,</p>
<p>then the cmake eccor as the follow:<br>
Configuring VTK<br>
Slicer_VTK_RENDERING_BACKEND is OpenGL2<br>
Slicer_VTK_SMP_IMPLEMENTATION_TYPE is TBB<br>
Slicer_VTK_VERSION_MAJOR is 8<br>
CMake Error at D:/Qt/Qt5.13.1/5.13.1/msvc2015_64/lib/cmake/Qt5UiTools/Qt5UiToolsConfig.cmake:74 (message):<br>
Library not found: Qt5Cored<br>
Call Stack (most recent call first):<br>
D:/Qt/Qt5.13.1/5.13.1/msvc2015_64/lib/cmake/Qt5UiTools/Qt5UiToolsConfig.cmake:227 (_qt5_UiTools_process_prl_file)<br>
D:/Qt/Qt5.13.1/5.13.1/msvc2015_64/lib/cmake/Qt5/Qt5Config.cmake:28 (find_package)<br>
CMake/SlicerBlockFindQtAndCheckVersion.cmake:22 (find_package)<br>
CMake/SlicerBlockFindQtAndCheckVersion.cmake:67 (__SlicerBlockFindQtAndCheckVersion_find_qt)<br>
CMakeLists.txt:620 (include)</p>
<p>Why did i meet the error, but i choose full installation for Qt.</p>

---

## Post #2 by @jamesobutler (2020-10-30 17:29 UTC)

<p>It appears you are using Windows, so I would suggest that you follow the latest Windows build instructions if you are looking to build the <code>master</code> Slicer branch. Notable differences include using VS2019 to build and using Qt 5.15 instead.</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html" target="_blank" rel="noopener nofollow ugc">slicer.readthedocs.io</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="" height="">

<h3><a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html" target="_blank" rel="noopener nofollow ugc">Windows — 3D Slicer  documentation</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @chenyx (2020-10-31 05:54 UTC)

<p>Thank James for your reply.<br>
So different version VS tools will affect the building process.<br>
Indeed，i build the Slicer with</p>
<blockquote>
<p>master</p>
</blockquote>
<p>branch，but if i download the v4.11， should i must use VS2019 and Qt5.15 for compile？</p>

---

## Post #4 by @chenyx (2020-10-31 14:19 UTC)

<p>Today, i download the Qt 5.15 source code and VS 2019,<br>
and i use VS2019 Native Tools command Prompt to do the following instructions:<br>
1.cd to qtbase<br>
2.run configure ( <code>configure -prefix D:\Qt\qt-everywhere-build  -release -opensource -mp -platform win32-msvc -c++std c++11</code> )<br>
3.nmake &amp;&amp; nmake install<br>
Then i use Cmake GUI tool to compile Slicer code, but the cmake show me can not find <code>QtMultimedia</code> and <code>QtWebEngine</code></p>
<p>Can you enlight me the argument of Qt’s configure command?</p>

---

## Post #5 by @jamesobutler (2020-10-31 14:39 UTC)

<p>I don’t personally build Qt from source. I follow the directions as I linked above which says</p>
<blockquote>
<p><a href="https://www.qt.io/download-open-source" rel="noopener nofollow ugc">Qt5</a>: Download Qt universal installer and install Qt 5.15 components: MSVC2019 64-bit, Qt Script, Qt WebEngine.</p>
</blockquote>
<p>The gets the Qt binaries and I then build Slicer using the same configuration of VS2019 64bit.</p>

---

## Post #7 by @chenyx (2020-10-31 14:48 UTC)

<p>I just find the highest version Qt binary file is 5.14.X， the 5.15.X just only source code need to compile by myself.</p>

---

## Post #8 by @jamesobutler (2020-10-31 20:03 UTC)

<p>Have you downloaded the latest version of the Qt maintenance tool? Usually for the latest versions of Qt to show up to download, you have to have the latest maintenance tool. This could be achieved by redownloading the online installer. You may have to remove your current Qt install as well.</p>

---

## Post #9 by @chenyx (2020-11-01 10:12 UTC)

<p>Thanks， this time i use online tool to download the Qt5.15 succeeded. Thank you very much！！！</p>
<p>I chosen offline to download source code with many problem，now i can happily compile the Slicer without any configure error.</p>
<p>Thank you again !!!</p>

---
