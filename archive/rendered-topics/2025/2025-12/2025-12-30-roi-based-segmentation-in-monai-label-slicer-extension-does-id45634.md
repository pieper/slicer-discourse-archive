# ROI-based segmentation in MONAI Label Slicer extension does not work correctly for specific labels

**Topic ID**: 45634
**Date**: 2025-12-30
**URL**: https://discourse.slicer.org/t/roi-based-segmentation-in-monai-label-slicer-extension-does-not-work-correctly-for-specific-labels/45634

---

## Post #1 by @anuragp2018 (2025-12-30 04:27 UTC)

<h3><a name="p-130946-problem-description-1" class="anchor" href="#p-130946-problem-description-1" aria-label="Heading link"></a>Problem Description</h3>
<p>I am using the <strong>MONAI Label Slicer extension</strong> to perform <strong>ROI-based segmentation</strong> for a <strong>specific label</strong>.<br>
Although the ROI is drawn correctly in Slicer, the segmentation result does <strong>not respect the selected ROI and target label</strong>.</p>
<p>Observed behavior:</p>
<ul>
<li>
<p>The model <strong>ignores the ROI</strong> or partially applies it</p>
</li>
<li>
<p>The output segmentation includes <strong>regions outside the ROI</strong></p>
</li>
<li>
<p>Sometimes a <strong>different label</strong> is segmented instead of the selected one</p>
</li>
<li>
<p>Results are inconsistent across multiple runs on the same data</p>
</li>
</ul>
<p>Expected behavior:</p>
<ul>
<li>
<p>Segmentation should be <strong>strictly constrained to the provided ROI</strong></p>
</li>
<li>
<p>Only the <strong>selected label</strong> should be segmented</p>
</li>
<li>
<p>Output should be deterministic for the same ROI and input volume</p>
</li>
</ul>

---
