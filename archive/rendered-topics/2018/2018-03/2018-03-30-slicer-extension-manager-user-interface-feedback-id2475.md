# Slicer Extension Manager: User Interface Feedback

**Topic ID**: 2475
**Date**: 2018-03-30
**URL**: https://discourse.slicer.org/t/slicer-extension-manager-user-interface-feedback/2475

---

## Post #1 by @jcfr (2018-03-30 13:52 UTC)

<p>Hi Slicers,</p>
<p>During the past few months, we have been hard at work crafting what will be the <a href="https://github.com/girder/slicer_package_manager#readme">new backend</a> for managing Slicer (or Slicer-based) application and extension packages.</p>
<p>Later today, <a class="mention" href="/u/pierre-assemat">@Pierre-Assemat</a>  and I will meet with our UI/UX designer at Kitware to discuss the next version of the <strong>extension manager frontend</strong>.</p>
<p>It would be great to collect your input on what worked well and what didn’t regarding the <strong>User Interface</strong>, this will help drive the requirements for the backend and associated infrastructure.</p>
<p>Links:</p>
<ul>
<li><a href="http://slicer.kitware.com/midas3/slicerappstore/?os=win&amp;arch=amd64&amp;revision=26813&amp;category=&amp;search=&amp;layout=layout">Full web page</a></li>
<li>
<a href="http://slicer.kitware.com/midas3/slicerappstore/?os=win&amp;arch=amd64&amp;revision=26813&amp;category=&amp;search=&amp;layout=empty">Minimal web page</a> (similar to what is visible in the extension manager)</li>
</ul>
<p>I created few polls (see below), please consider voting for which pros/cons/feature-request you agree the most. Based on the comment posted, I can definitively update the polls.</p>
<h3>What I like about the current Extension Manager:</h3>
<div class="poll" data-poll-status="open" data-poll-type="multiple" data-poll-name="pros">
<div>
<div class="poll-container">
<ul>
<li data-poll-option-id="032c7f030533e73cd80b129560f79d5a">full text search capabilities</li>
<li data-poll-option-id="471953f6b82e0e28cea846c14da601c6">link to the documentation</li>
<li data-poll-option-id="ff2c8bcb60ba8bae55c6c94072bb9f3b">link to the source code</li>
<li data-poll-option-id="87a2ce58f16338c5d95ab7be939d8e17">icon</li>
<li data-poll-option-id="d52a775c1a65fc1c52f20925f8c0f863">short description</li>
<li data-poll-option-id="f851927855f6d3b36b4e61cd848ff91b">screenshots</li>
<li data-poll-option-id="4b5dc0d470e1c803f1a0f55e192b8bec">possibility to install/download extension inside/outside of Slicer</li>
<li data-poll-option-id="eb08b3b2e358997ae3abfdbe876ac3e2">when using the web version, the URL is updated</li>
</ul>
</div>
<div class="poll-info">
<p>
<span class="info-number">0</span>
<span class="info-text">voters</span>
</p>
</div>
</div>
<div class="poll-buttons">
<a title="Display the poll results">Show results</a>
</div>
</div>
<h3>Issues that impact my user experience:</h3>
<div class="poll" data-poll-status="open" data-poll-type="multiple" data-poll-name="issues">
<div>
<div class="poll-container">
<ul>
<li data-poll-option-id="f3dd1baaa5ebb85a12fb682ea047017b">not all icon are showing up</li>
<li data-poll-option-id="b19a5cb9cb526718c5d747e8ccf72d0a">category are hard to read.  (why <code>Virtual Fracture</code> is in  <code>Examples -&gt; Virtual Fracture</code>)</li>
<li data-poll-option-id="65e79f42af0f6ee38802d80e7853c610">web version doesn’t show the latest available extension for each platform. You have to enter the revision.</li>
</ul>
</div>
<div class="poll-info">
<p>
<span class="info-number">0</span>
<span class="info-text">voters</span>
</p>
</div>
</div>
<div class="poll-buttons">
<a title="Display the poll results">Show results</a>
</div>
</div>
<h3>Feature I wish to have:</h3>
<div class="poll" data-poll-status="open" data-poll-type="multiple" data-poll-name="missing_features">
<div>
<div class="poll-container">
<ul>
<li data-poll-option-id="41797878f089a722b636e9d1c91aec18">sort alphabetically</li>
<li data-poll-option-id="b83a8278addeb65049a0e5fd9d6ff18f">markdown support for description</li>
<li data-poll-option-id="0490f112e26d22b9b641d62ecea8786e">share on social network</li>
<li data-poll-option-id="b1959b8565c3adbc34a1460596fe34cb">licenses used in the extensions are not listed. See <a href="https://issues.slicer.org/view.php?id=2171">#2171</a>
</li>
<li data-poll-option-id="e6eb094622ae0188f7c3775ddb83f808">list of modules bundled in the extension not available</li>
<li data-poll-option-id="062c660ca38ee24bc480a6d71ffd05ce">list of funding grants</li>
<li data-poll-option-id="908b516f867de3d61f6b453b237fec12">include acknowledgments. See <a href="https://issues.slicer.org/view.php?id=3415">#3415</a>
</li>
<li data-poll-option-id="938e7a50efb2bd3830d2f79ef3c954a2">list of associated publications</li>
<li data-poll-option-id="30b573aad4ce59c39ea468021eaca324">add link between <a href="http://download.slicer.org">download.slicer.org</a> and the extension manager</li>
<li data-poll-option-id="81927cc6f014e309bf6c76b17808b4e5">add concept of channels. (possibility to select a channel for installing/downloading extensions uploaded by a user, a lab, …). See <a href="https://issues.slicer.org/view.php?id=2334">#2334</a>
</li>
<li data-poll-option-id="8863a43de3ff2d3c60a592a0ecafb82f">extension should list their dependencies. See <a href="https://issues.slicer.org/view.php?id=3696">#3696</a>
</li>
<li data-poll-option-id="ed20d114d3b4d4c6f09581a541af9503">google analytics</li>
</ul>
</div>
<div class="poll-info">
<p>
<span class="info-number">0</span>
<span class="info-text">voters</span>
</p>
</div>
</div>
<div class="poll-buttons">
<a title="Display the poll results">Show results</a>
</div>
</div>
<h3>What type of stats should we keep around ?:</h3>
<div class="poll" data-poll-status="open" data-poll-type="multiple" data-poll-name="stats_and_rating">
<div>
<div class="poll-container">
<ul>
<li data-poll-option-id="50a5e2a89056aaf53a5167e6ca462923">download count (assuming it is kept around even if the extension is removed)</li>
<li data-poll-option-id="6c38897e6125b05545a6d84873469603">download with IP location, date, time, …</li>
<li data-poll-option-id="d4cd3b8b37d77337a602ce6244eb175d">behavior of the user using Google analytics or pixel beacon (which page, how long, which action, …). User could opt-out.</li>
<li data-poll-option-id="1afbf7ff8643af55d4e11618546adf8e">anonymous “stars” rating</li>
<li data-poll-option-id="6498dfe0e24589a9b0c02c9173c2cc8c">anonymous “+1”</li>
<li data-poll-option-id="b443e4cc897067ac29000925f567abd6">identified “+1” (assuming you can login using Google Account / GitHub / …)</li>
<li data-poll-option-id="452c86516c369539247dee0e5636db59">identified “stars” rating (assuming you can login using Google Account / GitHub / …)</li>
</ul>
</div>
<div class="poll-info">
<p>
<span class="info-number">0</span>
<span class="info-text">voters</span>
</p>
</div>
</div>
<div class="poll-buttons">
<a title="Display the poll results">Show results</a>
</div>
</div>
<p>References:</p>
<ul>
<li>Next generation of the Slicer application and extension package manager:
<ul>
<li><a href="https://github.com/girder/slicer_package_manager#readme">https://github.com/girder/slicer_package_manager#readme</a></li>
<li><a href="http://slicer-package-manager.readthedocs.io">http://slicer-package-manager.readthedocs.io</a></li>
</ul>
</li>
<li>Slicer wiki:
<ul>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ExtensionsManager">https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ExtensionsManager</a></li>
<li><a href="https://www.slicer.org/wiki/Documentation/Labs/ExtensionsFrameworkRoadmap">https://www.slicer.org/wiki/Documentation/Labs/ExtensionsFrameworkRoadmap</a></li>
</ul>
</li>
</ul>

