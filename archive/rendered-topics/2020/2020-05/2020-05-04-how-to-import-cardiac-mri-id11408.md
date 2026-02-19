---
topic_id: 11408
title: "How To Import Cardiac Mri"
date: 2020-05-04
url: https://discourse.slicer.org/t/11408
---

# How to import cardiac MRI

**Topic ID**: 11408
**Date**: 2020-05-04
**URL**: https://discourse.slicer.org/t/how-to-import-cardiac-mri/11408

---

## Post #1 by @Calin (2020-05-04 19:20 UTC)

<p>Hello.</p>
<p>I have imported a series of DICOM files of a cardiac MRI, but it shows just all slides separated. How can I merge them? I drag-and-dropped the folder - it did not work. Also, I tried to drag as “AnyData” and then disselect “Single file”…  it did not work.</p>
<p>I want to mention that when I upload images to a viewer, they are separate … it’s not a series. This is how the technician makes the acquisition.<br>
Could be a solution to create a series of images using 3dslicer? “converter -&gt; Create a DICOM series”…I couldn’t make it work.<br>
Could you help me find the answer here? It would really help me out. Thank you very much!</p>

---

## Post #2 by @lassoan (2020-05-04 21:14 UTC)

<p>Clear the DICOM database folder or choose a different DICOM folder and use latest nightly build of Slicer. If you have further issues then follow instructions on the <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ#When_I_click_on_.22Load_selection_to_slicer.22_I_get_an_error_message_.22Could_not_load_..._as_a_scalar_volume.22">DICOM FAQ page </a>. If those instructions don’t help then you’ll probably have to share an anonymized data set so that we can investigate what is going on with your data, as from what you described it is impossible for us to guess what could be the issue.</p>

---

## Post #4 by @Calin (2020-05-05 22:39 UTC)

<p>Thanks for the reply.<br>
The problem is that some series work and some don’t. I have attached the following to this message:<br>
patient 1: series of images that load fine in 3d slicer. I also attached printscreen with the aspect in 3dslicer.<br>
patient 2 and 3: images purchased 1 by 1 by the technician. This is the protocol, this is the sequence used (PSIR). I attached printscreen with the aspect in 3dslicer.<br>
<a href="https://wetransfer.com/downloads/2bf82abbee6ed08bdca541498998ca1520200505223411/f70757" rel="nofollow noopener">https://wetransfer.com/downloads/2bf82abbee6ed08bdca541498998ca1520200505223411/f70757</a></p>
<p>I am interested in delimiting certain areas on these PSIR images and calculating volumes, areas.<br>
Thank you very much!</p>

---

## Post #5 by @Calin (2020-05-10 10:50 UTC)

<p>I tried the methods you suggested, but I didn’t succeed. I don’t know if you managed to download the images already sent by wetransfer (I can’t upload dicom images here).<br>
Below you have the aspect in a basic viewer and in 3dslicer. Thank you very much for your help! I’m looking forward to your response!<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3dff385f024ff79cb2660a83ab6a4bed49503393.jpeg" data-download-href="/uploads/short-url/8QrVOlLwf4BUElyE5r7ElrngKBl.jpeg?dl=1" title="3dslicer view" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3dff385f024ff79cb2660a83ab6a4bed49503393_2_690x388.jpeg" alt="3dslicer view" data-base62-sha1="8QrVOlLwf4BUElyE5r7ElrngKBl" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3dff385f024ff79cb2660a83ab6a4bed49503393_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3dff385f024ff79cb2660a83ab6a4bed49503393_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3dff385f024ff79cb2660a83ab6a4bed49503393_2_1380x776.jpeg 2x" data-dominant-color="676870"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3dslicer view</span><span class="informations">1920×1080 204 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21f13fbd3df34e44278fe31f74a991bcb4b687f5.jpeg" data-download-href="/uploads/short-url/4QgD42yALQypVxKfuKnrFwqaJ4V.jpeg?dl=1" title="viewer image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21f13fbd3df34e44278fe31f74a991bcb4b687f5_2_690x388.jpeg" alt="viewer image" data-base62-sha1="4QgD42yALQypVxKfuKnrFwqaJ4V" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21f13fbd3df34e44278fe31f74a991bcb4b687f5_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21f13fbd3df34e44278fe31f74a991bcb4b687f5_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21f13fbd3df34e44278fe31f74a991bcb4b687f5_2_1380x776.jpeg 2x" data-dominant-color="343434"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">viewer image</span><span class="informations">1920×1080 275 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
