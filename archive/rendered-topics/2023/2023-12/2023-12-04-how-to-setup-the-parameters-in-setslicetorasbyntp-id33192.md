# How to setup the parameters in SetSliceToRASByNTP?

**Topic ID**: 33192
**Date**: 2023-12-04
**URL**: https://discourse.slicer.org/t/how-to-setup-the-parameters-in-setslicetorasbyntp/33192

---

## Post #1 by @derekcbr (2023-12-04 05:17 UTC)

<p>I am trying to use plane matrix to control the green slice position and rotation.<br>
matrix_transform = np.array([<br>
[1, 0, 0, 0.2],<br>
[0, 1, 0, 0.3],<br>
[0, 0, 1, 0.4],<br>
[0, 0, 0, 1]<br>
])<br>
How to use matrix to setup the parameters in SetSliceToRASByNTP? Do I need to use function to get the the normal of plane, also need to know the previous plane position as well? Thanks a lot.</p>

---
