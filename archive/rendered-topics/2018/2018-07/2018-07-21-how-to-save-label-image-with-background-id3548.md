# How to save label image with background

**Topic ID**: 3548
**Date**: 2018-07-21
**URL**: https://discourse.slicer.org/t/how-to-save-label-image-with-background/3548

---

## Post #1 by @Suradech (2018-07-21 04:16 UTC)

<p>Hello Everyone,</p>
<p>I am segmenting and labeling brain lesions on the MRI brain, but  I cannot save the image with background. The results what I have is image labeling lesion only without background on nii. Do you know how to save the label lesion color on the background of MRI brain?</p>
<p>Another questions can I export/save images with a series of brain MRI into serial PNG file?</p>
<p>Thank you so much in advance for your help.</p>
<p>Suradech</p>

---

## Post #2 by @muratmaga (2018-07-21 05:00 UTC)

<p>If you want to save the image contained within the segmentation, you need to use the Mask Scalar Volume, specify the label to keep and then save that as a new volume.</p>
<p>As for saving the resultant data as PNG stack, you should be able to do that in the save dialog box, by changing the volume format to PNG.</p>

---

## Post #3 by @pieper (2018-07-21 12:51 UTC)

<p>It sounds like you want the ScreenCapture module:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.8/Modules/ScreenCapture" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.8/Modules/ScreenCapture</a></p>

---

## Post #4 by @Suradech (2018-07-21 21:44 UTC)

<p>Hello</p>
<p>Thank you for your reply. I tried but it didn’t work. I might did something wrong.</p>
<p>I want the image like lesion label on MRI with series of PNG images (whole brain mri axial). Attached image what I want (i just did screen capture it) but i could not find the way to save it or export them as whole series of png images. Do you know how can 3d slicer allow to do that.</p>
<p>Thank you so much<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5966299ce396354f2f228b2699911939fdc89ec.jpeg" data-download-href="/uploads/short-url/wL1xrEf50PY2WMJh6oTY4hTStZi.jpg?dl=1" title="example" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e5966299ce396354f2f228b2699911939fdc89ec_2_690x388.jpg" alt="example" data-base62-sha1="wL1xrEf50PY2WMJh6oTY4hTStZi" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e5966299ce396354f2f228b2699911939fdc89ec_2_690x388.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e5966299ce396354f2f228b2699911939fdc89ec_2_1035x582.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5966299ce396354f2f228b2699911939fdc89ec.jpeg 2x" data-dominant-color="9D9D9D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">example</span><span class="informations">1280×720 71.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @lassoan (2018-07-22 02:31 UTC)

<aside class="quote no-group" data-username="Suradech" data-post="4" data-topic="3548">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/8e7dd6/48.png" class="avatar"> Suradech:</div>
<blockquote>
<p>I tried but it didn’t work. I might did something wrong.</p>
</blockquote>
</aside>
<p>ScreenCapture seems to be the appropriate tool for this. We may be able to help if you describe in detail what you did, what you expected to happen, and what happened instead.</p>

---

## Post #6 by @Suradech (2018-07-23 02:23 UTC)

<p>Hi everyone</p>
<p>Thank you again for your help. The outcome I want is the series of brain mri with label lesion on them (total whole brain axial 256 images).</p>
<p>I attached the screen captures of the program during i proformed segmentation for you to review what i did something wrong.</p>
<p>Thank you for your help<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/7179354e28e5b24f7133bc1156c6166621fb73ea.jpeg" data-download-href="/uploads/short-url/gbPDMf7VxMB18fc0DisMn5zd5c6.JPG?dl=1" title="Slide1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7179354e28e5b24f7133bc1156c6166621fb73ea_2_690x388.JPG" alt="Slide1" data-base62-sha1="gbPDMf7VxMB18fc0DisMn5zd5c6" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7179354e28e5b24f7133bc1156c6166621fb73ea_2_690x388.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7179354e28e5b24f7133bc1156c6166621fb73ea_2_1035x582.JPG 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/7179354e28e5b24f7133bc1156c6166621fb73ea.jpeg 2x" data-dominant-color="A0A0A0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slide1</span><span class="informations">1280×720 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9d328641d9d83a57971339c1608fca6003d871c.jpeg" data-download-href="/uploads/short-url/oel5WRu5SZV4xpIv5w3pb2w3eRC.JPG?dl=1" title="Slide2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a9d328641d9d83a57971339c1608fca6003d871c_2_690x388.JPG" alt="Slide2" data-base62-sha1="oel5WRu5SZV4xpIv5w3pb2w3eRC" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a9d328641d9d83a57971339c1608fca6003d871c_2_690x388.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a9d328641d9d83a57971339c1608fca6003d871c_2_1035x582.JPG 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9d328641d9d83a57971339c1608fca6003d871c.jpeg 2x" data-dominant-color="B4B4B4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slide2</span><span class="informations">1280×720 96.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc7f80a6d4d9610c6b715f13f9823401bfb112ff.jpeg" data-download-href="/uploads/short-url/qTwW7jX23ZAtA7Hcj4SkaO38FtB.JPG?dl=1" title="Slide3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc7f80a6d4d9610c6b715f13f9823401bfb112ff_2_690x388.JPG" alt="Slide3" data-base62-sha1="qTwW7jX23ZAtA7Hcj4SkaO38FtB" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc7f80a6d4d9610c6b715f13f9823401bfb112ff_2_690x388.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc7f80a6d4d9610c6b715f13f9823401bfb112ff_2_1035x582.JPG 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc7f80a6d4d9610c6b715f13f9823401bfb112ff.jpeg 2x" data-dominant-color="69696B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slide3</span><span class="informations">1280×720 69.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @lassoan (2018-07-23 04:18 UTC)

<p>It seems that you used the legacy Editor module for editing segmentation, instead of the current Segment editor module. Please try again with Segment Editor (see tutorials <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation">here</a>) and let us know if you still have any problems.</p>

---
