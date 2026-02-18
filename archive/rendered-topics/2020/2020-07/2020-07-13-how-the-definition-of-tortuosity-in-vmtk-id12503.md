# How the definition of tortuosity in VMTK?

**Topic ID**: 12503
**Date**: 2020-07-13
**URL**: https://discourse.slicer.org/t/how-the-definition-of-tortuosity-in-vmtk/12503

---

## Post #1 by @wwx992881 (2020-07-13 12:01 UTC)

<p>HI,All<br>
I’ve  extracted the center line,and I don’t know the definition of tortuosity in 3D table.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e89040b9c7959efb59c1c0540f6ce4cf463c530b.png" data-download-href="/uploads/short-url/xblPFEGbqqIZlm0NWeiNn3F1mOL.png?dl=1" title="微信图片_20200713195110" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e89040b9c7959efb59c1c0540f6ce4cf463c530b_2_556x499.png" alt="微信图片_20200713195110" data-base62-sha1="xblPFEGbqqIZlm0NWeiNn3F1mOL" width="556" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e89040b9c7959efb59c1c0540f6ce4cf463c530b_2_556x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e89040b9c7959efb59c1c0540f6ce4cf463c530b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e89040b9c7959efb59c1c0540f6ce4cf463c530b.png 2x" data-dominant-color="CFD0E4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">微信图片_20200713195110</span><span class="informations">736×661 36 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I see a definition of tortuosity in the literature:Tortuosity was defined as L/D–1, where L is the length of the centre line from one point to another point, and D is the straight-line distance between these two points.I want to know the definition of tortuosity in the 3d slicer is the same as this one.<br>
Thanks~!</p>

---

## Post #2 by @lassoan (2020-07-13 13:49 UTC)

<p>Yes, tortuosity is computed as the ratio between the centerline length and the distance between the line endpoints - 1. Since VMTK is open-source, you can always verify what the exact computation is. Implementation of this metric is available <a href="https://github.com/vmtk/vmtk/blob/94d2789a8cd22197352e25e1d65e4644d751e870/vtkVmtk/ComputationalGeometry/vtkvmtkCenterlineGeometry.cxx#L284">here</a>.</p>

---

## Post #3 by @wwx992881 (2020-07-13 13:54 UTC)

<p>Thanks!That will help me a lot.</p>

---
