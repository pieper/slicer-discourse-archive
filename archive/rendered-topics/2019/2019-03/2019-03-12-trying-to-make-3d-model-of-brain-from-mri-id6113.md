---
topic_id: 6113
title: "Trying To Make 3D Model Of Brain From Mri"
date: 2019-03-12
url: https://discourse.slicer.org/t/6113
---

# Trying to make 3d model of brain from MRI

**Topic ID**: 6113
**Date**: 2019-03-12
**URL**: https://discourse.slicer.org/t/trying-to-make-3d-model-of-brain-from-mri/6113

---

## Post #1 by @tjop92 (2019-03-12 04:47 UTC)

<p>Hello.  I am trying to create a 3d model of my brain so that I can 3d print it.  I have MRI scans that were done last year.  I have no experience with this software or anything like this.  I have tried a few tutorials and so far haven’t succeeded in any of them.  Does anyone have a guide or tutorial that could show me how to do this?</p>

---

## Post #2 by @lassoan (2019-03-12 04:52 UTC)

<p>Would you like to strip the skull and just print the brain surface? If yes, then I would recommend to use SwissSkullStipper extension to remove the skull, use Segment Editor module to create a segment and add the brain surface by using “Threshold” effect, then export it to STL file using Segmentation module’s “Export to files” section.</p>

---

## Post #4 by @tjop92 (2019-03-12 13:18 UTC)

<p>Alright, so that has gotten me pretty far.  But what I am ending up with are thick slices of my brain that make it appear like it is made out of Legos.  Is there a way for it to be smoother/look more like my actual brain?</p>

---

## Post #5 by @lassoan (2019-03-12 13:40 UTC)

<p>Most probably the image data has low resolution along one or more axes that’s why you see “blocks” (staircase artifacts). There are many ways to address this:</p>
<ul>
<li>Use “Crop volume” module with “Isotropic spacing” option enabled, with potentially decreased “Spacing scale” value to resample the input volume before doing any processing</li>
<li>In Segment Editor, try higher threshold value for retrieving the brain surface</li>
<li>Apply “Smoothing” effect after thresholding in Segment Editor</li>
<li>Adjust “Smoothing factor” (drop-down menu of “Show 3D” button) in Segment Editor</li>
</ul>
<p>If you still have problems achieving good image quality then post some sample images.</p>

---

## Post #6 by @tjop92 (2019-03-12 14:53 UTC)

<p>Firstly, I want to thank you so much for taking time out of your day to help me.  I truly appreciate it.  I am also sorry if my questions are stupid, I know nothing about this software or settings.</p>
<p>Where can I find the settings you mentioned below?</p>
<p>" * Use “Crop volume” with “Isotropic spacing” option enabled, with potentially decreased “Spacing scale” value to resample the input volume before doing any processing"</p>
<ul>
<li>In Segment Editor, try higher threshold value for retrieving the brain surface<br>
<strong>I have it set to basically the highest and lowest settings that are on the slide scale.  Is that a good way to go, or are there better higher and lower values that you know of?</strong>
</li>
</ul>

---

## Post #7 by @tjop92 (2019-03-12 15:10 UTC)

