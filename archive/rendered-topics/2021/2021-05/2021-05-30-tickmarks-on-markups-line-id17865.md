---
topic_id: 17865
title: "Tickmarks On Markups Line"
date: 2021-05-30
url: https://discourse.slicer.org/t/17865
---

# Tickmarks on markups line

**Topic ID**: 17865
**Date**: 2021-05-30
**URL**: https://discourse.slicer.org/t/tickmarks-on-markups-line/17865

---

## Post #1 by @jumbojing (2021-05-30 17:51 UTC)

<p>查了这里才知道,没有vtkMRMLMarkupsRulerNode,我想加入ruler的效果,该怎么实现呢?</p>
<blockquote>
<p>In <a href="http://apidocs.slicer.org/master/classvtkMRMLMarkupsNode.html" rel="noopener nofollow ugc">Slicer: vtkMRMLMarkupsNode Class Reference</a>, I found out that there is no “vtkMRMLMarkupsRulerNode”, I want to add the effect of “Ruler”(Line with  tick marks), how can I achieve it?</p>
</blockquote>

---

## Post #2 by @pieper (2021-06-09 14:11 UTC)

<p>As far as I know there are no tick marks on the Markups lines like there were on Annotation rulers.  It would be a nice feature for both straight lines and curves to have configurable tick marks at regular intervals in world space.</p>

---

## Post #3 by @lassoan (2021-07-18 03:11 UTC)

