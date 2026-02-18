# Loading a FFS CT Volume using "Add Data" vs "Import Dicom files"

**Topic ID**: 30495
**Date**: 2023-07-10
**URL**: https://discourse.slicer.org/t/loading-a-ffs-ct-volume-using-add-data-vs-import-dicom-files/30495

---

## Post #1 by @neverpaymoney (2023-07-10 12:33 UTC)

<p>Hello,</p>
<p>I am loading a CT dicom volume using:<br>
<strong>AddData</strong></p>
<ol>
<li>“Add Data”</li>
<li>Correct display:</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb00d7e4e3722926ef27fe68e356bab987eb825b.jpeg" data-download-href="/uploads/short-url/xwW0LE8err5AquanqqOEE2vcJm3.jpeg?dl=1" title="AddData" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb00d7e4e3722926ef27fe68e356bab987eb825b_2_690x324.jpeg" alt="AddData" data-base62-sha1="xwW0LE8err5AquanqqOEE2vcJm3" width="690" height="324" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb00d7e4e3722926ef27fe68e356bab987eb825b_2_690x324.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb00d7e4e3722926ef27fe68e356bab987eb825b_2_1035x486.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb00d7e4e3722926ef27fe68e356bab987eb825b_2_1380x648.jpeg 2x" data-dominant-color="252523"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">AddData</span><span class="informations">2911×1370 198 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>ImportDicomFiles</strong></p>
<ol>
<li>"import dicom files</li>
<li>Load Data</li>
<li>Wrong display?</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48eb4b9c6054505edd669a102a2f4aaeef0f7f50.jpeg" data-download-href="/uploads/short-url/ap4uK1MEYdZmpZpNE4b62dyNM0o.jpeg?dl=1" title="ImportDicom" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48eb4b9c6054505edd669a102a2f4aaeef0f7f50_2_690x329.jpeg" alt="ImportDicom" data-base62-sha1="ap4uK1MEYdZmpZpNE4b62dyNM0o" width="690" height="329" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48eb4b9c6054505edd669a102a2f4aaeef0f7f50_2_690x329.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48eb4b9c6054505edd669a102a2f4aaeef0f7f50_2_1035x493.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48eb4b9c6054505edd669a102a2f4aaeef0f7f50_2_1380x658.jpeg 2x" data-dominant-color="2C2C2A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ImportDicom</span><span class="informations">2917×1391 206 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Does anyone know the reason of the difference?</p>
<p>Thanks.</p>

---

## Post #2 by @pieper (2023-07-10 14:33 UTC)

<p>Always use the DICOM module for loading DICOM data to void issues like this.  Using Add Data bypasses some checks.</p>
<p>As it happens we are planning to make that behavior the default in the future:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/7077">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/7077" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/7077" target="_blank" rel="noopener">ENH: Load DICOM files using DICOM module by default</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>lassoan:load-dicom-using-dicom-module</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2023-07-09" data-time="19:43:40" data-timezone="UTC">07:43PM - 09 Jul 23 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 3 files with 40 additions and 62 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/7077/files" target="_blank" rel="noopener">
            <span class="added">+40</span>
            <span class="removed">-62</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Drag-and-dropping a DICOM file made Slicer use ITK DICOM reader, which often did<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/7077" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> not load the data correctly.

This commit adds a new "DICOM import" reader type, which is selected by default for DICOM files. This reader imports the files into the Slicer DICOM database and switches to the DICOM module.

The workaround of interpreting all files as DICOM by default while in DICOM module has now been removed. "Add data" window is brought up when loading a file, regardless of what is the active module. The workaround surprised users when they could not load non-DICOM data while they were in DICOM module.

If a user wants to read the DICOM file using ITK reader, it is possible by changing "Description" in the "Add data" module to "Volume".

fixes #5726</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2023-07-10 17:11 UTC)

<p>Your example shows that “Add data” loaded the data incorrectly (the orientation marker - yellow guy - is inconsistent with the image content), while the DICOM module loaded it correctly.</p>
<p>If you want to change the orientation of slice views then you can use the sliders in <code>Reformat</code> module.</p>

---
