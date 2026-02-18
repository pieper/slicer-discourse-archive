# Optical Coherence Tomography (OCT) images

**Topic ID**: 14171
**Date**: 2020-10-20
**URL**: https://discourse.slicer.org/t/optical-coherence-tomography-oct-images/14171

---

## Post #1 by @syedf (2020-10-20 19:52 UTC)

<p>Hello,</p>
<p>I was wondering if VMTK can segment OCT .dcm images. I’ve used VMTK before for MRI/CT dicoms, but when I try it for the OCT file, I get no output. The PypePad executes, but stops after a while.</p>
<p>Command:<br>
vmtklevelsetsegmentation -ifile Dicom/Patient_02/IM-0001-0000-0001.dcm -ofile global.vti</p>
<p>PypePad:<br>
LevelSetsOutputFilename = global.vti<br>
FeatureImageOutputFilename =</p>
<p>and nothing after this.</p>
<p>The command prompt produces the following error:<br>
This application has requested the Runtime to terminate it in an unusual way.</p>
<p>Please let me know if there is any information regarding this.</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2020-10-20 22:25 UTC)

<p>OCT images are typically much lower quality than CT and MRI, so it is not surprising if automatic segmentation fails, but you can try to apply some processing that makes them more similar to CT: convert RGB images to grayscale, apply noise filtering, vessel enhancement, etc. If you post a few example images then we might have more specific suggestions.</p>
<p>If automatic segmentation fails then you can always segment your image manually, using Segment Editor module in 3D Slicer.</p>

---

## Post #3 by @shabnam_esmaeelzadeh (2020-12-05 18:41 UTC)

<p>Hello<br>
How to insert a DICOM or radiology image into software such as simvascular?</p>

---

## Post #4 by @lassoan (2020-12-05 18:46 UTC)

<p>What would you like to achieve?<br>
Most software that works with medical images can read images from DICOM files.</p>

---

## Post #5 by @shabnam_esmaeelzadeh (2020-12-06 17:30 UTC)

<p>Thanks for the response, to build three-dimensional geometry of the aorta. From which site can I find DICOM photos?</p>

---

## Post #6 by @guangxv (2020-12-07 16:50 UTC)

<p>In my experiment, it is more easier to use ImageJ to segment OCT images semi-automiticly. ImageJ-&gt;Plugins-&gt;Segmentation Editor.</p>

---

## Post #7 by @lassoan (2020-12-08 02:23 UTC)

<aside class="quote no-group" data-username="shabnam_esmaeelzadeh" data-post="5" data-topic="14171" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shabnam_esmaeelzadeh/48/9090_2.png" class="avatar"> shabnam_esmaeelzadeh:</div>
<blockquote>
<p>Thanks for the response, to build three-dimensional geometry of the aorta. From which site can I find DICOM photos?</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/shabnam_esmaeelzadeh">@shabnam_esmaeelzadeh</a> Do you work with OCT data?</p>
<aside class="quote no-group" data-username="guangxv" data-post="6" data-topic="14171" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/guangxv/48/9024_2.png" class="avatar"> guangxv:</div>
<blockquote>
<p>In my experiment, it is more easier to use ImageJ to segment OCT images semi-automiticly. ImageJ-&gt;Plugins-&gt;Segmentation Editor.</p>
</blockquote>
</aside>
<p>What kind to semi-automatic segmentation plugins ImageJ’s Segmentation Editor has? I’ve checked what is in Fiji-&gt;Plugins-&gt;Segmentation Editor and found this thing:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5683e57d017c2acd864daf853814cbbd24cd343.jpeg" data-download-href="/uploads/short-url/urT2BbPE53RaFyRfv1ZipEM8jgn.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d5683e57d017c2acd864daf853814cbbd24cd343_2_556x500.jpeg" alt="image" data-base62-sha1="urT2BbPE53RaFyRfv1ZipEM8jgn" width="556" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d5683e57d017c2acd864daf853814cbbd24cd343_2_556x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d5683e57d017c2acd864daf853814cbbd24cd343_2_834x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d5683e57d017c2acd864daf853814cbbd24cd343_2_1112x1000.jpeg 2x" data-dominant-color="AAA5A5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1154×1037 145 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Do you mean that you would recommend this instead of Slicer’s Segment Editor? Have you tried the <a href="https://uide/image_segmentation.html#segment-editor-module">Segment Editor module in Slicer</a>?</p>
<p><img src="https://github.com/Slicer/Slicer/releases/download/docs-resources/image_segmentation_segment_editor_module.png" alt="" role="presentation" width="" height=""></p>

---
