---
topic_id: 43706
title: "Volume Or Surface Area For 2D Ultrasound Segmentation"
date: 2025-07-13
url: https://discourse.slicer.org/t/43706
---

# Volume or Surface Area for 2D Ultrasound Segmentation?

**Topic ID**: 43706
**Date**: 2025-07-13
**URL**: https://discourse.slicer.org/t/volume-or-surface-area-for-2d-ultrasound-segmentation/43706

---

## Post #1 by @Arian_Amini (2025-07-13 22:16 UTC)

<p>Hello,</p>
<p>I posted this a few weeks ago but received no response, and wanted to try my luck again. I won’t continue to spam with this question if there are no responses again. Thank you for understanding.</p>
<p>I have segmented my ROI of 2D ultrasound images, and confused on how to measure the surface area of my segmentation.</p>
<p>I exported a Segment Statistics table that includes Voxel Count, Volume (mm3), and Surface area (mm2). My assumption was that the Surface Area (mm2) measure would simply give me the surface area of my segmentation, based on the documents on the Slicer website. However, I am receiving some mixed inputs from peers and internet resources, and would appreciate if someone could clear my confusion.</p>
<p>I’m also curious as to why the volume and surface area values would be different for a 2D segmentation. Assuming the depth of the segment is 1 mm (given that it’s 2D), shouldn’t the formula for calculating volume and surface area yield the same result?</p>
<p>For example, one of my segments has the following properties:<br>
Voxel Count: 164574<br>
Volume [mm3]: 691.31<br>
Surface area [mm2]: 1900.42</p>
<p>This is all quite new to me, so I would greatly appreciate some clarity. Thank you.</p>

---

## Post #2 by @pieper (2025-07-13 22:30 UTC)

<p>Everything in Slicer is 3D, so your ultrasound frame is a one-slice volume.  You can check the spacing value (it’s probably one) then the surface area is the top surface plus the bottom surface plus the thin extruded edge around the side (show your segmentation in 3D to see what I mean).</p>

---

## Post #3 by @Arian_Amini (2025-07-14 17:24 UTC)

<p>That makes a lot of sense now, thank you so much. Visualizing the segmentation helps.</p>

---
