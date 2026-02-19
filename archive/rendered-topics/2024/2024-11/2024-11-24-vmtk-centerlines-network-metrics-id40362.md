---
topic_id: 40362
title: "Vmtk Centerlines Network Metrics"
date: 2024-11-24
url: https://discourse.slicer.org/t/40362
---

# Vmtk centerlines/network metrics

**Topic ID**: 40362
**Date**: 2024-11-24
**URL**: https://discourse.slicer.org/t/vmtk-centerlines-network-metrics/40362

---

## Post #1 by @LB95 (2024-11-24 23:59 UTC)

<p>Hi,</p>
<p>I’ve been doing a lot of reading on these forums and managed to piece together a lot, however I’m still having some difficulty solving my problem. My aim is to extract the centerline of a vessel tree in order to compute various metrics for each branch/section of the tree ( e,g, min/max/avg radius/curvature/torsion/tortuosity, volume/surface area of branch etc).</p>
<p>In most cases, the auto end points are working well (and made better from this <a href="https://discourse.slicer.org/t/how-to-obtain-the-complete-center-lines-using-vmtk/14068/11" class="inline-onebox">How to obtain the complete center lines using VMTK? - #11 by perecanals</a> ). In most cases however, the centerline computation is really poor, even with doing oversampling from here (<a href="https://discourse.slicer.org/t/how-to-obtain-the-complete-center-lines-using-vmtk/14068/4" class="inline-onebox">How to obtain the complete center lines using VMTK? - #4 by lassoan</a>). FWIW I know from postprocessing that my segmentation method is completely connected. see img for centerlines (in light green):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b8ac9fec1885348e415daf4880cd5ed020589b9.jpeg" data-download-href="/uploads/short-url/aMhac6bDaoxlymeksBFVU5e8hVD.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b8ac9fec1885348e415daf4880cd5ed020589b9_2_690x459.jpeg" alt="image" data-base62-sha1="aMhac6bDaoxlymeksBFVU5e8hVD" width="690" height="459" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b8ac9fec1885348e415daf4880cd5ed020589b9_2_690x459.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b8ac9fec1885348e415daf4880cd5ed020589b9_2_1035x688.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b8ac9fec1885348e415daf4880cd5ed020589b9.jpeg 2x" data-dominant-color="8B8FAD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1334×889 141 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Regardless, in most cases the network calculation is good (see below for another example), so I am not too bothered about centerlines provided the network can be used to calculate the metrics I need. My question is is this possible? Would I be missing out on anything by not using centerlines?<br>
I’m sorry if I’m missing something, maybe there is something within the vmtk package that already does this that i’m missing?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9240ab47525ed700ff3778cc81c8b0c1f3b15a0.jpeg" data-download-href="/uploads/short-url/uYUPtL2hvri7s4dNYvT6o5LYnwk.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9240ab47525ed700ff3778cc81c8b0c1f3b15a0_2_690x498.jpeg" alt="image" data-base62-sha1="uYUPtL2hvri7s4dNYvT6o5LYnwk" width="690" height="498" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9240ab47525ed700ff3778cc81c8b0c1f3b15a0_2_690x498.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9240ab47525ed700ff3778cc81c8b0c1f3b15a0_2_1035x747.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9240ab47525ed700ff3778cc81c8b0c1f3b15a0.jpeg 2x" data-dominant-color="8F96BF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1082×781 272 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
