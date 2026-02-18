# SlicerApp-real.exe becomes non responsive when running my module

**Topic ID**: 30059
**Date**: 2023-06-15
**URL**: https://discourse.slicer.org/t/slicerapp-real-exe-becomes-non-responsive-when-running-my-module/30059

---

## Post #1 by @drdH (2023-06-15 18:30 UTC)

<p>Team,</p>
<p>I am running custom slicer extension in debug mode.  When the debug is started and my extension loaded the following happen:</p>
<ol>
<li>I am able to run the Slicer UI for some time then it stops responding</li>
<li>The command prompt which shows my cout messages are all running despite the ui being un responsive.</li>
</ol>
<p>Tools and OS used : Visual Studio 2022, Windows 10 OS, Slicer version 5.3.0</p>
<p>here are my questions:</p>
<ol>
<li>Kindly wanted to know if there is a way to debug this or get a dump of message when the application goes non responsive?</li>
<li>Is there a windows tool or Slicer tool which gives such information?</li>
</ol>
<p>Thanks</p>

---

## Post #2 by @lassoan (2023-06-16 14:01 UTC)

<p>Make sure you build the extension and Slicer with the same build options, on the same computer (e.g., you cannot run your extension with a Slicer release that you downloaded). If you experience hang then <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html#debug-slicer">you can debug it by starting Slicer from Visual Studio</a>. If you want to see what your application is doing anytime (for example when it is not responding) then you can use <code>Break all</code> action in the <code>Debug</code> menu in Visual Studio.</p>

---
