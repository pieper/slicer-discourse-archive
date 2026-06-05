---
topic_id: 47219
title: "Clarification on L3 SMA calculations and Pixel Spacing"
date: 2026-06-03
url: https://discourse.slicer.org/t/47219
last_bumped: 2026-06-04T07:31:29.487Z
---

# Clarification on L3 SMA calculations and Pixel Spacing

**Topic ID**: 47219
**Date**: 2026-06-03
**URL**: https://discourse.slicer.org/t/clarification-on-l3-sma-calculations-and-pixel-spacing/47219

---

## Post #1 by @merckins (2026-06-03 09:33 UTC)

<p>Hello,</p>
<p>I’m working on calculating CT L3 SMA, but some aspects are still unclear to me. I may be overlooking something, so I would really appreciate any feedback.</p>
<p>I have original CT volumes with differing pixel spacings, and L3 slices were selected from these volume. For example, an L3 slice from patient 1 has the following image dimensions (from 3D Slicer) (512 x 512 x 1) and image spacing information (0.806, 0.806, 1.0mm).</p>
<p>I also have a segmentation mask with the following dimensions (512 x 512 x 1) and the following image spacing information (1,1,1). The mask was the output of a segmentation algorithm + some postprocessing steps.</p>
<p>When I try to calculate the SMA using the original CT spacings, I get more reasonable values. However, when I calculate the SMA using (1,1) spacing, the calculated L3 SMAs are too large. So in this case it’s 192 cm2 vs. 295.13 cm2. For some others the SMA is in the 300s.</p>
<p>Here is my python code for calculating the SMA:</p>
<pre><code class="lang-auto"># read dicom file - orig CT slice
ds = pydicom.dcmread(str(file_dcm))

spacing_x, spacing_y = ds.PixelSpacing 
#print(“Pixel spacings:”, spacing_x, spacing_y)


# calculate SMA
pixel_area = spacing_x * spacing_y 
# pixel_area = 1

sma = np.sum(muscle == 1) * pixel_area / 100  # cm²
</code></pre>
<p>Thank you</p>

---

## Post #2 by @lassoan (2026-06-03 20:57 UTC)

<p>Since now skeletal muscles can be segmented properly in 3D, I would recommend to not bother with 2D slices. You can get the muscles using TotalSegmentator or other models and then get all the cross-sectional areas of all the muscles or any other structures in across a line using <code>Segment Cross-Section Area</code> module in Sandbox extension or using <a href="https://github.com/jmhuie/Slicer-SegmentGeometry">Segment Geometry</a> or <a href="https://github.com/vmtk/SlicerExtension-VMTK#the-vmtk-extension-for-3d-slicer">SlicerVMTK</a> extensions. Getting the cross sections in all the slices instead of an arbitrarily selected point at L3 level would give you more confidence in your data.</p>
<p>In general, make sure you always work in physical space, i.e., always know the geometry of your image (origin, spacing, axis directions; usually stored as an IJK to LPS matrix), and always maintain the geometry information when you process an image (copy IJK to LPS from the input image to the output image).</p>

---

## Post #3 by @merckins (2026-06-04 07:31 UTC)

<p>Thank you for the response. I will focus on the 3D volume instead.</p>

---
