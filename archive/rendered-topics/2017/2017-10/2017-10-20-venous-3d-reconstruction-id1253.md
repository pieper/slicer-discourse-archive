---
topic_id: 1253
title: "Venous 3D Reconstruction"
date: 2017-10-20
url: https://discourse.slicer.org/t/1253
---

# Venous 3d reconstruction

**Topic ID**: 1253
**Date**: 2017-10-20
**URL**: https://discourse.slicer.org/t/venous-3d-reconstruction/1253

---

## Post #1 by @Keno_Mentor (2017-10-20 13:42 UTC)

<p>Operating system: macOS<br>
Slicer version: 4.5<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Good day all,</p>
<p>I am trying to create a 3D reconstruction of the portal vein and related structures. I have a CT with liver portal phase.</p>
<p>The radiology department at my institution tell me it’s not possible as the contrast intensity in a portal phase isn’t enough to differentiate from the surrounding tissue. My thinking is that it should be possible, as I can clearly see the portal structures by scrolling through the scan in the usual way.</p>
<p>I’ve tried using the rendering presets in Slicer but havent had much luck. Can anyone suggest another method? Or extension that specifically deals with this?</p>
<p>With thanks,<br>
Keno</p>

---

## Post #2 by @lassoan (2017-10-20 14:08 UTC)

<p>It should be doable. You can use the Segment Editor module to semi-automatically segment the vein.</p>
<p>Threshold effect can probably get you some of the larger vessels segments.</p>
<p>For segmenting smaller vessels you can:</p>
<ol>
<li>Use <code>Crop volume</code> module to resample your input volume:
<ul>
<li>set isotropic voxel spacing</li>
<li>adjust Spacing scale to make the cropped volume spacing (shown in Volume information section) at least a few times smaller than the smallest vessel diameter that you want to segment</li>
<li>adjust the region of interest to the minimum to keep the cropped image dimensions reasonable (preferably not more than a few hundred along each axis)</li>
</ul>
</li>
<li>Preprocess the image using <code>Vesselness filtering</code> module in VMTK extension, which removes structures that has similar intensity as vessels but not have a tubular shape</li>
<li>In <code>Segment editor</code> module, choose vesselness image as master volume and use Threshold effect and/or use Paint effect with intensity threshold to segment vessels.</li>
</ol>

---

## Post #3 by @Keno_Mentor (2017-10-20 15:06 UTC)

<p>Thanks Andras!  I’ll give that a try…</p>

---

## Post #4 by @Keno_Mentor (2017-10-23 13:40 UTC)

<p>Hello Andras,</p>
<p>I’m having some trouble following your advice.  When I select the vessel<br>
ness option under the VMTK module, I get and "error to load VMTK libraries<br>
error.</p>
<p>Any ideas?</p>

---

## Post #5 by @lassoan (2017-10-23 14:06 UTC)

<p>Why Slicer version do you use? What operating system?<br>
Please try with the latest nightly version.</p>

---

## Post #6 by @whu (2022-08-16 06:00 UTC)

<p>I don’t know if the method you mentioned can divide the femoral vein from the CT data.<br>
thanks. <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>

---
