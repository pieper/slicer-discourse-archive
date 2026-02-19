---
topic_id: 12460
title: "Ignore Modules At Startup"
date: 2020-07-09
url: https://discourse.slicer.org/t/12460
---

# Ignore modules at startup

**Topic ID**: 12460
**Date**: 2020-07-09
**URL**: https://discourse.slicer.org/t/ignore-modules-at-startup/12460

---

## Post #1 by @ada (2020-07-09 13:45 UTC)

<p>Hi all,</p>
<p>I want to disable some modules when starting 3DSlicer.<br>
I know I can select all specific modules in Edit&gt;Application Settings but I would like to know if there is any easier way to disable a list of modules.<br>
It is working starting 3DSlicer with command line such as “Slicer.exe -modules-to-ignore Welcome,Data,Cameras,AtlasTests,Colors,Charting,WebEngine…” but all these settings are not preserved if I restart the software without command line.</p>
<p>How can I do ?</p>
<p>Best,<br>
Ada</p>

---

## Post #2 by @lassoan (2020-07-09 13:54 UTC)

<p>Edit/Application Settings is just a visual editor for your Slicer-NNNNN.ini file. You can edit the file directly with a text editor.</p>
<p>Alternatively, you can simply delete those module files (.dll or .py file) that you don’t need. Note that there are dependencies between modules, so if you disable a module then it may disable other ones. You can see which module requires which listed in the new module finder dialog - when you press Ctrl-F in the latest Slicer preview releases.</p>

---
