# Obtain single-voxel surface/shell of a segmentation

**Topic ID**: 34411
**Date**: 2024-02-19
**URL**: https://discourse.slicer.org/t/obtain-single-voxel-surface-shell-of-a-segmentation/34411

---

## Post #1 by @Young_Wang (2024-02-19 21:15 UTC)

<p>Hi, I’m currently working on an image segmentation project where my objective is to extract only the outermost points (single-voxel surface) from a given segmentation. The ideal outcome is to achieve a shell or contour that resembles the segmentation but without any slice fill.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a40ad0c8c901eb32f9f9771b20881a828dff8a01.jpeg" data-download-href="/uploads/short-url/npbtB5TRyhsq9b1pXN8QvQx97IR.jpeg?dl=1" title="slice fill off" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a40ad0c8c901eb32f9f9771b20881a828dff8a01_2_582x500.jpeg" alt="slice fill off" data-base62-sha1="npbtB5TRyhsq9b1pXN8QvQx97IR" width="582" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a40ad0c8c901eb32f9f9771b20881a828dff8a01_2_582x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a40ad0c8c901eb32f9f9771b20881a828dff8a01_2_873x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a40ad0c8c901eb32f9f9771b20881a828dff8a01_2_1164x1000.jpeg 2x" data-dominant-color="1E1E1E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slice fill off</span><span class="informations">1670×1434 183 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So far, I’ve experimented with two different approaches:</p>
<p><strong>Approach One</strong>: This involved obtaining the segmentation through intensity thresholding, followed by a hollow operation. However, I haven’t specified the tools or parameters used here, which might be crucial for understanding the process and its pitfalls.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/67ce0b7bccf1a2d62bd295e84e66e7577e13133a.jpeg" data-download-href="/uploads/short-url/eOiCY3QZmV5H1AvOv5xzC11kBm2.jpeg?dl=1" title="hallow" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67ce0b7bccf1a2d62bd295e84e66e7577e13133a_2_582x500.jpeg" alt="hallow" data-base62-sha1="eOiCY3QZmV5H1AvOv5xzC11kBm2" width="582" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67ce0b7bccf1a2d62bd295e84e66e7577e13133a_2_582x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67ce0b7bccf1a2d62bd295e84e66e7577e13133a_2_873x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67ce0b7bccf1a2d62bd295e84e66e7577e13133a_2_1164x1000.jpeg 2x" data-dominant-color="1E1F1E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">hallow</span><span class="informations">1670×1434 231 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<strong>Approach Two</strong>: In this method, I again started with intensity thresholding, but this time followed it with Surface Wrap Solidify. I experimented with various parameters, but the results were not as successful as I had hoped. It would be beneficial to detail the specific parameters and the software used, as well as the issues encountered with this approach.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9cf83d2b0100605f90521a77b36040c993ad11d1.jpeg" data-download-href="/uploads/short-url/moCkLcFsCgtSNMFKgvFcwVCawut.jpeg?dl=1" title="Solidify" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9cf83d2b0100605f90521a77b36040c993ad11d1_2_569x500.jpeg" alt="Solidify" data-base62-sha1="moCkLcFsCgtSNMFKgvFcwVCawut" width="569" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9cf83d2b0100605f90521a77b36040c993ad11d1_2_569x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9cf83d2b0100605f90521a77b36040c993ad11d1_2_853x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9cf83d2b0100605f90521a77b36040c993ad11d1_2_1138x1000.jpeg 2x" data-dominant-color="21211E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Solidify</span><span class="informations">1670×1466 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’m seeking advice or suggestions on how to improve these methods or alternative techniques that could help in accurately extracting the most exterior points of a segmentation. Any insights or recommendations would be greatly appreciated.</p>

---

## Post #2 by @muratmaga (2024-02-20 00:30 UTC)

<p>WrapSurfaceSolidy shell option would work well for this. After your threshold, run some dilation/erosion and closing operations to fill the interior. Then you should be able extract a single voxel thick shell with WrapSurfaceSolidify</p>

---

## Post #3 by @Young_Wang (2024-02-20 14:41 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> . Thank you for your suggestion regarding the use of WrapSurfaceSolidify. I implemented this approach, but encountered unexpected results in the segmentation process. As illustrated in Figure 3, the segmentation is characterized by unusual yellow contour lines. This outcome differs significantly from the anticipated results. I would appreciate any insights or recommendations you might have to address this issue.</p>

---

## Post #4 by @muratmaga (2024-02-20 15:56 UTC)

<p>One problem is your structure of interest is touching the boundaries of your image. So operations like dilation, closing etc that WrapSurfaceSolidfy also relies on is failing (they have no place to grow the label).</p>
<p>Pad your image (you can use cropvolume for that), and try what i suggested</p>

---

## Post #5 by @Young_Wang (2024-02-20 16:08 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> Thank you again for that. I’ll give it a try. On a related note, I’m curious about the possibility of cropping the segmentation to a specific region of interest (ROI). One problem I encountered during image registration is this: I need a larger ROI for initial registration to better understand the surrounding anatomical structures. However, when it comes to segmentation and subsequently quantifying the results, I want to zoom in or crop the segmentation. This is to avoid an almost perfect Hausdorff distance resulting from a large portion of similar points from the surrounding anatomical structures. I came across a few posts made by others and saw one of your suggestions. I tried specifying the region of interest after performing segmentation, but it alters the resolution of my segmentation. Any advice would be appreciated.</p>

---
