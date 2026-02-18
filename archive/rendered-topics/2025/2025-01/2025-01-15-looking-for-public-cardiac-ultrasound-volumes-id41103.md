# Looking for Public Cardiac Ultrasound Volumes

**Topic ID**: 41103
**Date**: 2025-01-15
**URL**: https://discourse.slicer.org/t/looking-for-public-cardiac-ultrasound-volumes/41103

---

## Post #1 by @Hanae (2025-01-15 23:26 UTC)

<p>Hello,</p>
<p>I’m currently exploring how reinforcement learning can be applied to autonomous ultrasound scanning. As part of my research, I’m looking for publicly available 3D volumes of cardiac ultrasound that I can use in <strong>3D Slicer</strong> to simulate ultrasound images and corresponding probe interactions. Unfortunately, I don’t have access to a real environment at the moment to collect actual scanning data and trajectories.</p>
<p>Could anyone kindly point me to any resources or public datasets for cardiac ultrasound volumes that could help with this task?</p>
<p>Thank you for your help</p>

---

## Post #2 by @lassoan (2025-01-16 03:00 UTC)

<p>If you install SlicerHeart extension then you’ll get a couple of 4D cardiac ultrasound image series in the Sample Data module.</p>
<p>However, if you plan to position a 2D probe then you probably want to get actual 2D ultrasound images for training, because you cannot accurately simulate 2D ultrasound images by reslicing a 3D ultrasound volume (they have very different image resolution, beam thickness, frame rate, direction of sound relative to image plane normal, shape and size of the transducer, etc.).</p>

---

## Post #3 by @Hanae (2025-01-20 00:56 UTC)

<p>Thank you for your reply.</p>

---
