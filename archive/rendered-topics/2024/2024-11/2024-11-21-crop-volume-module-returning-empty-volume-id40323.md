# Crop Volume module returning empty volume

**Topic ID**: 40323
**Date**: 2024-11-21
**URL**: https://discourse.slicer.org/t/crop-volume-module-returning-empty-volume/40323

---

## Post #1 by @Dboerma (2024-11-21 22:24 UTC)

<p>Hello Slicer team!</p>
<p><strong>OS</strong>: Windows 10 (22H2)<br>
<strong>Slicer Version:</strong> 5.6.2<br>
<strong>RAM</strong>: 128 GB</p>
<p><strong>Data</strong>: DICOMs (12.4 GB)</p>
<p><strong>Expected Behavior</strong>: When using an ROI to define a cropping region (both in the Crop Volumes module and when using the ROI in the Volume Renderer), I select the active volume as my Input Volume, successfully resize the Input ROI, create &amp; name a new Output Volume, and click “Apply”. The new Output Volume contains only the region of the Input Volume within the Input ROI.</p>
<p><strong>Actual Behavior:</strong> The cropping does not occur – the new output volume remains empty. When attempting to view the cropped Output Volume, I hide the original Input Volume, show the Output Volume, and the cross-sectional views display only the middle slice of the original Input Volume. When I attempt to scroll through the slices in the new Output Volume, the scroll bar snaps to the far-left, center, and far-right (3 “slices”), but the images themselves do not change.</p>
<p>This issue persists for different Input Volume formats, including .nrrd files.</p>

---

## Post #2 by @lassoan (2024-11-21 22:25 UTC)

<p>Does it work well for smaller volumes? For example volumes in Sample Data module.</p>

---
