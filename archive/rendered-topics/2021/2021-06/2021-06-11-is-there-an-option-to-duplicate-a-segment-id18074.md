---
topic_id: 18074
title: "Is There An Option To Duplicate A Segment"
date: 2021-06-11
url: https://discourse.slicer.org/t/18074
---

# Is there an option to duplicate a segment?

**Topic ID**: 18074
**Date**: 2021-06-11
**URL**: https://discourse.slicer.org/t/is-there-an-option-to-duplicate-a-segment/18074

---

## Post #1 by @Giovanni_Cunha (2021-06-11 09:18 UTC)

<p>I would like to know how to duplicate a segmentation on Slicer. Is there some option to do it?</p>
<p>best</p>

---

## Post #2 by @simonoxen (2021-06-11 10:17 UTC)

<p>Hi, I guess you can do the following:</p>
<p>To duplicate a <strong>segment</strong> you can Add a new segment and use the Copy operation under the Logical operations Effect.</p>
<p>To duplicate a <strong>segmentation</strong> you can clone the node by right clicking → Clone in the Data module</p>

---

## Post #3 by @OpenSource_Contri (2021-06-11 16:00 UTC)

<p><a class="mention" href="/u/simonoxen">@simonoxen</a><br>
Could you please tell where to find “clone” segment file to explore its functionalities (i.e. .cxx or .py file)?</p>

---

## Post #4 by @simonoxen (2021-06-11 16:17 UTC)

<blockquote>
<p>To duplicate a <strong>segment</strong> you can Add a new segment and use the Copy operation under the Logical operations Effect.</p>
</blockquote>
<p><a href="https://github.com/Slicer/Slicer/blob/4483cc0e6f288b0816b6329f1829d9ef8c5aa81a/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorLogicalEffect.py" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/blob/4483cc0e6f288b0816b6329f1829d9ef8c5aa81a/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorLogicalEffect.py</a></p>
<blockquote>
<p>To duplicate a <strong>segmentation</strong> you can clone the node by right clicking → Clone in the Data module</p>
</blockquote>
<p><a href="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Modules/Loadable/SubjectHierarchy/Logic/vtkSlicerSubjectHierarchyModuleLogic.cxx" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Modules/Loadable/SubjectHierarchy/Logic/vtkSlicerSubjectHierarchyModuleLogic.cxx</a></p>

---

## Post #5 by @lassoan (2021-06-11 19:32 UTC)

<p>This question has just been asked and answered here, too:</p>
<aside class="quote" data-post="2" data-topic="18081">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/clone-segment-button/18081/2">Clone Segment Button</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    I’ve added an example for this in the script repitository: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#clone-a-segment">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#clone-a-segment</a>
  </blockquote>
</aside>


---

## Post #6 by @lassoan (2021-06-12 11:59 UTC)

<p>A post was split to a new topic: <a href="/t/how-to-disable-the-clone-button/18090">How to disable the clone button?</a></p>

---

## Post #7 by @Giovanni_Cunha (2021-06-17 07:45 UTC)

<p>Thank you everyone for the explanations!</p>

---

## Post #8 by @lassoan (2021-06-17 13:19 UTC)

<p>I’ve submitted a pull request that makes “Clone” action clone the segment if the user right-clicks on a segment (and not clone the entire segmentation):</p>
<aside class="onebox githubpullrequest">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/5700" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/5700" target="_blank" rel="noopener">ENH: Make Clone action clone a segment when a segment is selected in subject hierarchy</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>lassoan:clone-segment-sh-action</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-06-17" data-time="13:17:54" data-timezone="UTC">01:17PM - 17 Jun 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="1 commits changed 6 files with 141 additions and 13 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/5700/files" target="_blank" rel="noopener">
          <span class="added">+141</span>
          <span class="removed">-13</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Previously, "Clone" action duplicated the entire segmentation node, even when ri<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/5700" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ght-clicked on a segment.
This commit changes the behavior so that if the user right-clicks on a Segment and chooses Clone then only that selected segment will be cloned.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It will be probably merged within 1-2 days and appear in Slicer Preview Release the next day.</p>

---
