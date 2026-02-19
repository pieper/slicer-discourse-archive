---
topic_id: 9671
title: "How To Show Vr In View2 3 By Code"
date: 2019-12-31
url: https://discourse.slicer.org/t/9671
---

# How to show VR in View2/3 by code?

**Topic ID**: 9671
**Date**: 2019-12-31
**URL**: https://discourse.slicer.org/t/how-to-show-vr-in-view2-3-by-code/9671

---

## Post #1 by @apparrilla (2019-12-31 12:14 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc8129cd1d351658b8e99fa2f4d1fbc4de5fba35.png" data-download-href="/uploads/short-url/vsFM1q1bRpnlKdPttiJAqZ5vFyt.png?dl=1" title="Anotación 2019-12-31 131150" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc8129cd1d351658b8e99fa2f4d1fbc4de5fba35_2_517x226.png" alt="Anotación 2019-12-31 131150" data-base62-sha1="vsFM1q1bRpnlKdPttiJAqZ5vFyt" width="517" height="226" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc8129cd1d351658b8e99fa2f4d1fbc4de5fba35_2_517x226.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc8129cd1d351658b8e99fa2f4d1fbc4de5fba35_2_775x339.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc8129cd1d351658b8e99fa2f4d1fbc4de5fba35.png 2x" data-dominant-color="5F6266"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Anotación 2019-12-31 131150</span><span class="informations">783×343 16.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>How can I switch on/off volume rendering in secondary views by code?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2019-12-31 13:59 UTC)

<p>You can get the volume rendering display node by calling <a href="http://apidocs.slicer.org/master/classvtkSlicerVolumeRenderingLogic.html#aa6f86f51fec274f8a28ea966a1ee3a10">GetFirstVolumeRenderingDisplayNode</a> then call its <a href="http://apidocs.slicer.org/master/classvtkMRMLDisplayNode.html#a62cff2549fe8c0c4fbff5b363031e242">AddViewNodeID</a> method for each view that you want your volume to be displayed in.</p>

---

## Post #3 by @apparrilla (2019-12-31 15:23 UTC)

<p>Super…<br>
Thanks and happy New year.</p>

---
