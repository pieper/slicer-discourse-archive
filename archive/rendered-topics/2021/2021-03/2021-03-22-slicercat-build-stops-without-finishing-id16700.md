---
topic_id: 16700
title: "Slicercat Build Stops Without Finishing"
date: 2021-03-22
url: https://discourse.slicer.org/t/16700
---

# SlicerCAT build stops without finishing

**Topic ID**: 16700
**Date**: 2021-03-22
**URL**: https://discourse.slicer.org/t/slicercat-build-stops-without-finishing/16700

---

## Post #1 by @keri (2021-03-22 19:56 UTC)

<p>Hi,</p>
<p>I’ve started to develop custom <a href="https://github.com/TierraColada/Colada" rel="noopener nofollow ugc">slicer app for geoscience</a>. I follow SlicerCAT strategy and as examples I use <a href="https://gitlab.kitware.com/aeva/aevaslicer/-/tree/master/" rel="noopener nofollow ugc">aevaSlicer</a> and <a href="https://github.com/Punzo/SlicerAstro" rel="noopener nofollow ugc">SlicerAstro</a></p>
<p>My slicerCAT has two additional dependencies:</p>
<ul>
<li>
<a href="https://github.com/TierraColada/h5geo" rel="noopener nofollow ugc">h5geo</a> is a C++ library</li>
<li>
<a href="https://pypi.org/project/GDAL/" rel="noopener nofollow ugc">GDAL</a> is a C++ library but I’m trying to install it with python (it has python bindings and it is supposed to be used in both C++ and python)</li>
</ul>
<p>I also turn on C++17 flag (h5geo needs it) and turn VTK 9 (as I remember there were problems with VTK 8.2.0 and C++17) as it is done in aevaSlicer.</p>
<p>I build it with commands:</p>
<ul>
<li>
<p>mkdir C:\C\d</p>
</li>
<li>
<p>cd C:\C\d</p>
</li>
<li>
<p>“C:/Qt/Tools/CMake_64/bin/cmake.exe” -G “Visual Studio 16 2019” -A x64 -DQt5_DIR:PATH=C:/Qt/5.15.2/msvc2019_64/lib/cmake/Qt5 C:/C/Colada</p>
</li>
<li>
<p>“C:/Qt/Tools/CMake_64/bin/cmake.exe” --build . --config Debug</p>
</li>
</ul>
<p>The build process has errors while building python but it continues building. After some more packages are successfully built (including h5geo) the building process stops:</p>
<pre><code class="lang-auto">--------------- snippet output ------------------
  -- Up-to-date: C:/C/d/h5geo-install/lib/h5geo.dll
  Completed 'h5geo'
  Generate version-jqPlot.txt and license-jqPlot.txt
  Completed 'jqPlot'
  Performing update step for 'vtkAddon'
  Generate version-vtkAddon.txt and license-vtkAddon.txt
  No patch step for 'vtkAddon'
  No configure step for 'vtkAddon'
  No build step for 'vtkAddon'
  No install step for 'vtkAddon'
  Completed 'vtkAddon'

C:\C\d&gt;
</code></pre>
<p>Thus some libraries were not built (as VTK for example) and thus the building process can’t seem to be finished successfully.<br>
What may be the reason of that?</p>
<p>I attach <a href="https://drive.google.com/file/d/1CmpIO28eknsqFYoNudoC7cKZg6VYGkxF/view?usp=sharing" rel="noopener nofollow ugc">full build log</a> and <a href="https://drive.google.com/file/d/1jl2W-LBXZhBqhiFD-I_dAZKa1ew8CSxh/view?usp=sharing" rel="noopener nofollow ugc">snippet of python error</a>.</p>
<p>Windows 10, MSVC 2019 x64, Qt 5.15.2</p>

---

## Post #2 by @lassoan (2021-03-23 05:44 UTC)

<p>Was the build successful when you built the default template (without adding h5geo and gdal)?</p>

---

