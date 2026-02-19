---
topic_id: 28305
title: "Point Coordinates In Model Imported Into The 3D Slicer Diffe"
date: 2023-03-11
url: https://discourse.slicer.org/t/28305
---

# Point coordinates in model imported into the 3D Slicer differ from the coordinates in the file

**Topic ID**: 28305
**Date**: 2023-03-11
**URL**: https://discourse.slicer.org/t/point-coordinates-in-model-imported-into-the-3d-slicer-differ-from-the-coordinates-in-the-file/28305

---

## Post #1 by @BARNEY (2023-03-11 05:32 UTC)

<p>Hi, all!<br>
I was wondering why the position point of the 3D slicer I imported directly is different from the actual one.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8dd19f2f75434fc6511ba0fd56c294139bbbafad.png" data-download-href="/uploads/short-url/keAr20EghQWbuVKAzisvo14HJUx.png?dl=1" title="2023-03-11 13.29.02" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8dd19f2f75434fc6511ba0fd56c294139bbbafad_2_622x500.png" alt="2023-03-11 13.29.02" data-base62-sha1="keAr20EghQWbuVKAzisvo14HJUx" width="622" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8dd19f2f75434fc6511ba0fd56c294139bbbafad_2_622x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8dd19f2f75434fc6511ba0fd56c294139bbbafad.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8dd19f2f75434fc6511ba0fd56c294139bbbafad.png 2x" data-dominant-color="9A9DD2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2023-03-11 13.29.02</span><span class="informations">848×681 8.93 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d78d1751d2d3af3ba8cf5900cc3b327cda03a3e.png" data-download-href="/uploads/short-url/4cIHiL11RxZePpXd5fhkvwkNHBA.png?dl=1" title="截屏2023-03-11 13.28.46" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d78d1751d2d3af3ba8cf5900cc3b327cda03a3e_2_620x500.png" alt="截屏2023-03-11 13.28.46" data-base62-sha1="4cIHiL11RxZePpXd5fhkvwkNHBA" width="620" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d78d1751d2d3af3ba8cf5900cc3b327cda03a3e_2_620x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d78d1751d2d3af3ba8cf5900cc3b327cda03a3e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d78d1751d2d3af3ba8cf5900cc3b327cda03a3e.png 2x" data-dominant-color="9A9DD2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">截屏2023-03-11 13.28.46</span><span class="informations">844×680 7.66 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c3326d3c40512f51069f4022fa5b1407b194eb4c.png" data-download-href="/uploads/short-url/rQN915Hr3bC3xELAoHkXqaznuQ4.png?dl=1" title="截屏2023-03-11 13.29.35" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c3326d3c40512f51069f4022fa5b1407b194eb4c.png" alt="截屏2023-03-11 13.29.35" data-base62-sha1="rQN915Hr3bC3xELAoHkXqaznuQ4" width="557" height="499" data-dominant-color="2C2C2C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">截屏2023-03-11 13.29.35</span><span class="informations">592×531 12 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>As shown in the figure, the red dot represents a model I imported into slicer (vtk format), which is represented by 6 dots, respectively 0.00 0.00 0.00, -0.04 0.33 1.10, -0.15 1.22 1.82,<br>
-0.30 2.35 1.92, -0.42 3.35 1.37, -0.49 3.87 0.35, the red cubes in the pictures.<br>
But I visualized the points by entering the X, Y, Z coordinate values, and found that there was a difference between them, specifically the X and Y values turned negative.<br>
So? Is there something wrong in the transform hierarchy？<br>
Any advice will be great! Thank you！</p>

---

## Post #2 by @lassoan (2023-03-11 06:30 UTC)

<p>Almost all medical image computing software standardized on using LPS coordinate system in files. Slicer follows this convention. If coordinate values in your model file are in RAS coordinate system and you don’t want to change that then you can indicate this in the file header. See more information at these links:</p>
<ul>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer#Slicer_5.0:_Models_are_saved_in_LPS_coordinate_system_by_default" class="inline-onebox">Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer - Slicer Wiki</a></li>
<li><a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html#models" class="inline-onebox">Data Loading and Saving — 3D Slicer documentation</a></li>
</ul>

---

## Post #3 by @BARNEY (2023-03-12 09:02 UTC)

<p>That is very helpful! Thank you very much!</p>

---
