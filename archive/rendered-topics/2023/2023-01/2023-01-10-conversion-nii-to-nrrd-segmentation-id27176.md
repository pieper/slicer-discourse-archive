---
topic_id: 27176
title: "Conversion Nii To Nrrd Segmentation"
date: 2023-01-10
url: https://discourse.slicer.org/t/27176
---

# conversion NII to NRRD segmentation

**Topic ID**: 27176
**Date**: 2023-01-10
**URL**: https://discourse.slicer.org/t/conversion-nii-to-nrrd-segmentation/27176

---

## Post #1 by @Marianne_75 (2023-01-10 20:51 UTC)

<p>Hello,</p>
<p>I used Slicer 5.0.3 to segment brain lesions on MRIs. After that, I converted the seg.nrrd files into nii.gz files to fit in my coregistration workflow (I have to work on different dates for each patient).</p>
<p>Whereas the conversion of the segmentations from nrrd to nii was fairly simple, using sitk.writeimage, the inverse does not seem to work.<br>
It produces a seg.nrrd file of one slice (instead of 3D) which seems to be empty when I load it with Slicer.</p>
<p>I would really appreciate your help, or your ideas!<br>
Thanks a lot,<br>
Marianne</p>

---

## Post #2 by @muratmaga (2023-01-11 00:23 UTC)

<p>What format your registration pipeline is outputting? If you registration pipeline is creating new label maps in a format slicer understands (like nii.gz), you can load them directly into Slicer as segmentation without having to do any conversion. Just expand the load dialog box option, and at the description field instead of default volume choose “Segmentation”</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0a437c1b5633e630692a70f388054b1ac031495.png" data-download-href="/uploads/short-url/rubvzTKt1TC3BoS1k8uZrERTA0J.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0a437c1b5633e630692a70f388054b1ac031495_2_690x235.png" alt="image" data-base62-sha1="rubvzTKt1TC3BoS1k8uZrERTA0J" width="690" height="235" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0a437c1b5633e630692a70f388054b1ac031495_2_690x235.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0a437c1b5633e630692a70f388054b1ac031495.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0a437c1b5633e630692a70f388054b1ac031495.png 2x" data-dominant-color="E6E1E8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">969×331 19.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @Marianne_75 (2023-01-11 10:01 UTC)

<p>Thanks a lot for your quick answer !<br>
I didn’t think that Nifti format could be recognized as segmentation since Slicer only proposes nrrd and vtm format when I save my label maps.</p>

---

## Post #4 by @muratmaga (2023-01-11 16:14 UTC)

<aside class="quote no-group" data-username="Marianne_75" data-post="3" data-topic="27176">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/e9a140/48.png" class="avatar"> Marianne_75:</div>
<blockquote>
<p>I didn’t think that Nifti format could be recognized as segmentation since Slicer only proposes nrrd and vtm format when I save my label maps.</p>
</blockquote>
</aside>
<p>I believe any volumetric format that Slicer understands can be imported as a segmentation. The quality of the output you are going to get out of that process can vary though (based on the format). So give it a try… But for the segmentations you are doing in Slicer, it is best to keep them in the seg.nrrd format.</p>

---
