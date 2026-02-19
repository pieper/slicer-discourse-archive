---
topic_id: 16204
title: "Change Handle Property Of Markups Node Like Implant"
date: 2021-02-25
url: https://discourse.slicer.org/t/16204
---

# Change handle property of markups node like implant

**Topic ID**: 16204
**Date**: 2021-02-25
**URL**: https://discourse.slicer.org/t/change-handle-property-of-markups-node-like-implant/16204

---

## Post #1 by @forfullstack (2021-02-25 08:07 UTC)

<p>I’m trying to change property(color and opacity) of implant handle. Because when we move implant in the 2d slice view, it’s difficult to look implant itself because it’s overlapped by handle. If I hide handle, I can’t move/rotate implant icon also.<br>
I know when create implant it creates ModelDisplay named Implant and MarkupsFiducialDisplay named ImplantPlacer.<br>
But I didn’t get point where is decided handle color like red, green, blue and orange of center. Only I did is setting of glyph scale.<br>
I’ll be appreciated any advise.<br>
Thanks<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf8b3525b7df1c1414d13a2adeb99efe7e02af13.png" alt="image" data-base62-sha1="tC15pBdB7MzFushOTQTeEDeeeST" width="177" height="162"></p>

---

## Post #2 by @lassoan (2021-02-25 19:07 UTC)

<p>Change the glyph size in display settings should allow you to reduce the handle size so that it does not occlude important details.</p>
<p>But there could be of course additional setting to make the handles appear less strongly. Allow users to adjust transparency would be probably easy to implement. Render the handles with a thin opaque outline and semitransparent filling could help, too (and could improve overall aesthetics). <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> do you have any other ideas?</p>
<p>Can you attach a few screenshots that show how the handles interfere with visualization of underlying content?</p>
<p>We are working on improving the new markups ROI widget, so most likely we’ll have to get back to this later. If you want to make sure that customization of handles will be added to the roadmap, submit a feature request at <a href="http://issues.slicer.org">issues.slicer.org</a>.</p>

---
