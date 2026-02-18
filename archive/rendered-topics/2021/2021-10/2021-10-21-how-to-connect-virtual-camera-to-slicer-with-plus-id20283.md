# How to connect virtual camera to Slicer with Plus ？

**Topic ID**: 20283
**Date**: 2021-10-21
**URL**: https://discourse.slicer.org/t/how-to-connect-virtual-camera-to-slicer-with-plus/20283

---

## Post #1 by @slicer365 (2021-10-21 11:04 UTC)

<p>I can load the camera into the Slicer through Plus,</p>
<p>but if I want to capture the surgical field of view under the microscope to the computer through the capture card,</p>
<p>then start the virtual camera to Plus and then transfer it to the Slicer，how to make it possible?</p>
<p>At present ,I cann’t capture the virtual camera by Plus，even I start the virtual camera, the default camera is still the actual camera.</p>

---

## Post #2 by @lassoan (2021-10-22 18:08 UTC)

<p>If you use Microsoft Media Foundation video source then you can select the device by adjusting the <code>CaptureDeviceId</code> and <code>CaptureStreamIndex</code> attributes. See details <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceMicrosoftMediaFoundation.html">here</a>.</p>

---
