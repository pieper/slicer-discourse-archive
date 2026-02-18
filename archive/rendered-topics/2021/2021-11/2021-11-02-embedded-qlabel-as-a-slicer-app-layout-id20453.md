# Embedded Qlabel as a Slicer app layout

**Topic ID**: 20453
**Date**: 2021-11-02
**URL**: https://discourse.slicer.org/t/embedded-qlabel-as-a-slicer-app-layout/20453

---

## Post #1 by @Srijeet_Chatterjee (2021-11-02 11:12 UTC)

<p>Hello everyone,</p>
<p>Hope it’s going good!<br>
Currently, I am using slicer to display some images(or video) on a Qlabel. It seems to work fine, but I want to embedd the Qlabel window on the slicer layout, instead of any one of the Planar or 3D views. Can anyone share some ideas/ let me know a nice way to get this done?</p>
<p>Thanks in advance,<br>
Best regards,<br>
Srijeet</p>

---

## Post #2 by @lassoan (2021-11-02 19:39 UTC)

<p>You can use the same method how the DICOM module shows the DICOM browser widget in the layout.</p>
<p>However, to take full advantage of all Slicer features, such as real-time processing, analysis, annotation, measurement, recording and replay, etc. of 2D/3D image streams, I would strongly recommend to use a 2D or 3D viewer instead of the extremely limited QLabel.</p>
<p>You don’t even need to implement the streaming interface, you can use SlicerOpenIGTLink module to receive and visualize real-time image streams. By using <a href="https://plustoolkit.github.io/">Plus toolkit</a> there is a good chance that you don’t need to do any custom software development if you want to connect to your ultrasound, endoscope, video camera, depth camera, etc… See <a href="https://www.slicerigt.org/">https://www.slicerigt.org/</a> for some examples.</p>

---

## Post #3 by @Srijeet_Chatterjee (2021-11-03 07:03 UTC)

<p>Thank you so much for the explanations and hints, I would look into the DICOM module and the Plus toolkit. I could already get the image streams on the viewers, this one I wanted to try out additionally.</p>

---
