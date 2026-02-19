---
topic_id: 42933
title: "Windows Not Responding Error Remains After Reinstallation"
date: 2025-05-15
url: https://discourse.slicer.org/t/42933
---

# Windows "not responding" error remains after reinstallation

**Topic ID**: 42933
**Date**: 2025-05-15
**URL**: https://discourse.slicer.org/t/windows-not-responding-error-remains-after-reinstallation/42933

---

## Post #1 by @sulli419 (2025-05-15 02:25 UTC)

<p>Is there a way to more thoroughly uninstall Slicer?  After uninstalling via Windows add/remove programs and reinstalling, it seems to remember my previous settings and I’m not sure if it is actually removing all the various extensions from the python environment.  Even worse, it seems to remember the problems I was having.  It still gets hung up (windows “not responding”) after nearly every command or drawing, usually recovers, but sometimes crashes.</p>
<p>I am using the latest version of slicer.  It worked fine until I started experimenting with installing various extensions.  I had installed: slicermorph, a few AI tools that I couldn’t get working (SAM, NVIDIA, complete organ segmentation, nnUnet).  I know some of these extensions (SAM for example) had installed multiple GB of data.  After uninstalling slicer I didn’t see any hard drive space clear out.</p>
<p>Maybe there is a way to purge the python environment and start a truly fresh install?</p>
<p>Thanks much,<br>
Steve</p>

---

## Post #2 by @lassoan (2025-05-15 03:20 UTC)

<p>This documentation page should help: <a href="https://slicer.readthedocs.io/en/latest/user_guide/get_help.html#slicer-application-does-not-start">Get help / Troubleshooting / Application does not start</a></p>

---

## Post #3 by @muratmaga (2025-05-15 04:21 UTC)

<p>If the troubleshooting steps doesn’t help and you want to reset everything</p>
<ol>
<li>go to <code>C:/Users/YOURUSERNAME/AppData/Local/Slicer.org</code> and delete everything in there.</li>
<li>go to <code>C:/Users/YOURUSERNAME/AppData/Roaming/Slicer.org/</code> and delete the slicer.ini.</li>
</ol>
<p>Then you can try reinstalling. All libraries and python packages are installed in the Slicer’s build tree. Another option is to try giving a completely different path to install (e.g., C:\Slicer)</p>

---

## Post #4 by @sulli419 (2025-05-16 00:23 UTC)

<p>I uninstalled my existing slicer, then backed up these complete directories on a different drive and deleted them, and reinstalled.  Slicer is definitely behaving better, although I think it might still be getting hung up more than it used to.  I still get “not responding” after clicking the button to show my segmentations in 3d but it eventually works.  I no longer get “not responding” after every time I draw pixels, so this is an improvement.</p>
<p>In the instructions Iassoan shared, it sounds like there might be libraries that went into the wrong directories (different from the ones I deleted on your advice).  Any good way to hunt for these?</p>
<p>Thanks, Steve</p>

---

## Post #5 by @muratmaga (2025-05-16 15:18 UTC)

<aside class="quote no-group" data-username="sulli419" data-post="4" data-topic="42933">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sulli419/48/78859_2.png" class="avatar"> sulli419:</div>
<blockquote>
<p>my segmentations in 3d but it eventually works. I no longer get “not responding” after every time I draw pixels, so this is an improvement.</p>
</blockquote>
</aside>
<p>That slowness is normal if your segmentation is too large. When Show 3D is enabled, every time you point a voxel, the displayed model is regenerated. I advise keeping the show 3D disabled during the manual voxel-by-voxel segmentations to avoid that slowdown.</p>

---
