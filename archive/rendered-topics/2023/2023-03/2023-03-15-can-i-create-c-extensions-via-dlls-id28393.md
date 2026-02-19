---
topic_id: 28393
title: "Can I Create C Extensions Via Dlls"
date: 2023-03-15
url: https://discourse.slicer.org/t/28393
---

# Can I create c++ extensions via DLLs?

**Topic ID**: 28393
**Date**: 2023-03-15
**URL**: https://discourse.slicer.org/t/can-i-create-c-extensions-via-dlls/28393

---

## Post #1 by @dsa934 (2023-03-15 07:55 UTC)

<p>Operating system: window 10<br>
Slicer version: 5.2.1</p>
<p>Hi, slicer users</p>
<p>I’m trying to create a C++ dll(dynamic-link library) to use a function implemented in C++ in Python.</p>
<p>Can this DLL be applied to 3d slicer?</p>
<p>So, wouldn’t it be possible to extend C++ modules the same way Python extends?</p>
<p>If this is not possible you will have to learn some more advanced ways of handling Cmake.</p>

---

## Post #2 by @RafaelPalomar (2023-03-15 14:04 UTC)

<p>C++ components of 3D Slicer Qt Loadable Modules (<a href="https://slicer.readthedocs.io/en/latest/developer_guide/module_overview.html#loadable-modules" class="inline-onebox" rel="noopener nofollow ugc">Module Overview — 3D Slicer documentation</a>) are wrapped in python and exposed automatically (mostly). These wrapped python components will be available in Slicer and can be used by other modules.</p>
<p>I would recommend that you try to integrate this C++ code as part of a Loadable Module. It is also possible to have a sort of hybrid module, where Scripted module (<a href="https://slicer.readthedocs.io/en/latest/developer_guide/module_overview.html#scripted-modules" class="inline-onebox" rel="noopener nofollow ugc">Module Overview — 3D Slicer documentation</a>) can include some C++ components (an example of this approach is one of the modules of Slicer-Liver: <a href="https://github.com/ALive-research/Slicer-Liver/tree/develop/LiverSegments" class="inline-onebox" rel="noopener nofollow ugc">Slicer-Liver/LiverSegments at develop · ALive-research/Slicer-Liver · GitHub</a>)</p>

---

## Post #3 by @lassoan (2023-03-15 15:36 UTC)

<p>You can also integrate the C++ code into Slicer via CLI module. It is simpler to create and maintain CLI modules, as they consists of only a single file and don’t contain any Slicer specific code. But perhaps more importantly, the code is executed in a separate process, so any errors in the code cannot make the application crash. Execution can also run in the background, keeping the application responsive during lengthy computations. These are all very important advantages. The only drawback is that you need to pass input and output data between Slicer and this process, which may be too slow for interactive use (when you need updates at dozens of times per second).</p>

---

## Post #4 by @pieper (2023-03-15 16:09 UTC)

<p>If you need faster communication between Slicer and custom C++ code than you can get with a CLI module you can also consider using the WebServer or OpenIGTLink networking options.  CLI modules are started as a new process each time they run, while the networking options all back-and-forth communication for a running process.</p>

---

## Post #5 by @jamesobutler (2023-03-15 16:33 UTC)

<p>You could also consider using <a href="https://cython.readthedocs.io/en/stable/src/userguide/wrapping_CPlusPlus.html" rel="noopener nofollow ugc">C++ in Python</a> techniques with cython. My group has a Slicer Scripted CLI (python) that contains a custom cythonized python module to speed up a specific calculation in a processing algorithm.</p>

---

## Post #6 by @pieper (2023-03-15 16:50 UTC)

<p>Yes, there’s cython and also <a href="https://gist.github.com/pieper/f9da3e0a73c70981b48d0747132526d5">cppyy</a> that I find interesting, but if the goal is to provide a maintainable Slicer extension or even custom app then putting the C++ code in either a VTK or ITK class will allow you to use all the existing cross-platform deployment infrastructure without a second thought.</p>

---

## Post #7 by @dsa934 (2023-03-17 02:39 UTC)

<p>Thanks everyone for your replies. I’ll try it as soon as the preceding work is finished. Thank you!</p>

---
