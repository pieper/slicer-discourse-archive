---
topic_id: 32036
title: "More Precision Of Totalsegmentator"
date: 2023-10-04
url: https://discourse.slicer.org/t/32036
---

# More precision of TotalSegmentator?

**Topic ID**: 32036
**Date**: 2023-10-04
**URL**: https://discourse.slicer.org/t/more-precision-of-totalsegmentator/32036

---

## Post #1 by @zariliusra (2023-10-04 17:06 UTC)

<p>Hi,<br>
Is there some way to get better resolution when using TotalSegmentator (less than the default resolution of 1.5mm)? Or is there any other program?</p>

---

## Post #2 by @pieper (2023-10-04 19:04 UTC)

<p>I believe the MONAI Label full body CT model trained on the TotalSegmentator data operates at native CT resolution.  <a class="mention" href="/u/diazandr3s">@diazandr3s</a> should be able to say for sure.</p>

---

## Post #3 by @diazandr3s (2023-10-04 22:35 UTC)

<p>Thanks for the ping, <a class="mention" href="/u/pieper">@pieper</a>.</p>
<p><a class="mention" href="/u/zariliusra">@zariliusra</a> this is a good question. The original resolution of the TotalSegmentator dataset is 1.5mm. You could potentially resample volumes and labels to better resolution, but that will modify the labels and might need to be rechecked by an expert again.</p>
<p>Copied from the TotalSegmentator paper (Page 3, first paragraph):</p>
<blockquote>
<p>All images were resampled to 1.5 mm isotropic resolution.</p>
</blockquote>
<p>MONAI model was trained at 2 resolutions: original (1.5mm) and low resolution (3mm) <a href="https://github.com/Project-MONAI/model-zoo/tree/dev/models/wholeBody_ct_segmentation#high-resolution-and-low-resolution-models" rel="noopener nofollow ugc">https://github.com/Project-MONAI/model-zoo/tree/dev/models/wholeBody_ct_segmentation#high-resolution-and-low-resolution-models</a></p>
<p>Here you see the spacing set for those two models: <a href="https://github.com/Project-MONAI/model-zoo/blob/dev/models/wholeBody_ct_segmentation/configs/inference.json#L16" rel="noopener nofollow ugc">https://github.com/Project-MONAI/model-zoo/blob/dev/models/wholeBody_ct_segmentation/configs/inference.json#L16</a></p>

---

## Post #4 by @rbumm (2023-10-08 23:08 UTC)

<p>So the answer to the good question is - No - without complete new training and investing in better hardware? This is an important topic because the resolution is borderline.</p>

---

## Post #5 by @diazandr3s (2023-10-09 11:04 UTC)

<p>Hi <a class="mention" href="/u/rbumm">@rbumm</a>,</p>
<p>I agree. The TotalSegmentator dataset’s resolution is borderline and a limitation to accurately segmenting tumours and/or small organs. Many CT volumes in real scenarios are 1mm or even bigger (i.e. 0.8mm, 0.4mm).</p>
<p>If we want to train a model using a dataset with a bigger resolution (1mm, 0.8mm, etc.), we’ll need more computing resources to have one model segmenting all segments at once OR train multiple models segmenting fewer segments (10 segments per model)</p>
<p>If we have a verified upsampled dataset, we can retrain the MONAI Label models - no need to start from scratch.</p>
<p>Hope this makes sense.</p>

---

## Post #6 by @mangotee (2023-10-09 13:26 UTC)

<p>I also agree, the main limitation is the dataset’s current resolution. With a higher-res dataset, one could train a higher-res model. Of course, that would benefit from better compute, especially memory: a 32-bit float volume at 512x512x512 and 104 regions requires ~52 GB VRAM just to hold the inference result - alternatively, one could split the labels (as Andres said, and as it was done with nnunet on TotalSegmentator v1).</p>
<p>The TotalSegmentator dataset is an amazing resource, I think it might be even repurposed to create a high-res model, at least to <em>pre-train</em> it. My take on this:</p>
<ul>
<li><strong>High-quality image upsampling:</strong> (e.g. from 1.5mm to e.g. 1mm or even more). For interpolation, one could use at least bicubic or Lanczos, perhaps even deep learning superresolution (not sure whether there is a robust model out there).</li>
<li><strong>High-quality label upsampling:</strong>  Instead of using nearest-neighbor interpolation to upsample the labelmaps, I would recommend using SimpleITK with the interpolator <a href="https://itk.org/Doxygen/html/classitk_1_1LabelImageGaussianInterpolateImageFunction.html" rel="noopener nofollow ugc"><code>sitkLabelGaussian</code></a> - for me, this always works wonders compared nearest-neighbors.</li>
</ul>
<p>Something like <a href="https://gist.github.com/mrajchl/ccbd5ed12eb68e0c1afc5da116af614a" rel="noopener nofollow ugc">this function</a>, but replacing the <code>sitkNearestNeighbor</code> interpolator for labels to:</p>
<pre><code class="lang-python">def resample_img(itk_image, out_spacing=[1.0, 1.0, 1.0], is_label=False):
    resample = sitk.ResampleImageFilter()
    resample.SetOutputSpacing(out_spacing)
    ...
    if is_label:
        resample.SetInterpolator(sitk.sitkLabelGaussian)
    ...
</code></pre>
<p>It would probably be best to run such pre-processing once to create a HD version of the TotalSegmentator dataset. To train e.g. a model at 1mm^3 resolution, the network input of the <a href="https://github.com/Project-MONAI/model-zoo/tree/dev/models/wholeBody_ct_segmentation" rel="noopener nofollow ugc">wholeBody_ct_segmentation</a> model in the Model Zoo would need to be increased from 96x96x96 to 144x144x144. That is a lot (especially for 105+ output labels), but not impossible with current GPUs.</p>
<p>But training at this scale is easier said than done. Just out of curiosity, what image resolution would be a good “aim”? Are large-FOV CT scans often done at 0.4mm or even 0.8mm?? Would 1mm be a good target resolution?</p>

---

## Post #7 by @lassoan (2023-10-09 14:08 UTC)

<p>For most use cases, the 1.5mm resolution of the segmentation is good enough. You often have to work with lower-resolution input images anyway. Discussion about improving the resolution only makes sense if you have a specific goal in mind, as creating perfect segmentations (that are suitable for every possible applications) is impossible. What is your clinical application?</p>
<p>Note that if the goal is to just to create nicer visualization then surface rendering is probably not a good approach anyway. Segmentation-enhanced volume rendering has much bigger potential for visualization - see for example in <a href="https://discourse.slicer.org/t/vtk-multivolume-cinematic-volume-rendering/31981/12">this topic</a>.</p>

---
