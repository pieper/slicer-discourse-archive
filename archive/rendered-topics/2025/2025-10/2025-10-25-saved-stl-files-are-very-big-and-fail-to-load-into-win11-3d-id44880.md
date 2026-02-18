# Saved stl files are very big and fail to load into win11 3D viewer

**Topic ID**: 44880
**Date**: 2025-10-25
**URL**: https://discourse.slicer.org/t/saved-stl-files-are-very-big-and-fail-to-load-into-win11-3d-viewer/44880

---

## Post #1 by @FinnR (2025-10-25 14:11 UTC)

<p>Operating system: Windows 11<br>
Slicer version: 5.8<br>
Expected behavior: exported .stl  should be viewable in, e.g., Win 11 3D viewer.<br>
Actual behavior: The exported .stl’s  are huge (c. 5 GB, or 2.5 GB if “only visible slices” are ticked off). I have tried Exocad, Meshmixer and 3D paint, same prblem. I have also tried saving as .obj with the same result.</p>

---

## Post #2 by @lassoan (2025-10-25 14:19 UTC)

<p>After thresholding, it is recommended to use the Smoothing effect to reduce surface roughness. The default Median method should be suitable.</p>
<p>After this, you can further reduce the number of triangles in the mesh using Surface toolbox module using decomation or unfiform remeshing. Usually you can reduce the number of triangles by 90-95% with minimal visible change. Often you can go up to 99-99.9% reduction if you can accept some quality loss.</p>

---

## Post #3 by @FinnR (2025-10-26 20:26 UTC)

<p>Thank you - after applying median smoothing the saved .stl file is much smaller (c. 708 Kb) and loads in Windows 3D viewer with no problems. But it actually looks better in 3D Slicer, in 3D Viewer the object is covered with what loks like contour lines.<br>
I would have tried decimation and uniforn remesh in Surface toolbox too, but the the “toggle models” and the “Apply” bars are greyed out. What may cause this?</p>

---

## Post #4 by @lassoan (2025-10-26 21:21 UTC)

<aside class="quote no-group" data-username="FinnR" data-post="3" data-topic="44880">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/fbc32d/48.png" class="avatar"> FinnR:</div>
<blockquote>
<p>3D Viewer the object is covered with what loks like contour lines</p>
</blockquote>
</aside>
<p>Please attach a screenshot to show what you mean.</p>
<aside class="quote no-group" data-username="FinnR" data-post="3" data-topic="44880">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/fbc32d/48.png" class="avatar"> FinnR:</div>
<blockquote>
<p>the “toggle models” and the “Apply” bars are greyed out</p>
</blockquote>
</aside>
<p>You need to select/create an output model.</p>

---
