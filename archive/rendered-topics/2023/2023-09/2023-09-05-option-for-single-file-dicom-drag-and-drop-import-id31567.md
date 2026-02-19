---
topic_id: 31567
title: "Option For Single File Dicom Drag And Drop Import"
date: 2023-09-05
url: https://discourse.slicer.org/t/31567
---

# Option for Single-File DICOM Drag-and-Drop Import

**Topic ID**: 31567
**Date**: 2023-09-05
**URL**: https://discourse.slicer.org/t/option-for-single-file-dicom-drag-and-drop-import/31567

---

## Post #1 by @alireza (2023-09-05 13:20 UTC)

<p>The current behavior in 3D Slicer for loading DICOM files have changed and automatically indexes all the DICOM files present in the same folder as the dragged DICOM file. This causes inconvenience in scenarios where a user wants to load only a specific DICOM file for inspection, especially when it resides in a folder containing multiple DICOM files.</p>
<p>Drag and drop usecase should just care about the dragged content and not the directory, similar to other apps in my opinion: e.g., in powerpoint, if you drag and drop an image you don’t get all the other images in that folder imported, word, and other apps too</p>
<p>You can make a case for when a directory is imported, but darg and drop becomes meaningless if you import all files in that folder.</p>
<p>Read more here <a href="https://discourse.slicer.org/t/dicom-drag-and-drop-loads-all-the-dicoms-in-the-same-folder-instead-of-just-the-dragged-one/31437/4" class="inline-onebox">DICOM drag and drop loads all the dicoms in the same folder instead of just the dragged one - #4 by alireza</a></p>

---

## Post #2 by @jamesobutler (2023-09-05 17:04 UTC)

<p>This may go well with my PR to add a “DICOM Direct Load” option which allows for loading DICOM image data without using the DICOM browser of the DICOM module if all you care about is the image data and not viewing all the metadata info.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/7156">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/7156" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/7156" target="_blank" rel="noopener nofollow ugc">ENH: Add DICOM direct load reader</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>jamesobutler:dicom-direct-load-reader</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2023-08-06" data-time="18:00:10" data-timezone="UTC">06:00PM - 06 Aug 23 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
            <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
            jamesobutler
          </a>
        </div>

        <div class="lines" title="2 commits changed 8 files with 97 additions and 6 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/7156/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+97</span>
            <span class="removed">-6</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This is used for directly loading DICOM files into the scene without adding to t<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/7156" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">he DICOM database. The DICOM module however is still used in the logic for loading. Currently there is the "DICOM import" reader option from the Add Data dialog which will import it into the DICOM database, but will not load it into the scene.

Based on https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#load-dicom-files-into-the-scene-from-a-folder</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
