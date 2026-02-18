# Add number of extension installations to extension manager

**Topic ID**: 18847
**Date**: 2021-07-21
**URL**: https://discourse.slicer.org/t/add-number-of-extension-installations-to-extension-manager/18847

---

## Post #1 by @brhoom (2021-07-21 08:10 UTC)

<ul>
<li>In extension manager when a user installs an extension, it would be nice to add a counter that tracks the number of installations e.g. next to the stars vote.</li>
<li>It would be nice if the counter also tracks other dependant extensions.</li>
</ul>
<p>This will help to show if a plugin is active and give some useful realistic statistical feedback.</p>

---

## Post #2 by @pieper (2021-07-21 12:14 UTC)

<p>That’s a good idea.  We have been tracking extension installations internally so that extension authors and quote the figures in grant applications and progress reports, but yes, it would be even better if the figures were available to users as well.  <a class="mention" href="/u/jcfr">@jcfr</a> has been completely revamping the extension server infrastructure so let’s finish that up but once that is done it should be easier for someone to contribute this upgrade.</p>

---

## Post #3 by @lassoan (2021-07-21 12:48 UTC)

<p>You can use DeveloperToolsForExtensions extension to query download counts from the current extension server.</p>

---

## Post #4 by @jamesobutler (2021-07-21 12:54 UTC)

<p>Yes you can use DeveloperToolsForExtensions to generate download counts. Here is what the results reveal for SlicerCochlea for example. I removed earlier versions (before 4.8.0) where there were no downloads since it was not available then.</p>
<p>This only provides details about downloads which is not necessarily unique users. People could uninstall/reinstall, download using different machines (work and home), and download using different versions of Slicer.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d5c2317652ac3a0de46075b151b89fa66152f42.png" data-download-href="/uploads/short-url/4bJfsL8OGbm3dgUqJ7ge1S61twS.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d5c2317652ac3a0de46075b151b89fa66152f42.png" alt="image" data-base62-sha1="4bJfsL8OGbm3dgUqJ7ge1S61twS" width="690" height="305" data-dominant-color="F4F7FA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">932×412 6.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @pieper (2021-07-21 13:27 UTC)

<p>I believe <a class="mention" href="/u/brhoom">@brhoom</a> was suggesting these numbers be included in the Extension Manager dialog, which should be quite doable.</p>

---

## Post #6 by @jamesobutler (2021-07-21 13:44 UTC)

<p>Is the motivation to put them in the Extensions Manager for Developer insight? Or user insight?</p>

---

## Post #7 by @pieper (2021-07-21 13:49 UTC)

<p>Probably convenience for both, to build an awareness of what people are finding interesting and useful.  Like pypi and npm where they provide download stats and you get a sense of whether a package is new or well established and popular.</p>

---

## Post #8 by @brhoom (2021-07-21 14:02 UTC)

<p>Thank you all for your replies.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="6" data-topic="18847" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Is the motivation to put them in the Extensions Manager for Developer insight? Or user insight?</p>
</blockquote>
</aside>
<p>Both!</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="4" data-topic="18847">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Here is what the results reveal for SlicerCochlea for example</p>
</blockquote>
</aside>
<p>Are these numbers realistic? if the <a href="https://slicer.cdash.org/" rel="noopener nofollow ugc">cdash testing process</a> is included then these numbers are not realistic.</p>

---

## Post #9 by @lassoan (2021-07-21 19:38 UTC)

<aside class="quote no-group" data-username="brhoom" data-post="8" data-topic="18847">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/brhoom/48/1228_2.png" class="avatar"> brhoom:</div>
<blockquote>
<p>Are these numbers realistic? if the <a href="https://slicer.cdash.org/">cdash testing process </a> is included then these numbers are not realistic.</p>
</blockquote>
</aside>
<p>Yes, the numbers are correct. CDash tests do not download any extensions from the extension server (all the extensions upload and download tests use a local mock server).</p>

