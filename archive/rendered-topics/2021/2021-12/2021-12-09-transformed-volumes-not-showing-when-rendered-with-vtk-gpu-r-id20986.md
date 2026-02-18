# Transformed Volumes Not Showing when Rendered with VTK GPU Ray Casting

**Topic ID**: 20986
**Date**: 2021-12-09
**URL**: https://discourse.slicer.org/t/transformed-volumes-not-showing-when-rendered-with-vtk-gpu-ray-casting/20986

---

## Post #1 by @jasoncox13 (2021-12-09 21:24 UTC)

<p>Operating system: Windows</p>
<p>Slicer version: 4.13.0-2021-11-18</p>
<p>Expected behavior: After applying a centering transform to an eligible volume in the Volumes module, switching to the Transforms module and selecting “volume name” centering transform should display “volume name” under the list of Transformed volumes.</p>
<p>Actual behavior: After applying a centering transform to an eligible volume in the Volumes module, switching to the Transforms module and selecting “volume name” centering transform does not display “volume name” under the list of Transformed volumes if “volume name” has been rendered with VTK GPU Ray Casting in the Volume Rendering module. This issue occurs with .AIM and SEG.AIM volume formats using the CT-AAA rendering preset. The issue can be easily fixed by switching “volume name” to VTK CPU Ray Casting in the Volume Rendering module.</p>

---

## Post #2 by @dzenanz (2021-12-15 16:10 UTC)

<p>I guess that the biggest problem of this issue is that it confuses the user. Does this need to be submitted to the issue tracker?</p>

---

## Post #3 by @jasoncox13 (2021-12-15 17:22 UTC)

<p>The solution is a bit unintuitive and I only happened across it by chance, so it might be worthwhile to let the devs know.</p>

---

## Post #4 by @jasoncox13 (2021-12-15 17:26 UTC)

<p>Posted this issue to the issue tracker as of 12/15/2021</p>

---

## Post #5 by @lassoan (2021-12-16 17:34 UTC)

<p>Could you perhaps take a screen capture video of your workflow? I’m not sure if what you described is the intended behavior (and the issue is documentation or usability) or if there is a software problem.</p>

---
