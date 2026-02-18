# Efficiently removing osteoderms?

**Topic ID**: 17666
**Date**: 2021-05-18
**URL**: https://discourse.slicer.org/t/efficiently-removing-osteoderms/17666

---

## Post #1 by @Isaac.Annal (2021-05-18 00:09 UTC)

<p>Hi all,</p>
<p>I have been segmenting skink skulls (first in Avizo and now primarily through slicer) and it is terribly tedious due to their osteoderms. When thresholding, the osteoderms show up in the same grayscale range as the bones I would like to select. Additionally, the osteoderms fuse to the skull bones. I usually have to go slide by slide until I have completed the skull. I have been trying to find a way to efficiently remove these on a mass scale, although I somewhat doubt that one exists. The most efficient way I have found so far is the grow from seeds function. This still requires a lot of manual cleaning on slides that bone and osteoderm are in close proximity, which seems to be the majority of the skull. Has anyone dealt with osteoderms (in skinks or other groups) and found an efficient way to remove them? I will explore any and all suggestions!!</p>
<p>thank you,</p>
<p>Isaac</p>

---

## Post #2 by @muratmaga (2021-05-18 00:59 UTC)

<p>I suspect anybody on the forum worked specifically on the skink skulls or osteoderms, but they may have encountered similar challenges in different contexts. If you can share your data, or at least provide some screenshots of your challenges that will be great.</p>
<p>In general if tissues are continuous in nature, and there is no intensity difference, it can be challenging. I would have suggested grow from the seeds but it looks like that’s what you are already doing.</p>

---
