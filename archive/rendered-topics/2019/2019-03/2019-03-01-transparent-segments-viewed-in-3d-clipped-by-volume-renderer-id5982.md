---
topic_id: 5982
title: "Transparent Segments Viewed In 3D Clipped By Volume Renderer"
date: 2019-03-01
url: https://discourse.slicer.org/t/5982
---

# Transparent segments viewed in 3D clipped by volume renderer?

**Topic ID**: 5982
**Date**: 2019-03-01
**URL**: https://discourse.slicer.org/t/transparent-segments-viewed-in-3d-clipped-by-volume-renderer/5982

---

## Post #1 by @hherhold (2019-03-01 13:04 UTC)

<p>Can transparent segments be viewed in 3D along with the volume renderer? I searched through similar topics but didn’t find anything exactly like this.</p>
<p>Quick list of steps:</p>
<ol>
<li>Make a segment</li>
<li>Enable viewing in 3D</li>
<li>Turn on volume rendering</li>
<li>Crop volume in volume rendering so segment “sticks out”</li>
<li>Change segment opacity to something other than 1.0</li>
<li>Segment disappears, except where volume is not in background - if you rotate around, segment becomes visible.</li>
</ol>
<p>This is on the latest nightly (Feb 28), on both Mac and PC, and I have depth peeling enabled.</p>
<p>Any ideas? Thanks!!</p>
<p>-Hollister</p>

---

## Post #2 by @lassoan (2019-03-01 15:05 UTC)

<p>For me it works as you describe (segment disappears) if depth peeling is disabled but works perfectly if depth peeling is enabled.</p>
<p>Could you show a screen capture video of what you do?</p>

---

## Post #3 by @hherhold (2019-03-01 16:42 UTC)

<p>Hmm. I just re-did my scene from scratch after turning on depth peeling and it works properly (with transparency). Is depth peeling a setting in the scene’s MRML file, and it’s not properly set in my original (not working) file?</p>
<p>Thanks for the help!</p>
<p>-Hollister</p>

---

## Post #4 by @lassoan (2019-03-13 23:42 UTC)

<p>Yes, UseDepthPeeling flag is saved in the scene. It might be possible that if you enable it later then not everything is initialized correctly.</p>

---

## Post #5 by @hherhold (2019-03-14 10:51 UTC)

<p>Thanks, Andras.</p>
<p>Not to nit-pick, but that’s a little confusing - setting depth peeling is in “Application Settings”, which I would take to mean application-wide, not per-file. Would it make more sense to move depth peeling to Volume Rendering or Segment Editor?</p>
<p>I guess the problem is that it’s an application setting, not a module setting, so there isn’t one good place to put it. Maybe a note by the depth peeling check box saying the setting is saved in scene files? (I’m happy to add that if agreed upon.)</p>

---

## Post #6 by @lassoan (2019-03-14 16:03 UTC)

<p>You can set <strong>default</strong> view settings in application settings, which is applied to new views.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f185bde58392ae1e8f695b7af213529ea5d8ba52.png" alt="image" data-base62-sha1="ysBBS1j6R4NkOQvdWiAgsiU1cJ4" width="651" height="332"></p>
<p>You can change the current settings in the view controller.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74a298bcba2e25616b5f7bddfaadc4a40e1078fc.png" alt="image" data-base62-sha1="gDNKofF7E8AruYpPTH5u5VJxPOI" width="504" height="232"></p>

---

## Post #7 by @hherhold (2019-03-14 16:41 UTC)

<p>Got it, ok - that makes sense.</p>
<p>“Problem between chair and keyboard”, as they say.</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #8 by @lassoan (2021-01-27 21:13 UTC)

<p>A post was split to a new topic: <a href="/t/separate-vessels-from-bones/15703">Separate vessels from bones</a></p>

---
