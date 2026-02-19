---
topic_id: 24683
title: "Pyradiomics Brain Mri How To Interpolate And Remove Outliers"
date: 2022-08-09
url: https://discourse.slicer.org/t/24683
---

# Pyradiomics, Brain MRI: How to Interpolate and remove outliers? 

**Topic ID**: 24683
**Date**: 2022-08-09
**URL**: https://discourse.slicer.org/t/pyradiomics-brain-mri-how-to-interpolate-and-remove-outliers/24683

---

## Post #1 by @someOne (2022-08-09 06:39 UTC)

<p>Hello Team</p>
<p>I was trying to extract features from brain MRI images using pyradiomics.</p>
<p>According to this article (Page4)<br>
<a href="https://rdcu.be/cTh2N" class="onebox" target="_blank" rel="noopener nofollow ugc">https://rdcu.be/cTh2N</a></p>
<p>Two essential steps before the feature extraction are <em>Interpolation to isotropic voxel spacing</em> and <em>intensity outlier filtering</em></p>
<p>Does pyradiomics provides such functions?</p>
<p>I learned a little bit about pyradiomics parameter customization from this source, I wonder if that could help?</p><aside class="onebox githubblob" data-onebox-src="https://github.com/AIM-Harvard/pyradiomics/blob/master/docs/customization.rst">
  <header class="source">

      <a href="https://github.com/AIM-Harvard/pyradiomics/blob/master/docs/customization.rst" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/AIM-Harvard/pyradiomics/blob/master/docs/customization.rst" target="_blank" rel="noopener nofollow ugc">AIM-Harvard/pyradiomics/blob/master/docs/customization.rst</a></h4>


      <pre><code class="lang-rst">.. _radiomics-customization-label:

==========================
Customizing the Extraction
==========================

----------------------
Types of Customization
----------------------

There are 4 ways in which the feature extraction can be customized in PyRadiomics:

1. Specifying which image types (original/derived) to use to extract features from
2. Specifying which feature(class) to extract
3. Specifying settings, which control the pre processing and customize the behaviour of enabled filters and feature
   classes.
4. Specifying the voxel-based specific settings, which are only needed when using PyRadiomics to generate feature maps

.. warning::
    At initialization of the feature extractor or an individual feature class, settings can be provided as keyword
</code></pre>



  This file has been truncated. <a href="https://github.com/AIM-Harvard/pyradiomics/blob/master/docs/customization.rst" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
Namely, under <strong>setting</strong>, it mentioned two functions * removeOutliers* and <em>interpolator</em>, although i am not positive if they are the functions I am looking for. Could you help me on that?</p>
<p>Thank<br>
Have a good day</p>

---
