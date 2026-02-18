# Failing loading scalar volume warning it was given as seen at the hospital

**Topic ID**: 19405
**Date**: 2021-08-30
**URL**: https://discourse.slicer.org/t/failing-loading-scalar-volume-warning-it-was-given-as-seen-at-the-hospital/19405

---

## Post #1 by @yndpr (2021-08-30 02:24 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c500be90a44dc9a1fc750017170d4f505c021034.jpeg" data-download-href="/uploads/short-url/s6LEHJ1bEQinDxD022KXZtpi0S0.jpeg?dl=1" title="UntitleREDDDITTTTTTTTTd" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c500be90a44dc9a1fc750017170d4f505c021034_2_690x388.jpeg" alt="UntitleREDDDITTTTTTTTTd" data-base62-sha1="s6LEHJ1bEQinDxD022KXZtpi0S0" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c500be90a44dc9a1fc750017170d4f505c021034_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c500be90a44dc9a1fc750017170d4f505c021034_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c500be90a44dc9a1fc750017170d4f505c021034_2_1380x776.jpeg 2x" data-dominant-color="5A5A62"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">UntitleREDDDITTTTTTTTTd</span><span class="informations">1920×1080 222 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>the first one survey is a mix of a few slides   {herniated disc c5 c6, …on my 30s… would love to get a 3d model… low res few images sadly…)</p>
<p>the radiologist said i moved— most expensive slight breathing move ever</p>
<p>there is RADIAL which is like a almost a 360 scan … dont know where to put it …</p>
<p>here are the dicom files give in a DVD google drive - <em>link has been removed due to potentially containing patient health information</em>.</p>
<p>if you can guide me to the right path to make this work i would totally appreciate it . thanks in advance:D</p>

---

## Post #2 by @lassoan (2021-08-30 05:45 UTC)

<aside class="quote no-group" data-username="yndpr" data-post="1" data-topic="19405">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/y/cab0a1/48.png" class="avatar"> yndpr:</div>
<blockquote>
<p>survey is a mix of a few slides</p>
</blockquote>
</aside>
<p>You can ignore those. They are very quick, low-resolution slices acquired just to see where you are in the scanner and set the field of view for the actual image acquisition.</p>
<aside class="quote no-group" data-username="yndpr" data-post="1" data-topic="19405">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/y/cab0a1/48.png" class="avatar"> yndpr:</div>
<blockquote>
<p>there is RADIAL which is like a almost a 360 scan … dont know where to put it …</p>
</blockquote>
</aside>
<p>This is a very special acquisition type, I’m not sure what it can be used for, you can ignore these, too.</p>
<p>All the other volumes are Cartesian volumes acquired with highly-anisotropic spacing, in 3 directions. These kind of acquisitions are optimized for review by humans and not well suited for 3D reconstruction. See detailed explanation here:</p>
<aside class="quote quote-modified" data-post="2" data-topic="2941">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/combining-volumes-what-am-i-missing/2941/2">Combining volumes - what am I missing?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    In general, these multiple low-resolution acquisitions are not well suited for any 3D processing, so the best would be to acquire proper 3D volume, with as isotropic spacing (cubic voxel shape) as possible. 
You may try to find toolkits that can create an isotropic super-resolution image from multiple low-resolution sweeps, but this is a difficult image reconstruction problem, so there are no standard solutions. Have a look at this post <a href="https://discourse.slicer.org/t/import-volume-by-projections/2871/6">Import volume by projections</a> for info on a toolkit that mig…
  </blockquote>
</aside>

<p>You may segment structures in the images using Segment Editor module and generate 3D model. I would recommend to resample the volume to be isotropic (using Crop volume module) before you start segmenting it. You can switch between volumes during segmentation to utilize information in all the volumes.</p>

---

## Post #3 by @yndpr (2021-08-31 01:02 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6a675223082bcbb466bf52cbfe44fb0958937e2.jpeg" data-download-href="/uploads/short-url/uCSOmD0y2Nosgqpizsxn1wO0Tlg.jpeg?dl=1" title="UntitleREDDDITTTTTTTTTd2222222" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d6a675223082bcbb466bf52cbfe44fb0958937e2_2_690x388.jpeg" alt="UntitleREDDDITTTTTTTTTd2222222" data-base62-sha1="uCSOmD0y2Nosgqpizsxn1wO0Tlg" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d6a675223082bcbb466bf52cbfe44fb0958937e2_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d6a675223082bcbb466bf52cbfe44fb0958937e2_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d6a675223082bcbb466bf52cbfe44fb0958937e2_2_1380x776.jpeg 2x" data-dominant-color="555559"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">UntitleREDDDITTTTTTTTTd2222222</span><span class="informations">1920×1080 146 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>after 6 hours. this is the best ive come up with.</p>
<p>dont ask me doing it again cause i wont know how haha.</p>
<p>i might be able to paint one by one now… but i believe i am missing the front COR  file …never written in the DVD maybe…</p>
<p>i called to the hospital today and tomorrow i might be able to speak with the radiologist in charge of the exporting the files in the dvd… so i will try to get a isotropic sequence even if i have to pay for the DVD again.    (the guy i spoke with knows about dicom files to 3d. i was surprised, the future is now… haha… but he wasnt in charge of the magnetic resonance department so couldnt help me. i guess) …</p>
<p>i set 1,1, 15, because that was roughly the distance between  scan lines i was able to measure by pixel… was about 14.75 so it was a wild guess…</p>
<p>is this is as good as it gets or i just have gibberish and havent done anything yet? hahaha</p>

---

## Post #4 by @cpinter (2021-08-31 10:30 UTC)

<p>First, make sure that you have resampled the volumes to isotropic (cubic voxels in the image instead of elongated boxes). You can do it in the Crop Volumes module).</p>
<p>Since MRI is not the best modality to get an (semi-)automated segmentation of bones, probably it is best if you do it manually. Make sure you name the resample isotropic images so that you can identify them by name. Then right-click one of them in Data module and choose “Segment this…”. Start painting or use any of the tools that you think are convenient. As <a class="mention" href="/u/lassoan">@lassoan</a> suggest you can switch master volume to make use of image information in the places that have ambiguity. Good luck!</p>

---
