# Voxel-based extraction depends on mask

**Topic ID**: 10709
**Date**: 2020-03-16
**URL**: https://discourse.slicer.org/t/voxel-based-extraction-depends-on-mask/10709

---

## Post #1 by @geraghbj (2020-03-16 21:44 UTC)

<p>I have a case where there are multiple ROIs representing multiple lesions from a brain metastasis patient. Running a voxel-based extraction on two of these ROIs independently provides different answers than when I extract features on a combined ROI of the two lesions, then separate it after. This is very disturbing.</p>
<p>This tells me that the voxel-based extraction is not localized, and will always depend on what’s going on in other voxels. I’d like to train a classifier based on the values from individual voxels, but the pipeline used to extract these voxels i.e. combined ROI or individual, makes the classifier invalid.</p>
<p>I’m currently attempting to simply extract features across the entire brain, from which I’ll collect from the appropriate ROIs later… but it seems like this is going to be prohibitively slow.</p>
<p>How can I extract feature maps without the values in one voxel being determined by distant values? Is the voxel-based extraction local? what does the kernel size mean if this test-case fails?</p>
<p>Thank you,<br>
Benjamin</p>

---

## Post #2 by @JoostJM (2020-03-17 13:18 UTC)

<p>There are 2 reasons for the behaviour you’re describing, and both occur only when you use a masked kernel (values for a voxel are calculated on a region surrounding the voxel: the kernel. A masked kernel is is the intersection between the region surrounding the voxel, and the original mask: i.e. part of the mask that surrounds the voxel).</p>
<p>Reason 1: some voxels are exluded when they are not in the mask<br>
Reason 2: image discretization is done on a global (image) level. When using a masked kernel, this is done on the masked region. If unmasked kernels are used, the entire image is discretized.</p>
<p>If you want to have similar results, try using unmasked kernels (parameter “maskedKernel” = False)</p>

---

## Post #3 by @JoostJM (2020-03-17 13:21 UTC)

<p>As to speed: Keep in mind that voxel-based radiomics is like doing segment-based radiomics, but for each voxel separately. So yes, in case of large regions, this will indeed be very slow. I tried to enhance performance by computing ‘batches’ of voxels (allowing more matrix calculations in python, reducing the number of python loops), and improving the iteration algorithm when calculating the texture matrices. While this certainly improves the performance, it still remains a fairly slow process.</p>

---

## Post #4 by @geraghbj (2020-03-17 14:35 UTC)

<p>Thank you for your quick response, Joost.</p>
<p>I suspected that maskedKernel would be involved and I was already playing around with it before sending a message since it didn’t seem to solve the problem. Consider the following output:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1c59643d53ef4155c365d69fbd32fadb587c3f1.png" data-download-href="/uploads/short-url/yuOoHTaKkQ6IOGSfLxib2MYxGY9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1c59643d53ef4155c365d69fbd32fadb587c3f1.png" alt="image" data-base62-sha1="yuOoHTaKkQ6IOGSfLxib2MYxGY9" width="690" height="431" data-dominant-color="FAFAFA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1566×980 11.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This data set has 7 contoured lesions, so in this analysis, I’m only considering the first lesion alone in a single segment vs the first lesion and the 7th lesion combined into a single segment. I ran the voxel-based feature extraction on both cases and then considered the value of a single pixel that originated from the FIRST segment. There were four runs:</p>
<ol>
<li>roi 1 alone, maskedKernel = True</li>
<li>roi 1 + roi 7, maskedKernel = True</li>
<li>roi 1 alone, maskedKernel = False</li>
<li>roi 1 + roi 7, maskedKernel = False</li>
</ol>
<p>As far as I can tell, the values depend on the segment fed into it, regardless of maskedKernel being true or false.</p>
<p>It would be ideal to first perform discretization globally across the unmasked image, and then compute features across local regions, using the pre-computed discretization bins.</p>
<p>Perhaps I’m misunderstanding. Wouldn’t you expect this test-case to return the same values for a pixel in region 1 IF maskedKernel = false, regardless of the segment size/shape i.e. regardless of whether a combined ROI is used vs a single ROI?</p>
<p>Thank you,<br>
Benjamin</p>

---

## Post #5 by @geraghbj (2020-03-17 17:23 UTC)

<p>I think I might have tracked down the issue. In base.py, it appears the self.InputImage has already been clipped to the bounding box of the segment. The logic checks maskedKernel and will perform binning on the masked region if maskedKernel == True; otherwise, it will create a mask that is the size of the <strong>bounding box</strong>.</p>
<p>Perhaps a clumsy workaround will be to set the corner voxels in the mask to 1. I will try and see if this fixes my problem.</p>

---

## Post #6 by @geraghbj (2020-03-17 17:50 UTC)

<p>This workaround solved my problem. The feature values are now consistent whether or not a single or combined ROI was used.</p>

---