## Post #3 by @keri (2021-03-23 10:31 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I’ve just tried to clean build (delete all and try slicerCAT again) it without my dependencies but with C++17 enbaled, <code>Slicer_BUILD_DICOM_SUPPORT</code> disabled and two strings added:</p>
<pre><code class="lang-auto"># Force VTK9
set(Slicer_VTK_VERSION_MAJOR 9 CACHE STRING "VTK major version (8 or 9)")
mark_as_superbuild(Slicer_VTK_VERSION_MAJOR)
</code></pre>
<p>The behaviour is the same.<br>
Last lines of output are:</p>
<pre><code class="lang-auto">  Creating directories for 'vtkAddon'
  Performing download step (git clone) for 'vtkAddon'
  Cloning into 'vtkAddon'...
  Note: switching to '4a5061920f6f72a2ddff6932176f7de2661b5f76'.

  You are in 'detached HEAD' state. You can look around, make experimental
  changes and commit them, and you can discard any commits you make in this
  state without impacting any branches by switching back to a branch.

  If you want to create a new branch to retain commits you create, you may
  do so (now or later) by using -c with the switch command. Example:

    git switch -c &lt;new-branch-name&gt;

  Or undo this operation with:

    git switch -

  Turn off this advice by setting config variable advice.detachedHead to false

  HEAD is now at 4a50619 BUG: Fix tests execution on windows adding "vtkAddon_LAUNCH_COMMAND" option
  Performing update step for 'vtkAddon'
  Generate version-vtkAddon.txt and license-vtkAddon.txt
  No patch step for 'vtkAddon'
  No configure step for 'vtkAddon'
  No build step for 'vtkAddon'
  No install step for 'vtkAddon'
  Completed 'vtkAddon'
  Building Custom Rule C:/C/d/slicersources-src/CMakeLists.txt

C:\C\d&gt;
</code></pre>
<p>Few weeks ago there were not any problems building SlicerCAT but with C++11 and without VTK 9 enabled.<br>
So I suppose the problem is connected with it.</p>

---

## Post #4 by @lassoan (2021-03-23 12:09 UTC)

<p>Please retry the build, making one change at a time and let us know if you run into an issue that you don’t know how to resolve.</p>

---

## Post #5 by @keri (2021-03-23 22:07 UTC)

<p>This time I only enabled C++17 and the compilation was successful for about 7 hours and then I got errors:</p>
<pre><code class="lang-auto">    vtkOrientedImageData.cxx
    vtkOrientedImageDataResample.cxx
    vtkSegment.cxx
    vtkSegmentation.cxx
C:\C\d\slicersources-src\Libs\vtkSegmentationCore\vtkSegmentation.cxx(60,53): error C2143: syntax error: missing ',' be
fore '&lt;' [C:\C\d\Slicer-build\Libs\vtkSegmentationCore\vtkSegmentationCore.vcxproj] [C:\C\d\slicersources-build\Slicer.
vcxproj]
  C:\C\d\slicersources-src\Libs\vtkSegmentationCore\vtkSegmentation.cxx(67): message : see reference to class template
  instantiation 'MapValueCompare&lt;T&gt;' being compiled [C:\C\d\Slicer-build\Libs\vtkSegmentationCore\vtkSegmentationCore.v
  cxproj]
C:\C\d\slicersources-src\Libs\vtkSegmentationCore\vtkSegmentation.cxx(60,24): error C2518: keyword 'typename' is invali
d in a base class list; expected a class name [C:\C\d\Slicer-build\Libs\vtkSegmentationCore\vtkSegmentationCore.vcxproj
] [C:\C\d\slicersources-build\Slicer.vcxproj]
C:\C\d\slicersources-src\Libs\vtkSegmentationCore\vtkSegmentation.cxx(60,78): error C2518: keyword 'typename' is invali
d in a base class list; expected a class name [C:\C\d\Slicer-build\Libs\vtkSegmentationCore\vtkSegmentationCore.vcxproj
] [C:\C\d\slicersources-build\Slicer.vcxproj]
C:\C\d\slicersources-src\Libs\vtkSegmentationCore\vtkSegmentation.cxx(471,58): error C2039: 'bind2nd': is not a member
of 'std' [C:\C\d\Slicer-build\Libs\vtkSegmentationCore\vtkSegmentationCore.vcxproj] [C:\C\d\slicersources-build\Slicer.
vcxproj]
  C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.28.29910\include\sstream(20): message
  : see declaration of 'std' [C:\C\d\Slicer-build\Libs\vtkSegmentationCore\vtkSegmentationCore.vcxproj]
