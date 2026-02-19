---
topic_id: 2366
title: "Trouble 3D Slicer Hangs While Saving Big Amount Of Data Afte"
date: 2018-03-19
url: https://discourse.slicer.org/t/2366
---

# Trouble: 3D Slicer hangs while saving big amount of data after registration

**Topic ID**: 2366
**Date**: 2018-03-19
**URL**: https://discourse.slicer.org/t/trouble-3d-slicer-hangs-while-saving-big-amount-of-data-after-registration/2366

---

## Post #1 by @RomanKir (2018-03-19 22:18 UTC)

<p>Hello!</p>
<p>I have a trouble with saving files.<br>
The task I do is really simple. I load 2 files in Analyse format (.img, .hdr) and perform a Landmark-based registration. After hardening the transform I try to save my transformed file, but the app hangs and doesn’t responce (even in an hour).<br>
The problem appears definitely while saving, not during the transformation.</p>
<p>The computer configuration is that:<br>
Intel Server, 64GB RAM, Nvidia GTX1080, more than 4 TB free space. In ‘App Settings’ set Buffer size to 40Gb.<br>
Tested on another computer with 128Gb RAM. The same.</p>
<p>The size of data to load:<br>
2 (.img+.hdr) files, each 1241x847x529 pixels (around 1,45 GB)</p>
<p>Tryed to save in formats .nddr, .nii, .img+.hdr<br>
Nothing changed</p>
<p>With images that smaller in 1.5 times (501x280x353) everything is okey, the Slicer works and saves correctly. But I don’t want to resize images.</p>
<p>Could you please help me? Somehow</p>

---

## Post #2 by @pieper (2018-03-20 07:16 UTC)

<p>Hi Roman -</p>
<p>It’s probably taking a long time to compress that big data.  You could try unchecking the compress option in the save dialog (enable ‘show options’ first).</p>
<p>HTH,<br>
Steve</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/faee3130b9d1cdd51a0ea5c6ec0f0a5bf3e07d22.jpeg" data-download-href="/uploads/short-url/zNPGTOyE0fqtXmUs0Dq5tFceDDA.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/faee3130b9d1cdd51a0ea5c6ec0f0a5bf3e07d22_2_690x225.jpg" alt="image" data-base62-sha1="zNPGTOyE0fqtXmUs0Dq5tFceDDA" width="690" height="225" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/faee3130b9d1cdd51a0ea5c6ec0f0a5bf3e07d22_2_690x225.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/faee3130b9d1cdd51a0ea5c6ec0f0a5bf3e07d22_2_1035x337.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/faee3130b9d1cdd51a0ea5c6ec0f0a5bf3e07d22_2_1380x450.jpg 2x" data-dominant-color="EDEFF1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1894×620 163 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @RomanKir (2018-03-20 08:58 UTC)

<p>Thank you for an idea. But, unfortunately, the same. Just hangs.<br>
I tried with 1241x847x529 pixels size images, saving in .img with no compress.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3a305a65269c39f1aeee42331f0bfbb74e8f2ec.jpeg" data-download-href="/uploads/short-url/nlB6fGG7BW5d7xYZVi9V7lCnzti.jpg?dl=1" title="Slicer_hangs" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a3a305a65269c39f1aeee42331f0bfbb74e8f2ec_2_690x433.jpg" alt="Slicer_hangs" data-base62-sha1="nlB6fGG7BW5d7xYZVi9V7lCnzti" width="690" height="433" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a3a305a65269c39f1aeee42331f0bfbb74e8f2ec_2_690x433.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a3a305a65269c39f1aeee42331f0bfbb74e8f2ec_2_1035x649.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a3a305a65269c39f1aeee42331f0bfbb74e8f2ec_2_1380x866.jpg 2x" data-dominant-color="6F735E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer_hangs</span><span class="informations">1668×1048 556 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Could there be any other variants?<br>
Kind Regards,<br>
Roman</p>

---

## Post #4 by @lassoan (2018-03-20 11:37 UTC)

<p>Have you tried other file formats, such as .nrrd or .mha?</p>

---

## Post #5 by @RomanKir (2018-06-02 10:15 UTC)

<p>Hey!<br>
Sorry for so long, just forgot to write here.</p>
<p>I had a problem for saving a huge amount of data from Slicer 4.8.1 after landmark-based registration. I had a problem with .nii formats. Now the situation improved.</p>
<ol>
<li>The idea of Steve Pieper to uncheck the “Compress” option worked, it helped a bit to increase the speed of saving.</li>
<li>I tested .mha, .nrrd formats, but they didn’t work properly, they also made Slicer hang during the saving process.</li>
<li>The only format worked for me was uncompressed .nhdr, which creates .raw files. With that I could save my files, decreased by 1.5. So, using .nhdr could be a solution to a problem of saving large files.</li>
</ol>
<p>But there is another trouble.<br>
If I want to load the original resolution (2148x1437x500 pixels), the Slicer can’t load it from .nii format, it quits. How could I solve this problem?</p>
<p>Best Regards,<br>
Roman</p>

---

## Post #6 by @lassoan (2018-06-02 15:28 UTC)

<p>You can try to convert using command line tools, such as unu. Or you may write a short ITK application that reads the nii image and writes as nhdr (it should be just a couple of lines of code). Even SimpleITK that is bundled with Slicer might work.</p>
<p>If all else fails, you can create nhdr headers for these nii files. You just have to make sure you set the file offset (header size) field so that it ignores the nifti header at the beginning of the file.</p>

---

## Post #7 by @RomanKir (2018-06-02 20:53 UTC)

<p>Thank you, that could be really a solution. I would try.</p>

---

## Post #8 by @ihnorton (2018-06-04 17:14 UTC)

<aside class="quote no-group" data-username="RomanKir" data-post="5" data-topic="2366">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/439d5e/48.png" class="avatar"> RomanKir:</div>
<blockquote>
<p>If I want to load the original resolution (2148x1437x500 pixels), the Slicer can’t load it from .nii format, it quits.</p>
</blockquote>
</aside>
<p>That sounds like a bug, but I could not reproduce it on Mac: I saved an empty nii file with those dimensions (UInt16 array), and it loads fine in Slicer 4.8.1.</p>
<p>(there was a bug in the current nightly, which caused Slicer to hang for a long time when trying to read a large nifti image; I just submitted a patch for that to ITK)</p>

---
