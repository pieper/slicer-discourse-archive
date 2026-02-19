---
topic_id: 34967
title: "Control Point Grid Output From Niftyreg Not Loaded Correctly"
date: 2024-03-19
url: https://discourse.slicer.org/t/34967
---

# Control point grid output from NiftyReg not loaded correctly

**Topic ID**: 34967
**Date**: 2024-03-19
**URL**: https://discourse.slicer.org/t/control-point-grid-output-from-niftyreg-not-loaded-correctly/34967

---

## Post #1 by @koeglfryderyk (2024-03-19 07:20 UTC)

<p>I’m integrating <a href="http://cmictig.cs.ucl.ac.uk/wiki/index.php/NiftyReg_documentation" rel="noopener nofollow ugc">NiftyReg</a> into an extension.</p>
<p>I registered two images with <a href="http://cmictig.cs.ucl.ac.uk/wiki/index.php/Reg_f3d" rel="noopener nofollow ugc">f3d</a> and saved the control point grid (to later get the deformation).</p>
<p>However, the grid isn’t loaded correctly into Slicer. In the Data module it says that it has dimensions (55, 55, 26), however, it actually has dimensions (55, 55, 26, 1, 3) if you extract the data array.</p>
<p>Is this a problem with Slicer or is the output just not according to some standards?</p>
<p>Here’s a <a href="https://www.dropbox.com/scl/fi/9gtq37lw1bct1cj0743c9/controlPointGrid.nii?rlkey=enukco6xnp11yyeh0dg81sing&amp;dl=0" rel="noopener nofollow ugc">link</a> to the control point grid output.</p>

---

## Post #2 by @koeglfryderyk (2024-03-21 07:59 UTC)

<p>I actually needed the displacement field anyway, and the way to get it and use it is described in this <a href="https://discourse.slicer.org/t/deforming-with-niftyreg-is-different-than-deforming-in-slicer/34992/3">issue</a></p>

---
