# Neighborhood Size in median filter

**Topic ID**: 17110
**Date**: 2021-04-15
**URL**: https://discourse.slicer.org/t/neighborhood-size-in-median-filter/17110

---

## Post #1 by @Gonzalo_Rojas_Costa (2021-04-15 18:35 UTC)

<p>Hi:</p>
<p>The Neighborhood Size in the Median Filter parameters section is in voxels or mm?</p>
<p>Sincerely,</p>
<p>Gonzalo Rojas Costa</p>

---

## Post #2 by @pieper (2021-04-15 21:45 UTC)

<p>That’s based on an ITK filter of the same name and I’m pretty sure it’s in pixels.  You can try changing the spacing in the Volumes module and run the filter again and confirm you get the same result.</p>

---
