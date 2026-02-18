# How to acquire X-ray images from C-arm?

**Topic ID**: 30393
**Date**: 2023-07-04
**URL**: https://discourse.slicer.org/t/how-to-acquire-x-ray-images-from-c-arm/30393

---

## Post #1 by @palani_narayanan (2023-07-04 09:48 UTC)

<p>Hi…How to get c arm video as multiple x ray images frame by frame… How to extract video from c arm in a computer… please guide…ty</p>

---

## Post #2 by @lassoan (2023-07-04 15:54 UTC)

<p>You can use the <a href="https://plustoolkit.github.io/">PLUS toolkit</a> to acquire live X-ray images from a C-arm using a framegrabber and the send the images to Slicer via OpenIGTLink. You can find many tutorials on the <a href="https://slicerigt.org/">SlicerIGT project website</a> for ultrasound - framegrabbing of X-ray images works the same way.</p>
<p>You can also use the PLUS toolkit to acquire C-arm orientation using a pose tracker or IMU or MARG sensor.</p>

---

## Post #3 by @henrykrumb (2023-07-05 12:51 UTC)

<p>This will very much depend on the C-arm device you’re using and the interfaces it supports.</p>
<p>In our lab, we use a Ziehm vision RFD C-arm which has an analog video out. We use an analog USB video grabber stick to acquire the image that is currently displayed on screen, but with nasty watermark overlays and decreased resolution (it is a PAL signal…). But for prototyping, this is perfectly fine. Then, proceed with SlicerIGT and an IGT server like Plus as <a class="mention" href="/u/lassoan">@lassoan</a> suggested (we use Python OpenCV to grab frames and pyigtl to talk to Slicer via SlicerIGT).</p>
<p>You might be able to get higher res images or even full sequences by accessing a PACS or connecting your C-arm to your own PACS like Orthanc. For our Ziehm Vision, this was not an option as it doesn’t support DICOM query/retrieve.</p>

---
