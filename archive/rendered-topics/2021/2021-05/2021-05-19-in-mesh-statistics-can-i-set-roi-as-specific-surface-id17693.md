# In mesh statistics, can I set ROI as specific surface?

**Topic ID**: 17693
**Date**: 2021-05-19
**URL**: https://discourse.slicer.org/t/in-mesh-statistics-can-i-set-roi-as-specific-surface/17693

---

## Post #1 by @yspark (2021-05-19 12:30 UTC)

<p>Operating system: window 10<br>
Slicer version: 4.10.1<br>
Expected behavior: average closest point distance of specific surface<br>
Actual behavior:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/acdacbdf9548feb3403630acc2c456d69085093c.png" alt="제목 없음" data-base62-sha1="oF8Tqxhye9uOCFjq40Vr0hL6Q9u" width="211" height="340"></p>
<p>Hello, I’m working on a dental university project, and I’m trying to get average closest point distance of specific surface(the area inside several landmark, like that picture).<br>
I made color map file(.vtk file) using model to model distance with two superimposed files. And I tried to use mesh statistics, but I can not define the ROI surface.<br>
please kindly advise to me that how can I define the ROI surface which like attached picture.<br>
Thank you!!</p>

---

## Post #2 by @lassoan (2021-05-19 16:02 UTC)

<p>You can crop models using Dynamic modeler module. In tomorrow’s Slicer Preview Release an additional ROI clip tool will be available, too.</p>

---

## Post #3 by @yspark (2021-05-20 06:32 UTC)

<p>It works fine. I have struggled for a week with this problem, thank you for your help!!</p>

---
