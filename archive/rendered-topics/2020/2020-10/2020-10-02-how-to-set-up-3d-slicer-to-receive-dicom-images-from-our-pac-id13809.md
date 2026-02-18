# How to set up 3D Slicer to receive DICOM images from our PACS?

**Topic ID**: 13809
**Date**: 2020-10-02
**URL**: https://discourse.slicer.org/t/how-to-set-up-3d-slicer-to-receive-dicom-images-from-our-pacs/13809

---

## Post #1 by @mariobjc (2020-10-02 01:07 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10.2<br>
Expected behavior: PACS images flow into Slicer application<br>
Actual behavior: N/A</p>
<p>My name is Mario and I’m a Senior Analyst for our hospital’s PACS system. I haven’t used or supported 3D Slicer before but I have a user who needs to use the application.</p>
<p>I was wondering if you could point me to some documentation or provide a walk through on how to set up the Slicer application to receive images from our PACS? If it helps, we’re currently using Syngo Plaza and I’ve already created a DICOM node for the workstation that has Slicer installed on it.</p>
<p>Thank you.</p>
<p>Regards,</p>
<p>Mario</p>

---

## Post #2 by @pieper (2020-10-02 13:55 UTC)

<p>There have been several posts about this, so the answers should be in there.  Warning in advance that Slicer query implementation is not the most efficient, but it should work.</p>
<p><a href="https://discourse.slicer.org/search?q=aetitle%20order%3Alatest">https://discourse.slicer.org/search?q=aetitle%20order%3Alatest</a></p>
<p>This post from yesterday has the key info about AETITLE and port: <a href="https://discourse.slicer.org/t/configuration-of-the-3d-slicer-dicom-listener-to-hospital-ct/13754/2" class="inline-onebox">Configuration of the 3D Slicer DICOM Listener to Hospital CT</a></p>

---

## Post #3 by @mariobjc (2020-10-02 16:08 UTC)

<p>Hello Steve,</p>
<p>Thank you so much for this information! I really appreciate it.</p>
<p>-Mario</p>

---
