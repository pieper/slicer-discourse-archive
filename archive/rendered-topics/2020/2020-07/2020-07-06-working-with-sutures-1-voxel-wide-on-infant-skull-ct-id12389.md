---
topic_id: 12389
title: "Working With Sutures 1 Voxel Wide On Infant Skull Ct"
date: 2020-07-06
url: https://discourse.slicer.org/t/12389
---

# Working with sutures <1 voxel wide on infant skull CT

**Topic ID**: 12389
**Date**: 2020-07-06
**URL**: https://discourse.slicer.org/t/working-with-sutures-1-voxel-wide-on-infant-skull-ct/12389

---

## Post #1 by @Otoco (2020-07-06 00:17 UTC)

<p>Operating system: OS X Catalina (10.15.5)<br>
Slicer version: 4.10.2 r28257<br>
Expected behavior: Use thresholding or threshold masking + grow from seeds to create accurate segmentation of skull<br>
Actual behavior: Unable to use automated methods to appropriately distinguish the sutures on CT scan from surrounding bone due to how small they are - either I have to under-threshold the scan and I lose the sutures entirely but retain all of the bony structures or I over-threshold the scan and lose all of the cancellous bone + several less radiodense bony features of the skull (especially nasal bones)</p>
<p>Hello everyone,</p>
<p>Fairly new to slicer but reasonably comfortable with the features (or so I’d like to think), apologies if I’m breaking forum etiquette as this is my first post. I’ve been wracking my brain over this particular issue for a while - I have a set of infant skull CT scans that I wish to segment for research, specifically of the whole skull and separately the temporal bone. While obtaining all of the bone is fairly simple because of the marked difference in contrast between the soft tissue and the bone, the major issue that I have been running into is with the sutures in the skull.</p>
<p>Obtaining the sutures is especially important and relevant to the patient population I’m working with, but they are in various states of fusion and are extremely difficult to delineate well in 3D slicer. My main methods for segmenting the whole skull (I have been manually growing the temporal bone from seeds but that has been its own set of problems) have been either thresholding the entire skull to start or threshold-masking the skull and then growing out the bones from seeds. However, the sutures are so narrow that a given voxel on the scan will include not just the suture but the surrounding bone as well, which affects the hounsfield unit that Slicer reads. This means that I’m either overcorrecting in including all of the bone but then erasing the sutures, or I’m undercorrecting but then losing all of the cancellous bone along with several bony structures like the turbinates, parts of the orbit, pieces of the zygomatic processes, etc. I have an existing volume rendering of this patient that I’m using as a guide in creating my segmentation and using the volume rendering tool in slicer with the CT Bones preset also creates a fairly accurate skull, but it has been immensely difficult figuring out a good solution with Slicer’s tools that doesn’t eventually end up with me manually painting out the sutures on an overcorrected scan (which I started doing but this would not be efficient for 100+ scans with approximately 300 images each).</p>
<p>Any help in finding an effective solution would be huge and I hope this is a reasonable question for the forum. I’ve included some screenshots of my volume rendering guide, my current segmentation, and zoomed in screenshots of the left squamosal suture where this patient is especially troublesome.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/876761c32112e761505e7a9ae8ff5ead96f52cc6.jpeg" alt="Screen Shot 2020-06-26 at 4.37.43 PM" data-base62-sha1="jjPX60gwdvQLGsh31RcyDq4xnnw" width="540" height="316"><br>
zoomed-in on the volume-rendered left squamosal suture<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c86b783d3d9340a5b3cde190c90d52e87818cf8.jpeg" data-download-href="/uploads/short-url/8DrhdHyXXcOxiRAbM0Kr6JEZIyk.jpeg?dl=1" title="Screen Shot 2020-07-05 at 6.29.30 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3c86b783d3d9340a5b3cde190c90d52e87818cf8_2_468x500.jpeg" alt="Screen Shot 2020-07-05 at 6.29.30 PM" data-base62-sha1="8DrhdHyXXcOxiRAbM0Kr6JEZIyk" width="468" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3c86b783d3d9340a5b3cde190c90d52e87818cf8_2_468x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3c86b783d3d9340a5b3cde190c90d52e87818cf8_2_702x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3c86b783d3d9340a5b3cde190c90d52e87818cf8_2_936x1000.jpeg 2x" data-dominant-color="938A85"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-07-05 at 6.29.30 PM</span><span class="informations">1092×1166 237 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
sagittal view of volume rendered CT skull<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e572d42a8efd3b42c487c529d4889723b39eadcb.jpeg" data-download-href="/uploads/short-url/wJNmkN1I23CVr6jZVRUP8adbVd9.jpeg?dl=1" title="Screen Shot 2020-07-05 at 6.48.20 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e572d42a8efd3b42c487c529d4889723b39eadcb_2_438x500.jpeg" alt="Screen Shot 2020-07-05 at 6.48.20 PM" data-base62-sha1="wJNmkN1I23CVr6jZVRUP8adbVd9" width="438" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e572d42a8efd3b42c487c529d4889723b39eadcb_2_438x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e572d42a8efd3b42c487c529d4889723b39eadcb_2_657x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e572d42a8efd3b42c487c529d4889723b39eadcb_2_876x1000.jpeg 2x" data-dominant-color="4B4848"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-07-05 at 6.48.20 PM</span><span class="informations">1190×1356 388 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
overcorrected threshold where all bony structures are present but suture is effectively lost<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7abf1ca684d965b3fbeb5754f73741107f39965b.jpeg" data-download-href="/uploads/short-url/hvRHOSVPRTJIO2CDVZecI2uBsmv.jpeg?dl=1" title="Screen Shot 2020-07-05 at 6.50.25 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7abf1ca684d965b3fbeb5754f73741107f39965b_2_454x500.jpeg" alt="Screen Shot 2020-07-05 at 6.50.25 PM" data-base62-sha1="hvRHOSVPRTJIO2CDVZecI2uBsmv" width="454" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7abf1ca684d965b3fbeb5754f73741107f39965b_2_454x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7abf1ca684d965b3fbeb5754f73741107f39965b_2_681x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7abf1ca684d965b3fbeb5754f73741107f39965b_2_908x1000.jpeg 2x" data-dominant-color="4B4845"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-07-05 at 6.50.25 PM</span><span class="informations">1236×1360 396 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
undercorrected threshold where sutures are more prominent but at the cost of losing lots of bone (note the loss in the nasal cavity for ex)</p>
<p>Didn’t include the grow from seeds shots because grow from seeds has trouble distinguishing the sutures even when I paint them as background due to how well fused it is - even though the sutures are pretty visible on the scan it’s too small for the grow from seeds to create accurate structures so I end up having to correct the segmentation at basically every slice anyway for obtaining both a whole skull and an individual temporal bone.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f784d9f8dd3303b8888af8ae775e401b3f7419b.png" alt="Screen Shot 2020-06-26 at 4.36.30 PM" data-base62-sha1="2cQUrZxK3UhMvxbnXdvU1v3C4tB" width="528" height="500"><br>
quick picture of the left temporal bone I was individually trying to capture - this is after providing multiple seeds over the course of several hours and it still loses a lot of the structure/adds extra structures which leads me to have to go through every slice correcting the seeds.</p>
<p>Again, hope this is sufficient info and any insight would be a huge help.</p>

