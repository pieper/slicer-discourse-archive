---
topic_id: 36677
title: "When Did The Slicer Switch To Lps For Fcsv"
date: 2024-06-10
url: https://discourse.slicer.org/t/36677
---

# When did the Slicer switch to LPS for fcsv?

**Topic ID**: 36677
**Date**: 2024-06-10
**URL**: https://discourse.slicer.org/t/when-did-the-slicer-switch-to-lps-for-fcsv/36677

---

## Post #1 by @muratmaga (2024-06-10 05:26 UTC)

<p>As per <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/markups.html#markups-fiducial-point-list-file-format-fcsv" class="inline-onebox">Markups — 3D Slicer documentation</a></p>
<p>There was a time coordinates was written in RAS. Is it possible to get the specific date LPS became the “standard” for markup files?</p>

---

## Post #2 by @jamesobutler (2024-06-10 11:19 UTC)

<p>See the detailed commit message info in the following 2 commits:</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/Slicer/commit/61b18e4906bfba3f7585c101e3dd5fb2d7762080">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/commit/61b18e4906bfba3f7585c101e3dd5fb2d7762080" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/61b18e4906bfba3f7585c101e3dd5fb2d7762080" target="_blank" rel="noopener nofollow ugc">ENH: Write coordinate system to model files</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2017-09-27" data-time="22:58:52" data-timezone="UTC">10:58PM - 27 Sep 17 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener nofollow ugc">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="changed 2 files with 127 additions and 76 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/61b18e4906bfba3f7585c101e3dd5fb2d7762080" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+127</span>
          <span class="removed">-76</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">https://issues.slicer.org/view.php?id=4408

In recent years, LPS coordinate syst<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/commit/61b18e4906bfba3f7585c101e3dd5fb2d7762080" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">em has become much more widely used than RAS.
When Slicer saves a node to file, it already uses RAS for images and transforms and can use LPS for markups.
However, model node have been still saved as RAS. This caused a problem, because when models and images are
used or created by external software, models and images are not displayed consistently.

Unfortunately, generic mesh file formats have no standard way of storing coordinate system (axis orientation)
information, therefore switching to LPS could not be performed in a single step without breaking backward compatibility.

Proposed solution: Switch to LPS-based model files in multiple steps.

Step 1: Write coordinate system information (SPACE=RAS) to model files. Use comments in STL, PLY, and OBJ files; as field data in VTK files.
Keep writing data as RAS.

Step 2: Allow reading/writing models that use LPS coordinate system (add an option in Add data dialog; add an option in storage node).
Use coordinate system that is stored in the file header. If no coordinate system information is found in the file then assume RAS.

Step 3: Write models to file in LPS coordinate system by default.

Step 4: If no coordinate system information is found in the file then assume LPS.

---

Step 3-4 somewhat break backward compatibility, therefore there should be either sufficient amount of time (1-2 years) has to be
left after Step 1, or these steps should be done in a new major release.

This commit implements Step 1 (with the limitation that coordinate system info cannot be saved into OBJ files and ascii STL files
due to limitation of VTK API - but these formats are rarely used anyway).

svn-url: http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26398
git-svn-id: http://svn.slicer.org/Slicer4/trunk@26398 3bd1e089-480b-0410-8dfb-8563597acbee</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/Slicer/commit/6036edbc4b67712822ccb4ee89139cab1cbce3f2">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/commit/6036edbc4b67712822ccb4ee89139cab1cbce3f2" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/6036edbc4b67712822ccb4ee89139cab1cbce3f2" target="_blank" rel="noopener nofollow ugc">ENH: Store markups and models in LPS coordinate system by default</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2020-02-26" data-time="15:44:10" data-timezone="UTC">03:44PM - 26 Feb 20 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener nofollow ugc">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="changed 19 files with 657 additions and 160 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/6036edbc4b67712822ccb4ee89139cab1cbce3f2" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+657</span>
          <span class="removed">-160</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Slicer used LPS coordinate system when storing images, transforms, and markups. <span class="show-more-container"><a href="https://github.com/Slicer/Slicer/commit/6036edbc4b67712822ccb4ee89139cab1cbce3f2" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">All medical image computing software (maybe except a few very old ones) uses LPS coordinate system, too. Slicer started embedding coordinate system name in mesh files (STL, VTK, VTP, OBJ, PLY) a few years ago, but still has been using RAS by default for saving models. This caused inconsistencies when Slicer-exported data was used in third-party software. See https://issues.slicer.org/view.php?id=4445 for details.

This commit changes default coordinate system in saved models to LPS. When loading a model that has coordinate system information embedded in the file, then that coordinate system is used. If the model does not contain coordinate system information then the CoordinateSystem property of model storage node is used. CoordinateSystem is set to LPS by default but the user can change it in "Add data" dialog (in "Options" column).

Backward compatibility:
- all old Slicer scenes are loaded correctly (if model coordinate system is not specified in the storage node the mrml scene file, then it is assumed to be RAS)
- all standalone model files that Slicer created since 2017-09-27 (Slicer-4.8.0) are read correctly (except obj files created by Slicer-4.8.x)
- all files created by external software that use LPS coordinate system are read correctly
- as a result, the only files that require manual selection of RAS coordinate system (and only when loading without a scene): model files created by Slicer-4.6 (2017-09-27) and earlier; and obj files created by Slicer-4.6 and Slicer-4.8 (between 2016-10-11 and 2018-03-26).

Also cleaned up markups node coordinate system writing (use LPS/RAS string instead of magic numbers, similar style as model nodes, added tests).

svn-url: http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=28794
git-svn-id: http://svn.slicer.org/Slicer4/trunk@28794 3bd1e089-480b-0410-8dfb-8563597acbee</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @muratmaga (2024-06-10 14:42 UTC)

<p>Exactly what I needed. Thanks.</p>

---
