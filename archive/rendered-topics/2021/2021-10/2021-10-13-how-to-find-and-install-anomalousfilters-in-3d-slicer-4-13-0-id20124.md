# How to find and install AnomalousFilters in 3D Slicer 4.13.0?

**Topic ID**: 20124
**Date**: 2021-10-13
**URL**: https://discourse.slicer.org/t/how-to-find-and-install-anomalousfilters-in-3d-slicer-4-13-0/20124

---

## Post #1 by @kai.cheng.ias (2021-10-13 02:56 UTC)

<p>Hello,</p>
<p>How to find and install AnomalousFilters in 3D Slicer 4.13.0?<br>
I couldn’t find it in the Extensions Manager.</p>
<p>Thank you.</p>
<p>Kai</p>

---

## Post #2 by @lassoan (2021-10-13 03:28 UTC)

<p>Slicer-4.13 uses ITK5 and the maintainer of the extension has not updated his code yet to make it compatible with this ITK version - see this bug report:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/CSIM-Toolkits/AnomalousFiltersExtension/issues/12">
  <header class="source">

      <a href="https://github.com/CSIM-Toolkits/AnomalousFiltersExtension/issues/12" target="_blank" rel="noopener">github.com/CSIM-Toolkits/AnomalousFiltersExtension</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/CSIM-Toolkits/AnomalousFiltersExtension/issues/12" target="_blank" rel="noopener">Make the filters compatible with ITK5</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-04-07" data-time="23:01:27" data-timezone="UTC">11:01PM - 07 Apr 20 UTC</span>
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
    <p class="github-body-container">Thank you for these great noise filters.

Slicer recently switched to ITK5 and<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> since then we get this error when we try to run the filter:

```
Anisotropic Anomalous Diffusion standard error:

C:/Users/andra/AppData/Roaming/NA-MIC/Extensions-28926/AnomalousFiltersExtension/lib/Slicer-4.11/cli-modules/AADImageFilter.exe: exception caught !

itk::ExceptionObject (00000088D34FB120)
Location: "unknown" 
File: d:\d\p\slicer-0-build\itk\modules\core\common\include\itkImageSource.hxx
Line: 273
Description: itk::ERROR: itk::ERROR: AnisotropicAnomalousDiffusionImageFilter(0000019115E83E20): Subclass should override this method!!! If old behavior is desired invoke this-&gt;DynamicMultiThreadingOff(); before Update() is called. The best place is in class constructor.
```

Could you update the filters to make them compatible with ITK5? Thank you very much.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>You can write a comment to this bug report and see if we get any response. You can fix the code yourself, too (you can ask help on the <a href="https://discourse.itk.org">ITK forum</a>, they are always very responsive and could tell you what needs to be changed. If things work on your computer then we can fork the repository and make those fixes, even if we don’t hear from the original maintainer.</p>

---
