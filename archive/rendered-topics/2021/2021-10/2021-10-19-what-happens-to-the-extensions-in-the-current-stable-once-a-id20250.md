# What happens to the extensions in the current stable once a new one is released?

**Topic ID**: 20250
**Date**: 2021-10-19
**URL**: https://discourse.slicer.org/t/what-happens-to-the-extensions-in-the-current-stable-once-a-new-one-is-released/20250

---

## Post #1 by @muratmaga (2021-10-19 19:56 UTC)

<p>Assuming there will soon be a new stable release of Slicer, we need to understand what happens to the previous (current) stable and its extensions?</p>
<p>My understanding is that the extensions for r29738 (current stable) will be frozen at whether the latest built extensions were for it at the time (as opposed to rebuilding it with new changes to the extension). Is that correct?</p>
<p>The reason I am asking, at this point we have to do a lot of slicer version checks to make sure SlicerMorph works correctly with the current stable and the preview due to major changes to Markups, subject hierarchy and other module. When the new release comes, we would like to remove these, and get rid off the code to support 4.11, as long as r29738 continues to function with its own last SlicerMorph build.</p>

---

## Post #2 by @jcfr (2021-10-19 20:44 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="1" data-topic="20250">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>My understanding is that the extensions for r29738 (current stable) will be frozen at whether the latest built extensions were for it at the time (as opposed to rebuilding it with new changes to the extension). Is that correct?</p>
</blockquote>
</aside>
<p>Your understanding is correct.</p>

---

## Post #3 by @jmhuie (2021-10-20 01:27 UTC)

<p>Will we need to resubmit a new pull request to add extensions to the new stable release or will they automatically be pulled from the preview release GitHub repository?</p>

---

## Post #4 by @jamesobutler (2021-10-20 02:46 UTC)

<p>A new branch is made off of the latest <code>master</code> branch of the ExtensionsIndex where effectively the specification for Slicer Preview and Slicer Stable are the same at this time of branching. <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/ReleaseProcess#Update_ExtensionsIndex" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/Developers/ReleaseProcess - Slicer Wiki</a></p>
<p>Developers will have to submit PRs to this new branch potentially if the Slicer preview becomes incompatible with the new Slicer stable requiring the extension to maintain a separate branch. For example some extensions have a <code>4.11</code> branch that is compatible with the 4.11 stable, but the <code>master</code> branch is compatible with the Slicer Preview.</p>

---
