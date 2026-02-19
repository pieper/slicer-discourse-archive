---
topic_id: 10150
title: "How To Fill Color To The Vtkmrmlannotationroinode"
date: 2020-02-07
url: https://discourse.slicer.org/t/10150
---

# How to fill color to the vtkMRMLAnnotationROINode?

**Topic ID**: 10150
**Date**: 2020-02-07
**URL**: https://discourse.slicer.org/t/how-to-fill-color-to-the-vtkmrmlannotationroinode/10150

---

## Post #1 by @tbuikr (2020-02-07 05:56 UTC)

<p>I have created a ROI box as following code</p>
<pre><code class="lang-auto">        import SampleData
        sampleDataLogic = SampleData.SampleDataLogic()
        self.delayDisplay("Getting MR Head Volume")
        mrHeadVolume = sampleDataLogic.downloadMRHead()

        # Create clipping ROI
        roiNode = slicer.vtkMRMLAnnotationROINode()
        roiNode.SetXYZ(36, 17, -10)
        roiNode.SetRadiusXYZ(25, 40, 65)
        roiNode.Initialize(slicer.mrmlScene)
</code></pre>
<p>I want to fill color to the roiNode (such as blue color). Is it possible to do it? I have found some methods but it does not work.</p>

---

## Post #2 by @lassoan (2020-02-07 14:17 UTC)

<p>See how it is done in <a href="https://github.com/PerkLab/SlicerVolumeClip/blob/master/VolumeClipWithRoi/VolumeClipWithRoi.py">Volume clip with ROI module</a> (in Volume Clip extension). Probably the simplest is to set values in a labelmap volume (and then if you want you can import that into a segmentation node).</p>

---