---

## Post #10 by @muratmaga (2021-07-21 19:48 UTC)

<p>I am not sure if they are on the roadmap of the new extension mechanism, but I would like to remind about these two requests (second should have been renamed more like “reminder for available updates”).</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5469">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5469" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5469" target="_blank" rel="noopener nofollow ugc">Add last modified date for extensions.</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-02-18" data-time="18:13:24" data-timezone="UTC">06:13PM - 18 Feb 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/muratmaga" target="_blank" rel="noopener nofollow ugc">
          <img alt="muratmaga" src="https://avatars.githubusercontent.com/u/21285140?v=4" class="onebox-avatar-inline" width="20" height="20">
          muratmaga
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:enhancement
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">As I described in [forum topic](https://discourse.slicer.org/t/please-add-last-m<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">odified-date-for-extensions/16052), it will be good to have last revision date to be displayed in the Extension information. Revision number itself is not all that helpful to see if you are using the latest version of the extension.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5470">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5470" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5470" target="_blank" rel="noopener nofollow ugc">Add "Update Extension" option under Manage Extensions </a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-02-18" data-time="18:23:30" data-timezone="UTC">06:23PM - 18 Feb 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/muratmaga" target="_blank" rel="noopener nofollow ugc">
          <img alt="muratmaga" src="https://avatars.githubusercontent.com/u/21285140?v=4" class="onebox-avatar-inline" width="20" height="20">
          muratmaga
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:enhancement
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">An addition the issue #5469, i think it would be good to have a mechanism to let<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> users know when their installed extensions become stale for the stable versions. Something like this would be a good way:

