---
topic_id: 1348
title: "Replacing Bone Model In Ultrasound Simulator"
date: 2017-11-01
url: https://discourse.slicer.org/t/1348
---

# Replacing bone model in ultrasound simulator

**Topic ID**: 1348
**Date**: 2017-11-01
**URL**: https://discourse.slicer.org/t/replacing-bone-model-in-ultrasound-simulator/1348

---

## Post #1 by @XUXIN_ZENG (2017-11-01 18:14 UTC)

<p>Recently, I wanted to simulate ultrasound image from CT scan data. And then, I tried to replace the vessel model with a bone model in tracked ultrasound simulator. But the simulated bone ultrasound image seems more like a vessel ultrasound image. So I wonder what parameters I should use to get a better result?<br>
Here are my parameters values and the result I got:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/1743111c75e7fea3d3dcd0282fcfc25a5c299c1c.png" data-download-href="/uploads/short-url/3jMFEDSdB0RKq1eOWbUXfTd0vPm.png?dl=1" title="spine" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/1743111c75e7fea3d3dcd0282fcfc25a5c299c1c_2_690x437.png" alt="spine" data-base62-sha1="3jMFEDSdB0RKq1eOWbUXfTd0vPm" width="690" height="437" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/1743111c75e7fea3d3dcd0282fcfc25a5c299c1c_2_690x437.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/1743111c75e7fea3d3dcd0282fcfc25a5c299c1c_2_1035x655.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/1743111c75e7fea3d3dcd0282fcfc25a5c299c1c.png 2x" data-dominant-color="ACACB5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">spine</span><span class="informations">1294×820 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/256302e4a7a92d6f44c4980b5c5fdb0cefec06b5.png" alt="parameters" data-base62-sha1="5kJNqdc8tSCHb844XSjycTOh7Vj" width="593" height="331"></p>

---

## Post #2 by @lassoan (2017-11-01 20:30 UTC)

<p>You have to adjust acoustic parameters of the SpatialModel element to model behavior of a bone. See <a href="https://github.com/PlusToolkit/PlusLibData/blob/master/ConfigFiles/Testing/PlusDeviceSet_UsSimulatorAlgoTestLinear.xml">PlusDeviceSet_UsSimulatorAlgoTestLinear.xml</a> file:</p>
<pre><code>  DensityKgPerM3="1900"
  SoundVelocityMPerSec="4000"
  AttenuationCoefficientDbPerCmMhz="15.0"
  BackscatterDiffuseReflectionCoefficient="0.03"
  SurfaceSpecularReflectionCoefficient="0.1"
  SurfaceDiffuseReflectionCoefficient="0.0"
  TransducerSpatialModelMaxOverlapMm="10"</code></pre>

---
