# Normalization question

**Topic ID**: 14759
**Date**: 2020-11-24
**URL**: https://discourse.slicer.org/t/normalization-question/14759

---

## Post #1 by @mcastro (2020-11-24 16:43 UTC)

<p>I am performing 3D organ-based radiomics analysis and I have a few questions about normalization.</p>
<p>Let’s call:<br>
A the original image<br>
Bj the image where the organ was masked and the background was set to a value j<br>
Bk the image where the organ was masked and the background was set to a value k</p>
<p>Radiomics features are different when I use the A and Bj. This is because the normalization process uses all information from the image, not only the segmentation. So, this is ok.</p>
<p>Furthermore, if I do not normalize, the feature values remain the same when I use A and Bj. This is because information only from the segmentation is used. So, this is ok too.</p>
<p>However, if I set a different background in the image Bk, the radiomics features remain the same as in Bj. This is what I do not understand. I may assume that the only way radiomics features in Bj and Bk are the same is if PyRadiomics detects that this is a background and ignores it. In this case, the image is normalized, but using only the information from the segmentation, not the background.</p>
<p>Is that correct?</p>

---

## Post #2 by @JoostJM (2020-11-26 16:52 UTC)

<p>Not entirely. Normalization in PyRadiomics calculates the mean and standard deviation on the entire image, which are then used to make a zero mean, unit deviation normalization. The main reason for the similar feature values I can think of is that the background constitutes a very large volume, compared to the masked area. In that sense, the mean will most likely apporach the value set for your background value, and the standard deviation is only small, and mainly controlled by the area inside the ROI.</p>
<p>This results in the nomalization division being comparable (=standard deviation), and the only difference beteen Bj and Bk being the offset (=mean). That offset is not visible in the larger part of extracted features, due to gray value discretization (which removes the effect of the offset). You can check this by reviewing the diagnostic features, they also give information regarding the entire image.</p>
<p>That said, it’s best to not set the background in the image to some particular value. Identification of the ROI is what your mask is for. Setting the background in the image defeats some assumptions in the definition of normalization (by setting the background, it indirectly becomes dependent on the mask, which is what you are trying to avoid when normalizing).</p>

---
