---
topic_id: 11380
title: "Plus Luncher Keeps Saying Launching"
date: 2020-05-01
url: https://discourse.slicer.org/t/11380
---

# Plus Luncher keeps saying "Launching"?

**Topic ID**: 11380
**Date**: 2020-05-01
**URL**: https://discourse.slicer.org/t/plus-luncher-keeps-saying-launching/11380

---

## Post #1 by @kristjanq (2020-05-01 16:45 UTC)

<p>Hello,</p>
<p>I am trying to transmit some ultrasound images(NRRD format) thought Open IGTlink form PLUS to Slicer. The final goal is to reconstruct an accuracy evaluation phantom for evaluation of tracked Ultrasound.</p>
<p>Here is what I did:<br>
1- set the Device " <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceSavedDataSource.html" rel="noopener nofollow ugc">Replay recorded data from file</a>" in the config file with a link to the <code>directory</code><br>
2- set the device “VolumeReconstructorDevice” in the config file<br>
3- set up the connection through Open IGTlink<br>
3.1- Add the connector (+)<br>
3.1- check ACTIVE<br>
3.2- I/O configuration: Image data as volume and Transform data is available but no output<br>
4- View controllers: chose the right connection, Axial, and click the eye<br>
5- Volume reslice driver: Transverse</p>
<p>Yet, the Plus Server indicates “Lunching …”. Is that right? And Should there be an output (3.2)</p>
<p>I should note that I could not see any image or Volume yet!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f89a620fdf37670a5954408c46f3d22535ad568e.png" data-download-href="/uploads/short-url/ztfaXM3zTudhQln9szbOllTc7fw.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f89a620fdf37670a5954408c46f3d22535ad568e.png" alt="Capture" data-base62-sha1="ztfaXM3zTudhQln9szbOllTc7fw" width="690" height="193" data-dominant-color="F1EEEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1428×401 28.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Sunderlandkyl (2020-05-01 17:04 UTC)

<p>Can you make an issue on the PlusLib issue tracker (<a href="https://github.com/PlusToolkit/PlusLib/issues/new" rel="nofollow noopener">https://github.com/PlusToolkit/PlusLib/issues/new</a>), and attach your config file to the issue?<br>
Thanks!</p>

---
