# Confused with labelmap node and segmentation, and ROI?

**Topic ID**: 9465
**Date**: 2019-12-10
**URL**: https://discourse.slicer.org/t/confused-with-labelmap-node-and-segmentation-and-roi/9465

---

## Post #1 by @aiden.zhu (2019-12-10 17:39 UTC)

<p>If this question is silly, please do not laugh out loudly.</p>
<p>I am confused with the slicer’s labelmap (image volume or node) and the slicer’s segmentation, and ROIs.  What’s critical difference between them? from data-view,  aren’t they be the same? All may have multiple phases, labemap with 0, 1, 2, … while segments with ???, ROIs with different names…</p>
<p>Is there any relationship between them or conversion? ( I saw some posts talking about such conversions).</p>
<p>Anyway, I need read more and please help me and send me if you have any good links or ideas.</p>
<p>Thanks a lot.</p>

---

## Post #2 by @muratmaga (2019-12-10 17:53 UTC)

<p>The big difference between labelmap and segmentation volume is that labelmap doesn’t allow overlap between two different structures (i.e., a voxel can only assigned to one of the labels), whereas segmentation let you do that. With the exception of that constraint, you can back and forth between those two very easily using the Segmentation module.  There benefits to both of them, you can turn both into masks to define a region of interest (ROI) to run your computations on.</p>
<p>ROI can be a number of things, a mask derived from a segmentation, a rectangular box to define axes that constrains your volume, 3D primitives (like spheres, prisms etc). It simply means you are only interested what’s going on within that region/volume (volume of interest is probably more appropriate in Slicer, but ROI predates VOI).</p>

---

## Post #3 by @aiden.zhu (2019-12-10 18:55 UTC)

<p>Thanks you so much!<br>
It seems segmentation volumes have more benefit than the labelmap volumes.</p>
<p>By the way, would you have some comments on models? <a class="mention" href="/u/muratmaga">@muratmaga</a></p>

---

## Post #4 by @muratmaga (2019-12-10 20:31 UTC)

<p>I am not sure I understood your inquiry about models? You can generate 3D mesh representation of your data both from labelmap and segmentation representation, just look under the Export/Import section of the <code>Segmentations</code> module</p>

---

## Post #5 by @aiden.zhu (2019-12-11 14:17 UTC)

<p>Thanks. I guess that info is enough for me now. LOL.</p>

---

## Post #6 by @RayCui (2020-10-26 07:16 UTC)

<p>Hi, <a class="mention" href="/u/muratmaga">@muratmaga</a></p>
<p>I am confused about if export segmentation(have the situation of overlap) to labelmap, what will hapeen? Or what is the logic to deal with overlap?</p>

---

## Post #7 by @RayCui (2020-10-26 07:35 UTC)

<aside class="quote no-group" data-username="RayCui" data-post="6" data-topic="9465">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/raycui/48/4517_2.png" class="avatar"> RayCui:</div>
<blockquote>
<p>I am confused about if export segmentation(have the situation of overlap) to labelmap, what will hapeen? Or what is the logic to deal with overlap?</p>
</blockquote>
</aside>
<p>I have try it. It maybe depends on your segment order. You can right click the segment, select move up or move down.</p>

---
