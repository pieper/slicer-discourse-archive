# Load Dicom Data Error

**Topic ID**: 1159
**Date**: 2017-10-02
**URL**: https://discourse.slicer.org/t/load-dicom-data-error/1159

---

## Post #1 by @rclipp (2017-10-02 20:21 UTC)

<p>I am trying to load several different Dicom data sets and getting the error shown in the image. Sometimes, the data seems to load anyway and I can continue. But othertimes I get image shown. I am using the nightly build from 9/30/2017 on a windows 10 machine.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8c74c54b3099d43d586156f12f6642083c100b0.png" data-download-href="/uploads/short-url/xdfLAgoSzKf5JzckQ62A7ZEMdGM.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8c74c54b3099d43d586156f12f6642083c100b0.png" alt="image" data-base62-sha1="xdfLAgoSzKf5JzckQ62A7ZEMdGM" width="690" height="129" data-dominant-color="FBEDED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1007×189 14.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a5a099a61f72beafa5f5cd1026bf25c035ab2ee.jpeg" data-download-href="/uploads/short-url/62EXpt4vF82uV5luyIdpCSDb2Y6.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/2a5a099a61f72beafa5f5cd1026bf25c035ab2ee_2_690x316.jpg" alt="image" data-base62-sha1="62EXpt4vF82uV5luyIdpCSDb2Y6" width="690" height="316" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/2a5a099a61f72beafa5f5cd1026bf25c035ab2ee_2_690x316.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a5a099a61f72beafa5f5cd1026bf25c035ab2ee.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a5a099a61f72beafa5f5cd1026bf25c035ab2ee.jpeg 2x" data-dominant-color="494947"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">924×424 37.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks for any help!<br>
Rachel</p>

---

## Post #2 by @pieper (2017-10-02 22:31 UTC)

<p>Hi Rachel -</p>
<p>Looks like that is an issue in the MultiVolume plugin.  On thing to try as a workaround is going into Advanced mode in the DICOM browser (checkbox on lower right) and then unchecking that plugin from the list on the left.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f90756b94644687e7e62081867806b50ae68e1c.png" data-download-href="/uploads/short-url/fUWv1UTEPNgFAb710ovHLvILRYo.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f90756b94644687e7e62081867806b50ae68e1c_2_690x115.png" alt="image" data-base62-sha1="fUWv1UTEPNgFAb710ovHLvILRYo" width="690" height="115" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f90756b94644687e7e62081867806b50ae68e1c_2_690x115.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f90756b94644687e7e62081867806b50ae68e1c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f90756b94644687e7e62081867806b50ae68e1c.png 2x" data-dominant-color="F8F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">908×152 10.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>HTH,<br>
Steve</p>

---

## Post #3 by @lassoan (2017-10-03 03:51 UTC)

<p>The issue is due to slicer.dicomDatabase.fileValue(file,self.tags[frameTag]) returning <code>__TAG_NOT_IN_INSTANCE__</code> value instead of empty value (when a file is not found on disk).</p>
<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/fedorov">@fedorov</a> - do you know why this may be happening now?</p>
<p>Pull request with the fix is submitted: <a href="https://github.com/fedorov/MultiVolumeImporter/pull/23">https://github.com/fedorov/MultiVolumeImporter/pull/23</a></p>

---

## Post #4 by @pieper (2017-10-03 11:40 UTC)

<p>Yes, <a class="mention" href="/u/fedorov">@fedorov</a> pointed this out the other day and there’s a fix to the database here:</p>
<aside class="onebox githubpullrequest">
  <header class="source">
      <a href="https://github.com/commontk/CTK/pull/750" target="_blank">github.com/commontk/CTK</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/commontk/CTK/pull/750" target="_blank">BUG: consistent return for value of uninitialized data</a>
    </h4>

    <div class="branches">
      <code>commontk:master</code> ← <code>pieper:749-tag-cache-on-bad-data</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2017-09-29" data-time="15:08:45" data-timezone="UTC">03:08PM - 29 Sep 17 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/pieper" target="_blank">
          <img alt="pieper" src="https://avatars0.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
          pieper
        </a>
      </div>

      <div class="lines" title="1 commits changed 2 files with 15 additions and 10 deletions">
        <a href="https://github.com/commontk/CTK/pull/750/files" target="_blank">
          <span class="added">+15</span>
          <span class="removed">-10</span>
        </a>
      </div>
    </div>

  </div>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #5 by @fedorov (2017-10-03 15:52 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I experienced the same issue in a different context with a different plugin. The issue is not in MultiVolumeImporter plugin, but in the DICOM database code due to that inconsistent return value. But why that is happening, I don’t know. I hope it goes away once the PR above is merged, but let me know if you still want to merge <a href="https://github.com/fedorov/MultiVolumeImporter/pull/23">https://github.com/fedorov/MultiVolumeImporter/pull/23</a> - it should be harmless.</p>

---
