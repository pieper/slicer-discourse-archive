# Removal of Lightbox Mode

**Topic ID**: 45227
**Date**: 2025-11-25
**URL**: https://discourse.slicer.org/t/removal-of-lightbox-mode/45227

---

## Post #1 by @dokay1 (2025-11-25 21:42 UTC)

<p>I’ve just installed Version 5.10.0 to realize that Lightbox view was removed.</p>
<p>While I understand that many don’t use it, it was the single most helpful image review setting. It allows one to review and compare thick sliced imaging in a single view. Would it be possible to return it?</p>

---

## Post #2 by @pieper (2025-11-27 18:42 UTC)

<p>Thanks for the feedback about the utility of lightbox mode.  The mode was removed because it was carried forward from an older generation of Slicer infrastructure and difficult to maintain while modernizing other features.  There’s some more detail, and a suggested alternative in the links below.  It would be great to support your use case with one of the more sustainable implementations.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/thibault_pelletier">@Thibault_Pelletier</a></p>
<aside class="quote quote-modified" data-post="1" data-topic="495">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/who-uses-lightbox-view/495">Who uses Lightbox view?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    Slicer can show a lightbox view of slices (mosaic of slightly shifted views along the slice normal). The view can be activated in slice view controller by clicking on the lightbox icon and selecting number of views to show. 
[image] 
However, it seems there are many issues with lightbox views: 

interaction within lightbox views is extremely difficult to implement correctly (see for example this issue <a href="https://issues.slicer.org/view.php?id=1690" class="inline-onebox">fiducial shows in wrong lightbox cell · Issue #1690 · Slicer/Slicer · GitHub</a> - which explains w…
  </blockquote>
</aside>

<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/4749">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/4749" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/4749" target="_blank" rel="noopener">Replace dynamic lightbox views with static image generation</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-20" data-time="13:30:41" data-timezone="UTC">01:30PM - 20 Mar 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Type: Enhancement
        </span>
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Priority: Low
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Support of lightbox views in displayable managers would introduce a lot of compl<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">exity. Updating a lightbox view is also very slow.

Replace dynamic rendering of lightbox views with generation of a single static image. Probably screen capture module can be upgraded to implement this.

See discussion here: https://discourse.slicer.org/t/who-uses-lightbox-view/495</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/8773">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/8773" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/8773" target="_blank" rel="noopener">ENH: Add vtkMRMLScriptedLightBoxRendererManagerProxy</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>Thibault-Pelletier:add_scripted_lightbox_proxy</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2025-10-07" data-time="08:37:32" data-timezone="UTC">08:37AM - 07 Oct 25 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/Thibault-Pelletier" target="_blank" rel="noopener">
            <img alt="" src="https://avatars.githubusercontent.com/u/58782295?v=4" class="onebox-avatar-inline" width="20" height="20">
            Thibault-Pelletier
          </a>
        </div>

        <div class="lines" title="1 commits changed 3 files with 114 additions and 0 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/8773/files" target="_blank" rel="noopener">
            <span class="added">+114</span>
            <span class="removed">-0</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Add scripted light box renderer manager proxy to allow python based applications<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/8773" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">, including slicer-trame, to provide light box renderer and activate associated features including cross hair display.

@jcfr &amp; @lassoan let me know if this should go in Slicer or if I should put that in the SlicerTrame extension.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/8776">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/8776" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/8776" target="_blank" rel="noopener">ENH: Simplify Slice view removing LightBox feature</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>jcfr:remove-lightbox-feature</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2025-10-07" data-time="18:41:45" data-timezone="UTC">06:41PM - 07 Oct 25 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/jcfr" target="_blank" rel="noopener">
            <img alt="" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
            jcfr
          </a>
        </div>

        <div class="lines" title="11 commits changed 45 files with 226 additions and 1130 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/8776/files" target="_blank" rel="noopener">
            <span class="added">+226</span>
            <span class="removed">-1130</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This removes LightBox configuration from the slice view controller, and displaya<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/8776" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ble managers.

- UI: remove LightBox actions/controls from slice controller and info widgets.
- Display managers: remove `vtkMRMLLightBoxRendererManagerProxy` and wiring.
- Coordinates: XYZ conversions now always set z = 0.0 (was LightBox id). X/Y remain pane-local by subtracting the renderer origin.
- Crosshair: add the actor to the default slice renderer and drop LightBox renderer switching logic.
- API:
  - Mark `vtkMRMLAbstractDisplayableManager::GetRenderer(int)` as deprecated (forwards to `GetRenderer()`; `idx` ignored).
  - Keep `SetCrosshairRAS(..., int)` but ignore the id parameter and document it as deprecated.
  - Mark `qMRMLSliceInformationWidget::setLightboxLayoutRows`/`setLightboxLayoutColumns` as deprecated
  - Mark `qMRMLSliceControllerWidget::setLightbox`/`setLightboxTo*` as deprecated

Related issue(s) and pull-request(s):
- https://github.com/Slicer/Slicer/pull/8773
- https://github.com/Slicer/Slicer/issues/4749</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2025-11-28 13:01 UTC)

<p>The lightbox feature is still available, but in Screen Capture module. If works more similarly to a traditional film, e.g., you get one static high-resolution image. If you provide more information about your workflow and needs then we may be able to make it work more conveniently for you (for example, make it easier to generate or review the image).</p>

---

## Post #4 by @dokay1 (2025-12-21 20:20 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="45227">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>le, but in Screen Capture module. If works more similarly to a traditional film, e.g., you get one static high-resolution image. If you provide more information about your workflow and needs then we may be able to make it work more conveniently for you (for example, make it easier to generate or review the image</p>
</blockquote>
</aside>
<p>Yeah I use it to co-register too images and then move the slider to review whole studies by moving the fader between fore- and background. It’s the single most efficient method to review longitudinal changes in patients with numerous brain metastases, or people with large tumors with spatially heterogeneous responses.</p>
<p>I do agree that the handling is tedious but I got it figured. So when I have 1mm slice thickness it would take way too many slices to review a study so I go to Manual slice thickness, turn it to somewhere between 3 and 5mm. THen this doesn’t get applied automatically, so I turn on the lightbox again and it then yields the thicker slices (fewer images laid out). Fiducials and the crosshair don’t work in this mode but it’s still extremely efficient.</p>
<p>I reverted back to the previous mode for now. Perhaps keeping it but hiding it under a menu could provide both simplification in the interface but also would keep this legacy formatting. I’m working on a paper at the moment to show clinical utility of this approach.</p>
<p>Thanks for all the work on these updates / Köszi szépen!</p>
<p>Cheers</p>
<p>Dave</p>

---
