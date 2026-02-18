# Updating the display while we in a for loop

**Topic ID**: 16053
**Date**: 2021-02-18
**URL**: https://discourse.slicer.org/t/updating-the-display-while-we-in-a-for-loop/16053

---

## Post #1 by @11141 (2021-02-18 07:35 UTC)

<p>Hi.</p>
<p>I created an extension using the Extension Wizard, which allows to place fiducials on positions where the moving machine is tracked.</p>
<p>for implementing this feature, I used the ‘for’ loop.<br>
when the loop is executing, however, Slicer program is put on standby, and the fiducials are displayed at once after the loop are completed.</p>
<p>I would like to see the fiducials every time the loop runs one cycle.<br>
What should I do?? I would appreciate it if I could get your help.</p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2021-02-18 12:32 UTC)

<p>If you want to update the screen while you are processing data you need the give the application a chance to process events, by calling <code>slicer.app.processEvents()</code>. However, blocking the event queue by a for loop should be avoided in general (it is OK if you do some long processing, but not for collecting data), because GUI updates will not be smooth.</p>
<p>Instead, you can can add an observer to the transform that you want to collect data from and add the point in the callback function. If you want to do time-based sampling (record a point at regular time intervals) then use a qt.QTimer and add the point in its callback function.</p>
<p>Note that there are several modules for collecting fiducials in SlicerIGT extension, <a href="https://github.com/SlicerIGT/SlicerTrackingErrorInspector">TrackingErrorInspector</a>, etc. If to describe what you would like to achieve then we can recommend similar modules that you can use or extend to fit your needs.</p>

---

## Post #3 by @11141 (2021-02-19 06:32 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="16053">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>slicer.app.processEvents()</p>
</blockquote>
</aside>
<p>I really appreciate your help!<img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
