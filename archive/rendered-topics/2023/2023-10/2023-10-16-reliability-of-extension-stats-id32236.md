# Reliability of extension stats

**Topic ID**: 32236
**Date**: 2023-10-16
**URL**: https://discourse.slicer.org/t/reliability-of-extension-stats/32236

---

## Post #1 by @muratmaga (2023-10-16 03:37 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a></p>
<p>How reliable old download statistics? I just ran the extension download statistics, for all extensions, and why I sort them grand total, I am a little surprised with the some of the top results, such as SlicerXNAT, which I believe is not even maintained.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc2de75650b6500d8596dbad64eaadeea0f61509.png" data-download-href="/uploads/short-url/zYSFA8TpuTZrQfh6VRBWuUFmG01.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc2de75650b6500d8596dbad64eaadeea0f61509_2_325x500.png" alt="image" data-base62-sha1="zYSFA8TpuTZrQfh6VRBWuUFmG01" width="325" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc2de75650b6500d8596dbad64eaadeea0f61509_2_325x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc2de75650b6500d8596dbad64eaadeea0f61509_2_487x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc2de75650b6500d8596dbad64eaadeea0f61509_2_650x1000.png 2x" data-dominant-color="E8E8E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">664×1020 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Most of these packages very high download stats for version 4.10.2 (in the orders of 50-80K), which kind of looked a bit superfluous to me, particularly given their recent usage has been quite low.</p>

---

## Post #2 by @jcfr (2023-10-16 18:46 UTC)

<p>Downloads for both the Slicer built-in extension manager or the corresponding web page loaded in a regular browser are accounted for.</p>
<p>We are not discriminating between both and we are not performing filtering like it has been implemented for the Slicer download packages.</p>
<p>Possible ways to improve this and tease apart the “source” of the download would be to either customize the user agent associated with Slicer built-in browser and/or append a new parameter.</p>

---

## Post #3 by @muratmaga (2023-10-16 19:00 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="2" data-topic="32236">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Downloads for both the Slicer built-in extension manager or the corresponding web page loaded in a regular browser are accounted for.</p>
</blockquote>
</aside>
<p>Oh, I see if the source repo like <a href="https://github.com/MokaCreativeLLC/XNATSlicer">GitHub - MokaCreativeLLC/XNATSlicer: XNAT-Slicer Integration</a> is accessed from a web browser, that still counts as a download?</p>

---

## Post #4 by @lassoan (2023-10-16 20:56 UTC)

<p>I don’t think it is necessary to distinguish download count obtained from the web browser or from the extensions manager. When someone downloads a package via the web browser, the intent is most likely to install it in Slicer.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="32236">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Oh, I see if the source repo like <a href="https://github.com/MokaCreativeLLC/XNATSlicer">GitHub - MokaCreativeLLC/XNATSlicer: XNAT-Slicer Integration</a> is accessed from a web browser, that still counts as a download?</p>
</blockquote>
</aside>
<p>This does not count as a download. Only extension package downloads are counted.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="1" data-topic="32236">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>How reliable old download statistics? I just ran the extension download statistics, for all extensions, and why I sort them grand total, I am a little surprised with the some of the top results, such as SlicerXNAT, which I believe is not even maintained.</p>
</blockquote>
</aside>
<p>The numbers look good to me, I don’t see any reason to doubt their accuracy.</p>
<p>Slicer has a long history, so if a more recently added extension needs to be compared with older ones then you may consider limiting your analysis range to releases from the past few years.</p>

---

## Post #5 by @lassoan (2023-10-16 21:04 UTC)

<p>The main limitation of the download count that it does not reflect usage. For example, a completely useless extension may get larger download count if its name suggests that it could be useful.</p>
<p>We would need to collect usage statistics to more accurately measure impact or usefulness - see <a href="https://discourse.slicer.org/t/should-we-start-collecting-software-usage-data/30873" class="inline-onebox">Should we start collecting software usage data?</a></p>

---

## Post #6 by @jamesobutler (2023-10-16 22:44 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="2" data-topic="32236">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Downloads for both the Slicer built-in extension manager or the corresponding web page loaded in a regular browser are accounted for.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> What is meant by this is that both from within the Extensions Manager web browser inside the 3D Slicer application or from <a href="https://extensions.slicer.org/catalog/All/31938/win" rel="noopener nofollow ugc">https://extensions.slicer.org/catalog/All/31938/win</a> which can be accessed by the instructions at <a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html#download-extension-packages" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html#download-extension-packages</a>.</p>

---

## Post #7 by @pieper (2023-10-16 23:10 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> you just spent a week with a bunch of users at the workshop, did you happen to get a sense of how they would feel about the question of sharing anonymous usage statistics?  If not, could we reach out to them and ask?</p>
<p>I think most people would be okay with something along the lines of the RenderDoc example (<a href="https://discourse.slicer.org/t/should-we-start-collecting-software-usage-data/30873/24" class="inline-onebox">Should we start collecting software usage data? - #24 by jcfr</a>).</p>

---

## Post #8 by @muratmaga (2023-10-16 23:18 UTC)

<p>We did not discuss this (in hindsight would have been a good topic, but then we already have a good sense what modules Slicermorph users are interacting with).</p>
<p>I think most people would be ok with anonymous usage stats provided:</p>
<ol>
<li>It is not intrusive and enabling the telemetry does not slow the work.</li>
<li>Clear indication of they would benefit from this.</li>
</ol>

---
