---
topic_id: 36206
title: "2D Measure On Overlapped 3D Dental Stl"
date: 2024-05-16
url: https://discourse.slicer.org/t/36206
---

# 2D measure on overlapped 3D dental STL 

**Topic ID**: 36206
**Date**: 2024-05-16
**URL**: https://discourse.slicer.org/t/2d-measure-on-overlapped-3d-dental-stl/36206

---

## Post #1 by @MarinBP13 (2024-05-16 12:33 UTC)

<p>Hello everyone,<br>
I am having an issue with taking measurements on overlapping 3D STL files. These are dental models showing before and after scenarios on which I would like to measure the movements occurring in the vertical and horizontal planes. I would like to perform 2D measurements on previously overlapped 3D models. However, whenever I try to take a measurement, I am unable to draw a 2D line; it automatically appears in 3D, thus affecting the accuracy of the measurement.</p>
<p>Is there a keyboard shortcut that allows a 2D measure ?</p>
<p>I am attaching an example. I am trying to compare the vertical movement of this tooth. However, when I place it in the front view, the line is not vertical, so the measurement is distorted.</p>
<p>Thanks a lot for your answer.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/612d6baa59c65bf0f809c57863cb6bf064983562.png" data-download-href="/uploads/short-url/dRFCV4QYJ4l4UJBuglA9Ir70NgK.png?dl=1" title="Capture d'écran_20240516_101854" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/612d6baa59c65bf0f809c57863cb6bf064983562_2_690x399.png" alt="Capture d'écran_20240516_101854" data-base62-sha1="dRFCV4QYJ4l4UJBuglA9Ir70NgK" width="690" height="399" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/612d6baa59c65bf0f809c57863cb6bf064983562_2_690x399.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/612d6baa59c65bf0f809c57863cb6bf064983562_2_1035x598.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/612d6baa59c65bf0f809c57863cb6bf064983562.png 2x" data-dominant-color="A5A695"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d'écran_20240516_101854</span><span class="informations">1096×634 152 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b3cdb6176d5b689b4f3bbd3b66f9bcb4b013470.png" data-download-href="/uploads/short-url/hAd75kYUAjVGvDGm3OSr32cIPGo.png?dl=1" title="Capture d'écran_20240516_101921" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b3cdb6176d5b689b4f3bbd3b66f9bcb4b013470_2_690x392.png" alt="Capture d'écran_20240516_101921" data-base62-sha1="hAd75kYUAjVGvDGm3OSr32cIPGo" width="690" height="392" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b3cdb6176d5b689b4f3bbd3b66f9bcb4b013470_2_690x392.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b3cdb6176d5b689b4f3bbd3b66f9bcb4b013470_2_1035x588.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b3cdb6176d5b689b4f3bbd3b66f9bcb4b013470.png 2x" data-dominant-color="A3A379"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d'écran_20240516_101921</span><span class="informations">1061×603 212 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2024-05-16 15:02 UTC)

<p>The point picking in the 3D view (roughly speaking) finds the surface point in 3D closest to the camera that intersects the line defined by your 2D click. Thus, you won’t be able to enforce a “vertical” line. Does anything prevent you from defining your points in a 2D view? I mean you could show the coronal view in 3D, and you could make the measurements in the 2D view while verifying it in the 3D one.</p>

---

## Post #3 by @MarinBP13 (2024-05-16 18:13 UTC)

<p>Thanks a lot for your answer. But how can you show the coronal view ?</p>

---

## Post #4 by @MarinBP13 (2024-05-16 18:23 UTC)

<p>It is not a DICOM but a STL file…</p>

---

## Post #5 by @muratmaga (2024-05-16 21:16 UTC)

<p>It wouldn’t be as nice, but you can enable Slice views in the Models module and then use crosshairs to find the spot in slice views:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c3d4d16407350780e28222314e9857eae1f941e.jpeg" data-download-href="/uploads/short-url/aSrCJJg9b69ba9dReEG3NmX9BxA.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c3d4d16407350780e28222314e9857eae1f941e_2_690x367.jpeg" alt="image" data-base62-sha1="aSrCJJg9b69ba9dReEG3NmX9BxA" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c3d4d16407350780e28222314e9857eae1f941e_2_690x367.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c3d4d16407350780e28222314e9857eae1f941e_2_1035x550.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c3d4d16407350780e28222314e9857eae1f941e_2_1380x734.jpeg 2x" data-dominant-color="787989"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1023 93.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @MarinBP13 (2024-05-17 14:40 UTC)

<p>Unfortunately, it is not displaying for me… How can I make it show?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2aa9fb8da14e59c460a76876b08e389629ef4d54.png" data-download-href="/uploads/short-url/65qeS2ePpQsA4vyze170e6Y6enW.png?dl=1" title="Capture d'écran_20240517_163759" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2aa9fb8da14e59c460a76876b08e389629ef4d54_2_690x441.png" alt="Capture d'écran_20240517_163759" data-base62-sha1="65qeS2ePpQsA4vyze170e6Y6enW" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2aa9fb8da14e59c460a76876b08e389629ef4d54_2_690x441.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2aa9fb8da14e59c460a76876b08e389629ef4d54_2_1035x661.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2aa9fb8da14e59c460a76876b08e389629ef4d54.png 2x" data-dominant-color="A1A0A8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d'écran_20240517_163759</span><span class="informations">1274×816 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @muratmaga (2024-05-17 16:03 UTC)

<p>please look at my screenshot and make sure your display options are the same.</p>

---

## Post #8 by @cpinter (2024-05-20 09:08 UTC)

<p>Well, if you don’t have a volume then the slice views are not that reliable (there is no volume extent or slice thickness), and you need to use the crosshair or similar as <a class="mention" href="/u/muratmaga">@muratmaga</a> suggests. You can also load a volume from the Sample Data module and match the extent, but then the volume will have nothing to do with your model. You can also create a segmentation from the model (right-click model in Data module) and then export it to labelmap (right click segmentation), and show that in the slice views. Slicer is not really designed to work with data without at least an image…</p>

---
