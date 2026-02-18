# How to getcenter of vtkplane by python?

**Topic ID**: 21135
**Date**: 2021-12-19
**URL**: https://discourse.slicer.org/t/how-to-getcenter-of-vtkplane-by-python/21135

---

## Post #1 by @jumbojing (2021-12-19 14:54 UTC)

<p>How to getcenter of vtkplane by python?<br>
<a class="mention" href="/u/lassoan">@lassoan</a>@Juicy@jamesobutler <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #2 by @lassoan (2021-12-19 15:12 UTC)

<p>Add half of the origin-&gt;point1 and origin-&gt;point2 vector to the origin to get the center.</p>
<p>I would recommend to use the markup plane node. It allows you to display and interactively modify the plane and has convenience functions for setting/getting the center position.</p>

---
