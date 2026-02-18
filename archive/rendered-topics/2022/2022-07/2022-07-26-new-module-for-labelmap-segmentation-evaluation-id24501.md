# New Module for Labelmap/Segmentation Evaluation

**Topic ID**: 24501
**Date**: 2022-07-26
**URL**: https://discourse.slicer.org/t/new-module-for-labelmap-segmentation-evaluation/24501

---

## Post #1 by @Mehran (2022-07-26 15:01 UTC)

<p>Dear members,<br>
I shared a new module to evaluate labelmap/segmentation by extracting several metrics such as DICE, Jaccard, AUC, AVD,… . In order to use this module you need to provide a reference and a test image to extract such metrics. Depending on your OS (win/linux) you need to download EvaluateSegmentation module (<a href="https://github.com/Mehrancd/EvaluateSegmentation" rel="noopener nofollow ugc">GitHub - Mehrancd/EvaluateSegmentation: A Slicer module Evaluate Segmentation </a>) and add it to Slicer-&gt;Edit-&gt;Application Settings-&gt;Modules, then add the path of the module to “Additional module paths” and restart. The module needs some dependencies which automatically will be installed.<br>
Please have a look (<a class="mention" href="/u/lassoan">@lassoan</a> ) and your feedback will be considered to improve the module.<br>
More detail about algorithm can be found in: <a href="https://doi.org/10.1016/j.mri.2019.11.002" rel="noopener nofollow ugc">https://doi.org/10.1016/j.mri.2019.11.002 </a>) and <a href="https://doi.org/10.1186/s12880-015-0068-x" rel="noopener nofollow ugc">https://doi.org/10.1186/s12880-015-0068-x </a>)<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6de942fa45d411851dc83b6f4d653a82aa6d2d17.png" alt="EvaluationSegmentation" data-base62-sha1="fGjNUuD6FL9Bij6VCtU3UpaQY7l" width="128" height="128"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/73e27b8bd743d6dd85eaa7c50a48d0ce0d8ea163.jpeg" data-download-href="/uploads/short-url/gxa92BGJtkJSB9rIo5PJm0OHzBp.jpeg?dl=1" title="Screenshot1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73e27b8bd743d6dd85eaa7c50a48d0ce0d8ea163_2_345x195.jpeg" alt="Screenshot1" data-base62-sha1="gxa92BGJtkJSB9rIo5PJm0OHzBp" width="345" height="195" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73e27b8bd743d6dd85eaa7c50a48d0ce0d8ea163_2_345x195.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73e27b8bd743d6dd85eaa7c50a48d0ce0d8ea163_2_517x292.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73e27b8bd743d6dd85eaa7c50a48d0ce0d8ea163_2_690x390.jpeg 2x" data-dominant-color="6B6C6E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot1</span><span class="informations">1920×1090 113 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Mehran</p>

---
