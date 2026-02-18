# SlicerRT isocenter configuration

**Topic ID**: 45122
**Date**: 2025-11-17
**URL**: https://discourse.slicer.org/t/slicerrt-isocenter-configuration/45122

---

## Post #1 by @Mafer_Calix (2025-11-17 15:35 UTC)

<p>Hello. I need to know whether the isocenter for the slicerRT is fixed at 100 cm. Sure, in the software I can edit the isocenter position within the body and the SDD. But I need to know if the beam’s field defined in beam geometry forms at the SDD or at the isocenter position (eg. if I define a 100x100 mm beam geometry, SDD = 1000 mm and isocenter at the center of target volume, will the 100x100 mm area form at the surface of the volume target or the isocenter?)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/350a43b7ca095ee19f360e1207d9cdd2dec8444f.png" data-download-href="/uploads/short-url/7zdirS1Y8wCtzLijHm6gHOKoJgr.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/350a43b7ca095ee19f360e1207d9cdd2dec8444f.png" alt="image" data-base62-sha1="7zdirS1Y8wCtzLijHm6gHOKoJgr" width="642" height="463"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">642×463 20.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3905572b11fd4788a4d8bbdc99384c2946c399f.png" data-download-href="/uploads/short-url/nkX3NXoVMRaFZxUtTu7iKJH8vo3.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3905572b11fd4788a4d8bbdc99384c2946c399f.png" alt="image" data-base62-sha1="nkX3NXoVMRaFZxUtTu7iKJH8vo3" width="522" height="500" data-dominant-color="3D3E3E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">640×613 25.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2025-12-09 12:19 UTC)

<p>Sorry for the delay; I read this at the time but didn’t understand the issue clearly then moved on. Now, looking at it again…</p>
<p>First of all, what is SDD? Source-detector distance? In SlicerRT we have SAD, source-axis distance as a parameter of the beams.</p>
<p>When changing SAD, basically the visualization of the beam geometry is updated, nothing else, at least in SlicerRT core. Then the dose engines will use this parameter as their author decided to implement it. Which dose engine are you interested in?</p>
<p>(FYI pyRadPlan has been integrated into SlicerRT recently)</p>

---
