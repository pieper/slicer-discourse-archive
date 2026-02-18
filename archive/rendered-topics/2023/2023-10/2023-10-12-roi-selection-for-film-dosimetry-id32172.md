# ROI selection for film dosimetry

**Topic ID**: 32172
**Date**: 2023-10-12
**URL**: https://discourse.slicer.org/t/roi-selection-for-film-dosimetry/32172

---

## Post #1 by @jmw972 (2023-10-12 03:00 UTC)

<p>Hello, I am new to the Slicer Film Dosimetry module. I am running through the steps and using the example data provided. However, I am stuck at the region selection stage for calibration. I could not add ROI after clicking on the <em>Add Region</em>. Attached is the image of the calibration window. Any help would be great, thank you.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3513f79cfd12207e76a661cf00821c422387f6b.png" data-download-href="/uploads/short-url/yIu65GMsdCajPGY0X5pWvoJJ7d1.png?dl=1" title="Screenshot (104)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f3513f79cfd12207e76a661cf00821c422387f6b_2_690x388.png" alt="Screenshot (104)" data-base62-sha1="yIu65GMsdCajPGY0X5pWvoJJ7d1" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f3513f79cfd12207e76a661cf00821c422387f6b_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f3513f79cfd12207e76a661cf00821c422387f6b_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f3513f79cfd12207e76a661cf00821c422387f6b_2_1380x776.png 2x" data-dominant-color="83838B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (104)</span><span class="informations">1920×1080 196 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2023-10-13 12:23 UTC)

<p>This extension is not maintained anymore, so it is probable that your issue is due to the API changes since then, see</p><aside class="onebox githubissue" data-onebox-src="https://github.com/SlicerRt/FilmDosimetryAnalysis/issues/2">
  <header class="source">

      <a href="https://github.com/SlicerRt/FilmDosimetryAnalysis/issues/2" target="_blank" rel="noopener">github.com/SlicerRt/FilmDosimetryAnalysis</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/SlicerRt/FilmDosimetryAnalysis/issues/2" target="_blank" rel="noopener">Update modules to use markups instead of annotations</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-09-14" data-time="17:18:21" data-timezone="UTC">05:18PM - 14 Sep 22 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Annotations module, which provides `vtkMRMLAnnotationROI` and `vtkMRMLAnnotation<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">Ruler` nodes have been deprecated since April 2021 and will be removed in Slicer-5.4 stable version early next year.
Since some modules in this extension use annotation nodes, these modules need to be updated to use markups nodes before the end of this year.

[This section](https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer#Slicer_5.3%3A_Removed_Annotation_module) of the migration guide should help with implementing the changes and any questions can be asked at the [Remove Annotations module topic in the Slicer forum](https://discourse.slicer.org/t/remove-annotations-module/25271).

Impacted modules:
- FilmDosimetryAnalysis\FilmDosimetryAnalysisLogic\FilmDosimetryAnalysisLogic.py 
- FilmDosimetryAnalysis\FilmDosimetryAnalysis.py</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Maybe you can try the film dosimetry extension with an older version of Slicer, such as 4.10.</p>
<p>Or you can try to fix the extension for the latest version if you feel motivated. I can give pointers if you decide to go for it.</p>

---
