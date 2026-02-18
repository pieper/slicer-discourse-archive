# Different wall thickness

**Topic ID**: 14018
**Date**: 2020-10-13
**URL**: https://discourse.slicer.org/t/different-wall-thickness/14018

---

## Post #1 by @Andreas (2020-10-13 19:57 UTC)

<p>Hello all,</p>
<p>when measuring my vessel models, I noticed that the wall thickness deviates significantly from the nominal thickness, for example if I want to print a vessel with a wall thickness of 0.5mm , I sometimes have wall thicknesses of 0.4mm to 0.6mm.</p>
<p>What is the reason for that?</p>

---

## Post #2 by @lassoan (2020-10-13 20:36 UTC)

<p>Wall thickness must be a multiple of labelmap spacing. When you use Hollow effect, you can see both the requested and the  actual wall thickness.</p>

---

## Post #3 by @Andreas (2020-10-13 21:11 UTC)

<p>Thanks for your answer.</p>
<p>Unfortunately, your explanation did not answer my question, so I can send you two pictures to illustrate the problem. If I want to print a wall thickness of 0,5 mm and the result varies from 0,4 mm to 0,6 mm, this is not satisfactory.</p>
<p>How does this deviation come about and how can the problem be solved?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/3341d6e65e02363deb861a67029c03fb3b89f19b.jpeg" data-download-href="/uploads/short-url/7jrpviTeFNho6Z468FTcCn58Eu7.jpeg?dl=1" title="Different wall thickness" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3341d6e65e02363deb861a67029c03fb3b89f19b_2_690x464.jpeg" alt="Different wall thickness" data-base62-sha1="7jrpviTeFNho6Z468FTcCn58Eu7" width="690" height="464" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3341d6e65e02363deb861a67029c03fb3b89f19b_2_690x464.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/3341d6e65e02363deb861a67029c03fb3b89f19b.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/3341d6e65e02363deb861a67029c03fb3b89f19b.jpeg 2x" data-dominant-color="7F8894"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Different wall thickness</span><span class="informations">1002×675 78 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d29096867d11d92872fa3e879cbd9db8ef08588.jpeg" data-download-href="/uploads/short-url/mqiSMUbLKRF0wtP2Hk7GJVeEAdi.jpeg?dl=1" title="7" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d29096867d11d92872fa3e879cbd9db8ef08588_2_690x377.jpeg" alt="7" data-base62-sha1="mqiSMUbLKRF0wtP2Hk7GJVeEAdi" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d29096867d11d92872fa3e879cbd9db8ef08588_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d29096867d11d92872fa3e879cbd9db8ef08588_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d29096867d11d92872fa3e879cbd9db8ef08588_2_1380x754.jpeg 2x" data-dominant-color="898D6D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">7</span><span class="informations">1587×869 243 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2020-10-14 00:22 UTC)

<p>You choose the labelmap spacing (in Crop volume module). For very high accuracy, you can choose labelmap spacing that is a magnitude lower than the minimum wall thickness, but it may result in prohibitively large labelmap, so you may need to choose a spacing that is just 4-6x smaller than the wall thickness.</p>
<p>You may have measurement error due to inspecting a cross-section that is not exactly orthogonal to the vessel centerline. You may also have error due to finite (and anisotropic) resolution of the 3D printer and minimum wall thickness limitations.</p>
<p>These modeling errors are rarely significant (because for example you have magnitudes larger errors due to uncertainty in patient-specific material properties <em>in vivo</em>), but if you need to reproduce thin walls very accurately then you can run <a href="https://vtk.org/doc/nightly/html/classvtkLinearExtrusionFilter.html">vtkLinearExtrusionFilter</a> with <a href="https://vtk.org/doc/nightly/html/classvtkLinearExtrusionFilter.html#a4dd01aa4140f5fceb2b2b415de84dcec">SetExtrusionTypeToNormalExtrusion</a> option on the exported mesh. The disadvantage of this approach is that mesh may self-intersect, but if the wall is thin enough then this is usually not a serious problem.</p>

---

## Post #5 by @Andreas (2020-10-14 21:11 UTC)

<p>Many thanks for the help, everything worked.</p>
<p>I wanted to ask how to hide the white coordinate system (white lines).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/eccfb78d537fdcf2c6dc3d4fba7b6ba7419e6c89.jpeg" data-download-href="/uploads/short-url/xMVIj6grQJ0orct8FEu4j9dU8UF.jpeg?dl=1" title="white coordinate system" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eccfb78d537fdcf2c6dc3d4fba7b6ba7419e6c89_2_629x500.jpeg" alt="white coordinate system" data-base62-sha1="xMVIj6grQJ0orct8FEu4j9dU8UF" width="629" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eccfb78d537fdcf2c6dc3d4fba7b6ba7419e6c89_2_629x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eccfb78d537fdcf2c6dc3d4fba7b6ba7419e6c89_2_943x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/eccfb78d537fdcf2c6dc3d4fba7b6ba7419e6c89.jpeg 2x" data-dominant-color="565268"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">white coordinate system</span><span class="informations">1129×897 136 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @muratmaga (2020-10-14 21:47 UTC)

<p>You have two different white lines. The rectangles in the slice view are from an active, visible ROI. Set the visibility off in the <code>Data</code> module. You also have the bounding box enabled in the 3D viewer. You can also set that off using the little pin putton very upper left corner of your screenshot.</p>

---
