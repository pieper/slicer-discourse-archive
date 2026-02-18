# Optical Tracking System Recommendations

**Topic ID**: 40670
**Date**: 2024-12-13
**URL**: https://discourse.slicer.org/t/optical-tracking-system-recommendations/40670

---

## Post #1 by @PhotoJoe (2024-12-13 04:56 UTC)

<p>Hi all,<br>
I am brand new to this area, so I’m sorry for my very basic and limited understanding. I have joined a research team that is looking at using SlicerIGT in combination with Ultrasound Transducers and other cameras. We are looking for recommendations for Optical Tracking systems, and would likely need multiple options in order to apply for the grant. I have seen NDI mentioned several times. Is this the system that is most widely recommended for integration with 3DSlicer and SlicerIGT? Are there any other options that so that we could present quotes for our grant application?</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2024-12-13 05:04 UTC)

<p>For research use, I would recommend <a href="https://www.optitrack.com/cameras/v120-duo/">Optitrack Duo</a> for optical tracking, because it is small, inexpensive, and it has similar accuracy as routinely used clinical optical trackers. Its main limitation for clinical use is that its housing is hard to disinfect, so in sterile environment you need to add a custom housing. Therefore, for clinical use, it is simpler to use an NDI Polaris tracker, which has similar accuracy as the Optitrack Duo, costs 5x more, but has disinfectable housing. PLUS/SlicerIGT is compatible with both (and many other optical and electromagnetic trackers), so you can switch between trackers anytime, without any software change.</p>

---

## Post #3 by @aysegul_sayin (2025-02-26 19:56 UTC)

<p>Hello, I am new here as well and I have a few questions. We are planning to purchase the OptiTrack Duo, a probe, and markers. What I want to achieve is probe tracking and alignment between the MRI and the skull. We also want to use 3D Slicer as the tool. We aim to do something similar to what is shown in this video but with MRI: <a href="https://www.youtube.com/watch?v=d_vHpBRZJco&amp;ab_channel=PerkLabResearch" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=d_vHpBRZJco&amp;ab_channel=PerkLabResearch</a>.<br>
After setting up the system, how should we proceed? Is there a tutorial available for performing these tasks with OptiTrack? If so, could you share it? Another thing I don’t understand is about OptiTrack’s Motive software. Is it necessary to establish the connection between Motive and 3D Slicer?<br>
Thank you</p>

---
