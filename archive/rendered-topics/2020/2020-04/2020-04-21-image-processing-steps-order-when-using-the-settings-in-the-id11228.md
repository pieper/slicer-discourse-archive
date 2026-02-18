# Image processing steps order when using the settings in the parameter file?

**Topic ID**: 11228
**Date**: 2020-04-21
**URL**: https://discourse.slicer.org/t/image-processing-steps-order-when-using-the-settings-in-the-parameter-file/11228

---

## Post #1 by @radio5 (2020-04-21 15:18 UTC)

<p>Hi!<br>
After I have cropped images to their tumour masks, I am aiming to:</p>
<ul>
<li>Resize all images to a specific image resolution</li>
<li>Normalize image intensities</li>
<li>Discretize images (Binning)</li>
</ul>
<p>However, I do not know what is the correct order or, simply, what is the order that pyRadiomics applies when all these steps are implicitly “required” through specification of their settings in the parameter file.</p>
<p>Thank you in advance for your time!</p>

---

## Post #2 by @JoostJM (2020-04-27 15:52 UTC)

<p>The order forced in PyRadiomics is:</p>
<ol>
<li>Normalization (using Z-score)</li>
<li>Resampling the spacing (resolution)</li>
<li>Discretizing the gray values (only when calculating texture features and firstorder Uniformity and Entropy)</li>
</ol>

---

## Post #3 by @radio5 (2020-04-27 17:10 UTC)

<p>Thank you for your reply <a class="mention" href="/u/joostjm">@JoostJM</a>; Why should one normalize before resampling? What is the rationale behind it? I would like to hear your opinion on this, as I am not sure which order should be best, I’ve read that resampling should be first. Thank you!</p>

---

## Post #4 by @JoostJM (2020-06-30 10:32 UTC)

<p>Normalization is applied to reduce systemic differences between different vendors. In short, to increase the repeatability of features and make them more robust against variations due to image acquistion. We do this before resampling, as resampling also partially crops the image around the mask (much more computationally efficient, especially in large images with small masks). normalizing the cropped area makes the normalization dependent on the location and size of the mask, introducing unwanted noise. Therefore we normalize before resampling.</p>
<p>I’m not entirely sure what the rationale would be for normalizing after resampling, other than that it would entail images of the same pixel spacing and therefore more comparable. IMHO that difference is less than the difference introduced due to cropping.</p>

---
