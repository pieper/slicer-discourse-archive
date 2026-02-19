---
topic_id: 28207
title: "Please Quickly Check My Slicerradiomics Pyradiomics Paramete"
date: 2023-03-07
url: https://discourse.slicer.org/t/28207
---

# Please quickly check my SlicerRadiomics/Pyradiomics parameters file for any contradictions and errors

**Topic ID**: 28207
**Date**: 2023-03-07
**URL**: https://discourse.slicer.org/t/please-quickly-check-my-slicerradiomics-pyradiomics-parameters-file-for-any-contradictions-and-errors/28207

---

## Post #1 by @harad (2023-03-07 10:05 UTC)

<p>Hi all, I would be extremely grateful if anyone could check my parameters file.<br>
It works but I am concerned that any of the settings may contradict each other?<br>
In the settings, it is essential that I have  resampling, normalization and supposedly the bin-number settings. The analysis is intended for MRB files (MRI) in 3D Slicer.</p>
<p>As to image types and feature classes, I need as many features calculated as possible, with this parameters file I get 2200 features.<br>
Is any more detail needed in the settings of either the image types or feature classes?</p>
<p>Feedback on this file would help me a lot and also, if OK or corrected,  it could be shown on GitHub and be of wider help as an example of how to exploit the full capacity of SlicerRadiomics.</p>
<p>Finally the file is below, cheers, Marko</p>
<p>setting:</p>
<p>binCount: 20<br>
label: 1<br>
interpolator: ‘sitkBSpline’</p>
<p>resampledPixelSpacing: [1, 1, 1]<br>
normalize: True</p>
<p>removeOutliers: 4</p>
<p>imageType:</p>
<pre><code>Original: {}
LoG: {'sigma' : [1.0, 2.0, 3.0, 4.0, 5.0]} 
Wavelet: {}
  
Square: {}
SquareRoot: {}
Logarithm: {}
Exponential: {}
Gradient: {}
LBP2D: {}
LBP3D: {}
</code></pre>
<p>featureClass:<br>
glcm:<br>
firstorder:<br>
shape2D:<br>
shape:<br>
glrlm:<br>
glszm:<br>
gldm:<br>
ngtdm:</p>

---

## Post #3 by @lassoan (2023-03-13 14:09 UTC)

<p>Maybe by providing a bit more context of what you would like to achieve and/or asking more specific questions could help getting answers. You can also try to <code>@mention</code> people who have answered similar questions before.</p>

---

## Post #4 by @harad (2023-03-14 07:56 UTC)

<p>I am very grateful for your answer! My strong assumption was that everyone would be a parameter file expert because this is the very first step for any type of analysis. I started a new topic where I followed your advice to be more specific, also more concise. It is just that I want to avoid errors in the settings file, the first file I submitted here had resampling prior to normalization which seems to be the obvious mistake, luckily chatGPT noticed that.<br>
I also want to calculate the very maximum number of parameters, this parameter file delivers 2200. There may be some missing settings in the “image type” and “feature class” sections as none of the files provided as examples or discussed here instruct to analyse all image types and feature classes.</p>

---
