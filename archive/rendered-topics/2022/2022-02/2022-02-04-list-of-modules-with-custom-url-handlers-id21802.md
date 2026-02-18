# List of modules with custom URL handlers

**Topic ID**: 21802
**Date**: 2022-02-04
**URL**: https://discourse.slicer.org/t/list-of-modules-with-custom-url-handlers/21802

---

## Post #1 by @swirlsky (2022-02-04 14:15 UTC)

<p>Based on <a href="https://discourse.slicer.org/t/is-there-an-api-for-rpc/21734/6">this thread</a> I managed to invoke Slicer from Brave browser on Ubuntu and fetch a DICOM study from Orthanc using the <code>slicer://viewer/?studyUID=...</code> custom URL.</p>
<p>My question is, if these custom URL handlers of modules are documented somewhere. I’m no Python guy, I just searched for <code>QUrl</code> and <code>QUrlQuery</code> in Slicer’s repo on github, and couldn’t find any more modules with this custom URL listener functionality besides <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#launch-slicer-directly-from-a-web-browser" rel="noopener nofollow ugc">those two mentioned in the docs</a>.</p>
<p>Also in the docs:</p>
<blockquote>
<p>any module can specify additional actions</p>
</blockquote>
<p>A list of these actions would be useful, if there are any more actions supported by other modules. Are there?</p>

---

## Post #2 by @pieper (2022-02-04 18:10 UTC)

<aside class="quote no-group" data-username="swirlsky" data-post="1" data-topic="21802">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/ecc23a/48.png" class="avatar"> swirlsky:</div>
<blockquote>
<p>My question is, if these custom URL handlers of modules are documented somewhere.</p>
</blockquote>
</aside>
<p>I’m pretty sure there’s only what you linked so far.  If you want to add more it would make sense to add them to the docs the same way.</p>

---
