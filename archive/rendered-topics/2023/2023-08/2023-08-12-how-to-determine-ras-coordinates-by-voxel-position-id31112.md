# How to determine RAS coordinates by voxel position

**Topic ID**: 31112
**Date**: 2023-08-12
**URL**: https://discourse.slicer.org/t/how-to-determine-ras-coordinates-by-voxel-position/31112

---

## Post #1 by @slicer365 (2023-08-12 01:06 UTC)

<p>Throughout the scene, the center point of each voxel has a corresponding RAS coordinate, and I can place a marker point anywhere to see the RAS coordinates of that location.<br>
Now I have a requirement, and I want to loop to find out the location of the maximum CT value in the current 2D view and display its RAS coordinates.<br>
For example, in the following picture, I found this voxel position, and I need to calculate its approximate RAS coordinates, and the error is permissible, because this voxel is not a point, but a very small rectangular region.<br>
Relative to the whole matrix, its position is (346,235,136), and I need to get its approximate RAS coordinates, which can be the coordinates of any point in the whole voxel, or its central coordinates.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76e25602c5d2b77a99d915798c2345fc76e04ca8.png" data-download-href="/uploads/short-url/gXHgnfAHQjZJTjS9MHhyX2jRGsM.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76e25602c5d2b77a99d915798c2345fc76e04ca8_2_690x412.png" alt="image" data-base62-sha1="gXHgnfAHQjZJTjS9MHhyX2jRGsM" width="690" height="412" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76e25602c5d2b77a99d915798c2345fc76e04ca8_2_690x412.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76e25602c5d2b77a99d915798c2345fc76e04ca8_2_1035x618.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76e25602c5d2b77a99d915798c2345fc76e04ca8_2_1380x824.png 2x" data-dominant-color="A4A3A4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1662×994 92.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2023-08-12 15:44 UTC)

<p>You can look at the code of the DataProbe module, and also this example should help:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-reformatted-image-from-a-slice-viewer-as-numpy-array" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-reformatted-image-from-a-slice-viewer-as-numpy-array</a></p>

---