![image](https://user-images.githubusercontent.com/21285140/108403161-45eb0380-71d3-11eb-8ca3-26cac3d33cbc.png)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #11 by @jamesobutler (2021-07-21 21:21 UTC)

<aside class="quote no-group" data-username="brhoom" data-post="8" data-topic="18847">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/brhoom/48/1228_2.png" class="avatar"> brhoom:</div>
<blockquote>
<p>Are these numbers realistic? if the <a href="https://slicer.cdash.org/" rel="noopener nofollow ugc">cdash testing process </a> is included then these numbers are not realistic.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/brhoom">@brhoom</a> Are you surprised by the results? Are they higher than you would have expected?</p>

---

## Post #12 by @brhoom (2021-07-22 06:54 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="11" data-topic="18847">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p><a class="mention" href="/u/brhoom">@brhoom</a> Are you surprised by the results? Are they higher than you would have expected?</p>
</blockquote>
</aside>
<p>somehow! it seems the reason is clear:</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="4" data-topic="18847">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>This only provides details about downloads which is not necessarily unique users. People could uninstall/reinstall, download using different machines (work and home), and download using different versions of Slicer.</p>
</blockquote>
</aside>

---

## Post #13 by @lassoan (2021-07-22 11:39 UTC)

<p>Download statistics show how much people are interested in trying your extension. It shows how well your advertise your extension with its name, icon, description, documentation, posts on discourse, social media, etc.</p>
<p>We don’t have direct usage statistics of Slicer and extensions. It would require implementing data collection, prompt users to opt in, set up the storage backend, and a frontend to access the results. With the new extension manager and Slicer download page, we are one step closer to have a backend that could store the information,but there is still a lot to do.</p>

---

## Post #14 by @muratmaga (2021-07-22 17:50 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="13" data-topic="18847">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Download statistics show how much people are interested in trying your extension</p>
</blockquote>
</aside>
<p>I should add that, while download stats might have the confounding issues <a class="mention" href="/u/jamesobutler">@jamesobutler</a> mentioned, they cannot be happening all the time for all users. So while we may not knowing the exact user count, a continuous download trend indicates a sustained core group of users/usage, which very important for any kind of funding.</p>

---

## Post #15 by @jamesobutler (2021-07-22 17:55 UTC)

<p>If I create a bot that makes web requests to download an extension some amount of times on a schedule, I could in theory greatly influence a result to make it appear that an extension is more popular than it actually is.</p>

---

## Post #16 by @muratmaga (2021-07-22 18:43 UTC)

<p>You sure can. But an obscure extension with off the roof download statistics will not get you the funding, at least not from major funding institutions. While the download stats are important, it is not the only thing that matters.</p>
<p>But i get your point, it is hard to document real usage. More real time tracking is not reliable solution either. For example my institutions network policy blocks all outgoing ports. So you might have slicer working on every single hospital computer, but wouldn’t get a single hit.</p>

---

## Post #17 by @lassoan (2021-07-22 22:02 UTC)

<p>To move this discussion beyond speculation and hypotheses, have a look at the <a href="https://1drv.ms/x/s!Arm_AFxB9yqHxeYAKv8Sf5RS6lOxLw?e=fTyFKw">all-time download statistics of all extensions in this excel sheet</a> (compiled in May 2021).</p>
<p>There are some very surprising numbers. The absolute numbers seem to be heavily influenced by the extension’s name and icon, maybe also by description and documentation, because very important and widely used and advertised extensions fall behind compared to some much “better” ones.</p>
<p>However, even though there are big outliers and some surprising numbers, the magnitude of the download count is informative. Also, download trends for an extension is useful information, too.</p>

---

## Post #18 by @muratmaga (2021-07-22 22:24 UTC)

<p>This is very useful and definitely interesting. SlicerXNAT hasn’t been touched in quite a few years, and was definitely surprising for me to see as one of the top total downloads.</p>
<p>SlicerMorph bundles a number of other extensions, so they might be increasing the their total count. These are:<br>
IGT, SegmentEditorExtraEffects, SurfaceWrapSolidy, DCM2NIIX, auto3DGM, sandbox and rawimageguess.</p>

---

## Post #19 by @jamesobutler (2021-07-22 22:24 UTC)

<p>Interesting that your stats from May 2021 show SlicerCochlea at 260 downloads for Slicer 4.11.20210226, while the stats I generated the other day showed that version as having a little over 2000 downloads. That’s quite the increase from May to July (now).</p>
<p><a class="mention" href="/u/brhoom">@brhoom</a> Does this match behavior that you are aware of? Has your increase of this extension gone up since May?</p>
<p>The over 5000 count for Slicer 4.10.2 matches and so does the over 3000 count for post-4.10.2.</p>

---

## Post #20 by @rbumm (2021-07-23 07:05 UTC)

<p>Very interesting. In extensions: Would it be allowed (theoretically)  to implement a “send usage statistics” checkbox or even include parameter feedback (f.e. thresholds used, training data etc) back to a central server?</p>

---

## Post #21 by @brhoom (2021-07-23 07:19 UTC)

<blockquote>
<p><a class="mention" href="/u/brhoom">@brhoom</a> Does this match behavior that you are aware of? Has your increase of this extension gone up since May?</p>
</blockquote>
<p>I think the extension has some issues with Slicer 4.11. I already added many new functionalities and I am planning to update the extension soon.</p>

---

## Post #22 by @pieper (2021-07-23 11:43 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="20" data-topic="18847">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>In extensions: Would it be allowed (theoretically) to implement a “send usage statistics” checkbox or even include parameter feedback (f.e. thresholds used, training data etc) back to a central server?</p>
</blockquote>
</aside>
<p>I don’t see why not, as long as the users were informed of it.  We’d need to be sure to follow best practices about opting in and so forth.  <a class="mention" href="/u/muratmaga">@muratmaga</a> and I had discussed and prototyped a “SlicerAnalytics” module that observed Slicer activity and reported back to google analytics but didn’t take it very far.  It wasn’t clear how much to report and google analytics is probably not the right server but in principle it could be done.</p>

---
