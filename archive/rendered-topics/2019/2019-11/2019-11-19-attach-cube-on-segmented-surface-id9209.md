---
topic_id: 9209
title: "Attach Cube On Segmented Surface"
date: 2019-11-19
url: https://discourse.slicer.org/t/9209
---

# Attach cube on segmented surface

**Topic ID**: 9209
**Date**: 2019-11-19
**URL**: https://discourse.slicer.org/t/attach-cube-on-segmented-surface/9209

---

## Post #1 by @lausiv (2019-11-19 05:08 UTC)

<p>Is there any editing tools like “Fill between slices”</p>
<p>I want to attach cube(below pupple colored cube) on the surface(it means segmented region on the slice)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e83c6ccb3c07e8e2449f074772a8979dc320e1de.jpeg" data-download-href="/uploads/short-url/x8serSlMXIsGymCeeXyD3EKGc7I.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e83c6ccb3c07e8e2449f074772a8979dc320e1de_2_674x500.jpeg" alt="image" data-base62-sha1="x8serSlMXIsGymCeeXyD3EKGc7I" width="674" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e83c6ccb3c07e8e2449f074772a8979dc320e1de_2_674x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e83c6ccb3c07e8e2449f074772a8979dc320e1de.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e83c6ccb3c07e8e2449f074772a8979dc320e1de.jpeg 2x" data-dominant-color="D6D6D8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">699×518 71.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2019-11-20 05:20 UTC)

<aside class="quote no-group" data-username="lausiv" data-post="1" data-topic="9209">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lausiv/48/4984_2.png" class="avatar"> lausiv:</div>
<blockquote>
<p>Is there any editing tools like “Fill between slices”</p>
</blockquote>
</aside>
<p>There is an effect called “Fill between slices” in Segment Editor module.</p>
<aside class="quote no-group" data-username="lausiv" data-post="1" data-topic="9209">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lausiv/48/4984_2.png" class="avatar"> lausiv:</div>
<blockquote>
<p>I want to attach cube(below pupple colored cube) on the surface</p>
</blockquote>
</aside>
<p>Would you like to 3D print a template that fits on the segmented surface? You can do that by the following steps:</p>
<ul>
<li>Add a new segment</li>
<li>Select Scissors effect, set “Operation” to “Fill inside”, “Shape” to “Rectangle”, and “Editable area” to “Outside all segments”, then draw the rectangle in 3D view</li>
<li>You can use Islands effect’s “Keep selected island” method to keep only that part of the cube that sits on the surface</li>
</ul>

---

## Post #3 by @lausiv (2019-11-20 15:53 UTC)

<p>Thank you. i will do that <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"><br>
i think 3d slicer is  very powerful tool as i think.<br>
3d image processing is very interesting for me<br>
i m in flow in that field. i love it. i am enthusiast!</p>

---

## Post #4 by @lausiv (2019-12-25 07:22 UTC)

<p>So, I am now automate below behavior using python script.<br>
but, python scrip for effect of hollow and scissors by fiducial was not found</p>
<h1><a name="p-33712-behavior-1" class="anchor" href="#p-33712-behavior-1" aria-label="Heading link"></a>behavior</h1>
<p>after generating mesh,</p>
<ol>
<li>new segment  &lt;== it is ok</li>
<li>threshold-smooth  &lt;== ok</li>
<li>markup by fiducial &lt;== ok<br>
<strong>4. hollow effect &lt;== not found</strong><br>
<strong>5. scissors effect using markup &lt;== c++ code founded but python not found</strong></li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b760a97ae64ac7715689edd5335cb526b923b5d5.png" data-download-href="/uploads/short-url/qaetq85gpsrBVDa6W8jxz0dLaxn.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b760a97ae64ac7715689edd5335cb526b923b5d5_2_281x500.png" alt="image" data-base62-sha1="qaetq85gpsrBVDa6W8jxz0dLaxn" width="281" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b760a97ae64ac7715689edd5335cb526b923b5d5_2_281x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b760a97ae64ac7715689edd5335cb526b923b5d5_2_421x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b760a97ae64ac7715689edd5335cb526b923b5d5_2_562x1000.png 2x" data-dominant-color="1D2D3B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1082×1920 259 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/1605f3c24b56ccbf2a3d1f01499b81811c6b5bef.png" data-download-href="/uploads/short-url/38PfVj8Gu7ntBBPsuA1mWhmN2jl.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/1605f3c24b56ccbf2a3d1f01499b81811c6b5bef.png" alt="image" data-base62-sha1="38PfVj8Gu7ntBBPsuA1mWhmN2jl" width="690" height="409" data-dominant-color="F7F6FB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1236×733 23.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b198167dcbed32fe9a6cbb5f255b615605b0f23.jpeg" data-download-href="/uploads/short-url/hyZnc98hTUz3rKbmT5QutEqu3Wr.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7b198167dcbed32fe9a6cbb5f255b615605b0f23_2_676x500.jpeg" alt="image" data-base62-sha1="hyZnc98hTUz3rKbmT5QutEqu3Wr" width="676" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7b198167dcbed32fe9a6cbb5f255b615605b0f23_2_676x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b198167dcbed32fe9a6cbb5f255b615605b0f23.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b198167dcbed32fe9a6cbb5f255b615605b0f23.jpeg 2x" data-dominant-color="787B63"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">943×697 187 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2019-12-26 23:34 UTC)

