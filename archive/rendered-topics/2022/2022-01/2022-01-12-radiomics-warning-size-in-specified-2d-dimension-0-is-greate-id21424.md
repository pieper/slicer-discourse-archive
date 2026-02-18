# Radiomics warning Size in specified 2D dimension (0) is greater than 1, cannot calculate 2D shape

**Topic ID**: 21424
**Date**: 2022-01-12
**URL**: https://discourse.slicer.org/t/radiomics-warning-size-in-specified-2d-dimension-0-is-greater-than-1-cannot-calculate-2d-shape/21424

---

## Post #1 by @zandarina (2022-01-12 16:34 UTC)

<p>Dear all,</p>
<p>I am trying to compute the radiomics and I get this warning:<br>
Size in specified 2D dimension (0) is greater than 1, cannot calculate 2D shape</p>
<pre><code> result = extractor.execute(image, mask)
</code></pre>
<p>and the image size is: (208, 150, 1)</p>
<p>Thank you for the help</p>

---

## Post #2 by @zandarina (2022-01-17 09:41 UTC)

<p>Any idea? I do not understand this problem. Thanks</p>

---

## Post #3 by @JoostJM (2022-01-18 12:38 UTC)

<p>Fixed in <a href="https://github.com/AIM-Harvard/pyradiomics/issues/742">PyRadiomics issue #742</a>.</p>

---

## Post #4 by @JoostJM (2022-01-18 12:38 UTC)



---
