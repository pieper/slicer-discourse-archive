# Extension not built by build system

**Topic ID**: 2462
**Date**: 2018-03-29
**URL**: https://discourse.slicer.org/t/extension-not-built-by-build-system/2462

---

## Post #1 by @adamrankin (2018-03-29 00:32 UTC)

<p>Hello,</p>
<p>I have confirmed that my (and several other) extensions are not built with the build system. I have set up my own build machine, and several extensions are not cloned, and my build log has entries for configuration (of all extensions in the extension index), but nothing for building/testing/etc. (of a few extensions). There is nothing in the build log explaining why they aren’t built (that I could find via search).</p>
<p>Opening up SlicerExtensions.sln and building the extension (via Project SlicerVASST-&gt;Build Only This Project) results in a successful build of the extension.<br>
<a href="http://slicer.cdash.org/buildSummary.php?buildid=1228388" class="onebox" target="_blank" rel="noopener nofollow ugc">http://slicer.cdash.org/buildSummary.php?buildid=1228388</a></p>
<p>I will continue investigating, but if anyone has any ideas, it would be much appreciated.</p>
<p>Cheers,<br>
Adam</p>

---

## Post #2 by @lassoan (2018-03-29 03:08 UTC)

<p>We experienced the same. Do the extensions that are not built depend on other extensions? Do the dependencies have failing tests? Jc said he fixed the problem of extensions not being built if extensions that it depends on have <em>test</em> failures; but there may be still similar problems.</p>

---

## Post #3 by @cpinter (2018-03-29 12:24 UTC)

<p>The problem Andras is referring to is still a problem, and I have commented this to every thread where it comes up.</p>
<p>This is the <a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=4&amp;showfilters=1&amp;filtercombine=or&amp;field1=label&amp;compare1=63&amp;value1=SlicerRT&amp;field2=label&amp;compare2=63&amp;value2=GelDosimetry&amp;field3=label&amp;compare3=63&amp;value3=FilmDosimetry&amp;field4=label&amp;compare4=63&amp;value4=SegmentRegistration">latest dashboard with filters</a> where it shows.</p>

---

## Post #4 by @adamrankin (2018-03-29 13:45 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> No test failures on dependencies on same platform (error on other platform).</p>
<p>Investigating.</p>

---
