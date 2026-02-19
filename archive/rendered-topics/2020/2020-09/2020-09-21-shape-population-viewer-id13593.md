---
topic_id: 13593
title: "Shape Population Viewer"
date: 2020-09-21
url: https://discourse.slicer.org/t/13593
---

# Shape Population Viewer

**Topic ID**: 13593
**Date**: 2020-09-21
**URL**: https://discourse.slicer.org/t/shape-population-viewer/13593

---

## Post #1 by @Madelene_Habib (2020-09-21 17:45 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10.2</p>
<p>I’m trying to use the ‘shape population view’ module, when I installed and restarted 3Dslicer it does not show up when i search for the module. I tried reinstalling 3dslicer but still have the same issue. Is there a solution to this problem? Thank you.</p>

---

## Post #2 by @lassoan (2020-09-21 18:21 UTC)

<p>You may need to use latest Slicer Preview Release.</p>

---

## Post #3 by @sfglio (2021-07-06 19:24 UTC)

<p>ShapePoupulationViewer (and CMFreg) cannot be installed anymore in Slicer (latest nigthy version). Is it only accessible any more via SlicerSALT???</p>

---

## Post #4 by @lassoan (2021-07-09 05:22 UTC)

<p>It seems that Shape Population Viewer has not been updated to be compatible with VTK9 (the new visualization toolkit version that is used in recent Slicer Preview Releases). You can add a comment to this issue to indicate that you would need this feature:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/NIRALUser/ShapePopulationViewer/issues/55">
  <header class="source">

      <a href="https://github.com/NIRALUser/ShapePopulationViewer/issues/55" target="_blank" rel="noopener">github.com/NIRALUser/ShapePopulationViewer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/NIRALUser/ShapePopulationViewer/issues/55" target="_blank" rel="noopener">Fix build error when building against VTK9</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-03-10" data-time="14:25:39" data-timezone="UTC">02:25PM - 10 Mar 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener">
          <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">See  https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2021-03-10&amp;fi<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ltercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=ShapePopulationViewer

```
D:\D\P\S-0-E-b\ShapePopulationViewer\src\vtkPVPostFilter.h(37,61): error C3646: 'VTK_OVERRIDE': unknown override specifier [D:\D\P\S-0-E-b\ShapePopulationViewer-build\src\ShapePopulationViewerWidget.vcxproj]
```

```
src/customizeColorMapByDirectionDialogQT.h:33:25: fatal error: QVTKWidget.h: No such file or directory
```</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
