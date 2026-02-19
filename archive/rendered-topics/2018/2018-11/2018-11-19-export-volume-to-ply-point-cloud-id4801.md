---
topic_id: 4801
title: "Export Volume To Ply Point Cloud"
date: 2018-11-19
url: https://discourse.slicer.org/t/4801
---

# Export volume to PLY point cloud?

**Topic ID**: 4801
**Date**: 2018-11-19
**URL**: https://discourse.slicer.org/t/export-volume-to-ply-point-cloud/4801

---

## Post #1 by @Stephan.st (2018-11-19 13:07 UTC)

<p>Hello everyone!</p>
<p>This is my first post here on the forum. I am looking for a way to export data from Slicer as a 3D point cloud, preferable in PLY format. Is there a plugin / extension that can be used for this? Otherwise I will look into coding my own…<br>
Kind regards,<br>
Stephan</p>

---

## Post #2 by @lassoan (2018-11-19 13:16 UTC)

<p>Would you like to export each voxel as a point? Whatvwould be the use case? Point cloud rendering would be probably lower quality and require more computation than volume (rectilinear grid) rendering.</p>
<p>If you are looking for rendering of particular structures then you need to segment the volume, for example using Segment Editor module.</p>
<p>What is your end goal? Rendering, processing, analysis, printing,…?</p>

---

## Post #3 by @Stephan.st (2018-11-19 14:20 UTC)

<p>Hi Andras,</p>
<p>I work on DNN-based point cloud analysis tools, and would be curious to see what can be done with this type of data as input <img class="emoji" src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/2X/8/89c8323b83c7b72d5f03986f5a01ac353cb27076.png" alt="simple_smile"> I could develop a tool to take still image slices and project them as point clouds myself but I would need to figure out how to get the scale correct and interpret MRI scan data from scratch, so I was wondering whether this would be possible directly using Slicer.</p>
<p>cheers,</p>
<p>Stephan</p>

---

## Post #4 by @timeanddoctor (2021-02-25 14:37 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="2" data-topic="4801">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>例是什么？点云渲染的质量可能较低，并且比体积（直线网格）渲染需要更多的计算。</p>
</blockquote>
</aside>
<p>Did you deal with it ?</p>

---

## Post #5 by @mluerig (2021-05-11 08:23 UTC)

<p>I am also looking for a way to convert a volume model to a point cloud (XYZ coords), both for visualization purposes and to use for classification in a neural network (<a href="https://github.com/charlesq34/pointnet2" class="inline-onebox" rel="noopener nofollow ugc">GitHub - charlesq34/pointnet2: PointNet++: Deep Hierarchical Feature Learning on Point Sets in a Metric Space</a>)</p>

---

## Post #6 by @Stephan.st (2021-05-11 09:40 UTC)

<p>I think in the end I just used open3d and numpy and made point clouds by stacking pixels exported as points (like having one flat point cloud with no camera projection every Xmm (slice size)).</p>

---

## Post #7 by @lassoan (2021-05-11 19:58 UTC)

<p>Every model is a point cloud as well. You can just ignore the connectivity information between the points. You can also <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.arrayFromModelPoints">get the point list as a numpy array</a> and save it in any format you want.</p>
<p>However, if you drop the connectivity information then you lose lots of information and you can never reconstruct the original surface just from point positions. The more densely and uniformly the mesh points are distributed, the more information can be reconstructed later. So, before dropping connectivity information, you may want to remesh the model (subdivide, decimate, etc. or resample on a grid or use more sophisticated algorithms, such as ACVD).</p>
<p>Labelmaps seem to be much more natural, efficient, and predictable, and lossless representation of volumes, though. So I’m not sure if it is worth all the trouble of converting to a point cloud representation.</p>

---
