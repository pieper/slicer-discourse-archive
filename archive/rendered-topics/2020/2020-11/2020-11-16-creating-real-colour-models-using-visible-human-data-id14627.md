---
topic_id: 14627
title: "Creating Real Colour Models Using Visible Human Data"
date: 2020-11-16
url: https://discourse.slicer.org/t/14627
---

# Creating real colour models using visible human data

**Topic ID**: 14627
**Date**: 2020-11-16
**URL**: https://discourse.slicer.org/t/creating-real-colour-models-using-visible-human-data/14627

---

## Post #1 by @SteveJJ (2020-11-16 04:35 UTC)

<p>Hello</p>
<p>I am using the visible human data set to create some 3D sliceable images.  However, when I create a model, say of the head, the colour on the outside is simply the standard green used by the segment editor.  I would like this to be the actual colouration of the visible human’s skin.  Is this possible?  I hope I am making myself clear!  I enclose a screenshot of what I have got so far</p>
<p>Thanks in advance</p>
<p>Steve<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/5325c47775c7a12328eb549f749c81b6412ee820.jpeg" data-download-href="/uploads/short-url/bRyxStOzEs1bbF8Q8iKAElTRvHi.jpeg?dl=1" title="Screenshot 2020-11-15 134353" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5325c47775c7a12328eb549f749c81b6412ee820_2_690x369.jpeg" alt="Screenshot 2020-11-15 134353" data-base62-sha1="bRyxStOzEs1bbF8Q8iKAElTRvHi" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5325c47775c7a12328eb549f749c81b6412ee820_2_690x369.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5325c47775c7a12328eb549f749c81b6412ee820_2_1035x553.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5325c47775c7a12328eb549f749c81b6412ee820_2_1380x738.jpeg 2x" data-dominant-color="756E7B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2020-11-15 134353</span><span class="informations">1920×1027 229 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-11-16 07:07 UTC)

<p>You can use “Probe volume with model” to color a model surface using an RGB volume. After you computed the scalars, go to Models module and Display/Scalars/Scalar Range Mode choose “Direct color mapping”.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1cd72804108dbe5b821255fe4ae41b413b081d4b.jpeg" data-download-href="/uploads/short-url/478l2PgYgcoqsDZTDXhYaWc1fgT.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1cd72804108dbe5b821255fe4ae41b413b081d4b_2_690x424.jpeg" alt="image" data-base62-sha1="478l2PgYgcoqsDZTDXhYaWc1fgT" width="690" height="424" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1cd72804108dbe5b821255fe4ae41b413b081d4b_2_690x424.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1cd72804108dbe5b821255fe4ae41b413b081d4b_2_1035x636.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1cd72804108dbe5b821255fe4ae41b413b081d4b_2_1380x848.jpeg 2x" data-dominant-color="999AA3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2237×1375 585 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @lassoan (2020-11-16 16:25 UTC)

<p>2 posts were split to a new topic: <a href="/t/how-to-hide-empty-black-regions-of-the-slice-in-3d-view/14639">How to hide empty black regions of the slice in 3D view</a></p>

---

## Post #4 by @lassoan (2020-11-16 16:28 UTC)

<p>A post was merged into an existing topic: <a href="/t/how-to-hide-empty-black-regions-of-the-slice-in-3d-view/14639/3">How to hide empty black regions of the slice in 3D view</a></p>

---

## Post #5 by @SteveJJ (2020-11-20 22:38 UTC)

<p>Sometimes when I do this the colour is just plain black. If I reload the problem seems to resolve itself, but it can be quite annoying if you do a time consuming segmentation only to find you can’t add colour. Any ideas what is happening here? I’m assuming it’s a bug</p>
<p>Thanks</p>
<p>Steve</p>

---

## Post #6 by @lassoan (2020-11-20 22:51 UTC)

<p>I’m not sure what you are referring to. If we can reproduce a problem then we can fix it, but for that you may need to give us step-by-step instructions (what you do, what you expect to happen, and what happens instead).</p>

---

## Post #7 by @SteveJJ (2020-11-21 18:52 UTC)

<p>Turns out I needed to harden the transform I was using.  All sorted now.<br>
Thanks</p>

---
