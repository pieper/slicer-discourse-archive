---
topic_id: 42653
title: "Do We Have This Feature For Watershed Topographic Maps Or Ho"
date: 2025-04-22
url: https://discourse.slicer.org/t/42653
---

# Do we have this feature for watershed topographic maps, or how can we implement it

**Topic ID**: 42653
**Date**: 2025-04-22
**URL**: https://discourse.slicer.org/t/do-we-have-this-feature-for-watershed-topographic-maps-or-how-can-we-implement-it/42653

---

## Post #1 by @lhefeng662 (2025-04-22 14:25 UTC)

<p>Watershed Topographic Map 2.0 simulates the true boundaries of pulmonary vascular basins using artificial intelligence algorithms based on personalized lung anatomical variation patterns. Principle of watershed topographic map: Use digital simulation of the watershed boundary of the pulmonary artery and vein watershed to simulate the real boundary, block the pulmonary branch arteries - the watershed blood dries up; Blocking pulmonary branch veins - venous hypertension leads to blood stasis in the watershed, slow entry of peripheral circulating ICG into the watershed, and clear visualization of watershed boundaries within 30s to 30min after injection of fluorescent ICG into the peripheral vein. Guide doctors in preoperative planning and real-time intraoperative navigation, shorten surgical time, and reduce unexpected risks such as surgical bleeding.</p>

---

## Post #2 by @pieper (2025-04-22 15:50 UTC)

<p>This sounds like a great idea but I don’t think we have this currently.  The models for extracting the pulmonary vasculature are getting very good though and it should be possible to implement this feature.</p>

---

## Post #3 by @lassoan (2025-04-26 14:26 UTC)

<p>The watershed segmentation method is available in the Segment Editor module (in <code>Watershed</code> effect, provided by SegmentEditorExtraEffects extension). You can also use the competitive region growing method implemented in <code>Grow from seeds</code> effect to compute regions that are closest to each vessel branch.</p>
<p>That said, currently, clinicians plan sublobar resection in Slicer by segmenting the arteries and veins (AI segmentation of lobes and vessels, followed by arteries/veins separation by Grow from seeds effect) and then defining the segments by a few cuts in 3D (using Scissors effect). After this the lesion is segmented and based on all these segmentation results the clinician can make a judgment about what region to remove. The tedious, time-consuming step is the artery and vein segmentation, so I’m not sure if computation of the watershed would be particularly helpful. It seems to be more impactful to focus the efforts in automating the artery and vein segmentation.</p>
<p>Maybe <a class="mention" href="/u/eserval">@Eserval</a> can provide some additional useful insights.</p>

---

## Post #4 by @Eserval (2025-05-05 10:44 UTC)

<p>Hello everyone,</p>
<p>I have never used the Watershed effect to segment lung vessels. I tried this time but the result was not very good:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d683cd8668aa890704abfbe626a5cfc6f6b4f63.jpeg" data-download-href="/uploads/short-url/4c9aQ4k3iy4fGMuY0iJQnSX407x.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d683cd8668aa890704abfbe626a5cfc6f6b4f63_2_690x286.jpeg" alt="image" data-base62-sha1="4c9aQ4k3iy4fGMuY0iJQnSX407x" width="690" height="286" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d683cd8668aa890704abfbe626a5cfc6f6b4f63_2_690x286.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d683cd8668aa890704abfbe626a5cfc6f6b4f63_2_1035x429.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d683cd8668aa890704abfbe626a5cfc6f6b4f63_2_1380x572.jpeg 2x" data-dominant-color="374751"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1918×795 154 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Maybe I`m not just used to the tool yet.</p>
<p><a class="mention" href="/u/lhefeng662">@lhefeng662</a>, it’s a great pleasure to meet you. I’m not sure I fully understand the result you’re aiming to achieve. Are you trying to segment only the pulmonary artery and vein, or are you looking for something else?</p>
<p>I’m a thoracic surgeon and use ICG intraoperatively to assess lung parenchyma perfusion and define the intersegmental plane during sublobar resections. I’m not familiar with its application in preoperative CT planning.</p>
<p>If you could elaborate more on your objective, maybe we can develop some ideas together.</p>

---

## Post #5 by @lhefeng662 (2025-05-28 09:38 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09ade5fbe8c6ab24c6b1c683f38615275bdf398f.jpeg" data-download-href="/uploads/short-url/1nCS6YWPN6PKIopIpsouO5yNXK7.jpeg?dl=1" title="b5d5c1d33b2cd8bbca0fcd6d3528cf72" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09ade5fbe8c6ab24c6b1c683f38615275bdf398f.jpeg" alt="b5d5c1d33b2cd8bbca0fcd6d3528cf72" data-base62-sha1="1nCS6YWPN6PKIopIpsouO5yNXK7" width="406" height="500" data-dominant-color="A2A98C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">b5d5c1d33b2cd8bbca0fcd6d3528cf72</span><span class="informations">418×514 44.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Hello, perhaps my meaning is similar to the function of lung segment segmentation. Randomly select a certain segment of blood vessel and obtain its watershed</p>

---

## Post #6 by @lhefeng662 (2025-05-28 09:39 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8fec5efd11a69c4dbce72fa393572888088a34e9.png" data-download-href="/uploads/short-url/kxcHsiKKjQRyH8iMJXU5YNnir0Z.png?dl=1" title="889eca0fff04f1c642fa6d2c67a67c19" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8fec5efd11a69c4dbce72fa393572888088a34e9.png" alt="889eca0fff04f1c642fa6d2c67a67c19" data-base62-sha1="kxcHsiKKjQRyH8iMJXU5YNnir0Z" width="356" height="334"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">889eca0fff04f1c642fa6d2c67a67c19</span><span class="informations">356×334 76.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
For example, in this image, after segmenting these segments of blood vessels, the watershed (a certain lung segment) is obtained</p>

---
