# Different results with different versions of pyradiomics +/- O-RAW

**Topic ID**: 12165
**Date**: 2020-06-23
**URL**: https://discourse.slicer.org/t/different-results-with-different-versions-of-pyradiomics-o-raw/12165

---

## Post #1 by @GVK (2020-06-23 01:04 UTC)

<p>Hi,</p>
<p>I’m calculating radiomics features using different versions of Pyradiomics (v2 and V3 +/- O-RAW) on the same dataset and comparing also to the literature (which used version 1.3 +O-RAW) and getting different results for the same features. Is there a reason the results should be different depending upon which version of Pyradiomics is used and whether O-RAW is used or not?</p>
<p>Thanks</p>
<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @JoostJM (2020-06-23 09:51 UTC)

<p>Hello <a class="mention" href="/u/gvk">@GVK</a>,</p>
<p>What do you mean by “O-RAW”?<br>
As to different values for features between different versions, this is indeed the case for some of the features/filters. All code changes are listed in the <a href="https://pyradiomics.readthedocs.io/en/latest/changes.html">release notes</a>, with result-changing changes listed under “Feature Calculation Changes”.</p>
<p>PyRadiomics is extensively tested for a range of possible settings, using the 5 test cases included in the repository. Every commit is checked to ensure the calculation result does not change unintentionally by comparing calculated results against a fixed baseline. Every time this baseline is changed, it will be listed under Feature Calculation Changes.</p>

---

## Post #3 by @GVK (2020-06-23 10:15 UTC)

<p>Thanks for your reply.</p>
<p>We are having issues in particular with trying to replicate results from a study by Shi et al 2019 which used a TCIA dataset and extracted 4 features (first order energy, compactness 2, gray level non uniformity and Wavelet gray level non uniformity) using Pyradiomics v1.3 and o-Raw please see (<a href="https://doi.org/10.1002/mp.13844" rel="nofollow noopener">https://doi.org/10.1002/mp.13844</a>).</p>
<p>We used Pyradiomics v3.0 and found that the results for first order energy and sphericity were very different, however when we used it in combination with O-RAW sphericty wasn similar however gray level non uniformity results were different.</p>
<p>I will have a look through the release notes to see if I can work out the changes in features that have occurred since v1.3 was released.</p>
<p>Thank you,<br>
Gargi</p>

---

## Post #4 by @JoostJM (2020-06-30 10:35 UTC)

<p>Shape features are expected to be different, as we introduced a different method (mesh-based instead of voxel-based) for calculation volume in 2.1.0. This also affects many other shape features, as they are based on the relationship between volume and surface area.<br>
Moreover, version 2.0.0 fixed some bugs in the calculation of the Wavelet filtered images (<a href="https://github.com/Radiomics/pyradiomics/pull/346">#346</a>).</p>
<p>As to the use of O-RAW, I think the most important part to consider is the interpolation of RTSTRUCT to binary labelmaps, which may introduce differences between different software implementations. We genarally use plastimatch for this, but other tools exist.</p>
<p>Finally, it is very important to ensure all customization parameters are similar between extractions, as these can have a large influence on the calcutated feature value.</p>

---
