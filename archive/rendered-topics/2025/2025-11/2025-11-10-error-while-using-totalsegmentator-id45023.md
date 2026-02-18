# Error while using TotalSegmentator。

**Topic ID**: 45023
**Date**: 2025-11-10
**URL**: https://discourse.slicer.org/t/error-while-using-totalsegmentator/45023

---

## Post #1 by @hwy13140 (2025-11-10 14:51 UTC)

<ul>
<li>System: Window 11</li>
<li>Slicer Version: 5.8.1<br>
When I use the total segmentator extension, the Python console keeps showing the following warning during torch installation:<br>
<code>WARNING: Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /whl/cu125/torch/ Could not fetch URL https://download.pytorch.org/whl/cu125/torch/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='download.pytorch.org', port=443): Max retries exceeded with url: /whl/cu125/torch/ (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))) - skipping</code>.<br>
This warning appears regardless of whether I disable the VPN.</li>
</ul>

---
