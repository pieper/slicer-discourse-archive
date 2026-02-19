---
topic_id: 22201
title: "Increase Slice Thickness In Only One Plane Anisotropically"
date: 2022-02-28
url: https://discourse.slicer.org/t/22201
---

# Increase slice thickness in only one plane (anisotropically)

**Topic ID**: 22201
**Date**: 2022-02-28
**URL**: https://discourse.slicer.org/t/increase-slice-thickness-in-only-one-plane-anisotropically/22201

---

## Post #1 by @Fluvio_Lobo (2022-02-28 00:31 UTC)

<p>Hello,</p>
<p>I am trying to increase the slice thickness of a volume in one view/plane. The current volume features 0.3 mm slices in all three views/planes. I was hoping there was a way of creating a volume with 1 mm slices in the axial and 0.3-0.6 mm slices in coronal and sagittal.</p>
<p>I would normally use <strong>crop volume</strong> to achieve the opposite result, so I was wondering if there was a similar approach.</p>
<p>The motivation here is to test some datasets using MONAI Label. I just don’t have enough GPU to use the original volume <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=12" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @muratmaga (2022-02-28 03:06 UTC)

<p>ResampleScalarVolume will allow you to enter requested image spacing of output image and will resample based on that.<br>
Try that first.</p>

---

## Post #3 by @Fluvio_Lobo (2022-02-28 03:51 UTC)

<p>Thank you <a class="mention" href="/u/muratmaga">@muratmaga</a>! I did not know this module existed.</p>

---
