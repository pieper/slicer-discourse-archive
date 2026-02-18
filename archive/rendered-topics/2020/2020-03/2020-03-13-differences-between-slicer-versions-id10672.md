# Differences between Slicer Versions

**Topic ID**: 10672
**Date**: 2020-03-13
**URL**: https://discourse.slicer.org/t/differences-between-slicer-versions/10672

---

## Post #1 by @siaeleni (2020-03-13 15:16 UTC)

<p>Hi,<br>
I am trying to run the same ICP algorithm “vtkIterativeClosestPointTransform” and it seems that I get different results with exactly the same data and algorithm between “4.11.0-2020-03-10” and “4.11.0-2019-06-12” versions. Is there any stable 4.11 version to use? When are you going to release a stable 4.11 version?</p>
<p>Thanks</p>

---

## Post #2 by @pieper (2020-03-13 16:11 UTC)

<p>Hi <a class="mention" href="/u/siaeleni">@siaeleni</a> -</p>
<p>Is it related to <a href="https://discourse.slicer.org/t/model-files-are-now-saved-in-lps-coordinate-system/10446">the change from LPS to RAS</a>?  If not, then it could be related to the version of VTK.  If so the best thing might be to create a short python script to reproduce the issue with sample data to post on the VTK github.</p>
<p>Regarding the release, it’ll be called Slicer5, and it’s being tracked here:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Labs/Slicer5-roadmap" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Labs/Slicer5-roadmap</a></p>
<p>It’s a major effort that doesn’t currently have dedicated funding so people are doing it as a kind of side project with no firm release date.  Hopefully soon.</p>

---

## Post #3 by @siaeleni (2020-03-13 16:40 UTC)

<p>Thanks Steve!<br>
It is related to the change from LPS to RAS.</p>

---

## Post #4 by @lassoan (2020-03-13 17:10 UTC)

<aside class="quote no-group" data-username="siaeleni" data-post="1" data-topic="10672">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/b4bc9f/48.png" class="avatar"> siaeleni:</div>
<blockquote>
<p>Is there any stable 4.11 version to use?</p>
</blockquote>
</aside>
<p>I would consider current 4.11 version as stable. List of issues that we plan to address before releasing it as a new stable version is available <a href="https://github.com/Slicer/Slicer/milestone/1">here</a>. I don’t think there are any serious open issues.</p>

---

## Post #5 by @lassoan (2020-03-13 17:18 UTC)

<aside class="quote no-group" data-username="siaeleni" data-post="1" data-topic="10672">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/b4bc9f/48.png" class="avatar"> siaeleni:</div>
<blockquote>
<p>Is there any stable 4.11 version to use?</p>
</blockquote>
</aside>
<p>I would consider current 4.11 version is stable. List of issues that we plan to address before releasing it as a new stable version is available <a href="https://github.com/Slicer/Slicer/milestone/1">here</a>.</p>

---

## Post #6 by @pieper (2020-03-13 17:55 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="10672">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>List of issues that we plan to address before releasing it as a new stable version is available <a href="https://github.com/Slicer/Slicer/milestone/1">here</a>.</p>
</blockquote>
</aside>
<p>By the way, the content of these issues is still being migrated - should be up later today.</p>

---
