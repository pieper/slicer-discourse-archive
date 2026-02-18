# Segments automatically eraised when new overlapping segment added

**Topic ID**: 20921
**Date**: 2021-12-05
**URL**: https://discourse.slicer.org/t/segments-automatically-eraised-when-new-overlapping-segment-added/20921

---

## Post #1 by @alan6690 (2021-12-05 22:24 UTC)

<p>I am trying to use segment editor to create a body trunk segmentation from my CBCT images, in which I need to use logical operator to manipulate multiple segments under the same segmentation object. However, I don’t know why when I create the second segments using ‘threshold’ effect, the overlapping region between the first and second segments would be erased from the first one. How can I allow the overlapping to exist before I do the logical operation? Thank you.</p>

---

## Post #2 by @mau_igna_06 (2021-12-05 22:53 UTC)

<p>Please read the “Masking” part of this document:<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html</a></p>

---
