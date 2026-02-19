---
topic_id: 8777
title: "Plus Server Error With 3D Slicer"
date: 2019-10-14
url: https://discourse.slicer.org/t/8777
---

# Plus Server Error with 3D Slicer

**Topic ID**: 8777
**Date**: 2019-10-14
**URL**: https://discourse.slicer.org/t/plus-server-error-with-3d-slicer/8777

---

## Post #1 by @hripat (2019-10-14 18:56 UTC)

<p>Hello,<br>
I am trying to use Slicer with the Plus Server connected so that I can use the transforms function for the Ultrasound images. However, I am getting the error show in the image. I have installed all four SlicerIGT related extensions in Slicer but I’m not sure what’s causing this error.</p>
<p>The error says:<br>
|ERROR|022.003000| Cannot connect to the server (127.0.0.1:18946).| in E:\D\PSNP64b\PlusLib\src\PlusDataCollection\OpenIGTLink\vtkPlusOpenIGTLinkDevice.cxx(152)<br>
|ERROR|022.311000| Socket error in device TrackerDevice: failed to receive OpenIGTLink transforms. Attempt to reconnect.| in E:\D\PSNP64b\PlusLib\src\PlusDataCollection\OpenIGTLink\vtkPlusOpenIGTLinkDevice.cxx(241)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d8aa86ef30cc2f89c720c0df36bec13ce572857.png" data-download-href="/uploads/short-url/hUAKWd53RtmUuep6YJ1pW5Gb0zR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d8aa86ef30cc2f89c720c0df36bec13ce572857.png" alt="image" data-base62-sha1="hUAKWd53RtmUuep6YJ1pW5Gb0zR" width="690" height="343" data-dominant-color="1D1818"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">959×478 23.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2019-10-17 05:00 UTC)

<p>Your Plus configuration file seems to be incorrect. You can get help on writing configuration files for Plus by submitting your question as an issue at PlusLib repository’s tracker (<a href="https://github.com/PlusToolkit/PlusLib/issues/new" rel="nofollow noopener">https://github.com/PlusToolkit/PlusLib/issues/new</a>).</p>

---

## Post #3 by @hripat (2019-10-18 15:51 UTC)

<p>Ok, thank you for your help!</p>

---
