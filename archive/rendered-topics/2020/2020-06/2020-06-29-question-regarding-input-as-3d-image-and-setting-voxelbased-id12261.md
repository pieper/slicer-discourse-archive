# Question regarding input as 3D image and setting voxelbased = False

**Topic ID**: 12261
**Date**: 2020-06-29
**URL**: https://discourse.slicer.org/t/question-regarding-input-as-3d-image-and-setting-voxelbased-false/12261

---

## Post #1 by @Haoxin_Zheng (2020-06-29 01:17 UTC)

<p>Hi,</p>
<p>I think I just asked 2 related question but I wish I could get answers from your side both if possible.</p>
<p>Im dealing with 2D MRI images. For each patient, the resolution in x-y direction is higher than the z direction, which means it is a very common case – a stack of 2D images for each patient. When I input a stack of the 2D images (seen as 3D image, ) and it’s corresponding stack of 2D mask image (seen as 3D mask image) to the “.execute” function, for example:</p>
<p>result_vec = extractor.execute(curr_img_path, curr_mask_path, voxelBased=True/False)</p>
<p>Here, curr_img_path is the path to the 3D image (.nrrd format) and the curr_mask_path is the path to the 3D mask image (.nrrd format).</p>
<p>If I set voxelBased=True, then the returned result_vec is a set of 3D images with respect to each radiomics features, but if I set voxelBased=False, the retured result_vec is a feature vector that for each feature there is a corresponding scalar value.</p>
<p>My quesion:</p>
<ol>
<li>
<p>If I’d like to calculate the radiomics feature for the entire 3D image as a whole, e.g. I want the firstorder_10Percentile feature for this 3D image, do I need to set voxelBased = True? Or False?</p>
</li>
<li>
<p>If I set Voxelbased = True, what do the returned 3D feature maps mean?</p>
</li>
</ol>
<p>Thanks!</p>

---

## Post #2 by @JoostJM (2020-06-30 10:46 UTC)

<p>Addressed in PyRadiomics issue <a href="https://github.com/Radiomics/pyradiomics/issues/600">#600</a>.</p>

---

## Post #3 by @JoostJM (2020-06-30 10:46 UTC)



---
