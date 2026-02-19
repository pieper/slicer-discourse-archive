---
topic_id: 7468
title: "Virtual Bronchoscopy"
date: 2019-07-08
url: https://discourse.slicer.org/t/7468
---

# Virtual Bronchoscopy

**Topic ID**: 7468
**Date**: 2019-07-08
**URL**: https://discourse.slicer.org/t/virtual-bronchoscopy/7468

---

## Post #1 by @rbumm (2019-07-08 17:24 UTC)

<p>Hi,</p>
<p>This is my first post here.<br>
I really enjoy 3D Slicer.</p>
<p>Was using the airway segmentation tool of the chest imaging suite to produce an airway model from a CT scan. Worked well. The endoscopy module, however, does not work well with that model.<br>
The model looks great from the outside, but as soon as I am inside, I do not have a closed wall of the model.</p>
<p>Are any tricks available?</p>
<p>Thank you and regards<br>
Rudolf</p>

---

## Post #2 by @pieper (2019-07-08 17:40 UTC)

<p>Yes, you can change the culling (visible sides) option in the Models module:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/Models" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/4.10/Modules/Models</a></p>
<aside class="quote no-group" data-username="rbumm" data-post="1" data-topic="7468">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>I really enjoy 3D Slicer.</p>
</blockquote>
</aside>
<p>Glad to hear it!</p>

---

## Post #3 by @rbumm (2019-07-09 14:58 UTC)

<p>Thank you, that did the trick.</p>

---

## Post #4 by @saeedeh_lavasany (2020-07-19 05:41 UTC)

<p>Hi.<br>
is the virual bronchoscopy mudule available in the 3D slicer?</p>

---

## Post #5 by @lassoan (2020-07-20 02:10 UTC)

<p>Yes, the module is called “Endoscopy”.</p>

---

## Post #6 by @saeedeh_lavasany (2020-07-20 03:11 UTC)

<p>But in endoscopy module you need to set fiducials. What I saw as the bronchoscopy module on YouTube it moves on centerline. Is there anyway to choose start and end point and move on centerline?</p>

---

## Post #7 by @lassoan (2020-07-20 03:31 UTC)

<p>You can set fiducials or use a curve node. you can place the curve points manually or use SlicerVMTK extension’s Extract centerline module to do it automatically from airway segmentation: you can extract the entire bronchial tree automatically then mark two points between them, and use the resulting curve as input in endoscopy module.</p>
<p>Airway segmentation:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="tJMGe3FMTk0" data-video-title="Airway segmentation from CT in 1 minute using 3D Slicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=tJMGe3FMTk0" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/tJMGe3FMTk0/maxresdefault.jpg" title="Airway segmentation from CT in 1 minute using 3D Slicer" width="" height="">
  </a>
</div>

<p>Finding path between two points in the bronchial tree:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="UpfDP6ejCjg" data-video-title="Finding shortest path between two points in the bronchial tree" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=UpfDP6ejCjg" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/UpfDP6ejCjg/maxresdefault.jpg" title="Finding shortest path between two points in the bronchial tree" width="" height="">
  </a>
</div>

<p>After this, you can resample the curve to a new curve in Markups module and use the resulting curve in Endoscopy module. Or you can straighten the selected branch using Curved Planar Reformat module (in Sandbox extension) to make it easier to traverse and make measurements.</p>

---

## Post #8 by @saeedeh_lavasany (2020-07-20 03:57 UTC)

<p>Thank you so much for your help</p>

---

## Post #9 by @akshay_pillai (2020-11-20 16:02 UTC)

<p>Can I ask what settings in models you used to get the result? I have the same issue but I don’t know what visibility is the right one.</p>

---

## Post #10 by @whu (2023-03-06 09:01 UTC)

<p>what’s the name of the new extension of “Endoscopy” ?<br>
I can not find the Endoscopy in the extensions.</p>

---

## Post #11 by @rbumm (2023-03-06 10:37 UTC)

<p>Slicer 5.2.2: it is already included, see</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/1389d8fbac239fc589fd5c4af90477091f381d33.png" alt="image" data-base62-sha1="2MQpmlkaE3erxNqyWWOaY8XoyQz" width="388" height="59"></p>

---
