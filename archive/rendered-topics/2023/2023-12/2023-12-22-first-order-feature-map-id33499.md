# First order feature map 

**Topic ID**: 33499
**Date**: 2023-12-22
**URL**: https://discourse.slicer.org/t/first-order-feature-map/33499

---

## Post #1 by @MicheleMureddu (2023-12-22 12:11 UTC)

<p>Hi<br>
i was trying to extract first order feature maps with this configurations:</p>
<pre><code class="lang-auto">setting:
  binWidth: 0.3125
  label: 1
  interpolator: 'sitkBSpline'
  resampledPixelSpacing:   
  resegmentMode: 'absolute'
  resegmentRange: [0,20]


imageType:
  Original: {} 

</code></pre>
<p>For all the textural features the code seems to work and i obtain feature maps. If i enable, for example, first order entropy i get "segmentation fault (core dumped).</p>

---
