---
topic_id: 6951
title: "Camera Linking Broken"
date: 2019-05-28
url: https://discourse.slicer.org/t/6951
---

# Camera linking broken

**Topic ID**: 6951
**Date**: 2019-05-28
**URL**: https://discourse.slicer.org/t/camera-linking-broken/6951

---

## Post #1 by @smrolfe (2019-05-28 18:54 UTC)

<p>I’m not able to get the dual 3D views to link correctly in the nightly version of Slicer. The link/unlink button links the zoom, but not rotation and translation.</p>
<p>I tested an older nightly from 4-17, and it was broken in this version also. Linking is working in Slicer 4.10.2.</p>

---

## Post #2 by @pieper (2019-05-29 19:24 UTC)

<p>Hi <a class="mention" href="/u/smrolfe">@smrolfe</a> -</p>
<p>I’ve been debugging this and hope to find a fix.  In the mean time I noticed that while the camera view linkage doesn’t happen on normal mouse interaction events, it does happen when you use the mouse wheel to scroll  in or out.  You could use this as a workaround if it helps while a better fix is in the works.</p>

---

## Post #3 by @pieper (2019-05-29 19:45 UTC)

<p>Proposed fix here: <a href="https://github.com/Slicer/Slicer/pull/1145" rel="nofollow noopener">https://github.com/Slicer/Slicer/pull/1145</a></p>

---

## Post #4 by @pieper (2019-05-29 21:33 UTC)

<p>It won’t fix all camera linking use cases, but I went ahead and committed the fix because I think it will address the SlicerMorph use case.  <a class="mention" href="/u/smrolfe">@smrolfe</a> can you try and let me know?</p>

---

## Post #5 by @smrolfe (2019-05-29 22:35 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a>, I’ll try this and report back.</p>

---

## Post #6 by @smrolfe (2019-05-30 16:45 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a>, this fix works perfectly for me, thanks!</p>

---

## Post #7 by @pieper (2019-05-30 17:06 UTC)

<p>That’s great <a class="mention" href="/u/smrolfe">@smrolfe</a> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p>Referring to <a class="mention" href="/u/lassoan">@lassoan</a>’s point in the pull request thread, I suspect there are still some issues loading/restoring scenes with linked 3D views, possibly because of some kind of race condition about when the observers are added.  Let’s keep our eyes open for any lingering issues.</p>

---

## Post #8 by @smrolfe (2019-05-30 17:48 UTC)

<p>Currently, linked views cannot be restored from an MRB scene file. I posted on this a while ago <a href="https://discourse.slicer.org/t/loading-mrb-file-breaks-linked-views/5951">here</a>.</p>
<p>This issue is related to the cameras loaded from the MRB scene file and I can manually fix it by deleting the extra cameras loaded with the scene file. Is there another use case where these cameras are needed?</p>

---

## Post #9 by @pieper (2019-05-30 18:14 UTC)

<p>Thanks for pointing out the other issue - sorry it fell through the cracks.  I haven’t looked lately, but in the past there were cases cameras were being created automatically as the scene is being read, and that could explain what we are seeing here.  Do you think that issue is in the critical path for SlicerMorph?</p>

---

## Post #10 by @smrolfe (2019-05-30 18:21 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a>. We were interested in using MRB files to package our sample data, but we found a work-around. So it’s not a priority for us now.</p>

---
