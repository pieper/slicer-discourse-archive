---
topic_id: 8721
title: "Build Machine Failing When Local Clean Build Doesnt"
date: 2019-10-09
url: https://discourse.slicer.org/t/8721
---

# Build machine failing when local clean build doesn't

**Topic ID**: 8721
**Date**: 2019-10-09
**URL**: https://discourse.slicer.org/t/build-machine-failing-when-local-clean-build-doesnt/8721

---

## Post #1 by @adamrankin (2019-10-09 14:18 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a></p>
<p><a href="http://slicer.cdash.org/viewBuildError.php?buildid=1716023" class="onebox" target="_blank" rel="nofollow noopener">http://slicer.cdash.org/viewBuildError.php?buildid=1716023</a></p>
<p>I did a clean build of Slicer and SlicerOpenCV yesterday and it passed, but the build machine is failing. How can I go about diagnosing?</p>

---

## Post #2 by @adamrankin (2019-10-09 18:01 UTC)

<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> any chance either of you or JC would be able to help me diagnose?</p>

---

## Post #3 by @Sam_Horvath (2019-10-09 19:10 UTC)

<p>I’ll have some time to look at it tomorrow.</p>

---

## Post #4 by @Sam_Horvath (2019-10-10 00:47 UTC)

<p>A thought on debugging:</p>
<p>To test the extension, are you building it standalone, or from the ExtensionsIndex framework? (may have different behavior)</p>
<p>See:  <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_ExtensionsIndex" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_ExtensionsIndex</a></p>

---

## Post #5 by @adamrankin (2019-10-10 13:38 UTC)

<p>I was doing standalone, I’ll give EI build a try</p>

---
