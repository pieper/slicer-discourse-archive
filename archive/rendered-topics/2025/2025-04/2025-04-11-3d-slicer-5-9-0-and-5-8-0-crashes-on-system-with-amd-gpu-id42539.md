---
topic_id: 42539
title: "3D Slicer 5 9 0 And 5 8 0 Crashes On System With Amd Gpu"
date: 2025-04-11
url: https://discourse.slicer.org/t/42539
---

# 3d slicer 5.9.0 and 5.8.0 crashes on system with amd GPU.

**Topic ID**: 42539
**Date**: 2025-04-11
**URL**: https://discourse.slicer.org/t/3d-slicer-5-9-0-and-5-8-0-crashes-on-system-with-amd-gpu/42539

---

## Post #1 by @phranchi (2025-04-11 17:20 UTC)

<p>Problem report for <code>Slicer 5.9.0-2025-04-08 win-amd64</code>: The AMD driver and 3d slicer crash after 2 mins of operating.</p>
<p>I am currently working on the segmentation of CSF space in the brain. Everything works fine when I work on a Mac or Windows PC with an Nvidia GPU or Intel’s integrated GPU.</p>
<p>My GPU Model number is RX9070 xt, and the driver version is 25.3.1.</p>
<p>Here is the log:</p>
<pre><code class="lang-auto">[DEBUG][Qt] 09.04.2025 21:20:42 [] (unknown:0) - Session start time .......: 20250409_212042
[DEBUG][Qt] 09.04.2025 21:20:42 [] (unknown:0) - Slicer version ...........: 5.9.0-2025-04-08 (revision 33600 / cd62f82) win-amd64 - installed release
[DEBUG][Qt] 09.04.2025 21:20:42 [] (unknown:0) - Operating system .........: Windows /  Professional / (Build 26100, Code Page 65001) - 64-bit
[DEBUG][Qt] 09.04.2025 21:20:42 [] (unknown:0) - Memory ...................: 32607 MB physical, 73567 MB virtual
[DEBUG][Qt] 09.04.2025 21:20:42 [] (unknown:0) - CPU ......................: GenuineIntel , 16 cores, 16 logical processors
[DEBUG][Qt] 09.04.2025 21:20:42 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 09.04.2025 21:20:42 [] (unknown:0) - Qt configuration .........: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)
[DEBUG][Qt] 09.04.2025 21:20:42 [] (unknown:0) - DCMTK configuration ......: version 3.6.8, no SSL
[DEBUG][Qt] 09.04.2025 21:20:42 [] (unknown:0) - Internationalization .....: disabled, language=
[DEBUG][Qt] 09.04.2025 21:20:42 [] (unknown:0) - Developer mode ...........: disabled
[DEBUG][Qt] 09.04.2025 21:20:42 [] (unknown:0) - Application path .........: C:/Users/*/AppData/Local/slicer.org/Slicer 5.9.0-2025-04-08/bin
[DEBUG][Qt] 09.04.2025 21:20:42 [] (unknown:0) - Additional module paths ..: (none)
[DEBUG][Python] 09.04.2025 21:20:43 [Python] (C:\Users\*\AppData\Local\slicer.org\Slicer 5.9.0-2025-04-08\lib\Slicer-5.9\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 09.04.2025 21:20:43 [Python] (C:\Users\*\AppData\Local\slicer.org\Slicer 5.9.0-2025-04-08\lib\Slicer-5.9\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 09.04.2025 21:20:44 [] (unknown:0) - Switch to module:  "Welcome"
[DEBUG][Qt] 09.04.2025 21:20:44 [] (unknown:0) - Ignored arguments: ("C:\\Users\\*\3D Slicer Modeling\\CSP006\\2025-04-04-Scene.mrml")
[DEBUG][Qt] 09.04.2025 21:20:44 [] (unknown:0) - Local filepath received via command-line:  "C:\\Users\\*\3D Slicer Modeling\\CSP006\\2025-04-04-Scene.mrml"
[ERROR][VTK] 09.04.2025 21:20:44 [vtkMRMLSliceNode (0000020BF9AFDD80)] (vtkMRMLSliceNode.cxx:359) - GetSliceOrientationPreset: invalid orientation preset name: Reformat
[ERROR][VTK] 09.04.2025 21:20:44 [vtkMRMLSliceNode (0000020BF9AFF440)] (vtkMRMLSliceNode.cxx:359) - GetSliceOrientationPreset: invalid orientation preset name: Reformat
[ERROR][VTK] 09.04.2025 21:20:44 [vtkMRMLSliceNode (0000020BF9AFEDC0)] (vtkMRMLSliceNode.cxx:359) - GetSliceOrientationPreset: invalid orientation preset name: Reformat
[DEBUG][Qt] 09.04.2025 21:20:44 [] (unknown:0) - "MRML Scene" Reader has successfully read the file "C:/Users/*/3D Slicer Modeling/CSP006/2025-04-04-Scene.mrml" "[0.32s]"
</code></pre>
<p>The file path is manually omitted.</p>

---

## Post #2 by @lassoan (2025-04-11 17:27 UTC)

<p>What you describes sounds like a graphics driver bug. Try the latest driver version and if it is still crashing then try an older version (e.g., from a year ago). Also check your Windows system logs, they may give a hint of what went wrong and how to fix it (e.g., if it is a TDR timeout then you can increase TDR delay in the registry to avoid the operating system to restart the driver that makes all GPU-using applications crash).</p>

---

## Post #3 by @jamesobutler (2025-04-11 18:17 UTC)

<aside class="quote no-group quote-modified" data-username="phranchi" data-post="1" data-topic="42539">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/phranchi/48/80667_2.png" class="avatar"> phranchi:</div>
<blockquote>
<p><em>[DEBUG][Qt] 09.04.2025 21:20:44 [] (unknown:0) - “MRML Scene” Reader has successfully read the file "C:/Users/</em>/3D Slicer Modeling/CSP006/2025-04-04-Scene.mrml” “[0.32s]”</p>
</blockquote>
</aside>
<p>Does your MRML file have some specific volume rendering state properties saved for the specific scene? If you attempt to set up the same type scene from a fresh opened Slicer (don’t load the mrml file), then when using your system with the AMD GPU, at what point does Slicer crash?</p>

---
