---
topic_id: 33683
title: "Starting 3Dslicer Stops With Loading Module Viewcontrollers"
date: 2024-01-08
url: https://discourse.slicer.org/t/33683
---

# starting 3Dslicer stops with loading module "ViewControllers"

**Topic ID**: 33683
**Date**: 2024-01-08
**URL**: https://discourse.slicer.org/t/starting-3dslicer-stops-with-loading-module-viewcontrollers/33683

---

## Post #1 by @FinnR (2024-01-08 20:42 UTC)

<p>When I download and install 3D slicer 5.6.1. I can run it just once - If I exit and restarts the program the loading stops with loading module “WiewControllers”.</p>
<p>It looks like a trivial problem, but I have been unable tio solve it - any suggestions?<br>
FinnR</p>

---

## Post #2 by @pieper (2024-01-09 00:42 UTC)

<p>Hmm, this doesn’t happen for me with 5.6.1.</p>
<p>Try the suggestions here (especially disabling settings).</p>
<p><a href="https://slicer.readthedocs.io/en/v4.11/user_guide/get_help.html#troubleshooting" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/v4.11/user_guide/get_help.html#troubleshooting</a></p>
<p>You could also try looking in the log files.  If you don’t know where to look for them let us know what OS you are on and someone can point you to the right place to look.</p>

---

## Post #3 by @FinnR (2024-01-09 11:17 UTC)

<p>Thank you - deleting slicer.ini solves the problem temporarily. But a new one is created every tim I run Slicer, so it seems like I will have to find and delete slicer.ini every time I want to start the program. I have renamed the NA-MIC folder  in both C:\Users\Bruger\AppData\Local and C:\Users\Bruger\AppData\Roaming but it doesn’t change anything.<br>
I am running Slicer in Windows 10.</p>

---

## Post #4 by @pieper (2024-01-09 14:07 UTC)

<p>Perhaps there’s something else going on, like a temp directory path.  Inspecting the settings file and/or the log file may give some more clues.</p>

---

## Post #5 by @lassoan (2024-01-10 22:22 UTC)

<aside class="quote no-group" data-username="FinnR" data-post="3" data-topic="33683">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/fbc32d/48.png" class="avatar"> FinnR:</div>
<blockquote>
<p>I will have to find and delete slicer.ini every time I want to start the program</p>
</blockquote>
</aside>
<p>Slicer.ini stores application settings that you want to preserve, so it should not be deleted before each application start.</p>
<p>If the issue ever comes up again then it would be great if you could save the Slicer.ini file and share it with us (upload to dropbox, onedrive, … and post the link here).</p>
<p>Also have a look at the logs as <a class="mention" href="/u/pieper">@pieper</a> suggested - they are in the temporary files folder, within <code>Slicer</code> subfolder. You can jump there by putting this into the File explorer path line edit: <code>%tmp%\Slicer</code>).</p>

---
