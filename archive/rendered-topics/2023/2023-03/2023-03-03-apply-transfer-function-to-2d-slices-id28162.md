---
topic_id: 28162
title: "Apply Transfer Function To 2D Slices"
date: 2023-03-03
url: https://discourse.slicer.org/t/28162
---

# Apply transfer function to 2D slices

**Topic ID**: 28162
**Date**: 2023-03-03
**URL**: https://discourse.slicer.org/t/apply-transfer-function-to-2d-slices/28162

---

## Post #1 by @Amin_Nasim_saravi (2023-03-03 23:28 UTC)

<p>Hello,</p>
<p>Is it possible to use the manually designed transfer function in the “Volume Rendering” section as a color map for 2D slices? I want to see a slice of the volume, but with the color mapping that I defined in the transfer function. If this feature does not exist, how can I define a new color map for 2D slices?</p>
<p>Thanks,</p>

---

## Post #2 by @lassoan (2023-03-04 03:35 UTC)

<p>This feature is already available, but it does not work exactly the way you described.</p>
<p>You can synchronize slice view and volume rendering display settings by checking the checkbox in the “Synchronize with Volumes module” button in Volume Rendering module → Advanced… → Volume Properties.</p>
<p>Differences compared to what you wish:</p>
<ul>
<li>It is not really a “sync” but a “one-way copy”. After enabling synchronization, transfer functions (opacity and color mapping) must be set in Volumes module and changes are automatically applied to volume rendering.</li>
<li>Since slice views look similar to volume rendering only if the opacity transfer function contains just 0.0 and 1.0 values. Therefore, only “thresholding” opacity transfer function is available (opacity = 1.0 between the lower and upper threshold values and 0.0 outside).</li>
<li>Color transfer function can be edited in Colors module. Select a continuous scale colormap (such as any of the PET… colormaps), click “Copy” button to create an editable version, then modify it according to your needs. You can then select this colormap in the Volumes module.</li>
</ul>

---
