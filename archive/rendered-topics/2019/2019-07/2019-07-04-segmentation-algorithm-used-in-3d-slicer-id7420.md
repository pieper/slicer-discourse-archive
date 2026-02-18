# Segmentation algorithm used in 3D Slicer

**Topic ID**: 7420
**Date**: 2019-07-04
**URL**: https://discourse.slicer.org/t/segmentation-algorithm-used-in-3d-slicer/7420

---

## Post #1 by @sara04 (2019-07-04 18:11 UTC)

<p>Hi,</p>
<p>I’m using 3D Slicer for tooth segmentation and I’ve created an  stl model from ct scan (DICOM).<br>
I’ve done that using Segment editor module.</p>
<p>Can someone tell me which segmentation algorithm is used in slicer to create an stl model from ct scan?</p>

---

## Post #2 by @cpinter (2019-07-04 18:26 UTC)

<aside class="quote no-group" data-username="sara04" data-post="1" data-topic="7420">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/6de8d8/48.png" class="avatar"> sara04:</div>
<blockquote>
<p>I’ve created an stl model from ct scan (DICOM)</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="sara04" data-post="1" data-topic="7420">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/6de8d8/48.png" class="avatar"> sara04:</div>
<blockquote>
<p>which segmentation algorithm is used in slicer to create an stl model from ct scan</p>
</blockquote>
</aside>
<p>I don’t understand the question. You said you did all that. Am I misunderstanding something?</p>

---

## Post #3 by @lassoan (2019-07-04 19:53 UTC)

<p>If you mean which algorithms are used for generating closed surface from binary labelmap representation of the segmentation: see implementation <a href="https://github.com/Slicer/Slicer/blob/master/Libs/vtkSegmentationCore/vtkBinaryLabelmapToClosedSurfaceConversionRule.cxx" rel="nofollow noopener">here</a>. In short: <a href="https://vtk.org/doc/nightly/html/classvtkDiscreteFlyingEdges3D.html" rel="nofollow noopener">vtkDiscreteFlyingEdges3D</a> followed by <a href="https://vtk.org/doc/nightly/html/classvtkWindowedSincPolyDataFilter.html" rel="nofollow noopener">vtkWindowedSincPolyDataFilter</a>, <a href="https://www.vtk.org/doc/nightly/html/classvtkDecimatePro.html" rel="nofollow noopener">vtkDecimatePro</a> (optional), and <a href="https://www.vtk.org/doc/nightly/html/classvtkPolyDataNormals.html" rel="nofollow noopener">vtkPolyDataNormals</a>.</p>

---

## Post #4 by @sara04 (2019-07-05 10:38 UTC)

<p>I need to write some theory about image segmentation and the things I’ve done in 3D Slicer. Since I used thresholding, I wanted to know the names of algorithms you used in implementation ( eg. k-means clustering).<br>
I’m a student and new to this so I don’t understand this very well. It will be very helpfull if you could give me the names of some algorithms you used.  Hope you understand what I’m trying to say.</p>

---

## Post #5 by @sara04 (2019-07-05 10:40 UTC)

<p>Thank you  <a class="mention" href="/u/lassoan">@lassoan</a> , I think you get my point. So, you used marching cubes algorithm and flying edges? I need to write something about this algorithms and I really want to write about algorithms that are implemented in slicer.</p>

---

## Post #6 by @lassoan (2019-07-05 12:19 UTC)

<p>We did not use matching cubes. We used flying edges algorithm instead because it is faster. You can find description of the methods at the associated links.</p>

---

## Post #7 by @cpinter (2019-07-05 13:02 UTC)

<p>I see, thanks! Andras gave you the details, but if you’re looking for some text, then I can send you my PhD thesis in which these are described in detail (it will be publicly accessible in a few weeks but I can send you an unofficial copy).</p>

---

## Post #8 by @sara04 (2019-07-05 17:49 UTC)

