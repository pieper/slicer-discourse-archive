# Any way to plot error bars in Slicer?

**Topic ID**: 12362
**Date**: 2020-07-03
**URL**: https://discourse.slicer.org/t/any-way-to-plot-error-bars-in-slicer/12362

---

## Post #1 by @xlucox (2020-07-03 18:01 UTC)

<p>Hi!!!</p>
<p>I have a data set which has its own standard deviation. I would like to plot in Slicer the error bar of this data. I read in <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Plots" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Plots</a> that VTKPlots can’t do this, is there any other way to do it?</p>
<p>Thank you very much.</p>

---

## Post #2 by @lassoan (2020-07-03 18:19 UTC)

<p>VTK currently does not support error plots, but there is an <a href="https://gitlab.kitware.com/vtk/vtk/-/merge_requests/4668">near-ready implementation</a>. To be able to use this, the features has to be merged into VTK, Slicer has to be upgraded to use latest VTK, and Plots module has to be extended to support this plot type. The first two tasks will take a few weeks. Adding error bar display to Plots module is not planned yet, but the need has come up a few times, so it is likely that one of the funded projects will pay for the development at some point (or you or somebody volunteers his time to implement it).</p>

---
