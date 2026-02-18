# Firefox: Discourse shown as blank page -> Tweak "Privacy Badger" extension settings

**Topic ID**: 98
**Date**: 2017-04-13
**URL**: https://discourse.slicer.org/t/firefox-discourse-shown-as-blank-page-tweak-privacy-badger-extension-settings/98

---

## Post #1 by @jcfr (2017-04-13 02:05 UTC)

<p>Hi Folks,</p>
<p>If this website is shown as a blank page using firefox and you have  <a href="https://www.eff.org/privacybadger">privacybadger</a><br>
extension  installed, consider tweaking the parameter as illustrated below:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9fd6cf67577c17ab583374b7efdcf1ebc59c93a2.png" data-download-href="/uploads/short-url/mO0951L4BVNBPQdOEsFRyvoRvOi.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9fd6cf67577c17ab583374b7efdcf1ebc59c93a2_2_432x500.png" alt="image" data-base62-sha1="mO0951L4BVNBPQdOEsFRyvoRvOi" width="432" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9fd6cf67577c17ab583374b7efdcf1ebc59c93a2_2_432x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9fd6cf67577c17ab583374b7efdcf1ebc59c93a2.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9fd6cf67577c17ab583374b7efdcf1ebc59c93a2.png 2x" data-dominant-color="E7E7E5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">471×545 39.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @ihnorton (2017-04-13 02:34 UTC)

<p>Ref:</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/EFForg/privacybadger/issues/1121" target="_blank">github.com/EFForg/privacybadger</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/EFForg/privacybadger/issues/1121" target="_blank">cdn-enterprise.discourse.org's DNT policy not being recognized</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2017-01-05" data-time="01:42:25" data-timezone="UTC">01:42AM - 05 Jan 17 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2017-04-18" data-time="20:14:26" data-timezone="UTC">08:14PM - 18 Apr 17 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/mpalmer" target="_blank">
          <img alt="mpalmer" src="https://avatars2.githubusercontent.com/u/357?v=4" class="onebox-avatar-inline" width="20" height="20">
          mpalmer
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">This is a follow-on to EFForg/privacybadgerfirefox-legacy#490
We've just got another report of problems: https://twitter.com/flobin/status/816726049748910080
I cannot reproduce this issue myself: Privacy Badger considers...</p>
</div>

<div class="labels">
    <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">broken site</span>
    <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">heuristic</span>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>from:</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://d11a6trkgmumsb.cloudfront.net/optimized/3X/b/3/b33be9538df3547fcf9d1a51a4637d77392ac6f9_2_32x32.png" class="site-icon" width="32" height="32">
      <a href="https://meta.discourse.org/t/discourse-cdns-are-blocked-by-privacy-badger/17127/46" target="_blank" title="01:36AM - 05 January 2017">Discourse Meta – 5 Jan 17</a>
  </header>
  <article class="onebox-body">
    <img src="https://d11a6trkgmumsb.cloudfront.net/original/3X/e/c/ecc92a52ee7353e03d5c0d1ea6521ce4541d9c25.png" class="thumbnail onebox-avatar" width="500" height="500">

<h3><a href="https://meta.discourse.org/t/discourse-cdns-are-blocked-by-privacy-badger/17127/46" target="_blank">Discourse CDNs are blocked by privacy badger</a></h3>

<p>Oh, right. Hmmm… the v parameter maybe?  That’d be a real pain if that’s what’s tripping it.  Here’s one of the relevant source files from last time I was investigating this stuff:</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
