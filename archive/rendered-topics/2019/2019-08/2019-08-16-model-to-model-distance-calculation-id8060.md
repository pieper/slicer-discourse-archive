# Model to model distance calculation

**Topic ID**: 8060
**Date**: 2019-08-16
**URL**: https://discourse.slicer.org/t/model-to-model-distance-calculation/8060

---

## Post #1 by @Jainey (2019-08-16 14:48 UTC)

<p>Hi All<br>
I created two models and was trying to get model to model distance. The following error came up.</p>
<ol>
<li>Model To Model Distance standard error:</li>
</ol>
<p>dyld: Library not loaded: /Volumes/Dashboards/Support/qt-everywhere-build-5.10.0/lib/QtSql.framework/Versions/5/QtSql<br>
Referenced from: /Applications/Slicer.app/Contents/Extensions-28349/ModelToModelDistance/lib/Slicer-4.11/cli-modules/libModelToModelDistanceLib.dylib<br>
Reason: image not found</p>
<ol start="2">
<li>Also - I am trying to create a sequence of models registered to one other-with a transform sequence and an output sequence - Is this possible</li>
</ol>
<p>Thanks</p>

---

## Post #2 by @lassoan (2019-08-16 15:38 UTC)

<p>Could you check if it works with Slicer-4.10.2?</p>

---

## Post #3 by @Jainey (2019-08-16 15:57 UTC)

<p>Thanks Professor <a class="mention" href="/u/lassoan">@lassoan</a> .</p>
<p>I will- then I saw a post saying this had a problem with Mac built . I will try with windows 10 as well and then post the result.</p>
<p>Also what is the best way if I want to get translation and rotation between two segments.please. I am not a programmer I am afraid. Thanks</p>

---

## Post #4 by @lassoan (2019-08-17 19:28 UTC)

<aside class="quote no-group" data-username="Jainey" data-post="3" data-topic="8060">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/a88e57/48.png" class="avatar"> Jainey:</div>
<blockquote>
<p>what is the best way if I want to get translation and rotation between two segments</p>
</blockquote>
</aside>
<p>You can use Segment Registration extension to spatially align/warp segments.</p>

---

## Post #5 by @Jainey (2019-08-18 20:28 UTC)

<p>Thanks Professor <a class="mention" href="/u/lassoan">@lassoan</a><br>
With windows slicer nightly - I don’t get the error. SO probably its Mac related. However I don’t know how to get the distance in numbers or created model sequence/ transformation sequence,.</p>
<p>Thank you</p>

---

## Post #6 by @lassoan (2019-08-19 02:32 UTC)

<p>The simplest is to go through the sequence item by item and perform the computation you need. If you have many sequences or many time points then you can automate the process using a short Python script.</p>

---
