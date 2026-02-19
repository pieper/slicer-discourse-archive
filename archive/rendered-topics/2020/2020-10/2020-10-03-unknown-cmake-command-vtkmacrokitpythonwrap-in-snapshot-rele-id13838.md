---
topic_id: 13838
title: "Unknown Cmake Command Vtkmacrokitpythonwrap In Snapshot Rele"
date: 2020-10-03
url: https://discourse.slicer.org/t/13838
---

# Unknown CMake command "vtkMacroKitPythonWrap" in snapshot release for vtkTeem

**Topic ID**: 13838
**Date**: 2020-10-03
**URL**: https://discourse.slicer.org/t/unknown-cmake-command-vtkmacrokitpythonwrap-in-snapshot-release-for-vtkteem/13838

---

## Post #1 by @cpinter (2020-10-03 16:19 UTC)

<p>Hi all,</p>
<p>I am upgrading all the projects I have to the new snapshot release, and one of them produced a strange CMake error:</p>
<pre><code class="lang-auto">Configuring library: vtkTeem
CMake Error at Libs/vtkTeem/CMakeLists.txt:149 (include):
  include could not find load file:

    vtkMacroKitPythonWrap

CMake Error at Libs/vtkTeem/CMakeLists.txt:151 (vtkMacroKitPythonWrap):
  Unknown CMake command "vtkMacroKitPythonWrap".
</code></pre>
<p>The reason it is strange is that for vtkAddon and vtkSegmentationCore the same thing does not happen (or maybe the build process does not get that far?). Anyway, before starting digging deep in what changed in CMake, I thought I ask here because I have seen lots of things changing lately around Python wrapping of CMake. What I tried so far is adding vtkTeem in lists where vtkSegmentationCore was present but not vtkTeem, but it did not help.</p>
<p>Do you <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/lassoan">@lassoan</a> have any idea or suggestion what to try? Thanks a lot!</p>

---

## Post #2 by @jcfr (2020-10-03 16:33 UTC)

<blockquote>
<p>I am upgrading all the projects I have to the new snapshot release<br>
Unknown CMake command “vtkMacroKitPythonWrap” in snapshot release for vtkTeem</p>
</blockquote>
<p>To summarize, you are building a custom application based of <a href="https://github.com/Slicer/Slicer/tree/v4.11.20200930" class="inline-onebox">GitHub - Slicer/Slicer at v4.11.20200930</a> and you observe this build error ?</p>
<p>Was the custom app built following this pattern: <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate" class="inline-onebox">GitHub - KitwareMedical/SlicerCustomAppTemplate: Template to be used as a starting point for creating a custom 3D Slicer application</a> ?</p>

---

## Post #3 by @cpinter (2020-10-04 16:45 UTC)

<p>Yes and yes. However, only one custom app has this error and it occurs if I do repetitive clean builds.</p>

---

## Post #4 by @cpinter (2020-10-05 14:55 UTC)

<p>I enabled building vtkAddon and the build succeeded.</p>

---