<p>Scissors effect is developed for interactive use. If you want to place a box on a surface from a script then it is probably much easier to create a box-shaped model node from output of a vtkCurbeSource, then set its pose using a transform node (set translation based on a markups fiducial point position, set orientation by getting the surface normal at the fiducial point), then import the model into a segment in the segmentation node (using <code>segmentationNode.AddSegmentFromClosedSurfaceRepresentation</code>).</p>

---

## Post #6 by @lausiv (2020-01-10 04:27 UTC)

<p>From your advise, i did 1 box but now extend 9 boxes.<br>
If python script is completed well, let it share this page.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/acdcd1bb14c36ab931e0e79c7fbef0fc056c2150.png" data-download-href="/uploads/short-url/oFde8rcq7Gwj39se1K8DBHWWgk8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/acdcd1bb14c36ab931e0e79c7fbef0fc056c2150_2_689x500.png" alt="image" data-base62-sha1="oFde8rcq7Gwj39se1K8DBHWWgk8" width="689" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/acdcd1bb14c36ab931e0e79c7fbef0fc056c2150_2_689x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/acdcd1bb14c36ab931e0e79c7fbef0fc056c2150.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/acdcd1bb14c36ab931e0e79c7fbef0fc056c2150.png 2x" data-dominant-color="8893AF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">968×702 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac75a58285165de6ef12fbc685db7ddb16789272.jpeg" data-download-href="/uploads/short-url/oBEbfpPqwnvkK7LVJvhXJ8kpU9I.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ac75a58285165de6ef12fbc685db7ddb16789272_2_689x500.jpeg" alt="image" data-base62-sha1="oBEbfpPqwnvkK7LVJvhXJ8kpU9I" width="689" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ac75a58285165de6ef12fbc685db7ddb16789272_2_689x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac75a58285165de6ef12fbc685db7ddb16789272.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac75a58285165de6ef12fbc685db7ddb16789272.jpeg 2x" data-dominant-color="8893AE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">968×702 147 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @lassoan (2020-01-16 21:07 UTC)

<p>You can apply a transform by setting the parent transform node (<code>SetAndObserveTransformNodeID</code>). See in example in <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Transforms#Examples">Transforms module documentation</a>.</p>

---

## Post #12 by @lausiv (2020-01-20 04:18 UTC)