<p><a class="mention" href="/u/jumbojing">@jumbojing</a> you could add a feature request to the bugtracker about adding tickmarks to markups line. If the issue gets enough upvotes (<img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:">) then we’ll implement it. If it is urgent for you then you can try to implement it yourself or find a student or software developer with C++ and VTK programming experience who contribute this enhancement.</p>

---

## Post #4 by @lassoan (2021-09-25 19:33 UTC)

<p>The idea of adding tickmarks has come up again <a href="https://github.com/Slicer/Slicer/issues/5889#issuecomment-927158122">here</a>, as we are getting closer to the phase-out of the deprecated annotation ruler and ROI.</p>
<p>Adding tickmarks to markup lines would not be hard, but I’m not sure yet if this is the best fulfillment of the user requirements, or if this is just motivated by limitations (limited display settings, no vertical line, line not movable) of the current view ruler:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba66e17cb7080cb0b64185f59ae5e525155e42a2.jpeg" alt="image" data-base62-sha1="qAZeivnYvUYL6OedsAKzXpQaLfQ" width="522" height="479"></p>
<p>All, who are interested in showing tickmarks for markupines, please describe your workflows: how would you make use of tickmarks and how it would work (would you subdivide the lines to a fix number of sections, or tickmarks positions would be at predefined physical distances, etc).</p>
<p>Showing tick marks for distance measurement is not common in medical image analysis software. If you know of <em>any</em> software that displays tickmarks for distance measurement lines then it would be useful if you could provide screenshots and explain how those software work.</p>

---

## Post #5 by @jamesobutler (2021-09-25 19:51 UTC)

<p>Tickmarks on Markups Line nodes would be to mimic the styling of the Slice viewer ruler. There are ticks marks on that ruler for a reason so therefore should be supported for the line node as well. If you think tickmarks on a ruler is not necessary, you must think the tickmarks on the Slice viewer are also not necessary. Would you have plans to remove these?</p>
<p>The tick mark positions would at minimum be set like the Slice viewer ruler which is determined by the scale. Since a line node is usually fully in view, having the tick interval set by the length of the line makes sense. A line node that is 50mm&gt;length&gt;25mm would have a tick interval of 10mm. A line node that is 25mm&gt;length&gt;10mm would have a major tick interval of 5mm with minor tick interval of 1mm.</p>
<p>Screenshots can be acquired of the slice view and sometimes you can place a ruler node with the tickmarks to be seen in the screenshot to give better detail than the Slice viewer ruler.</p>

---

## Post #6 by @pieper (2021-09-25 20:38 UTC)

<p>I agree with <a class="mention" href="/u/jamesobutler">@jamesobutler</a> that tick marks on markups lines in slice views would be useful in cases where the bottom ruler is not as helpful.  For example a diagonal measurement in the middle of a view.</p>
<p>But it’s especially important in 3D views, where you may want several lines at different orientations and distances from the camera and you don’t wan to be in parallel projection mode to turn on the ruler (which still may be harder to interpret than a line directly on the anatomy of interest).</p>

---

## Post #7 by @lassoan (2021-09-26 01:22 UTC)

<p>Thanks for the additional information.</p>
<h2><a name="p-66947-use-cases-1" class="anchor" href="#p-66947-use-cases-1" aria-label="Heading link"></a>Use cases</h2>
<p>It seems that we have a few quite distinct use cases:</p>
<ol>
<li>Displaying size reference. Have a single object in the view that helps assessing sizes and distances.</li>
<li>Measure distances and size of objects. Trivial in both 2D and 3D, using a linear measurement tool.</li>
<li>Providing visual cues for sizes and distance in 3D, between specific objects or along specific trajectories.</li>
</ol>
<h2><a name="p-66947-implementation-2" class="anchor" href="#p-66947-implementation-2" aria-label="Heading link"></a>Implementation</h2>
<ol>
<li>Displaying size reference in slice views it is trivial - using the “view ruler”. The view ruler is like a scale bar on a map. It is useful if you can read different distances from it, that’s why it often has tickmarks in most software. Tickmarks are well defined because the ruler always shows a “round” distance value (5, 10, 50, 100, …). We can improve it for sure. For example adding an option for displaying a vertical one would make a lot of sense.</li>
</ol>
<p>In 3D views, it is more tricky due to foreshortening and potentially using perspective projection. Some applications show 3 axes or a box with tickmarks or lines, but I don’t think they are really effective. For parallel projection the horizontal/vertical bars are sufficient and for perspective projection nothing really helps. I think it is simply too hard to estimate sizes and distances from a single view in perspective projection mode, with some static size reference objects.</p>
<ol start="2">
<li>
<p>The current markups line implementation fulfills this need quite well.</p>
</li>
<li>
<p>Providing visual distance and size cues between specific obejcts etc. in 3D is hard. Displaying a reference object in 3D that has multiple size markings (such as a ruler object with tickmarks or needle object with depth markers) works quite well. However, simple static rulers are not sufficient for this, as you need to dynamically align the reference object position and direction. For this, you need a specialized module anyway, for example the Breach Warning module in SlicerIGT extension:</p>
</li>
</ol>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62db75e8b65a8da2f2bce12f8e77f98a8ada480b.mp4">
  </div><p></p>
<p>The module used annotation rulers to display the line and the tickmarks were handy, but the appearance of rulers were very poor (2D line, no occluded opacity support, disks as tickmarks were ugly, etc.). Adding nice tickmarks to markup lines would be one solution, but since we need to use a special module anyway, we could get a better, more specialized, more optimized solution with less effort overall.</p>
<hr>
<p>It would be important to know if there are any other use cases, because that would help with deciding on implementations, especially for use case 3.</p>

---

## Post #8 by @jamesobutler (2021-09-26 01:41 UTC)

<p>I can’t comment on 3D view usage as my group use it as 2D slice view stuff only. Placing line node points is difficult in 3D view and then also hard to navigate and see in the 2D slice views. Sometimes yes we might rotate slice intersections and place the points for the line node in a slice view but then it gets difficult to see both endpoints after resetting slice orientations. Anyways…mostly a 2D visual for my group. Really for our ultrasound data we only use 3D view for volume rendering and visualizing the shape of a segmentation.</p>

---

## Post #9 by @lassoan (2021-09-26 04:08 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="8" data-topic="17865">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Placing line node points is difficult in 3D view</p>
</blockquote>
</aside>
<p>It is OK. I don’t know about any obvious limitations. By default the point is placed on the visible surface. You can then choose to move the point in the view plane or move it on the surface.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="8" data-topic="17865">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>then also hard to navigate and see in the 2D slice views</p>
</blockquote>
</aside>
<p>A simple left click jumps all the slice views on the clicked position. Recent Preview Release allows you to click on a line and jump to the nearest point; or click on a point and jump to the previous or next point.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="8" data-topic="17865">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>then it gets difficult to see both endpoints after resetting slice orientations</p>
</blockquote>
</aside>
<p>We could add an action (view context menu action and/or double-click or something like that) to fit the slice view(s) to the object.</p>

---
