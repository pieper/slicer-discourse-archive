# Cannot “Center view” on 3D volume

**Topic ID**: 3132
**Date**: 2018-06-10
**URL**: https://discourse.slicer.org/t/cannot-center-view-on-3d-volume/3132

---

## Post #1 by @arcampos (2018-06-10 08:43 UTC)

<p>Hi</p>
<p>I’m doing some segmentation on brain slices. I don’t know what I did, but suddenly my purple box is much bigger than my segmentation volumes. I’ve already tried “Center view” and to hide everything but my segmented volumes and still I can’t reduce de size of this box.</p>
<p>Can you help me on this?</p>
<p>I’m working on a cropped isotropic volume with a voxel of 0,045x0,045x0,045 mm.</p>
<p>Thank you for your help</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/7233026168d5efbf84c41b961b4594f4cd0ab9a8.jpeg" data-download-href="/uploads/short-url/gifIy6zz938W274Cm3RXPY5BPsI.jpg?dl=1" title="Screenshot_41" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7233026168d5efbf84c41b961b4594f4cd0ab9a8_2_683x500.jpg" alt="Screenshot_41" data-base62-sha1="gifIy6zz938W274Cm3RXPY5BPsI" width="683" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7233026168d5efbf84c41b961b4594f4cd0ab9a8_2_683x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7233026168d5efbf84c41b961b4594f4cd0ab9a8_2_1024x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7233026168d5efbf84c41b961b4594f4cd0ab9a8_2_1366x1000.jpg 2x" data-dominant-color="83838F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_41</span><span class="informations">1741×1274 488 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2018-06-10 14:15 UTC)

<p>Probably there is some node (it may be even hidden), which makes the extents of the box that large. Go to Data module and try to delete all nodes that you don’t need (if you deleted all irrelevant nodes visible in the Subject hierarchy tab, you can go to All nodes tab and see if there are something more to delete there). If you are not sure what to delete then save the scene and then just load what you need (probably your a volume and a segmentation).</p>

---

## Post #3 by @arcampos (2018-06-10 23:18 UTC)

<p>Thank you very much Andras</p>
<p>I solved this with your advice. I’ve deleted “VolumeDisplay” node and everything returned to normal again.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34d28ccee3fa8d1158c36d5763a431484262ffeb.png" alt="Screenshot_3D" data-base62-sha1="7xhVEfCUdHDioG7hcFjisdvuf9x" width="639" height="335"></p>

---
