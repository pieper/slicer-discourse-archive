---
topic_id: 28150
title: "Fcal Temporal Calibration With Live Streaming Data"
date: 2023-03-03
url: https://discourse.slicer.org/t/28150
---

# Fcal Temporal calibration with live streaming data

**Topic ID**: 28150
**Date**: 2023-03-03
**URL**: https://discourse.slicer.org/t/fcal-temporal-calibration-with-live-streaming-data/28150

---

## Post #1 by @Qianqian_Cai (2023-03-03 06:14 UTC)

<p>Hardware:</p>
<ul>
<li>OptiTrack for tracking</li>
<li>Clarius probe for imaging</li>
</ul>
<p>In the example configuration file of the temporal calibration, the two datasets from the tracker and probe were recorded and provided to fcal as sequence files.</p>
<ul>
<li>SequenceFile=“WaterTankBottomTranslationTrackerBuffer-trimmed.igs.mha”</li>
<li>SequenceFile=“WaterTankBottomTranslationVideoBuffer.igs.mha”</li>
</ul>
<p>I was able to stream the image and tracking data to Slicer as instructed in “Streaming of live images and tracking data to 3D Slicer”. So I am wondering, with a similar configuration, can I perform the temporal calibration using the living streamed datasets?</p>

---
