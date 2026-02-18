# Create a smooth segmented 3D model from PNG images

**Topic ID**: 22957
**Date**: 2022-04-14
**URL**: https://discourse.slicer.org/t/create-a-smooth-segmented-3d-model-from-png-images/22957

---

## Post #1 by @bhowmisp (2022-04-14 02:59 UTC)

<p>Hi,</p>
<p>I have been using the Visible Human project TIFF images to segment out the spinal cord and DRG. The DRG is not clearly visible but I want to get an idea of the relative vertical levels of the DRG and the Spine, especially in the lumbosacral region.</p>
<p>However, the issue is when I segment the images to create a 3D model, the model appears as a combination of layers of slices, which I segmented in each slice but not a continuous 3D model. How to get rid of this?  Is it an issue with my segmentation or something inherent with the quality of images? I am attaching two pictures to demonstrate what I mean.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34626076e8b542ebd847a9150dca648cb07cd035.jpeg" data-download-href="/uploads/short-url/7tpBbGYZYCl0JsWCnJ7LT3ZCzK5.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34626076e8b542ebd847a9150dca648cb07cd035.jpeg" alt="image" data-base62-sha1="7tpBbGYZYCl0JsWCnJ7LT3ZCzK5" width="690" height="499" data-dominant-color="785B5E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">818×592 64.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed8e9692293561848edcae8f0f96ce231db35333.jpeg" data-download-href="/uploads/short-url/xTwEySY2sLwwYWJwlPpRHxpvwoH.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed8e9692293561848edcae8f0f96ce231db35333.jpeg" alt="image" data-base62-sha1="xTwEySY2sLwwYWJwlPpRHxpvwoH" width="668" height="500" data-dominant-color="6F575C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">822×615 65.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I have an additional question, the CT and MRI data from the VHP come in extensions of .fre and .t1/.t2 respectively. I am unable to load these in Slicer, neither via add data nor via add DICOM. Are these not supported?</p>

---

## Post #2 by @lassoan (2022-04-14 11:44 UTC)

<p>If you use “Grow from seeds” effect, your need to click “Apply” if the previewed results are satisfactory.</p>
<p>Note that you click “Show 3D” button at the top of the effect list then it toggles visibility of the current segments (the seeds that you painted). If you want to preview the grown segments in 3D then click “Show 3D” button within the effect options section.</p>

---

## Post #3 by @bhowmisp (2022-04-14 16:34 UTC)

<p>Hi,</p>
<p>Sorry, I got confused.</p>
<p>I am segmenting the required slices and then clicking “Show 3D”.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac4807ef4977a0a852a5d354617867670c9873e6.jpeg" data-download-href="/uploads/short-url/oA4rW9vQ4u9j2ACo146YvI0gEmO.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ac4807ef4977a0a852a5d354617867670c9873e6_2_690x321.jpeg" alt="image" data-base62-sha1="oA4rW9vQ4u9j2ACo146YvI0gEmO" width="690" height="321" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ac4807ef4977a0a852a5d354617867670c9873e6_2_690x321.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ac4807ef4977a0a852a5d354617867670c9873e6_2_1035x481.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ac4807ef4977a0a852a5d354617867670c9873e6_2_1380x642.jpeg 2x" data-dominant-color="897E80"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×895 187 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I don’t see any other Show 3D option and when I use the Grow from seeds, there is no change in the visible 3D structure. (It doesn’t make any changes after I initialize.)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/59e785a1e3318bf9b1e4d7ac909fb9050a193dae.jpeg" data-download-href="/uploads/short-url/cPkwLriglslDoup2xdmls4XSxps.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/59e785a1e3318bf9b1e4d7ac909fb9050a193dae_2_690x321.jpeg" alt="image" data-base62-sha1="cPkwLriglslDoup2xdmls4XSxps" width="690" height="321" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/59e785a1e3318bf9b1e4d7ac909fb9050a193dae_2_690x321.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/59e785a1e3318bf9b1e4d7ac909fb9050a193dae_2_1035x481.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/59e785a1e3318bf9b1e4d7ac909fb9050a193dae_2_1380x642.jpeg 2x" data-dominant-color="8B7F80"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1917×893 189 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2022-04-14 19:51 UTC)

<p>The “Show 3D” button for the result preview is next to the “Display” slider, on the right side. It is useful if you paint seeds in the image that you use for computing complete segmentations. See a very simple tutorial for segmenting a single object here:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="cybL5A0w3hw" data-video-title="Brain tumor segmentation on MRI in 1 minute" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=cybL5A0w3hw" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/cybL5A0w3hw/maxresdefault.jpg" title="Brain tumor segmentation on MRI in 1 minute" width="" height="">
  </a>
