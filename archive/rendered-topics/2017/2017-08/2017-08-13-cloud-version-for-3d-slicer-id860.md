---
topic_id: 860
title: "Cloud Version For 3D Slicer"
date: 2017-08-13
url: https://discourse.slicer.org/t/860
---

# Cloud version for 3D Slicer

**Topic ID**: 860
**Date**: 2017-08-13
**URL**: https://discourse.slicer.org/t/cloud-version-for-3d-slicer/860

---

## Post #1 by @hamedtopic (2017-08-13 04:20 UTC)

<p>Hi</p>
<p>Is there any way for me to work with my datasets right from my iPad?!</p>

---

## Post #2 by @jcfr (2017-08-14 15:55 UTC)

<p>Hi Hamed,</p>
<p>It is currently not possible to run 3D Slicer  on an IPad. For now, only devices running Linux or Windows operating systems are supported.</p>
<p>Regarding the cloud version, there is not yet turn-key solution readily available to run 3D Slicer on the cloud. Based on your specific needs, we could recommend possible approaches.</p>
<p>Here is an example from <a class="mention" href="/u/lassoan">@lassoan</a> running 3D Slicer on a windows tablet:</p>
<div class="lazyYT" data-youtube-id="0Nsya9vBswE" data-youtube-title="Running 3D Slicer on inexpensive tablet" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>

---

## Post #3 by @lassoan (2017-08-15 02:42 UTC)

<p>There is also the option of running Slicer in any web browser. In this case, Slicer runs on a container on a desktop computer or on a virtual machine hosted on Amazon, etc. For example, you can try this Slicer instance, running in a Docker container: <em>(link removed)</em></p>
<p>In case you want to replicate this, it is the dit4c-container-slicer container, available on Docker Hub.</p>

---

## Post #4 by @hamedtopic (2017-08-15 09:39 UTC)

<p>Hey!it’s really amazing!<br>
Could I define a new project for my datasets which are 3DRA of a brain aneurysm with XA modality?!</p>

---

## Post #5 by @lassoan (2017-08-15 18:22 UTC)

<p>What would you like to do? Just use Slicer in the angio room? Where the data would come from and when? Would you need to process the acquired data (segment, create surgical plan, etc)? Would you like to do this pre-processing/planning on the tablet or someone else would do it with a mouse/keyboard on a computer?</p>
<p>The simplest to set up is to run Slicer on a Windows tablet directly (as shown in the video above). Difficulty may be to push acquired data to Slicer (need to connect to hospital DICOM network) and preprocess on tablet.</p>
<p>You can also run Slicer directly on a desktop/laptop and connecting from a tablet using VNC free remote desktop software, as we do it during breast surgeries - see an example here:</p>
<div class="lazyYT" data-youtube-id="90l0T1ADe_Y" data-youtube-title="Navigated breast conserving surgery" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque&amp;start=56"></div>
<p>The computer can be on the wired hospital network, so getting acquired images would work reliably and the same application can be operated from the control room using keyboard/mouse (so that segmentation or other pre-processing can be performed quickly and accurately there) and in the angio suite from the tablet (browsing slices, adjusting views, etc).</p>
<p>Running Slicer “on the cloud” can be configured very similarly to how you set it up on a local computer. However, it is a bit more steps to set it up and sending patient data to public cloud providers might be problematic. It may worth the trouble to choose this option if you want to access the data from outside the hospital network but hospital network policies do not let you access computers remotely.</p>

---

## Post #6 by @hamedtopic (2017-08-16 06:11 UTC)

<p>Thanks so much for your reply dear Andras,<br>
Actually, the 2nd case is true! I want to access 3d slicer when my laptop is not at hand but I simply have access to the internet via my cellular iPad and I could analyze the case thorugh my mailbox. But, unfortunately, 3d slicer has not an iOS version, so I was thinking of a way to access the app through the net or a cloud-based version or sth like this. Remote control is not a good solution for this subject since the PC/laptop is not always turned on.</p>

---

## Post #7 by @lassoan (2017-08-16 13:58 UTC)

<p>You could rent a virtual machine on a cloud provider, but a strong one that can run Slicer very well would probably cost at least $100 or so a month. It is probably cheaper to buy a laptop or desktop computer and run it in your basement and set up remote access on it. It is probably even cheaper and simpler to just buy a Windows tablet that can run Slicer directly, you can get smaller and cheaper ones as an iPad and they can do much more - you can connect a mouse/keyboard/monitor if needed, you can use touch or pen, connect to hospital network to get the images directly, etc.</p>
<p>If you only need to view data then you may consider using one of the simple DICOM image viewers that are available for iOS.</p>
<p>Storing patient data on non-hospital-controlled computers might be problematic due to data security, so make sure to comply with all regulations of your hospital.</p>

---

## Post #8 by @hamedtopic (2017-08-16 14:12 UTC)

<p>Thanks so much!<br>
It was helpful!</p>

---