C:\C\d\slicersources-src\Libs\vtkSegmentationCore\vtkSegmentation.cxx(60,38): error C2039: 'binary_function': is not a
member of 'std' [C:\C\d\Slicer-build\Libs\vtkSegmentationCore\vtkSegmentationCore.vcxproj] [C:\C\d\slicersources-build\
Slicer.vcxproj]
  C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.28.29910\include\sstream(20): message
  : see declaration of 'std' [C:\C\d\Slicer-build\Libs\vtkSegmentationCore\vtkSegmentationCore.vcxproj]
  C:\C\d\slicersources-src\Libs\vtkSegmentationCore\vtkSegmentation.cxx(471): message : see reference to class template
   instantiation 'MapValueCompare&lt;vtkSegmentation::SegmentMap&gt;' being compiled [C:\C\d\Slicer-build\Libs\vtkSegmentatio
  nCore\vtkSegmentationCore.vcxproj]
C:\C\d\slicersources-src\Libs\vtkSegmentationCore\vtkSegmentation.cxx(60,24): error C2504: 'binary_function': base clas
s undefined [C:\C\d\Slicer-build\Libs\vtkSegmentationCore\vtkSegmentationCore.vcxproj] [C:\C\d\slicersources-build\Slic
er.vcxproj]
C:\C\d\slicersources-src\Libs\vtkSegmentationCore\vtkSegmentation.cxx(471,65): error C3861: 'bind2nd': identifier not f
ound [C:\C\d\Slicer-build\Libs\vtkSegmentationCore\vtkSegmentationCore.vcxproj] [C:\C\d\slicersources-build\Slicer.vcxp
roj]
C:\C\d\slicersources-src\Libs\vtkSegmentationCore\vtkSegmentation.cxx(538,56): error C2039: 'bind2nd': is not a member
of 'std' [C:\C\d\Slicer-build\Libs\vtkSegmentationCore\vtkSegmentationCore.vcxproj] [C:\C\d\slicersources-build\Slicer.
vcxproj]
  C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.28.29910\include\sstream(20): message
  : see declaration of 'std' [C:\C\d\Slicer-build\Libs\vtkSegmentationCore\vtkSegmentationCore.vcxproj]
C:\C\d\slicersources-src\Libs\vtkSegmentationCore\vtkSegmentation.cxx(538,63): error C3861: 'bind2nd': identifier not f
ound [C:\C\d\Slicer-build\Libs\vtkSegmentationCore\vtkSegmentationCore.vcxproj] [C:\C\d\slicersources-build\Slicer.vcxp
roj]
C:\C\d\slicersources-src\Libs\vtkSegmentationCore\vtkSegmentation.cxx(837,56): error C2039: 'bind2nd': is not a member
of 'std' [C:\C\d\Slicer-build\Libs\vtkSegmentationCore\vtkSegmentationCore.vcxproj] [C:\C\d\slicersources-build\Slicer.
vcxproj]
  C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.28.29910\include\sstream(20): message
  : see declaration of 'std' [C:\C\d\Slicer-build\Libs\vtkSegmentationCore\vtkSegmentationCore.vcxproj]
C:\C\d\slicersources-src\Libs\vtkSegmentationCore\vtkSegmentation.cxx(837,63): error C3861: 'bind2nd': identifier not f
ound [C:\C\d\Slicer-build\Libs\vtkSegmentationCore\vtkSegmentationCore.vcxproj] [C:\C\d\slicersources-build\Slicer.vcxp
roj]
</code></pre>
<p>Were there attempts to build Slicer with C++17?</p>

---

## Post #6 by @keri (2021-03-23 22:28 UTC)

<p>I’ve just found that <code>std::binary_function</code> is <a href="https://en.cppreference.com/w/cpp/utility/functional/binary_function" rel="noopener nofollow ugc">removed in C++17</a><br>
So this is the problem.</p>
<p>Could you recommend me something if my external dependencies need to use C++17 ?</p>

---

## Post #7 by @lassoan (2021-03-24 16:15 UTC)

<aside class="quote no-group" data-username="keri" data-post="6" data-topic="16700">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>So this is the problem.</p>
</blockquote>
</aside>
<p>This should not be a problem. You can rewrite that part of the code and send a pull request with the proposed change.</p>

---

## Post #8 by @keri (2021-03-25 19:17 UTC)

<p>With <a href="https://github.com/Slicer/Slicer/pull/5548" rel="noopener nofollow ugc">pull request</a>  I could compile Slicer with C++17 enabled</p>

---