---

## Post #2 by @lassoan (2020-07-06 02:58 UTC)

<p>It is very common that there is no single global threshold that separates all bone fragments, as in live human patients image resolution and contrast are always limited by maximum allowed X-ray radiation exposure and imaging time.</p>
<p>There are many solutions and the best choice depends on the clinical goal that you would like to achieve. For example, if you need to measure surface areas or you can do surgical planning based on surface segmentation then it is enough to partition the outer surface of the skull. However, if you want to measure bone thickness or density then you need volumetric segmentation. It is also important to know where do you need high accuracy and where do you only need approximate, illustrative segmentation/separation.</p>
<p>Here are two potentially interesting tools (depending on what exactly you want to achieve):</p>
<ol>
<li>For surface-based analysis/segmentation, you can start with drawing suture lines on volume rendering and then use those to extract fragments using Dynamic Modeler’s module Boundary Cut tool:</li>
</ol>
<div class="youtube-onebox lazy-video-container" data-video-id="2105n1ECk9w" data-video-title="Bone surface segmentation using suture lines" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=2105n1ECk9w" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/2105n1ECk9w/maxresdefault.jpg" title="Bone surface segmentation using suture lines" width="" height="">
  </a>
</div>

<p>It may be even possible to automatically extract the suture lines from a few points by extracting bone density and make the curve follow minimal bone density - similarly as it is done for cortical parcellation:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="F6fNMQTxD-4" data-video-title="3D Slicer: Dynamic Modeler - Parametric Surface Editing for Biomedical Applications" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=F6fNMQTxD-4" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/F6fNMQTxD-4/maxresdefault.jpg" title="3D Slicer: Dynamic Modeler - Parametric Surface Editing for Biomedical Applications" width="" height="">
  </a>
