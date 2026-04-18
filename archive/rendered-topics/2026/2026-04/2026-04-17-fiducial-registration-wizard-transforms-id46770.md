---
topic_id: 46770
title: "Fiducial Registration Wizard Transforms"
date: 2026-04-17
url: https://discourse.slicer.org/t/46770
---

# Fiducial Registration Wizard transforms

**Topic ID**: 46770
**Date**: 2026-04-17
**URL**: https://discourse.slicer.org/t/fiducial-registration-wizard-transforms/46770

---

## Post #1 by @Zaky_Alfarizi (2026-04-17 13:51 UTC)

<p>I’m a beginner, I already have a calibrated pointer. I have a tracker at my object in real life, the pointer should be relative to the tracker on my real life object/reference, right? So my pointer transform will be calculated with the reference or anchor of the tracker that I attached to my object. How do I do it? Because I see that there is only one in the fiducial registration wizard, so I only created it for my dcom/ctscan data.</p>

---

## Post #2 by @lassoan (2026-04-18 00:19 UTC)

<p>I’m not sure what you mean by “tracker” (your tracking camera? a tracker marker attached to your “patient”?) and “at my object” (is the marker actually attached - clamped, screwed - to the object?). If you can describe very precisely what tracking markers you have and what transforms do you stream via PLUS then we have a better chance of answering. Just in case you have not seen it already, the <a href="https://www.slicerigt.org/wp/user-tutorials/">SlicerIGT-U12_LandmarkRegistration tutorial</a> gives a very detailed explanation of the whole process.</p>

---

## Post #3 by @Zaky_Alfarizi (2026-04-18 03:06 UTC)

<p>Hi Andras,</p>
<p>Thank you for your reply.</p>
<p>Let me clarify my setup more precisely.</p>
<p>By “tracker”, I mean a rigid body with optical markers (OptiTrack) that is physically attached to my phantom skull (like a reference marker, similar to a patient reference in navigation systems). It is fixed to the object and moves together with it.</p>
<p>So in my setup I have:</p>
<ul>
<li>A PhantomTracker (rigid body attached to the skull → serves as reference frame)</li>
<li>A StylusTracker (rigid body attached to the pointer tool)</li>
<li>Both are streamed via PLUS (OptiTrack → PLUS → OpenIGTLink → Slicer)</li>
</ul>
<p>What I want to achieve is:</p>
<ul>
<li>The stylus position should be computed relative to the PhantomTracker (object reference), not relative to the global tracking coordinate system.</li>
</ul>
<p>So effectively:</p>
<ul>
<li>StylusToPhantomTracker = StylusToTracker × inverse(PhantomTrackerToTracker)</li>
</ul>
<p>Currently, I have:</p>
<ul>
<li>Performed pivot calibration for the stylus</li>
<li>Performed fiducial registration between CT (DICOM) and the tracked object (phantom)</li>
</ul>
<p>But I am unsure about:</p>
<ul>
<li>The correct way to define and use this object reference (PhantomTracker) in Slicer</li>
<li>Whether this relative transform should be handled via PLUS configuration or within Slicer (e.g., transform chaining or scripting)</li>
</ul>
<p>Also, in the Fiducial Registration Wizard, I only see one transform being generated (CT to tracker), so I’m not sure how to properly incorporate the PhantomTracker as a reference frame in this workflow.</p>
<p>Any clarification on the correct pipeline for this setup would be very helpful.</p>
<p>Thank you!</p>
<p>Best regards,<br>
Zaky</p>

---
