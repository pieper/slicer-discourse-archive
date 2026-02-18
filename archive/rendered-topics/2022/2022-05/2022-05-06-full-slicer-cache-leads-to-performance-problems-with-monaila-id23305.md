# Full slicer cache leads to performance problems with MONAILabel

**Topic ID**: 23305
**Date**: 2022-05-06
**URL**: https://discourse.slicer.org/t/full-slicer-cache-leads-to-performance-problems-with-monailabel/23305

---

## Post #1 by @jlvahldiek (2022-05-06 12:47 UTC)

<p>We use 3D slicer with MONAILabel to create large data sets. After a certain time the slicer cache fills up. When the upper limit of the cache is reached, loading images via MONAILabel’s ‘Next Sample’ takes a very long time. As soon as the cache is manually cleared again, the performance of Slicer/MONAILabel is back to normal.</p>
<p>I have observed this behavior on various Windows workstations but also on a MacOS workstation. Actually, I would have expected an automatic clearing of the cache. I am not sure if this is a Slicer or a MONAILabel problem.</p>
<p>Is this a known issue? Or is there a corresponding setting option?</p>

---

## Post #2 by @pieper (2022-05-06 13:54 UTC)

<p>Thanks for reporting this.  To help nail down the issue, you could try running the Activity Monitor on the mac and selecting Slicer and then using the Sample Process option to see where time is being spent during the slowdown.</p>

---

## Post #3 by @muratmaga (2022-05-06 16:12 UTC)

<aside class="quote no-group" data-username="jlvahldiek" data-post="1" data-topic="23305">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jlvahldiek/48/13507_2.png" class="avatar"> jlvahldiek:</div>
<blockquote>
<p>Or is there a corresponding setting option?</p>
</blockquote>
</aside>
<p>I think you can change the location of cache and increase its size (I believe default is only 200MB) from Application Settings.</p>

---

## Post #4 by @jlvahldiek (2022-05-09 08:07 UTC)

<p>Thank you for your quick answers. I just installed the latest Slicer Preview version and did some tests for both Windows and Mac. The problem seems to be gone with the latest version. I still had a preview version from early December installed on the workstations affected by the problem…</p>

---

## Post #5 by @jlvahldiek (2022-05-09 08:11 UTC)

<p>Is there some automagic for when the slicer cache gets cleared or do you rely on system cleanups?</p>

---

## Post #6 by @pieper (2022-05-09 13:14 UTC)

<p>You shouldn’t need to think about the cache under normal circumstances.  If it becomes an issue again please report with any details you have about what might have caused the issue.</p>

---
