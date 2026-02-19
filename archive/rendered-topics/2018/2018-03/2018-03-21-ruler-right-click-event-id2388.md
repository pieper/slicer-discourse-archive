---
topic_id: 2388
title: "Ruler Right Click Event"
date: 2018-03-21
url: https://discourse.slicer.org/t/2388
---

# Ruler Right-click event

**Topic ID**: 2388
**Date**: 2018-03-21
**URL**: https://discourse.slicer.org/t/ruler-right-click-event/2388

---

## Post #1 by @jperdomo23 (2018-03-21 17:18 UTC)

<p>Hi Slicer Discourse,</p>
<p>I am trying to show a context menu when a <a href="http://apidocs.slicer.org/master/classvtkMRMLAnnotationRulerNode.html" rel="nofollow noopener">vtkMRMLAnnotationRulerNode</a> object is right-clicked in Slicer, similar to this example using fiducials from the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Show_a_context_menu_when_a_markup_point_is_clicked_in_a_slice_or_3D_view" rel="nofollow noopener">Slicer Script Repository</a>. Is this possible with ruler objects?</p>
<p>Thank you,</p>
<p>Jonathan Perdomo</p>

---

## Post #2 by @lassoan (2018-03-21 19:26 UTC)

<p>I don’t think there is an event that could be observed. We are working on improving the widgets and in a couple of months we might get to the ruler widget and add this feature. Till then you might use Markup fiducials and connect them using a line created by MarkupsToModel module.</p>

---

## Post #3 by @jperdomo23 (2018-03-21 19:31 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="2388">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>MarkupsToModel</p>
</blockquote>
</aside>
<p>OK thank you, I will look into that!</p>

---
