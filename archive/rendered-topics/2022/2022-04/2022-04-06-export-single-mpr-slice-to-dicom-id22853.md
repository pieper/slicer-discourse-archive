# Export single MPR slice to DICOM

**Topic ID**: 22853
**Date**: 2022-04-06
**URL**: https://discourse.slicer.org/t/export-single-mpr-slice-to-dicom/22853

---

## Post #1 by @mikebind (2022-04-06 21:54 UTC)

<p>I have a CT volume that I have navigated and manipulated so that the Red slice view shows a slice plane that I would like to export to a single DICOM image (so that collaborators can make measurements with their non-Slicer software to compare with measurements made within Slicer).  I know that I can capture a PNG of what is shown in the Red slice using Screen Capture, but I need an output which retains the pixel spacing information (resampling to whatever resolution the slice view is using is fine, I just want area measurements to be in meaningful physical units).  Any suggestions about how to accomplish this?</p>

---

## Post #2 by @mikebind (2022-04-06 22:21 UTC)

<p>I see this in the script repository:  <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-a-volume-to-dicom-file-format" class="inline-onebox">Script repository — 3D Slicer documentation</a></p>
<p>So, I think that I can perhaps use Screen Capture to get the image as PNG, then read the PNG into a numpy array, create a scalar volume with the image as that numpy array and a pixel resolution based on data extracted from the slice view.  Then apply a parent patient and study in the subject hierarchy and export to DICOM.</p>
<p>Does this approach sound like it would work?  The part I am least sure of accomplishing is getting the pixel size of the screen capture PNG from the slice view.  Is this possible?  How?<br>
Thanks for any help you can provide.</p>

---

## Post #3 by @pieper (2022-04-06 22:38 UTC)

<p>Maybe the easiest would be to convert the slice plane orientation to a transform and then resample the volume through the transform and export the result as dicom.  You’d also need to figure out which dicom slice corresponds to the slice view, but you can do that by iterating through the positions and orientations in the exported dicoms.  You may need to adjust the translation of the the resampling transform so the slice of interest is in the exact same plane as the red slice view so your measurement won’t be biased.</p>

---

## Post #4 by @mikebind (2022-04-06 23:15 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a>, I’ll give this a try.</p>

---

## Post #5 by @lassoan (2022-04-07 12:29 UTC)

<p>Crop volume can extract a single slice of the volume at arbitrary orientation, with correct spacing. You can enable ROI rotation and set orientation and position of the ROI manually; or initialize the ROI automatically from the SliceToRAS transform of the slice node.</p>

---

## Post #6 by @mikebind (2022-04-07 14:45 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>, this is exactly what I have ended up doing. As I started to work through <a class="mention" href="/u/pieper">@pieper</a>’s suggestion, an ROI/CropVolumes based solution occurred to me also, and some quick testing confirmed that it would work even for a single slice.</p>
<p>The only issue I have run into is that the orientation of the exported DICOM image seems wrong in the external DICOM viewer I have been using to test (MicroDICOM).  In one example the exported image was displayed with both the x and y axes inverted relative to the display in Slicer, while in another only the x axis was inverted relative to the display in Slicer.  My first thought was that this was due to the axis orientation of the ROI, but inverting one or more columns of the ROI’s <code>ObjectToNodeMatrix</code> didn’t seem to have any effect.  For the very limited task for which I am generating these images, making specific area measurements, reflections and rotations are not an issue, so I’m not sure how much I am going to try to chase the cause of these inversions down.</p>

---

## Post #7 by @pieper (2022-04-07 14:51 UTC)

<p>Most dicom viewers work in image space (ignoring ImageOrientationPatient and ImagePositionPatient), so you probably want to pick the origin of your resampling to be close to a cardinal plane, usually axial, and the direction to match the layout of pixels in an image.</p>

---

## Post #8 by @mikebind (2022-04-07 15:39 UTC)

<p>Thanks for the insight, Steve.  Can I control the origin of the resampling by controlling the axis directions of the ROI used for cropping?  That’s sort of what I was imagining I was doing when I inverted the ROI axis directions to try to invert the displayed DICOM image, but I didn’t see the effect I expected in the DICOM viewer.  However, I may also have not thought things through sufficiently; for example maybe I should have tried switching the x and y directions rather than negating each individually.  Or, are you saying that all that orientation information ends up in the DICOM header orientation information where the viewer  mostly ignores it and just displays the 2D image based on the voxel order in memory?  If that’s the case, then how do I control the voxel order in the exported file to achieve a desired 2D orientation?</p>

---

## Post #9 by @pieper (2022-04-07 15:51 UTC)