<p>Thank you, that was really helpful!</p>

---

## Post #9 by @sara04 (2019-08-30 19:55 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/cpinter">@cpinter</a><br>
Hi, I have another problem. I have done tooth segmentation and I extracted two stl files, tooth crown and root .<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef575454cd4154c07742f8f3f6ce499f8e9572be.png" alt="image" data-base62-sha1="y9jdvqQfBvElQam7pEXFEqIUhC6" width="175" height="378"></p>
<p>My question is… Is it possible to do an automatic segmentation of the contact surface between two volumes in contact (crown and root ) that were themselves constructed by segment editor? It is needed to impose the boundary conditions so as to treat two volumes as two bodies in contact.</p>

---

## Post #10 by @lassoan (2019-08-30 20:18 UTC)

<p>You can export segments to models and then use “Model to model distance” extensions to compute distance between them. You can visualize the distance using color mapping or set a threshold value to show only parts that are closer to each other than the chosen threshold value (in Models module / Display / Scalars section).</p>

---

## Post #11 by @sara04 (2019-08-31 13:51 UTC)

<p>I got this<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c228cf672c13f58d619ba394d2ef73f0b7da9f87.png" data-download-href="/uploads/short-url/rHC40vDxWUeE0YSkj5EEelagEN9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c228cf672c13f58d619ba394d2ef73f0b7da9f87_2_557x500.png" alt="image" data-base62-sha1="rHC40vDxWUeE0YSkj5EEelagEN9" width="557" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c228cf672c13f58d619ba394d2ef73f0b7da9f87_2_557x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c228cf672c13f58d619ba394d2ef73f0b7da9f87.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c228cf672c13f58d619ba394d2ef73f0b7da9f87.png 2x" data-dominant-color="737DA2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">560×502 85.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and then i set a threshold value to get this<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e15a1a241fe6025d62e9b76a9d63a3fcb4c245a.png" alt="image" data-base62-sha1="4i8Fu9OP4u3mN4irnIilk7cwzea" width="399" height="282"></p>
<p>Is it possible to save this last surface as stl file?<br>
I tried to save it but when I load it, i got the whole crown (first picture), not the surface I wanted.</p>

---

## Post #12 by @lassoan (2019-09-01 02:50 UTC)

<p>Adjusting display options in Models module does not alter the model’s geometry, just modifies display settings. You can create a new model node from the displayed thresholded model by copy-pasting this line into the Python console:</p>
<pre><code class="lang-python">slicer.modules.models.logic().AddModel(getNode('sphere').GetDisplayNode().GetOutputMeshConnection())
</code></pre>
<p>If you just need a list of point IDs where the distance is smaller than a threshold (for example, 0.5) then you can get it by a few lines of Python code:</p>
<pre><code class="lang-python">import numpy as np
distances = slicer.util.arrayFromModelPointData(getNode('sphere'), 'Signed')
pointIDs = np.where(distances &lt; 0.5)
</code></pre>
<p>(replace <code>sphere</code> by the actual name of the model node; and <code>Signed</code> by the actual name of the distance array)</p>

---

## Post #13 by @sara04 (2019-09-01 11:27 UTC)

<p>Thank you for your help. I created a new model and it’s fine now, but I can’t get a list of point IDs.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0bed5472d1e567dd1c7a8a9ff5eb40d6d0d31cc.png" alt="image" data-base62-sha1="w4bOjcY5HDZgpLcyq0nxPmwQgji" width="629" height="100"></p>

---

## Post #14 by @lassoan (2019-09-01 14:08 UTC)

<p>There was a typo in the sample script above (distanceValues &lt;-&gt; distances), I’ve updated it now.</p>

---

## Post #15 by @lassoan (2023-06-24 14:12 UTC)

<p>A post was split to a new topic: <a href="/t/segmentation-and-feature-extraction-of-brain-tumors/30209">Segmentation and feature extraction of brain tumors</a></p>

---
