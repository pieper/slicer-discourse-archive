# Line Intensity profile resolution

**Topic ID**: 17785
**Date**: 2021-05-25
**URL**: https://discourse.slicer.org/t/line-intensity-profile-resolution/17785

---

## Post #1 by @marianaslicer (2021-05-25 11:18 UTC)

<p>Hi everyone,</p>
<p>I would like to calculate the intensity profile along a line. My data has a resolution of 2 mm in the cranio-caudal direction and I don’t want to interpolate any value along the line.</p>
<p>Currently, I’m using the LineIntensityProfile module from SandBox extension, but it requires the resolution line parameter. Any idea how to compute the line intensity profile without changing the resolution?</p>

---

## Post #2 by @lassoan (2021-05-25 11:59 UTC)

<p>If you want to extract a line along one of the 3 image axes then you can do that by getting the volume as a numpy array and use array indexing. You can find examples for each step in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">script repository</a>.</p>
<p>If the line is not exactly parallel with an image axis and you want to get samples at equal distances then you must resample (at any chosen resolution).</p>

---
