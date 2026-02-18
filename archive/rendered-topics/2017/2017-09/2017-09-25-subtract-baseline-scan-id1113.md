# Subtract baseline scan

**Topic ID**: 1113
**Date**: 2017-09-25
**URL**: https://discourse.slicer.org/t/subtract-baseline-scan/1113

---

## Post #1 by @mitenp (2017-09-25 12:49 UTC)

<p>Hi,</p>
<p>We have imaged a mouse before and after injecting a vascular contrast agent.</p>
<p>Looking to subtract the before-scan to eliminate the skeletal structure and amplify the arteries for segmentation</p>
<p>Tried the subtraction scalar volumes routing however the resulting image is all grey with a silhouette of the body issue, skeletal structures. Noted there are other masking and registration modules.</p>
<p>As not done such subtraction before, would appreciate any and all guidance on how to perform this using Slicer.</p>
<p>Thanks,</p>
<p>Miten</p>

---

## Post #2 by @lassoan (2017-09-25 13:26 UTC)

<p>You need to adjust brightness/contrast after subtraction. Left click+drag over the slice view or go to Volumes module and edit window/level in Display section. If you see artifacts due to small displacements between the two scans then you may use “General registration (BRAINS)” module (in SlicerCore) or “General registration (Elastix)” module (in SlicerElastix extension) to align the scans before subtraction.</p>

---

## Post #3 by @mitenp (2017-09-25 21:44 UTC)

<p>Hi,</p>
<p>There is no registration required as the mouse was not moved between the two scans so the image locations are practically  the same.</p>
<p>I think there’s an issue with how I am doing the subtraction. See attached images <a href="http://tinyurl.com/slicer-subtract" rel="nofollow noopener">http://tinyurl.com/slicer-subtract</a> or <a href="https://drive.google.com/drive/folders/0B_nZ6skqKQv-aUxQWkx2cHJFZ0k?usp=sharing" rel="nofollow noopener">https://drive.google.com/drive/folders/0B_nZ6skqKQv-aUxQWkx2cHJFZ0k?usp=sharing</a></p>
<p>There are three images, pre, post and subtract. The Subtract is pretty much all grey whereas the mouse and structures are quite defined in the pre &amp; post.</p>
<p>Thanks,</p>
<p>Miten</p>

---

## Post #4 by @lassoan (2017-09-26 02:54 UTC)

<p>The subtracted image looks correct. You just have to adjust the window/level (brightness/contrast) as I described above.</p>

---

## Post #5 by @mitenp (2017-09-26 13:54 UTC)

<p>Cool. Just realised I was subtracting in wrong order ie ended up with Pre - Post rather than Post - Pre</p>
<p>Am re-doing.</p>
<p>Can you advise what Interpolation order controls ?</p>
<p>Thanks</p>

---

## Post #6 by @mitenp (2017-09-26 18:12 UTC)

<p>Hi,</p>
<p>We did a subtraction using MATLAB of two tiffs saved from slicer of Pre and Post and the resulting image has higher contrast, in line with what we were expecting to see, <a href="https://drive.google.com/file/d/0B_nZ6skqKQv-amM0TnpKR1l6MVE/view?usp=sharing" rel="nofollow noopener">https://drive.google.com/file/d/0B_nZ6skqKQv-amM0TnpKR1l6MVE/view?usp=sharing</a></p>
<p>Could you advise if the subtraction module in Slicer can produce similar contrast or that requires further processing after subtraction in slicer?</p>
<p>Thanks again,</p>
<p>Miten</p>

---

## Post #7 by @lassoan (2017-09-26 18:24 UTC)

<p>No further processing should ne needed, just adjusting the window/level to have higher contrast. If you share an anonymized data set through dropbox/onedrive/gdrive and post the link here then I can have a look.</p>

---

## Post #8 by @mitenp (2017-09-26 22:54 UTC)

