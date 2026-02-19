---
topic_id: 34386
title: "Addnewnodebyclass Basename Does Not Increment"
date: 2024-02-18
url: https://discourse.slicer.org/t/34386
---

# AddNewNodeByClass: basename does not increment

**Topic ID**: 34386
**Date**: 2024-02-18
**URL**: https://discourse.slicer.org/t/addnewnodebyclass-basename-does-not-increment/34386

---

## Post #1 by @chir.set (2024-02-18 21:16 UTC)

<p>Hi,</p>
<p>From my understanding, <em>AddNewNodeByClass</em> accepts a <em>basename</em> that would increment with a suffix on repeat calls. For example:</p>
<p><code>slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelNode", "M")</code></p>
<p>should yield model nodes with names M, M_1, M_2…</p>
<p>I could not observe this naming pattern.</p>
<p>I’m probably missing something here. Can someone point to the right usage for this expectation?</p>
<p>Thank you.</p>

---

## Post #2 by @jamesobutler (2024-02-18 21:32 UTC)

<p><code>AddNewNodeByClass</code> accepts a name that is set to the node, but sets it exactly as specified. If you’d like to generate a unique name then utilize <code>slicer.mrmlScene.GenerateUniqueName("…")</code> as part of the string you pass into <code>AddNewNodeByClass</code>. If any documentation is incorrect or unclear, then I’m sure improvements to the API documentation would be welcome.</p>

---

## Post #3 by @chir.set (2024-02-18 21:52 UTC)

<p>vtkMRMLScene.h has this note:</p>
<pre><code class="lang-auto">/// \note Instead of calling SetName() after creating the node, prefer
/// passing \a nodeBaseName, indeed the method AddNode() ensures that the
/// final node name is unique in the scene by appending a suffix if needed.
</code></pre>
<p>It may mean that the unique name is handled by ‘AddNode’, itself called by ‘AddNewNodeByClass’.</p>
<p>Anyway, it’s easy to use ‘GenerateUniqueName’.</p>
<p>Thank you.</p>

---

## Post #4 by @jamesobutler (2025-05-27 11:52 UTC)

<p>For future reference, there was an attempt made at the following that was ultimately abandoned.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/8434">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/8434" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/8434" target="_blank" rel="noopener nofollow ugc">BUG: Fix basename not incrementing for AddNewNodeByClass</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>jamesobutler:add-new-node-basename-increment</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2025-05-20" data-time="17:16:57" data-timezone="UTC">05:16PM - 20 May 25 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
            <img alt="" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
            jamesobutler
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 2 additions and 2 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/8434/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+2</span>
            <span class="removed">-2</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">As originally pointed out in https://discourse.slicer.org/t/addnewnodebyclass-ba<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/8434" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">sename-does-not-increment/34386.

This logic setting the name in `AddNewNodeByClass` has seemingly been the same since it was introduced in https://github.com/Slicer/Slicer/commit/31551523b242a03c0f8f5fa17999f0eb7b7cd360. This PR has been made under the assumption that the input argument of "nodeBaseName" means that the intention is for the specified name to serve as a base and increment to provide a unique name.

https://github.com/Slicer/Slicer/blob/673ddca536801eedfdc3287dbc6ab110c494382c/Libs/MRML/Core/vtkMRMLScene.h#L211-L214

It appears that developers have worked around this issue of the name not incrementing by calling `GenerateUniqueName` manually.
https://github.com/Slicer/Slicer/blob/673ddca536801eedfdc3287dbc6ab110c494382c/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L460-L464
https://github.com/Slicer/Slicer/blob/673ddca536801eedfdc3287dbc6ab110c494382c/Modules/Scripted/Endoscopy/Endoscopy.py#L878-L881

However in some places it is unclear if the specified `nodeBaseName` has instead been used as a `nodeName` with expectation that it would not increment and be used exactly as specified. If this is the desire then we could instead change the `AddNewNodeByClass` method to name the input argument `nodeName` instead of `nodeBaseName`.
https://github.com/Slicer/Slicer/blob/673ddca536801eedfdc3287dbc6ab110c494382c/Docs/developer_guide/script_repository/markups.md?plain=1#L687-L689
https://github.com/Slicer/Slicer/blob/673ddca536801eedfdc3287dbc6ab110c494382c/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsJsonStorageNode.cxx#L168-L177</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
