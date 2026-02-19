---
topic_id: 7766
title: "Ct Is Cropped Atfer Elastix Deformable Registraton"
date: 2019-07-26
url: https://discourse.slicer.org/t/7766
---

# CT is cropped atfer Elastix deformable registraton

**Topic ID**: 7766
**Date**: 2019-07-26
**URL**: https://discourse.slicer.org/t/ct-is-cropped-atfer-elastix-deformable-registraton/7766

---

## Post #1 by @kuba_grepl (2019-07-26 06:56 UTC)

<p>Dear community,<br>
I need your help <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
I used Elastix module to register MR and CT of radiotherapy head and neck patient. MR is fixed volume and CT is moving volume. MR scan does not contain shoulders and upper part of the head , unlike CT scan. Output volume is cropped at the border of MR scan after Elastix deformable registration. But I need missing parts of body in Output volume due to dose calculation. How to solve it?</p>
<p>PS: I attach original CT, MR and Output Volume is screen capture.</p>
<p>Thank you.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2e0eef18a2714cac55b7c49155d65991a8155ba.png" data-download-href="/uploads/short-url/neTgBcqkINWbJvWqZMNZ0y9MNjc.png?dl=1" title="MR" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2e0eef18a2714cac55b7c49155d65991a8155ba_2_690x370.png" alt="MR" data-base62-sha1="neTgBcqkINWbJvWqZMNZ0y9MNjc" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2e0eef18a2714cac55b7c49155d65991a8155ba_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2e0eef18a2714cac55b7c49155d65991a8155ba_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2e0eef18a2714cac55b7c49155d65991a8155ba_2_1380x740.png 2x" data-dominant-color="78787B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">MR</span><span class="informations">1920×1031 328 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2019-07-26 19:03 UTC)

<p>I think your CT has a larger field of view than your MR. If you want to keep the MR as the reference volume, you may pad the volume with 0s to enlarge the field of view. Or use the MR with Crop Volume with "interpolated cropping’ option and set a ROI that will cover the extend of the CT scan and create a new volume to use with elastix.</p>

---
