---
topic_id: 17603
title: "Calculating Area Surface"
date: 2021-05-13
url: https://discourse.slicer.org/t/17603
---

# Calculating area surface

**Topic ID**: 17603
**Date**: 2021-05-13
**URL**: https://discourse.slicer.org/t/calculating-area-surface/17603

---

## Post #1 by @Pseudoceros (2021-05-13 10:44 UTC)

<p>Hi all,</p>
<p>I created a 3D volume by stacking histological slices and I’m trying to calculate the area of different organs within the sample. I have created a segment outlining one of the organs but the surface value that I get is incredibly large as seen in the picture. The dimensions of the sample are 15mm long, 1mm tall and each slice is 7um thick (85 slices total). However I don’t know where to input these data to calibrate the surface area calculation. Any tips are appreciated.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fad324a989aff56b4ef88bc8078546f3ac66ebae.png" data-download-href="/uploads/short-url/zMTJS0Lt2zTHdUVWSCpuN2FlIgS.png?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fad324a989aff56b4ef88bc8078546f3ac66ebae_2_690x466.png" alt="Screenshot" data-base62-sha1="zMTJS0Lt2zTHdUVWSCpuN2FlIgS" width="690" height="466" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fad324a989aff56b4ef88bc8078546f3ac66ebae_2_690x466.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fad324a989aff56b4ef88bc8078546f3ac66ebae_2_1035x699.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fad324a989aff56b4ef88bc8078546f3ac66ebae.png 2x" data-dominant-color="4B4C4D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1331×899 163 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2021-05-13 12:35 UTC)

<p>You can enter the pixel spacing in the Volumes module (or load with ImageStacks)</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumes.html#load-a-series-of-png-jpeg-or-tiff-images-as-volume" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/volumes.html#load-a-series-of-png-jpeg-or-tiff-images-as-volume</a></p>

---

## Post #3 by @Pseudoceros (2021-05-13 12:38 UTC)

<p>What is the pixel to mm relation? Is 1 pixel 1 mm?</p>

---

## Post #4 by @pieper (2021-05-13 12:41 UTC)

<p>That depends on how the images were acquired.  If they came from a calibrated device like a pathology whole slide imaging scanner then the values would be in the header and you need to use some tool to extract them.  Otherwise maybe there’s a reference structure (ruler) in the image that you can use to calculate.</p>

---

## Post #5 by @Pseudoceros (2021-05-13 12:48 UTC)

<p>What I found in the files is:</p>
<p>Scaling (per pixel): 0.220m x 0.22um</p>
<p>Would that mean that 1 pixel = 0.22um?</p>
<p>Thank you for all your help!</p>

---

## Post #6 by @pieper (2021-05-13 13:31 UTC)

<aside class="quote no-group" data-username="Pseudoceros" data-post="5" data-topic="17603">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/919ad9/48.png" class="avatar"> Pseudoceros:</div>
<blockquote>
<p>Scaling (per pixel): 0.220m x 0.22um</p>
</blockquote>
</aside>
<p>That’s almost surely not correct notation, since it indicates meters by micrometers (very anisotropic).  Most likely it means .22 millimeters but I would suggest you do more research before relying on it.</p>

---

## Post #7 by @Pseudoceros (2021-05-13 13:40 UTC)

<p>Apologies that was a typo, I meant 0.220um x 0.220um</p>
<p>I tried using those values and, although I cannot see the 3D render since it’s so small, I can still see the segments in the green and yellow windows and the resulting area was 0.33 mm2 which I believe is more reasonable. Thank you again.</p>

---

## Post #8 by @Pseudoceros (2021-05-15 08:27 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="17603">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>You can enter the pixel spacing in the Volumes module (or load with ImageStacks)</p>
</blockquote>
</aside>
<p>Sorry to bump this up again <a class="mention" href="/u/pieper">@pieper</a> . I double checked the numbers and the calculation still doesn’t seem right. The original data in the slice files is in the picture below, however when I extracted the images I reduced them to 10% of the original size due to the large files, and edited them on Photoshop to remove the messy background (but without changing anything else). I still don’t know how to properly set the image size, the default values are all 1mm but when I change them to either the pixel data (0.220um) or the size of the sample (15 mm long, 1 mm tall, 0.007 mm thick per slice (or 0,595 mm total since there are 85 slices), the 3D volume either disappears because of the small size or it creates a weird shape. Does anyone have any more tips? Thanks in advance</p>
<p>Also maybe worth noting, when I create the 3D volume I leave the default values on the Image Spacing section for the X and Y (1 mm) but change the Z since otherwise the reconstruction is too thin. I have found that setting the Z value to a value between 5 and 10 mm recovers a better shape but I’m not sure what would be the appropriate value with the settings I mentioned. The width should be 0,595 mm but if I use that number while leaving X and Y as 1 mm it just makes the object even thinner. And again, changing it to either 15mm/1mm/0.595mm or 0.00022/0.00022/0.007 recovers wrong shapes.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e512207e86969d41e2256554e8cfa24283dcf19.png" alt="1ce18205bb323e50826384fc8573c3e2" data-base62-sha1="baP4i0VD5bltxfvInlHuIXXz6fD" width="686" height="253"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72d58876b9366c2ffa59e6f75edd392c3f940109.png" data-download-href="/uploads/short-url/gnRVigg8oKb4d8hfaskEtSkTYtb.png?dl=1" title="a410788b0965123424d89417c8df9fa6" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72d58876b9366c2ffa59e6f75edd392c3f940109_2_690x281.png" alt="a410788b0965123424d89417c8df9fa6" data-base62-sha1="gnRVigg8oKb4d8hfaskEtSkTYtb" width="690" height="281" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72d58876b9366c2ffa59e6f75edd392c3f940109_2_690x281.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72d58876b9366c2ffa59e6f75edd392c3f940109_2_1035x421.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72d58876b9366c2ffa59e6f75edd392c3f940109_2_1380x562.png 2x" data-dominant-color="5E6073"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">a410788b0965123424d89417c8df9fa6</span><span class="informations">1932×788 187 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @pieper (2021-05-15 14:06 UTC)

<p>Since Slicer uses mm as the default unit, something that really is .22um pixel spacing can run into numerical issues (multiplying two very small numbers can lose precision).  A common workaround is to pretend that um are mm and then convert the final measurements back to um.</p>

---

## Post #10 by @lassoan (2021-05-15 22:09 UTC)

<p>Custom unit support is partially implemented (see <a href="https://github.com/Slicer/Slicer/issues/5040" class="inline-onebox">Fix custom unit management · Issue #5040 · Slicer/Slicer · GitHub</a> for details). For example you can select length unit to micrometer in the application settings and it is used in Markups measurements, but it is barely used anywhere else yet. If you often work with microscopy images and figure out a quantification workflow that you want to use then we can probably add unit support for those tools.</p>

---
