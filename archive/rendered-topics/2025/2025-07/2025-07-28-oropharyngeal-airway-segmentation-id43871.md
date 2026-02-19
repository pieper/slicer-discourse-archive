---
topic_id: 43871
title: "Oropharyngeal Airway Segmentation"
date: 2025-07-28
url: https://discourse.slicer.org/t/43871
---

# Oropharyngeal airway segmentation

**Topic ID**: 43871
**Date**: 2025-07-28
**URL**: https://discourse.slicer.org/t/oropharyngeal-airway-segmentation/43871

---

## Post #1 by @bilbro (2025-07-28 10:26 UTC)

<p>Can somebody help me how to segment oropharyngeal airway in the 3D slicer. Thank you</p>

---

## Post #2 by @nagy.attila (2025-07-28 11:04 UTC)

<p>Hi,</p>
<p>What modality? If you have a CT that’s super easy hen because the Hounsfield value for air is pretty much different from anything else on the scan.<br>
If this is the case, a simple Threshold operation will do. You may need to cut a few parts (scissor tool), but that’s about it.<br>
With CBCT and MRI it is a bit more complicated, but not by much.<br>
If you plan to use the segment in other software (FEM for example), then it gets a bit more tricky but then most of the difficulties can be treated outside Slicer.</p>
<p>Let me know if you have further questions!<br>
Attila<br>
Attila</p>

---

## Post #3 by @bilbro (2025-08-05 13:40 UTC)

<p>Thank you for the inputs. I want to do it using CBCT. Is it possible?</p>
<p>Also i need to assess the volume of the segmented airway</p>

---

## Post #5 by @nagy.attila (2025-08-05 14:14 UTC)

<p>CBCT should work nicely. It’s just that the threshold tool will not use HU units (someone can correct me if I’m wrong here <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> )<br>
Other than that, the procedure should be the same. Segment, correct, the segmentation, and there you go.<br>
Volume: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html" rel="noopener nofollow ugc">segment statistics</a> should cover you.</p>

---

## Post #6 by @bilbro (2025-08-05 16:14 UTC)

<p>can you please guide with any document or videos to do a airway segment. As am new to slicer 3d struggling lil bit to find a way to do it. Thanks in advance</p>

---

## Post #7 by @nagy.attila (2025-08-14 19:38 UTC)

<p>Sorry for the late reply!<br>
I’m planning to put together a short video, in case it’s still interesting to you.</p>
<p>Just need a little more patience, I’m a bit busy these days.<br>
Will get back to you in a week or so.</p>
<p>Best.</p>
<p>Attila</p>

---
