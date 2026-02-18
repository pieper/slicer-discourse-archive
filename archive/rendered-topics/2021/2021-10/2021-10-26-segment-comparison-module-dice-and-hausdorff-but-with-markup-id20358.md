# Segment comparison module (Dice and Hausdorff) - but with markup points

**Topic ID**: 20358
**Date**: 2021-10-26
**URL**: https://discourse.slicer.org/t/segment-comparison-module-dice-and-hausdorff-but-with-markup-points/20358

---

## Post #1 by @mk.kassai (2021-10-26 11:43 UTC)

<p>Hi,</p>
<p>I want to evaluate segmentation by comparing them to markup points.<br>
I would be interested in the Dice metrics; however, the only module I found with Dice is the segment comparison which works only with segments.<br>
I tried a few ways to solve the problem, my ideas were to mask a volume or segmentation with the points or create new segmentations from the points, but they all failed.<br>
If someone can give me a solution to create small uniform dots for each of the points in a node, that would solve my problem.</p>
<p>Thank you!</p>

---

## Post #2 by @cpinter (2021-10-27 16:36 UTC)

<p>After a few re-reads of your description it is not clear to me how would you compare segmentation to markups (image to points basically).</p>
<p>How are these markup points placed? Are they marking the edge of the object? If you use the <code>Surface cut</code> effect in Segment Editor (you may need to install the SegmentEditorExtraEffects extension), does it help?</p>

---

## Post #3 by @mk.kassai (2021-10-28 07:53 UTC)

<p>Dear Csaba,</p>
<p>Thank you for your reply.<br>
I would like to compare left atrium electroanatomic maps to segmentations I made from MRI images.<br>
The electroanatomic maps from Carto arrive in a .txt format, which can be imported to slicer as markup points (Or at least I could only import them that way).<br>
In <a href="https://discourse.slicer.org/t/import-carto-electroanatomic-maps-to-slicer/19316">this other</a> thread, we discussed about it with <a class="mention" href="/u/lassoan">@lassoan</a>  and <a class="mention" href="/u/stephan">@stephan</a>. That’s my other challenge, but the data is the same.<br>
I would like to convert the points to segments/models to be able to get the Dice and Hausdorff metrics. By this I mean converting each point in a markup node to a segment that has small uniform volumes, like 1 mm wide spheres for each point so I can run the Segment Comparison module to calculate Hausdorff distances and Slice metrics.<br>
The markup points basically the raw data of the electroanatomic map, however I filtered them based on bipolar value, to create two sets of points: scarred and not scarred regions.<br>
I know I can recreate the approximation of the map by using the MarkupsToModel module, but it would just give me two slightly different shape, that won’t correspond to the atrium wall.<br>
On the screenshots, I tried to show the wall segmentation and the points that I’d like to compare.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf185e5ab07229ae2fe0d4750f7948e67c65cb90.png" data-download-href="/uploads/short-url/rgvpbJF9jEm1QLtHqAt8vz9ANwY.png?dl=1" title="Screenshot 2021-10-28 at 9.38.31" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf185e5ab07229ae2fe0d4750f7948e67c65cb90_2_596x500.png" alt="Screenshot 2021-10-28 at 9.38.31" data-base62-sha1="rgvpbJF9jEm1QLtHqAt8vz9ANwY" width="596" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf185e5ab07229ae2fe0d4750f7948e67c65cb90_2_596x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf185e5ab07229ae2fe0d4750f7948e67c65cb90_2_894x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf185e5ab07229ae2fe0d4750f7948e67c65cb90_2_1192x1000.png 2x" data-dominant-color="9A9CC4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2021-10-28 at 9.38.31</span><span class="informations">1363×1142 244 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/cabaf7bfb74932640d1603fdbfc9de4804dbadf8.png" alt="Screenshot 2021-10-28 at 9.38.51" data-base62-sha1="sVr1Aw0ppMGl2HjfeMbK02EwRkc" width="674" height="100"></p>

---

## Post #4 by @cpinter (2021-10-29 14:14 UTC)

<p>I think your best bet is still the MarkupsToModel approach, then importing that model into a segmentation (right-click model in Data module), then use the Segment Comparison module to compute the values you need.</p>
<p>If you read about how Dice and Hausdorff works (I think you should), then you’ll see that Dice works on volumes. Also Dice performs very poorly on data that consists of thin or elaborately shaped objects, and your small sphere approach fits this category fully, so Dice will give you values that cannot be interpreted well. For a simple maximum Hausdorff distance you don’t actually need volumes, you can just compare the two sets of points. It is quite easy to do with a short Python script.</p>

---
