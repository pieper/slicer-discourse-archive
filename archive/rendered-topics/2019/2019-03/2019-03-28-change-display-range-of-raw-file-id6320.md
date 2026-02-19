---
topic_id: 6320
title: "Change Display Range Of Raw File"
date: 2019-03-28
url: https://discourse.slicer.org/t/6320
---

# Change display range of .raw file

**Topic ID**: 6320
**Date**: 2019-03-28
**URL**: https://discourse.slicer.org/t/change-display-range-of-raw-file/6320

---

## Post #1 by @anitakh1 (2019-03-28 06:44 UTC)

<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @anitakh1 (2019-03-28 06:49 UTC)

<p>hello<br>
i have three questions and would be glad if solved:</p>
<ol>
<li>i have .mhd along with .zraw volume CT data. can i change it to .raw file</li>
<li>i want to convert display range of .zraw file or .raw file from negative and positive range to all positive range from 0 to 255. is it possible using 3D slicer.</li>
<li>as i am working on lung volume data, some volumes contrast is very bad to work on. is it possible to improve it’s contrast to work on.</li>
</ol>

---

## Post #3 by @muratmaga (2019-03-28 19:40 UTC)

<p>I do not know what .zraw format is. But if you can manage to get your data in, you can use the CastScalarVolume module to change your intensity ranges from signed (-127 to 128) to unsigned (0 to 255).</p>
<p>Perhaps take a look at <a href="https://github.com/lassoan/SlicerRawImageGuess" rel="nofollow noopener">https://github.com/lassoan/SlicerRawImageGuess</a> to get your images into slicer.</p>

---

## Post #4 by @jamesobutler (2019-03-28 21:09 UTC)

<p>zraw just means the data is in a compressed format. The corresponding MHD indicates this with the header entry <code>CompressedData = True</code>.  Slicer will load the volume normally.</p>

---

## Post #5 by @lassoan (2019-03-31 04:32 UTC)

<p>You can rescale intensity values in a volume by using numpy:</p>
<pre><code class="lang-auto">volumeNode = getNode('MRHead')

import numpy as np
volumeArray = slicer.util.arrayFromVolume(volumeNode)
# Scale and shift values to be in 0..255 range
scale = 255.0 / (volumeArray.max()-volumeArray.min())
offset = -volumeArray.min()
volumeArray[:] = (volumeArray+offset)*scale
# Signal that voxel data modification is completed
slicer.util.arrayFromVolumeModified(volumeNode)
</code></pre>

---

## Post #6 by @anitakh1 (2019-05-06 05:17 UTC)

<p>sir i am trying to use the codes you mentioned but it’s giving error : Attribute Error: ‘module’ object has no attribute ‘arrayFromVolumeModified’</p>

---

## Post #7 by @anitakh1 (2019-05-06 05:23 UTC)

<p>but it has done the job. you can’t imagine how thankful i am…thanks again</p>

---

## Post #8 by @lassoan (2019-05-06 05:25 UTC)

<aside class="quote no-group" data-username="anitakh1" data-post="6" data-topic="6320">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/anitakh1/48/3350_2.png" class="avatar"> anitakh1:</div>
<blockquote>
<p>Attribute Error: ‘module’ object has no attribute ‘arrayFromVolumeModified’</p>
</blockquote>
</aside>
<p>Use more recent Slicer version, at least the latest stable (currently Slicer-4.10.1).</p>

---

## Post #9 by @anitakh1 (2019-05-06 12:02 UTC)

<p>sir i installed Slicer 4.10.1 but airway related modules are not there.</p>

---

## Post #10 by @lassoan (2019-05-06 13:23 UTC)

<p>Please report this issue to Chest Imaging Platform developers, hopefully they can address this issue soon.</p>
<p><a class="mention" href="/u/raul">@raul</a></p>

---

## Post #11 by @technobrigade (2019-05-07 05:25 UTC)

<p>Use the CastScalarVolume module to change intensity ranges.</p>

---

## Post #12 by @anitakh1 (2019-05-07 07:05 UTC)

<p>thanks for reply. one more thing sir. how to make the figure i enclosed?<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/9938ff32403ad8dd0a9a8c0e25e18d7151b46026.png" data-download-href="/uploads/short-url/lRtaqwbLsuxnqKwblH3DF7pUFV4.png?dl=1" title="airway_slice" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/9938ff32403ad8dd0a9a8c0e25e18d7151b46026_2_690x437.png" alt="airway_slice" data-base62-sha1="lRtaqwbLsuxnqKwblH3DF7pUFV4" width="690" height="437" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/9938ff32403ad8dd0a9a8c0e25e18d7151b46026_2_690x437.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/9938ff32403ad8dd0a9a8c0e25e18d7151b46026.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/9938ff32403ad8dd0a9a8c0e25e18d7151b46026.png 2x" data-dominant-color="CAC2C1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">airway_slice</span><span class="informations">696×441 148 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @textilemarket (2019-05-07 08:48 UTC)

<p>CastScalarVolume module will help change intensity ranges.</p>

