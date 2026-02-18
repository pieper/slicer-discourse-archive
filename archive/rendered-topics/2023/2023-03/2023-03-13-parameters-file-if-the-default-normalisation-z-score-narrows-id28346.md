# Parameters file: If the default normalisation (z-score) narrows the pixel intensity range to -3/+3 this should mean that binWidth cannot be lower than 6? And that is for only one bin?

**Topic ID**: 28346
**Date**: 2023-03-13
**URL**: https://discourse.slicer.org/t/parameters-file-if-the-default-normalisation-z-score-narrows-the-pixel-intensity-range-to-3-3-this-should-mean-that-binwidth-cannot-be-lower-than-6-and-that-is-for-only-one-bin/28346

---

## Post #1 by @harad (2023-03-13 13:33 UTC)

<p>This parameter file (below) works fine and calculates about 2200 features but I am still concerned that any of the settings may contradict each other, or be in the wrong order and therefore deliver incorrect values.<br>
If the default normalisation (z-score)  narrows the pixel intensity range to -3/+3 this should mean that binWidth cannot be lower than 6? And that is for only one bin?<br>
Is it then better to set the binCount?</p>
<p>Would normalizeScale be useful to define, say to 100?<br>
What is the optimal binCount for MRI?</p>
<p>Is any more detail needed for the image types or feature classes?</p>
<p>Feedback on this file would be of tremendous help to me!</p>
<p>Cheers, Marko</p>
<p>setting:</p>
<pre><code>normalize: true

resampledPixelSpacing: [1, 1, 1]

interpolator: 'sitkBSpline' 

binCount: 32

label: 1
</code></pre>
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
shape:</p>
<pre><code>glrlm:
glszm:
gldm:
ngtdm:
</code></pre>

---
