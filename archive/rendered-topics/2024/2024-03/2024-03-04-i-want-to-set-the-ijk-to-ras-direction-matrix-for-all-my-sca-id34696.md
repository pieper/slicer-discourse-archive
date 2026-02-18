# I want to set the IJK to RAS direction matrix for all my scans I upload. 

**Topic ID**: 34696
**Date**: 2024-03-04
**URL**: https://discourse.slicer.org/t/i-want-to-set-the-ijk-to-ras-direction-matrix-for-all-my-scans-i-upload/34696

---

## Post #1 by @Bartdh (2024-03-04 16:27 UTC)

<p>I want to set the IJK to RAS direction matrix for all my scans I upload. The current matrix gives me a mirrored volume after segmentation. I believe the “IJK to RAS direction matrix” should be (1 0 0, 0 1 0, 0 0 1). How do I configure this matrix in my settings?</p>

---

## Post #2 by @pieper (2024-03-04 20:27 UTC)

<p>If you look through the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">script repository</a> you can find examples of setting the IJKToRAS matrix.  Also you’ll find examples of setting your slicerrc.py file to do things automatically when nodes are added to the scene.</p>

---
