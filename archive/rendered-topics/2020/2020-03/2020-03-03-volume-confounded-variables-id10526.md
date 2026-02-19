---
topic_id: 10526
title: "Volume Confounded Variables"
date: 2020-03-03
url: https://discourse.slicer.org/t/10526
---

# Volume confounded variables

**Topic ID**: 10526
**Date**: 2020-03-03
**URL**: https://discourse.slicer.org/t/volume-confounded-variables/10526

---

## Post #1 by @Martin_Bzr (2020-03-03 18:15 UTC)

<p>Hi,</p>
<p>Thank you for this great toolbox !</p>
<p>As I understood from the docs the ‘_firstorder_Energy’ feature is volume confounded.<br>
What about ‘_ngtdm_Coarseness’ ?</p>
<p>I’m looking at relationships between features and and the size of the ROI and the predictions capacities of this feature are suspiciously good.</p>
<p>Thank you!</p>
<p>Martin</p>

---

## Post #2 by @fedorov (2020-03-03 18:37 UTC)

<p>For the reference, Coarseness is documented here: <a href="https://pyradiomics.readthedocs.io/en/latest/features.html#radiomics.ngtdm.RadiomicsNGTDM.getCoarsenessFeatureValue">https://pyradiomics.readthedocs.io/en/latest/features.html#radiomics.ngtdm.RadiomicsNGTDM.getCoarsenessFeatureValue</a></p>
<p>I think this will depend, but it is not unexpected that larger regions will have more heterogeneity, affecting “spatial rate of change”.</p>
<p>You might want to generate some synthetic examples that have homogeneous regions of increasing size, or regions with the same texture. If coarseness is not constant for those regions, then either I missed something, or there is a problem in the code.</p>

---

## Post #3 by @Martin_Bzr (2020-03-03 20:44 UTC)

<p>Thank you for your answer !<br>
I will run some tests on synthetic example to double check.</p>

---

## Post #4 by @Martin_Bzr (2020-03-03 21:38 UTC)

<p>So I tested on a synthetic image (attached) with 3 ROIs of increasing sizes.<br>
Coarseness for the small, medium and large ROIs were respectively:<br>
0.00117546487955<br>
0.000528825969796<br>
0.000139595116939</p>
<p>Larger the ROI, smaller the values, which is consistent with my findings (T2_FLAIR Brain MRI analysis)<br>
I did not verify yet but it seems that the glrlm and glszm _GrayLevelNonUniformity show also an association with the size of the ROI (Larger the ROI, Larger the values or Larger the ROI smaller the values if you look at GrayLevelNonUniformityNormalized)</p>
<p>Any insight? I have looked at the formulas but I don’t get why I observe that.</p>
<p>( This synthetic image is a modified image of a carpet <img src="https://emoji.discourse-cdn.com/twitter/grin.png?v=12" title=":grin:" class="emoji" alt=":grin:" loading="lazy" width="20" height="20"> )</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/9528be6082f8a01b2c69916edbd1a9aadd32902a.jpeg" data-download-href="/uploads/short-url/lhwr1VIrdtBG9EkjRsLwGT3b1ns.jpeg?dl=1" title="layout_slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9528be6082f8a01b2c69916edbd1a9aadd32902a_2_609x500.jpeg" alt="layout_slicer" data-base62-sha1="lhwr1VIrdtBG9EkjRsLwGT3b1ns" width="609" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9528be6082f8a01b2c69916edbd1a9aadd32902a_2_609x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9528be6082f8a01b2c69916edbd1a9aadd32902a_2_913x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9528be6082f8a01b2c69916edbd1a9aadd32902a_2_1218x1000.jpeg 2x" data-dominant-color="8F8A6F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">layout_slicer</span><span class="informations">1283×1053 512 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @fedorov (2020-03-04 18:11 UTC)

<p>This is an interesting finding that I cannot explain. Thank you for testing this. I don’t have insight as to why this would be though.</p>

---

## Post #6 by @JoostJM (2020-03-10 16:40 UTC)

<p><a class="mention" href="/u/martin_bzr">@Martin_Bzr</a>, good catch! I did not realize this before.</p>
<p>If you look closely at how NGTDM is defined, you can see there is a volume dependency in the calculation of <code>s_i</code> (sum of absolute differences between centervoxel and average of neighborhood). As the image becomes larger, this sum also increases.<br>
In some NGTDM formulas, this is corrected by some use of <code> N_vp</code> (total number of voxels in ROI), but not for Coarseness (and Busyness and Strength). A potential non-volume confound variation on Coarseness would be <code>N_vp / SUM(s_i)</code>, which would reflect the (inverse of the) average of differences between center voxel and neighborhood.</p>
<p>As to GLN for GLRLM and GLSZM, that is very likely, and maybe partly the reason the GLNN formula is also there.</p>

---

## Post #7 by @Martin_Bzr (2020-03-11 13:56 UTC)

<p><a class="mention" href="/u/joostjm">@JoostJM</a>  Thank you for that answer !</p>
<p>I’ll just exclude the features I find correlated with N_vp then.</p>

---

## Post #8 by @Martin_Bzr (2020-03-19 15:45 UTC)

<p>Actually there is an article that has just been published addressing this issue and consistent with my findings:<br>
<a href="https://doi.org/10.1016/j.ejmp.2020.02.010" class="onebox" target="_blank" rel="nofollow noopener">https://doi.org/10.1016/j.ejmp.2020.02.010</a></p>
<p>They have also provide a table with some of the most correlated features with ROI volume:<br>
<a href="https://www.physicamedica.com/cms/10.1016/j.ejmp.2020.02.010/attachment/48df926d-151c-48d6-bd8b-93949c897c45/mmc1.docx" class="onebox" target="_blank" rel="nofollow noopener">https://www.physicamedica.com/cms/10.1016/j.ejmp.2020.02.010/attachment/48df926d-151c-48d6-bd8b-93949c897c45/mmc1.docx</a></p>

---

## Post #9 by @MachadoL (2020-04-07 20:33 UTC)

<p>Excellent topic,</p>
<p>Did you guys reach any conclusion on which classes are sensible to the number of voxels in the ROI and which are not (are normalized)?</p>

---

## Post #10 by @Martin_Bzr (2020-05-26 20:32 UTC)

<p>Hey everyone,</p>
<p>So I have been doing some experiments on that subject today:<br>
I have generated 30 random noise images and 30 spheres of increasing sizes.<br>
I have extracted the radiomics features from all these ROIs and calculated the std deviation and the correlations with the number of voxel in the ROI (spearman and pearson).<br>
You can find the csv file with the results as well as the images and the VOIs and the extraction params in the google drive link below.<br>
I think Spearman’s correlation is more sensitive than Pearson’s for that task.</p>
<p>I was thinking of setting a spearman threshold based on a robust feature such as original_firstorder_Mean or original_firstorder_Median and keeping all the features that are below that.<br>
What do you think?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09374ac172b0ce90aaf3fd64fc7fd52c6ad7fe59.png" alt="download-1" data-base62-sha1="1jwL6Mmem1GKZjBDzE5bmILhLMl" width="352" height="255"><br>
<a href="https://drive.google.com/drive/folders/1Qfi16GeqxelLaFJMV7gpCJHggquYfjOb?usp=sharing" rel="noopener nofollow ugc">Link to the folder with the images, masks and results</a></p>

---
