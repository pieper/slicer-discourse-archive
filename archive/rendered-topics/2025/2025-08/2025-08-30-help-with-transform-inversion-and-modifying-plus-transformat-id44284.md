# Help with Transform Inversion and Modifying PLUS Transformation in Slicer

**Topic ID**: 44284
**Date**: 2025-08-30
**URL**: https://discourse.slicer.org/t/help-with-transform-inversion-and-modifying-plus-transformation-in-slicer/44284

---

## Post #1 by @daimon2 (2025-08-30 09:24 UTC)

<p>Dear Slicer Community,</p>
<p>I am a beginner working through the tutorial “day2_PrototypingImageGuidedTherapyApplications,” and I need some help with transformations. The transformation I am receiving from Optitrack through PLUS is “Reference-To-Tracker,” but I require a “Tracker-To-Reference” transformation. I tried to invert the transformation in Slicer’s Transform module, but the data is quickly overwritten.</p>
<p>Could anyone guide me on how the inversion step is achieved in the tutorial? Is this done within Slicer or by modifying the PLUS configuration file?</p>
<p>Additionally, I have a question about the received PLUS transformation data (Stylus-To-Tracker). What is the significance of modifying the “Center of Transformation” in the Transform module (world vs. local)?</p>
<p>Lastly, I’m curious about how to handle dynamic transformations that are input into Slicer. How can I clone the transformation to preserve its current state (since cloning directly seems to result in static data)? (working in an IGT system with multiple tools)</p>
<p>Thank you for your help!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/892a574a245c2e9f2ce760a2f76763669dc90789.jpeg" data-download-href="/uploads/short-url/jzq7YemsfbtBFGgL9BAdknLnn5v.jpeg?dl=1" title="wechat_2025-08-30_172616_660" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/892a574a245c2e9f2ce760a2f76763669dc90789_2_690x475.jpeg" alt="wechat_2025-08-30_172616_660" data-base62-sha1="jzq7YemsfbtBFGgL9BAdknLnn5v" width="690" height="475" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/892a574a245c2e9f2ce760a2f76763669dc90789_2_690x475.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/892a574a245c2e9f2ce760a2f76763669dc90789_2_1035x712.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/892a574a245c2e9f2ce760a2f76763669dc90789.jpeg 2x" data-dominant-color="EAE8E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">wechat_2025-08-30_172616_660</span><span class="informations">1342×924 149 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @ungi (2025-08-31 16:12 UTC)

<p>I would recommend adding both TrackerToReference and ReferenceToTracker in the PLUS config file in the PlusOpenIGTLinkServer section. That way, you will have both in Slicer and you can use whichever is needed.</p>
<p>Alternatively, you could add an observer to the Modified event of ReferenceToTracker and implement a python function in Slicer that computes its inverse or does anything else. This callback function is hopefully an answer to your last question too.</p>
<p>For your second question, the “Center of transformation” on the Transforms module UI is just a convenience feature that I never use. I guess it allows you to define a center of rotation in the two different coordinate systems (world meaning the 3D viewer and local meaning the the selected transform node).</p>

---

## Post #3 by @lassoan (2025-08-31 19:41 UTC)

<aside class="quote no-group" data-username="ungi" data-post="2" data-topic="44284">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/ungi/48/78573_2.png" class="avatar"> ungi:</div>
<blockquote>
<p>For your second question, the “Center of transformation” on the Transforms module UI is just a convenience feature that I never use. I guess it allows you to define a center of rotation in the two different coordinate systems (world meaning the 3D viewer and local meaning the the selected transform node).</p>
</blockquote>
</aside>
<p>If you choose <code>Local</code> then the displayed coordinate values are in the local (i.e., transform’s parent) coordinate system. If you choose <code>World</code> then the center of rotation coordinates are displayed in the renderer’s world coordinate system. You can see the difference if you apply a parent transform and modify it - <code>Local</code> coordinates don’t change, while <code>World</code> coordinates do.</p>

---
