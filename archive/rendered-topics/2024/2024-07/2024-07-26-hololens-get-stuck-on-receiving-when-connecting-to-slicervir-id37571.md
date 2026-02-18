# HoloLens get stuck on "Receiving..." when connecting to SlicerVirtualReality

**Topic ID**: 37571
**Date**: 2024-07-26
**URL**: https://discourse.slicer.org/t/hololens-get-stuck-on-receiving-when-connecting-to-slicervirtualreality/37571

---

## Post #1 by @Beatriz_2 (2024-07-26 10:50 UTC)

<p>Operating system: Windows 11 on pc</p>
<p>Hi.</p>
<p>I tried to connect HoloLens 2 to SlicerVirtualReality. For that purpose I follow the steps in the github. However when I try the first step - set up Windows Mixed Reality - I have encountered some problems. As shown in the image after the PC check, I receive a message saying connect to headeset (as shown in the picture), which I don’t understand since I am connected via cable to my computer.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb799c704cf0ad19837f7d7bb9d6cc82de272abf.png" data-download-href="/uploads/short-url/qKtPVsKBUs6jX9k8wDrpvALvDqv.png?dl=1" title="Captura de ecrã 2024-07-23 163553" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb799c704cf0ad19837f7d7bb9d6cc82de272abf_2_690x313.png" alt="Captura de ecrã 2024-07-23 163553" data-base62-sha1="qKtPVsKBUs6jX9k8wDrpvALvDqv" width="690" height="313" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb799c704cf0ad19837f7d7bb9d6cc82de272abf_2_690x313.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb799c704cf0ad19837f7d7bb9d6cc82de272abf_2_1035x469.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb799c704cf0ad19837f7d7bb9d6cc82de272abf.png 2x" data-dominant-color="050405"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de ecrã 2024-07-23 163553</span><span class="informations">1379×626 107 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I tried to ignore this step since I don’t understood the reason, and I followed the other steps. When writing the IP address given by Holographic Remoting Player. The headsets get stuck in “Receiving…”. However the 3D model, uploaded to the 3D Slicer in my computer, is moving when I move my hands. This makes me think that I am somehow connected but I simply can’t visualize the 3D model. In the next picture, I show the transform that have been applied to the 3D model, automatically.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43ddd2cb188f08ac7bbb8b059267b041a5a4ad21.png" alt="Captura de ecrã 2024-07-26 114645" data-base62-sha1="9GnfbJlHUWNdPx6J7Lh1OgB9I9X" width="528" height="117"></p>
<p>I have tried other versions of the 3D Slicer; however, the same problem continue.<br>
Does anyone can help me solve this problem?</p>

---

## Post #2 by @cpinter (2024-08-02 12:27 UTC)

<p>Unfortunately I can’t help, but maybe someone who has experience with HoloLens 2 can.<br>
Maybe you <a class="mention" href="/u/aliciapose">@AliciaPose</a>, or if not please suggest someone. Thanks!</p>

---

## Post #3 by @AliciaPose (2025-06-23 10:49 UTC)

<p>Dear Beatriz_2,</p>
<p>I’m afraid I don’t have direct experience connecting HoloLens 2 to the SlicerVirtualReality module in 3D Slicer. According to the documentation, it should be compatible, but I’ve personally never managed to get it working—I encountered the same error.</p>
<p>Were you able to find a solution?<br>
If not, I can recommend an alternative approach published in <a href="https://github.com/BSEL-UC3M/HoloLens2and3DSlicer-PedicleScrewPlacementPlanning" rel="noopener nofollow ugc">this GitHub repository</a>, especially if your goal is to display 3D models from 3D Slicer in HoloLens 2 and manipulate them directly from the headset. I hope it helps!</p>
<p>Best regards,<br>
Alicia</p>

---
