# Do we need to create an isotropic image in radiomics study?

**Topic ID**: 1779
**Date**: 2018-01-08
**URL**: https://discourse.slicer.org/t/do-we-need-to-create-an-isotropic-image-in-radiomics-study/1779

---

## Post #1 by @MimiPoon (2018-01-08 02:54 UTC)

<p>Hi,</p>
<p>As medical images are usually anisotropic images, do we need to convert images to isotropic ones for the purpose of texture analysis? Does Radiomics module take care of it?<br>
If it is needed to convert the images, which module should I use?<br>
Thanks!</p>

---

## Post #2 by @lassoan (2018-01-08 03:25 UTC)

<p>For certain operations, such as segmentation and surface model generation, it is highly recommended to resample to have uniform spacing. For other operations it may not be necessary.</p>
<p>All algorithms in Slicer that I know of operate in physical space (anisotropic spacing information is taken into account), so resampling usually only slightly affects results.</p>
<p>You can try to resample to uniform spacing using Crop volume module and see how much difference it makes.</p>

---

## Post #3 by @JoostJM (2018-01-17 13:32 UTC)

<p>The Radiomics module uses <a>PyRadiomics</a> as back-end to calculate features. It supports resampling to isotropic voxels (which is recommended when extracting textures in 3D) or a forced 2D extraction (only requiring isotropic in-plane spacing). Both these settings are switched off by default.</p>
<p>Resampling can be enabled by specifying the resampled spacing in the configuration. forced 2D extraction is only possible when using the parameter file for customization.</p>
<p>In the latest version of the Radiomics module (obtainable via the slicer nightly build), a PyRadiomics parameter file can be used to customize the extraction. Some examples can be found <a href="https://github.com/Radiomics/pyradiomics/tree/master/examples/exampleSettings" rel="nofollow noopener">here</a></p>

---

## Post #4 by @hugo_Schmutz (2023-09-02 10:10 UTC)

<p>Hi,</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a>, can you explain why resampling is highly recommended for segmentation?</p>

---

## Post #5 by @lassoan (2023-09-02 11:15 UTC)

<p>If your image has anisotropic spacing then it is made up of sticks instead of cubes. This can introduce various artifacts (e.g., staircase artifact in reconstructed 3D surface), inaccuracies (when you measure distances from a position then along the axes where the spacing is larger, the measurement will be less accurate), and unnecessary computations (if you have lower resolution along one axis then you cannot really make use of higher resolution in other axes).</p>

---
