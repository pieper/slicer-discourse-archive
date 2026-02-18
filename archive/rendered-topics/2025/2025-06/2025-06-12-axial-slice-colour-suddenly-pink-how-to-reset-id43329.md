# Axial slice colour suddenly pink - how to reset?

**Topic ID**: 43329
**Date**: 2025-06-12
**URL**: https://discourse.slicer.org/t/axial-slice-colour-suddenly-pink-how-to-reset/43329

---

## Post #1 by @tcrnscw (2025-06-12 14:46 UTC)

<p>Hello,</p>
<p>I’m having an issue with the axial slice view in 5.8.1. It suddenly is loading only this slice plane in bright pink, and I’m not sure what I’ve done or how to fix this. The sagittal and coronal views are still in black and white. I’ve tried adjusting things in the color module but it only seems to apply colour changes to the sagittal and coronal views. I’ve also tried restarting slicer, restarting my computer, and loading different dicom stacks and there’s been no change.</p>
<p>Any advice would be greatly appreciated!!</p>

---

## Post #2 by @lassoan (2025-06-12 19:01 UTC)

<p>The slice view appears as a solid colored rectangle in 3D view if no image is selected for that slice view. You can select a background volume for the slice using <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#view-data">slice view controls</a>.</p>

---

## Post #3 by @tcrnscw (2025-06-12 19:16 UTC)

<p>Hello! I think there might be a miscommunication. I can see the anatomy of the person in the axial and other views. It is not a solid colour. It is just that instead of the bone highlighting as white, it is on a black to pink scale only for the axial view. As in, the air to soft tissue to bone is black to pink.</p>

---

## Post #4 by @lassoan (2025-06-12 19:21 UTC)

<p>It is hard to tell if this is normal (due to using a lookup table with these colors) or something is wrong. Could you provide a screenshot?</p>
<p>You can choose lookup table in “Volumes” module / Display / Lookup Table.</p>

---

## Post #5 by @jamesobutler (2025-06-12 19:21 UTC)

<p>It is likely that you are showing a different volume in the Axial slice which has something like the “Magenta” lookup table set for it. See the state below where there are 2 volumes loaded in the scene and in the Volume’s module I have set “MRHead_1” to use the “Magenta” lookup table.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9a782de09425caa11e82d82e9a2e196e07459ff.jpeg" data-download-href="/uploads/short-url/sLURu2a0JZjZLgpYpurak5v6lPN.jpeg?dl=1" title="{BDA34375-5246-4AC9-8552-C40D8E881F98}" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9a782de09425caa11e82d82e9a2e196e07459ff_2_690x370.jpeg" alt="{BDA34375-5246-4AC9-8552-C40D8E881F98}" data-base62-sha1="sLURu2a0JZjZLgpYpurak5v6lPN" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9a782de09425caa11e82d82e9a2e196e07459ff_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9a782de09425caa11e82d82e9a2e196e07459ff_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9a782de09425caa11e82d82e9a2e196e07459ff_2_1380x740.jpeg 2x" data-dominant-color="837D8A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">{BDA34375-5246-4AC9-8552-C40D8E881F98}</span><span class="informations">1916×1028 297 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
