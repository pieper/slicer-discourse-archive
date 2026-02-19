---
topic_id: 26176
title: "Stretched Cpr Instead Of Straightened Cpr"
date: 2022-11-10
url: https://discourse.slicer.org/t/26176
---

# Stretched CPR instead of Straightened CPR

**Topic ID**: 26176
**Date**: 2022-11-10
**URL**: https://discourse.slicer.org/t/stretched-cpr-instead-of-straightened-cpr/26176

---

## Post #1 by @hbr (2022-11-10 05:26 UTC)

<p>hi</p>
<p>i want to use Stretched CPR in slicer but i found in sandbox extension in curved planar reformat just Straightened CPR.<br>
like this pic:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/7316dbc82e8a763e9ed985bd5428d9d54451a561.png" alt="cpr" data-base62-sha1="gq7SLg2Hp9nKs1UPv7gT7rfkiVr" width="371" height="426"></p>
<p>Is Stretched CPR in any extensions in slicer?</p>
<p>thanks.</p>

---

## Post #2 by @lassoan (2022-11-21 22:06 UTC)

<p>Currently only straightened mode is implemented. It would not be hard to add the stretched mode - this code part would need to be updated to compute the slice axes so that the two axes are not the curve normal and binormal but the curve normal and a fixed direction. This paper explains the difference between the straightened and stretched mode: <a href="https://www.cg.tuwien.ac.at/research/vis/adapt/Vis2002/AKanitsar_CPR.pdf">https://www.cg.tuwien.ac.at/research/vis/adapt/Vis2002/AKanitsar_CPR.pdf</a></p>

---

## Post #3 by @lassoan (2022-11-22 21:50 UTC)

<p>I’ve implemented <a href="https://github.com/PerkLab/SlicerSandbox#curved-planar-reformat">“stretched” mode</a>.</p>
<p><img src="https://raw.githubusercontent.com/PerkLab/SlicerSandbox/master/CurvedPlanarReformat_4.png" alt="CurvedPlanarReformat_4.png" width="690" height="201"></p>
<p>You can get it by updating Sandbox module from the Extensions Manager tomorrow. Let me know how it works for you.</p>

---

## Post #4 by @hbr (2022-11-23 04:56 UTC)

<p>Hi Andras</p>
<p>thanks alot</p>
<p>it is great work</p>
<p>i will test it and let you know how it works</p>

---

## Post #5 by @hbr (2022-11-23 05:33 UTC)

<p>sorry</p>
<p>i updated sandbox but i can not found where it is</p>

---

## Post #6 by @lassoan (2022-11-24 02:33 UTC)

<p>It is available in the extensions manager for Slicer versions 5.2.0 (to be released in a day or two) or the latest Slicer 5.3.1 release (not for 5.0.3).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/28b792964b40233eb21e617c8a70198e07fe2f53.png" data-download-href="/uploads/short-url/5OcoSDT1s7WQLdKCaU1WXKIkoMP.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/28b792964b40233eb21e617c8a70198e07fe2f53_2_450x500.png" alt="image" data-base62-sha1="5OcoSDT1s7WQLdKCaU1WXKIkoMP" width="450" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/28b792964b40233eb21e617c8a70198e07fe2f53_2_450x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/28b792964b40233eb21e617c8a70198e07fe2f53.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/28b792964b40233eb21e617c8a70198e07fe2f53.png 2x" data-dominant-color="F0F0F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">660×732 93.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @hbr (2022-11-24 06:36 UTC)

<p>ok</p>
<p>i have to change slicer version</p>
<p>thanks</p>

---
