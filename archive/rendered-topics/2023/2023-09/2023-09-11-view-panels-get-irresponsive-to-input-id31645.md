---
topic_id: 31645
title: "View Panels Get Irresponsive To Input"
date: 2023-09-11
url: https://discourse.slicer.org/t/31645
---

# View Panels get irresponsive to input

**Topic ID**: 31645
**Date**: 2023-09-11
**URL**: https://discourse.slicer.org/t/view-panels-get-irresponsive-to-input/31645

---

## Post #1 by @HOAreg (2023-09-11 17:43 UTC)

<p>Hi!</p>
<p>First of all thanks for all who helped to create this wonderful software, really outstanding project!</p>
<p>I frequently have a “freeze” of one or several of the view panels, which means that no mouse input is working in them any more. Happens after any refresh of the panel content (like rotation, MPR, selection of content etc). The software itself is fully functional, but I found no option to make the frozen panel responsive again (tried changing panel layout, resizing the window, other content/CT series in the panel etc). Only solution that I found is to save everything and restart Slicer.</p>
<p>Experienced that behavior on a Mac book 2017 and current MacPro M2 max. Not sure if relevant, but am mostly working with external Monitor and Mouse (problem persists if external monitor is disconnected and the resolution is reset to the native display resolution).</p>
<p>Wonder if this is a known issue? Does anybody have an idea how get the frozen panels responsive without restarting Slicer?</p>
<p>Thanks for all input!</p>

---

## Post #2 by @pieper (2023-09-11 22:07 UTC)

<p>I use various versions of Slicer on a Mac Pro 2019 with external monitor and on a mac air M2 and don’t recall any issues with viewers freezing.  I do have the popup menus show up in the wrong place sometimes.</p>
<p>If you can, please describe the workflow that leads to this issue, and also check the python consoles and log files when the freeze happens and send along any info you find.  It could be that a tool or widget is grabbing the input but not releasing it due to an error condition and it would help to know which one.</p>

---

## Post #3 by @HOAreg (2023-09-18 09:50 UTC)

<p>Hi!</p>
<p>Thanks for your feedback. The workflow is variable, happens mostly while segmenting in CTs.<br>
Just had it happen while using the standard segmentation tools (Paint, Scissors etc) without leaving Segment Editor since rebooting.</p>
<p>I found one message that is potentially helpful in the Python console:</p>
<p>[Qt] Window position QRect(-37,287 84x15) outside any known screen, using primary screen</p>
<p>Is this helpful to get an idea what happens?<br>
Where do  I find the log files?</p>
<p>I think it is due to a strange definition of where the panels of the views are, is this correct?<br>
Can I somehow force to recalculate that to overcome the freeze/irresponsiveness of one of the panels?</p>
<p>Thanks for all help,<br>
Andreas</p>

---

## Post #4 by @jamesobutler (2023-09-18 12:16 UTC)

<aside class="quote no-group" data-username="HOAreg" data-post="3" data-topic="31645">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hoareg/48/67493_2.png" class="avatar"> HOAreg:</div>
<blockquote>
<p>Just had it happen while using the standard segmentation tools (Paint, Scissors etc) without leaving Segment Editor since rebooting.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/hoareg">@HOAreg</a> does this happen to include the “Draw” tool as well?</p>
<p>I have had slice views become unresponsive if I am using the draw tool, unknowingly place a point of the draw effect in a slice view and then change the slice offset. It becomes unresponsive to place new draw points because its does not allow points to be drawn on different slice offsets.</p>
<p>When it happens again can you try clearing the scene and reloading your data? This will be differently then closing Slicer and reopening.</p>

---

## Post #5 by @HOAreg (2024-10-04 06:52 UTC)

<p>Hello,</p>
<p>Closing Scene is not helpful, issue remains also when different scene than the crashed one is loaded. I noticed that it get unfreezes when it happens in one of the by changing Window Width/Level in the three regular panels. Didn’t find any trick to unfreeze in the 3d panel.</p>
<p>Very strange behavior. Would be very nice to get any input!</p>

---

## Post #6 by @HOAreg (2024-10-04 06:58 UTC)

<p>Solution: That was too easy. Just reconnect the monitor from the Mabook, change anything in the view panel like zooming in/out and reconnect. Gets responsive by this way. Not a satisfying clean way but still better than restarting Slicer all 10 mins…</p>

---

## Post #7 by @HOAreg (2024-10-04 06:59 UTC)

<p>PS: if anyone is still interested in this issue I can add that it is also happening when using a 2023 14" MBP on the Thunderbolt Display</p>

---
