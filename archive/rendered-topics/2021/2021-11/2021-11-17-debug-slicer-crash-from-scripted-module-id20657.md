---
topic_id: 20657
title: "Debug Slicer Crash From Scripted Module"
date: 2021-11-17
url: https://discourse.slicer.org/t/20657
---

# Debug Slicer crash from scripted module

**Topic ID**: 20657
**Date**: 2021-11-17
**URL**: https://discourse.slicer.org/t/debug-slicer-crash-from-scripted-module/20657

---

## Post #1 by @atracsys-sbt (2021-11-17 12:23 UTC)

<p>Hi,<br>
At a certain stage in my scripted module, I’m experiencing a crash of Slicer that occurs around 1 out of 10 times. I have no clue what’s causing it, especially since this crash leaves no trace: no popup, nothing in the Slicer log and nothing while Python remote debugging using Pycharm.<br>
I would like to know how I could get more information about this crash. Running my scripted module in Slicer in Debug mode ? Would I be able to install the necessary extensions then ?<br>
Thanks</p>

---

## Post #2 by @pieper (2021-11-17 20:29 UTC)

<p>This can be tricky.  Probably some operation does a non-safe memory operation but doesn’t trigger a crash until later depending on the sequence of operations.</p>
<p>Easiest can be to look for unsafe usages by taking out pieces of functionality to see if you can isolate the cause of the crash.</p>
<p>If that doesn’t work you may need to resort to building Slicer from source and use a debugger.  This can be a big step depending on your experience but it’s the best way to know what’s really going on.  Unfortunately if you need extensions you also need to build them in debug mode.</p>

---

## Post #3 by @atracsys-sbt (2021-11-18 10:06 UTC)

<p>Thanks for the reply Steve !<br>
I already tried to compile Slicer in Debug mode, but I ran into the link issue with Python still being in Release (<a href="https://discourse.slicer.org/t/latest-master-does-not-build-in-debug-mode/191/5">similar issue here</a> but with SimpleITK).</p>
<pre><code class="lang-auto">Error LNK1104 cannot open file 'python36.lib' [D:\...\build\Slicer\CTK-build\PythonQt-build\PythonQt.vcxproj]
</code></pre>
<p>Unfortunately, my module relies on PythonQt so I cannot just disable the dependency.<br>
So, in the meantime, I guess I’m stuck with trying to figure out the bug by progressively dismantling my code, which is still very tedious given the rare occurrence of the crash.</p>

---

## Post #4 by @pieper (2021-11-18 13:08 UTC)

<p>It would be great if the regular windows users could help you with the compile issue.  As a rule we want to make sure that anyone who follows developer documentation should have a painless compile experience.</p>

---

## Post #5 by @lassoan (2021-11-18 13:30 UTC)

<p>Many of us build Slicer in debug mode every day without problems. It is fine that Python is built in release mode and the rest of the application in debug mode. Python is built in release mode by default in Slicer (and probably in all other applications that embed Python), because we rarely need to debug Python itself and debug-mode Python would execute scripts much slower.</p>
<p>Have you created a new build tree for the debug build or you just switched the build mode to Debug in Visual Studio? You must use a new build tree.</p>
<p>If you use a new build tree then check the compilation error messages that appear before the linker error. Those should tell why python36.lib build failed on your computer.</p>
<p>If you don’t use the latest Slicer master or you build a custom application then you can try to build a Slicer master using the standard build instructions to confirm that everything works well in that configuration.</p>

---

## Post #6 by @atracsys-sbt (2021-11-18 16:40 UTC)

