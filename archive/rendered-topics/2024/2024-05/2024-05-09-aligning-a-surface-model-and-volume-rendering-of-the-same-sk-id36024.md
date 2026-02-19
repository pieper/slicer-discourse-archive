---
topic_id: 36024
title: "Aligning A Surface Model And Volume Rendering Of The Same Sk"
date: 2024-05-09
url: https://discourse.slicer.org/t/36024
---

# Aligning a surface model and volume rendering of the same skull

**Topic ID**: 36024
**Date**: 2024-05-09
**URL**: https://discourse.slicer.org/t/aligning-a-surface-model-and-volume-rendering-of-the-same-skull/36024

---

## Post #1 by @paleomariomm (2024-05-09 12:17 UTC)

<p>Hi community.</p>
<p>I have the DICOM files of a skull and the Surface model (in PLY format) separately.</p>
<p>When I load both into Slicer, and do the volume rendering of the DICOM files, I can see that they are NOT aligned.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2bd485588bc91026f02d402c0eb31bd80af23774.jpeg" data-download-href="/uploads/short-url/6fJR14ZQhUbSGt7HVqg3sDm0HME.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2bd485588bc91026f02d402c0eb31bd80af23774_2_650x500.jpeg" alt="image" data-base62-sha1="6fJR14ZQhUbSGt7HVqg3sDm0HME" width="650" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2bd485588bc91026f02d402c0eb31bd80af23774_2_650x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2bd485588bc91026f02d402c0eb31bd80af23774_2_975x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2bd485588bc91026f02d402c0eb31bd80af23774_2_1300x1000.jpeg 2x" data-dominant-color="BEBFD8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1748×1343 240 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>How can I align/superimpose both (volume rendering and surface model)?</p>
<p>Thanks</p>

---

## Post #2 by @muratmaga (2024-05-09 13:12 UTC)

<aside class="quote no-group" data-username="paleomariomm" data-post="1" data-topic="36024">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/paleomariomm/48/68475_2.png" class="avatar"> paleomariomm:</div>
<blockquote>
<p>do the volume rendering of the DICOM files, I can see that they are NOT aligned.</p>
</blockquote>
</aside>
<p>This seems like RAS vs LPS coordinate issue. What happens when you choose the coordinate system for your 3d Model explicitly during the load.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87a6344d531ce4bc4f28b462a7f28898da91a916.png" data-download-href="/uploads/short-url/jm0y4D3tip3Ve0caTpkfxUVlW2a.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87a6344d531ce4bc4f28b462a7f28898da91a916_2_690x206.png" alt="image" data-base62-sha1="jm0y4D3tip3Ve0caTpkfxUVlW2a" width="690" height="206" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87a6344d531ce4bc4f28b462a7f28898da91a916_2_690x206.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87a6344d531ce4bc4f28b462a7f28898da91a916_2_1035x309.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87a6344d531ce4bc4f28b462a7f28898da91a916_2_1380x412.png 2x" data-dominant-color="EBECED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1468×440 53.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @paleomariomm (2024-05-09 13:33 UTC)

<p>Thats perfect. By changing to RAS the surface model load it was perfectly aligned. Thanks</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e30b4eb9b90c791a6634fbb2e9cdc8379d2ebc56.jpeg" data-download-href="/uploads/short-url/wowBWHpR4bdq8cJ4ua3jfFxjWbI.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e30b4eb9b90c791a6634fbb2e9cdc8379d2ebc56.jpeg" alt="image" data-base62-sha1="wowBWHpR4bdq8cJ4ua3jfFxjWbI" width="690" height="474" data-dominant-color="95969D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1099×756 53.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @muratmaga (2024-05-09 13:47 UTC)

<aside class="quote no-group" data-username="paleomariomm" data-post="3" data-topic="36024">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/paleomariomm/48/68475_2.png" class="avatar"> paleomariomm:</div>
<blockquote>
<p>Thats perfect. By changing to RAS the surface model load it was perfectly aligned. Thanks</p>
</blockquote>
</aside>
<p>Where did you do this segmentation? If this was done in slicer, this shouldn’t have happened.</p>

---

## Post #5 by @paleomariomm (2024-05-09 13:49 UTC)

<p>Yes, I did my segmentation in Slicer. My flow was:</p>
<ol>
<li>Load the skull and segment it entirely.</li>
<li>Export model to PLY format.</li>
<li>Load the DICOM files and do volume rendering.</li>
<li>Load the exported PLY file.</li>
</ol>
<p>Best</p>

---

## Post #6 by @muratmaga (2024-05-09 17:58 UTC)

<aside class="quote no-group" data-username="paleomariomm" data-post="5" data-topic="36024">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/paleomariomm/48/68475_2.png" class="avatar"> paleomariomm:</div>
<blockquote>
<ul>
<li>Load the skull and segment it entirely.</li>
<li>Export model to PLY format.</li>
</ul>
</blockquote>
</aside>
<p>Can you share a one dataset of dicom and segmentaiton. This should not have happened, if you exported from Slicer.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #7 by @bserrano (2024-08-29 12:02 UTC)

<p>Hi all,</p>
<p>I’m facing the same problem. I export a segment as stl using:</p>
<pre><code class="lang-auto">slicer.modules.segmentations.logic().ExportSegmentsClosedSurfaceRepresentationToFiles(saveResults_path,segmentationNode,segmentIDsVTK, 'STL',False,1.0,False)
</code></pre>
<p>Following the documentation (<a href="https://apidocs.slicer.org/master/classvtkSlicerSegmentationsModuleLogic.html" rel="noopener nofollow ugc">link</a>) it should save the geometry in RAS coordinates.</p>
<p>I need to load this geometry in slicer automatically. I tried:</p>
<pre><code class="lang-auto">modelNode = slicer.util.loadModel(path)
</code></pre>
<p>But it seems that it is loading the model in LPS.</p>
<p>When I do it manually and selecting RAS it loads the model correctly.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d3cd71ea3f252f3f9c7f49201b20f235920456e.png" alt="imagen" data-base62-sha1="diOKMmEsK9NzYTdwNWYVq3gRUPY" width="445" height="72"></p>
<p>How can I automate this process?</p>

---
