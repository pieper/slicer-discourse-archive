# Segment Editor Dilation - margin size question

**Topic ID**: 3691
**Date**: 2018-08-07
**URL**: https://discourse.slicer.org/t/segment-editor-dilation-margin-size-question/3691

---

## Post #1 by @fedorov (2018-08-07 20:28 UTC)

<p>We use Segment Editor dilation for a project, and today I realized that the behavior is somewhat unexpected. Apparently, it is not possible to grow the margin in a given direction unless the “Margin size” parameter is above spacing*2 in that direction.</p>
<p>So if the spacing of the image is 0.5x0.5x3, the margin will not be dilated in the z direction unless the margin size parameter is larger than 6mm.</p>
<p>Is this the correct behavior?</p>
<p>Does it make sense to instead specify the margin parameter in voxels, since it will grow in voxels? (and this operation will only work when the master representation is “binary”).</p>
<p>cc: <a class="mention" href="/u/kmacneil0102">@Kmacneil0102</a></p>

---

## Post #2 by @lassoan (2018-08-07 20:46 UTC)

<p>This is correct. Minimum margin increase/decrease is 1 voxel. For representing smaller margins, you need to set a smaller voxel size in the segmentation (conveniently using the recently added feature that allows adjusting segmentation geometry - <a href="https://github.com/Slicer/Slicer/pull/975">https://github.com/Slicer/Slicer/pull/975</a>).</p>
<p>You can see the exact number of voxels that are used in the dilation/erosion. Maybe we could display a warning message when the difference between the requested and feasible size is too large. In general, users don’t know (and don’t really care to find out) what the axis directions are and what the spacing values are along each axis, so specifing size in voxels would be too much to ask for.</p>

---

## Post #3 by @fedorov (2018-08-08 16:53 UTC)

<p>Andras, thanks! I still have two questions:</p>
<ol>
<li>Since the goal of this functionality is to add pixel layers, why is margin size specified in mm? It seems quite confusing, since margin changes only have effect in multiples of 2 of the pixel dimensions.</li>
<li>Why should the margin parameter be <strong>2 times voxel size</strong> in given direction <strong>to add a layer of 1 voxel</strong>?</li>
</ol>
<p>Those 2 issues above are very counter-intuitive to me.</p>

---

## Post #4 by @lassoan (2018-08-08 18:09 UTC)

<p>Physical space has real-world, absolute meaning, which users can directly interpret. Users should not care about voxel size, they should only make sure that voxel size is small enough to be able to represent all relevant details.</p>
<p>Kernel diameter must be an odd number, that’s why the minimum increment is two voxels.</p>

---