<p>I checked out yesterday’s head of the master (<a href="https://github.com/Slicer/Slicer/commit/0e7423fc359ddcba5d30356e87f097fa20822b38" rel="noopener nofollow ugc">0e7423f</a>), left the CMake options untouched and I built into an empty folder.<br>
What’s weird is that it says it has found python36.lib in release (and python39 in debug) at the beginning of the PyhtonQt part:</p>
<pre><code class="lang-auto">43&gt;  -- Found PythonLibs: optimized;D:/dev-ext/build/Slicer/python-install/libs/python36.lib;debug;C:/Python/Python39/libs/python39_d.lib (found version "3.6.7")
43&gt;  -- PythonQt: Required Qt components [Core;Widgets;Multimedia;PrintSupport;Network;MultimediaWidgets;UiTools]
43&gt;  -- Configuring done
43&gt;  -- Generating done
43&gt;  -- Build files have been written to: D:/dev-ext/build/Slicer/CTK-build/PythonQt-build
</code></pre>
<p>And yet it gives the same error afterwards:</p>
<pre><code class="lang-auto">44&gt;  Performing update step for 'PythonQt'
44&gt;  Performing configure step for 'PythonQt'
44&gt;  loading initial cache file D:/dev-ext/build/Slicer/CTK-build/PythonQt-cmake/tmp/PythonQt-cache-Debug.cmake
44&gt;  -- Selecting Windows SDK version 10.0.18362.0 to target Windows 10.0.18363.
44&gt;  -- PythonQt: Required Qt components [Core;Widgets;Multimedia;PrintSupport;Network;MultimediaWidgets;UiTools]
44&gt;  -- Configuring done
44&gt;  -- Generating done
44&gt;  -- Build files have been written to: D:/dev-ext/build/Slicer/CTK-build/PythonQt-build
44&gt;  No build step for 'PythonQt'
44&gt;  Performing install step for 'PythonQt'
44&gt;  Microsoft (R) Build Engine version 16.11.0+0538acc04 for .NET Framework
44&gt;  Copyright (C) Microsoft Corporation. All rights reserved.
44&gt;
44&gt;Qt5UiToolsd.lib(moc_quiloader.obj) : warning LNK4099: PDB 'Qt5UiToolsd.pdb' was not found with 'Qt5UiToolsd.lib(moc_quiloader.obj)' or at 'D:\dev-ext\build\Slicer\CTK-build\PythonQt-build\Debug\Qt5UiToolsd.pdb'; linking object as if no debug info [D:\dev-ext\build\Slicer\CTK-build\PythonQt-build\PythonQt.vcxproj] [D:\dev-ext\build\Slicer\CTK-build\PythonQt.vcxproj]
44&gt;Qt5UiToolsd.lib(quiloader.obj) : warning LNK4099: PDB 'Qt5UiToolsd.pdb' was not found with 'Qt5UiToolsd.lib(quiloader.obj)' or at 'D:\dev-ext\build\Slicer\CTK-build\PythonQt-build\Debug\Qt5UiToolsd.pdb'; linking object as if no debug info [D:\dev-ext\build\Slicer\CTK-build\PythonQt-build\PythonQt.vcxproj] [D:\dev-ext\build\Slicer\CTK-build\PythonQt.vcxproj]
...
44&gt;Qt5UiToolsd.lib(moc_properties_p.obj) : warning LNK4099: PDB 'Qt5UiToolsd.pdb' was not found with 'Qt5UiToolsd.lib(moc_properties_p.obj)' or at 'D:\dev-ext\build\Slicer\CTK-build\PythonQt-build\Debug\Qt5UiToolsd.pdb'; linking object as if no debug info [D:\dev-ext\build\Slicer\CTK-build\PythonQt-build\PythonQt.vcxproj] [D:\dev-ext\build\Slicer\CTK-build\PythonQt.vcxproj]
44&gt;LINK : fatal error LNK1104: cannot open file 'python36.lib' [D:\dev-ext\build\Slicer\CTK-build\PythonQt-build\PythonQt.vcxproj] [D:\dev-ext\build\Slicer\CTK-build\PythonQt.vcxproj]
</code></pre>

---

## Post #7 by @lassoan (2021-11-18 16:45 UTC)

<p>“D:\dev-ext\build\Slicer” - this path is too long. Please try from scratch with “D:\S4” source and “D:\S4D” binary directory.</p>

---

## Post #8 by @atracsys-sbt (2021-11-19 12:17 UTC)

<p>I did exactly that and still faced the same error <img src="https://emoji.discourse-cdn.com/twitter/slightly_frowning_face.png?v=10" title=":slightly_frowning_face:" class="emoji" alt=":slightly_frowning_face:"></p>

---

## Post #9 by @lassoan (2021-11-19 17:28 UTC)

<p>We had a look at the build and it turned out that the problem was that that on that computer a debug-mode Python was listed in the PATH environment variable, which caused build system to find that unrelated Python distribution (without the required Python development files) instead of Slicer’s Python.</p>

---

## Post #10 by @atracsys-sbt (2021-11-19 21:12 UTC)

<p>After temporarily renaming C:\Python to something else, it worked !</p>

---
