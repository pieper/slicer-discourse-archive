---
topic_id: 7172
title: "Cant See Source Code Cpp Files In Solution Slicer Sln Source"
date: 2019-06-14
url: https://discourse.slicer.org/t/7172
---

# Can't see source code(.cpp files) in solution Slicer.sln. Source code hierarchy is missing in Solution manager.

**Topic ID**: 7172
**Date**: 2019-06-14
**URL**: https://discourse.slicer.org/t/cant-see-source-code-cpp-files-in-solution-slicer-sln-source-code-hierarchy-is-missing-in-solution-manager/7172

---

## Post #1 by @Programming_Freak (2019-06-14 17:48 UTC)

<p>I configured slicer.sln using cmake on windows.<br>
I opened the project in VS 2015, but I can’t see any source code hierarchy or any src folder.<br>
I compiled th solution and I got Slicer.exe generated. But still cpp files in solution manager are missing.<br>
Is there any other way to get those cpp files in Visual studio-&gt; solution manager?</p>

---

## Post #2 by @lassoan (2019-06-14 17:50 UTC)

<p>The top-level solution builds all dependencies of Slicer core and Slicer core itself. You can see Slicer source files if you open <code>&lt;Slicer-top-level-build-folder&gt;\Slicer-build\Slicer.sln</code>.</p>

---
