---
topic_id: 2293
title: "Brain Visibility In Ct Images"
date: 2018-03-12
url: https://discourse.slicer.org/t/2293
---

# Brain visibility in CT images

**Topic ID**: 2293
**Date**: 2018-03-12
**URL**: https://discourse.slicer.org/t/brain-visibility-in-ct-images/2293

---

## Post #1 by @ReNeu (2018-03-12 02:02 UTC)

<p>Hi Andras,</p>
<p>I’m fairly new to slicer as well and am working on lesion mapping of brain MRI and CT images.</p>
<p>All my files are in DICOM and I was successful uploading, working with and mapping the MRI images.  However, when I open the CT scans I see a fairly grey image with white skull and lack of brain tissue differentiation.  It doesn’t look at all like the CT scan when I view it outside of slice (changing the contrast doesn’t solve the problem).</p>
<p>I searched for answer and someone suggested making sure I import with single file boxes un ticked (which I did).  Nothing seem to work. Do you have any suggestions of what might be going on?</p>
<p>Thanks in advance,</p>
<p>Ettie</p>

---

## Post #2 by @lassoan (2018-03-12 05:50 UTC)

<p>You can set brightness/contrast (window width/level) of CT images to highlight bones or soft tissues, and these settings are quite different. You should be able to see brain if you go to Volumes module and set window/level to W: 80, L: 40.</p>
<p>CTBrain sample data set shown with default W/L settings:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23763ad6be95848bf8153dd989616180f6b4fcbd.png" data-download-href="/uploads/short-url/53I1695G7Sr8ZJG7Pib5SAXplFj.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/23763ad6be95848bf8153dd989616180f6b4fcbd_2_690x492.png" alt="image" data-base62-sha1="53I1695G7Sr8ZJG7Pib5SAXplFj" width="690" height="492" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/23763ad6be95848bf8153dd989616180f6b4fcbd_2_690x492.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/23763ad6be95848bf8153dd989616180f6b4fcbd_2_1035x738.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/23763ad6be95848bf8153dd989616180f6b4fcbd_2_1380x984.png 2x" data-dominant-color="B5B5B5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1956×1396 428 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>CTBrain sample data set shown with W: 80, L: 40:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/efdf9d54cea91b95400350098a4a9ff18f94f080.png" data-download-href="/uploads/short-url/ye1cRsqegVvak5FowkeDPV4FGfu.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/efdf9d54cea91b95400350098a4a9ff18f94f080_2_690x492.png" alt="image" data-base62-sha1="ye1cRsqegVvak5FowkeDPV4FGfu" width="690" height="492" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/efdf9d54cea91b95400350098a4a9ff18f94f080_2_690x492.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/efdf9d54cea91b95400350098a4a9ff18f94f080_2_1035x738.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/efdf9d54cea91b95400350098a4a9ff18f94f080_2_1380x984.png 2x" data-dominant-color="9E9D9E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1956×1396 469 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @ReNeu (2018-03-12 14:21 UTC)

<p>Thank you very much for your prompt reply Andras, your suggestion worked really well, the problem is solved and I’m happily mapping my CT scans.</p>
<p>Just for my understanding, what is the W/L control and how did you decide on the values of 80 and 40?</p>
<p>Cheers,</p>
<p>Ettie</p>

---

## Post #4 by @lassoan (2018-03-12 15:27 UTC)

<p>W and L are width and level (center) of the displayed intensity range. I chose 80 and 40 by looking at the image while adjusting the slider, but CT intensity values are standardized, so this setting should work for most images.</p>

---

## Post #5 by @JMcNaughton (2022-10-04 23:48 UTC)

<p>Hello, I have many CT images and want to set them all to W: 80 and L: 40. Is there a way to do it to all of them at once without changing it individually for each one?</p>
<p>Thanks,<br>
Jake</p>

---

## Post #6 by @pieper (2022-10-05 14:59 UTC)

<p>You can do this with a simple python script.  Check the script repository.</p>

---
