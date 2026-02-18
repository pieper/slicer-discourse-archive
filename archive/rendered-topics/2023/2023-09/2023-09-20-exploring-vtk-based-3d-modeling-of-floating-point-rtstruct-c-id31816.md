# Exploring VTK-Based 3D Modeling of Floating-Point RTStruct Contours in 3D Slicer

**Topic ID**: 31816
**Date**: 2023-09-20
**URL**: https://discourse.slicer.org/t/exploring-vtk-based-3d-modeling-of-floating-point-rtstruct-contours-in-3d-slicer/31816

---

## Post #1 by @ranjan (2023-09-20 20:23 UTC)

<p>We are exploring how 3D Slicer handles the conversion of RTStruct contour data to 3D models, specifically concerning the handling of floating-point coordinates for each slice’s contour. Our primary questions are as follows:</p>
<p>Does 3D Slicer use a VTK process that inherently requires integer-based coordinates, or can it work directly with the floating-point values present in RTStruct files? We’ve observed that traditional methods like the marching cubes algorithm typically utilize an integer-indexed 3D grid.</p>
<p>In our own experiments, converting the floating-point contour data to an image representation necessitates rounding to whole numbers, as each pixel can only be a binary value (255 or 0). This rounding alters the resulting STL shape when meshing via the marching cubes algorithm. However, we’ve noticed that 3D Slicer appears not to round the contour points. Could you clarify whether 3D Slicer’s VTK process operates directly on contour data or if it first converts to an image representation?</p>
<p>If 3D Slicer uses the contours directly, how does it fill the surface between the inner and outer contours to create a complete 3D model?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/459a6e3d3ebd9f175e68d1944a360d0d29ac5768.jpeg" data-download-href="/uploads/short-url/9VJOjzm9OyPyQaYnasUWj1M5NG0.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/459a6e3d3ebd9f175e68d1944a360d0d29ac5768_2_690x331.jpeg" alt="image" data-base62-sha1="9VJOjzm9OyPyQaYnasUWj1M5NG0" width="690" height="331" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/459a6e3d3ebd9f175e68d1944a360d0d29ac5768_2_690x331.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/459a6e3d3ebd9f175e68d1944a360d0d29ac5768_2_1035x496.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/459a6e3d3ebd9f175e68d1944a360d0d29ac5768_2_1380x662.jpeg 2x" data-dominant-color="332F29"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1506×723 171 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2023-09-22 10:18 UTC)

<p>Hi Ranjan,</p>
<p>Some resources about segmentation representation conversion:</p>
<ul>
<li>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html" class="inline-onebox">Image Segmentation — 3D Slicer documentation</a></p>
</li>
<li>
<p><a href="https://qspace.library.queensu.ca/handle/1974/26422">https://qspace.library.queensu.ca/handle/1974/26422</a></p>
</li>
<li>
<p><a href="https://www.sciencedirect.com/science/article/abs/pii/S0169260718313038?via%3Dihub">https://www.sciencedirect.com/science/article/abs/pii/S0169260718313038?via%3Dihub</a></p>
</li>
</ul>
<p>The short answer to your question is that the RTStruct 2D contours are triangulated to closed surfaces for each segment (i.e. RT structure), thus there is no need for discretization. As long as you do not change the source representation, the closed surface representation will be a lossless interpolation of the original contour sets.</p>

---

## Post #3 by @ranjan (2023-09-25 21:45 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="31816">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>The short answer to your question</p>
</blockquote>
</aside>
<p>Thank you for your reply. That makes sense that we need to triangulate 2D contours to closed surfaces without the need for discretization. I have been trying a few methods such as delaunay after interpolation and surface reconstruction filter. Delaunay works well in 2D when trying to convert from point cloud per slice to a 2D surface as shown in the image but the interpolation when converting them to 3D doesnt work as well. Is there a recommended method for triangulating in 3D?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3fde4f82b969232ef546926d981de39e03cc60c5.png" data-download-href="/uploads/short-url/970nup5hGpCgIa8m94KUmBrDeWF.png?dl=1" title="Screenshot 2023-09-25 174444" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3fde4f82b969232ef546926d981de39e03cc60c5_2_628x500.png" alt="Screenshot 2023-09-25 174444" data-base62-sha1="970nup5hGpCgIa8m94KUmBrDeWF" width="628" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3fde4f82b969232ef546926d981de39e03cc60c5_2_628x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3fde4f82b969232ef546926d981de39e03cc60c5_2_942x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3fde4f82b969232ef546926d981de39e03cc60c5_2_1256x1000.png 2x" data-dominant-color="6C8072"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-09-25 174444</span><span class="informations">1958×1557 29.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @cpinter (2023-09-26 08:27 UTC)

<p>I don’t understand why you are trying custom methods. The built-in conversion pipeline is well tested and robust, I recommend using that. Is there a reason that it is not good enough? As we established, the floating point coordinates are preserved for the closed surface.</p>

---
