# Sandbox extension needed for mandible reconstruction extension and it is not available

**Topic ID**: 20413
**Date**: 2021-10-29
**URL**: https://discourse.slicer.org/t/sandbox-extension-needed-for-mandible-reconstruction-extension-and-it-is-not-available/20413

---

## Post #1 by @mau_igna_06 (2021-10-29 13:29 UTC)

<p>Hi. Users are telling me that they cannot finish surgical planning because they cannot make boolean operations because the CombineModels module is not found, because the extension manager cannot install Sandbox extension because it is not available (it is one of the dependencies of BoneReconstructionPlanner)</p>
<p>If you search ‘Sandbox’ in the extension manager in the Stable release it doesn’t find it. If you search ‘Sandbox’ in the extension manager in the Preview release it finds it but the new webpage does not load, it just freezes.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/jcfr">@jcfr</a>, <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> could you help?<br>
Is there any chance the CombineModels module gets to be part of Slicer Core?</p>

---

## Post #2 by @jamesobutler (2021-10-29 14:03 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="1" data-topic="20413">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>If you search ‘Sandbox’ in the extension manager in the Stable release it doesn’t find it.</p>
</blockquote>
</aside>
<p>From today’s Slicer stable <a href="https://slicer.cdash.org/viewBuildError.php?buildid=2456111" rel="noopener nofollow ugc">build results of SlicerSandbox</a> it appears CombineModels is breaking the build likely because it was made compatible with VTK9 and Slicer stable 4.11.20210226 is using VTK8. It’s unclear as a “SandBox” extension if compatibility with latest stable is attempted, or only with latest Preview code.</p>
<aside class="quote no-group" data-username="mau_igna_06" data-post="1" data-topic="20413">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>If you search ‘Sandbox’ in the extension manager in the Preview release it finds it but the new webpage does not load</p>
</blockquote>
</aside>
<p>Yeah that is weird and I see it too. The link is below and the page doesn’t load the correct contents. I haven’t found yet another extension page that has this issue. Clicking the install button from Extensions Manager search results does work for it, but you can’t view the webpage for the extension.</p>
<p><a href="https://extensions.slicer.org/view/Sandbox/30338/win" class="onebox" target="_blank" rel="noopener nofollow ugc">https://extensions.slicer.org/view/Sandbox/30338/win</a></p>

---

## Post #3 by @lassoan (2021-10-29 15:46 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="20413">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>From today’s Slicer stable <a href="https://slicer.cdash.org/viewBuildError.php?buildid=2456111">build results of SlicerSandbox</a> it appears CombineModels is breaking the build likely because it was made compatible with VTK9 and Slicer stable 4.11.20210226 is using VTK8.</p>
</blockquote>
</aside>
<p>I haven’t thought of making Combine Models module compatible with VTK8. <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> has Combine Models ever worked in Slicer-4.11? If not, then we should just disable the Combine Models module for Slicer-4.11 (I don’t think anybody would want to spend time with debugging VTK8-related build errors on Windows, Linux, and Mac).</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="20413">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Yeah that is weird and I see it too. The link is below and the page doesn’t load the correct contents.</p>
</blockquote>
</aside>
<p>It seems that extensions that do not have screenshot URLs do not get a page. I’ve submitted an issue for this: <a href="https://github.com/Slicer/Slicer/issues/5973" class="inline-onebox">Extension page is empty if EXTENSION_SCREENSHOTURLS is empty in CMakeLists.txt · Issue #5973 · Slicer/Slicer · GitHub</a></p>
<p>I never click on the extension’s page because that <a href="https://github.com/Slicer/Slicer/issues/5863">install button there does not work</a>. You can click on the install button directly on the extension listing instead.</p>

---

## Post #4 by @mau_igna_06 (2021-10-29 17:43 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="20413">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I haven’t thought of making Combine Models module compatible with VTK8. <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> has Combine Models ever worked in Slicer-4.11?</p>
</blockquote>
</aside>
<p>Yes. It worked. But I could advice the users to use the preview release.</p>

---

## Post #5 by @mau_igna_06 (2021-10-29 22:16 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I could revert the combineModels changes in a new branch and change the extensios index file of the stable release to point to that branch. What do you think?</p>

---

## Post #6 by @lassoan (2021-10-29 22:18 UTC)

<p>Yes, you can create a 4.11 branch for the Sandbox extension and make changes that fix the VTK8 build errors. However, considering that we hope to replace Slicer-4.11 in a couple of weeks, I’m not sure if it is worth the effort.</p>

---