</div>

<ol start="2">
<li>For making hollow bones solid, you can use <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify">Surface Wrap Solidify effect</a> in Segment Editor (provided by WrapSolidify extension).</li>
</ol>
<p><a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify/raw/master/Resources/Media/result.gif" class="onebox" target="_blank" rel="noopener">https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify/raw/master/Resources/Media/result.gif</a></p>

---

## Post #3 by @pieper (2020-07-06 14:41 UTC)

<p>In addition, you should look at oversampling the segmentation so you can better capture the fine details of the sutures.  Isotropic oversampling by a factor or 2 should help a lot.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/990eb50e9dfd6fd4557981094100a212f7a9fcf6.png" data-download-href="/uploads/short-url/lQ0yUECwBKu7diewe5DSulsFldA.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/990eb50e9dfd6fd4557981094100a212f7a9fcf6_2_690x404.png" alt="image" data-base62-sha1="lQ0yUECwBKu7diewe5DSulsFldA" width="690" height="404" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/990eb50e9dfd6fd4557981094100a212f7a9fcf6_2_690x404.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/990eb50e9dfd6fd4557981094100a212f7a9fcf6.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/990eb50e9dfd6fd4557981094100a212f7a9fcf6.png 2x" data-dominant-color="DADADA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">871×511 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @tsehrhardt (2020-07-08 00:51 UTC)

<p>If you need the full skull as well, you should threshold what you need to get that first.</p>
<p>Then what I do is use the “Editable Intensity Range” checkbox to Erase only those dark threshold values that will give you a nice gap between parts. It can be tedious but by setting that editable range, you can be messy when painting over the area and not worry too much about following the suture closely. Once you think you’ve separated it enough, you can create another segment for the temporal bone and use the Islands tool to add the temporal bone island to it. If it’s still connected, you can go back and erase the connections.</p>
<p>“Editable Intensity Range” can also be used in Paint if you need to go back and add something back in. I tend to go back and forth, but make sure you adjust the range accordingly. Also use the “Editable Area” option. Sometimes I use the Level Tracing tool as well.</p>
<p>Maybe there’s an easier way, but this is what I do when separating complex fragments in skeletal specimens!</p>

---

## Post #5 by @Otoco (2020-07-13 20:25 UTC)

<p>Thank you for this one (and everyone for all of the help)! I’ve found that overcorrecting and erasing out the sutures with the editable mask like tsehrhardt mentioned is the fastest solution for what I need, since I can edit it depending on how fused the suture is. Wrap solidify was pretty powerful but since my sutures were so fused it kept assuming that the brain cavity was the inside of the bone and filled in the skull instead of the skull bones!</p>

---

## Post #6 by @lassoan (2020-07-14 05:56 UTC)

<aside class="quote no-group" data-username="Otoco" data-post="5" data-topic="12389">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/o/b4bc9f/48.png" class="avatar"> Otoco:</div>
<blockquote>
<p>Wrap solidify was pretty powerful but since my sutures were so fused it kept assuming that the brain cavity was the inside of the bone and filled in the skull instead of the skull bones!</p>
</blockquote>
</aside>
<p>For the future: in Wrap Solidify effect, you can adjust the size of cavities that are carved out, so you can ensure that the brain cavity is not filled in.</p>

---
