# Create an indipendent volumeNode for an organ obtained after segmentation

**Topic ID**: 40018
**Date**: 2024-11-04
**URL**: https://discourse.slicer.org/t/create-an-indipendent-volumenode-for-an-organ-obtained-after-segmentation/40018

---

## Post #1 by @Filippo_Parronchi (2024-11-04 15:32 UTC)

<p>Good morning everyone, after applying the ‘totalSegmentator’ module, I obtained all my abdominal organs segmented.<br>
How can I now associate, for example, only my ‘liver’ object with a new volume node so that I can manage and work on it independently, without working with all the other segmented structures?<br>
How can i do this operation also with a python script?<br>
thanks a lot</p>

---

## Post #2 by @mikebind (2024-11-04 16:25 UTC)

<p>Take a look at the Mask Scalar Volume module, it should provide exactly the functionality you need. Also, here is a python script linked from the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html" rel="noopener nofollow ugc">script repository</a> which does something similar operating directly from a segmentation <a href="https://gist.github.com/lassoan/2f5071c562108dac8efe277c78f2620f" rel="noopener nofollow ugc">MaskVolumeHistogramPlot.py</a></p>

---
