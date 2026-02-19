---
topic_id: 9876
title: "Difficulty With Multiple Landmark Registrations"
date: 2020-01-20
url: https://discourse.slicer.org/t/9876
---

# Difficulty With Multiple Landmark Registrations

**Topic ID**: 9876
**Date**: 2020-01-20
**URL**: https://discourse.slicer.org/t/difficulty-with-multiple-landmark-registrations/9876

---

## Post #1 by @jrhodes (2020-01-20 04:00 UTC)

<p>I was not sure if it was more appropriate to post this on the PlusLib or here, so I apologize for the repost.</p>
<p>I am on the last part of my arUco webcam project! I have the following setup:</p>
<pre><code>*TrackerToRas
   Marker8ToTracker
      NeedleTipToNeedle
         NeedleModel
*StationaryModel (STL)
*CT Data (.nrrd)
</code></pre>
<p>“NeedleTipToNeedle” was calculated using Pivot Calibration, where “Marker8” is the arUco marker on the stylus.</p>
<p>“TrackerToRas” was calculated using Landmark Registration by using “NeedleTipToNeedle” to place the “From” fiducials on a stationary physical model (i.e., the model will not move and it does NOT have an attached patient reference marker) and then placing the “To” fiducials on the virtual model. This was completed successfully!</p>
<p><strong>Here is the issue I am having:</strong><br>
I need to introduce a new, custom STL model (“NewModel.stl”) that has an arUco marker (“Marker6”) attached to it. Furthermore, when I move this object in real life, I need it to move in the virtual RAS scene in relation to the other objects.</p>
<p>I know I need to perform Landmark Registration; however, I am incredibly confused how to setup this hierarchy. I have been through the tutorials, but am still stuck on this part.</p>
<p>Any advice is appreciated and sorry for all of the questions lately! This is the last step of my project and I cannot thank the community enough for all of the help!</p>

---

## Post #2 by @timeanddoctor (2020-01-20 04:05 UTC)

<aside class="quote no-group" data-username="jrhodes" data-post="1" data-topic="9876">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jrhodes/48/5709_2.png" class="avatar"> jrhodes:</div>
<blockquote>
<p><strong>ssue I am having:</strong><br>
I need to introduce a new, custom STL model (“NewModel.stl”) that has an arUco marker (“Marker6”) attached to it. Furthermore, when I move this object in real life, I need it to move in the virtual RAS scene in relation to the other objects.</p>
</blockquote>
</aside>
<p>Did you connect the plus with the slicer(IGT).</p>

---

## Post #3 by @jrhodes (2020-01-20 04:07 UTC)

<p>Yes they are connected.</p>
<p>My confusion is how to setup the transform hierarchy (in relation to the hierarchy I posted above).</p>
<p>To clarify, I can get what I want through a very roundabout solution, but I cannot get there through landmark registration (which is more accurate and ideal in this scenario).</p>
<p>Here is my roundabout (but not ideal) solution:</p>
<pre><code>*TrackerToRas
   &gt;Marker8ToTracker
      &gt;NeedleTipToNeedle
         NeedleModel
   &gt;Marker6ToTracker
      Locator_Marker6ToTracker
      CoordinateModel
      &gt;ManualTransform
         NewModel (stl)
</code></pre>
<p>Since I knew where the center of the marker is on the model, I created a transform called “ManualTransform” to manually reposition (using the Transform module sliders in 3D Slicer) the NewModel.stl to be aligned properly. Now this works for my purposes, but it would be more accurate if I used landmark registration to complete this task.</p>
<p>However, no matter what I do, I cannot get landmark registration to work correctly on this NewModel.stl.</p>
<p><strong>Do you have any suggestions on how to accomplish this using landmark registration?</strong></p>

---

## Post #4 by @lassoan (2020-01-20 22:34 UTC)

<p>What does “NewModel (stl)” contains? Does it have landmarks that you can touch with a tracked pointer? If yes, then you can collect points in “Marker6” coordinate system and mark the corresponding points on the model (“NewModel” coordinate system) and landmark registration computes NewModelToMarker6Transform.</p>
<p>In general, if you name coordinate systems and transforms consistently then the you it is much easier to see what is the correct solution:</p>
<pre><code class="lang-nohighlight">- TrackerToRas
    - Marker8ToTracker
      - NeedleTipToNeedle
        - NeedleModel_Needle
    - Marker6ToTracker
      - GuideToMarker6
        - NewModel_Guide
- CTData_Ras
</code></pre>

---

## Post #5 by @lassoan (2021-07-12 14:49 UTC)

<p>A post was split to a new topic: <a href="/t/bone-model-registration-for-navigation/18642">Bone model registration for navigation</a></p>

---
