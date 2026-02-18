# why my PNG stack from SlicerFab is colorful and very large?

**Topic ID**: 10415
**Date**: 2020-02-24
**URL**: https://discourse.slicer.org/t/why-my-png-stack-from-slicerfab-is-colorful-and-very-large/10415

---

## Post #1 by @Lei (2020-02-24 15:01 UTC)

<p>Operating system: win 10<br>
Slicer version: 4.10.2<br>
Expected behavior: black and white PNG stack from Bitmap generator (600*300dpi)<br>
Actual behavior: very large and clolorful images, not covering the whole area</p>

---

## Post #2 by @pieper (2020-02-24 15:24 UTC)

<p>SlicerFab uses the current VolumeRendering settings to rasterize.  You can control the color in that module.  Also the volume area to be rasterized is controlled by the ROI node used for cropping in VolumeRendering.</p>
<p>Size of the images is controlled in the BitmapGenerator module itself.</p>

---

## Post #3 by @Lei (2020-02-25 08:52 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="10415">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>rasterize</p>
</blockquote>
</aside>
<p>Thank you very much, Steve.</p>
<p>I used ROI to crop my volume model, then I went to BitmapGenerator module and setted up the parameters, when I pressed the generate button it produced very strange PNG pictures. Did I miss something? Thanks!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/114238264731b607766f76642c21c584785ad3b6.jpeg" data-download-href="/uploads/short-url/2sFZsqA1cdzZcP2WXK70xwAOTwG.jpeg?dl=1" title="slice_0014" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/114238264731b607766f76642c21c584785ad3b6_2_507x500.jpeg" alt="slice_0014" data-base62-sha1="2sFZsqA1cdzZcP2WXK70xwAOTwG" width="507" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/114238264731b607766f76642c21c584785ad3b6_2_507x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/114238264731b607766f76642c21c584785ad3b6_2_760x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/114238264731b607766f76642c21c584785ad3b6_2_1014x1000.jpeg 2x" data-dominant-color="FEFDFC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slice_0014</span><span class="informations">1024×1009 62.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92b7ef0252fdf3354357048a11707fb801e4eec6.jpeg" data-download-href="/uploads/short-url/kVVMLXaWQh0hzKSXO4TIhXfJJI2.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/92b7ef0252fdf3354357048a11707fb801e4eec6_2_690x261.jpeg" alt="1" data-base62-sha1="kVVMLXaWQh0hzKSXO4TIhXfJJI2" width="690" height="261" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/92b7ef0252fdf3354357048a11707fb801e4eec6_2_690x261.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/92b7ef0252fdf3354357048a11707fb801e4eec6_2_1035x391.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/92b7ef0252fdf3354357048a11707fb801e4eec6_2_1380x522.jpeg 2x" data-dominant-color="908F94"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1849×702 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/606375c619c30f597f6b0e1d5a70c1c8ac8b3c53.jpeg" data-download-href="/uploads/short-url/dKGVCpc47Z7EclgSF54Pd4hXhU7.jpeg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/606375c619c30f597f6b0e1d5a70c1c8ac8b3c53_2_492x500.jpeg" alt="2" data-base62-sha1="dKGVCpc47Z7EclgSF54Pd4hXhU7" width="492" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/606375c619c30f597f6b0e1d5a70c1c8ac8b3c53_2_492x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/606375c619c30f597f6b0e1d5a70c1c8ac8b3c53_2_738x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/606375c619c30f597f6b0e1d5a70c1c8ac8b3c53_2_984x1000.jpeg 2x" data-dominant-color="FAF5F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1028×1044 69.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @pieper (2020-02-25 13:53 UTC)

<p>Hmm, those look pretty much like I’d expect.  They are thin cuts with the color transform applied.</p>

---

## Post #5 by @Lei (2020-02-25 14:00 UTC)

<p>So these are the pictures I suppose to get? <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20"><br>
I was expecting something like this:<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0ece432132c7185166d13621da010a0959109dd8.jpeg" alt="Képkivágás111" data-base62-sha1="26YB9XGuF2jFSEFwv8lPok8FW76" width="362" height="405"></p>

---

## Post #6 by @pieper (2020-02-25 14:24 UTC)

<p>yes, exactly.  Play with the volume rendering parameters and slice spacing.</p>
<p>Do you have a printer that will accept these images?  Basically each png file represents the material that will be deposited at each layer.  So if they are thin cuts there won’t be much material per-layer.</p>

---

## Post #7 by @Lei (2020-02-25 14:38 UTC)

<p>We have stratasys objet260, there is no voxel utility in the GrabCAD software. I guess we can’t print these images now.</p>
<p>I have another question, when should we use the Floyd–Steinberg dithering algorithm to convert the images into binary bitmaps of black and white pixels? As you see, I got colorful images from BitmapGenerator module.</p>

---

## Post #8 by @lassoan (2020-02-25 18:24 UTC)

<p>There are dithering algorithms developed over the past decades for color printing that could be applied here. However, for optimal color/material separation you would need to know exact specification of the printer and its materials. Independent calibration, parameter identification protocols could be developed to get this information, but since Stratasys knows their hardware and materials very well (even future ones) and they have low-level access to their devices, they will be always in a better position to develop color/material separation algorithms. I would recommend you to contact them and see where they are at with this.</p>

---
