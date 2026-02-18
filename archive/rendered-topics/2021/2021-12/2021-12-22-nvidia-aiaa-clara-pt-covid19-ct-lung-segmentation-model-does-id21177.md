# Nvidia AIAA clara_pt_covid19_ct_lung_segmentation model doesn't show up

**Topic ID**: 21177
**Date**: 2021-12-22
**URL**: https://discourse.slicer.org/t/nvidia-aiaa-clara-pt-covid19-ct-lung-segmentation-model-doesnt-show-up/21177

---

## Post #1 by @utkgl (2021-12-22 10:00 UTC)

<p>Hi everyone,<br>
Lately I was using Nvidia AIAA module ( clara_pt_covid19_ct_lung_segmentation) on 3D Slicer  to automatically segmentate and export lungs. On my main computer (with gpu rtx2060) the model shows up<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da990fcb81ea4d2b5c4a037d3fbc28ae1f4f6977.png" alt="clara" data-base62-sha1="vbO1lydfxqxbSSNSjRyJL9hab5R" width="623" height="244"><br>
but on my other computer (with gpu:gtx860), some of the models doesn’t show up.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2cc2fdf52f212f85e45f91860ab40062af9fa84.jpeg" alt="clara_nomodel" data-base62-sha1="pvIspZ5kiRMOLi5UdabKnkSDLGQ" width="612" height="411"><br>
I tried to uninstall and reinstall the 3D Slicer but it did not work. I would appreciate any help. Thanks!</p>

---

## Post #2 by @lassoan (2021-12-22 13:55 UTC)

<p>Until about half year ago, the default server was an older Clara server with a different set of models. You can switch to use the current server by upgrading to the latest Slicer Stable Release or latest Slicer Preview Release and update to the latest version of NvidiaAIAssistedAnnotation extension.</p>

---
