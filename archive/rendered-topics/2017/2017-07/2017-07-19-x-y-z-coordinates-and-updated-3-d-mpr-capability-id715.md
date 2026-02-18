# X, Y, Z Coordinates and Updated 3-D MPR Capability

**Topic ID**: 715
**Date**: 2017-07-19
**URL**: https://discourse.slicer.org/t/x-y-z-coordinates-and-updated-3-d-mpr-capability/715

---

## Post #1 by @krb01 (2017-07-19 12:23 UTC)

<p>I read through the wiki pages, but I still had a few unanswered questions.<br>
First, is there a way to indicate the x, y, z-axis coordinates when freely moving the cursor around the DICOM image. This feature is available in OsiriX.<br>
Secondly, is there a feature that allows updated 3-D MPR ability similarly to Osirix? There is a curved MPR view in 3-D slicer, but when one orientation is adjusted, the other two are are stagnant</p>

---

## Post #2 by @lassoan (2017-07-19 12:54 UTC)

<aside class="quote no-group" data-username="krb01" data-post="1" data-topic="715">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/9d8465/48.png" class="avatar"> krb01:</div>
<blockquote>
<p>is there a way to indicate the x, y, z-axis coordinates when freely moving the cursor around the DICOM image</p>
</blockquote>
</aside>
<p>It is shown in the DataProbe widget, in the bottom-left when the mouse pointer is over the image.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/7c47977d4ccda9009c266f5ebf4a0044f88c0819.png" data-download-href="/uploads/short-url/hJqADFsHtCr2yRxL12SqNAIBsGB.png?dl=1" title="image.png"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/7c47977d4ccda9009c266f5ebf4a0044f88c0819_2_690x469.png" width="690" height="469" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/7c47977d4ccda9009c266f5ebf4a0044f88c0819_2_690x469.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/7c47977d4ccda9009c266f5ebf4a0044f88c0819_2_1035x703.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/7c47977d4ccda9009c266f5ebf4a0044f88c0819_2_1380x938.png 2x" data-dominant-color="9A999E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">1732×1178 471 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote no-group" data-username="krb01" data-post="1" data-topic="715">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/9d8465/48.png" class="avatar"> krb01:</div>
<blockquote>
<p>is there a feature that allows updated 3-D MPR</p>
</blockquote>
</aside>
<p>There are many ways how to set up MPR slice orientation, one of them is using <code>Reformat</code> module. Let us know if you need different ways to set up your views.</p>

---

## Post #3 by @ghnguyen (2019-01-15 19:38 UTC)

<p>Hello,</p>
<p>Sorry to bump up an old thread but I was trying to look up answers for some coordinate questions as well.<br>
I have a 3D Mesh and when I click on a point on the Slice View (say Axial orientation for example), I’d like to pinpoint the exact point/cell in the mesh and get the point/cell data. In order to do so, I have tried using vtkDataSet::FindPoint(double x, doubly y, double z). My question is which values should I pass to these parameters? Or is there a better way of doing this that I have not known? I was using global xyz obtained from crosshair (GetCursorPositionXYZ) but it does not seem correct since the z-value for all Axial, Sagittal and Coronal are always 0.</p>
<p>Thanks!</p>

---

## Post #4 by @danpak94 (2019-01-15 21:23 UTC)

<p>Is there a way to enable adjustment of plane angles for MPR using crosshairs as in Radiant dicom viewer? It helps a lot with orienting myself within the image slices, but unfortunately I could not find such a feature on the Reformat module.</p>
<p>Thank you for your help.</p>

---

## Post #5 by @pieper (2019-01-15 21:40 UTC)

<p><a class="mention" href="/u/ghnguyen">@ghnguyen</a>: You may want to also look at vtkCellLocator to find the cell id and points.</p>
<p>For the point, you can use something like this:</p>
<pre><code class="lang-auto">slicer.mrmlScene.GetNodesByClass('vtkMRMLCrosshairNode').GetItemAsObject(0).GetCrosshairRAS()
</code></pre>
<p>it will update as you hold down shift and move the mouse in the 2D/3D views.</p>

---

## Post #6 by @ghnguyen (2019-01-15 21:52 UTC)

<p>Hi Steve,</p>
<p>I did try using an observer on the crosshair similar to your suggestion. For the vtkCellLocator, we would still need the xyz coordinates of the point right? So my original question would be do I use the CrosshairRAS or the CrosshairXYZ there? It does seem like the RAS would be the “global” coordinates here. Sorry I am confused by the wording of the documentation and need some confirmation.</p>

---

## Post #7 by @pieper (2019-01-15 22:08 UTC)

<p>Right, if you are looking for the closest cell/point in the vtkPolyData you get from a model node, then you want to use RAS (see <a href="https://www.slicer.org/wiki/Coordinate_systems" rel="nofollow noopener">https://www.slicer.org/wiki/Coordinate_systems</a>).</p>
<p>The other thing to keep in mind is that models can be transformed, so you need to handle that case you would need to transform the crosshair position through the model’s transforms first (let us know if you need pointers on that).</p>

---

## Post #8 by @ghnguyen (2019-01-16 16:26 UTC)

<p>Huge thanks Steve. As for transforms, I do have my mesh transformed at module startup (I am making a custom module), so do I need to transform the crosshair node too? It seems the slice widget can still catch the mesh and shows the slice. Are you saying the coordinates might be wrong or what should I be careful about?</p>

---

## Post #9 by @pieper (2019-01-16 18:04 UTC)

<p>Yes, if you have a transform you should be sure to take that into account.  The easiest would be to harden the model so that all the vertices of the polydata are in RAS space. The other, more general, option is to apply the inverse transform to the RAS coordinate of the crosshair so that it’s moved into the local space of the model.  You can use <a href="http://apidocs.slicer.org/master/classvtkMRMLTransformableNode.html" rel="nofollow noopener">TransformPointFromWorld</a> for this.</p>

---
