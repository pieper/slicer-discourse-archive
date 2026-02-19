---
topic_id: 30493
title: "About Lungctanalyzer Result"
date: 2023-07-10
url: https://discourse.slicer.org/t/30493
---

# about lungCTanalyzer Result

**Topic ID**: 30493
**Date**: 2023-07-10
**URL**: https://discourse.slicer.org/t/about-lungctanalyzer-result/30493

---

## Post #1 by @mikiN (2023-07-10 12:32 UTC)

<p>I have a question about the result of LungCTanalyzer.<br>
Why do the Volmetric analysis (Table 1) and the Extended analysis (Table 2) have different values for Inflated?<br>
For example, in Table1, Inflated right is 560.077cm3. In Table2, 448.888ml.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/50860eb79c44a194b72603ecd2b90fdade8f108e.jpeg" data-download-href="/uploads/short-url/bulpHgD2bhBRLSiVP7BmUZnD1F4.jpeg?dl=1" title="IMG_0483" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/50860eb79c44a194b72603ecd2b90fdade8f108e_2_690x435.jpeg" alt="IMG_0483" data-base62-sha1="bulpHgD2bhBRLSiVP7BmUZnD1F4" width="690" height="435" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/50860eb79c44a194b72603ecd2b90fdade8f108e_2_690x435.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/50860eb79c44a194b72603ecd2b90fdade8f108e_2_1035x652.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/50860eb79c44a194b72603ecd2b90fdade8f108e_2_1380x870.jpeg 2x" data-dominant-color="B0B1AF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_0483</span><span class="informations">1920×1213 351 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @mikiN (2023-07-10 12:38 UTC)

<p>Sorry.<br>
In correct, “in Table1, Inflated right is 429.947cm3”.</p>

---

## Post #3 by @rbumm (2023-07-10 14:49 UTC)

<p>Thank you for your feedback, actually a good catch.</p>
<p>So currently,  by convention, we have actually calculated the ml of “Inflated” in Table 2 as “inflated”  + “emphysema” because it is questionable if some parts of emphysema may still account for functional gas exchange.  So 448.888 in Table 2 makes sense for the right lung (429.947 + 18.9418), but 586.644 for the left lung (567.702 + 38.2556) does not.</p>
<p>I found and removed the bug and pushed an update, which will be available tomorrow.</p>

---
