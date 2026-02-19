---
topic_id: 4364
title: "Hovering Over A Fiducial Is No Longer Pointinghandcursor"
date: 2018-10-11
url: https://discourse.slicer.org/t/4364
---

# Hovering over a fiducial is no longer PointingHandCursor

**Topic ID**: 4364
**Date**: 2018-10-11
**URL**: https://discourse.slicer.org/t/hovering-over-a-fiducial-is-no-longer-pointinghandcursor/4364

---

## Post #1 by @jamesobutler (2018-10-11 17:50 UTC)

<p>Using the current Slicer nightly 4.9.0-2018-10-09 when hovering over a placed fiducial it no longer shows the Qt <a href="http://doc.qt.io/archives/qt-4.8/qt.html#CursorShape-enum" rel="nofollow noopener">PointingHandCursor</a> type. It maintains the regular arrow cursor type.</p>
<p>In Slicer 4.8.1 it would use the PointingHandCursor.  Is this change to be expected or is this a bug? Does this happen for anyone else? I’m on the latest Windows 10 public release.</p>
<p>I discovered this while using fiducial markups in the latest slicer. Other issues I ran into using fiducials I added to the issue tracker.<br>
<a href="https://issues.slicer.org/view.php?id=4628" rel="nofollow noopener">0004627: VTK Errors after pasting copied fiducial in markups module</a><br>
<a href="https://issues.slicer.org/view.php?id=4627" rel="nofollow noopener">0004628: Unable to move fiducial position with cursor</a></p>

---

## Post #2 by @lassoan (2018-10-11 18:13 UTC)

<p>It is like this since the switch to Qt5/OpenGL2 rendering backend. It is like this in other applications, such as ParaView.</p>
<p>We can switch cursor using <code>QWidget::setCursor()</code> but VTK methods do not seem to work anymore.</p>

---

## Post #3 by @pieper (2018-10-11 18:16 UTC)

<p>Thanks for reporting this - I hadn’t use fiducials lately but indeed they are all screwed up.</p>
<p>Do you happen to know when this broke?  I have a mac nightly from 2018-08-28 that is not broken.</p>

---

## Post #4 by @pieper (2018-10-11 18:17 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> it’s not just the cursor changing, the fiducials are completely non-functional.</p>

---

## Post #5 by @jamesobutler (2018-10-11 18:20 UTC)

<p>Ok, I figured it was due to one of the major updates Qt5/VTK9/etc. I think PointingHandCursor is a bit helpful to know if you can grab an object.  This specific thing isn’t a big deal, but I think changing the cursor could help some with usability.</p>

---

## Post #6 by @jamesobutler (2018-10-11 18:26 UTC)

<p>Regarding issue 4628 of not being able to move a placed fiducial with cursor, I only have a Windows nightly package from 2018-08-17 and it wasn’t an issue there.  Not sure when it started to happen either.  I attempted to post that as a note to the issue tracker, but it prevented me from posting thinking I was spam for so many actions within a certain time period <img src="https://emoji.discourse-cdn.com/twitter/laughing.png?v=6" title=":laughing:" class="emoji" alt=":laughing:"></p>

---
