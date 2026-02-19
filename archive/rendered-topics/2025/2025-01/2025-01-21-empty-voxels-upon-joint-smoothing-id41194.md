---
topic_id: 41194
title: "Empty Voxels Upon Joint Smoothing"
date: 2025-01-21
url: https://discourse.slicer.org/t/41194
---

# Empty voxels upon joint smoothing

**Topic ID**: 41194
**Date**: 2025-01-21
**URL**: https://discourse.slicer.org/t/empty-voxels-upon-joint-smoothing/41194

---

## Post #1 by @coco (2025-01-21 15:38 UTC)

<p>Dear all,<br>
We have brain samples that we segment using a seeding/grow from seeds approach followed by a joint smoothing. This last step results in a couple of empty voxels as you can see on the picture below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b520c22a8af0256996d0910ec52b2d513c991d59.jpeg" data-download-href="/uploads/short-url/pQkBCEYKjWWfSuY2iOkUBrGtxtT.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b520c22a8af0256996d0910ec52b2d513c991d59_2_686x500.jpeg" alt="image" data-base62-sha1="pQkBCEYKjWWfSuY2iOkUBrGtxtT" width="686" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b520c22a8af0256996d0910ec52b2d513c991d59_2_686x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b520c22a8af0256996d0910ec52b2d513c991d59.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b520c22a8af0256996d0910ec52b2d513c991d59.jpeg 2x" data-dominant-color="6B8268"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">778×567 72 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
the red circles some of these empty voxels. is there a way to fill them randomly by one adjacent segment ?<br>
thanks for your help and thoughts<br>
s</p>

---

## Post #2 by @pieper (2025-01-21 18:51 UTC)

<p>Probably running Grow from seeds would work (if those are the only unlabled ones in the segmentation)</p>

---

## Post #3 by @coco (2025-01-22 08:41 UTC)

<p>Obviously ! worked like a charm of course</p>

---

## Post #4 by @cpinter (2025-01-22 09:55 UTC)

<p>As far as I remembered this shouldn’t have occurred. The <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html">documentation</a> also backs my memory, it says: “smoothes multiple segments at once, preserving watertight interface between them”. Should we investigate this issue, or is it something known?</p>
<p><a class="mention" href="/u/coco">@coco</a> Was the original segmentation watertight to begin with?</p>

---

## Post #5 by @coco (2025-01-22 10:08 UTC)

<p>We do a grow from seeds so in principle yes, every pixel is then assigned to a segment.<br>
Just in case it is relevant, I will just add that we had a few voxels inside the structures that were masked (so can’t be assigned anyway) but the empty voxels are not those ones that ended up unassigned to a segment. I don’t think the masked pixels were anywhere near the ones that ended up non assigned. This is another matter we solved separatly but perhaps it is linked ?</p>

---

## Post #6 by @cpinter (2025-01-22 10:18 UTC)

<p>I am not sure. Is is possible for you to share the segmentation before doing the joint smoothing? Preferably in an MRB scene.</p>
<p>Btw which Slicer version do you use? If 5.6.2, can you please try the latest preview? 5.8 is cooking right now, so the latest preview is practically the new 5.8. Thanks!</p>

---

## Post #7 by @coco (2025-01-22 16:05 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="6" data-topic="41194">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>If 5.6.2, can you please try the latest preview? 5.8 is cooking right now, so the latest preview is practically the new 5.8. Thanks!</p>
</blockquote>
</aside>
<p>Yes, I use 5.6.2, and can try 5.8. will keep posted. I should have a file to share soon as well,<br>
many thanks to you<br>
s</p>

---
