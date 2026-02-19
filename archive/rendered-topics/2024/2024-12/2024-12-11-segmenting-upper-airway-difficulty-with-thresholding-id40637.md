---
topic_id: 40637
title: "Segmenting Upper Airway Difficulty With Thresholding"
date: 2024-12-11
url: https://discourse.slicer.org/t/40637
---

# Segmenting upper airway, difficulty with thresholding

**Topic ID**: 40637
**Date**: 2024-12-11
**URL**: https://discourse.slicer.org/t/segmenting-upper-airway-difficulty-with-thresholding/40637

---

## Post #1 by @dcg494 (2024-12-11 16:31 UTC)

<p>Hi all,</p>
<p>I’m trying to segment the upper airway but having difficulties as the thresholds I’ve been trying out either a) don’t capture all the air (as in the picture of the nasal cavity in green), or b) capture too much of the surrounding tissue (picture in yellow).</p>
<p>I’ve tried increasing the spacing using crop volume, and different methods of segmenting (starting with air and using operators to extract, and wrapsolidify to get the internal surface of the surrounding tissue).</p>
<p>Anything i can do to more accurately capture the air ?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f72273b8517b276810fb303552ce06fcd60b80b5.jpeg" data-download-href="/uploads/short-url/zgfKoBKIWcVYnQN3voiXKS8rJtj.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f72273b8517b276810fb303552ce06fcd60b80b5_2_440x500.jpeg" alt="image" data-base62-sha1="zgfKoBKIWcVYnQN3voiXKS8rJtj" width="440" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f72273b8517b276810fb303552ce06fcd60b80b5_2_440x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f72273b8517b276810fb303552ce06fcd60b80b5_2_660x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f72273b8517b276810fb303552ce06fcd60b80b5_2_880x1000.jpeg 2x" data-dominant-color="303530"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1047×1188 142 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/504d7e9b1a76d1b1df2f0f8a6201d0346fc53a54.jpeg" data-download-href="/uploads/short-url/bsoec5NLFjKFwGQOGZVUPkbYexe.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/504d7e9b1a76d1b1df2f0f8a6201d0346fc53a54_2_462x500.jpeg" alt="image" data-base62-sha1="bsoec5NLFjKFwGQOGZVUPkbYexe" width="462" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/504d7e9b1a76d1b1df2f0f8a6201d0346fc53a54_2_462x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/504d7e9b1a76d1b1df2f0f8a6201d0346fc53a54_2_693x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/504d7e9b1a76d1b1df2f0f8a6201d0346fc53a54_2_924x1000.jpeg 2x" data-dominant-color="817659"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1077×1165 191 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Esteban_Barreiro (2024-12-12 11:37 UTC)

<p>Maybe you can try to add the regions you need with “Use for Masking”, in the Threshold effect, adding the value you need to obtain, activating the Sphere Brush, and simply paint those little spaces. Is an easy way to do fine work just painting over. It will only let you paint the values you need and nothing else.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9ea804bf377800e1c347eaf9c066dd93a68284a3.png" data-download-href="/uploads/short-url/mDxpWk5GDc8CEMOHFarssT1Spft.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9ea804bf377800e1c347eaf9c066dd93a68284a3_2_394x500.png" alt="1" data-base62-sha1="mDxpWk5GDc8CEMOHFarssT1Spft" width="394" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9ea804bf377800e1c347eaf9c066dd93a68284a3_2_394x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9ea804bf377800e1c347eaf9c066dd93a68284a3.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9ea804bf377800e1c347eaf9c066dd93a68284a3.png 2x" data-dominant-color="353638"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">444×563 42.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/614c97657c406917555ad0ab696b047e759c9e19.png" data-download-href="/uploads/short-url/dSKptDfQ8D8vfTgQW6sSX5Q5wP7.png?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/614c97657c406917555ad0ab696b047e759c9e19_2_441x500.png" alt="2" data-base62-sha1="dSKptDfQ8D8vfTgQW6sSX5Q5wP7" width="441" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/614c97657c406917555ad0ab696b047e759c9e19_2_441x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/614c97657c406917555ad0ab696b047e759c9e19.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/614c97657c406917555ad0ab696b047e759c9e19.png 2x" data-dominant-color="353638"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">481×545 46.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @muratmaga (2024-12-12 14:35 UTC)

<aside class="quote no-group" data-username="dcg494" data-post="1" data-topic="40637">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/cdc98d/48.png" class="avatar"> dcg494:</div>
<blockquote>
<p>Anything i can do to more accurately capture the air ?</p>
</blockquote>
</aside>
<p>Not sure how well it works, but there is a Airway Segmentation extension in Slicer extension catalog. Did you give that a try?</p>

---

## Post #4 by @Arash1 (2024-12-13 11:08 UTC)

