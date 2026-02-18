# Dicom Output Orientation

**Topic ID**: 3815
**Date**: 2018-08-17
**URL**: https://discourse.slicer.org/t/dicom-output-orientation/3815

---

## Post #1 by @jstout (2018-08-17 17:14 UTC)

<p>When reviewing the data in Slicer, I am able to see the MRI and overlay in Radiological format in the axial slices (R&gt;&gt;L, A&gt;&gt;P). I believe this is called LPS space.</p>
<p>When I export to Dicom, the data is oriented differently  (L&gt;&gt;R, and P&gt;&gt;A).  I have checked the orientation labels on the dicoms and they are correct, but the images are not in radiological orientation.  Is there a way to force the dicom to be in radiological format (LPS space)?  Also, how is the dicom output slice direction chosen - is this embedded in the Nifti data somewhere?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b13e8a674824c9d0a78ca35aaa7db7e96df27012.jpeg" data-download-href="/uploads/short-url/phYvj6lBlnpX3XjRBr74xwkWGQy.jpeg?dl=1" title="Slicer_DicomExport_orientation" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b13e8a674824c9d0a78ca35aaa7db7e96df27012_2_690x295.jpeg" alt="Slicer_DicomExport_orientation" data-base62-sha1="phYvj6lBlnpX3XjRBr74xwkWGQy" width="690" height="295" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b13e8a674824c9d0a78ca35aaa7db7e96df27012_2_690x295.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b13e8a674824c9d0a78ca35aaa7db7e96df27012_2_1035x442.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b13e8a674824c9d0a78ca35aaa7db7e96df27012_2_1380x590.jpeg 2x" data-dominant-color="666666"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer_DicomExport_orientation</span><span class="informations">1469×629 186 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thank you,<br>
Jeff Stout</p>

---

## Post #2 by @pieper (2018-08-17 21:21 UTC)

<p>In Slicer we’re pretty careful with the coordinate systems and they are described here:</p>
<p><a href="https://www.slicer.org/wiki/Coordinate_systems" class="onebox" target="_blank">https://www.slicer.org/wiki/Coordinate_systems</a></p>
<p>If you export a volume (say loaded as nifti) to dicom and load the dicoms back into Slicer it should be an exact match.</p>
<p>As for other viewers that interpret nifti, there may be ambiguities in the interpretation of the header and you should use caution.</p>
<p>If you find an issue you can’t explain, see if you can replicate it with publicly sharable data and post the steps to reproduce.</p>

---

## Post #3 by @lassoan (2018-08-18 06:10 UTC)

<p>You can adjust slice view orientations using Reformat module and you can change default orientations as described here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Change_default_slice_view_orientation">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Change_default_slice_view_orientation</a></p>

---

## Post #4 by @fedorov (2018-08-19 20:11 UTC)

<p>In your screenshot you are showing the image displayed using different viewers.</p>
<p>What you see in the viewer depends both on how the dataset is encoded, and how it is interpreted by the viewer software. Different implementations have different conventions on how they interpret the data, and many viewers completely ignore orientation and generate the view purely based on how the pixel values are arranged in DICOM PixelData. In the general case, you cannot expect two arbitrary viewers to generate views showing images in consistent orientation.</p>

---

## Post #5 by @jstout (2018-08-20 15:12 UTC)

<p>Thank you for the responses.  I agree that all of the orientations are labelled correctly in the data and that it is the viewer that is causing the issue.  I was hoping to find a way to change the 2D pixel data matrix for each Dicom file to be oriented in radiological format, as that appears to be how several dicom viewers are presenting the data.</p>
<p>As suggested by Andras, I will attempt to adjust the slice view orientations using the reformat module.  I don’t know if this will just affect the Slicer view or if it will also change the 2D matrix output into each Dicom file.</p>
<p>Thanks again,<br>
Jeff</p>

---

## Post #6 by @lassoan (2018-08-20 15:27 UTC)

<aside class="quote no-group" data-username="jstout" data-post="5" data-topic="3815">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jstout/48/81473_2.png" class="avatar"> jstout:</div>
<blockquote>
<p>I was hoping to find a way to change the 2D pixel data matrix for each Dicom file to be oriented in radiological format, as that appears to be how several dicom viewers are presenting the data.</p>
</blockquote>
</aside>
<p>Each software that writes DICOM files can choose an arbitrary ordering of pixel rows and columns, as long as values of image position and orientation DICOM fields are consistent. DICOM viewers choose view axis orientation based on user preferences and not on the pixel ordering in the image file.</p>
<aside class="quote no-group" data-username="jstout" data-post="5" data-topic="3815">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jstout/48/81473_2.png" class="avatar"> jstout:</div>
<blockquote>
<p>I will attempt to adjust the slice view orientations using the reformat module. I don’t know if this will just affect the Slicer view or if it will also change the 2D matrix output into each Dicom file.</p>
</blockquote>
</aside>
<p>It will not affect DICOM export. It only changes how data is displayed in Slicer.</p>

---

## Post #7 by @jstout (2018-08-20 18:47 UTC)

<p>Great - thanks for the help.</p>

---
