# Send Rendering Information via OpenIGTLinkIF

**Topic ID**: 40392
**Date**: 2024-11-26
**URL**: https://discourse.slicer.org/t/send-rendering-information-via-openigtlinkif/40392

---

## Post #1 by @Filippo_Parronchi (2024-11-26 22:37 UTC)

<p>Hello everyone!<br>
After loading a volume into the scene, I send it to a receiving client (Unity script) via the OpenIGTLinkIF protocol, and thanks to an implemented plugin, I can perform volume rendering.<br>
However, through the IGT protocol, I can only send the raw volume information for rendering and cannot send or render the volume with the modifications applied and visible when I use the VolumeRendering module in 3D Slicer (e.g., smoothing).</p>
<p>For example, when I apply TotalSegmentator and extract the liver volume, I cannot send the smoothed volume obtained by selecting the value from the dropdown menu of the “Show3D” button. Instead, I send the raw segmentation, resulting in lower rendering quality.<br>
This is just an example, may it applies to any other similar option.</p>
<p>Is it possible to send these types of modifications through the protocol and receive and reconstruct the volume with the same adjustments visible in 3D Slicer?</p>
<p>Thank you very much for any help.</p>

---

## Post #2 by @Filippo_Parronchi (2024-11-27 14:54 UTC)

<p>Related to this, I would like to know the code that is executed when, from the <strong>Segment Editor</strong>, after applying <strong>TotalSegmentator</strong>, I go to <strong>“Show 3D”</strong> and apply a <strong>“smoothing factor”</strong>.</p>
<p>Additionally, I would like to know how it is possible to improve the sampling of my mask by reducing the steps and making the contour of my mask as continuous as possible, for example with a spline.</p>

---

## Post #3 by @diazandr3s (2024-12-01 13:37 UTC)

<p>Hi <a class="mention" href="/u/filippo_parronchi">@Filippo_Parronchi</a>,</p>
<p>That’s an interesting question. I’m interested in learning more.<br>
Could you share screenshots of your current results and what you plan to send via the IGT protocol?</p>

---
