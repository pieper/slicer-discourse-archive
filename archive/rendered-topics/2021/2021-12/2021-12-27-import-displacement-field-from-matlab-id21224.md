# Import displacement field from Matlab

**Topic ID**: 21224
**Date**: 2021-12-27
**URL**: https://discourse.slicer.org/t/import-displacement-field-from-matlab/21224

---

## Post #1 by @Engineer90 (2021-12-27 02:01 UTC)

<p>Hi everyone.</p>
<p>I was wondering if on 3D Slicer it was possible to import a registration matrix that I obtained with Matlab (using an optical flow algorithm), so to apply it to a segment.<br>
In my case I have three 512x512x306 matrices (pixel * pixel * number of slices), each one containing the displacements of each pixel respectively in x, y, z direction.</p>
<p>Thank you very much,<br>
kind regards</p>

---

## Post #2 by @lassoan (2021-12-28 16:44 UTC)

<p>Yes, you can import a displacement field into Slicer very easily. All you need is to save the displacement field matrix into a nrrd file using <a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/nrrdwrite.m">nrrdwrite.m</a> and <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#load-transform">load that file into Slicer as a Transform</a>.</p>

---

## Post #3 by @Engineer90 (2021-12-28 18:46 UTC)

<p>I tried with my 4D matrix 512x512x205x3 (where 3 is x, y, z displacement), and I got this error:</p>
<p><em>Undefined function ‘nrrdaddmetafield’ for input arguments of type ‘struct’.</em></p>
<p><em>Error in nrrdwrite (line 117)</em></p>
<ul>
<li>img = nrrdaddmetafield(img,‘MultiVolume.NumberOfFrames’,size(img.pixelData,4));*</li>
</ul>
<p><em>Error in PROVAnrrd (line 45)</em><br>
<em>nrrdwrite(‘testOutput_x.nrrd’, img);</em></p>
<p>So I divided the 4D displacement matrix into three 3D displacement matrices (512x512x205), each one containing x or y or z displacements. In this case nrrdwrite works.</p>
<p>However when I import one of these three matrices into 3D slicer I get this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e83640991797dc83c35107edaf5d09a09da1d74a.png" data-download-href="/uploads/short-url/x8f0vFlkPYdg4YkUiSORZwFM5ia.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e83640991797dc83c35107edaf5d09a09da1d74a_2_690x324.png" alt="image" data-base62-sha1="x8f0vFlkPYdg4YkUiSORZwFM5ia" width="690" height="324" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e83640991797dc83c35107edaf5d09a09da1d74a_2_690x324.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e83640991797dc83c35107edaf5d09a09da1d74a_2_1035x486.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e83640991797dc83c35107edaf5d09a09da1d74a_2_1380x648.png 2x" data-dominant-color="6A6B71"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×903 149 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Despite the grid origin, grid size … are correct (comparing with others transformation, for example by Elastix).</p>

---
