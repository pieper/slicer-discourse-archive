# Nightly Doxygen out of date

**Topic ID**: 10428
**Date**: 2020-02-25
**URL**: https://discourse.slicer.org/t/nightly-doxygen-out-of-date/10428

---

## Post #1 by @Sunderlandkyl (2020-02-25 17:01 UTC)

<p>The current nightly Doxygen doesn’t show the latest version of the API (Last updated January 30th).</p>
<p>How often is the documentation updated?</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a></p>

---

## Post #2 by @Sam_Horvath (2020-02-25 19:28 UTC)

<p>Looking into this.  It should be rebuilt with each commit to master</p>

---

## Post #3 by @Sam_Horvath (2020-02-25 19:31 UTC)

<p>This is the repo that controls/ holds the api docs: <a href="https://github.com/Slicer/apidocs.slicer.org" rel="nofollow noopener">https://github.com/Slicer/apidocs.slicer.org</a></p>
<p>It should be rebuilding triggered by CircleCI</p>

---
