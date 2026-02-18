# Sequence Registration - problem with menu

**Topic ID**: 41294
**Date**: 2025-01-26
**URL**: https://discourse.slicer.org/t/sequence-registration-problem-with-menu/41294

---

## Post #1 by @eNable_Polska (2025-01-26 18:44 UTC)

<p>Hello<br>
I came across a problem that I can’t solve.<br>
I have a sequential angioCT scan. I would like to make a 4D animation based on this scan. I found a tutorial <a href="https://youtu.be/qVgXdXEEVFU?si=ODlaC4UDf2wQ3bCW" rel="noopener nofollow ugc">https://youtu.be/qVgXdXEEVFU?si=ODlaC4UDf2wQ3bCW</a> up to 0:56 everything works fine.<br>
Unfortunately when I open the Sequence Registration module I don’t see the preset or Advance options and I can’t do anything further. I am working on version 5.6.2 in linux and windows, I also checked the latest version 5.8 and there is exactly the same problem. I am attaching a screenshot of the menu shown in the tutorial and what I have.<br>
Youtube<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48858bab0f90b953975883f5a95a4ae6fa4e2857.png" data-download-href="/uploads/short-url/alyuS8LxAzggxbESZVgjcC9djSf.png?dl=1" title="ScreenYoutube" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48858bab0f90b953975883f5a95a4ae6fa4e2857.png" alt="ScreenYoutube" data-base62-sha1="alyuS8LxAzggxbESZVgjcC9djSf" width="472" height="282"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ScreenYoutube</span><span class="informations">472×282 40 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Slicer<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/46df9d561eaade252bbb80bc7e23de8d5072b7a1.png" data-download-href="/uploads/short-url/a6YvVD6ynqD0mfdovWoSFi14A8N.png?dl=1" title="ScreenSlicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46df9d561eaade252bbb80bc7e23de8d5072b7a1_2_690x419.png" alt="ScreenSlicer" data-base62-sha1="a6YvVD6ynqD0mfdovWoSFi14A8N" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46df9d561eaade252bbb80bc7e23de8d5072b7a1_2_690x419.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/46df9d561eaade252bbb80bc7e23de8d5072b7a1.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/46df9d561eaade252bbb80bc7e23de8d5072b7a1.png 2x" data-dominant-color="EAEAEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ScreenSlicer</span><span class="informations">705×429 19.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Can I ask for help in solving this problem?</p>

---

## Post #2 by @eNable_Polska (2025-02-05 18:19 UTC)

<p>Is there really no one who can explain to me how to solve my problem? Please help.</p>

---

## Post #3 by @SassanHashemi (2025-03-07 15:27 UTC)

<p>Having the same issue after installing Slicer on a new machine. Looks like the screenshot above both on 5.8.1 and 5.6.2.</p>
<p>Sassan</p>

---

## Post #4 by @mikebind (2025-03-10 01:28 UTC)

<p>Sequence Registration uses Elastix, perhaps you don’t have the SlicerElastix extension installed?</p>

---

## Post #5 by @cpinter (2025-03-10 10:52 UTC)

<p>I just faced the same issue. If you look at the Python console I suppose you’ll also see an error, which causes the setup of the module to fail and thus only a part of the UI is generated.</p>
<p>The problem is that there has been a refactoring done in SlicerElastix around the preset loading/saving, which is not compatible any more with the Sequence Registration module. There is a fix already done, but in a private fork, which (as I was told) cannot get integrated until a certain publication.</p>
<p>Maybe <a class="mention" href="/u/mattjolley">@mattjolley</a> or <a class="mention" href="/u/che85">@che85</a> or <a class="mention" href="/u/lassoan">@lassoan</a> can tell you more about expected ETA.</p>

---

## Post #6 by @lassoan (2025-03-11 01:09 UTC)

<p>You can monitor the status of this issue here:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/moselhy/SlicerSequenceRegistration/issues/9">
  <header class="source">

      <a href="https://github.com/moselhy/SlicerSequenceRegistration/issues/9" target="_blank" rel="noopener">github.com/moselhy/SlicerSequenceRegistration</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/moselhy/SlicerSequenceRegistration/issues/9" target="_blank" rel="noopener">Incompatibility with Elastix</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2025-03-10" data-time="17:02:39" data-timezone="UTC">05:02PM - 10 Mar 25 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/swampl" target="_blank" rel="noopener">
          <img alt="" src="https://avatars.githubusercontent.com/u/161310933?v=4" class="onebox-avatar-inline" width="20" height="20">
          swampl
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">The last update in Elastix has changed the syntax for RegistrationPresets, which<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> is not yet reflected in the code of SequenceRegistration (see specifically lines 111 and 353 of SequenceRegistration.py: "...Elastix.RegistrationPresets_Modality").
I guess, it requires updating the respective parts with "self.refreshRegistrationPresetList()" or similar.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
