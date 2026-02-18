# BoneReconstructionPlanner: not able to make hemimandibulectomy

**Topic ID**: 44838
**Date**: 2025-10-21
**URL**: https://discourse.slicer.org/t/bonereconstructionplanner-not-able-to-make-hemimandibulectomy/44838

---

## Post #1 by @Davi_Matos (2025-10-21 20:04 UTC)

<p>Hello! I am getting used to use the extension to plan for ressections, but I’m finding some problems that I’m not being able to solve on my own. I’m trying to plan the ressection from the left side of a mandible, but the fibula segmentations is not cutting on the right way. Also, the cuts were cutting through the other side of the mandible. Clicking “fix cut goes through the mandible twice” solves it to an extension, but the condile is still getting cut. I’ll send the images so you guys can see whats happening.</p>
<p>I appreciate the help. Don’t know what am I doing wrong. <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa951ebb2864531a3134e84772ee3c07baec8108.png" data-download-href="/uploads/short-url/ol2EO6s2LNrOOF8M7rk2RvGHg0w.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa951ebb2864531a3134e84772ee3c07baec8108.png" alt="image" data-base62-sha1="ol2EO6s2LNrOOF8M7rk2RvGHg0w" width="589" height="364"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">589×364 70.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/0312cc93862ffd7d63eb0126609aee834f6199a5.jpeg" data-download-href="/uploads/short-url/rbHYKIeCDc8pUcU87oV9F6wwK1.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/0312cc93862ffd7d63eb0126609aee834f6199a5_2_690x464.jpeg" alt="image" data-base62-sha1="rbHYKIeCDc8pUcU87oV9F6wwK1" width="690" height="464" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/0312cc93862ffd7d63eb0126609aee834f6199a5_2_690x464.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/0312cc93862ffd7d63eb0126609aee834f6199a5_2_1035x696.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/0312cc93862ffd7d63eb0126609aee834f6199a5.jpeg 2x" data-dominant-color="9693B9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1191×802 160 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d00e9369a62761c1f2dce8a8e80d9c6f9653544d.jpeg" data-download-href="/uploads/short-url/tGyxD5wtWRa9CbjJYe9SciobrFb.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d00e9369a62761c1f2dce8a8e80d9c6f9653544d_2_690x470.jpeg" alt="image" data-base62-sha1="tGyxD5wtWRa9CbjJYe9SciobrFb" width="690" height="470" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d00e9369a62761c1f2dce8a8e80d9c6f9653544d_2_690x470.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d00e9369a62761c1f2dce8a8e80d9c6f9653544d_2_1035x705.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d00e9369a62761c1f2dce8a8e80d9c6f9653544d.jpeg 2x" data-dominant-color="9695BC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1186×808 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @mau_igna_06 (2025-10-21 20:09 UTC)

<p>Hi Davi,</p>
<p>I’m glad to help you. Could you provide a Slicer scene where the problem appears?</p>
<p>Thank you,<br>
Mauro</p>

---

## Post #3 by @Davi_Matos (2025-10-21 20:12 UTC)

<p>Sure! Here’s the link: <a href="https://drive.google.com/drive/folders/1vJh20Rj6Esaje9gRnVp3M8sr7brws9RD?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">forum - Google Drive</a></p>

---

## Post #4 by @mau_igna_06 (2025-10-21 22:40 UTC)

<p>You can delete the folder.</p>
<p>The problem is that the plane near the condyle was pointing in the wrong direction. I just turned it 180° and it worked as expected (see picture below)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f65c53944c646f0f79615b6b2308b32cae9630bc.png" data-download-href="/uploads/short-url/z9pgvFWszZyno2o7HUXr7ZRUGAI.png?dl=1" title="Screenshot from 2025-10-21 19-37-35_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f65c53944c646f0f79615b6b2308b32cae9630bc_2_619x500.png" alt="Screenshot from 2025-10-21 19-37-35_2" data-base62-sha1="z9pgvFWszZyno2o7HUXr7ZRUGAI" width="619" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f65c53944c646f0f79615b6b2308b32cae9630bc_2_619x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f65c53944c646f0f79615b6b2308b32cae9630bc_2_928x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f65c53944c646f0f79615b6b2308b32cae9630bc_2_1238x1000.png 2x" data-dominant-color="707094"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2025-10-21 19-37-35_2</span><span class="informations">1651×1333 241 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @Davi_Matos (2025-10-24 01:13 UTC)

<p>I see that now… The rotation on the plane cut influences a lot, I don’t quite get why, but it does. Thanks a lot, my friend!</p>

---
