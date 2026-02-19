---
topic_id: 30406
title: "How To Create Shadows Of The Segments"
date: 2023-07-05
url: https://discourse.slicer.org/t/30406
---

# How to Create shadows of the segments?

**Topic ID**: 30406
**Date**: 2023-07-05
**URL**: https://discourse.slicer.org/t/how-to-create-shadows-of-the-segments/30406

---

## Post #1 by @shahrokh (2023-07-05 12:16 UTC)

<p>Dear Developers and Users</p>
<p>I want to create an image, with a certain matrix and pixel sizes, of the shadows of the segments in RTSTRUCTURE (one of the inputs used in SlicerRT) on a plan at a distance of 160 cm from the target and perpendicular to the central axis of beam.</p>
<p>Please suppose that I want the matrix size of this image to be equal to 1024x1024 and pixel size to be equal to 0.4x0.4 mm.</p>
<p>It is assumed that the source of producing these shadows is the target of the linear accelerator (LINAC).<br>
I have shown this in the following figure.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e44ae11a060bc26eb0b5708b5ae8d09367ea0104.png" data-download-href="/uploads/short-url/wzzi4fU8nMyhLGtO8EAVOzGw8M4.png?dl=1" title="YellowPlan" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e44ae11a060bc26eb0b5708b5ae8d09367ea0104_2_690x424.png" alt="YellowPlan" data-base62-sha1="wzzi4fU8nMyhLGtO8EAVOzGw8M4" width="690" height="424" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e44ae11a060bc26eb0b5708b5ae8d09367ea0104_2_690x424.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e44ae11a060bc26eb0b5708b5ae8d09367ea0104_2_1035x636.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e44ae11a060bc26eb0b5708b5ae8d09367ea0104.png 2x" data-dominant-color="ADB0BF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">YellowPlan</span><span class="informations">1373×845 207 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In this figure, the radiation field (Beam) is seen in green. The plane I talked about is displayed in yellow.</p>
<p>At this figure, the segments that I want shadows to be created on this plan include the following:</p>
<p>RightLungCTNormal,<br>
LeftLungCTNormal,<br>
HEARTCTNormal,<br>
CTVCTNormal and<br>
LADCTNormal</p>
<p>I want the pixel value of each shadow area of the segments to be specific and different from the other.</p>
<p>Please guide me.</p>
<p>Best regards.</p>
<p>Shahrokh</p>

---

## Post #2 by @cpinter (2023-07-07 09:03 UTC)

<p>Hi Shahrokh,</p>
<p>This is an interesting problem. The first thing that occurs me is to check out the implementation of the “Markups perspective projection on the imager plane” part of the DRR Image Computation module, maybe it is easy to extend it to projections of segments.</p>
<p>FYI there is an RT planar image class in SlicerRT, probably it would make sense to use that instead of the model node.</p>

---

## Post #3 by @shahrokh (2023-07-07 09:59 UTC)

<p>Hi Csaba</p>
<p>Thank you very much for your advice.<br>
I will definitely check this issue, tomorrow.</p>
<p>I want to calculate the dose distribution inside the shadows of the segments at the EPID position and then plot the curve of dose versus area.</p>
<p>I converted DRR and EPID images to absorbed dose distribution.</p>
<p>Best regards.<br>
Shahrokh.</p>

---

## Post #4 by @lassoan (2023-07-07 11:30 UTC)

<p>I’m not sure if it helps, but you can add segments to a volume (using Mask volume effect) and then simulate an EPID image using DRR.</p>

---

## Post #5 by @shahrokh (2023-07-07 13:09 UTC)

<p>Hello Andras</p>
<p>This is also an interesting and creative method. Based on this, I can create (or projects) from the segments added to volume.</p>
<p>Best regards.<br>
Shahrokh</p>

---

## Post #6 by @shahrokh (2023-07-08 11:56 UTC)

