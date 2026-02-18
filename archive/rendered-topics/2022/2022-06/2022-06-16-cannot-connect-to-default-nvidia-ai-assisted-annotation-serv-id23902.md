# Cannot connect to default NVIDIA AI-assisted annotation server

**Topic ID**: 23902
**Date**: 2022-06-16
**URL**: https://discourse.slicer.org/t/cannot-connect-to-default-nvidia-ai-assisted-annotation-server/23902

---

## Post #1 by @Monkeyking123 (2022-06-16 13:28 UTC)

<p>I was opening 3D slicer but when opening files from “Recent”, Slicer</p>
<ol>
<li>No response</li>
<li>Pops out the following message</li>
<li>Automatically turns off and exit</li>
</ol>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef82b51da29007feafe7cb4ee195e68a97b1320c.png" alt="image" data-base62-sha1="yaO9BxW4akdwZMKN0JAmOcPbWSU" width="420" height="88"></p>
<ul>
<li>If opening other sample files which work and trying to use the Nvidia AIAA tool, this notification pops up about the server:</li>
</ul>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5ebe3c1151b00075df1f23e51cb8ee67c66ed17d.png" alt="image" data-base62-sha1="dw8soLPY6OTggEn3GPPBIFksgz3" width="512" height="127"></p>
<p>How can it be fixed?</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2022-06-16 13:30 UTC)

<p>The segmentation server had to be moved and its address has changed. You can update to the latest Slicer Stable Release (or latest Slicer Preview Release) and clear the server address field to connect to the server at the new address.</p>

---
