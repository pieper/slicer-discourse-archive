---
topic_id: 6924
title: "Level Set Segmentation Extracts Only One Vessel At A Time"
date: 2019-05-25
url: https://discourse.slicer.org/t/6924
---

# Level set segmentation extracts only one vessel at a time

**Topic ID**: 6924
**Date**: 2019-05-25
**URL**: https://discourse.slicer.org/t/level-set-segmentation-extracts-only-one-vessel-at-a-time/6924

---

## Post #1 by @Amine (2019-05-25 04:35 UTC)

<p>as in this tutorial <a href="https://www.youtube.com/watch?v=DJ2032yo5Co" rel="nofollow noopener">https://www.youtube.com/watch?v=DJ2032yo5Co</a><br>
i try to use level set segmentation (after successful vesselness filtering) but the newer version of level set segmentation seems to only extract one vessel at a time based on a starting and ending seed points, I can’t get it to work with only one seed ( to extract the whole tree like in the tutorial). thanks for your help</p>

---

## Post #2 by @lassoan (2019-05-25 13:30 UTC)

<p>Maybe the level set module used a different method a very many years ago, but it was later changed to the current method.</p>
<p>The old method looks similar to Fast marching. You can install SegmentEditorExtraEffects extension and try Fast marching, Grow from seeds, and Watershed effects in the Segment Editor module.</p>

---

## Post #3 by @Amine (2019-05-25 20:22 UTC)

<p>it indeed looks like a basic extraction method, i was hoping it would take in account contours or any tree/ branch detection algorithm, thanks for your reply!</p>

---

## Post #4 by @lassoan (2019-05-25 22:36 UTC)

<p>VMTK extension has centerline extraction and tree model builder module, too.</p>

---

## Post #5 by @Amine (2019-05-27 06:29 UTC)

<p>Thanks, i cant find the " tree builder " module anywhere, only have vesselness filtering, level set segmentation (wich does what i want but just for one at a time) and centerline extraction (wich uses an already made vascular model). i would just like to use vesselness output to segment the whole tree with a "tubular/branch seeking " algorithm instead of just painting it with threshold/ region growing (i assume the output would be a lot more refined)</p>

---

## Post #6 by @lassoan (2019-05-27 13:12 UTC)

<p>By tree builder I meant centerline extraction module. It can work on the model exported from segmentation (in Data module, right-click on segmentation node and choose to export to model).</p>
<aside class="quote no-group" data-username="Amine" data-post="5" data-topic="6924">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/amine/48/4844_2.png" class="avatar"> Amine:</div>
<blockquote>
<p>i would just like to use vesselness output to segment the whole tree with a "tubular/branch seeking " algorithm instead</p>
</blockquote>
</aside>
<p>In the current workflow, branch searching happens after segmentation, on the generated model node. Why would you like to change the order? Are you aware of a “tubular/branch seeking” vessel segmentation algorithm in VMTK?</p>

---

## Post #7 by @Amine (2019-05-27 23:52 UTC)

<p>The segmentation step is the problematic one here, vesselness enhances the volume but its not perfect, using any general purpose tool (grow from seeds/threshold paint/ region growing) can yield satisfying results but often has artifacts or irregular diameters<br>
No i did not see such a thing anywhere, just assumed it was part of Level set segmentation since it worked without artifacts in the video (but i now understand it only used something like region growing)</p>
<p>the purpose of this would be to “guide” the segmentation or model creation based on a tree-seeking logic (like centerline’s shape) thus keeping diameters as the average of the neighboring section, producing a more cylindrical shape and clean intersections. inputs would be either vesselness volume, a starting seed and a direction seed (materialise mimics did something similar for airway segmentation <a href="https://www.youtube.com/watch?v=OYncaVGtGEM" class="inline-onebox" rel="noopener nofollow ugc">How to Automatically Segment Airways | Mimics Innovation Suite | Materialise Medical - YouTube</a> )</p>
<p>for a practical example, here is a portal vein reconstruction after vesselness, after some smoothing , then i extracted the centerline and generated a tree model using it (this is just to show the tree generation concept, of course i’m talking about extraction right from a volume, without making an initial segmentation, thus taking in account the real diameter and shape data)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/81772e740b15a246f7f151c4465e7a99d8d440d9.jpeg" data-download-href="/uploads/short-url/itiWcGCjE8DMABMS7jeKnj40K6d.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/81772e740b15a246f7f151c4465e7a99d8d440d9_2_690x307.jpeg" alt="1" data-base62-sha1="itiWcGCjE8DMABMS7jeKnj40K6d" width="690" height="307" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/81772e740b15a246f7f151c4465e7a99d8d440d9_2_690x307.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/81772e740b15a246f7f151c4465e7a99d8d440d9_2_1035x460.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/81772e740b15a246f7f151c4465e7a99d8d440d9_2_1380x614.jpeg 2x" data-dominant-color="829CCA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1667×744 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>thanks for your answers, i hope i described the concept adequately</p>

---

## Post #8 by @Amine (2020-06-10 09:39 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="6924">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Are you aware of a “tubular/branch seeking” vessel segmentation algorithm in VMTK?</p>
</blockquote>
</aside>
<p>Hi, i came across <a href="https://pubmed.ncbi.nlm.nih.gov/25047734/" rel="noopener nofollow ugc">this study</a> which had me remember the branch based algorythm i spoke about, this uses the centerline tree to extrude varying diameter branches and output a clean model. tought this might be interesting.</p>

---
