---
topic_id: 10086
title: "Highlight Veins And Arteries In Volume Rendering"
date: 2020-02-03
url: https://discourse.slicer.org/t/10086
---

# Highlight veins and arteries in volume rendering

**Topic ID**: 10086
**Date**: 2020-02-03
**URL**: https://discourse.slicer.org/t/highlight-veins-and-arteries-in-volume-rendering/10086

---

## Post #1 by @bernland (2020-02-03 14:02 UTC)

<p>Is there a way to combine/merge three volume renderings into one using 3D Slicer 4.10.2? Given two distinct MRI scans, I can create maximum intensity projections to highlight veins (red) and arteries (blue).</p>
<p>What I’d like to achieve is merging both veins and arteries into another volume rendering showing a patient’s skin, e.g.:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/abcddc19b96f2307d91186f9c0222626a5c55e98.png" data-download-href="/uploads/short-url/ovQHoFa0sepElV2MpYVNalDbik0.png?dl=1" title="Veins-Arteries" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abcddc19b96f2307d91186f9c0222626a5c55e98_2_690x278.png" alt="Veins-Arteries" data-base62-sha1="ovQHoFa0sepElV2MpYVNalDbik0" width="690" height="278" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abcddc19b96f2307d91186f9c0222626a5c55e98_2_690x278.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abcddc19b96f2307d91186f9c0222626a5c55e98_2_1035x417.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abcddc19b96f2307d91186f9c0222626a5c55e98_2_1380x556.png 2x" data-dominant-color="332A32"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Veins-Arteries</span><span class="informations">1387×560 539 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Can this be done in 3D Slicer?</p>
<p>Thank you,<br>
Bernhard</p>

---

## Post #2 by @lassoan (2020-02-03 14:09 UTC)

<p>Multi-volume rendering is still experimental, but it should work well for this particular purpose. For displaying the skin, don’t use volume rendering, but segment it using Segment Editor using Threshold effect. To render the vessels, use Volume Rendering module, select each volume and click the “eye” icon to show them. Try both “VTK GPU Ray Casting” and “VTK Multi-Volume (experimental)” methods and various rendering presets. After selecting a preset, you can adjust colors in Advanced / Volume properties / Scalar Color Mapping.</p>
<p>If you managed to render something then please post it here and we can make further suggestions.</p>

---

## Post #3 by @bernland (2020-02-04 06:32 UTC)

<p>Thank you, <a class="mention" href="/u/lassoan">@lassoan</a>.</p>
<p>How do I assign distinct colors to volumes? Whenever I adjust colors as per your instructions, the changes are being applied to all rendered volumes. I’d rather highlight one volume in blue and another one in red. Is that possible at all?</p>
<p>Thank you,<br>
Bernhard</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be3060154036db457d0096ff8112fbab5da70d63.png" data-download-href="/uploads/short-url/r8umvwuoXkFU1qt5iKaABybKik3.png?dl=1" title="Colors" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be3060154036db457d0096ff8112fbab5da70d63_2_690x373.png" alt="Colors" data-base62-sha1="r8umvwuoXkFU1qt5iKaABybKik3" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be3060154036db457d0096ff8112fbab5da70d63_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be3060154036db457d0096ff8112fbab5da70d63_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be3060154036db457d0096ff8112fbab5da70d63_2_1380x746.png 2x" data-dominant-color="564F4F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Colors</span><span class="informations">1920×1040 262 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @bernland (2020-02-04 10:28 UTC)

<p>As a side note, rendering both vessels (MIP) and skin (segmentation) looks great:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee79b6e9318183c8f626d8e885ceefcb6bc28d69.jpeg" data-download-href="/uploads/short-url/y1Epqju1m69CfEJojGLyITwuR1D.jpeg?dl=1" title="3D" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ee79b6e9318183c8f626d8e885ceefcb6bc28d69_2_690x373.jpeg" alt="3D" data-base62-sha1="y1Epqju1m69CfEJojGLyITwuR1D" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ee79b6e9318183c8f626d8e885ceefcb6bc28d69_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ee79b6e9318183c8f626d8e885ceefcb6bc28d69_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ee79b6e9318183c8f626d8e885ceefcb6bc28d69_2_1380x746.jpeg 2x" data-dominant-color="69676A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3D</span><span class="informations">1920×1040 403 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>All that’s left is a way to assign distinct colors to arteries and veins.</p>

