---
topic_id: 1424
title: "Slicer Build Failed In Windows 10 Numpy Patch Problem"
date: 2017-11-09
url: https://discourse.slicer.org/t/1424
---

# Slicer build failed in windows 10, numpy patch problem

**Topic ID**: 1424
**Date**: 2017-11-09
**URL**: https://discourse.slicer.org/t/slicer-build-failed-in-windows-10-numpy-patch-problem/1424

---

## Post #1 by @brhoom (2017-11-09 20:55 UTC)

<p>Dear all,<br>
I am trying to build a release type build of Slicer -r 26489 source code in windows 10 using visual studio 2013 update 5.<br>
The build fail because of Numpy. I got this error when I try to build numpy:</p>
<pre><code>16&gt;  -- Applying 'numpy-01-system_info-fix-clang.patch' - failed
16&gt;  CMake Error at C:/sw/Slicer4.8/Slicer-r26489/CMake/SlicerPatch.cmake:54 (message):
16&gt;    
16&gt;  
16&gt;    
16&gt;  
16&gt;    This application has requested the Runtime to terminate it in an unusual
16&gt;    way.
16&gt;  
16&gt;    Please contact the application's support team for more information.
16&gt;  
16&gt;    Assertation failed!
16&gt;  
16&gt;    
16&gt;  
16&gt;    Program: C:\Strawberry\c\bin\patch.exe
16&gt;  
16&gt;    File: .\src\patch\2.5.9\patch-2.5.9-src\patch.c, Line 354
16&gt;  
16&gt;    
16&gt;  
16&gt;    Expression: hunk 
16&gt;  
16&gt;  
16&gt;C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(170,5): error MSB6006: "cmd.exe" exited with code 1.
========== Build: 15 succeeded, 1 failed, 0 up-to-date, 0 skipped ==========
</code></pre>
<p>note: The debug build was successful but I had to disable SimpleITK.<br>
Thanks for your input.</p>

---
