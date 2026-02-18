# Extension Catalogue search improvements

**Topic ID**: 42046
**Date**: 2025-03-10
**URL**: https://discourse.slicer.org/t/extension-catalogue-search-improvements/42046

---

## Post #1 by @muratmaga (2025-03-10 02:44 UTC)

<p>During the discussions of a new extension, it become clear that extension catalogue naming conventions are too restrictive. For example, an extension name cannot have spaces, since the label name is also used for project name.</p>
<p>Search in the extension catalogue also doesn’t search for the project descriptions. More detailed discussion can be found here: <a href="https://github.com/Slicer/ExtensionsIndex/pull/2146#issuecomment-2704556749" class="inline-onebox" rel="noopener nofollow ugc">ENH: add SlicerDeCA extension by smrolfe · Pull Request #2146 · Slicer/ExtensionsIndex · GitHub</a></p>
<p>I also think that if we do NOT want extensions to have Slicer in their extension name, we should stop requiring repos to have Slicer prefix. It perhaps makes sense for existing tools (e.g., ANTs, MONAI) that are ported to Slicer (so it becomes SlicerANTs, SlicerMONAI), but otherwise it is awkward for the project name and the repo not to be the same for extension specifically developer for Slicer.</p>
<p>This is meant to start a discussion of what I perceive shortcomings of the current extension naming requirements.</p>

---

## Post #2 by @jamesobutler (2025-03-10 05:51 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="1" data-topic="42046">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>but otherwise it is awkward for the project name and the repo not to be the same</p>
</blockquote>
</aside>
<p>It currently serves different search functionality as the CMakeLists.txt project name is the extension name that users will be searching with within Slicer. The GitHub repository name is for searchability within GitHub to find Slicer associated repositories. That is in addition to the <code>3d-slicer-extension</code> GitHub topic which is to be used as mentioned in the checklist for submitting a new Slicer extension.</p>
<p>Luckily the Slicer <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/extensionwizard.html" rel="noopener nofollow ugc">Extension Wizard</a> can set up all these naming schemes appropriately. If it is not currently doing this, we could update that code to fix any issues.</p>

---
