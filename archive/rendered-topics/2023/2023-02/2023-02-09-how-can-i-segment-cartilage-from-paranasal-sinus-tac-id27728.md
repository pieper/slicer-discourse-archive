# How can I segment cartilage from paranasal sinus tac

**Topic ID**: 27728
**Date**: 2023-02-09
**URL**: https://discourse.slicer.org/t/how-can-i-segment-cartilage-from-paranasal-sinus-tac/27728

---

## Post #1 by @mburibe_18 (2023-02-09 19:14 UTC)

<p>I am trying to segment nasal cartilage from a CT scan of the paranasal sinuses, but I have not been able to accurately locate the threshold so that this area to be segmented can be marked.<br>
Could you please help me ??</p>
<p>thank you !</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/236535b0f60c1ac6e9d7ef05bc5c1614ea8cfdac.png" data-download-href="/uploads/short-url/537yf6cGt6RbkdkliQz7vUGtKFe.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/236535b0f60c1ac6e9d7ef05bc5c1614ea8cfdac_2_690x387.png" alt="image" data-base62-sha1="537yf6cGt6RbkdkliQz7vUGtKFe" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/236535b0f60c1ac6e9d7ef05bc5c1614ea8cfdac_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/236535b0f60c1ac6e9d7ef05bc5c1614ea8cfdac_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/236535b0f60c1ac6e9d7ef05bc5c1614ea8cfdac.png 2x" data-dominant-color="515757"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×768 312 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @philippepellerin (2023-02-12 09:24 UTC)

<p>There is not enough contrast to easily segment the nasal cartilage, you will have to do that manually and can do that only if the CT is of high quality… I have tried the same for many years…</p>

---

## Post #3 by @mohammed_alshakhas (2023-02-13 12:01 UTC)

<p>Playing with contrast helps a lot when you need to segment a structure like that .<br>
You can use an option in contrast tool  to enhance the area you work in . It helped me many time .<br>
you will most likely end up manually painting it .<br>
but remember there are a lot of tool to make it easier like smudge paint and fill holes</p>

---

## Post #4 by @lassoan (2023-02-15 05:49 UTC)

<p>Note that once you segmented a few dozens cases, you can start to train an AI segmentation model using MONAILabel extension. Since this is a difficult segmentation task (thin structures and low contrast), so you might need a few hundred images for robust and accurate segmentation.</p>

---