<p>Hello Csaba and Andras</p>
<p>Thank you very much again for your guidance.</p>
<p>As you suggested, I tried to use the <strong>DRR Image Computation</strong> module. I have the SlicerRT module on Slicer version 5.0.2 r30822.<br>
Unfortunately, I do not find <strong>Markups perspective projection on the imager plane</strong> part in the module of <strong>DRR Image Computation</strong>.</p>
<p>Anyway at first, I used Andras’ guide by converting the Segment to Volume with the <strong>Mask Volume Effect</strong> in the <strong>Segment Editor</strong> module, as shown in below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4add5fa75b9956097f7dd2ca63a4021a68a33cd3.png" data-download-href="/uploads/short-url/aGhCFmW3njgfGhVP4p1BhouVR0D.png?dl=1" title="figure01" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4add5fa75b9956097f7dd2ca63a4021a68a33cd3_2_690x424.png" alt="figure01" data-base62-sha1="aGhCFmW3njgfGhVP4p1BhouVR0D" width="690" height="424" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4add5fa75b9956097f7dd2ca63a4021a68a33cd3_2_690x424.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4add5fa75b9956097f7dd2ca63a4021a68a33cd3_2_1035x636.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4add5fa75b9956097f7dd2ca63a4021a68a33cd3.png 2x" data-dominant-color="B3B5BF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">figure01</span><span class="informations">1373×845 221 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then I converted <em>LabelMapVolumeCTVCTNormal</em> to Volume in the <strong>Volumes</strong> module. I renamed <em>LabelMapVolumeCTVCTNormal</em> to <em>CTVCTNormalVolume</em>.</p>
<p>In the last step, I used the <strong>DRR Image Computation</strong> module. The settings made in this module are shown in the figure below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d02dfafb24a5dac43b879cc9115ec423c14de417.png" data-download-href="/uploads/short-url/tHDPeEY3EWsQJwTO1tw9TAvhuqH.png?dl=1" title="figure02" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d02dfafb24a5dac43b879cc9115ec423c14de417_2_690x424.png" alt="figure02" data-base62-sha1="tHDPeEY3EWsQJwTO1tw9TAvhuqH" width="690" height="424" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d02dfafb24a5dac43b879cc9115ec423c14de417_2_690x424.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d02dfafb24a5dac43b879cc9115ec423c14de417_2_1035x636.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d02dfafb24a5dac43b879cc9115ec423c14de417.png 2x" data-dominant-color="ABABB5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">figure02</span><span class="informations">1373×845 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As you can see in the above figure, I don’t see an the part of <strong>Markups perspective projection on the imager plane</strong> in this module.<br>
In this regard, where can I use (or tick) this part in this module?</p>
<p>Anyway, I get the following DRR image.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c51e2b4e994e677296ac6d0bdb795590bb4a05ee.png" data-download-href="/uploads/short-url/s7MHkh4OOZvWld7MOkDM4Xl0zH8.png?dl=1" title="figure03" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c51e2b4e994e677296ac6d0bdb795590bb4a05ee_2_450x500.png" alt="figure03" data-base62-sha1="s7MHkh4OOZvWld7MOkDM4Xl0zH8" width="450" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c51e2b4e994e677296ac6d0bdb795590bb4a05ee_2_450x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c51e2b4e994e677296ac6d0bdb795590bb4a05ee.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c51e2b4e994e677296ac6d0bdb795590bb4a05ee.png 2x" data-dominant-color="595B72"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">figure03</span><span class="informations">642×713 36 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The pixel value range in this DRR image is between -255 and zero.</p>
<p>Because I want an the accurate shadow of the segments in the form of a binary image (with sharp edges and no penumbra), the only way I can think of is to use Effects in the <strong>Segment Editor</strong> module; as following:</p>
<p>1- Threshold Effect<br>
Threshold range -255 to -255<br>
2- Logical Operators<br>
Operation: Invert<br>
3- Mask Volume.<br>
Outside fill value: 0<br>
Inside fill value: 1<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e57aed18a2851353944ee4e090ca5a7acecbde19.png" data-download-href="/uploads/short-url/wK4HWFeYryzmVRB603LJwr4uGJr.png?dl=1" title="figure04" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e57aed18a2851353944ee4e090ca5a7acecbde19_2_690x424.png" alt="figure04" data-base62-sha1="wK4HWFeYryzmVRB603LJwr4uGJr" width="690" height="424" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e57aed18a2851353944ee4e090ca5a7acecbde19_2_690x424.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e57aed18a2851353944ee4e090ca5a7acecbde19_2_1035x636.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e57aed18a2851353944ee4e090ca5a7acecbde19.png 2x" data-dominant-color="AFB1BB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">figure04</span><span class="informations">1373×845 144 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Result:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01b176807a447994411763733e511e58b2ba87fe.png" data-download-href="/uploads/short-url/eYGMgwRlp2fsyINInu5EWuahAO.png?dl=1" title="figure05" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01b176807a447994411763733e511e58b2ba87fe_2_452x500.png" alt="figure05" data-base62-sha1="eYGMgwRlp2fsyINInu5EWuahAO" width="452" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01b176807a447994411763733e511e58b2ba87fe_2_452x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01b176807a447994411763733e511e58b2ba87fe.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01b176807a447994411763733e511e58b2ba87fe.png 2x" data-dominant-color="272B29"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">figure05</span><span class="informations">641×708 30.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here is a question for me:</p>
<p>Can this final image be the geometric shadow of the segment of CTVCTNormal?</p>
<p>Please guide me.<br>
Best regards.<br>
Shahrokh.</p>

---

## Post #7 by @cpinter (2023-07-09 08:48 UTC)

<p>You use a Slicer version that is years old, so many features we now have are missing. Please update.</p>

---

## Post #8 by @shahrokh (2023-07-18 12:19 UTC)

<p>Hi Csaba</p>
<p>Thank you very much for your advice.<br>
Unfortunately, I did not succeed. I am trying to create the desired segment shadow in the imager position according to your guidance using <strong>Markups perspective projection on the imager plane</strong> part of the DRR Image Computation module.</p>

---
