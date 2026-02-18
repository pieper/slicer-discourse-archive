# Extract isosurface(or contour surface) from skin segment by MarchingCube

**Topic ID**: 27763
**Date**: 2023-02-11
**URL**: https://discourse.slicer.org/t/extract-isosurface-or-contour-surface-from-skin-segment-by-marchingcube/27763

---

## Post #1 by @Slicer360 (2023-02-11 10:16 UTC)

<p>Tasks:<br>
The facial skin was segmented from the craniofacial CT image, and the.ply/.stl file was obtained for registration with the actual face point cloud collected by the depth camera.<br>
Question:<br>
In the Segmentation module Representations of Slicer 4.11, there are only three options: Binary labelmap,Closed surface and Fractional labelmap. Figure 1(but I see in the Slicer document Image Segmentation section that there are also Planar contour and Ribbon model options, Figure 2). When I exported the skin Segment, since Slicer automatically selected Closed surface, the generated model was layered, as shown in Figure 3. This stratification creates two similar-shaped face point clouds in the point cloud, which can affect registration.<br>
Figure 1<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/80a4351c884851ec4dffef520d6ff237780b3c56.png" alt="image" data-base62-sha1="im0VBqG1VariMOM88CiDy7UxN42" width="555" height="220"><br>
Figure 2<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/590d05b343f626cceb6cecbcfdc42358f23a75e3.png" data-download-href="/uploads/short-url/cHMoub3sNMqoHwnkrCqyqf8C1Nh.png?dl=1" title="20230211_175645" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/590d05b343f626cceb6cecbcfdc42358f23a75e3_2_690x225.png" alt="20230211_175645" data-base62-sha1="cHMoub3sNMqoHwnkrCqyqf8C1Nh" width="690" height="225" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/590d05b343f626cceb6cecbcfdc42358f23a75e3_2_690x225.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/590d05b343f626cceb6cecbcfdc42358f23a75e3_2_1035x337.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/590d05b343f626cceb6cecbcfdc42358f23a75e3_2_1380x450.png 2x" data-dominant-color="E6EDE8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20230211_175645</span><span class="informations">1467×480 165 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Figure3<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d764ec9a5050f555923fe5e41cd221ff02f1d660.jpeg" data-download-href="/uploads/short-url/uJsST8tqMrrHQweqPbtaR1lvqLu.jpeg?dl=1" title="20230211_175917" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d764ec9a5050f555923fe5e41cd221ff02f1d660_2_690x470.jpeg" alt="20230211_175917" data-base62-sha1="uJsST8tqMrrHQweqPbtaR1lvqLu" width="690" height="470" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d764ec9a5050f555923fe5e41cd221ff02f1d660_2_690x470.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d764ec9a5050f555923fe5e41cd221ff02f1d660_2_1035x705.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d764ec9a5050f555923fe5e41cd221ff02f1d660.jpeg 2x" data-dominant-color="768594"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20230211_175917</span><span class="informations">1353×923 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/5832723ce509fbd09e24fdfd312a6cd3d5024bc7.png" data-download-href="/uploads/short-url/cAe64BUyqPo9gI0CS8aEDJUC9G7.png?dl=1" title="20230211_180307" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/5832723ce509fbd09e24fdfd312a6cd3d5024bc7.png" alt="20230211_180307" data-base62-sha1="cAe64BUyqPo9gI0CS8aEDJUC9G7" width="678" height="500" data-dominant-color="5F5F92"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20230211_180307</span><span class="informations">1135×837 311 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
When the MarchingCube algorithm of VS+VTK was used for skin contour surface extraction of CT images, it was found that the obtained point cloud only had one layer, as shown in FIG. 4(what I hope to obtain is similar to the point cloud obtained by depth camera). Therefore, I hope that in Slicer, MarchingCube is also used to export the single-layer isosurface model file for the segmtioned skin Segment. However, I have never found the implementation method of MarchingCube in Slicer.<br>
Figure 4<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a1ca18dc65006e6ba63b180f95cd74b84082ff3.png" data-download-href="/uploads/short-url/f8HX7PMWeiutXZjziWd367yxnXl.png?dl=1" title="20230211_180938" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a1ca18dc65006e6ba63b180f95cd74b84082ff3.png" alt="20230211_180938" data-base62-sha1="f8HX7PMWeiutXZjziWd367yxnXl" width="609" height="500" data-dominant-color="605F91"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20230211_180938</span><span class="informations">974×799 223 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I hope some friends can give me some suggestions. Is there something wrong with my Slicer version, which lacks Planar contour and Ribbon model? And is there a way to call MarchingCube in Slicer to extract isosurfaces for the skin Segment?</p>

---

## Post #2 by @lassoan (2023-02-11 19:56 UTC)

<p>To extract the skin surface, you need to fill all the internal holes. You can do that using the “Wrap Solidify” effect, provided by SurfaceWrapSolidify extension. See detailed step-by-step instructions <a href="https://lassoan.github.io/SlicerSegmentationRecipes/SkinSurface2/">here</a>.</p>

---

## Post #3 by @Slicer360 (2023-02-12 09:03 UTC)

<p>Thank you very much. Your advice is very effective. As a beginner, I am not familiar with 3D Slicer, and I did not expect this simple and efficient method of completely filling the whole head. Thank you again for your help.</p>

---

## Post #4 by @lassoan (2024-04-26 05:30 UTC)

<p>A post was split to a new topic: <a href="/t/extract-face-from-cbct/35743">Extract face from CBCT</a></p>

---
