# C++ debugging SlicerCAT takes about 10 minutes to start on Ubuntu

**Topic ID**: 21130
**Date**: 2021-12-18
**URL**: https://discourse.slicer.org/t/c-debugging-slicercat-takes-about-10-minutes-to-start-on-ubuntu/21130

---

## Post #1 by @keri (2021-12-18 18:18 UTC)

<p>Hi,</p>
<p>Is it ok that SicerCAT takes about 10 minutes to start debugging using C++?</p>
<p>I use QtCreator 4.15.1 on Ubuntu 20.04, gcc 9.3, debugger <code>usr/bin/gdb</code><br>
PC has 4 physical and 4 logical cores<br>
The processor: Intel(R) Core™ i7-7700K CPU @ 4.20GHz<br>
RAM: 20 Gb</p>
<p>The executable is <code>SlicerCAT/d/Slicer-build/bin/SlicerCATApp-real</code></p>
<p>I’ve tried debugging using both startup application and using attach to process.</p>
<p>I’m asking because previously I used to work on Windows 10 and Visual Studio 2019 with laptop about two times less powerful and it used to take maybe 4 minutes to start. That is why I have some doubts and this somehow restricts me in C++ debugging, I have to use std::cout or vtkError/qCritical staff to detect bugs.</p>

---

## Post #2 by @lassoan (2021-12-19 14:52 UTC)

<p>Starting under a debugger should be about as fast as without a debugger, except if you load debug symbols. In Visual Studio by default all available debug symbols are loaded, which takes maybe a minute and if you use VS2022 then I noticed that first time stopping at a breakpoint may take again a minute or so. However, you can reduce this symbol loading time by specifying what symbols to load.</p>

---
