# Post-treatment of vascular segmentation

**Topic ID**: 37874
**Date**: 2024-08-14
**URL**: https://discourse.slicer.org/t/post-treatment-of-vascular-segmentation/37874

---

## Post #1 by @dream520nb (2024-08-14 07:52 UTC)

<p>Dear friends:<br>
I used machine learning methods to get a model of blood vessel segmentation, but it is not perfect. I would like to ask you if there is any way to complete the undivided blood vessels.</p>
<p>Operating system: window<br>
Slicer version: 5.4.0</p>

---

## Post #2 by @lassoan (2024-08-15 13:53 UTC)

<p>Trying to improve segmentation results by post-processing sounds like a much more difficult task than improving the machine learning results.</p>
<p>There is a project that aims to solve similar issue for lung vessel segmentation. The current approach is to try to improve amount and quality of training data and also see how much the problem becomes easier when using better quality input images (e.g., better synchronization of imaging and contrast injection, higher resolution, …). You can follow updates in the <a href="https://github.com/rbumm/SlicerLungCTAnalyzer">LungCTAnalyzer extension</a> ask <a class="mention" href="/u/rbumm">@rbumm</a> or <a class="mention" href="/u/diazandr3s">@diazandr3s</a> in a couple of months.</p>

---
