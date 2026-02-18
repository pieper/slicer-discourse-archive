# SlicerSALT 6.0: Summary and Changelog

**Topic ID**: 42797
**Date**: 2025-05-05
**URL**: https://discourse.slicer.org/t/slicersalt-6-0-summary-and-changelog/42797

---

## Post #1 by @bpaniagua (2025-05-05 12:47 UTC)

<p>The SlicerSALT team is proud to announce that version 6.0 is <a href="http://salt.slicer.org/download">now available for download</a>. This release introduces new features as well as bug fixes for better performance and stability. This release of SlicerSALT includes several features such as <a href="https://www.kitware.com/accelerating-the-computation-of-shape-representations-in-spharm-pdm">a faster and optimized SPherical HARMonics representation (SPHARM)</a>, updated tutorials through <a href="https://slicersalt.readthedocs.io/en/latest/">ReadTheDocs</a>, new Surface Toolbox functionality, new evolutionary skeletal representation functionality and a Difference Statistics module. The development of SlicerSALT is supported by the NIH National Institute of Biomedical Imaging Bioengineering <a href="https://reporter.nih.gov/search/LDIEcgB_fUO4Dt_BnrqzCA/project-details/10812491">R01EB021391</a> (<em>Shape Analysis Toolbox: From medical images to quantitative insights of anatomy</em>).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1d7d492a1fa210b99b4d1464380bd2be624abd6.png" data-download-href="/uploads/short-url/tWmcKSfTrcGJm95vXLxHMfGpX5Y.png?dl=1" title="Screenshot 2025-05-05 at 8.45.10 AM"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1d7d492a1fa210b99b4d1464380bd2be624abd6_2_690x295.png" alt="Screenshot 2025-05-05 at 8.45.10 AM" data-base62-sha1="tWmcKSfTrcGJm95vXLxHMfGpX5Y" width="690" height="295" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1d7d492a1fa210b99b4d1464380bd2be624abd6_2_690x295.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1d7d492a1fa210b99b4d1464380bd2be624abd6_2_1035x442.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1d7d492a1fa210b99b4d1464380bd2be624abd6_2_1380x590.png 2x" data-dominant-color="A3A3C1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-05-05 at 8.45.10 AM</span><span class="informations">1423×610 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<em>SurfaceToolbox now includes multi-mesh operations, one of them being able to compute distances to multiple meshes from a target mesh. The figure shows the absolute surface distances from two ellipsoids (source models) to a sphere in the middle (target model, in yellow)</em></p>
<h1><a name="p-124842-changelog-1" class="anchor" href="#p-124842-changelog-1" aria-label="Heading link"></a>Changelog</h1>
<h2><a name="p-124842-features-2" class="anchor" href="#p-124842-features-2" aria-label="Heading link"></a>Features</h2>
<p><a href="https://github.com/Kitware/SlicerSALT/commit/9f9e8f77125e6507a442901abc86cb9f62d7409a">Read the Docs</a> tutorials.</p>
<p><a href="https://github.com/Kitware/SlicerSALT/commit/8dcbeb44177a828d34661e9fc3490845e8eb629a">Difference Statistics module</a>, for the calculation of hypothesis testing among delta of change within a population. This module also <a href="https://github.com/Kitware/SlicerSALT/commit/a134b7919ffbc1418facf46088d97ca3ed07d240">includes sample data</a> and <a href="https://github.com/Kitware/SlicerSALT/commit/725027439224588841136e6d72da06e235e9265c">a tutorial</a>.</p>
<p><a href="https://github.com/Kitware/SlicerSALT/commit/9021674541342dad32fda1aa18b7ddf7c81eda47">New SurfaceToolbox functionality</a>, including a number of multimesh operations including multi-mesh distance computation and averages.</p>
<p>New <a href="https://github.com/Kitware/SlicerSALT/commit/4305b5a975cbd3daa559403bcac66ad7d5f2c29b">evolutionary s-reps functionality</a> included in our skeletal representation modules.</p>
<h2><a name="p-124842-fixes-3" class="anchor" href="#p-124842-fixes-3" aria-label="Heading link"></a>Fixes</h2>
<p>Updates to the <a href="https://github.com/slicersalt/RegistrationBasedCorrespondence">Registration Based Correspondence module</a>, that now includes a <a href="https://github.com/Kitware/SlicerSALT/commit/0460e8cf836256f6a3819630c89e257a34389246">tutorial</a> and <a href="https://github.com/Kitware/SlicerSALT/commit/d4e2a63eaa3f96c9048d4ce41a10964583a41af3">sample data</a>.</p>
<p>Updates to the <a href="https://github.com/Kitware/SlicerSALT/commit/09ddbe2baa90308b45fd1d82373cc5b47a0c64b5">Surface Learner module</a>, that now includes a new tutorial.</p>
<p>Speed ups to the <a href="https://github.com/Kitware/SlicerSALT/commit/a96a78a42eb8cde4c49c86b5bbfa2ae595541d56">SPHARM-PDM module</a>.</p>
<p><a href="https://github.com/Kitware/SlicerSALT/commit/7ed9adfecce2e879ebefa2726ef9d88607122399">Updates to SlicerSALT’s Slicer version</a> (5.3.0 to 5.9.0)</p>
<p>Crash fixes and stability</p>
<p>Fixes to macOS packaging</p>
<p>Fixes to Windows packaging</p>
<p>Fixes to start up errors due to WebServer</p>
<p>Fixes to modules to reflect Slicer version’s bump</p>
<p>Fixes to <a href="https://github.com/Kitware/SlicerSALT/commit/5d82e0bf78ef6234d13a43bfea8541a8aa1076fe">ModelToModelDistance</a> module to enable Difference Statistics module</p>

---
