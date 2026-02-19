---
topic_id: 9768
title: "Problem Exporting Colorized Tractography To Ply Mesh"
date: 2020-01-10
url: https://discourse.slicer.org/t/9768
---

# Problem exporting Colorized tractography to PLY mesh

**Topic ID**: 9768
**Date**: 2020-01-10
**URL**: https://discourse.slicer.org/t/problem-exporting-colorized-tractography-to-ply-mesh/9768

---

## Post #1 by @tabildskov (2020-01-10 02:41 UTC)

<p>Hello - While I can export the the tractography to a PLY mesh, the fiber bundle coloring does not always do what is expected. It always seems to color fibers by mean orientation not by segment orientation, not by tensor property (ColorOrientation, FractionalAnisotropy, Trace, etc.) It is possible that it is working fine but when I use the latest version of MeshLab 2016.12 the colors do not come through as expected. Is this a bug or am I just doing something wrong? FYI, I am more inclined to think it is me and I am missing a step or two. Thanks.</p>

---

## Post #2 by @pieper (2020-01-10 19:41 UTC)

<p>Hi - I haven’t played a lot with this, but from <a href="https://github.com/SlicerDMRI/SlicerDMRI/blob/master/Modules/Scripted/TractographyExportPLY/TractographyExportPLY.py#L174-L203">a look at the code</a> it gets the scalar display mode from the line display (not the tube display as you might expect).</p>

---

## Post #3 by @tabildskov (2020-01-13 20:40 UTC)

<p>That makes a lot of sense and matches my experience. I was able to get colored lines to export fine.</p>
<p>Thank You Steve.</p>

---
