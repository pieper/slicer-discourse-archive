---
topic_id: 13500
title: "Can Radiomics In 3Dslicer Output Many Results Of Different P"
date: 2020-09-16
url: https://discourse.slicer.org/t/13500
---

# Can radiomics in 3dslicer output many results of different patients in a CSV?

**Topic ID**: 13500
**Date**: 2020-09-16
**URL**: https://discourse.slicer.org/t/can-radiomics-in-3dslicer-output-many-results-of-different-patients-in-a-csv/13500

---

## Post #1 by @Jeff_W (2020-09-16 11:36 UTC)

<p>Can radiomics in 3dslicer output many results of different patients in a CSV?Can radiomics in 3dslicer output many results of different patients in a CSV?Can radiomics in 3dslicer output many results of different patients in a CSV?Can radiomics in 3dslicer output many results of different patients in a CSV?Can radiomics in 3dslicer output many results of different patients in a CSV?Can radiomics in 3dslicer output many results of different patients in a CSV?</p>

---

## Post #2 by @JoostJM (2020-09-30 11:41 UTC)

<p>The slicerradiomics extension is intended for single-case processing.<br>
However batchprocessing is possible using the standalone version of PyRadiomics (which is the backend of slicerradiomics). See <a href="https://pyradiomics.readthedocs.io/en/latest/usage.html#batch-mode">the documentation on batch mode usage</a>.</p>
<p>When you installed slicerradiomics, pyradiomics was also installed in the slicer python environment and should therefore be available.</p>

---

## Post #3 by @Jeff_W (2020-09-30 13:42 UTC)

<aside class="quote no-group" data-username="JoostJM" data-post="2" data-topic="13500">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/joostjm/48/1091_2.png" class="avatar"> JoostJM:</div>
<blockquote>
<p>However batchprocessing is possible using the standalone version of PyRadiomics (which is the backend of slicerradiomics). See <a href="https://pyradiomics.readthedocs.io/en/latest/usage.html#batch-mode" rel="noopener nofollow ugc">the documentation on batch mode usage</a>.</p>
<p>When you installed slicerradiomics, pyradiomics was also installed in the slicer python environment and should therefore be available.</p>
</blockquote>
</aside>
<p>真的很感谢您的回复。影像组学相关研究在中国很火，您如果有精力的话可以找些华裔做个中文文档，相信对pyradiomics的推广会有帮助。<br>
You can use google translate it.</p>

---
