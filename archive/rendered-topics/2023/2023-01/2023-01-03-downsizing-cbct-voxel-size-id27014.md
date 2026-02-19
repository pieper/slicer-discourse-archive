---
topic_id: 27014
title: "Downsizing Cbct Voxel Size"
date: 2023-01-03
url: https://discourse.slicer.org/t/27014
---

# Downsizing CBCT voxel size 

**Topic ID**: 27014
**Date**: 2023-01-03
**URL**: https://discourse.slicer.org/t/downsizing-cbct-voxel-size/27014

---

## Post #1 by @Sophrobs (2023-01-03 03:37 UTC)

<p>I’m doing my masters in Orthodontics in Australia. I’m conducting a study examining the effects of another orthodontic appliance, the Twin Block Appliance. The CBCT data I have is 0.3 mm voxel size. I have been using the ‘downsize’ module to change the voxel size to 0.5 mm.</p>
<p>However, since the November update, the ‘Downsize’ module does not work anymore. It says ‘completed with errors’.<br>
Are you able to please help me solve this problem?</p>

---

## Post #2 by @muratmaga (2023-01-03 06:05 UTC)

<aside class="quote no-group" data-username="Sophrobs" data-post="1" data-topic="27014">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/7ba0ec/48.png" class="avatar"> Sophrobs:</div>
<blockquote>
<p>I have been using the ‘downsize’ module to change the voxel size to 0.5 mm.</p>
</blockquote>
</aside>
<p>I am not familiar with <code>Downsize</code> module, is this part of the SlicerCMF? If so, until it is fixed, you can probaby use the core Slicer module <code>Crop VOlume</code>. In crop volume you enter ratios of how much you want to downsample. FOr example 2 would reduce each axis by 50%. In your case you want to enter 1.66.</p>
<p>Alternatively, you can use another module called <code>Resample Scalar Volume</code>, which would allow you to enter the requested voxel spacing directly…</p>

---
