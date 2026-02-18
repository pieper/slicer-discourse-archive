# SlicerDMRI cannot be installed.

**Topic ID**: 22441
**Date**: 2022-03-10
**URL**: https://discourse.slicer.org/t/slicerdmri-cannot-be-installed/22441

---

## Post #1 by @lizhihong (2022-03-10 21:25 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0bd8c2d451a55ec5848304683bf30943551bdded.png" data-download-href="/uploads/short-url/1GNEXiv3hlGlaQtV423HhJFObnf.png?dl=1" title="0019_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0bd8c2d451a55ec5848304683bf30943551bdded_2_515x500.png" alt="0019_1" data-base62-sha1="1GNEXiv3hlGlaQtV423HhJFObnf" width="515" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0bd8c2d451a55ec5848304683bf30943551bdded_2_515x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0bd8c2d451a55ec5848304683bf30943551bdded_2_772x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0bd8c2d451a55ec5848304683bf30943551bdded.png 2x" data-dominant-color="F6F5F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">0019_1</span><span class="informations">783×760 33.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
version 4.13.0    revision 30691       built 2022-03-10</p>

---

## Post #2 by @lassoan (2022-03-10 21:27 UTC)

<p>Thanks for reporting. We are aware of this issue and will fix it hopefully in a couple of days. You can follow the progress of the work here:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5269">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5269" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5269" target="_blank" rel="noopener">Update extensions for Slicer-4.13</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-10-26" data-time="20:39:44" data-timezone="UTC">08:39PM - 26 Oct 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">It is expected that due to VTK and other library updates, extensions may need to<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> be updated, too. This ticket tracks these necessary updates.

Known issues:
- [x] SlicerRadiomics - https://discourse.slicer.org/t/slicerradiomics-error/14258
- [x] SlicerVMTK - macOS packaging is broken (https://github.com/vmtk/SlicerExtension-VMTK/issues/37)
- [x] SlicerJupyter - linux build failed, Python and library updates fixed it
- [x] ShapePopulationViewer - Windows build fails
- [ ] SlicerRT - linux build error due to ITK https://github.com/SlicerRt/SlicerRT/issues/206
- [ ] PathReconstruction - linux build fails, probably due to SlicerRT failure
- [ ] SlicerVirtualReality (https://github.com/KitwareMedical/SlicerVirtualReality/pull/90)
- [ ] CMFreg - Windows build fails
- [ ] DRRGenerator - Windows build fails
- [ ] SlicerRadiomics - https://discourse.slicer.org/t/factory-build-of-python-extensions-conflicting-with-each-other/21935
- [ ] SlicerIGSIO (https://github.com/IGSIO/SlicerIGSIO/issues/17)
- [ ] DCMQI (see https://github.com/QIICR/dcmqi/issues/446)
- [ ] Chest_Imaging_Platform ([C++11/14 configuration mismatch](https://github.com/acil-bwh/ChestImagingPlatform/pull/42) + [VTK API change](https://github.com/acil-bwh/SlicerCIP/pull/37))</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
