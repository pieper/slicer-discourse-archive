# Grid transform visualization in 3D is challenging for data with small voxel size

**Topic ID**: 4667
**Date**: 2018-11-07
**URL**: https://discourse.slicer.org/t/grid-transform-visualization-in-3d-is-challenging-for-data-with-small-voxel-size/4667

---

## Post #1 by @muratmaga (2018-11-07 05:55 UTC)

<p>In addition to the issues of working with fiducials in 3D for small voxel datasets (see <a href="https://discourse.slicer.org/t/markups-module-enhancements/4335/6">Markups Module enhancements</a>), visualizing displacement fields is also challenging. Maximum displacements in dataset I am trying to visualize is about 10-20 times the voxel size (which is 0.021mm), but because the smallest diameter I can choose for the grid is 1.0mm, the whole 3D grid looks like a box.</p>
<p>Is there any workaround? I can’t seem to manually enter values into the fields that control scaling/spacing/diameter etc…</p>

---

## Post #2 by @lassoan (2018-11-07 19:00 UTC)

<p>I’ve started adding a range selector to these widgets (so that you can customize min/max values), by making MRML slider widget more intelligent. Here is my branch (there is only a single relevant commit, the last one): <a href="https://github.com/lassoan/Slicer/tree/add-range-to-mrml-slider-widget">https://github.com/lassoan/Slicer/tree/add-range-to-mrml-slider-widget</a>. I think the only missing thing is to hide the range selector by default and update Transforms module to show the range selector. If you try it on your data sets then you may find other things to tune (e.g., step size).</p>
<p>It would be great if you could take it over from here. If you have any questions or have a pull request to review then let me know.</p>

---

## Post #3 by @muratmaga (2018-11-08 18:55 UTC)

<p>Thanks Andras. Our plates are full with few other things. But it is good to know where to start. I think we might be able to take over once we make progress in our current project.</p>

---
