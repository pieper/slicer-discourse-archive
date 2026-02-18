# How to display the specific slice number in 3D Slicer?

**Topic ID**: 36560
**Date**: 2024-06-02
**URL**: https://discourse.slicer.org/t/how-to-display-the-specific-slice-number-in-3d-slicer/36560

---

## Post #1 by @dan_zhao (2024-06-02 18:52 UTC)

<p>Hello everyone,</p>
<p>I am using 3D Slicer to view a series of medical images, and I would like to know how to display the specific slice number in the slice viewer. I have loaded my image data and set up the Four-up layout to view axial, sagittal, and coronal slices. However, I cannot find the option to show the current slice number in the viewer.</p>
<p>Could someone please guide me on how to enable this feature?</p>
<p>Thank you for your assistance!</p>
<p>Best regards,<br>
Dan Zhao</p>

---

## Post #2 by @lassoan (2024-06-02 19:01 UTC)

<p>Each image that you see in slice viewers are created by reconstructing a volume from all the input image slices and then extracting an arbitrary slice of it at any orientation. So, a single displayed image may be constructed from hundreds of input slices.</p>
<p>For a single point position you could determine the closest input image slice. But in general it is better if you can let go the concept of 2D slices and work in 3D instead.</p>
<p>What is your overall goal?</p>

---
