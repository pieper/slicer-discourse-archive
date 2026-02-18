# Can I read and modify a transform matrix with python

**Topic ID**: 6964
**Date**: 2019-05-29
**URL**: https://discourse.slicer.org/t/can-i-read-and-modify-a-transform-matrix-with-python/6964

---

## Post #1 by @timeanddoctor (2019-05-29 23:13 UTC)

<p>can I read and modify a transform matrix with python directly(not the GUI of transform) in slicer.<br>
for example:<br>
Read<br>
display (transformMatrix)<br>
I will get a 4*4matrix:<br>
[ [  1  0  0  52.64097]<br>
[ 0  1 0 -46.12696]<br>
[ 0   0   1  -0.48185]<br>
[  0.   0.   0.  1.  ]]</p>
<p>Modify<br>
transformMatrix=np.array[<br>
[  0.92979  -0.26946  -0.25075  52.64097]<br>
[  0.03835   0.74845  -0.66209 -46.12696]<br>
[  0.36608   0.60599   0.70623  -0.48185]<br>
[  0.        0.        0.        1.     ]]</p>

---

## Post #2 by @lassoan (2019-05-30 03:45 UTC)

<p>See example of setting a transform from a numpy array here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Transforms#Examples" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/Transforms#Examples</a></p>

---
