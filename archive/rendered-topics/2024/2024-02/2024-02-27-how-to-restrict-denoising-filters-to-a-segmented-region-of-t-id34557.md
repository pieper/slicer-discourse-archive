# How to restrict denoising filters to a segmented region of the VOI

**Topic ID**: 34557
**Date**: 2024-02-27
**URL**: https://discourse.slicer.org/t/how-to-restrict-denoising-filters-to-a-segmented-region-of-the-voi/34557

---

## Post #1 by @rsanaei (2024-02-27 00:23 UTC)

<p>Hi,</p>
<p>I am working with uCT images of metal lattices trying to quantify bone ingrowth. Due to the presence of metal, there is some noise which makes selection of the bone tissue using the threshold function challenging. There are more than 900 images in each dataset with a lot of spacial complexity so manual tracing or painting is impossible. Applying a median or gaussian filter generally helps but applying them globally also blurs the metal edges introducing more noise within the close vicinity of metal bits.</p>
<p>I am wondering if the denoising filters can be applied to a segmented region. If so, I can threshold the metal and apply the filter to the non-metal regions which I am hoping can help with later thresholding of bone.</p>
<p>Best,</p>
<p>Reza</p>

---

## Post #2 by @muratmaga (2024-02-27 02:45 UTC)

<p>There are median and gaussian filters for segments. You can threshold, use island tool to remove small artifacts (remove small islands option), and then use the median filter to create a smoothened labelmap. THen you can use the MaskVolume to extract only what’s inside the segment.</p>
<p>Is that close to what you want to do?</p>

---

## Post #3 by @rsanaei (2024-02-27 12:55 UTC)

<p>Thank you for your response. When you say ‘there are Gaussian and median filters for segments’, what do you mean exactly? Within which module should I find those? The standard ones I see from the denoising menu do not have that option.<br>
Re the latter part of your suggestion, how do you extract a part of a volume using mask volume? Apologies as I am not that experienced with 3D slicer.<br>
Cheers, R</p>

---

## Post #4 by @lassoan (2024-02-27 14:15 UTC)

<p>Most likely classic smoothing and denoising filters cannot remove such complex noise as metal artifacts in CT. However, if you segment a few dozen CTs manually then you can use them to train an nn-UNet or MONAI Auto3DSeg model that should be able to provide an accurate bone segmentation from the noisy images. Depending on complexity of the task and variability of the images, you may need to increase the size of the training data set (e.g., by manually correcting imperfections in the automatic segmentation results), but eventually you will reach a point when automatic segmentation provides results that are good enough for your purposes.</p>

---

## Post #5 by @muratmaga (2024-02-27 16:46 UTC)

<aside class="quote no-group" data-username="rsanaei" data-post="3" data-topic="34557">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rsanaei/48/66727_2.png" class="avatar"> rsanaei:</div>
<blockquote>
<p>‘there are Gaussian and median filters for segments’, what</p>
</blockquote>
</aside>
<p>Those are available in the Segment Editor module, during segmentation. Under the effect callled Smoothing.</p>
<p>MaskVolume is also another effect inside the Segment Editor.</p>

---

## Post #6 by @rsanaei (2024-02-28 05:58 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="34557">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>use them to train an nn-UNet or MONAI Auto3DSeg model that should be able to provide an accurate bone segm</p>
</blockquote>
</aside>
<p>Thanks Andras. I am interested in trying that, however, at this point, it is really hard to do that even manually for a few of the datasets especially with no filtering. I am hoping that if I could exclude (subtract) the metal parts from the volumes, and run the median filter afterwards, part of the problem will be solved. Preferrably, I don’t want to replace the metal segment with a black fill if possible - which I now know I can do based on <a class="mention" href="/u/muratmaga">@muratmaga</a>’s suggestion; that will result in its own error when applying the filter as it will use the black filled pixels to filter the margins. Rather, I would like to be able to run the filter in a smart way such that it automatically doesn’t apply it to the metal segment. Is there a way of doing that?</p>
<p>Acquisition is not a factor by the way - I have tried different energy parameters and it won’t get any better.</p>

---

## Post #7 by @rsanaei (2024-02-28 05:59 UTC)

<p>Thanks very much for your suggestions. I am going to give MaskVolume a try and see whether I can mix it up with Andras’s nn method.</p>

---
