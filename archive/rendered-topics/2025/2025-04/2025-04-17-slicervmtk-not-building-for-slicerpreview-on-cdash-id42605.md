---
topic_id: 42605
title: "Slicervmtk Not Building For Slicerpreview On Cdash"
date: 2025-04-17
url: https://discourse.slicer.org/t/42605
---

# SlicerVMTK not building for SlicerPreview on cdash

**Topic ID**: 42605
**Date**: 2025-04-17
**URL**: https://discourse.slicer.org/t/slicervmtk-not-building-for-slicerpreview-on-cdash/42605

---

## Post #1 by @chir.set (2025-04-17 17:11 UTC)

<p>SlicerVMTK is not building on cdash for SlicerPreview while it does build for SlicerStable. The error messages relate to the VMTK library itself.</p>
<p>FYI, hoping for an investigation.</p>

---

## Post #2 by @jamesobutler (2025-04-17 17:17 UTC)

<p>SlicerPreview is now using a version based on VTK 9.4.2 (<a href="https://github.com/Slicer/Slicer/commit/01624f0aa67be6a4522b8ce33319995ddd0eb421" class="inline-onebox" rel="noopener nofollow ugc">ENH: Update default VTK version in external project from 9.2 to 9.4 · Slicer/Slicer@01624f0 · GitHub</a>) while SlicerStable 5.8.x is using a version based on VTK 9.2.</p>
<p>See the below VTK commit which change <code>vtkCellLinks::BuildLinks</code> to no longer have an input as warned in the SlicerPreview <a href="https://slicer.cdash.org/viewBuildError.php?buildid=3762482" rel="noopener nofollow ugc">Windows build of SlicerVMTK</a>. This VTK commit was first part of the VTK 9.3 release.</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/Kitware/VTK/commit/6adb882209baddfed5cbd4eda4a06cc50e75ef6f">
  <header class="source">

      <a href="https://github.com/Kitware/VTK/commit/6adb882209baddfed5cbd4eda4a06cc50e75ef6f" target="_blank" rel="noopener nofollow ugc">github.com/Kitware/VTK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Kitware/VTK/commit/6adb882209baddfed5cbd4eda4a06cc50e75ef6f" target="_blank" rel="noopener nofollow ugc">vtkAbstractCellLinks: Use SetDataSet/BuildLinks instead of BuildLinks(dataset)</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2022-11-11" data-time="15:21:35" data-timezone="UTC">03:21PM - 11 Nov 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/spyridon97" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/32746433?v=4" class="onebox-avatar-inline" width="20" height="20">
          spyridon97
        </a>
      </div>

      <div class="lines" title="changed 17 files with 382 additions and 180 deletions">
        <a href="https://github.com/Kitware/VTK/commit/6adb882209baddfed5cbd4eda4a06cc50e75ef6f" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+382</span>
          <span class="removed">-180</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">vtkAbstractCellLinks now use the SetDataSet/BuildLinks like vtkLocators instead <span class="show-more-container"><a href="https://github.com/Kitware/VTK/commit/6adb882209baddfed5cbd4eda4a06cc50e75ef6f" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">of