---

## Post #2 by @fedorov (2018-03-30 21:44 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> could you refine the titles for the individual polls?</p>
<p>For example, it is not clear to me what “Pros:” poll title corresponds to. Should that be “What I like about the current Extension Manager:”? Or something else?</p>

---

## Post #3 by @jcfr (2018-03-30 21:48 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="2" data-topic="2475">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>refine the titles for the individual polls</p>
</blockquote>
</aside>
<p>Thanks for the feedback. Let me know what you think.</p>

---

## Post #4 by @fedorov (2018-03-30 21:48 UTC)

<p>Also, suggested additions for the polls (not sure into which category they fall):</p>
<ul>
<li>“stars” for the extensions (to me, this was a very weird feature that no one really used, due to the Midas login it relied upon - it should either be better implemented, or dropped)</li>
<li>“download count” (in most cases, it is bogus, since it shows count only for the given build, so I think it should also be either refined, or removed)</li>
</ul>

---

## Post #5 by @fedorov (2018-03-30 21:51 UTC)

<p>What do you mean by “when using the web version, the URL is updated”?</p>

---

## Post #6 by @jcfr (2018-03-30 22:13 UTC)

<h3><a name="p-10093-stars-rating-1" class="anchor" href="#p-10093-stars-rating-1" aria-label="Heading link"></a>stars rating</h3>
<blockquote>
<p>“stars” for the extensions</p>
</blockquote>
<p>We talked about removing that. And instead, we were thinking to have anonymous “+1” system.</p>
<h3><a name="p-10093-download-stats-2" class="anchor" href="#p-10093-download-stats-2" aria-label="Heading link"></a>download stats</h3>
<p>These data are from our test server.</p>
<blockquote>
<p>“download count” (in most cases, it is bogus, since it shows count only for the given build, so I think it should<br>
also be either refined, or removed)</p>
</blockquote>
<p>In the new backend, download count are kept around  at the release level in a json document. For example, for release, it like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5f6b01ba03f1d9796421259fcbe51c8f7804f2c2.png" data-download-href="/uploads/short-url/dC6CtwWlKi4FTN5cCRcrQiXwwym.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5f6b01ba03f1d9796421259fcbe51c8f7804f2c2.png" alt="image" data-base62-sha1="dC6CtwWlKi4FTN5cCRcrQiXwwym" width="690" height="351" data-dominant-color="FCFCFC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">800×408 11.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and for draft release (aka preview / nightly), we also keep track of it:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d047beaea062348f0edb8b35d001ed49d2436015.png" data-download-href="/uploads/short-url/tIx1DPkrHRSYgO76mPqyr4I8u7H.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d047beaea062348f0edb8b35d001ed49d2436015_2_504x499.png" alt="image" data-base62-sha1="tIx1DPkrHRSYgO76mPqyr4I8u7H" width="504" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d047beaea062348f0edb8b35d001ed49d2436015_2_504x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d047beaea062348f0edb8b35d001ed49d2436015_2_756x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d047beaea062348f0edb8b35d001ed49d2436015.png 2x" data-dominant-color="FCFCFC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">960×951 33.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @jcfr (2018-03-30 22:18 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="5" data-topic="2475" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>What do you mean by “when using the web version, the URL is updated”?</p>
</blockquote>
</aside>
<p>This should illustrate:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a56aba8377940f11aa940bc5b47ef3e4cc0f0dc.png" data-download-href="/uploads/short-url/m1ldIlLc0IK85Gzk6McjRyEa7NO.png?dl=1" title="web-url-updated"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a56aba8377940f11aa940bc5b47ef3e4cc0f0dc_2_690x167.png" alt="web-url-updated" data-base62-sha1="m1ldIlLc0IK85Gzk6McjRyEa7NO" width="690" height="167" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a56aba8377940f11aa940bc5b47ef3e4cc0f0dc_2_690x167.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a56aba8377940f11aa940bc5b47ef3e4cc0f0dc_2_1035x250.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a56aba8377940f11aa940bc5b47ef3e4cc0f0dc.png 2x" data-dominant-color="DDE3DC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">web-url-updated</span><span class="informations">1116×271 49 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @fedorov (2018-03-31 00:37 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="6" data-topic="2475">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>instead, we were thinking to have anonymous “+1” system.</p>
</blockquote>
</aside>
<p>Would be cool if instead the users werr authenticated against Slicer discourse.</p>

