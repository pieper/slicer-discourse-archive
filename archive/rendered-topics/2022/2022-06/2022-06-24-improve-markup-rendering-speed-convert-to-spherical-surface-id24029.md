# Improve Markup Rendering Speed (convert to spherical surface?)

**Topic ID**: 24029
**Date**: 2022-06-24
**URL**: https://discourse.slicer.org/t/improve-markup-rendering-speed-convert-to-spherical-surface/24029

---

## Post #1 by @skeltoh (2022-06-24 16:17 UTC)

<p>I have a bunch of RAS space coordinates (~1000) that I want to render on top of an MRI, atlas, and surfaces from 3D segmentation. I can make them into an .fcsv and import them into Markups, and they show up appropriately, but it’s extremely slow to do anything (sometimes it will hang for minutes if I pan the image).</p>
<p>How could I do this in a way that’s less computationally intensive? I’m thinking if I just had the marker spheres as voxel data, it would render fine, is there a built in way to “export” the markup glyphs as voxels or surfaces?</p>

---

## Post #2 by @lassoan (2022-06-24 16:43 UTC)

<p>Do you use the latest Slicer Stable Release? Rendering of markups with many points may be slower in earlier versions.</p>
<p>You can further speed up rendering by:</p>
<ul>
<li>hiding point labels: Markups module → Display → Advanced → Control Point Labels → uncheck)</li>
<li>locking the control points (disable interaction): Markups module → Control Points → Interaction → click the first icon so it appears as a closed lock</li>
</ul>

---
