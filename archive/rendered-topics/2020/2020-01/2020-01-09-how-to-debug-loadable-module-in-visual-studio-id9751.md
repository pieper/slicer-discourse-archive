---
topic_id: 9751
title: "How To Debug Loadable Module In Visual Studio"
date: 2020-01-09
url: https://discourse.slicer.org/t/9751
---

# How to debug loadable module in visual studio?

**Topic ID**: 9751
**Date**: 2020-01-09
**URL**: https://discourse.slicer.org/t/how-to-debug-loadable-module-in-visual-studio/9751

---

## Post #1 by @leemoncn (2020-01-09 07:38 UTC)

<p>I have compiled slicer through the source code. Then i created a module (C++) and compiled it using cmake to generate module.sln. I want to debug this module using visual studio. What should I do?</p>
<p>Should I add this module project to slicer’s source project? I found some documentation on python debugging, but no tutorials on C++ modules I do?</p>

---

## Post #2 by @cpinter (2020-01-09 10:14 UTC)

<p>There is documentation about this (however it seems to be a bit outdated):<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Debug_Instructions#Using_Visual_Studio" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Debug_Instructions#Using_Visual_Studio</a></p>
<p>Basically you need to start Visual Studio using the launcher:<br>
<code>.\S4D\Slicer-build\Slicer.exe --VisualStudio</code></p>
<p>If you want to debug your own extension then you’ll need to add AdditionalLauncherSettings. The way I open VS for debugging SlicerRT:<br>
<code>.\S4D\Slicer-build\Slicer.exe --VisualStudio --launcher-no-splash --launcher-additional-settings ./SlicerRT_D/inner-build/AdditionalLauncherSettings.ini c:\d\_Extensions\SlicerRT_D\inner-build\SlicerRT.sln</code><br>
It also opens the solution.</p>
<p>Then you need to set basically any project as startup, then set the command to<br>
<code>[superbuild_path]\Slicer-build\bin\Debug\SlicerApp-real.exe</code><br>
then just start debugging.</p>

---

## Post #3 by @lassoan (2020-01-09 17:05 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> I’ve updated the instructions based on your comments.</p>

---

## Post #4 by @leemoncn (2020-01-10 08:14 UTC)

<p>Thanks <a class="mention" href="/u/cpinter">@cpinter</a>. I followed you  tutorials, it works.</p>

---

## Post #5 by @PatrickR (2025-01-15 07:23 UTC)

<p>This may be related to my visual studio version (I am using 2022), but when I follow these instructions, my module is not available in slicer.</p>
<p>To fix this, I needed to copy the  <code>--additional-module-paths</code> from <code>inner-build\SlicerWithMyExtensionLauncherSettings.ini</code> and add them as command arguments to my startup project.</p>

---

## Post #6 by @cpinter (2025-01-15 11:36 UTC)

<p>Which extension are you trying to debug? Is it a superbuild extension? It would help if we could talk about it as a concrete case.</p>

---

## Post #7 by @PatrickR (2025-01-16 10:22 UTC)

<p>It is an internal development making some proprietary functionality available in Slicer. Unfortunately, I am not at liberty to share this.</p>
<p>I mainly posted this here, to document my finding, so that the next person having that same problem could benefit from it.</p>

---
