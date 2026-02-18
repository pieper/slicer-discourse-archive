# Displaying Hounsfield Units / Finding Average

**Topic ID**: 4071
**Date**: 2018-09-11
**URL**: https://discourse.slicer.org/t/displaying-hounsfield-units-finding-average/4071

---

## Post #1 by @Michael.C (2018-09-11 16:28 UTC)

<p>I’m trying to use 3D Slicer to calculate the Hounsfield Unit value for several different samples. The different regions of interest are easily demarcated from one another as they’re solutions in separate tubes within a scan. I believe I can see the Hounsfield value by hovering over specific pixels. I’d like to be able to see the mean HU value for a selected region, but haven’t been able to figure out how to use the Segment Editor tool to display the mean value. Any tips/referral to a tutorial page would be appreciated!</p>
<p>Operating system: Windows<br>
Slicer version: 4.8.1<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @fedorov (2018-09-11 16:28 UTC)

<p>You can use the “Segment Statistics” module for this task.</p>

---

## Post #3 by @Michael.C (2018-09-13 00:32 UTC)

<p>Thanks for the help! Segment Statistics was perfect to get the mean scalar value.</p>
<p>This video shows the steps to use the Segment Statistics tool:<br>
</p><div class="lazyYT" data-youtube-id="fM_rxfDTRi0" data-youtube-title="Segment statistics - new module in 3D Slicer" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>Just to be sure, the scalar value from a CT scan DICOM file is the HU value, correct? Because Slicer calculates (rescales?) the HU value using the file-specific values.</p>

---

## Post #4 by @lassoan (2018-09-13 04:44 UTC)

<aside class="quote no-group" data-username="Michael.C" data-post="3" data-topic="4071">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/6bbea6/48.png" class="avatar"> Michael.C:</div>
<blockquote>
<p>the scalar value from a CT scan DICOM file is the HU value, correct?</p>
</blockquote>
</aside>
<p>Yes. Voxel values in CT scans acquired by clinical scanners are in HU.</p>

---
