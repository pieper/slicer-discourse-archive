---
topic_id: 25546
title: "Extract Centerline Fails When Calculating The Centerline Wit"
date: 2022-10-04
url: https://discourse.slicer.org/t/25546
---

# Extract Centerline fails when calculating the centerline with "Tree" window

**Topic ID**: 25546
**Date**: 2022-10-04
**URL**: https://discourse.slicer.org/t/extract-centerline-fails-when-calculating-the-centerline-with-tree-window/25546

---

## Post #1 by @dalbenzioG (2022-10-04 15:56 UTC)

<p>Hello,</p>
<p>I am encountering the following error while computing the Centerline Model (from window tab <em>Tree</em>) from a segmentation node:<br>
<strong>Warning: In /home/davagh/built/Slicer-build041022/VTK/Filters/Core/vtkDelaunay3D.cxx, line 518</strong><br>
<strong>vtkDelaunay3D (0x55ecfe6ff650): 241 degenerate triangles encountered, mesh quality suspect</strong><br>
<strong>Error while constructing cell map: Invalid cell size for polys.</strong></p>
<p>The following are few tests I made for trying to find a possible solution:</p>
<ul>
<li>
<p>If no smoothing is applied to the segmentation, I am able to generate the below Centerline Network using the <em>Auto-Detect</em> option for detecting the end points:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/074cb663221e3323b0c1535668a5f055041fe84d.jpeg" data-download-href="/uploads/short-url/12zHgXjwFoh5dzpGylGjuCQBwTz.jpeg?dl=1" title="image_00033" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/074cb663221e3323b0c1535668a5f055041fe84d_2_647x500.jpeg" alt="image_00033" data-base62-sha1="12zHgXjwFoh5dzpGylGjuCQBwTz" width="647" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/074cb663221e3323b0c1535668a5f055041fe84d_2_647x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/074cb663221e3323b0c1535668a5f055041fe84d_2_970x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/074cb663221e3323b0c1535668a5f055041fe84d.jpeg 2x" data-dominant-color="8B97CE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image_00033</span><span class="informations">1174×906 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
</li>
<li>
<p>If no smoothing is applied to the segmentation, I am able to generate the below Centerline Network using the 4 displayed control points:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e7cf3c1138a766792ece40670092a962b8cc7ee.jpeg" data-download-href="/uploads/short-url/bckWZsNkwOR7a61JPsKOny4OCWq.jpeg?dl=1" title="image_00031" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e7cf3c1138a766792ece40670092a962b8cc7ee_2_647x500.jpeg" alt="image_00031" data-base62-sha1="bckWZsNkwOR7a61JPsKOny4OCWq" width="647" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e7cf3c1138a766792ece40670092a962b8cc7ee_2_647x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e7cf3c1138a766792ece40670092a962b8cc7ee_2_970x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e7cf3c1138a766792ece40670092a962b8cc7ee.jpeg 2x" data-dominant-color="8895CC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image_00031</span><span class="informations">1174×906 161 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
</li>
<li>
<p>If 0.3 smoothing is applied (from Segment Editor), I am able to generate the green Centerline Model (from window tab <em>Tree</em>) using the same 4 control points:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b762166e6ea1829ba75ef399b4d78fcc4339856.jpeg" data-download-href="/uploads/short-url/hCbOYHH0oZ5ttmqSciTMnMMyVUO.jpeg?dl=1" title="image_00032" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b762166e6ea1829ba75ef399b4d78fcc4339856_2_647x500.jpeg" alt="image_00032" data-base62-sha1="hCbOYHH0oZ5ttmqSciTMnMMyVUO" width="647" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b762166e6ea1829ba75ef399b4d78fcc4339856_2_647x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b762166e6ea1829ba75ef399b4d78fcc4339856_2_970x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b762166e6ea1829ba75ef399b4d78fcc4339856.jpeg 2x" data-dominant-color="8797CA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image_00032</span><span class="informations">1174×906 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
</li>
</ul>
<p>It seems that smoothing the surface could work around this problem. However, there are few cases where a smoothing is not the preferred choice for surgeons (like in this case).<br>
I am wondering: which factor could define a <em>“good enough”</em> smoothing, in order not to fail the extractCenterline method?</p>
<p>I appreciate if you could provide any feedback on this or even point out a vmtk link/documentation that could help me to better understand the problem. <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=12" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20"></p>
<p><strong>OS: Ubuntu 22.04.1 LTS<br>
Graphics: NVIDIA [GeForce RTX 3090]</strong></p>

---
