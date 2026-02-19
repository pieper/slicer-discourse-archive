---
topic_id: 27783
title: "How Can We Separate The Islands Of A Polydata Plane"
date: 2023-02-12
url: https://discourse.slicer.org/t/27783
---

# How can we separate the islands of a polydata plane?

**Topic ID**: 27783
**Date**: 2023-02-12
**URL**: https://discourse.slicer.org/t/how-can-we-separate-the-islands-of-a-polydata-plane/27783

---

## Post #1 by @chir.set (2023-02-12 18:41 UTC)

<p>The picture below show a model of a polydata obtained with vtkCutter. There are 2 islands, the blue one should be discarded, and the other perforated one enclosing a reference point (F1) should be kept as it is. After many hours, I could not find a way to do that. Please advise on a reliable method. Thanks.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/3561c9d0b89354980daa7222ccbc9c0549e9a2c9.png" data-download-href="/uploads/short-url/7CeOCA1Co8fV1l6iA2tCQN6YMYx.png?dl=1" title="SplitDisjointPolyData" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/3561c9d0b89354980daa7222ccbc9c0549e9a2c9_2_345x500.png" alt="SplitDisjointPolyData" data-base62-sha1="7CeOCA1Co8fV1l6iA2tCQN6YMYx" width="345" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/3561c9d0b89354980daa7222ccbc9c0549e9a2c9_2_345x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/3561c9d0b89354980daa7222ccbc9c0549e9a2c9.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/3561c9d0b89354980daa7222ccbc9c0549e9a2c9.png 2x" data-dominant-color="111015"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SplitDisjointPolyData</span><span class="informations">474×685 23.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @mau_igna_06 (2023-02-12 19:11 UTC)

<p>Hi</p>
<p>Please check this out:<br>
<a href="https://vtk.org/doc/nightly/html/classvtkPolyDataConnectivityFilter.html#aa131a463004257e3a7d665958441444e" class="onebox" target="_blank" rel="noopener nofollow ugc">https://vtk.org/doc/nightly/html/classvtkPolyDataConnectivityFilter.html#aa131a463004257e3a7d665958441444e</a></p>
<p>Hope it helps</p>

---

## Post #3 by @chir.set (2023-02-12 20:01 UTC)

<p>Thanks for your input.</p>
<p>Actually, the polydata used to add the model is obtained from vtkConnectivityFilter using SetExtractionModeToAllRegions. I tried again with vtkPolyDataConnectivityFilter and did not find much difference. With SetExtractionModeToSpecifiedRegions, I can extract any individual region separately. Each region is then a closed polydata, completely filled. The holes are then no longer holes.</p>
<p>I need the one enclosing F-1 with the holes, and any region not enclosing F-1 and the holes should be discarded. With SetExtractionModeToClosestPointRegion, it would sometimes extract a single hole, the opposite of what I need.</p>
<p>The problem would be to determine which one encloses F-1 and the holes; it remains the same headache with vtkFeatureEdges as below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a40ac947b1f9148211f2b1519b595c4e4ca00646.png" data-download-href="/uploads/short-url/npbpHFYm5P7fIauubvyWbL3NqGG.png?dl=1" title="FeatureEdges" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a40ac947b1f9148211f2b1519b595c4e4ca00646_2_328x500.png" alt="FeatureEdges" data-base62-sha1="npbpHFYm5P7fIauubvyWbL3NqGG" width="328" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a40ac947b1f9148211f2b1519b595c4e4ca00646_2_328x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a40ac947b1f9148211f2b1519b595c4e4ca00646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a40ac947b1f9148211f2b1519b595c4e4ca00646.png 2x" data-dominant-color="030202"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">FeatureEdges</span><span class="informations">450×685 10.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>N.B. : F-1 is co-planar to the polydata, F-2 is not.</p>

---

## Post #4 by @mau_igna_06 (2023-02-12 20:10 UTC)

<p>If you have a seed point (i.e. a markups fiducial) you can use the Dynamic Modeler SelectByPoints tool on your first post polydata to keep the colorful island</p>

---
