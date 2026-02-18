# Low Resolution Brain

**Topic ID**: 35323
**Date**: 2024-04-06
**URL**: https://discourse.slicer.org/t/low-resolution-brain/35323

---

## Post #1 by @chemicalsam (2024-04-06 14:56 UTC)

<p>Hello, I am using Swiss Skull Stripper and Slicer to isolate my brain file for a project, however the resolution is quite low when creating the 3D object.</p>
<p>I have tried all different files from the MRI folder and different thresholds but they all come out the same.</p>
<p>Thanks</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/82652eb6933e8a86bd15ec55e92541ff4462592e.png" data-download-href="/uploads/short-url/iBwQVgDAMgrlMRgtbDJ0pVBAHxQ.png?dl=1" title="CleanShot 2024-04-06 at 10.51.10@2x" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82652eb6933e8a86bd15ec55e92541ff4462592e_2_556x500.png" alt="CleanShot 2024-04-06 at 10.51.10@2x" data-base62-sha1="iBwQVgDAMgrlMRgtbDJ0pVBAHxQ" width="556" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82652eb6933e8a86bd15ec55e92541ff4462592e_2_556x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82652eb6933e8a86bd15ec55e92541ff4462592e_2_834x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/82652eb6933e8a86bd15ec55e92541ff4462592e.png 2x" data-dominant-color="7D8D9D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">CleanShot 2024-04-06 at 10.51.10@2x</span><span class="informations">1008×906 271 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-04-06 15:03 UTC)

<p>The output resolution is the same as the input resolution. You can <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">increase the segmentation resolution</a> and apply smoothing to remove the staircase artifacts, but it will not be able to reproduce any of the missing details in thick-slice images.</p>
<p>Note that you can also use AI segmentation tools for skull stripping, such as <a href="https://github.com/lassoan/SlicerHDBrainExtraction?tab=readme-ov-file#hdbrainextraction">HDBrainExtraction extension</a> in 3D Slicer, or the <a href="https://github.com/BBillot/SynthSeg">SynthSeg</a> segmentation model.</p>

---
