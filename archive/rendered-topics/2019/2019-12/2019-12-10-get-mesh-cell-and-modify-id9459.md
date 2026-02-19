---
topic_id: 9459
title: "Get Mesh Cell And Modify"
date: 2019-12-10
url: https://discourse.slicer.org/t/9459
---

# Get Mesh Cell and Modify

**Topic ID**: 9459
**Date**: 2019-12-10
**URL**: https://discourse.slicer.org/t/get-mesh-cell-and-modify/9459

---

## Post #1 by @lausiv (2019-12-10 08:05 UTC)

<p>for mesh cell 1 …, end of mesh   &lt;== executing all of the mesh</p>
<ol>
<li>Get each mesh cell(below first picture) of all the mesh cells in the volume</li>
<li>Modify each cell value(color)</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f8261af1125092ef1047c68237ecc5db9a2f6f2.png" data-download-href="/uploads/short-url/93Pq9HNdMNkBlUBaAnO0NE5q0pA.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f8261af1125092ef1047c68237ecc5db9a2f6f2.png" alt="image" data-base62-sha1="93Pq9HNdMNkBlUBaAnO0NE5q0pA" width="593" height="499" data-dominant-color="9F9D6E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">672×566 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f3726fb1cd714404b3f747cc292cd5bc89b9657.jpeg" data-download-href="/uploads/short-url/i9oNIEsMz2s8YNTKT4ltueSo1in.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7f3726fb1cd714404b3f747cc292cd5bc89b9657_2_690x362.jpeg" alt="image" data-base62-sha1="i9oNIEsMz2s8YNTKT4ltueSo1in" width="690" height="362" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7f3726fb1cd714404b3f747cc292cd5bc89b9657_2_690x362.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7f3726fb1cd714404b3f747cc292cd5bc89b9657_2_1035x543.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f3726fb1cd714404b3f747cc292cd5bc89b9657.jpeg 2x" data-dominant-color="979796"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1200×630 374 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>referral script code^^</p>
<blockquote>
<p>modelNode = slicer.util.getNode(inputVolume.GetID())<br>
m = modelNode.GetMesh()</p>
<pre><code class="lang-auto">trianglefilter = vtk.vtkTriangleFilter()

trianglefilter.SetInputData(m)
trianglefilter.Update()

cellPointIds = vtk.vtkIdList()

trianglefilter.GetOutput().GetCellPoints(2978, cellPointIds)

for i in range(0,3):
    print(cellPointIds.GetId(i))
    
neighbourcells = vtk.vtkIdList()

idList = vtk.vtkIdList()
idList.SetNumberOfIds(3)
idList.SetId(0,1552)
</code></pre>
</blockquote>

---

## Post #2 by @lassoan (2019-12-10 20:05 UTC)

<p>Let us know if you have any questions.</p>

---

## Post #3 by @lausiv (2019-12-11 00:17 UTC)

<p>I will do it by myself and let sample code shared in this page^^</p>

---

## Post #4 by @lausiv (2019-12-15 05:01 UTC)

<p>I found below when executing python script</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/6552df9ca578cc22a0e637545648f6ac377f4d0b.png" data-download-href="/uploads/short-url/eslMmQemFP3ChtuiD1vxKv7WxQL.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/6552df9ca578cc22a0e637545648f6ac377f4d0b.png" alt="image" data-base62-sha1="eslMmQemFP3ChtuiD1vxKv7WxQL" width="690" height="103" data-dominant-color="F7EFF4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">938×141 7.17 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_scalar_values_at_surface_of_a_model" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_scalar_values_at_surface_of_a_model</a></p>

---

## Post #5 by @lassoan (2019-12-15 06:05 UTC)

<p>You have set a segmentation node into <code>modelNode</code> variable. As the name suggests, a model node is expected. You can create model nodes from segmentations by exporting segments to model nodes (this creates surface meshes) or by using Segment Mesher extension (this creates volumetric mesh).</p>

---

## Post #6 by @lausiv (2019-12-16 03:19 UTC)

<p>I did mesh from Segment Mesher^^</p>
<p>when i call modelNode.GetMesh()</p>
<blockquote>
<p>cellScalars = modelNode.GetMesh().GetCellData()</p>
</blockquote>
<p>it seemed to be there’s no attribute ‘GetMesh’<br>
or python script can <strong>find</strong> ‘GetMesh’ function</p>

---

## Post #7 by @lassoan (2019-12-16 15:47 UTC)

<p>You can run <code>print(modelNode)</code> in the Python console to see if the object is indeed a model node.</p>

---

## Post #8 by @lausiv (2019-12-17 04:49 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="9459">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>print(modelNode)</p>
</blockquote>
</aside>
<p>I seemed to be real node<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe807c47e18ec3faf1b5ee011f658febc3a7a8ad.png" data-download-href="/uploads/short-url/AjqyuBgSseCgYWb6vUefXBcI4zz.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe807c47e18ec3faf1b5ee011f658febc3a7a8ad.png" alt="image" data-base62-sha1="AjqyuBgSseCgYWb6vUefXBcI4zz" width="690" height="262" data-dominant-color="FAF9F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1186×451 15.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @lassoan (2019-12-19 17:41 UTC)

<p>“modelNode” is a vtkMRMLSegmentationNode, so it is <em>not</em> a model node. Segmentation node is an input to model generators. You can create model nodes from segmentations by exporting segments to model nodes (this creates surface meshes) or by using Segment Mesher extension (this creates volumetric mesh).</p>

---

## Post #10 by @lausiv (2019-12-20 20:39 UTC)

<p>Thanks Adras, I have time so now analysis all of the slicer source code for accumulated and structured knowledges. I think slicer has positive contribution to the medical imaging and communication (like DICOM Concept). Always thinking your slicer community member’s hard working and Voluntary commitment <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
