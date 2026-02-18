# Changed the format /resolution of volume, now I cant see my segmentations

**Topic ID**: 27482
**Date**: 2023-01-26
**URL**: https://discourse.slicer.org/t/changed-the-format-resolution-of-volume-now-i-cant-see-my-segmentations/27482

---

## Post #1 by @Onur (2023-01-26 15:59 UTC)

<p>Hi there</p>
<p>I tryed to apply some filters on my volume file with imageJ. then imported it to 3dslicer make a segment using threshold. saved it and call my old volume file. (because I cant see all details with filtered volume but its better on some parts)</p>
<p>When I bring my old volume file, new segmentation cant be seen on axis. when I view on 3d I can see that its resolution changed.</p>
<p>left one is created using original volume file, right is made with filtered volume file. How can I merge my new segmentation with original volume file? ty</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1d9e9e8c4b0c940156cbdcc6e503c617fa8e8cf.jpeg" data-download-href="/uploads/short-url/rET1Qpk75T4rJs5nTQCqUsO6jtd.jpeg?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1d9e9e8c4b0c940156cbdcc6e503c617fa8e8cf_2_690x442.jpeg" alt="Screenshot" data-base62-sha1="rET1Qpk75T4rJs5nTQCqUsO6jtd" width="690" height="442" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1d9e9e8c4b0c940156cbdcc6e503c617fa8e8cf_2_690x442.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1d9e9e8c4b0c940156cbdcc6e503c617fa8e8cf_2_1035x663.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1d9e9e8c4b0c940156cbdcc6e503c617fa8e8cf_2_1380x884.jpeg 2x" data-dominant-color="9C9CC8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1419×909 163 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2023-01-26 23:26 UTC)

<aside class="quote no-group" data-username="Onur" data-post="1" data-topic="27482">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/onur/48/18190_2.png" class="avatar"> Onur:</div>
<blockquote>
<p>tryed to apply some filters on my volume file with imageJ.</p>
</blockquote>
</aside>
<p>ImageJ does not keep track of the image geometry (origin, spacing, axis directions), therefore the image gets corrupted when ImageJ saves it. You could restore the image geometry by editing the file header in a text editor or copy the geometry information from the original image by Python scripting.</p>
<p>But most likely you can find much more filters in Slicer and its extensions than in ImageJ. What operations do you perform on the image in ImageJ?</p>

---

## Post #3 by @Onur (2023-01-28 16:04 UTC)

<p>I have fixed the issue by taking volume info from original volume file and then enter same info to other broken one. Had to segment it again but lets say no big deal for first time.</p>
<p>For the other part, yes I have seen many filters in 3dslicer via SimpleITK, but most of them didnt worked well.(at least for me) My goal is to segment skull, teeth mandible via automated tools like threshold, grow from seed etc. Cant do it with my original files because it have a lot of noise and thin bones are not visible. (around eyeball is almost empty) thus makes it hard to segment and it take so much time doing manually.</p>
<p>Tryed using Richard-lucy filter on my data, it wanted 2 input files so as I understand it right I put gaussian blurred on in the first input and then original file in the second input. Not sure if it makes sense. Unsharp mask also did not worked and gives error (Pixel type: 16-bit signed integer is not supported in 3D by class)</p>
<p>With imageJ and some of its plugins, I have generated a PSF from my CT data. Applied unsharp mask (review button also helpfull) but still could not apply richardson because I think generating PSF from a CT data is not a valid way.</p>
<p>If you have suggestions for better skull segmentation, unvisible thin bones, filtering etc. would be gratefull to hear them. Thank you again.</p>

---

## Post #4 by @lassoan (2023-01-28 17:12 UTC)

<p>There have been extensive work on orbital bone reconstruction in Slicer from CTs with unsharp masking with optimal kernel designed based on PSF estimated from the image content. You may find the discussions on this forum. My conclusion was that these improvements were just marginally better (if at all) than basic a isotropic diffusion noise filters, therefore it is not worth the trouble.</p>
<p>If you want to experiment with more filters: Many ITK filters require float or double input mage type. You can use these filters by converting your image with “Cast scalar volume” module.</p>
<p>However, I found that instead of putting a lot of effort into image filtering I could get substantially better quality segmentation of the eyes socket by starting from an imperfect, partial bone segmentation (with lots of holes) and closing the holes (extract solid cavity) by using <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify">SurfaceWrapSolidify extension</a>.</p>
<p>Note that if you need to segment many cases then you can use these manual/semi-automatic methods to segment a few dozen cases, and then train an AI segmentation model and adaptively refine and further train the model with more cases until the AI model provides good enough results fully automatically. All you need for this is implementes in the MONAILabel extension.</p>

---
