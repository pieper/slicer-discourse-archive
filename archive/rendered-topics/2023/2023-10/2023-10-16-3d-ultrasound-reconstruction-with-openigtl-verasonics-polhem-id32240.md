# 3D Ultrasound Reconstruction with openIGTL (Verasonics & Polhemus)

**Topic ID**: 32240
**Date**: 2023-10-16
**URL**: https://discourse.slicer.org/t/3d-ultrasound-reconstruction-with-openigtl-verasonics-polhemus/32240

---

## Post #1 by @ehdrmfdl3648 (2023-10-16 07:57 UTC)

<p>US img: Verasonics 64 LE<br>
Position Sensor: Polhemus EMT Sensor</p>
<p>Here’s what’s going on</p>
<ol>
<li>
<p>made Verasonics’ images available for import in Python.</p>
</li>
<li>
<p>the values of the EMT sensor were imported into Python and a transform matrix was created.</p>
</li>
<li>
<p>successfully sent a random image and transform matrix to 3d slicer (using openIGTL).</p>
</li>
<li>
<p>We can now visualize the random image in real-time at the location. (Volume Rendering)</p>
</li>
</ol>
<p>Here are the results so far<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/771c4b6a90bbb2b74227fd95a5b11f59e89a2343.png" data-download-href="/uploads/short-url/gZHrgS6Hn8pRTBqvk7Pdh8xreRZ.png?dl=1" title="dassafa" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/771c4b6a90bbb2b74227fd95a5b11f59e89a2343_2_690x254.png" alt="dassafa" data-base62-sha1="gZHrgS6Hn8pRTBqvk7Pdh8xreRZ" width="690" height="254" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/771c4b6a90bbb2b74227fd95a5b11f59e89a2343_2_690x254.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/771c4b6a90bbb2b74227fd95a5b11f59e89a2343_2_1035x381.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/771c4b6a90bbb2b74227fd95a5b11f59e89a2343.png 2x" data-dominant-color="6A6981"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">dassafa</span><span class="informations">1319×486 64.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The result above is a random image I created for a simple experiment, floating in a random space.</p>
<p>By keeping the image the same and varying the transform matrix at 1s intervals, I was able to see the slices move in 3D space.</p>
<p>However, what I want is for the updated slices to continue to stack.</p>
<p>Currently, when a second slice is entered, the first one disappears.</p>
<p>That is, the update is made.</p>
<p>I want the slices to continue to accumulate.</p>
<hr>
<p>PLUS is difficult to use because it does not support verasonics devices (I think).</p>
<hr>
<p>I Googled a lot of different combinations of words, but never found a clear answer.</p>
<p>However, I’ve seen a few people struggle with loading data from verasonics and polhemus.</p>
<p>If this is you, I can help.<br>
Contact me at <a href="mailto:gu_hong3648@naver.com">gu_hong3648@naver.com</a> and I’ll help you out.</p>

---

## Post #2 by @lassoan (2023-10-16 18:15 UTC)

<p>I would recommend to use the <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#view-data">“Show slice in 3D views” button (eye icon)</a> to display the image slice in 3D instead of using volume rendering for a single slice. Volume rendering is much more expensive and more difficult to display an opaque image.</p>
<p>You can use volume reconstruction module of SlicerIGT extension to “stack” (it is much more complex than that, as images may be oriented arbitrarily) the images into a 3D volume. See step-by-step instructions in <a href="http://www.slicerigt.org/wp/user-tutorial/">SlicerIGT Tutorial</a> U-34.</p>
<p>Note that the diagonal line (and the gray area at the bottom of the image) indicates that you have not set a correct image width in the OpenIGTLink image header.</p>

---

## Post #3 by @ehdrmfdl3648 (2023-10-17 02:46 UTC)

<p>i got it!<br>
i love you<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a8b643039b1d224964c0447ce7ea4626a4f258c.jpeg" data-download-href="/uploads/short-url/aDrYBe6Y302eMGWH13ah6vdwk1e.jpeg?dl=1" title="sadsdadsa.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a8b643039b1d224964c0447ce7ea4626a4f258c_2_690x281.jpeg" alt="sadsdadsa.PNG" data-base62-sha1="aDrYBe6Y302eMGWH13ah6vdwk1e" width="690" height="281" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a8b643039b1d224964c0447ce7ea4626a4f258c_2_690x281.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a8b643039b1d224964c0447ce7ea4626a4f258c_2_1035x421.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a8b643039b1d224964c0447ce7ea4626a4f258c_2_1380x562.jpeg 2x" data-dominant-color="949399"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">sadsdadsa.PNG</span><span class="informations">1915×780 206 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2023-10-17 03:42 UTC)

<p>Great! You may consider writing a <a href="https://discourse.slicer.org/c/community/success-stories/29">“Success story”</a> topic about this (just a few sentences and the image that you included above).</p>

---

## Post #5 by @jslalu (2024-02-20 08:23 UTC)

<p>Hi, can I use Polhemus EM trackers in SlicerIGT?</p>

---

## Post #6 by @lassoan (2024-02-20 21:06 UTC)

<p>As far as I know, the situation is still the same as described here:</p>
<aside class="quote quote-modified" data-post="6" data-topic="7056">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/track-images-using-polhemus-fastrak-electromagnetic-tracker/7056/6">Track images using Polhemus Fastrak electromagnetic tracker</a> <a class="badge-category__wrapper " href="/c/support/feature-requests/9"><span data-category-id="9" style="--category-badge-color: #F1592A; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #3AB54A;" data-parent-category-id="11" data-drop-close="true" class="badge-category --has-parent" title="This category is for submitting ideas about what enhancements or new features should be added to 3D Slicer. Make your voice heard by voting on feature requests - by opening the topic and clicking the Vote button or by creating a new topics. Slicer developers will make it a priority to work on feature requests that have more votes."><span class="badge-category__name">Feature requests</span></span></a>
  </div>
  <blockquote>
    I’m not aware of an OpenIGTLink interface for Polhemus. Since cost of development, testing, optimization, maintenance, and support of a new interface would be higher than the cost of an already supported electromagnetic tracker (such as NDI Aurora or Ascension), probably most people end up buying an already supported tracker instead. Surgical navigation users may also end up choosing NDI instead of Polhemus, because NDI appears to be used in many more clinical products. 
If somebody already has …
  </blockquote>
</aside>


---

## Post #7 by @jslalu (2024-02-21 01:49 UTC)

<p>Thanks for the reply. But I wonder, since we already have a Polhemus tracker, is it possible to implement an OpenIGTLink interface for Polhemus ourselves? Is there a guide for doing this?</p>

---

## Post #8 by @lassoan (2024-02-21 19:49 UTC)

<p>A quick&amp;dirty bridge can be put together in Python, which converts Polhemus VRPN messages (received by some VRPN Python package) to OpenIGTLink messages (sent by <a href="https://github.com/lassoan/pyigtl">pyigtl</a>).</p>

---

## Post #9 by @jslalu (2024-02-22 00:59 UTC)

<p>Thanks. Is there any documentation on the definition of the sequence metafile, or any API for programmatically constructing a sequence metafile? We want to write ultrasound images and their corresponding tracker data into a single sequence metafile so that we can VolumeReconstructor command in Plus to reconstruct a 3D image.</p>

---