<p>Hello<br>
I would recommend changing the approach to the following instead of using thresholds.</p>
<ol>
<li>Change the volume to Air. So you get a more clear image of air and tissue. There are two presets, lung and air. I would prefer air.</li>
<li>Resampling if needed. For this case, Linear is somewhat more practical. However, others may recommend using a different interpolation. I wouldn’t go anything less than 0.5 and somewhere from 0.5 to .75 seems okay. Try to crop the image to save time and reduce RAM space.</li>
<li>Chest Imaging Platform. You can use CIP to get a segment of tissue and air.<br>
Please consider the fact that if you are resampling, CIP doesn’t work properly and you need to run a linear transform to overlap your segment and image.</li>
<li>If you only need the nasal cavity, use TotalSegmentator. If you have a CUDA-enabled system, consider using it. It will save you lots of time.</li>
</ol>
<p>Please let me know if you need more help with any of these steps.</p>

---

## Post #5 by @dcg494 (2024-12-16 16:50 UTC)

<p>Thanks so much, this is really helpful ! I tried this, and it does a pretty good job, but still not capturing only the airway. Maybe i’m using the wrong segmentation tool under the CIP ? (Interactive lobe segmentation, where i placed fiduciaries for one fissure and then ran the script).</p>
<p>You can see the result in the picture below. The red arrows show to some of the walls inside the nasal cavity that shouldn’t be part of the segment and this blank band in a circle that is somehow missed a few times during the segmentation. Appreciate any tips on this !</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb3834d1691d77a3e2959bdae7cb4e125d69e4e6.jpeg" data-download-href="/uploads/short-url/zQogwGMw1MCuCC115n8uzHsz2se.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb3834d1691d77a3e2959bdae7cb4e125d69e4e6_2_587x500.jpeg" alt="image" data-base62-sha1="zQogwGMw1MCuCC115n8uzHsz2se" width="587" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb3834d1691d77a3e2959bdae7cb4e125d69e4e6_2_587x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb3834d1691d77a3e2959bdae7cb4e125d69e4e6_2_880x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb3834d1691d77a3e2959bdae7cb4e125d69e4e6_2_1174x1000.jpeg 2x" data-dominant-color="313F4E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1221×1039 52.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @Arash1 (2024-12-16 18:59 UTC)

<p>Hello<br>
In the CIP, please use the Simple Lung Mask.<br>
Consider this that most probably the segments you receive will not overlap with your image and you need to use to a Transform to overlap these two. These has already been addressed to <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #7 by @Arash1 (2024-12-16 19:06 UTC)

<p>Just one more thing to add. Getting a very high detail segment of the airway requiring no adjustments is close to impossible. Using these modules and extensions will speed up your process. This from my experience but others might have a solution to this.</p>

---

## Post #8 by @dcg494 (2024-12-20 15:29 UTC)

<p>Thanks a lot Arash, really appreciate the help. You’re definitely right, that it seems i’ll have a lot of manual work left either way. One thing i’ve noticed, and a question, is that resampling doesn’t seem to help with masking / thresholding air. I’ve tried all different settings (spacing scales, interpolator options), but it all seems to end in the same resolution of segmentation. Any thoughts on this ?</p>

---

## Post #9 by @Arash1 (2024-12-28 04:02 UTC)

<p>Probably at normal viewing, there is no difference between a resampled and the original image and if we are just going by the threshold and as the result we are missing the resampled boundaries. That is one possibility.<br>
The other possibility is that when using a big ROI, or the interpolation factor is less than .5 which both of these can increase the processing time and occupied RAM and CPU usage. At times, this big calculation will result in a failed attempt and what you get is the original image just with s new title.<br>
You can monitor this through your Task Manager. DWI will be what you’re looking for.<br>
If you prefer not to use the Extensions and prefer to just go with the thresholds, I would recommend Grow from the seeds. Others have mentioned using the centreline extraction. Personally I haven’t used it.<br>
The other thing is to use the Anisotropic diffusion filters.<br>
Please let me know if I can help further.</p>

---

## Post #10 by @dcg494 (2024-12-29 14:52 UTC)

<p>Thanks so much Arash, super helpful. I’m trying the diffusion filters, do you recommend the gradient or curvature anisotropic diffusion module ? I assume the former ? Any recommendations on the conductance setting (very low?) and number of iterations ?</p>
<p>And regarding your first point, what do you mean by normal viewing ? And more generally, what would be the solution / i.e. what am i able to do to see the difference and to not miss the resampled boundaries ?</p>
<p>Regarding your second point, i checked the error log and one entry says the ‘DWI volume was rescaled without error’ but after that i get the following warning. Do you know if this is relevant at all ?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/1508de2d93802612d57d329ac5a9fa032e286fea.png" data-download-href="/uploads/short-url/3051CPA3rHqZsh0Z1ZsmSLHLe3w.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/1508de2d93802612d57d329ac5a9fa032e286fea.png" alt="image" data-base62-sha1="3051CPA3rHqZsh0Z1ZsmSLHLe3w" width="631" height="275"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">631×275 11.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
