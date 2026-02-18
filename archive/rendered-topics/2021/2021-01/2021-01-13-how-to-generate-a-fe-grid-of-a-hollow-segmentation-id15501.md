# How to generate a FE grid of a hollow segmentation

**Topic ID**: 15501
**Date**: 2021-01-13
**URL**: https://discourse.slicer.org/t/how-to-generate-a-fe-grid-of-a-hollow-segmentation/15501

---

## Post #1 by @nmmhuynh (2021-01-13 12:57 UTC)

<p>Hi all,<br>
I’m new to 3D slicer and probably my issue has been already solved in the past (if so, can someone please address me to the right topic?).</p>
<p>I would like to generate a volumetric mesh of the left ventricle wall for FE analysis from a CT/MRI/else.</p>
<p>I tried to work with the CT data set from the tutorial and I was able to segment the different parts of the heart and applied the hollow procedure to somehow approximate the epi- and endocardium layers.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/88ff6e436d1dcc126f0b175d881d0f43510812c9.jpeg" data-download-href="/uploads/short-url/jxWc0Q4XF76qx8i0fKyxlaEfJax.jpeg?dl=1" title="2021-01-11-Scene1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/88ff6e436d1dcc126f0b175d881d0f43510812c9_2_501x375.jpeg" alt="2021-01-11-Scene1" data-base62-sha1="jxWc0Q4XF76qx8i0fKyxlaEfJax" width="501" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/88ff6e436d1dcc126f0b175d881d0f43510812c9_2_501x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/88ff6e436d1dcc126f0b175d881d0f43510812c9_2_751x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/88ff6e436d1dcc126f0b175d881d0f43510812c9_2_1002x750.jpeg 2x" data-dominant-color="797A84"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2021-01-11-Scene1</span><span class="informations">1343×1005 170 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>However, when I use SegmentMesher for generate the FE (either with Clever or TetGen), the model is made of a “full” left ventricle, as if it doesn’t see the interior wall (what should be the endocardium) but as the meshing procedure fills the entire volume inside the exterior surface.</p>
<p>Moreover, if this procedure is possible, I would also need to generate the index matrices of the points only on the two surfaces, but only <strong>after</strong> generating the FE grid for the volume between the two surfaces.</p>
<p>Does anyone can help me?<br>
Thank you all,<br>
Mai</p>

---

## Post #2 by @lassoan (2021-01-24 18:43 UTC)

<p>You can create volumetric meshes of thin shells but it requires you to adjust meshing parameters to create a very fine mesh. Memory usage during meshing will be high and may take 5-10 minutes to generate the mesh, but you should be able to get good results.</p>
<p>However, if you want to model a thin-walled object then probably you will get much better if you represent it with a shell model in your FE software. Simulation may be magnitudes faster and more robust. You can get the shell model by <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#export-segmentation-to-model-surface-mesh-file">exporting the segmentation to a model</a>.</p>

---
