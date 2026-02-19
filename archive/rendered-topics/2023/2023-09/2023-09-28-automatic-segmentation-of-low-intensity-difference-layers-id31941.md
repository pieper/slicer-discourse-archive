---
topic_id: 31941
title: "Automatic Segmentation Of Low Intensity Difference Layers"
date: 2023-09-28
url: https://discourse.slicer.org/t/31941
---

# Automatic segmentation of low intensity-difference layers

**Topic ID**: 31941
**Date**: 2023-09-28
**URL**: https://discourse.slicer.org/t/automatic-segmentation-of-low-intensity-difference-layers/31941

---

## Post #1 by @Windy (2023-09-28 02:36 UTC)

<p>Hi,</p>
<p>I have an image dataset where the color intensity difference of classes in an image is pretty much similar (example given below, contains 4 layers of muscle, hence 4 classes). I tried many semiautomatic algorithms like grow from seed, flood fill, watershed, etc., but none of them worked well for me. So what I do now is fill in between slices, but I have to do this at least every 20 slices to get a fairly good segmentation. My datasets are large, but if they are downsampled, lots of helpful details are lost. I also have at least 30 datasets like that. So repeating the fill-in between slices is tedious. If you have any advice or suggestions, I would be really grateful.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/608827d5f8cbb7480e4991ed1a3848d3ef2de2fa.jpeg" data-download-href="/uploads/short-url/dLXy39YucLDsrg5qvHtqjSKNNbQ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/608827d5f8cbb7480e4991ed1a3848d3ef2de2fa_2_415x500.jpeg" alt="image" data-base62-sha1="dLXy39YucLDsrg5qvHtqjSKNNbQ" width="415" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/608827d5f8cbb7480e4991ed1a3848d3ef2de2fa_2_415x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/608827d5f8cbb7480e4991ed1a3848d3ef2de2fa.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/608827d5f8cbb7480e4991ed1a3848d3ef2de2fa.jpeg 2x" data-dominant-color="333333"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">564×678 36.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00255ca44d4b51aa6882d7f359e4734b2669f072.jpeg" data-download-href="/uploads/short-url/1i2WrMV1hVWyG8zkhNn6KCncqe.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00255ca44d4b51aa6882d7f359e4734b2669f072_2_351x375.jpeg" alt="image" data-base62-sha1="1i2WrMV1hVWyG8zkhNn6KCncqe" width="351" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00255ca44d4b51aa6882d7f359e4734b2669f072_2_351x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00255ca44d4b51aa6882d7f359e4734b2669f072_2_526x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00255ca44d4b51aa6882d7f359e4734b2669f072_2_702x750.jpeg 2x" data-dominant-color="413F39"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">777×828 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2023-09-28 02:39 UTC)

<p>Can you show a few segmented slices so that we can see what structures you need to separate?</p>

---

## Post #3 by @Windy (2023-09-28 03:31 UTC)

<p>Updated the question with segmentation</p>

---

## Post #4 by @muratmaga (2023-09-28 15:49 UTC)

<p>until <a class="mention" href="/u/lassoan">@lassoan</a> provides more complete answer here are my thoughts</p>
<p>So grow from the seed should work well for yellow and blue boundary, as well as brown structure, if you apply an intensity masking along with it.</p>
<p>yellow green boundary is a lot more challenging, because I can’t see a feature that separates them in the lower right corner.</p>
<p>When you say grow from the seeds didnt work, how extensive seeding have you done? For example have you tried growth from the seed after you painted every 20 slice (like you are doing for fill between the slices).</p>
<p>Nowadays, deep learning can be solution for this type of challenging segmentations, but you do need some segmented data to start training a model.</p>

---

## Post #5 by @lassoan (2023-09-28 16:03 UTC)

<p>I agree, “Grow from seeds” should work, the only question is how much work it takes to provide sufficient seeds. If you need to paint a lot then “Fill between slices” may be more efficient.</p>
<p>You can make the segmentation workflow much faster by first segmenting all the muscles and recolor parts of that segment (using Masking settings / Editable area).</p>
<p>I agree that nowadays you would train a neural network to automate this. However, if you only have 30 images than that may be just enough to train the network. You can try setting up MONAILabel extension or an nn-Unet training and maybe you would get usable results after 10-20 segmentation cases, so you could save some time and get some experience with AI segmentation.</p>

---

## Post #6 by @Windy (2023-09-29 01:17 UTC)

<p>Thank you <a class="mention" href="/u/muratmaga">@muratmaga</a> and <a class="mention" href="/u/lassoan">@lassoan</a>. I will try the MONAILabel extension as well</p>

---
