# How can I decrease the number of points of the model?

**Topic ID**: 1074
**Date**: 2017-09-18
**URL**: https://discourse.slicer.org/t/how-can-i-decrease-the-number-of-points-of-the-model/1074

---

## Post #1 by @Ramttoong (2017-09-18 02:07 UTC)

<p>The model’s number of points itself never change?<br>
How can I decrease the number of points of the model?</p>

---

## Post #2 by @lassoan (2017-09-18 02:08 UTC)

<p>You can use <code>Decimation</code> option in <code>Surface toolbox</code> module to reduce number of points in a model.</p>

---

## Post #3 by @helia77 (2024-07-17 22:42 UTC)

<p>Hello,<br>
regarding this issue, how can I reduce the points of a centerline model? Using <code>Decimation</code> won’t change the number of points. I also tried “Uniform remesh”, but that doesn’t work for centerlines (gives <code>zero-size array</code> error).<br>
The centerline extraction process took a long time due to my large volume, and I only chose the option to output the centerline model. I know it is possible to resample points on curves, but I’d like to avoid the long process time of centerline extraction if possible. Is there any other way to reduce the number of points in a centerline model?</p>

---
