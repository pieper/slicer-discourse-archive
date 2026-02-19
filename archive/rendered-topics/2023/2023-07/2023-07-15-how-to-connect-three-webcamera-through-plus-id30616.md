---
topic_id: 30616
title: "How To Connect Three Webcamera Through Plus"
date: 2023-07-15
url: https://discourse.slicer.org/t/30616
---

# How to connect three webcamera through Plus?

**Topic ID**: 30616
**Date**: 2023-07-15
**URL**: https://discourse.slicer.org/t/how-to-connect-three-webcamera-through-plus/30616

---

## Post #1 by @jay1987 (2023-07-15 06:12 UTC)

<p>I want to connect three webcamera into my slicer app , one for Axial , One for Saggital , On for Coronal,right now i have managered to connect one webcamera into my Slicer app through Plus,how to connect three ?</p>

---

## Post #2 by @lassoan (2023-07-15 14:55 UTC)

<p>If you use Microsoft Media Foundation video source in Plus then you can choose between devices by the device ID parameter.</p>
<p>Note that cheap cameras often have poor drivers, which may not allow to connect multiple devices to your computer at the same time.</p>

---

## Post #3 by @jay1987 (2023-07-16 00:52 UTC)

<p>thank you lassoan,i have managed change camera by device id, but right now i can show only  one camera image in the red 2d window  in one time, my compute have connected two cameras , is it possible to show one camera in red window and another in yellow window?</p>

---

## Post #4 by @lassoan (2023-07-16 01:11 UTC)

<p>Yes, sure, you can send any number of image streams. In PlusServer configuration, you need to create a <code>PlusOpenIGTLinkServer</code> element for each image stream (set a unique <code>ListeningPort</code> and the correct <code>OutputChannelId</code> for each).</p>

---

## Post #5 by @jay1987 (2023-07-16 01:12 UTC)

<p>thank you very much lassoan</p>

---
