# PlusToolkit compatible with GE Ultrasound

**Topic ID**: 23085
**Date**: 2022-04-22
**URL**: https://discourse.slicer.org/t/plustoolkit-compatible-with-ge-ultrasound/23085

---

## Post #1 by @J.vd.Zee (2022-04-22 12:51 UTC)

<p>Dear all,</p>
<p>Anyone with experience in connecting a General Electric Ultrasound device to the Plus Server?<br>
The devices of GE are not in the list of compatible hardware.</p>
<p>Thanks in advance!</p>

---

## Post #2 by @lassoan (2022-04-23 05:20 UTC)

<p>Plus toolkit can only acquire images from GE ultrasound systems via a framegrabber. You can use a high-quality framegrabber, such as Epiphan devices, or any Microsoft Media Foundation or OpenCV compatible device.</p>

---

## Post #3 by @J.vd.Zee (2022-04-25 08:52 UTC)

<p>Thanks again for your reply!<br>
Is it also possible without any external hardware device?</p>

---

## Post #4 by @lassoan (2022-04-25 12:25 UTC)

<p>It is possible to receive images in real-time from some GE scanners using GE’s AppAPI interface. You can get access to this API by <a href="https://www.gehealthcare.com/products/edison/edison-developer-program">signing up to GE’s Edison Developer Program</a>. You’ll be added to the <code>GEUltrasound/AppAPI</code> repository on GitHub, which contains SDK and examples.</p>
<p>I would recommend to modify one of the examples to create a small client that receives ultrasound images via AppAPI and makes them available via <a href="http://openigtlink.org/">OpenIGTLink</a>. Slicer can receive live images via OpenIGTLink, display, record, replay, reconstruct them into 3D volume (if you connect a tracker to it), etc.</p>

---