BuildLinks(dataset) which has been deprecated. Because of this change now we are
able to store built time and check the dataset time to avoid unnecessary rebuilding
of the links. Also deprecated vtkUnstructuredGrid::GetCellLinks() function.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @chir.set (2025-04-17 18:40 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="42605">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>a version based on VTK 9.4.2</p>
</blockquote>
</aside>
<p>Thank you for the information, at least I know the source of this issue.</p>

---

## Post #4 by @chir.set (2025-04-17 21:01 UTC)

<p>When Slicer is built with VTK 9.4, in <code>VTK-build/Common/Core/vtkVersionMacros.h</code>, there is</p>
<blockquote>
<p><span class="hashtag-raw">#define</span> VTK_MINOR_VERSION 2</p>
</blockquote>
<p>In my former build with VTK 9.2, this file contains:</p>
<blockquote>
<p><span class="hashtag-raw">#define</span> VTK_BUILD_VERSION 20230607</p>
</blockquote>
<p>SlicerVMTK could be built with Slicer/VTK9.4 with this patch:</p>
<pre><code class="lang-auto">diff --git a/vtkVmtk/ComputationalGeometry/vtkvmtkSimplifyVoronoiDiagram.cxx b/vtkVmtk/ComputationalGeometry/vtkvmtkSimplifyVoronoiDiagram.cxx
index 3ac28f0..ebcad5a 100644
--- a/vtkVmtk/ComputationalGeometry/vtkvmtkSimplifyVoronoiDiagram.cxx
+++ b/vtkVmtk/ComputationalGeometry/vtkvmtkSimplifyVoronoiDiagram.cxx
@@ -195,8 +195,9 @@ int vtkvmtkSimplifyVoronoiDiagram::RequestData(
   //   return 0;
   //   }
   poly-&gt;SetPolys(currentPolys);
-  
-#if (VTK_MAJOR_VERSION &gt;= 9 &amp;&amp; VTK_MINOR_VERSION &gt;= 0 &amp;&amp; VTK_BUILD_VERSION &gt;= 20221108)
+ 
+// #if (VTK_MAJOR_VERSION &gt;= 9 &amp;&amp; VTK_MINOR_VERSION &gt;= 0 &amp;&amp; VTK_BUILD_VERSION &gt;= 20221108)
+#if (VTK_MAJOR_VERSION &gt;= 9 &amp;&amp; VTK_MINOR_VERSION &gt;= 0)
   currentLinks-&gt;SetDataSet(poly);
   currentLinks-&gt;BuildLinks();
 #else
@@ -296,7 +297,8 @@ int vtkvmtkSimplifyVoronoiDiagram::RequestData(
     // #pragma message "vtkvmtkSimplifyVoronoiDiagram::RequestData not functional. Must be updated based on Kitware/VTK@88efc809a"
     // vtkErrorMacro(&lt;&lt; "!");
     poly-&gt;SetPolys(currentPolys);
-#if (VTK_MAJOR_VERSION &gt;= 9 &amp;&amp; VTK_MINOR_VERSION &gt;= 0 &amp;&amp; VTK_BUILD_VERSION &gt;= 20221108)
+// #if (VTK_MAJOR_VERSION &gt;= 9 &amp;&amp; VTK_MINOR_VERSION &gt;= 0 &amp;&amp; VTK_BUILD_VERSION &gt;= 20221108)
+#if (VTK_MAJOR_VERSION &gt;= 9 &amp;&amp; VTK_MINOR_VERSION &gt;= 0)
     currentLinks-&gt;SetDataSet(poly);
     currentLinks-&gt;BuildLinks();
 #else
</code></pre>
<p>It’s probably not a definite fix, just a hint rather.</p>
<p><code>VTK_BUILD_VERSION</code> is not being rightly set in <code>vtkVersionMacros.h</code>.</p>

---

## Post #5 by @jamesobutler (2025-04-17 22:37 UTC)

<aside class="quote no-group quote-modified" data-username="chir.set" data-post="4" data-topic="42605">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>When Slicer is built with VTK 9.4, in <code>VTK-build/Common/Core/vtkVersionMacros.h</code>, there is</p>
<blockquote>
<p><span class="hashtag-raw">#define</span> VTK_MINOR_VERSION 2</p>
</blockquote>
</blockquote>
</aside>
<p>If this is a clean build of Slicer rather than incremental build it should be minor version of 4 and build version of 2. The build version is not a date because it is based on a released tag rather than a nightly dev build.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/VTK/blob/454bb391dff78c6ff463298a5143ab5b4f0aa083/CMake/vtkVersion.cmake#L2-L4">
  <header class="source">

      <a href="https://github.com/Slicer/VTK/blob/454bb391dff78c6ff463298a5143ab5b4f0aa083/CMake/vtkVersion.cmake#L2-L4" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/VTK</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/VTK/blob/454bb391dff78c6ff463298a5143ab5b4f0aa083/CMake/vtkVersion.cmake#L2-L4" target="_blank" rel="noopener nofollow ugc">CMake/vtkVersion.cmake</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/VTK/blob/454bb391dff78c6ff463298a5143ab5b4f0aa083/CMake/vtkVersion.cmake#L2-L4" rel="noopener nofollow ugc"><code>454bb391d</code></a>
</div>



    <pre class="onebox"><code class="lang-cmake">
      <ol class="start lines" start="2" style="counter-reset: li-counter 1 ;">
          <li>set(VTK_MAJOR_VERSION 9)</li>
          <li>set(VTK_MINOR_VERSION 4)</li>
          <li>set(VTK_BUILD_VERSION 2)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>and what is used in SlicerStable 5.8.x:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/VTK/blob/59ec450206012e86d4855bc669800499254bfc77/CMake/vtkVersion.cmake#L2-L4">
  <header class="source">

      <a href="https://github.com/Slicer/VTK/blob/59ec450206012e86d4855bc669800499254bfc77/CMake/vtkVersion.cmake#L2-L4" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/VTK</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/VTK/blob/59ec450206012e86d4855bc669800499254bfc77/CMake/vtkVersion.cmake#L2-L4" target="_blank" rel="noopener nofollow ugc">CMake/vtkVersion.cmake</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/VTK/blob/59ec450206012e86d4855bc669800499254bfc77/CMake/vtkVersion.cmake#L2-L4" rel="noopener nofollow ugc"><code>59ec45020</code></a>
</div>



    <pre class="onebox"><code class="lang-cmake">
      <ol class="start lines" start="2" style="counter-reset: li-counter 1 ;">
          <li>set(VTK_MAJOR_VERSION 9)</li>
          <li>set(VTK_MINOR_VERSION 2)</li>
          <li>set(VTK_BUILD_VERSION 20230607)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @chir.set (2025-04-18 08:45 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="5" data-topic="42605">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p><code>set(VTK_BUILD_VERSION 2)</code></p>
</blockquote>
</aside>
<p>It’s consistent then.</p>
<p>I am doing a clean Slicer build and here is the content of <code>vtkVersionMacros.h</code> in the build tree.</p>
<pre><code class="lang-auto">// SPDX-FileCopyrightText: Copyright (c) Ken Martin, Will Schroeder, Bill Lorensen
// SPDX-License-Identifier: BSD-3-Clause
#ifndef vtkVersionMacros_h
#define vtkVersionMacros_h

#include "vtkVersionQuick.h"

/* Note: this file is deliberately both valid C and valid C++. */

#define VTK_BUILD_VERSION 2
#define VTK_VERSION "9.4.1"

#define VTK_SOURCE_VERSION "vtk version " VTK_VERSION

#define VTK_VERSION_NUMBER                                                                         \
  VTK_VERSION_CHECK(VTK_MAJOR_VERSION, VTK_MINOR_VERSION, VTK_BUILD_VERSION)

#endif
</code></pre>
<p>Since <code>vtkvmtkSimplifyVoronoiDiagram.cxx</code> is looking for <code>VTK_BUILD_VERSION &gt;= 20221108</code> in the revision being built, SlicerVMTK build is bound to fail.</p>
<p>This seems to have been addressed in <a href="https://github.com/vmtk/vmtk/blame/6c189dd6ee644a466498bd382b0c19229f20daa5/vtkVmtk/ComputationalGeometry/vtkvmtkSimplifyVoronoiDiagram.cxx#L199" rel="noopener nofollow ugc">6c189dd</a>. May be SlicerVMTK should pull a later revision.</p>

---

## Post #7 by @chir.set (2025-04-18 14:37 UTC)

<p>I built VMTK at <a href="https://github.com/vmtk/vmtk/commit/6c189dd6ee644a466498bd382b0c19229f20daa5" rel="noopener nofollow ugc">6c189dd6</a> with the following errors:</p>
<pre><code class="lang-auto">CMake Error at /home/arc/src/SlicerExtension-VMTK-SuperBuild9/VMTK-build/CMake/vtkWrapPython.cmake:209 (find_package):
  By not providing "FindPythonLibs.cmake" in CMAKE_MODULE_PATH this project
  has asked CMake to find a package configuration file provided by
  "PythonLibs", but CMake did not find one.
</code></pre>
<p>If the changes in CMakeLists introduced by that commit are reverted, VMTK builds fine. Then SlicerVMTK can be built in turn.</p>
<p>This commit (<a href="https://github.com/vmtk/vmtk/commit/6c189dd6ee644a466498bd382b0c19229f20daa5" rel="noopener nofollow ugc">6c189dd6</a>) probably needs the python changes it is expecting and they do not seem to be compatible with Slicer python.</p>
<p>It looks like there <em>might</em> be a need for a SlicerPreview specific branch in the VMTK repository. It won’t be an easy task to maintain SlicerVMTK otherwise.</p>
<p>Or may be there’s some simpler solution.</p>

---