</div>

<p>By the way, the image appears to be distorted: spacing along I/S axis seems to be too low compared to other axes. And the images is flipped along the I/S axis and the A/P axis.</p>
<aside class="quote no-group" data-username="bhowmisp" data-post="1" data-topic="22957">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/e5b9ba/48.png" class="avatar"> bhowmisp:</div>
<blockquote>
<p>I have an additional question, the CT and MRI data from the VHP come in extensions of .fre and .t1/.t2 respectively.</p>
</blockquote>
</aside>
<p>You can load any uncompressed images into Slicer. For example, you can do that conveniently using the RawImageGuess extension.</p>
<p>However, the VHP server contains the data set in so many representations that I would recommend to just read the images from a bit friendlier, more standard format.</p>

---

## Post #5 by @bhowmisp (2022-04-14 20:31 UTC)

<p>Once I paint the slices in all three views, click “grow from seeds” and then initialize: Nothing Happens. There is no 3D volume created and thus the Show 3D next to the display appears inactive.</p>
<p>I should also mention that I am painting across multiple slices.</p>
<p>But before I rectify any of those, I suspect is the incorrect orientation the reason for this? If so, how do I reorient the images?</p>

---

## Post #6 by @lassoan (2022-04-15 01:10 UTC)

<p>“Grow from seeds” (as most other effects) work in 3D, so it does not matter which slices you draw the input seeds, in what orientation.</p>
<p>Make sure you have at least two segments: one segment for the structure you are interested in, and one “background” segment for everything else.</p>

---

## Post #8 by @bhowmisp (2022-04-16 00:26 UTC)

<p>I tried the options suggested.</p>
<p>First, I re-oriented the images, just to have a proper visual. Then I select two segments, the Spinal cord which I want to segment and the rest of the body, it takes an enormous amount of time to compute and comes up with something like this, which is grossly incorrect.</p>
<p>I understand this might be due to the quality of the images, but I am curious to know how to rectify/improve this 3D model. The painted segments look a bit different than what I selected, so I am guessing the algorithm is picking up pixels I have not selected while growing from the seeds.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/779a5dffcc4bc576897367b41d67f200350fc60f.jpeg" data-download-href="/uploads/short-url/h43y2VZSzFSXhjhtqtiAqmD5Kyj.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/779a5dffcc4bc576897367b41d67f200350fc60f_2_690x313.jpeg" alt="image" data-base62-sha1="h43y2VZSzFSXhjhtqtiAqmD5Kyj" width="690" height="313" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/779a5dffcc4bc576897367b41d67f200350fc60f_2_690x313.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/779a5dffcc4bc576897367b41d67f200350fc60f_2_1035x469.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/779a5dffcc4bc576897367b41d67f200350fc60f.jpeg 2x" data-dominant-color="B3ACA4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1360×618 90.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #9 by @lassoan (2022-04-16 00:32 UTC)

<p>Grow from seeds may take up to a few ten seconds for large images. If computation takes much longer for you then either your computer does not have enough RAM (in general, it is recommended to have 10x more RAM than your image size) or something else is wrong.</p>
<p>If save the scene into an .mrb file before you hit “Apply” in “Grow from seeds”, upload the file somewhere, and post the link here then I can have a look.</p>

---

## Post #10 by @bhowmisp (2022-04-16 01:44 UTC)

<p>Thanks for your help! I appreciate it!</p>
<p>I think something else is wrong, I am using a work station so the machine shouldn’t be an issue.</p>
<p>Here is the link of the .mrb file:</p>
<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/14JjFbUFtPWa1u_sShtTf3UTZdH4-_eTz/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/14JjFbUFtPWa1u_sShtTf3UTZdH4-_eTz/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/14JjFbUFtPWa1u_sShtTf3UTZdH4-_eTz/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/14JjFbUFtPWa1u_sShtTf3UTZdH4-_eTz/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">2022-04-12-Scene.mrb</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Please let me know.</p>

---

## Post #11 by @DIV (2022-04-18 06:49 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="22957">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Grow from seeds may take up to a few ten seconds for large images.</p>
</blockquote>
</aside>
<p>Is there also an effect of the number of seeds (either number of seed ‘blobs’ or number of seed voxels)?<br>
I have tried <em>3D Slicer</em>’s grow-from-seeds functionality before, in a previous version of <em>3D Slicer</em>.  It was indeed slower (despite running on a fast workstation with plenty of RAM), and I suspected it was because I kept adding more seeds to try to get a satisfactory result.  (Sadly, I never got a satisfactory result with that scan!)</p>
<p>—DIV</p>

---
