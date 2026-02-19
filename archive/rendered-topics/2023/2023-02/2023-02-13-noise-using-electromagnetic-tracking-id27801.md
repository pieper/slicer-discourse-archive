---
topic_id: 27801
title: "Noise Using Electromagnetic Tracking"
date: 2023-02-13
url: https://discourse.slicer.org/t/27801
---

# Noise Using Electromagnetic Tracking

**Topic ID**: 27801
**Date**: 2023-02-13
**URL**: https://discourse.slicer.org/t/noise-using-electromagnetic-tracking/27801

---

## Post #1 by @brennachampion (2023-02-13 23:10 UTC)

<p>Hello,<br>
I’m trying to use electromagnetic tracking to track a tool through space. I have been able to connect to the tool, gone through pivot calibrations and fiducial registration wizard, and I am noticing a lot of noise in my system as it is being tracked. Is there some sort of filter I can use to reduce the noise within Slicer or is this something that should be taken care of through Plus Server Launcher or before? Any help/insights will be greatly appreciated.<br>
Thank you.</p>

---

## Post #2 by @lassoan (2023-02-14 02:32 UTC)

<p>You can apply additional smoothing to the Transform Processor module in SlicerIGT extension. However, it is probably better to acquire the transforms with less noise.</p>
<p>What EM tracker do you use (NDI Aurora, Ascension,…)? Aurora tends to be more susceptible to noise, but both systems can apply smoothing internally (at the cost of slower/less agile tracking).</p>
<p>Which field generator do you use? Larger, more powerful generators tend to reduce the electronic noise or noise coming from the environment.</p>
<p>What is your sensor size? Sensors that fit into a needle provide much more noisy measurements. The 8mm Ascension sensor and the large Aurora reference sensor are good. Use one of these bigger sensors for reference, as relative position measurement between two small sensors can be very noisy.</p>
<p>How far the reference and tool sensors are from the field generator? About 10-50cm is ideal. As you get farther, the signal may get more noisy.</p>
<p>How far is the tooltip from the sensor? If the sensor is farther than a few centimeters then any orientation error can lead to significant position error. If the distance is more than 10-20cm then a small noise in orientation leads to huge noise in position.</p>

---

## Post #3 by @brennachampion (2023-02-15 16:00 UTC)

<p>I am using the NDI Aurora system. I’m not sure which field generator we use, it is on loan from NDI. Our sensor is quite small, but we do have some larger sensors we can test for reference.</p>
<p>We stay just less than 50cm from the field generator for our purposes. I have noticed the signal gets more stable around 15-30cm, but we still need a better signal as we approach 50cm.</p>
<p>The sensor is about 1.5cm from the tip, so not too far.</p>
<p>When using the Transform Processor module, I’m assuming you’d want to use the Stabilize processing mode, is this correct? What would I put for my input and output transforms and where should they fall in the transform hierarchy?</p>

---

## Post #4 by @lassoan (2023-02-15 18:14 UTC)

<aside class="quote no-group" data-username="brennachampion" data-post="3" data-topic="27801">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/e19b73/48.png" class="avatar"> brennachampion:</div>
<blockquote>
<p>The sensor is about 1.5cm from the tip, so not too far.</p>
</blockquote>
</aside>
<p>What is the diameter of the cylinder (that contains the tracking coil) at the tip? If it is a small sensor then it is normal to have a noisy signal. The NDI Aurora tends to pick up various environmental noise anyway - try to move it away from everything, put your whole setup on a wooden table, move things around, etc. to see if you can reduce the jitter.</p>
<aside class="quote no-group" data-username="brennachampion" data-post="3" data-topic="27801">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/e19b73/48.png" class="avatar"> brennachampion:</div>
<blockquote>
<p>When using the Transform Processor module, I’m assuming you’d want to use the Stabilize processing mode, is this correct? What would I put for my input and output transforms and where should they fall in the transform hierarchy?</p>
</blockquote>
</aside>
<p>Correct. Use the ToolToReference transform as input and create a new transform, such as StabilizedToolToReference as output. Use the stabilized transform to position your tool in the scene.</p>

---

## Post #5 by @brennachampion (2023-02-21 23:53 UTC)

<p>Sounds great. This was helpful. Thank you.</p>

---
