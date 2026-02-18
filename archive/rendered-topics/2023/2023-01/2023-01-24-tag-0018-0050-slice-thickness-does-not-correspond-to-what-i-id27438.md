# Tag (0018,0050) Slice Thickness does not correspond to what I calculate in the image

**Topic ID**: 27438
**Date**: 2023-01-24
**URL**: https://discourse.slicer.org/t/tag-0018-0050-slice-thickness-does-not-correspond-to-what-i-calculate-in-the-image/27438

---

## Post #1 by @francesca_flore (2023-01-24 12:03 UTC)

<p>In the two sagittal slices it can be seen that the difference between one slice and the other is 6.5mm, unlike 5mm as reported in the Tag (0018,0050) Slice Thickness. How is this possible? Which should I consider correct?<br>
Thanks!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed4e6c87006d512eede825ee487d8e0fe40ff061.jpeg" data-download-href="/uploads/short-url/xRjblsxykXWS4n9mvmbY39wWN7r.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed4e6c87006d512eede825ee487d8e0fe40ff061_2_690x272.jpeg" alt="image" data-base62-sha1="xRjblsxykXWS4n9mvmbY39wWN7r" width="690" height="272" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed4e6c87006d512eede825ee487d8e0fe40ff061_2_690x272.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed4e6c87006d512eede825ee487d8e0fe40ff061_2_1035x408.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed4e6c87006d512eede825ee487d8e0fe40ff061.jpeg 2x" data-dominant-color="787876"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1104×436 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b8c2179829596fd739f0d763497da5556eebb4e.png" alt="image" data-base62-sha1="flpjINUAAIznGhm1sYXwlwqxalU" width="233" height="21"></p>

---

## Post #2 by @lassoan (2023-01-25 12:49 UTC)

<p><code>Slice Thickness</code> tag does not give any information on where slices are, it just provides some approximate measure of how much the image is focused on the slice plane.</p>
<p>If you want to know distance between neighbor slices then ignore the <code>Slice Thickness</code> tag and use the content of <code>Image Position Patient</code> and <code>Image Orientation Patient</code> tags.</p>

---

## Post #3 by @francesca_flore (2023-01-25 14:15 UTC)

<p>Thanks to reply Andras. But how can I know the distance between slices starting from just this two tags? I probably need where is the origin position? Is there a tag for this?</p>

---

## Post #4 by @cpinter (2023-01-25 15:24 UTC)

<p>You have a different <code>Image Position Patient</code> value for each instance (i.e. slice).</p>
<p>Here is an example where spacing is calculated, it may help: <a href="https://github.com/SlicerRt/SlicerRT/blob/master/DicomRtImportExport/Logic/vtkSlicerDicomRtImportExportModuleLogic.cxx#L2152-L2184" class="inline-onebox">SlicerRT/vtkSlicerDicomRtImportExportModuleLogic.cxx at master · SlicerRt/SlicerRT · GitHub</a></p>

---

## Post #5 by @lassoan (2023-01-25 20:26 UTC)

<aside class="quote no-group" data-username="francesca_flore" data-post="3" data-topic="27438">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/francesca_flore/48/15307_2.png" class="avatar"> francesca_flore:</div>
<blockquote>
<p>But how can I know the distance between slices starting from just this two tags?</p>
</blockquote>
</aside>
<p>In general, distance between slices cannot be computed because distance between slices may not be equal for each neighboring slices. Slices may not even be parallel, so computing distance between neighbor slices may not be feasible, as you cannot even specify what you mean by neighbor of a slice. Sometimes there are groups of slices in a series that are parallel, with neighbor slices being at equal distances. In some images, you may also find many slices at the same position, and you need to have a look at some other DICOM tags to tell them apart (e.g., they are acquired at a different time, flip angle, cardiac cycle, …). The DICOM standard does not even attempt to specify distance between slices. It is up to each application to deal with this mess.</p>
<p>Most 3D imaging software make assumptions (e.g., all slices are parallel, equal distance from the neighbors, slice normal is parallel to increment vector between slices) and while checking if these assumptions are correct, the constant distance between neighbors is computed as a side product. If no constant distance is found then most software rejects loading the image as a 3D volume.</p>
<p>Slicer’s DICOM importer can load sequences of arbitrarily oriented slices with automatic grouping based on dozens of possible tags, and reconstruct a 3D or 4D Cartesian volume with uniform spacing along each axis. If you need to deal with a wide range of images then I would recommend to let Slicer reconstruct the image for you and use the spacing of this reconstructed image.</p>

---
