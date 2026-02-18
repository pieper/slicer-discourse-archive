# Widen the range in ultrasound system

**Topic ID**: 1399
**Date**: 2017-11-08
**URL**: https://discourse.slicer.org/t/widen-the-range-in-ultrasound-system/1399

---

## Post #1 by @XUXIN_ZENG (2017-11-08 04:49 UTC)

<p>Hi everyone, can anyone help me how to expand the range of the ultrasound system or change the linear probe into convex probe? I tried to change the parameters about image reference in mrml file, but nothing change.</p>

---

## Post #2 by @lassoan (2017-11-08 04:53 UTC)

<p>If you mean simulating convex probe instead of a linear probe, then in the example configuration file delete/comment out the section that refers to linear scan conversion and use the one that refers to curvilinear probe:</p>
<p>From this:</p>
<pre><code>   &lt;RfProcessing&gt;
      &lt;ScanConversion
        TransducerName="Ultrasonix_L9-4/38"
        TransducerGeometry="LINEAR"
        ImagingDepthMm="60.0"
        TransducerWidthMm="40.0"
        OutputImageSizePixel="820 616"
        TransducerCenterPixel="410 0"
        OutputImageSpacingMmPerPixel="0.084 0.087"/&gt;
    &lt;/RfProcessing&gt;
  &lt;/vtkPlusUsSimulatorAlgo&gt;
</code></pre>
<p>To this:</p>
<pre><code>   &lt;RfProcessing&gt;
      &lt;ScanConversion
        TransducerName="Ultrasonix_C5-2/60"
        TransducerGeometry="CURVILINEAR"
        RadiusStartMm="60.0"
        RadiusStopMm="120.0"
        ThetaStartDeg="-28.0"
        ThetaStopDeg="28.0"
        TransducerCenterPixel="410 100"
        OutputImageSizePixel="820 616"
        OutputImageSpacingMmPerPixel="0.084 0.087" /&gt;
    &lt;/RfProcessing&gt;
  &lt;/vtkPlusUsSimulatorAlgo&gt;</code></pre>

---
