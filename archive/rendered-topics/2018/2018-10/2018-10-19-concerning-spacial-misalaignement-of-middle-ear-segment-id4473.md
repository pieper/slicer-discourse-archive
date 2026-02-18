# Concerning Spacial misalaignement of middle ear segment

**Topic ID**: 4473
**Date**: 2018-10-19
**URL**: https://discourse.slicer.org/t/concerning-spacial-misalaignement-of-middle-ear-segment/4473

---

## Post #1 by @kantzoul (2018-10-19 19:15 UTC)

<p>Hi everyone,</p>
<p>I am working on this middle ear model project that someone had previously started but never finished.<br>
After the previous internship ended, the project was put on hold until now where I have been assigned to it.</p>
<p>Currently the status of the model is that it is not functioning properly. This model is comprised of 2 segmentations of the same image set, where each segmentation is a different area. As of now, the main issue is that the segmentations are not aligned spatially and the tympanic membrane is basically floating in space, nowhere near where it is supposed to be located. I have attached an image for you to see exactly what the problem is.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d3954f5b725993f3cdc860fa5d0966915b817d6.png" data-download-href="/uploads/short-url/4awG8rOSCdIUazP8lCddHaULerc.png?dl=1" title="Screenshot-demo" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d3954f5b725993f3cdc860fa5d0966915b817d6_2_690x480.png" alt="Screenshot-demo" data-base62-sha1="4awG8rOSCdIUazP8lCddHaULerc" width="690" height="480" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d3954f5b725993f3cdc860fa5d0966915b817d6_2_690x480.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d3954f5b725993f3cdc860fa5d0966915b817d6.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d3954f5b725993f3cdc860fa5d0966915b817d6.png 2x" data-dominant-color="989BCA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot-demo</span><span class="informations">789×549 49.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2018-10-20 01:32 UTC)

<p>What form was the data given to you?  Was it only created in Slicer (if so, what version) or were there other tools involved?  If you can share the data people may be able to give you some ideas.</p>

---

## Post #3 by @kantzoul (2018-10-22 14:08 UTC)

<p>To my knowledge its was created solely using 3DSlicer, in 2015, so they probably used some 4.3.X version. The original data was given in the form of a “.nrrd” of the middle ear region. Because the Tympanic membrane is very thin it was manually segmented by the previous interns, as it could not be identified by 3DSlicer.</p>
<p>Currently I am using 3DSlicer 4.8.1. I have attached the files I have been given.</p>

---

## Post #4 by @lassoan (2018-10-22 14:28 UTC)

<p>Thank you, sharing the data will help a lot in resolving the problem. The link requires UWaterloo sharepoint account, so we cannot access it. Please use dropbox, onedrive, gdrive, or other similar file sharing service.</p>

---

## Post #5 by @kantzoul (2018-10-22 14:56 UTC)

<p>I have attached a drop box link</p>

---

## Post #6 by @pieper (2018-10-22 15:30 UTC)

<p>Thanks - sharing the data is a big help.</p>
<p>From a quick look I was able to load several of the nrrd files from the Anna and Susan directory and everything appears to line up nicely.  I saw there’s a word document with several scripts - I didn’t try to debug those bug my suspicion is that the image geometry is not being taken into account correctly.  If I look at the data using the Segmentations infrastructure it looks fine.  What operations did you perform that led to the misalignment?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3d39c8bfc41a9c701b8e8c2b447ab2b3f6b8a5c.jpeg" data-download-href="/uploads/short-url/udU7ykXHQUhH3FjjzQTMgrVQrus.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3d39c8bfc41a9c701b8e8c2b447ab2b3f6b8a5c_2_690x455.jpeg" alt="image" data-base62-sha1="udU7ykXHQUhH3FjjzQTMgrVQrus" width="690" height="455" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3d39c8bfc41a9c701b8e8c2b447ab2b3f6b8a5c_2_690x455.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3d39c8bfc41a9c701b8e8c2b447ab2b3f6b8a5c_2_1035x682.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3d39c8bfc41a9c701b8e8c2b447ab2b3f6b8a5c_2_1380x910.jpeg 2x" data-dominant-color="A0A0B0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1812×1195 611 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @pieper (2018-10-22 15:31 UTC)

<p>Note that for the Tympanic membrane you should probably crop and supersample that area so there are more segmentation samples - this will allow you to reconstruct a consistent surface model.</p>

---

## Post #8 by @kantzoul (2018-10-22 16:02 UTC)

<p>If you look at the original image I shared, the Tympanic membrane is a smooth surface. That is what I am trying get, the tympanic membrane to be a smooth surface at the proper anatomical special location . So I am a bit lost as to how to actually get to that point. Also when I follow the instructions and scripts in the word file, I end up getting an error in the first file. I have attached a screen shot below.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4bb88774c8988e4187df81fbf7cfb7158ee9e2b.png" alt="Error" data-base62-sha1="pMPJpsPesc8hIniDBCfTYewvJfd" width="562" height="200"></p>

---

## Post #9 by @pieper (2018-10-22 19:17 UTC)

<p>The problem is that the membrane is being approximated here as a single pixel width so the surface reconstruction doesn’t have enough samples to make a good surface.</p>
<p>Probably the easiest and most accurate thing is to use the CropVolume module to supersample the membrane volume to something like 3x resolution using linear interpolation.  This will give you a smooth volume several pixels wide that you can segment with thresholding.  If you use all the Slicer GUI tools the geometry will be maintained and you won’t need to do the scripting.</p>

---

## Post #10 by @kantzoul (2018-10-22 19:32 UTC)

<p>Thank you. I shall try this and get back to you.</p>

---

## Post #11 by @kantzoul (2018-10-25 17:05 UTC)

<p>Okay so I tried you suggestions and the issue was resolved. I have attached a screen shot for you to see. However a new issue has presented it self. I am having a hard time closing holes on the membrane and some other segmentations as well. I tried using closing holes in the smoothing option and it worked for some holes but not all of them. Is there another way I could fix this?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/842afa5caa0d74d5412cef74c2b41ab9a4c76162.png" data-download-href="/uploads/short-url/iRd6zqb8uDra3LsBAHGZao90xOO.png?dl=1" title="Capture6" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/842afa5caa0d74d5412cef74c2b41ab9a4c76162_2_689x402.png" alt="Capture6" data-base62-sha1="iRd6zqb8uDra3LsBAHGZao90xOO" width="689" height="402" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/842afa5caa0d74d5412cef74c2b41ab9a4c76162_2_689x402.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/842afa5caa0d74d5412cef74c2b41ab9a4c76162_2_1033x603.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/842afa5caa0d74d5412cef74c2b41ab9a4c76162.png 2x" data-dominant-color="9192BA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture6</span><span class="informations">1196×697 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @lassoan (2018-10-25 17:52 UTC)

<p>The models look beautiful!</p>
<p>Please create a new topic for smoothing/hole filling question. Include example images in the post so that we can have an idea what the problem is.</p>

---

## Post #13 by @yakeworld (2018-11-08 13:14 UTC)

<p>where is the ear data and where is the model</p>

---

## Post #14 by @yakeworld (2018-11-08 22:06 UTC)

<p>The dropbox link broken</p>

---

## Post #15 by @ramon3190 (2018-11-09 11:05 UTC)

<p>What a wonderful work¡¡Please,could you teaching how to do it.Thanks¡</p>

---
