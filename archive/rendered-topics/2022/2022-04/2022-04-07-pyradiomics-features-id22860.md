---
topic_id: 22860
title: "Pyradiomics Features"
date: 2022-04-07
url: https://discourse.slicer.org/t/22860
---

# Pyradiomics Features

**Topic ID**: 22860
**Date**: 2022-04-07
**URL**: https://discourse.slicer.org/t/pyradiomics-features/22860

---

## Post #1 by @mselmanerel (2022-04-07 11:49 UTC)

<p>Hello,</p>
<p>I’m Selman EREL from Ankara Yildirim Beyazit University, Ankara, Turkey. I’m pursuing my PhD in Electrical and Electronics Engineering Department. My PhD topic is Radiomics. I’m responsible to research on radiomics features defined as standard. I have seen PyRadiomics and it is rather useful. It says in pyradiomics website that approximately 1500 radiomics features can be extracted from an image by using pyradiomics. However, in documentation of it, 120 features (19+16+10+24+16+16+5+14) are described but rest is not mentioned. How can I reach the radiomics features that pyradiomics can extract approximately 1500 from a medical image?</p>
<p>Best Regards,</p>
<p>Selman EREL</p>

---

## Post #2 by @Giuli4 (2023-03-28 08:37 UTC)

<p>Hi Selman. I think by 1500 they mean the amount of information that contribute to extract radiomic features; in addition, it is written in the docs:</p>
<p>"Aside from the feature classes, there are also some built-in optional filters:</p>
<p>Laplacian of Gaussian (LoG, based on SimpleITK functionality)<br>
Wavelet (using the PyWavelets package)<br>
Square<br>
Square Root<br>
Logarithm<br>
Exponential<br>
Gradient<br>
Local Binary Pattern (2D)<br>
Local Binary Pattern (3D)"</p>

---

## Post #3 by @harad (2023-03-28 09:55 UTC)

<p>If you use the params.yml file below, you will get 2200 features. Mind that to calculate LBP2D and LBP3D you need to install the following, one by one in 3D Slicer:</p>
<p>from slicer.util import pip_install</p>
<p>pip_install(“scipy”)</p>
<p>pip_install(“trimesh”)</p>
<p>pip_install("<strong>scikit-image</strong> ")</p>
<p>Here is the params file below. Settings are optimized for MRI images. You need to check the pixel intensity range in your images and eventually change the binWidth settings</p>
<p>setting:</p>
<pre><code>normalize: true
normalizeScale: 100

resampledPixelSpacing: [1, 1, 1]

interpolator: 'sitkBSpline' 


binWidth: 5.0
</code></pre>
<p>imageType:</p>
<pre><code>Original: {}
LoG: {'sigma' : [1.0, 2.0, 3.0, 4.0, 5.0]} 
Wavelet: 
    binWidth: 3.0

Square: {}
SquareRoot: {}
Logarithm: {}
Exponential: {}
Gradient: {}
    
LBP2D: 
    binWidth: 0.2
LBP3D: 
    binWidth: 0.3
</code></pre>
<p>featureClass:<br>
glcm:<br>
firstorder:<br>
shape2D:<br>
shape:</p>
<pre><code>glrlm:
glszm:
gldm:
ngtdm:
</code></pre>

---
