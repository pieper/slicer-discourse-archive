---
topic_id: 47364
title: "New extension: MuscleMap --  Automated Whole-Body Muscle Segmentation"
date: 2026-06-16
url: https://discourse.slicer.org/t/47364
last_bumped: 2026-06-16T17:51:22.174Z
---

# New extension: MuscleMap --  Automated Whole-Body Muscle Segmentation

**Topic ID**: 47364
**Date**: 2026-06-16
**URL**: https://discourse.slicer.org/t/new-extension-musclemap-automated-whole-body-muscle-segmentation/47364

---

## Post #1 by @Eddo_Wesselink (2026-06-16 17:51 UTC)

<p><strong>New extension: MuscleMap — open-source, community-supported automated whole-body muscle segmentation</strong></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9a8cfa5c43f9d6a06e8c67ee604d6cac137d389.jpeg" data-download-href="/uploads/short-url/v3vhObTG5V8YbeeH7d7FtKtOYGJ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9a8cfa5c43f9d6a06e8c67ee604d6cac137d389_2_690x406.jpeg" alt="image" data-base62-sha1="v3vhObTG5V8YbeeH7d7FtKtOYGJ" width="690" height="406" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9a8cfa5c43f9d6a06e8c67ee604d6cac137d389_2_690x406.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9a8cfa5c43f9d6a06e8c67ee604d6cac137d389_2_1035x609.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9a8cfa5c43f9d6a06e8c67ee604d6cac137d389.jpeg 2x" data-dominant-color="1D1D19"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1190×701 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>MuscleMap is a 3D Slicer extension for fully automatic segmentation of skeletal muscle in MRI and CT. It is developed as an open-source framework by the MuscleMap consortium (led by dr. Kenneth Arnold Weber, Prof dr. James Elliott, dr. Marnee McKay and dr. Eddo Wesselink) — a large, community-supported collaboration of clinicians and researchers with the goal of making reproducible, standardized whole-body muscle measurements freely accessible to researchers and clinicians. Official documentation available on the <a href="https://musclemap.github.io/MuscleMap/" rel="noopener nofollow ugc">MuscleMap website</a>. The model weights are available on <a href="https://zenodo.org/search?q=musclemap" rel="noopener nofollow ugc">Zenodo</a>. Open-source sample data sets are available for easy testing, for example <a href="https://osf.io/svwa7/?view_only=c2c980c17b3a40fca35d088a3cdd83e2" rel="noopener nofollow ugc">MyoSegmentum Thigh</a> and <a href="https://osf.io/3j54b/?view-only=f5089274d4a449cda2fef1d2df0ecc56" rel="noopener nofollow ugc">MyoSegmentum Spine</a>.</p>
<p>To get started:</p>
<ul>
<li>Start 3D Slicer and go to the MuscleMap module.</li>
<li>The first time you use the module, click <strong>“Install MuscleMap dependencies”</strong> to download and install PyTorch and the other dependencies (this can take several minutes). The Slicer PyTorch module is installed alongside MuscleMap by default.</li>
<li>Load an input image into the Slicer scene, then click <strong>“Run MuscleMap Segmentation”</strong>.</li>
</ul>
<p>Video demo/tutorial showing the module in action: <a href="https://www.youtube.com/watch?v=aAXxopcMeKI" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=aAXxopcMeKI</a></p>
<p>For best performance, GPU acceleration is recommended: with a CUDA-capable NVIDIA GPU (<a href="https://developer.nvidia.com/cuda-toolkit" rel="noopener nofollow ugc">CUDA Toolkit</a>) or a compatible AMD GPU (<a href="https://www.amd.com/en/products/software/rocm.html" rel="noopener nofollow ugc">ROCm</a>) plus the matching GPU build of <a href="https://pytorch.org/get-started/previous-versions/" rel="noopener nofollow ugc">PyTorch v2.4.0</a>, whole-body segmentation runs in a few seconds up to about a minute. A GPU is not required — without one, segmentation typically takes between 1 and 20 minutes, depending on image resolution and size.</p>
<p>The extension runs locally and does not send any data to the cloud or any other computer (after setup is completed), which makes it suitable for use with sensitive medical data.</p>
<p>MuscleMap is open-source and freely accessible under the MIT License. The developers do not claim that the tools are appropriate for any specific clinical purpose, and the user is responsible for obtaining any necessary ethics or regulatory approvals.</p>
<p>Questions and issues can be posted to the <a href="https://github.com/MuscleMap/MuscleMap/issues" rel="noopener nofollow ugc">MuscleMap issue page</a>.</p>

---