<p>It’s an interesting question Mike.  We may have to go back to look at the CropVolume implementation to see if we can easily control it there.  Internally it uses <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/ResampleScalarVectorDWIVolume">an ITK-based CLI</a> that has extra parameters.</p>
<p>Or, since you are getting into the guts here a bit, you might just try to use <code>vtkImageReslice</code> directly with basically the transform from the slice view rendering path.</p>
<p>Now that I think. bit, maybe the easiest is to just take the image from the slice view, e.g. with ScreenCapture, and figure out the pixel spacing in mm to put in the dicom header and leave the orientation as identity, which will make the dicom viewer show it the same raster grid as Slicer displays.  You can get the screen space pixel spacing from the view settings by looking at <a href="https://github.com/Slicer/Slicer/blob/67295561c7f33b65bc763dd6282ecacd7e8c410d/Libs/MRML/DisplayableManager/vtkMRMLRulerDisplayableManager.cxx#L266-L281">how the ruler code does it</a>.</p>

---

## Post #10 by @lassoan (2022-04-07 19:53 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="8" data-topic="22853">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>then how do I control the voxel order in the exported file to achieve a desired 2D orientation?</p>
</blockquote>
</aside>
<p>Crop volume and DICOM export should preserve the correct image orientation (if you suspect that this is not the case then let us know). But it is then completely up to each DICOM viewer how they choose the default orientation. The orientation may be simply based on the order of pixel storage (e.g., first byte on disk is always displayed in top-left corner by default), or the viewer may use a hanging protocol that prescribes approximate anatomical directions for the displayed slice.</p>
<p>You can adjust the voxel storage order of a volume (without impacting physical location of the image) using <code>Orient Scalar Volume</code> module. This should take care of the image orientation if the viewer uses pixel order to orient the image.</p>
<p>Note that for 2D DICOM image viewers image flip and rotate functions are essential, they are always available. Therefore, if you don’t like the default orientation you can always change it by a few clicks in the 2D viewer.</p>

---

## Post #11 by @mikebind (2022-04-08 18:52 UTC)

<p>Thanks for your help, <a class="mention" href="/u/lassoan">@lassoan</a>  and <a class="mention" href="/u/pieper">@pieper</a>.  Here is a gist with the (not polished but perhaps helpful to someone else) code I used.   <a href="https://gist.github.com/mikebind/b3e01fdc57d7d3d0cef72cb43cb59a75" class="inline-onebox">Excerpt of 3D Slicer module logic code to essentially export the "Red" slice view image to a single slice DICOM file · GitHub</a></p>

---

## Post #12 by @lassoan (2022-04-08 22:13 UTC)

<p>Thanks for sharing. A small comment: inverting a single axis of a transformation matrix turns the 3D space inside out. In this specific case this did not end up causing a problem because you exported a single slice, but it would be better to invert another axis of the transform because in the future others may use your code snippet for extracting a multiple slices.</p>

---

## Post #13 by @mikebind (2022-04-08 22:26 UTC)

<p>Thanks for that point.  I added this clarifying note to the gist:</p>
<p>"IMPORTANT NOTE: Inverting a single axis is NOT appropriate if you are exporting more than one slice!!  Changing a single axis direction in 3D space is equivalent to a mirror reflection, and the “handedness” of any non-mirror symmetric 3D structure will be inverted compared to reality.  It’s OK for a single slice because there can’t be any “handedness” to a 2D structure (a reflection is equivalent to looking at the same plane from the other side). "</p>

---

## Post #14 by @lassoan (2022-04-08 22:40 UTC)

<p>This comment is too long and complicated and so most people will not understand what you mean. Instead, you could change the loop to:</p>
<pre><code class="lang-python">for row in range(4):
            for col in [0, 1]: # invert second axis
                roiTransformMatrix.SetElement(row, col, -1 * roiTransformMatrix.GetElement(row,col))
</code></pre>
<p>(If this leads to undesired flip then use <code>[1, 2]</code>.)</p>
<p>But even better, if you want simpler, safer code, then you can apply a rotation to the sliceToRas transform (you can replace <code>RotateX</code> by <code>RotateY</code> or <code>RotateZ</code> if you want to rotate along a different axis):</p>
<pre><code class="lang-python">roiTransform = vtk.vtkTransform()
roiTransform.Concatenate(sliceTransformMatrix)
roiTransform.RotateX(180)
roi.SetAndObserveObjectToNodeMatrix(roiTransform.GetMatrix())
</code></pre>
<p>As a general rule: in medical imaging the “F word” (flip) is taboo. Always rotate instead, except the very special cases when you actually need to mirror one side of the patient to the other (e.g., correct deformity by mirroring healthy side of the patient to the diseased side).</p>

---
