# Volume rendering and ROI points

**Topic ID**: 27244
**Date**: 2023-01-14
**URL**: https://discourse.slicer.org/t/volume-rendering-and-roi-points/27244

---

## Post #1 by @a.mohseni (2023-01-14 22:45 UTC)

<p>Is it possible to showcase an ROI and then make it static, so I can use a segmentation label inside of that ROI?</p>
<p>Now when i try to put a label inside of the markers of the ROI it moves them when using the scissor tool.</p>

---

## Post #2 by @jamesobutler (2023-01-14 22:54 UTC)

<p>In the Markups module you can either</p>
<ul>
<li>
<p>turn off the visibility of the interaction handles<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html#display-section" class="inline-onebox" rel="noopener nofollow ugc">Markups — 3D Slicer documentation</a></p>
</li>
<li>
<p>set the interaction state to be locked<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html#control-points-section" class="inline-onebox" rel="noopener nofollow ugc">Markups — 3D Slicer documentation</a></p>
</li>
</ul>

---
