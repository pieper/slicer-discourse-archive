# The coordinates of points in stl model after voxelization

**Topic ID**: 17515
**Date**: 2021-05-08
**URL**: https://discourse.slicer.org/t/the-coordinates-of-points-in-stl-model-after-voxelization/17515

---

## Post #1 by @wangyunning (2021-05-08 02:58 UTC)

<p>Hello everyone, I am learning about computer-assisted spine surgery planning.in slicer, how to obtain the coordinates of points on the intersection line between the plane and the STL model.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43ce46c38ce3f5552503a98bd53bc0f18d5fad4f.png" alt="image" data-base62-sha1="9FPW0SZGMPFVBi2mDNbVwuxvv43" width="372" height="263"></p>
<p>The positional relationship between the plane and the model is shown in the figure. The red line in the figure represents a plane perpendicular to the screen. I want to get the coordinates of this plane so that I can guide the path planning of the laminar grinding surgical robot.<br>
Sir, could you give me some guidance(<a class="mention" href="/u/lassoan">@lassoan</a>).</p>
<p>A little help appreciated!Thank you!</p>

---

## Post #2 by @lassoan (2021-05-13 05:02 UTC)

<p>You can use IntersectWithLine function in VTK - see this <a href="https://discourse.slicer.org/t/intersection-between-markups-closed-curve-node-on-the-plane-and-a-line/11281/5">post</a>. There are many examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">script repository</a> to show how you can set up a locator.</p>
<p>You can do much more sophisticated analysis of the pedicle screw trajectory, for example analyze bone density traversed by the screw (not just a line but an actual screw shape), as it is done in <a href="https://github.com/lassoan/PedicleScrewSimulator">Pedicle screw simulator extension</a>.</p>

---
