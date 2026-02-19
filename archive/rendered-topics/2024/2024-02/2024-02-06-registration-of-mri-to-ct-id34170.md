---
topic_id: 34170
title: "Registration Of Mri To Ct"
date: 2024-02-06
url: https://discourse.slicer.org/t/34170
---

# Registration of MRI to CT

**Topic ID**: 34170
**Date**: 2024-02-06
**URL**: https://discourse.slicer.org/t/registration-of-mri-to-ct/34170

---

## Post #1 by @robsfill (2024-02-06 15:23 UTC)

<p>Hi everyone!<br>
I have a problem with my thesis project. I segmented images of 5 vertebrae from CT and the corresponding 4 discs but from MRI. I have to transport the MRI discs in the same reference system. How can I do this? Is there a tutorial step by step?<br>
Please help me.</p>

---

## Post #2 by @pieper (2024-02-06 16:37 UTC)

<p>There’s a lot of information about registration like that.  Unless the data is particularly noisy or blurry it should work well, but if the spine is curved differently in the two scans it may be hard to get an exact solution.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/registration.html</a></p>

---
