---
topic_id: 15985
title: "Define Borders Between Bones"
date: 2021-02-14
url: https://discourse.slicer.org/t/15985
---

# Define borders between bones

**Topic ID**: 15985
**Date**: 2021-02-14
**URL**: https://discourse.slicer.org/t/define-borders-between-bones/15985

---

## Post #1 by @EL_JAAFARI (2021-02-14 18:05 UTC)

<p>Hello everyone,<br>
I need your support</p>
<p>After segmenting spine, I’d like now to segment the borders between all the vertebrae.<br>
Is there a method you recommend for this?</p>
<p>Thanks in advance</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a7c082071eb219c73ac0a8cd41ea2458c662954.jpeg" data-download-href="/uploads/short-url/htxZgzGyeW35OCUA7Siru0WlYqw.jpeg?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7a7c082071eb219c73ac0a8cd41ea2458c662954_2_451x500.jpeg" alt="Screenshot" data-base62-sha1="htxZgzGyeW35OCUA7Siru0WlYqw" width="451" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7a7c082071eb219c73ac0a8cd41ea2458c662954_2_451x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7a7c082071eb219c73ac0a8cd41ea2458c662954_2_676x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7a7c082071eb219c73ac0a8cd41ea2458c662954_2_902x1000.jpeg 2x" data-dominant-color="43434D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1287×1425 262 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @EL_JAAFARI (2021-02-14 18:05 UTC)

<p>Operating system: MacOS<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #3 by @lassoan (2021-02-15 03:21 UTC)

<p>You can use Grow from seeds effect by painting a seed into each vertebra.</p>
<p>If you have already segmented the whole spine then hide that segment (so that it does not participate in region growing) and choose that segment as “Editable area” in masking section.</p>
<p>If you haven’t segmented the whole spine then enable “Editable intensity range” and set the threshold range to include bones.</p>

---
