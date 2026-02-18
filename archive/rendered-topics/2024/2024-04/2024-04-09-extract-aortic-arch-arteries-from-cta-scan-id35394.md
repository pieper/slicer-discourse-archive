# Extract aortic arch arteries from CTA scan

**Topic ID**: 35394
**Date**: 2024-04-09
**URL**: https://discourse.slicer.org/t/extract-aortic-arch-arteries-from-cta-scan/35394

---

## Post #1 by @koenterheegde (2024-04-09 14:03 UTC)

<p>Hey everyone,</p>
<p>I’m trying to segment the aorta from a CTA scan. For the most part of the body, this works perfectly fine using thresholding, except for the arteries close to the heart. It basically becomes one big bulge of interconnected arteries and impossible to see which artery is which. I’ve tried grow from seeds but also here, you would have to know on the CTA scan where the arteries are, but thats very difficult to seperate as all the arteries have the same HU values around the heart area and the heart itself. Any ideas how to solve this? I want to have 3d model of the aorta from the femoral arteries to the renal arteries, then the mesenteric artery, celiac trunk and finally the arteries in the aortic arch: left subclavian artery, right subclavian artery, right common carotid artery. Thanks in advance</p>

---
