# Extension build failures

**Topic ID**: 1274
**Date**: 2017-10-24
**URL**: https://discourse.slicer.org/t/extension-build-failures/1274

---

## Post #1 by @fedorov (2017-10-24 13:55 UTC)

<p>There are new failures in some of the extensions starting from Oct 19 (sorry, I noticed just now). We did not change the extensions code in that period of time, so it must be due to some Slicer changes.</p>
<p>Specifically, DCMQI and PkModeling started to fail (both are superbuild-style extensions).</p>
<p>Last successful dashboard: <a href="http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2017-10-17&amp;filtercombine=or&amp;filtercount=2&amp;showfilters=1&amp;filtercombine=or&amp;field1=buildname&amp;compare1=63&amp;value1=DCMQI&amp;field2=buildname&amp;compare2=63&amp;value2=PkModeling" class="inline-onebox">CDash</a></p>
<p>First time they started to fail: <a href="http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2017-10-19&amp;filtercount=2&amp;showfilters=1&amp;filtercombine=or&amp;field1=buildname&amp;compare1=63&amp;value1=DCMQI&amp;field2=buildname&amp;compare2=63&amp;value2=PkModeling" class="inline-onebox">CDash</a></p>
<p>Specific errors:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54221807384cf4860ffed97e23830125a037b2ae.png" data-download-href="/uploads/short-url/c0h9vc1iPy1OM1gZVgseCdSVBUi.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54221807384cf4860ffed97e23830125a037b2ae_2_690x149.png" alt="image" data-base62-sha1="c0h9vc1iPy1OM1gZVgseCdSVBUi" width="690" height="149" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54221807384cf4860ffed97e23830125a037b2ae_2_690x149.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54221807384cf4860ffed97e23830125a037b2ae_2_1035x223.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54221807384cf4860ffed97e23830125a037b2ae.png 2x" data-dominant-color="EFEFEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1339×290 43.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa4bf4aa7a5cc59c6b175130f9306307f8a5fc6c.png" data-download-href="/uploads/short-url/oivU4oxVGOKyNqbPFxtkoZgiBJy.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa4bf4aa7a5cc59c6b175130f9306307f8a5fc6c_2_690x130.png" alt="image" data-base62-sha1="oivU4oxVGOKyNqbPFxtkoZgiBJy" width="690" height="130" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa4bf4aa7a5cc59c6b175130f9306307f8a5fc6c_2_690x130.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa4bf4aa7a5cc59c6b175130f9306307f8a5fc6c_2_1035x195.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa4bf4aa7a5cc59c6b175130f9306307f8a5fc6c_2_1380x260.png 2x" data-dominant-color="EFEFEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1478×279 44 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>At the same time, the packages appear to be generated.</p>

---

## Post #2 by @ihnorton (2017-10-24 15:35 UTC)

<p>Also seeing this, but only for Mac build (UKFTractography extension).</p>

---

## Post #3 by @fedorov (2017-10-24 15:51 UTC)

<p>For the extensions I mentioned, it is also only Mac builds.</p>

---

## Post #4 by @fedorov (2017-10-25 15:33 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> I did not test, but on the surface at least (the error happens in the fixup_extension step, the specific failure is about not being able to locate the extension dir, the error happens in the superbuild extensions) it looks like this commit is to blame:</p>
<p><a href="https://github.com/Slicer/Slicer/commit/d6c3a2cf4999c4a3eb5dedd974e1f1aa6fd7aac6" class="onebox" target="_blank">https://github.com/Slicer/Slicer/commit/d6c3a2cf4999c4a3eb5dedd974e1f1aa6fd7aac6</a></p>
<p>What do you think?</p>

---

## Post #5 by @markasselin (2017-10-27 01:55 UTC)

<p>In the latest Windows nightly (4.9.0-2017-10-25) I don’t see <em>any</em> extensions at all. Below is a screenshot of what I see.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3d3746e55afc64788b4f5f821bb5a00b286959d.jpeg" data-download-href="/uploads/short-url/yMZ42sL5KBJ2q5dDP5UM3wvV3Yx.jpg?dl=1" title="BrokenExtensionManager" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/f3d3746e55afc64788b4f5f821bb5a00b286959d_2_500x500.jpg" alt="BrokenExtensionManager" data-base62-sha1="yMZ42sL5KBJ2q5dDP5UM3wvV3Yx" width="500" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/f3d3746e55afc64788b4f5f821bb5a00b286959d_2_500x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/f3d3746e55afc64788b4f5f821bb5a00b286959d_2_750x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/f3d3746e55afc64788b4f5f821bb5a00b286959d_2_1000x1000.jpg 2x" data-dominant-color="CDCBCB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">BrokenExtensionManager</span><span class="informations">1043×1041 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @jcfr (2017-10-27 18:01 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="4" data-topic="1274">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>I did not test, but on the surface at least (the error happens in the fixup_extension step, the specific failure is about not being able to locate the extension dir, the error happens in the superbuild extensions) it looks like this commit is to blame:</p>
</blockquote>
</aside>
<p>Thanks for the report. If it hasn’t been addressed yet, I will follow up shortly.</p>

---

## Post #7 by @fedorov (2017-11-04 15:30 UTC)

<p>Unfortunately, the build errors are still there.</p>

---

## Post #8 by @fedorov (2017-11-04 15:31 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> what would be the consequences of reverting the commit that introduced the regression?</p>

---

## Post #9 by @jcfr (2017-11-04 19:51 UTC)

<p>Tackling this now, we should have fix in shortly.</p>

---

## Post #10 by @jcfr (2017-11-04 20:05 UTC)

<p>Problem identified. PR for PkModeling and DCMQI on the way</p>

---

## Post #11 by @jcfr (2017-11-04 20:51 UTC)

<p>PRs fixing DCMQI and PkModeling have been submitted:</p>
<ul>
<li><a href="https://github.com/QIICR/dcmqi/pull/310">https://github.com/QIICR/dcmqi/pull/310</a></li>
<li><a href="https://github.com/millerjv/PkModeling/pull/65">https://github.com/millerjv/PkModeling/pull/65</a></li>
</ul>
<p>Also, Slicer extension build system has been improved to help extension developer diagnose the problem at configuration time. An configure like the following will now be reported:</p>
<pre><code class="lang-auto">NameOfExtension: Variable CPACK_INSTALL_CMAKE_PROJECTS is expected to be set.
</code></pre>
<p><a href="https://github.com/Slicer/Slicer/commit/b160ec13f276a86306513954ef8b08a5332afc2e" class="onebox" target="_blank">https://github.com/Slicer/Slicer/commit/b160ec13f276a86306513954ef8b08a5332afc2e</a></p>

---

## Post #12 by @ihnorton (2017-11-06 15:01 UTC)

<p>Would the value of <code>CPACK_INSTALL_CMAKE_PROJECTS</code> ever be different than in those PRs?</p>

---

## Post #13 by @jcfr (2017-11-06 15:53 UTC)

<aside class="quote no-group" data-username="ihnorton" data-post="12" data-topic="1274" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p>Would the value of CPACK_INSTALL_CMAKE_PROJECTS ever be different than in those PRs?</p>
</blockquote>
</aside>
<p>If the project only includes Slicer modules, it should not be different.</p>
<p>In the case of this PR, we explicitly install the <code>RuntimeLibraries</code> component. Other more complex project could have other components …</p>

---
