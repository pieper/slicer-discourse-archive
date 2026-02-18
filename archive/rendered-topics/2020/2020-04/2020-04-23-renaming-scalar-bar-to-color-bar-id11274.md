# Renaming Scalar Bar to Color Bar

**Topic ID**: 11274
**Date**: 2020-04-23
**URL**: https://discourse.slicer.org/t/renaming-scalar-bar-to-color-bar/11274

---

## Post #1 by @jamesobutler (2020-04-23 22:10 UTC)

<p>Could we rename “ScalarBar” to something like “Color Bar” or “Color Scalar Bar” in the GUI? I know the underlying vtk object is called a <a href="https://vtk.org/doc/nightly/html/classvtkScalarBarActor.html#details" rel="noopener nofollow ugc">vtkScalarBarActor</a> with the description:</p>
<blockquote>
<p>A scalar bar is a legend that indicates to the viewer the correspondence between color value and data value.</p>
</blockquote>
<p>I’m not sure why “Color” was not included in the name of the object.</p>
<p>I have noticed in various forum posts people referring to it as the “Color Bar” while in the GUI it is labeled as “ScalarBar”. This is probably a contributing factor for people struggling to find it in addition to it being buried in DataProbe module which is a separate issue.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/80e249f8d3c8b04482ed9567a438206252c40599.png" data-download-href="/uploads/short-url/io9W9UMhYbPGE2m3UBM1VbPLp4B.png?dl=1" title="scalar-bar-slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80e249f8d3c8b04482ed9567a438206252c40599_2_690x373.png" alt="scalar-bar-slicer" data-base62-sha1="io9W9UMhYbPGE2m3UBM1VbPLp4B" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80e249f8d3c8b04482ed9567a438206252c40599_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80e249f8d3c8b04482ed9567a438206252c40599_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80e249f8d3c8b04482ed9567a438206252c40599_2_1380x746.png 2x" data-dominant-color="8E8D94"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">scalar-bar-slicer</span><span class="informations">1920×1040 243 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2020-04-23 22:24 UTC)

<p>It’s also confusing that the controls for the 2D scalar bar are in the DataProbe and the 3D scalar bar is in the Colors module.  I think it would be logical to access this kind of setting via right click on the background of the viewer (or maybe in the controller widget, but those are very busy already).</p>
<p>+1 for “Color Scalar Bar” in the GUI</p>

---

## Post #3 by @jamesobutler (2020-04-25 17:46 UTC)

<p>I issued <a href="https://github.com/Slicer/Slicer/pull/4889" rel="nofollow noopener">https://github.com/Slicer/Slicer/pull/4889</a> to update the name used in the GUI to “Color Scalar Bar”.</p>

---

## Post #4 by @lassoan (2020-04-25 20:53 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="11274">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I think it would be logical to access this kind of setting via right click on the background of the viewer (or maybe in the controller widget, but those are very busy already).</p>
</blockquote>
</aside>
<p>Yes, it should be shown/hidden at the same place where the displayed volumes are selected. Probably it just happened to be placed in the Data Probe module just because the developer who has implemented it was only comfortable with Python and did not know that it should have been implemented properly using a displayable manager. I think we already have an issue for reworking the Data Probe module.</p>

---

## Post #5 by @jamesobutler (2020-04-25 21:09 UTC)

<p>I don’t see a github issue for that work or transitioning it to use a displayable manager. The closest git issue seems to be <a href="https://github.com/Slicer/Slicer/issues/3820" rel="nofollow noopener">https://github.com/Slicer/Slicer/issues/3820</a> which is incorporating some changes from the Paraview scalar bar. You might want to write up a git issue with these specific details about converting to use a displayable manager</p>

---

## Post #6 by @lassoan (2020-04-26 01:12 UTC)

<p>I could not find a related issue, so added this:</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/4891" target="_blank">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/4891" target="_blank">Display color bar using displayable manager</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-04-26" data-time="01:11:37" data-timezone="UTC">01:11AM - 26 Apr 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank">
          <img alt="lassoan" src="https://avatars0.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">Color bars in slice and 3D views are currently not handled by displayable managers and not managed by appropriate modules.
All color...</p>
</div>

<div class="labels">
    <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">type:enhancement</span>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
