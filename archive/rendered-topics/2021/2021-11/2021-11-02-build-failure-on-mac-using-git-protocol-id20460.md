# Build failure on Mac using git:// protocol

**Topic ID**: 20460
**Date**: 2021-11-02
**URL**: https://discourse.slicer.org/t/build-failure-on-mac-using-git-protocol/20460

---

## Post #1 by @hherhold (2021-11-02 13:55 UTC)

<p>I haven’t built from scratch (clean) in a while, so apologies if this was mentioned elsewhere (didn’t see it in a quick search).</p>
<p>It looks like as of Nov 2, the “brownout” of the <code>git://</code> protocol is beginning. Cloning of DCMTK using this protocol during the build fails, but the solution is just to un-check <code>Slicer_USE_GIT_PROTOCOL</code> in CMake. Should this be the default now, as <code>git://</code> protocol is truly going away?</p>

---

## Post #2 by @RafaelPalomar (2021-11-02 13:59 UTC)

<p>There are ongoing discussions on this:</p>
<ul>
<li><a href="https://github.com/Slicer/Slicer/pull/5980" class="inline-onebox" rel="noopener nofollow ugc">COMP: Disabling git protocol by default by RafaelPalomar · Pull Request #5980 · Slicer/Slicer · GitHub</a></li>
<li><a href="https://discourse.slicer.org/t/2021-11-02-weekly-meeting/20436" class="inline-onebox">2021.11.02 Weekly Meeting</a></li>
</ul>
<p>I’m currently testing if configuring with <code>Slicer_USE_GIT_PROTOCOL=OFF</code> is a workaround for a complete build while this is sorted out. I’ll post  my findings here</p>

---

## Post #3 by @hherhold (2021-11-02 14:04 UTC)

<p>Got it, thanks - sorry for the extra post/noise. I’m building now, I can also post success/failure here if you’re interested.</p>

---

## Post #4 by @jcfr (2021-11-02 17:29 UTC)

<p>3 posts were split to a new topic: <a href="/t/macos-build-error-unknown-architecture-associated-with-dynamicmodeler-logic-fastmarching/20463">macOS build #error “Unknown architecture !” associated with DynamicModeler/Logic/FastMarching</a></p>

---

## Post #5 by @RafaelPalomar (2021-11-02 18:52 UTC)

<p>Just wanted to confirm that setting <code>Slicer_USE_GIT_PROTOCOL=OFF</code> is a valid workaround for this problem. We are working on a permanent solution in <a href="https://github.com/Slicer/Slicer/pull/5980" class="inline-onebox" rel="noopener nofollow ugc">COMP: Disabling git protocol by default by RafaelPalomar · Pull Request #5980 · Slicer/Slicer · GitHub</a></p>

---

## Post #6 by @hherhold (2021-11-02 18:54 UTC)

<p>Yes - I was able to build. <a class="mention" href="/u/jcfr">@jcfr</a> committed a fix for the unknown architecture problem; setting <code>Slicer_USE_GIT_PROTOCOL=OFF</code> fixed the git protocol issue with DCMTK (and possibly other packages using <code>git://</code> protocol.</p>
<p>Thanks!</p>

---
