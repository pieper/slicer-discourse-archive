# Trying to do tractography from DICOM DTI

**Topic ID**: 13964
**Date**: 2020-10-09
**URL**: https://discourse.slicer.org/t/trying-to-do-tractography-from-dicom-dti/13964

---

## Post #1 by @Cerebellum (2020-10-09 20:19 UTC)

<p>Hello! Recently I found an old disk from the place I used to work with where I saved my own brain MRI (I used to do tractography with FiberTrak in a Philips station for neuroanatomy teaching purposes).<br>
In that disk I have an anatomic T1 and the DTI sequence saved as dicom archives, is it possible to do tractography with them? I have already tried to load the DTI but haven’t managed to load it the correct way.</p>
<p>Sorry to bother you all with my newbie question (and my horrendous english). If this post is against the forum rules, please let me know so I can delete it.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd19698882f7e0f5f87f198d88382c7431fbf1ec.png" data-download-href="/uploads/short-url/A71fdGmbM2WvUgUxGcej6UUaBWs.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd19698882f7e0f5f87f198d88382c7431fbf1ec_2_690x251.png" alt="image" data-base62-sha1="A71fdGmbM2WvUgUxGcej6UUaBWs" width="690" height="251" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd19698882f7e0f5f87f198d88382c7431fbf1ec_2_690x251.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd19698882f7e0f5f87f198d88382c7431fbf1ec_2_1035x376.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd19698882f7e0f5f87f198d88382c7431fbf1ec_2_1380x502.png 2x" data-dominant-color="ECF0F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1912×697 43.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I hope that everyone is having a nice day!</p>

---

## Post #2 by @pieper (2020-10-09 20:22 UTC)

<p>Completely fair question.  As you know DTI from dicom can be tricky.  First step, it looks like you need to install <a href="http://dmri.slicer.org/">SlicerDMRI</a>.  It will install a plugin that should detect and convert your DWI (assuming the sequence and data format are compatible).  From there you can follow the tutorials on the site.  Good luck.</p>

---
