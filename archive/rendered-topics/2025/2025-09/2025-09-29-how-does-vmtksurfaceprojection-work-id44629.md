---
topic_id: 44629
title: "How Does Vmtksurfaceprojection Work"
date: 2025-09-29
url: https://discourse.slicer.org/t/44629
---

# how does vmtksurfaceprojection work

**Topic ID**: 44629
**Date**: 2025-09-29
**URL**: https://discourse.slicer.org/t/how-does-vmtksurfaceprojection-work/44629

---

## Post #1 by @furiabuia (2025-09-29 23:48 UTC)

<p>Hi, I’m new to vmtk and I was trying to use vmtksurfaceprojection to project coordinates points of a centerline to another centerline. The problem is that what I obtain in output is a centerline with the same geometry and coordinates point of the centerline that I put after “-ifile”.</p>
<p>Someone told me to modify the name of coordinates of one of the centerline (for example in x_c, y_c, z_c), and I’ve done this with the filter calculator in paraview, but when I use this new .vtp file I got an error in pypepad that says ‘No cells to subdivide’.</p>
<p>I’ve even tryed all these different solution with a 3d model (not a simple centerline) because I thought that maybe the problem could be the fact that I’m using a centerline but I got the same result.</p>
<p>what I am doing wrong?</p>

---
