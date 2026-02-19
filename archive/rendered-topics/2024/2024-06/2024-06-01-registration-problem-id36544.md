---
topic_id: 36544
title: "Registration Problem"
date: 2024-06-01
url: https://discourse.slicer.org/t/36544
---

# Registration problem

**Topic ID**: 36544
**Date**: 2024-06-01
**URL**: https://discourse.slicer.org/t/registration-problem/36544

---

## Post #1 by @aysegul_sayin (2024-06-01 23:33 UTC)

<p>I have two volumes and I want to overlay them. However, as seen in the image, they do not perfectly overlay. I have set their origins to be the same, aligned their directions from IJK to RAS, adjusted their spacing values, dimensions, and affine matrices to be identical. Despite all these adjustments, they still do not overlay properly. What other parameters can I change to achieve this?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/793899fe6e863994d0f681563053e0784448d1ca.png" data-download-href="/uploads/short-url/hin2C4fAqAhOZ1QARVvSGtLSFVU.png?dl=1" title="Ekran Resmi 2024-06-02 02.20.29" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/793899fe6e863994d0f681563053e0784448d1ca_2_603x500.png" alt="Ekran Resmi 2024-06-02 02.20.29" data-base62-sha1="hin2C4fAqAhOZ1QARVvSGtLSFVU" width="603" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/793899fe6e863994d0f681563053e0784448d1ca_2_603x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/793899fe6e863994d0f681563053e0784448d1ca.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/793899fe6e863994d0f681563053e0784448d1ca.png 2x" data-dominant-color="9A9BCE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Ekran Resmi 2024-06-02 02.20.29</span><span class="informations">724×600 55.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-06-02 13:03 UTC)

<p>Please copy here the complete image header of both images.</p>

---

## Post #3 by @aysegul_sayin (2024-06-02 14:35 UTC)

