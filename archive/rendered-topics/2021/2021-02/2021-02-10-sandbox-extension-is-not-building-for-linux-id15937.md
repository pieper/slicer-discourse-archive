# Sandbox extension is not building for linux

**Topic ID**: 15937
**Date**: 2021-02-10
**URL**: https://discourse.slicer.org/t/sandbox-extension-is-not-building-for-linux/15937

---

## Post #1 by @muratmaga (2021-02-10 16:40 UTC)

<p><a href="http://slicer.cdash.org/viewBuildError.php?buildid=2147110" class="onebox" target="_blank" rel="noopener nofollow ugc">http://slicer.cdash.org/viewBuildError.php?buildid=2147110</a><br>
<a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #2 by @lassoan (2021-02-10 17:16 UTC)

<p>Thanks for reporting. It is due to the new mesh Boolean operations module (Combine models) that we are experimenting with. I’ve pushed a <a href="https://github.com/PerkLab/SlicerSandbox/commit/666f6ebad48cd6b3446d3582fcc531c70e56df71">fix</a> now that solved the issue for others. It would be nice if you could check if it fixes the build for you, but if you don’t have time then we’ll see on the dashboard tomorrow.</p>

---

## Post #3 by @muratmaga (2021-02-10 17:56 UTC)

<p>Np. Will try tomorrow.</p>
<p>We showcase the Lights, CPR and a cross-sectional area modules in our workshops as useful tools, and trying to make sure there is a recent Linux build with segment visibility bug fixed with the Sandbox extension included.</p>

---
