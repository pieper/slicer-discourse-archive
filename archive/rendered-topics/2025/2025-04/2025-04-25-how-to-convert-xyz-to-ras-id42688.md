---
topic_id: 42688
title: "How To Convert Xyz To Ras"
date: 2025-04-25
url: https://discourse.slicer.org/t/42688
---

# How to convert xyz to RAS

**Topic ID**: 42688
**Date**: 2025-04-25
**URL**: https://discourse.slicer.org/t/how-to-convert-xyz-to-ras/42688

---

## Post #1 by @zxy630 (2025-04-25 16:06 UTC)

<p>I have an xyz coordinate of 31.4, -39.6, -216.4, but the corresponding RAS coordinates are -34.88, 38.816, -204.997. I find that there are deviations in the coordinates when importing. This is not just a simple relationship of reversing the xy axes. Could anyone please tell me what the cause is and how to solve it?<br>
My dicom’s detail is as follows:<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22bfc5d8a81b023b0c21346b6f43aedb21eba614.png" data-download-href="/uploads/short-url/4Xp6xaIENH1CsMTD2GWiNwLPDk8.png?dl=1" title="detail" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22bfc5d8a81b023b0c21346b6f43aedb21eba614.png" alt="detail" data-base62-sha1="4Xp6xaIENH1CsMTD2GWiNwLPDk8" width="690" height="123" data-dominant-color="F4F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">detail</span><span class="informations">844×151 2.52 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2025-04-25 16:07 UTC)

<p>What coordinate system do you refer to as XYZ? What are the origin, spacing, and axis directions?</p>

---

## Post #3 by @zxy630 (2025-04-26 02:54 UTC)

<p>Actually, i don’t know the origin coordinate system. I only know the coordinate is from FluoroCT, and we want to import the mark to 3Dslicer now. The spacing is [0.43, 0. 43, 0.625]. The origin is [78.132, 153.069, -275.262]. Can you give me some advice?</p>

---

## Post #4 by @lassoan (2025-04-26 12:25 UTC)

<p>Assuming that by “FluoroCT” you mean CBCT reconstruction by a fluoro (C-arm) that is saved in DICOM, the coordinates are in LPS coordinate system. You can convert between LPS and RAS coordinate systems by inverting the sign of the first two coordinates.</p>

---