---

## Post #5 by @lassoan (2020-02-04 14:47 UTC)

<p>Do you have all arteries in one volume and all veins in the other volume?</p>

---

## Post #6 by @bernland (2020-02-04 19:25 UTC)

<p>Yes, that’s correct. There are three different volumes that were acquired 18, 21, and 25 seconds after contrast agent had been administered. From each volume, I render a maximum intensity projection to show the vessels. That’s how I can tell veins from arteries.</p>
<p>Would it make a difference if I had all blood vessels in just one volume?</p>
<p>Thank you!</p>

---

## Post #7 by @lassoan (2020-02-04 19:35 UTC)

<p>Ok, if then show two volumes using volume rendering, each with a different color. You can change the color by setting all the control points on the color transfer function to have the same color.</p>

---

## Post #9 by @bernland (2020-02-05 08:57 UTC)

<p>Thank you for your help, <a class="mention" href="/u/lassoan">@lassoan</a>!</p>
<p>I finally managed to show each volume with a different color:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/44fc54dd5ad6757b0b782b9964eb20420ec54f38.png" data-download-href="/uploads/short-url/9Qh5jACdHHXr3epBHKH36qocDA4.png?dl=1" title="2020-02-05 Skin from Water Arteries and Veins 3D 3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/44fc54dd5ad6757b0b782b9964eb20420ec54f38_2_690x446.png" alt="2020-02-05 Skin from Water Arteries and Veins 3D 3" data-base62-sha1="9Qh5jACdHHXr3epBHKH36qocDA4" width="690" height="446" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/44fc54dd5ad6757b0b782b9964eb20420ec54f38_2_690x446.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/44fc54dd5ad6757b0b782b9964eb20420ec54f38.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/44fc54dd5ad6757b0b782b9964eb20420ec54f38.png 2x" data-dominant-color="1D1912"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2020-02-05 Skin from Water Arteries and Veins 3D 3</span><span class="informations">691×447 79.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>All I had to do was copy the MR-MIP property under Volume Rendering (module) &gt; Inputs &gt; Property.</p>
<p>Thanks again!</p>

---

## Post #10 by @SassanHashemi (2020-08-13 17:19 UTC)

<p>Fantastic images. I would really appreciate it if you could share one or a couple of screenshots of your workflow to show how you get 3D MIPs from two different datasets to show at the same time.</p>
<p>I haven’t updated my Slicer in a few months. So it’s either a new feature or I haven’t been able to figure it out.</p>
<p>Thank you in advance.</p>

---

## Post #11 by @lassoan (2020-08-13 18:20 UTC)

<p>You have multi-volume rendering in recent Slicer Preview Releases (and a few days ago even shading works well, so you can now create even nicer images). In Volume rendering module’s Display section, choose Rendering -&gt; “VTK Multi-Volume (experimental)”. It is still experimental, not thoroughly tested - if you encounter any issues then let us know.</p>

---

## Post #12 by @SassanHashemi (2020-08-18 17:23 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac445c4a8346e95583dd4ca7e814532bd25eaabd.gif" alt="IMB_4JbrNP" data-base62-sha1="ozWAn2q5HkOOISREDOJFHEVSF41" width="308" height="214"></p>
<p>Thanks a lot for your reply. It worked perfectly. In this example I am showing 3D recon of chest vasculature in a single ventricle patient with Fontan palliation (Orange) and 3D recon of increased Lymphatic channels in the neck. Some might say it’s gimmicky, but who are they to judge me!!</p>
<p>Cheers,<br>
Sassan</p>

---

## Post #13 by @lassoan (2020-08-19 01:45 UTC)

<p>This looks really nice!</p>

---

## Post #14 by @cpinter (2020-08-19 08:59 UTC)

<p>Based on this gif, it seems that you use the “VTK GPU Ray Casting” setting instead of “VTK Multi-Volume (experimental)”. This way depth information is lost, and the green structures are always “behind” the orange ones. I suggest trying the multi-volume setting.</p>

---