<p>this one is my volume:<br>
Image (0x7f7e26737340)<br>
RTTI typeinfo:   itk::Image&lt;short, 3u&gt;<br>
Reference Count: 1<br>
Modified Time: 12445<br>
Debug: Off<br>
Object Name:<br>
Observers:<br>
none<br>
Source: (none)<br>
Source output name: (none)<br>
Release Data: Off<br>
Data Released: False<br>
Global Release Data: Off<br>
PipelineMTime: 12422<br>
UpdateMTime: 12444<br>
RealTimeStamp: 0 seconds<br>
LargestPossibleRegion:<br>
Dimension: 3<br>
Index: [0, 0, 0]<br>
Size: [256, 256, 256]<br>
BufferedRegion:<br>
Dimension: 3<br>
Index: [0, 0, 0]<br>
Size: [256, 256, 256]<br>
RequestedRegion:<br>
Dimension: 3<br>
Index: [0, 0, 0]<br>
Size: [256, 256, 256]<br>
Spacing: [0.2, 0.2, 0.2]<br>
Origin: [53.5598, 27.6676, -19.3769]<br>
Direction:<br>
-0.84309 -0.149155 -0.516674<br>
-0.122292 -0.88242 0.454291<br>
-0.523683 0.446193 0.725719</p>
<p>IndexToPointMatrix:<br>
-0.168618 -0.029831 -0.103335<br>
-0.0244584 -0.176484 0.0908582<br>
-0.104737 0.0892386 0.145144</p>
<p>PointToIndexMatrix:<br>
-4.21545 -0.61146 -2.61841<br>
-0.745774 -4.4121 2.23097<br>
-2.58337 2.27145 3.62859</p>
<p>Inverse Direction:<br>
-0.84309 -0.122292 -0.523683<br>
-0.149155 -0.88242 0.446193<br>
-0.516674 0.454291 0.725719</p>
<p>PixelContainer:<br>
ImportImageContainer (0x600006145920)<br>
RTTI typeinfo:   itk::ImportImageContainer&lt;unsigned long, short&gt;<br>
Reference Count: 1<br>
Modified Time: 12441<br>
Debug: Off<br>
Object Name:<br>
Observers:<br>
none<br>
Pointer: 0x7f7dceae0000<br>
Container manages memory: true<br>
Size: 16777216<br>
Capacity: 16777216</p>
<p>and this one is original:<br>
Image (0x7f7df6974590)<br>
RTTI typeinfo:   itk::Image&lt;short, 3u&gt;<br>
Reference Count: 1<br>
Modified Time: 8217<br>
Debug: Off<br>
Object Name:<br>
Observers:<br>
none<br>
Source: (none)<br>
Source output name: (none)<br>
Release Data: Off<br>
Data Released: False<br>
Global Release Data: Off<br>
PipelineMTime: 8194<br>
UpdateMTime: 8216<br>
RealTimeStamp: 0 seconds<br>
LargestPossibleRegion:<br>
Dimension: 3<br>
Index: [0, 0, 0]<br>
Size: [256, 256, 256]<br>
BufferedRegion:<br>
Dimension: 3<br>
Index: [0, 0, 0]<br>
Size: [256, 256, 256]<br>
RequestedRegion:<br>
Dimension: 3<br>
Index: [0, 0, 0]<br>
Size: [256, 256, 256]<br>
Spacing: [0.2, 0.2, 0.2]<br>
Origin: [53.5598, 27.6676, -19.3769]<br>
Direction:<br>
-0.84309 -0.149155 -0.516674<br>
-0.122292 -0.88242 0.454291<br>
-0.523683 0.446193 0.725719</p>
<p>IndexToPointMatrix:<br>
-0.168618 -0.029831 -0.103335<br>
-0.0244584 -0.176484 0.0908582<br>
-0.104737 0.0892386 0.145144</p>
<p>PointToIndexMatrix:<br>
-4.21545 -0.61146 -2.61841<br>
-0.745774 -4.4121 2.23097<br>
-2.58337 2.27145 3.62859</p>
<p>Inverse Direction:<br>
-0.84309 -0.122292 -0.523683<br>
-0.149155 -0.88242 0.446193<br>
-0.516674 0.454291 0.725719</p>
<p>PixelContainer:<br>
ImportImageContainer (0x600006179440)<br>
RTTI typeinfo:   itk::ImportImageContainer&lt;unsigned long, short&gt;<br>
Reference Count: 1<br>
Modified Time: 8213<br>
Debug: Off<br>
Object Name:<br>
Observers:<br>
none<br>
Pointer: 0x7f7e52000000<br>
Container manages memory: true<br>
Size: 16777216<br>
Capacity: 16777216</p>
<p>there is two volume: <a href="https://drive.google.com/drive/folders/1GtVvnPv0G-xs9hYxugUKF_ENNJM6fdSK?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">example_nii - Google Drive</a></p>

---

## Post #4 by @lassoan (2024-06-02 15:55 UTC)

<p>Nifti file stores image orientation in a redundant and potentially ambiguous way, so this kind of issues are practically inevitable. I would recommend to use nrrd file format instead.</p>

---

## Post #5 by @AlfredoMoralesPinzon (2024-06-06 01:21 UTC)

<p>I loaded the images “case12” and “exm2” (exam2 loaded as a segmentation) in Slicer, and they are actually in the same space. However, the object is in different places in the images.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7fdd127d960b45ec4af251703c7fb60218c1a0c.png" data-download-href="/uploads/short-url/x6i5XtOYhVrnRop5RUBlOmeTUjG.png?dl=1" title="Compare_case12_exm2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7fdd127d960b45ec4af251703c7fb60218c1a0c_2_690x375.png" alt="Compare_case12_exm2" data-base62-sha1="x6i5XtOYhVrnRop5RUBlOmeTUjG" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7fdd127d960b45ec4af251703c7fb60218c1a0c_2_690x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7fdd127d960b45ec4af251703c7fb60218c1a0c_2_1035x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7fdd127d960b45ec4af251703c7fb60218c1a0c_2_1380x750.png 2x" data-dominant-color="10100E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Compare_case12_exm2</span><span class="informations">1788×973 82.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
