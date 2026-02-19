---
topic_id: 20511
title: "How To Change Pixel Size Image Spacing Without Changing Of M"
date: 2021-11-07
url: https://discourse.slicer.org/t/20511
---

# How to change pixel size (Image Spacing) without changing of matrix size

**Topic ID**: 20511
**Date**: 2021-11-07
**URL**: https://discourse.slicer.org/t/how-to-change-pixel-size-image-spacing-without-changing-of-matrix-size/20511

---

## Post #1 by @shahrokh (2021-11-07 12:27 UTC)

<p><strong>Dear Users and Developers</strong></p>
<p>I want to change <em>pixel size</em> (<strong>Image Spacing</strong>) without changing of <em>matrix size</em> (<strong>Image Dimensions</strong>).<br>
I check some modules such as <strong>Resample Scalar Volume</strong> and <strong>Resize Image</strong>. I do not success to do it. At these modules, the <em>matrix size</em> and <em>pixel size</em> are changed simultaneously that I do not mean.</p>
<p>Anyway, I am able to do it very simply by changing the <strong>Image Spacing</strong> values in the module of <strong>Volume</strong>. This is OK.</p>
<p>At now, my questions are mentioned as:<br>
1- How can I do this through another module (without <strong>Volume</strong> module)?<br>
2- Is my method correct in doing so (using <strong>Volume</strong> module to change <em>pixel size</em> with changing <em>matrix size</em> using <strong>Volume</strong> module)?</p>
<p>Please guide me.<br>
Best regards.<br>
Shahrokh</p>

---

## Post #2 by @lassoan (2021-11-07 17:18 UTC)

<aside class="quote no-group" data-username="shahrokh" data-post="1" data-topic="20511">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahrokh/48/1499_2.png" class="avatar"> shahrokh:</div>
<blockquote>
<p>How can I do this through another module (without <strong>Volume</strong> module)?</p>
</blockquote>
</aside>
<p>You can change spacing value by calling <code>SetSpacing</code> method of the volume node.</p>
<aside class="quote no-group" data-username="shahrokh" data-post="1" data-topic="20511">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahrokh/48/1499_2.png" class="avatar"> shahrokh:</div>
<blockquote>
<p>Is my method correct in doing so (using <strong>Volume</strong> module to change <em>pixel size</em> with changing <em>matrix size</em> using <strong>Volume</strong> module)?</p>
</blockquote>
</aside>
<p>Changing the pixel size would change the physical size of an object so, it is normally not needed. There are only a few exceptions when it is valid to change the pixel size, for example when the volume is loaded from a format where image spacing is not available and you need to change the default 1.0 value to the actual value.</p>
<p>Why are you considering changing the image spacing without resampling the image? What would you like to achieve?</p>

---

## Post #3 by @shahrokh (2021-11-08 12:49 UTC)

<p>Thanks a lot for your guidance.<br>
In summary, I want to determine the <strong>patient setup error</strong> in radiotherapy by automatically registering two EPID and DRR images.</p>
<p>I want to first make the DRR and EPID images identical in the aspect of pixel size (<strong>Image Spacing</strong>). At first, I must mentioned that these two images are different from these two aspects.</p>
<p>DRR:<br>
Image Dimensions: 512 512 1<br>
Image Spacing: 2.1864mm 2.1864mm 1.0000mm</p>
<p>EPID:<br>
Image Dimensions: 1024 1024 1<br>
Image Spacing: 0.4mm 0.4mm 1.0mm</p>
<p>The following figure is shown this issue.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76f9869318db174cc18d918d9d1add541bfc3049.png" data-download-href="/uploads/short-url/gYuWLqjIw46Pg1NLqTPBxAydUyR.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/76f9869318db174cc18d918d9d1add541bfc3049_2_690x388.png" alt="1" data-base62-sha1="gYuWLqjIw46Pg1NLqTPBxAydUyR" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/76f9869318db174cc18d918d9d1add541bfc3049_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/76f9869318db174cc18d918d9d1add541bfc3049_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/76f9869318db174cc18d918d9d1add541bfc3049_2_1380x776.png 2x" data-dominant-color="737272"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1920×1080 327 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>As you mentioned, I can do it by calling <code>SetSpacing</code> method of the volume node. Thanks a lot.<br>
Result:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/272514917a5e6efe9f2e2a2b414546a3cf5f116e.png" data-download-href="/uploads/short-url/5Ai44f3AlDr0Z0XL170anxrGvJc.png?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/272514917a5e6efe9f2e2a2b414546a3cf5f116e_2_690x388.png" alt="2" data-base62-sha1="5Ai44f3AlDr0Z0XL170anxrGvJc" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/272514917a5e6efe9f2e2a2b414546a3cf5f116e_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/272514917a5e6efe9f2e2a2b414546a3cf5f116e_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/272514917a5e6efe9f2e2a2b414546a3cf5f116e_2_1380x776.png 2x" data-dominant-color="71706F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1920×1080 294 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>At this moment, I can match the centers of these two images with <strong>Center Volume</strong> in <strong>Volume</strong> module. In practice, the centers of these two images are the place through which the central axis of the radiation field of LINAC passes.</p>
<p>Now, with the guidance you gave me in my topics entitled “ <strong>Crop regions outside the radiation field of the DRR image</strong> ”, I can crop out-of-field areas of the DRR image.</p>
<p>After completing these steps, I want to compare the two images matrices <strong>row</strong> by <strong>row</strong>. I assume these rows as the spatial one-dimensional signals. I think that I can do it with numpy arrays.</p>
<p>After doing it, I want to evaluate the similarity of these two signals (from DRR cropped and EPID) with a tool like xcor. This work must be done for finding similar signals (rows). I interpret that two similar signals correspond to the same anatomical regions.</p>
<p>If this is true, I can determine the amount of spatial shift of the two similar signals. This value of spatial shift can be a patient setup error in the <em>Right - Left</em> direction of the patient.</p>
<p>The same can be done for the columns of EPID and DRR and determine patient setup error in the <em>Inferior - Superior</em> direction of the patient.</p>
<p>I’ll be happy to receive your feedback on these steps.</p>
<p>‌Best regards.<br>
Shahrokh</p>

---

## Post #4 by @lassoan (2021-11-08 13:17 UTC)

<p>You should be able to register these images fully automatically after an approximate initial alignment. All the automatic registration methods in Slicer are set up for 3D (multi-slice) images, so you need to change their parameters to constrain the transformation to 2D (or split the síngle-slice image to 3-5 identical slice.</p>
<p>You may also consider using SimpleITK for this registration, as the basic ITK registration framework could be sufficient for this and there are many 2D Image registration examples online for SimpleITK. If you get stuck you can ask help for this on the <a href="https://discourse.itk.org/">ITK forum</a>.</p>

---

## Post #5 by @simonoxen (2021-11-08 15:41 UTC)

<p>Hi, not sure if this helps, but you can do 2D registration with SlicerANTs Extension. See the <strong>dimensionality</strong> property under <strong>Settings</strong></p>

---