---

## Post #9 by @lassoan (2018-03-31 01:21 UTC)

<p>+1 is about the same as download count. Anonymous star system is not really good, as people may want to change their star rating.</p>
<blockquote>
<p>“download count” (in most cases, it is bogus, since it shows count only for the given build, so I think it should also be either refined, or removed)</p>
</blockquote>
<p>Yes, download count of specific nightly builds don’t tell much, but you can get download count summed for a range of releases using DeveloperToolsForExtensions extension. I find extension download count to be a very important metric.</p>

---

## Post #10 by @lassoan (2018-03-31 01:40 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="8" data-topic="2475">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>users werr authenticated against Slicer discourse</p>
</blockquote>
</aside>
<p>GitHub would be even better, because you can log on to Discourse (and access many other Slicer resources) with your GitHub account, but you cannot do much else with a Discourse account.</p>

---

## Post #11 by @jcfr (2018-03-31 01:49 UTC)

<blockquote>
<p>Yes, download count of specific nightly builds don’t tell much, but you can get download count summed for a range of releases</p>
</blockquote>
<p>The good news is that we the new backend already has <a href="https://github.com/girder/slicer_package_manager/blob/79cef92ba59e8a1821d0995d0a0cda2019cc2f8e/server/api/app.py#L48">an endpoint</a> to the get the stats. It turn a maps of stats for each revision.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/436f277c9e19b788276987cb6180dcd832cfcc2d.png" data-download-href="/uploads/short-url/9Cy8w8pVuMY9AuR13wLnmi8uaE5.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/436f277c9e19b788276987cb6180dcd832cfcc2d_2_583x500.png" alt="image" data-base62-sha1="9Cy8w8pVuMY9AuR13wLnmi8uaE5" width="583" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/436f277c9e19b788276987cb6180dcd832cfcc2d_2_583x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/436f277c9e19b788276987cb6180dcd832cfcc2d.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/436f277c9e19b788276987cb6180dcd832cfcc2d.png 2x" data-dominant-color="EBECE1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">870×746 37.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Or you could get the the stats for all releases using <code>GET /app/{app_id}/release</code>. These include download count for both application and extension packages.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/436f277c9e19b788276987cb6180dcd832cfcc2d.png" data-download-href="/uploads/short-url/9Cy8w8pVuMY9AuR13wLnmi8uaE5.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/436f277c9e19b788276987cb6180dcd832cfcc2d_2_583x500.png" alt="image" data-base62-sha1="9Cy8w8pVuMY9AuR13wLnmi8uaE5" width="583" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/436f277c9e19b788276987cb6180dcd832cfcc2d_2_583x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/436f277c9e19b788276987cb6180dcd832cfcc2d.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/436f277c9e19b788276987cb6180dcd832cfcc2d.png 2x" data-dominant-color="EBECE1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">870×746 37.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @jcfr (2018-03-31 01:56 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="2475">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>GitHub would be even better, because you can log on to Discourse</p>
</blockquote>
</aside>
<p>There is officially <a href="http://girder.readthedocs.io/en/latest/plugins.html#google">support for Google Auth</a>, and available implementation for few others including GitHub:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/1829fc8e09cc156f8adb3fff8b0753c153d961fe.png" alt="image" data-base62-sha1="3rLpJqkDvypi0AT4PAitgXYOLwO" width="564" height="445"></p>

---

## Post #13 by @dzenanz (2018-03-31 14:34 UTC)

<p>It is not easy to grade extensions on a 1-5 scale, so I am for +1 system. On the web, the user should have to log in using OAuth (Google, GitHub and perhaps a few more). But it should be possible to vote using the extension manager built into Slicer. Otherwise there is not going to be a lot of votes.</p>

---

## Post #14 by @lassoan (2018-03-31 15:05 UTC)

<p>We can define what we mean by each star (1-does not work at all; 3 - somewhat useful; 5 - very useful and easy to use). I’m not sure even this would be specific enough - probably getting separate stats for functionality, robustness, ease of use, documentation, etc. would be much better. It is also not trivial what would be the effect if somebody got bad ratings.</p>
<p>+1 should give info about how frequently used and useful an extension is - which I think is about the same information as download count.</p>

---

## Post #15 by @fedorov (2018-04-02 13:23 UTC)

<p>+1 for 5-star rating. It provides more info than “thumbs up”, and I don’t think there is a need to provide any definitions - it will be hard to find someone who did not use 5-star rating in mobile phone store apps, in Amazon, etc.</p>
<p>The idea to authenticate with Slicer Discourse directly was to link the slicer community specifically with the rating process.</p>

---

## Post #16 by @jamesobutler (2018-04-02 16:46 UTC)

<p>As an end user, if I was to even provide a rating for an extension it would probably be a 1 or 5. I feel like no one will provide 2 or 4 star reviews which is behavior you can usually observe on app stores or amazon pages. I would want to know with a description why someone gave a 2 versus a 1 if that was an option. Also, I would need explicit descriptions like Andras mentioned so that I could match what developers interpret a 3-star review to mean otherwise it’s a little hand wavy.</p>

---

## Post #17 by @fedorov (2018-04-02 17:00 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="16" data-topic="2475">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>otherwise it’s a little hand wavy</p>
</blockquote>
</aside>
<p>IMHO, ratings are hand-wavy by definition …</p>

---

## Post #18 by @jamesobutler (2018-04-02 18:34 UTC)

<p>True, ratings are hand-wavy by definition.  I think you’re going to have people rate only if they have a strong opinion hence 1 and 5 star ratings probably being the most popular.  There would probably be more response by the casual users if the rating system was within the module somewhere instead of having to go back to the extension manager, search for the extension, and then provide the rating. As an end-user, I’d rather have a more curated experience with a most popular/featured section to guide me into picking which extensions to download instead of looking at the ratings.</p>
<p>I know many casual users are completely unaware of the extension manager.  Those that do find it might provide 1-stars simply because the extensions usually have very few helpful screenshots and <strong>most importantly</strong> there’s very rarely any type of documentation associated with how to use the features offered in the extension (this plagues some core modules too). If I don’t know how to use an extension, I’m likely going to give it a 1-star. I know documentation is boring to write, but it really impacts if I’m going to continue to use the module/extension or just give up.</p>
<p>Would a 1-star rating(or down vote) due to a user-found bug or lack of functionality be cleared when the developer updates the extension?  Would there be enough ratings to support clearing an extension’s rating every time it has an update? Would there be an easy communication channel(more like discourse and less github-issue based) between a user and the developer of the extension for questions how to use the extension/bug fixes/feature requests?</p>

---

## Post #19 by @ihnorton (2018-04-03 13:27 UTC)

<p>A post was merged into an existing topic: <a href="/t/trouble-with-extension-manager/2457">Trouble with Extension Manager</a></p>

---

## Post #20 by @fedorov (2018-04-03 14:23 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="1" data-topic="2475">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Feature I wish to have:</p>
</blockquote>
</aside>
<p>Sounds like proxy option should be added to the list in the poll above.</p>

---