<p>Hi,</p>
<p>Great, Have copied both sets of DICOM files on to google drive<br>
<a href="http://tinyurl.com/pre-post-review" rel="nofollow noopener">http://tinyurl.com/pre-post-review</a> OR<br>
<a href="https://drive.google.com/open?id=0B_nZ6skqKQv-ZUMtMDJuRER5Vms" rel="nofollow noopener">https://drive.google.com/open?id=0B_nZ6skqKQv-ZUMtMDJuRER5Vms</a></p>
<p>Two directories with DICOM directories  in each.</p>
<p>Let me know if you need anything else.</p>
<p>Many Thanks</p>
<p>Miten</p>

---

## Post #9 by @lassoan (2017-09-27 04:13 UTC)

<p>I’ve checked your images and I can confirm that subtraction works as expected. A couple of comments and recommendations:</p>
<ol>
<li>
<p>Your images are very high resolution and very noisy. Before you can analyze your images, most likely you need to apply smoothing filters, so you won’t be able to benefit from high frequency details in your image but you still have to deal with the large image size (consuming lots of memory, taking long time to compute, etc). If you can change your imaging protocol, I would suggest to try to lower the resolution and/or increase dose. If that’s not feasible, then use Crop volume module to reduce image extent and resolution of your input volumes (Spacing scale = 2.0x, use the same ROI on both pre and post volumes).</p>
</li>
<li>
<p>After you performed subtraction, go to Volumes module and set W: 500, L: 100 (you can left-click + drag on the image to adjust the values). Don’t forget to select the difference volume as <code>Active volume</code> at the top before you adjust the W/L values. You should get something like this:</p>
</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1215dc5be31d0be301f5fb97482e64241fed185.jpeg" data-download-href="/uploads/short-url/yp8yyquwCpjkWKnIdbOjoFmfzI9.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/f1215dc5be31d0be301f5fb97482e64241fed185_2_690x373.jpg" alt="image" data-base62-sha1="yp8yyquwCpjkWKnIdbOjoFmfzI9" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/f1215dc5be31d0be301f5fb97482e64241fed185_2_690x373.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/f1215dc5be31d0be301f5fb97482e64241fed185_2_1035x559.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/f1215dc5be31d0be301f5fb97482e64241fed185_2_1380x746.jpg 2x" data-dominant-color="9A9AA1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 730 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="3">
<li>Even if nothing supposed to be moving between pre and post images, typically there is some motion, which causes very visible artifacts in the difference image. You can use Slicer’s deformable registration modules to compensate motion. I would recommend “General registration (Elastix)” module (in SlicerElastix extension) to align the pre/post image before subtraction.</li>
</ol>
<p>Difference image without motion compensation:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/609f0357f65167e27f49db5020ca2e88b72e3062.jpeg" data-download-href="/uploads/short-url/dMKwj0KPhXz9L665LEAV3aC9moy.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/609f0357f65167e27f49db5020ca2e88b72e3062_2_690x330.jpg" alt="image" data-base62-sha1="dMKwj0KPhXz9L665LEAV3aC9moy" width="690" height="330" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/609f0357f65167e27f49db5020ca2e88b72e3062_2_690x330.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/609f0357f65167e27f49db5020ca2e88b72e3062.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/609f0357f65167e27f49db5020ca2e88b72e3062.jpeg 2x" data-dominant-color="7D7D7D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">762×365 41 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Difference image with motion compensation:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d43f23e6cef56fcce655d94c0b1236e57a182688.jpeg" data-download-href="/uploads/short-url/uhCv48DgSZofEzfOrnK0PbctPXW.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d43f23e6cef56fcce655d94c0b1236e57a182688_2_690x330.jpg" alt="image" data-base62-sha1="uhCv48DgSZofEzfOrnK0PbctPXW" width="690" height="330" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d43f23e6cef56fcce655d94c0b1236e57a182688_2_690x330.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d43f23e6cef56fcce655d94c0b1236e57a182688.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d43f23e6cef56fcce655d94c0b1236e57a182688.jpeg 2x" data-dominant-color="7F7F7F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">762×365 39.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="4">
<li>For 3D visualization, volume measurement, etc. you most likely need to segment the image. You can do that using Segment Editor module. Use the difference image as master volume, select <code>Threshold</code> effect, approximately 100 as lower threshold, and click Apply. Then click <code>Show 3D</code> to show the reconstructed structures in 3D. There will be always small, isolated artifacts that you can remove by <code>Islands</code> effect’s <code>Keep largest island</code> method (removes all disconnected regions) and/or remove unwanted parts with the <code>Scissors</code> effect manually.</li>
</ol>
<p>Show 3D - before Islands effect (difference image computed <em>without</em> motion compensation):</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d9881f65e3c2440f975ea2df08a6caded1e57bb.jpeg" alt="image" data-base62-sha1="8MTS3rzcNqUYjs2N43kKxUgaq9R" width="631" height="440"></p>
<p>Show 3D - after Islands effect (difference image computed <em>without</em> motion compensation):</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22ec7575bd0f2fbb8fa2d2ee85788aa66afd9e57.jpeg" alt="image" data-base62-sha1="4YWQn120iCNdLYV817pC7CpaX0H" width="630" height="438"></p>
<p>Show 3D - after Islands effect (difference image computed <em>with</em> motion compensation):</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac948c73ef5564ac04d261cbbd254ec1ab29ff31.png" alt="image" data-base62-sha1="oCIo70lrzV6LHxgTlECbhEM0Sn7" width="593" height="428"></p>
<p>Rotation view (created by Screen Capture module):</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62db375364e83edbd4ecd7691cc45f9c6749e24d.gif" alt="SlicerCapture" data-base62-sha1="e6wsy2aHO5aogJmBw4r4i46iKQJ" width="608" height="446"></p>