<p>purpose : I make 9 segmentation pads for generating mesh with the brain skin.</p>
<p>I successfully transformed the pad(cylinder object) on the surface of skin by transform module. and i make segmentation node each pad. but like below picture. when i merge segments to one Segementation Node To Send Segment Mesher, but the transformed setting(Rotation,Trans) is disappeard, in other words, my pad object go to (0,0,0) coordinates. I think this is small bug.</p>
<p>Or, Is there any suggestion for generating mesh with <strong>multiple Segementation Nodes</strong>?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca78e6957ce88d0263b8b071163fe06211b77ca6.jpeg" data-download-href="/uploads/short-url/sT9tBZwxIMocq57ldKAyYVPycD4.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ca78e6957ce88d0263b8b071163fe06211b77ca6_2_439x500.jpeg" alt="image" data-base62-sha1="sT9tBZwxIMocq57ldKAyYVPycD4" width="439" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ca78e6957ce88d0263b8b071163fe06211b77ca6_2_439x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ca78e6957ce88d0263b8b071163fe06211b77ca6_2_658x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ca78e6957ce88d0263b8b071163fe06211b77ca6_2_878x1000.jpeg 2x" data-dominant-color="576564"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1046×1191 277 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27c2156e0dd0e46d54b992c3690d507a0c6b2223.png" alt="image" data-base62-sha1="5FIrvT6nt9idWkL2aIiEQM09sVJ" width="625" height="161"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/634f5677ebbc5b2eceb0f8d76fd86e9ddda0a0c9.png" alt="image" data-base62-sha1="eaxfuPLrlKRRf1lygQ6UvQoKSzD" width="634" height="222"><br>
![image|634x222](upload:/<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0a072d8c6e7b5655e105eeef1c5cbf8040ffb74.png" alt="image" data-base62-sha1="w38IcDiNNm3WLzED8J53cRnyJuY" width="634" height="222"></p>

---

## Post #13 by @lausiv (2020-01-20 05:53 UTC)

<p>I make 9 cylinder object, -&gt; transform node -&gt; segmentation node</p>
<pre><code>cylSource = vtk.vtkCylinderSource()
cylSource.SetRadius(10)
cylSource.SetResolution(50)
cylSource.SetHeight(10)
cylSource.SetCenter([0,0,0])
cylSource.Update()

transform = vtk.vtkTransform()
applyTransform = vtk.vtkTransformPolyDataFilter()
applyTransform.SetTransform(transform)
applyTransform.SetInputConnection(cylSource.GetOutputPort())
applyTransform.Update()

nOfPad = 9
for i in range(0,nOfPad):
    transformlNode = slicer.mrmlScene.AddNode(slicer.vtkMRMLTransformNode())
    segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
    segmentationNode.AddSegmentFromClosedSurfaceRepresentation(cylSource.GetOutput(), "Pad", [1.0,0.0,0.0])</code></pre>

---

## Post #14 by @lassoan (2020-01-20 08:58 UTC)

<p><code>applyTransform</code> is a filter (you chose a somewhat misleading name). You need to add the <em>output</em> of that filter to the segmentation: <code>segmentationNode.AddSegmentFromClosedSurfaceRepresentation(applyTransform.GetOutput()) </code></p>

---

## Post #15 by @lausiv (2020-01-20 09:31 UTC)

<p>Thank you Lasso^^ Aha <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"> <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #17 by @lassoan (2020-01-20 16:50 UTC)

<p>You should not add new segmentation node for each pad. Instead, create a single segmentation node and add all the pads to that.</p>

---

## Post #19 by @lausiv (2020-01-20 21:38 UTC)

<p>but i don not set Rotation on Matrix ^^ . I want to know the fomular or <strong>python function t</strong>o set Matrix from Rx,Ry,Rz</p>
<p>in other words, i want to access python script function for setting below UI Rotation&amp;Translation Value on transformation module, so i can get the transform matrix using</p>
<p><code>transformNode.SetMatrixTransformToParent(transformMatrix)</code></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2af324b2863b298f16d024da13b9b31d84df5817.png" data-download-href="/uploads/short-url/67WZ873aquo0uDlxY2JsEcFOj1d.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2af324b2863b298f16d024da13b9b31d84df5817.png" alt="image" data-base62-sha1="67WZ873aquo0uDlxY2JsEcFOj1d" width="690" height="213" data-dominant-color="EDF2F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">982×304 10.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #20 by @lassoan (2020-01-20 22:21 UTC)

<aside class="quote no-group quote-post-not-found" data-username="lausiv" data-post="18" data-topic="9209">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lausiv/48/4984_2.png" class="avatar"> lausiv:</div>
<blockquote>
<p>You should not add new segmentation node for each pad. Instead, create a single segmentation node and add all the pads to that.<br>
==&gt; Yes. But this case, can i transform for each pad(segmentation) on the Transforms Module?</p>
</blockquote>
</aside>
<p>Yes, you can. The transformation that was applied to the model at the time of import will be preserved in the imported segment.</p>

---
