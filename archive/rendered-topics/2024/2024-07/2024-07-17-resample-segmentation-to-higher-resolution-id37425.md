---
topic_id: 37425
title: "Resample Segmentation To Higher Resolution"
date: 2024-07-17
url: https://discourse.slicer.org/t/37425
---

# Resample segmentation to higher resolution

**Topic ID**: 37425
**Date**: 2024-07-17
**URL**: https://discourse.slicer.org/t/resample-segmentation-to-higher-resolution/37425

---

## Post #1 by @mabe2416 (2024-07-17 11:00 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 5.6.2</p>
<p>Hi,<br>
I am trying to run the code of the script repository: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#resample-segmentation-to-higher-resolution" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a></p>
<p>However,  I get: NameError: name ‘segmentationGeometryLogic’ is not defined.</p>
<p>And if I add, segmentationGeometryLogic = slicer.vtkSlicerSegmentationGeometryLogic()</p>
<p>AttributeError: ‘vtkSlicerSegmentationsModuleLogicPython.vtkSlicerS’ object has no attribute ‘SetReferenceImageGeometryInSegmentationNode’</p>
<p>Any help would be greatly appreciated!<br>
Thanks,<br>
Maria</p>

---

## Post #2 by @Barrie (2025-08-27 13:05 UTC)

<p>I just tripped over this too. The example is clearly missing some code.</p>
<p>Did you find a solution that works? If so, can you share it? I’m looking to try this…</p>
<p>Thanks!!!</p>

---

## Post #3 by @Barrie (2025-08-27 13:08 UTC)

<p>Found this, which might be helpful. Haven’t tried it yet, YMMV:</p>
<aside class="quote quote-modified" data-post="5" data-topic="19025">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pj_yu/48/11851_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/change-segmentation-oversampling-factor/19025/5">Change segmentation oversampling factor</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    <a class="mention" href="/u/lassoan">@lassoan</a> Thanks for your help again! 
The source code of vtkSlicerSegmentationGeometryLogic::ResampleLabelmapsInSegmentationNode is really helpful, and I finally completed this function correctly based on the source code. The issues aren’t technical issues, and since it works right now, there’s no needs to worry about upgrading. 
For those who are interested, here is my code. 
segmentIDs = vtk.vtkStringArray()
segmentationNode.GetSegmentation().GetSegmentIDs(segmentIDs)

#Create desired geometry…
  </blockquote>
</aside>


---

## Post #4 by @pieper (2025-08-27 13:21 UTC)

<p>It would be great if someone could submit a PR to fix the script.</p>

---

## Post #5 by @Barrie (2025-08-27 13:31 UTC)

<p>Wish I were less of a “script kiddie in 3D Slicer land”, that’d be fun.</p>

---

## Post #6 by @cpinter (2025-08-27 13:36 UTC)

<p>This should do it</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/8679">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/8679" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/8679" target="_blank" rel="noopener">DOC: Fix segmentation oversampling snippet in script repository</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>cpinter:scriptrepo-segmentation-geometry-fix</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2025-08-27" data-time="13:36:07" data-timezone="UTC">01:36PM - 27 Aug 25 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/cpinter" target="_blank" rel="noopener">
            <img alt="" src="https://avatars.githubusercontent.com/u/1325980?v=4" class="onebox-avatar-inline" width="20" height="20">
            cpinter
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 6 additions and 0 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/8679/files" target="_blank" rel="noopener">
            <span class="added">+6</span>
            <span class="removed">-0</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Re https://discourse.slicer.org/t/resample-segmentation-to-higher-resolution/374<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/8679" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">25</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @jcfr (2025-08-27 18:27 UTC)

<p><img src="https://emoji.discourse-cdn.com/twitter/folded_hands.png?v=14" title=":folded_hands:" class="emoji" alt=":folded_hands:" loading="lazy" width="20" height="20"> <a class="mention" href="/u/cpinter">@cpinter</a> <img src="https://emoji.discourse-cdn.com/twitter/100.png?v=14" title=":100:" class="emoji" alt=":100:" loading="lazy" width="20" height="20"></p>
<p>The pull request has been reviewed &amp; integrated <img src="https://emoji.discourse-cdn.com/twitter/rocket.png?v=14" title=":rocket:" class="emoji" alt=":rocket:" loading="lazy" width="20" height="20"></p>

---
