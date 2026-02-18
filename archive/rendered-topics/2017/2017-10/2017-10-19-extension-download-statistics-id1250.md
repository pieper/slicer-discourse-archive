# Extension download statistics

**Topic ID**: 1250
**Date**: 2017-10-19
**URL**: https://discourse.slicer.org/t/extension-download-statistics/1250

---

## Post #1 by @gcsharp (2017-10-19 21:30 UTC)

<p>Hi, is it possible to get download statistics for an extension?</p>

---

## Post #2 by @jcfr (2017-10-19 21:34 UTC)

<p>Yes.</p>
<p>You can install this extension and gather the stats of your choice.</p>
<p>See <a href="https://github.com/fbudin69500/SlicerDeveloperToolsForExtensions#slicerdevelopertoolsforextensions">https://github.com/fbudin69500/SlicerDeveloperToolsForExtensions#slicerdevelopertoolsforextensions</a></p>

---

## Post #3 by @muratmaga (2019-06-07 17:51 UTC)

<p>I am looking at the current stats for SlicerMorph, which is only available as part of the preview versions. Download stats shows it as 4.10.2-nightly. Is this referring to the current preview version? Because all previews I installed have names like 4.11.0-some_date?</p>
<p>Also, there was some discussion on developer calls about enabling more stats about extensions (like monthly download stats, os versions they are requested from). Would this be possible sometime?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9b838db243b19e6b5a1466a414880843cc8619c.png" data-download-href="/uploads/short-url/odpnXMVl1vfs3Siie5HIRx0l0cY.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9b838db243b19e6b5a1466a414880843cc8619c.png" alt="image" data-base62-sha1="odpnXMVl1vfs3Siie5HIRx0l0cY" width="690" height="274" data-dominant-color="F1F0F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">909×362 13.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @jcfr (2019-06-07 18:11 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="1250">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>4.10.2-nightly. Is this referring to the current preview version?</p>
</blockquote>
</aside>
<p>yes, may be we could rename this to <code>post-4.10.2</code></p>
<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="1250">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Also, there was some discussion on developer calls about enabling more stats about extensions (like monthly download stats, os versions they are requested from). Would this be possible sometime?</p>
</blockquote>
</aside>
<p>It should be possible. First we need to transition the current infrastructure, I documented the current status and needs on this page: <a href="https://www.slicer.org/wiki/Documentation/Labs/ExtensionsServer" class="inline-onebox">Documentation/Labs/ExtensionsServer - Slicer Wiki</a></p>
<p>If we can allocate resources to support this transition, consolidating the existing download stats with the slicer extension infrastructure so it provides monthly download stats … could be addressed as well.</p>

---