---

## Post #14 by @anitakh1 (2019-05-07 10:45 UTC)

<p>one more thing. can you tell me the way to evaluate number of branches in each tree division from my airway segmented result. true results are as shown in pic.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/614e09253ea7cc2124448dff1494ec30ce9024bb.png" data-download-href="/uploads/short-url/dSNvkLwXTu8Vveb7heyQ7rKtwAH.png?dl=1" title="airway_generations" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/614e09253ea7cc2124448dff1494ec30ce9024bb_2_619x500.png" alt="airway_generations" data-base62-sha1="dSNvkLwXTu8Vveb7heyQ7rKtwAH" width="619" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/614e09253ea7cc2124448dff1494ec30ce9024bb_2_619x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/614e09253ea7cc2124448dff1494ec30ce9024bb.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/614e09253ea7cc2124448dff1494ec30ce9024bb.png 2x" data-dominant-color="F8F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">airway_generations</span><span class="informations">765×617 66 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #15 by @anitakh1 (2019-05-18 08:20 UTC)

<p>sir, i am ready with some work on airway segmentation and 3D airway segmented results but i am not able to evaluate my work in terms of number of branches detected, airway length measurement and total false positives. can someone help me in this? i can pay also for that. pl help</p>

---

## Post #16 by @lassoan (2019-05-18 17:10 UTC)

<p>If people will not contact you through the forum here then you may ask <a href="https://www.slicer.org/wiki/CommercialUse#Commercial_Partners" rel="nofollow noopener">Slicer Commercial Partners</a> if they can help and provide a cost estimation.</p>

---

## Post #17 by @anitakh1 (2019-05-19 01:32 UTC)

<p>thanks. will contact them</p>

---

## Post #18 by @anitakh1 (2019-05-22 05:47 UTC)

<p>dear sir,<br>
your rescale intensity code worked very well on my most of the CT volumes but i am having problem with the volume i am enclosing. m getting error<br>
“D:/3Dslicer/Slicer 4.10.1/bin/…/bin/Python/slicer/slicerqt.py:1: RuntimeWarning: overflow encountered in short_scalars   import logging”<br>
can you help.<br>
oops, can’t upload as it’s raw file. sir that volume is available in Exact09 challenge website under testing data (Case24).  pl see sir if you can help. i am confused on type of CT data.<br>
thanks a lot sir</p>

---

## Post #19 by @anitakh1 (2019-05-23 09:59 UTC)

<p>sir,<br>
i contacted slicer commerial partners. they don’t do such work. can we mark different branches of segmented airways with different colour dots in 3D slicer and some way to measure distance between the dots. this way number of airway branches and airway lengths can be calculated.</p>

---

## Post #20 by @lassoan (2019-05-23 14:03 UTC)

<aside class="quote no-group" data-username="anitakh1" data-post="19" data-topic="6320">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/anitakh1/48/3350_2.png" class="avatar"> anitakh1:</div>
<blockquote>
<p>can we mark different branches of segmented airways with different colour dots in 3D slicer and some way to measure distance between the dots. this way number of airway branches and airway lengths can be calculated.</p>
</blockquote>
</aside>
<p>Yes, sure you can do that. In most recent Slicer preview (nightly) versions you can use markups curves to define and get length of entire branch at once. You can compute distance between control points very easily (Euclidean distance, computed from point coordinates). To get started, see <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Tutorials_for_software_developers">Slicer programming tutorials</a>.</p>
<aside class="quote no-group" data-username="anitakh1" data-post="18" data-topic="6320">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/anitakh1/48/3350_2.png" class="avatar"> anitakh1:</div>
<blockquote>
<p>can’t upload as it’s raw file</p>
</blockquote>
</aside>
<p>Upload to onedrive/dropbox/gdrive and just post the link here.</p>

---

## Post #21 by @anitakh1 (2019-08-09 05:56 UTC)

<p>thanks for information. sir i could put points on my segmented length but how to calculate distance between the points. can you please explain.<br>
one more thing sir. i tried airway segmentation by simple region growing module and segment  lung airway module but many airway points are not picked. is it possible to add more airway points somehow to create the actually ground truth. kindly suggest. i read this in one paper, attaching a clipping.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/087ec4cfcaa917dc51ab00c5ec343288fd4a7646.png" data-download-href="/uploads/short-url/1d9q501nh7aGUtBYt6lz4inyUQK.png?dl=1" title="AVIEW_clip" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/087ec4cfcaa917dc51ab00c5ec343288fd4a7646_2_690x277.png" alt="AVIEW_clip" data-base62-sha1="1d9q501nh7aGUtBYt6lz4inyUQK" width="690" height="277" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/087ec4cfcaa917dc51ab00c5ec343288fd4a7646_2_690x277.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/087ec4cfcaa917dc51ab00c5ec343288fd4a7646_2_1035x415.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/087ec4cfcaa917dc51ab00c5ec343288fd4a7646.png 2x" data-dominant-color="C7C8C8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">AVIEW_clip</span><span class="informations">1182×475 203 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
