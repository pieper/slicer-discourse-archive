# registering freesurfer segmentation to 7 Tesla Volume

**Topic ID**: 28230
**Date**: 2023-03-08
**URL**: https://discourse.slicer.org/t/registering-freesurfer-segmentation-to-7-tesla-volume/28230

---

## Post #1 by @teresababy (2023-03-08 03:41 UTC)

<p>hi all,</p>
<p>I have a subject that I need to make a brain segmentation for. I have already run the 3T MRI through freesurfer and have segmentation files. Is it possible to register the 7T Volume to the 3T segmentation? The voxel sizes are different and my previous attempts have failed. Any advice?</p>

---

## Post #2 by @pieper (2023-03-08 18:57 UTC)

<p>If they are nice quality scans, which they must be if they worked with freesurfer, then registration should be easy.  There’s <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html#automatic-image-registration">background material here</a>.  With current slicer the easiest is to right click one of the volumes in the Data module and pick “Register this” and then right click the other one and pick rigid registration from the pull aside menu.  Everything should be preset for you, but you may want to select to align by center of head or one of the other options if your volumes don’t initially overlap.</p>

---

## Post #3 by @teresababy (2023-03-09 03:37 UTC)

<p>Thanks! I’ve registered the 7t volume to the segmentation file (which I’ve loaded as a label map) but none of the segments are showing up in the segment editor tab. I also can’t visualize both volumes at the same time. Ideally, I would like to overlay the files, lower the opacity on the segmentation volume, and edit the segmentation by hand (on the 7t volume) where necessary. Then I can easily segment out all of the relevant areas. What am I missing?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e74f871029c2784d4bf7a2f710697bf9eca80d4f.png" data-download-href="/uploads/short-url/x0gGkuvSA6nNpszSWqGNysYsuD5.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e74f871029c2784d4bf7a2f710697bf9eca80d4f_2_631x500.png" alt="image" data-base62-sha1="x0gGkuvSA6nNpszSWqGNysYsuD5" width="631" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e74f871029c2784d4bf7a2f710697bf9eca80d4f_2_631x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e74f871029c2784d4bf7a2f710697bf9eca80d4f_2_946x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e74f871029c2784d4bf7a2f710697bf9eca80d4f.png 2x" data-dominant-color="4A3F3F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1057×837 182 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @pieper (2023-03-09 14:46 UTC)

<p>If you right click on a label map in the Data module you can convert it to a segmentation that can be edited.  Then you can pick the 7T scan as the Source volume for editing.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/5086f737b77d9d7474535f0f0ff97392e8ad0ccf.png" alt="image" data-base62-sha1="bunmkZWGohzX8VqDXZAXITuP2k7" width="447" height="244"></p>

---