<p>So here are some pictures.  Let me know if those settings are good.  Only thing I wasn’t able to do was the “Crop Volume” as I haven’t figured out how to actually do that yet.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b441b4079982d06e6eb943a4e6bd7468ed8f398.jpeg" data-download-href="/uploads/short-url/6aKrOxjJJb0VWcQXwCqt8uD5Ufe.jpeg?dl=1" title="PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2b441b4079982d06e6eb943a4e6bd7468ed8f398_2_690x493.jpeg" alt="PNG" data-base62-sha1="6aKrOxjJJb0VWcQXwCqt8uD5Ufe" width="690" height="493" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2b441b4079982d06e6eb943a4e6bd7468ed8f398_2_690x493.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2b441b4079982d06e6eb943a4e6bd7468ed8f398_2_1035x739.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b441b4079982d06e6eb943a4e6bd7468ed8f398.jpeg 2x" data-dominant-color="3A3D45"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PNG</span><span class="informations">1239×887 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @tjop92 (2019-03-12 15:11 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/631c28001e827fb032f96f0c9acbbe1a716aaa24.png" data-download-href="/uploads/short-url/e8LAPAvkD9sir9AZBsPtdHOI2gs.png?dl=1" title="Scans" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/631c28001e827fb032f96f0c9acbbe1a716aaa24_2_610x500.png" alt="Scans" data-base62-sha1="e8LAPAvkD9sir9AZBsPtdHOI2gs" width="610" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/631c28001e827fb032f96f0c9acbbe1a716aaa24_2_610x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/631c28001e827fb032f96f0c9acbbe1a716aaa24.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/631c28001e827fb032f96f0c9acbbe1a716aaa24.png 2x" data-dominant-color="EBEEF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Scans</span><span class="informations">681×558 110 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @tjop92 (2019-03-12 15:23 UTC)

<p>I have scans from different angles, would it be possible to merge them so that I get one high resolution image from all sides?</p>

---

## Post #10 by @lassoan (2019-03-12 15:46 UTC)

<aside class="quote no-group" data-username="tjop92" data-post="7" data-topic="6113">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/5fc32e/48.png" class="avatar"> tjop92:</div>
<blockquote>
<p>Only thing I wasn’t able to do was the “Crop Volume” as I haven’t figured out how to actually do that yet.</p>
</blockquote>
</aside>
<p>“Crop Volume” is a module, you can find it in the module list in “Converters” category (or by pressing Ctrl+F and typing the module name).</p>
<aside class="quote no-group" data-username="tjop92" data-post="9" data-topic="6113" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/5fc32e/48.png" class="avatar"> tjop92:</div>
<blockquote>
<p>I have scans from different angles, would it be possible to merge them so that I get one high resolution image from all sides?</p>
</blockquote>
</aside>
<p>Unfortunately, you cannot reconstruct a single high-resolution image from 3 sparse images. See more information in this topic:</p>
<aside class="quote quote-modified" data-post="1" data-topic="4792">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/f07891/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/segmenting-issue-i-cant-remove-ridges-in-3-d-model/4792">I cannot remove "ridges" in 3D segmentation</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9195209a43ef8caf6103e25de91c2d0624c89d9.jpeg" data-download-href="/uploads/short-url/xg5uXSIKtT2QwexG65i6DMoQtEl.jpeg?dl=1" title="image" rel="noopener nofollow ugc">[image]</a> 
Hello! I am a surgeon trying to segment a hip joint for 3-D printing. I have become pretty good at isolating the femur and pelvis bones making different segments, however, I’ve noticed in all of my models I have these “ridges” or “steps” on the side of the segmented model. When I set the master file as axial, I notice the steps in the axial plane. In this picture, I used the sagittal file and have these ridges in that plane. 
The CT DICOMs I’m using have high resolution cuts in axial, …
  </blockquote>
</aside>


---

## Post #11 by @tjop92 (2019-03-12 16:17 UTC)

<p>Followed your awesome advice and posted picture of my settings above.  Still ended up with a similarly blocky brain.  I went ahead and attached an image of the result.  <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e51e61fc9f465fde832a2e952004627c4ea6fc7.jpeg" data-download-href="/uploads/short-url/fJVZlbmUozAvqg7iwst1FYJ1ONp.jpeg?dl=1" title="PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6e51e61fc9f465fde832a2e952004627c4ea6fc7_2_685x500.jpeg" alt="PNG" data-base62-sha1="fJVZlbmUozAvqg7iwst1FYJ1ONp" width="685" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6e51e61fc9f465fde832a2e952004627c4ea6fc7_2_685x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6e51e61fc9f465fde832a2e952004627c4ea6fc7_2_1027x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e51e61fc9f465fde832a2e952004627c4ea6fc7.jpeg 2x" data-dominant-color="404449"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PNG</span><span class="informations">1256×916 182 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #12 by @lassoan (2019-03-12 17:12 UTC)

<p>You need to do crop&amp;resample as the very first processing step. Decrease “Spacing scale” value in “Crop volume” module until you get small enough voxel size (but an overall image size that your computer can still handle).</p>

---

## Post #13 by @dr_usman_sani (2023-11-18 06:05 UTC)

<p>I am having same issue. If i select sagital coronal and axial images in all three windows and when i go to segment editor module it automatically selects one of the planes and the rest are blocky lego type views. And then the 3D model is also blocky.</p>

---

## Post #14 by @dr_usman_sani (2024-02-22 06:31 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5df0e703798ccbc7ee3d4470234f9a6707ad8b20.jpeg" data-download-href="/uploads/short-url/dp2xdrLFBzd9Jh4eZcaRiwYH8eQ.jpeg?dl=1" title="leggo image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5df0e703798ccbc7ee3d4470234f9a6707ad8b20_2_652x499.jpeg" alt="leggo image" data-base62-sha1="dp2xdrLFBzd9Jh4eZcaRiwYH8eQ" width="652" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5df0e703798ccbc7ee3d4470234f9a6707ad8b20_2_652x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5df0e703798ccbc7ee3d4470234f9a6707ad8b20_2_978x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5df0e703798ccbc7ee3d4470234f9a6707ad8b20.jpeg 2x" data-dominant-color="343436"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">leggo image</span><span class="informations">1173×899 144 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
this is happening with me … please help</p>

---
