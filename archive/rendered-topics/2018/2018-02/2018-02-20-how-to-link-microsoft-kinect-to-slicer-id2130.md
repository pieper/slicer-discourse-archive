---
topic_id: 2130
title: "How To Link Microsoft Kinect To Slicer"
date: 2018-02-20
url: https://discourse.slicer.org/t/2130
---

# How to link microsoft kinect to slicer

**Topic ID**: 2130
**Date**: 2018-02-20
**URL**: https://discourse.slicer.org/t/how-to-link-microsoft-kinect-to-slicer/2130

---

## Post #1 by @Ahmed_Soufane (2018-02-20 19:49 UTC)

<p>I am working on my fourth year project, and I do not know how to interface 3D slicer with kinect for windows version 2. Can anyone help me please ? I want to control the 3D slicer using the gestures from the kinect windows which uses c# and 3D slicer uses python. I was wondering how to control the rotation, zooming in and out using the gestures instead of a mouse or keyboard.</p>

---

## Post #2 by @lassoan (2018-02-20 20:30 UTC)

<p>I don’t think Slicer has ever had Microsoft Kinect support in any of its public extensions, and since Microsoft has <a href="https://www.polygon.com/2017/10/25/16543192/kinect-discontinued-microsoft-announcement">discontinued Kinect</a>. It is highly unlikely that anybody will invest any time into this.</p>
<p>However, Slicer has Intel RealSense support via <a href="http://www.slicerigt.org">SlicerIGT extension</a> and <a href="http://www.plustoolkit.org">Plus</a>. Currently you can acquire real-time image data and position&amp;orientation of optical markers (2D black-and-white barcodes) and stream it in real-time to Slicer. We’ll add real-time surface acquisition as well in the coming months. Our group does not develop gesture recognition but you can use optical markers to track hands or tools and you can update slice zoom, rotation, etc. based on them.</p>
<div class="lazyYT" data-youtube-id="MOqh6wgOOYs" data-youtube-title="Webcam-based tracking in 3D Slicer/SlicerIGT" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>You can also use LeapMotion controller to adjust slice views:</p>
<div class="lazyYT" data-youtube-id="BG8udCVo1gg" data-youtube-title="Using a LeapMotion controller in 3D Slicer" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>

---
