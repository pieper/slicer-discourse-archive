# Only a single slice is loading for cine MRI

**Topic ID**: 18933
**Date**: 2021-07-26
**URL**: https://discourse.slicer.org/t/only-a-single-slice-is-loading-for-cine-mri/18933

---

## Post #1 by @arjmarj (2021-07-26 21:09 UTC)

<p>Hi,</p>
<p>I am trying to load a cine cardiac MRI into slicer using the DICOM module. Unfortunately it is not loading and I am having the same problem across all patients.</p>
<p>I have tried using the DICOME patcher function but the output is the exact same as the picture below (only a single slice can be seen). I have also tried changing the DICOM reader approach in applications settings to both DCMTK and GDCM.</p>
<p>I can upload an anonymized file for someone to try to load.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af2e70e461d5fabd0d98fa40530bb1163cfd9963.jpeg" data-download-href="/uploads/short-url/oZJ3vSmpndVOjUPS8B6E8G9Dh4f.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/af2e70e461d5fabd0d98fa40530bb1163cfd9963_2_690x320.jpeg" alt="image" data-base62-sha1="oZJ3vSmpndVOjUPS8B6E8G9Dh4f" width="690" height="320" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/af2e70e461d5fabd0d98fa40530bb1163cfd9963_2_690x320.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/af2e70e461d5fabd0d98fa40530bb1163cfd9963_2_1035x480.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/af2e70e461d5fabd0d98fa40530bb1163cfd9963_2_1380x640.jpeg 2x" data-dominant-color="36353E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2094×974 163 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-07-26 21:10 UTC)

<p>You can replay the sequence by pressing the play button on the Sequence browser toolbar.</p>
<p>How would you like to use these images?</p>

---

## Post #3 by @arjmarj (2021-07-27 13:56 UTC)

<p>Hi thank you,</p>
<p>Yes I am able to play the cine video by pressing the play button. However I am only able to see a sliver of the moving video (see green and yellow panel). I would be important to see the whole image, much like the red panel as I would like to pause the image at certain points to segment part of the images (namely adipose tissue around the heart). I will need to see the whole image for segmentation.</p>
<p>Is this a problem that has happened before where cine images are not fully visualized? Is there a way around this?</p>

---

## Post #4 by @lassoan (2021-07-27 15:42 UTC)

<p>It’s all good, this is how single-slice volumes are supposed to appear if the slice view direction (aligned with anatomical axes by default) is not the same as the image slice direction (which may be oblique). You can click the <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view">“Rotate to volume plane” button</a> to align the slice view with the image slice and see the full image. In recent Slicer Preview Releases this is done automatically to make things simpler for new users.</p>

---
