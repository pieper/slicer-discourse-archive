---
topic_id: 10201
title: "Put Vtkimagedata On Red Yellow Green View"
date: 2020-02-11
url: https://discourse.slicer.org/t/10201
---

# Put vtkImageData on Red Yellow Green view

**Topic ID**: 10201
**Date**: 2020-02-11
**URL**: https://discourse.slicer.org/t/put-vtkimagedata-on-red-yellow-green-view/10201

---

## Post #1 by @CreepyTrick (2020-02-11 14:02 UTC)

<p>Hello</p>
<p>I want to put an vtkImageData on the RGY view….<br>
I already initialized my image data like this:</p>
<pre><code class="lang-auto">	img-&gt;SetExtent(….)
	img-&gt;AllocateScalars(VTK_DOUBLE, 1);
	for (….)
	{
		for (….)
		{
			img-&gt;SetScalarComponentFromDouble( …...);
		}
	}
</code></pre>
<p>It give me (let’s suppose ….) an orange square in a test renderView.<br>
I want that orange square to be on a certain position on the red view in Slicer, like this (photoshoped result):<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddec91da028fa0b85bd183b6febdf86ca35051b8.jpeg" alt="squareXRed" data-base62-sha1="vFemTwM5ugmSffivlFve0UPprN6" width="255" height="360"></p>
<p>So i face two problems …<br>
Get the redView and manipulate it<br>
A correct way to set bounds…</p>
<p>My current result:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f6a78c2b34ecf7c8cb99b49d516a6234ae121ef.png" data-download-href="/uploads/short-url/ibaKHU3ZMTM7M30Ij0U2Niykz7N.png?dl=1" title="CaptureIHAVE" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f6a78c2b34ecf7c8cb99b49d516a6234ae121ef_2_323x500.png" alt="CaptureIHAVE" data-base62-sha1="ibaKHU3ZMTM7M30Ij0U2Niykz7N" width="323" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f6a78c2b34ecf7c8cb99b49d516a6234ae121ef_2_323x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f6a78c2b34ecf7c8cb99b49d516a6234ae121ef.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f6a78c2b34ecf7c8cb99b49d516a6234ae121ef.png 2x" data-dominant-color="190F04"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">CaptureIHAVE</span><span class="informations">461×713 17.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
(Not really beautiful…)</p>
<p>I reach that point with that code:</p>
<pre><code class="lang-auto">qSlicerLayoutManager* layoutManager = qSlicerApplication::application()-&gt;layoutManager();

vtkRenderWindowInteractor*  interactor  = layoutManager-&gt;sliceWidget("Red")-&gt;sliceView()-&gt;interactor();
vtkRendererCollection *rendererCollection= interactor-&gt;GetRenderWindow()-&gt;GetRenderers();

//ImageActor is my vtkImageData red square
rendererCollection-&gt;GetFirstRenderer()-&gt;AddActor(imageActor);
</code></pre>
<p>Any ideas ?</p>

---
