---
topic_id: 10506
title: "Problem In Point Orientation"
date: 2020-03-02
url: https://discourse.slicer.org/t/10506
---

# Problem in Point Orientation

**Topic ID**: 10506
**Date**: 2020-03-02
**URL**: https://discourse.slicer.org/t/problem-in-point-orientation/10506

---

## Post #1 by @brhoom (2020-03-02 19:18 UTC)

<p>Dear all,<br>
I got a dataset from VerSeg challenge. It has json files that describes center points of vertebral bodies in a  3D image. here is what ir says:</p>
<blockquote>
<p>The centroid annotations are with respect to the coordinate axis fixed on a (P, I, R) or (A, S, L) orientation, described as:<br>
1. Origin at Superior (S) - Right (R) - Anterior (A)<br>
2. ‘X’ corresponds to S → I direction<br>
3. ‘Y’ corresponds to A → P direction<br>
4. ‘Z’ corresponds to R → L direction</p>
</blockquote>
<p>I tried to visualize L4 centroid in Slicer by adding a fiducial and add the values from the json fil but the point looks far away</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de0c971f1cd854868c306aeaa5c0271598987150.png" alt="fiducials" data-base62-sha1="vGkYkust1gIqHnrNkBvbdhKyR4k" width="498" height="70"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e57e66aa7a28d14ede4f836c432f1e15dc2daea9.png" alt="L4" data-base62-sha1="wKc9wRgevnmTaE3o8N3ShFlKqSJ" width="500" height="274"></p>
<p>How can I change the orientation of L4 correctly to be something like L4s (L4s is located by me)<br>
Here are the files:<br>
json file: <a href="https://drive.google.com/file/d/1vu-YW68CrkIuRQPwAxNsRUl-Ja6NzfSP/view" rel="noopener nofollow ugc">https://drive.google.com/file/d/1vu-YW68CrkIuRQPwAxNsRUl-Ja6NzfSP/view</a><br>
image: <a href="https://drive.google.com/file/d/1nDn_2S_HoqqPcMR_M8ixyv2O4j0huHkh/view" rel="noopener nofollow ugc">https://drive.google.com/file/d/1nDn_2S_HoqqPcMR_M8ixyv2O4j0huHkh/view</a></p>

---

## Post #2 by @lassoan (2020-03-02 20:05 UTC)

<p>This code snippets sets markup fiducial points positions correctly:</p>
<pre><code class="lang-python">import json
data = json.load(open("verse063_ctd.json", 'r'))
bounds = [0,0,0,0,0,0]
slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLSegmentationNode").GetBounds(bounds)
markupsNode=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode")
for point in data:
    markupsNode.AddControlPointWorld(vtk.vtkVector3d(bounds[0]+point["Z"], bounds[2]+point["Y"], bounds[4]+point["X"]), "Label: {0}".format(point["label"]))
</code></pre>
<p>From this, it is quite clear that the json file is not optimal, because:</p>
<ol>
<li>You can only interpret in with respect to another file. Instead, the file should contain physical coordinates (the origin of the input image included).</li>
<li>Coordinate system axes direcrtions are S, A, R, while in DICOM (and therefore all other files derived from them), anatomical coordinate axis directions are L, P, S (order should be inverted and directions of first two axes should be inverted)</li>
</ol>

---

## Post #3 by @brhoom (2020-03-02 20:33 UTC)

<p>Thanks, <a class="mention" href="/u/lassoan">@lassoan</a> for your quick reply.</p>
<blockquote>
<p>You can only interpret in with respect to another file. Instead, the file should contain physical coordinates (the origin of the input image included).</p>
</blockquote>
<p>The files come with images here is the one from this segmentation</p>
<p><a href="https://drive.google.com/file/d/1J4p6CWSczylnsfjwS-fV0VXOrAaFC31i/view" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/file/d/1J4p6CWSczylnsfjwS-fV0VXOrAaFC31i/view</a></p>
<p>Here is the result of your script.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/ccb94de55a404a5add312adb27f2d5ebfe08aafb.png" data-download-href="/uploads/short-url/td4pPgudyo7Rps4C9E5l7dEFuDV.png?dl=1" title="andras" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/ccb94de55a404a5add312adb27f2d5ebfe08aafb_2_347x500.png" alt="andras" data-base62-sha1="td4pPgudyo7Rps4C9E5l7dEFuDV" width="347" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/ccb94de55a404a5add312adb27f2d5ebfe08aafb_2_347x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/ccb94de55a404a5add312adb27f2d5ebfe08aafb.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/ccb94de55a404a5add312adb27f2d5ebfe08aafb.png 2x" data-dominant-color="8F8BAA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">andras</span><span class="informations">348×501 79.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The points are now close to the vertebrae but not in the center.  How can I involve the origin correctly?</p>

---

## Post #4 by @lassoan (2020-03-03 01:34 UTC)

<p>You could probably tune the code snippet above to get the correct results, but it would be just a workaround. Instead, I would recommend to ask developers of the software to put save physical coordinates in LPS coordinate system.</p>

---
