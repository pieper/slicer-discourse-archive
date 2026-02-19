---
topic_id: 3575
title: "Segmenting Fractured Bone Fragments"
date: 2018-07-25
url: https://discourse.slicer.org/t/3575
---

# Segmenting fractured bone fragments

**Topic ID**: 3575
**Date**: 2018-07-25
**URL**: https://discourse.slicer.org/t/segmenting-fractured-bone-fragments/3575

---

## Post #1 by @Shamay_Agaron (2018-07-25 17:39 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/1515b3c3124afc113045dbe61baa17b3864dcf4f.jpeg" data-download-href="/uploads/short-url/30wwsMVPZq5fKoryISAAvGzHUNV.jpeg?dl=1" title="jkfs-24-96-g001-l" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/1515b3c3124afc113045dbe61baa17b3864dcf4f_2_487x500.jpeg" alt="jkfs-24-96-g001-l" data-base62-sha1="30wwsMVPZq5fKoryISAAvGzHUNV" width="487" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/1515b3c3124afc113045dbe61baa17b3864dcf4f_2_487x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/1515b3c3124afc113045dbe61baa17b3864dcf4f.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/1515b3c3124afc113045dbe61baa17b3864dcf4f.jpeg 2x" data-dominant-color="504D48"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">jkfs-24-96-g001-l</span><span class="informations">712×730 76.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I was wondering if anyone can recommend a semi-automatic way to separate different fractured bone fragments. I’ve been trying to use the various functions available in Segment Editor and it’s extension, but the main issue seems to be that the different fragments are often connected/fused in several places and are of the same intensity so the Grow from Seeds function, for example, has a hard time locating/identifying the different fracture pieces.</p>
<p>Any ideas? For privacy reasons, I just posted a picture featuring a similar injury from Google rather than the model I am working with.</p>

---

## Post #2 by @lassoan (2018-07-25 19:03 UTC)

<p>There are many tools for separating different parts of a segment. Get familiar with masking section, as it allows you to restrict what parts of segments may be edited and how.</p>
<p>For example, you can use Scissors effect combined with masking as shown here: <a href="https://lassoan.github.io/SlicerSegmentationRecipes/Craniotomy/">https://lassoan.github.io/SlicerSegmentationRecipes/Craniotomy/</a></p>
<p>You can also use Paint, Draw, and Erase effects with masking.</p>
<p>You may also use Grow from seeds without any masking. Just add a segment for all “other” materials (soft tissue, air, etc.). If there is not enough separation between parts of the bone then you may need to paint more seeds interactively, while in preview mode.</p>

---

## Post #3 by @Shamay_Agaron (2018-07-25 19:44 UTC)

<p>Thank you for the thorough reply. One of the masking features that I’m interested in is the “editable intensity range”, as I’ve gotten it to work for paint/draw/erase tools but not for the “grow from seeds” function. Regardless of the range that I choose, the function picks up noise from outside of the editable intensity range and I can’t figure out why.</p>

---

## Post #4 by @lassoan (2018-07-25 20:41 UTC)

<p>As stated in documentation of ‘Grow from seeds’, masking effects are bypassed. However, you can very easily simulate masking, because seeds are never modified by the effect. So, if you fill some regions with simple thresholding, then those regions will never assigned to any other segment.</p>

---

## Post #5 by @three_wise_surgeons (2019-06-10 20:22 UTC)

<p>Hi Andreas and Shamay<br>
I have the same problem when it comes to any metaphyseal fracture. The fragments are usually in contact, the HU are similar and to segment them, i go in a slice-by-slice fashion. I watched the craniotomy example, but I found it quite different from segmenting a fractured /distal radius/proximal humerus/distal tibia…<br>
What I’m looking for is to find a method allowing me to automate the multifragmented fracture to be segmented, thus easily reduced.<br>
I think combining different segmenting tools, this could be done.<br>
Thanks!</p>

---

## Post #6 by @lassoan (2019-06-12 15:05 UTC)

<p>“Grow from seeds” effect now supports masking, so it should be well suited for segmenting/separating bone segments in contact. See step-by-step instructions in segmentation <a href="https://lassoan.github.io/SlicerSegmentationRecipes/AortaMaskedGrowFromSeeds/" rel="nofollow noopener">recipe for separating contrasted vessels and bones</a>.</p>

---
