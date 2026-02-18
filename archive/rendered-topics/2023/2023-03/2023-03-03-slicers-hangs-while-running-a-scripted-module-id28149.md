# Slicers hangs while running a scripted module

**Topic ID**: 28149
**Date**: 2023-03-03
**URL**: https://discourse.slicer.org/t/slicers-hangs-while-running-a-scripted-module/28149

---

## Post #1 by @Saima (2023-03-03 02:40 UTC)

<p>Hi,<br>
could you please suggest the best way to avoid any slicer hang.<br>
The python scripted module I wrote runs succesfully but in between the slicer hangs asking for to wait or force quit. how to avoid?</p>
<p>The module purpose is to run 300 images and get the segmentation automatically using bratstoolkit and managing the directories it create for 300 images. On top of that I am using 3D Slicer to apply the transform to the segmented region of interest to get it aligned with the original MRI for each of these images and saving the transformed segmentation.</p>
<p>The slicer windows pop up telling to force quit or wait? how to get rid of this issue? I did wait every time and then it runs fine but how to avoid this issue?</p>
<p>Also i am using the nightly build version of slicer not the stable release.</p>
<p>Thank you</p>
<p>regards,<br>
Saima</p>

---

## Post #2 by @lassoan (2023-03-03 05:12 UTC)

<p>If Slicer is busy running your long script then it is normal that it is not responsive. Quit if you want to abort your processing, but otherwise just wait for your operations to complete. If you want to be able to have some interaction (visualize something, process button click events, etc.) then you can call <code>slicer.app.processEvents()</code> time to time.</p>

---

## Post #3 by @RafaelPalomar (2023-03-07 06:07 UTC)

<p>In Ubuntu and the like this is due to the operating system checking if the application is responsive. You can change the OS parameters driving this check to make it less sensitive (<a href="https://ubuntuforums.org/showthread.php?t=2476794" class="inline-onebox" rel="noopener nofollow ugc">Ubuntu 22.04 too eager</a>).</p>

---
