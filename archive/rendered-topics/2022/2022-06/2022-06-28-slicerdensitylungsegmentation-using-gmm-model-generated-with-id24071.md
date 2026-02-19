---
topic_id: 24071
title: "Slicerdensitylungsegmentation Using Gmm Model Generated With"
date: 2022-06-28
url: https://discourse.slicer.org/t/24071
---

# SlicerDensityLungSegmentation – using GMM model generated with older scikit-learn

**Topic ID**: 24071
**Date**: 2022-06-28
**URL**: https://discourse.slicer.org/t/slicerdensitylungsegmentation-using-gmm-model-generated-with-older-scikit-learn/24071

---

## Post #1 by @ashipde (2022-06-28 01:25 UTC)

<p>I am testing the DensityLungSegmentation extension, as available in Extension Manager in Slicer 5.0.2 in Python 3.9.10/macOS 12.4 setting. It seems the precomputed GMM model that the extension uses was generated with some older libraries – Python 3.8.5, scikit learn 0.23.2, <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7919807/" rel="noopener nofollow ugc">etc</a>. – and, as expected, Slicer issues a warning:</p>
<pre><code class="lang-auto">/Users/ashipde/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/sklearn/base.py:329: UserWarning: Trying to unpickle estimator GaussianMixture from version 0.23.2 when using version 1.1.1. This might lead to breaking code or invalid results. Use at your own risk. For more info please refer to:
https://scikit-learn.org/stable/model_persistence.html#security-maintainability-limitations
  warnings.warn(
</code></pre>
<p>The extension works and generates results, but is the likelihood of inaccuracy high?</p>

---

## Post #2 by @ashipde (2022-06-28 07:30 UTC)

<p>May be not too much of an issue? I compared results with the extension (A) against those with LungCTAnalyzer (B) for six CT scans from a 2-yr period and found them to be similar.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99862abff1841167baa0a73336bdda36761e94dd.jpeg" alt="image" data-base62-sha1="lU8vh2fjViLQW1SfyNFawuNPZ0N" width="317" height="325"></p>

---