---

## Post #10 by @mitenp (2017-09-27 20:28 UTC)

<p>Wow Andras, thanks for that. You answered the some other questions we were starting to have once we had resolved how to subtraction !</p>
<p>Lowering scanning resolution is not ideal as the carotid we are interested in are only 500um in diameter. However we will be reducing the actual ROI (scanROI) that we scan. Also using slicer crop ROI (cropROI) to eliminate bulk of the image captured was an idea we had. We will be able to take advantage of cropping even in the refined scanROI at imaging as we are only interested in the carotids on either side of the trachea.</p>
<p>However we weren’t too sure how we can ensure the cropROI created from Pre and Post scans are of exactly the same location ?</p>
<p>Is there a trick to do ensure both are exactly the same that or is that by eye ?</p>
<p>Ultimate aim is to segment the carotids to generate STL and centerline for CFD &amp; FSI modelling. Generally familiar with that process though the info you mentioned for segmenting will improve the approach we had tried before. Will forward the outcome for your review and in case it helps others.</p>
<p>Cheers, much appreciated !</p>
<p>Miten</p>

---

## Post #11 by @lassoan (2017-09-29 00:31 UTC)

<aside class="quote no-group" data-username="mitenp" data-post="10" data-topic="1113">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/cdc98d/48.png" class="avatar"> mitenp:</div>
<blockquote>
<p>Is there a trick to do ensure both are exactly the same that or is that by eye ?</p>
</blockquote>
</aside>
<p>Use the same ROI node and then the images will be cropped exactly to the same size. If you register them after cropping then small differences do not matter anyway, as the moving volume is always resampled at the end to the grid of the fixed volume.</p>
<aside class="quote no-group" data-username="mitenp" data-post="10" data-topic="1113">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/cdc98d/48.png" class="avatar"> mitenp:</div>
<blockquote>
<p>Ultimate aim is to segment the carotids to generate STL and centerline</p>
</blockquote>
</aside>
<p>Segment Editor module creates surface mesh (that can be saved as STL), just export it to a model node after the segmentation is completed. VMTK extension can segment vessel and extract vessel centerline automatically.</p>

---
