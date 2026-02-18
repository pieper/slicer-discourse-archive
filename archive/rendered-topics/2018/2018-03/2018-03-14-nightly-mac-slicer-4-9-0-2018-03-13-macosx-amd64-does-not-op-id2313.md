# Nightly mac Slicer-4.9.0-2018-03-13-macosx-amd64 does not open

**Topic ID**: 2313
**Date**: 2018-03-14
**URL**: https://discourse.slicer.org/t/nightly-mac-slicer-4-9-0-2018-03-13-macosx-amd64-does-not-open/2313

---

## Post #1 by @pieper (2018-03-14 13:23 UTC)

<p>Message is:</p>
<pre><code class="lang-auto">
Termination Reason:    DYLD, [0x1] Library missing

Application Specific Information:
dyld: launch, loading dependent libraries

Dyld Error Message:
  Library not loaded: @rpath/Frameworks/QtMultimedia.framework/Versions/5/QtMultimedia
  Referenced from: /private/var/folders/*/Slicer.app/Contents/MacOS/Slicer
  Reason: image not found

</code></pre>
<p>All the Slicer.app/Contents/Frameworks/Qt*.framework/Versions/5 directories are empty, whereas in previous builds they include the libraries.</p>

---

## Post #2 by @ihnorton (2018-03-14 13:53 UTC)

<p><s>I wasn’t able to open that package at all from Finder – nothing happened after double-clicking.</s> I was able to load the image successfully with <code>hdiutil attach &lt;Slicer-###.dmg&gt;</code>, and the Qt frameworks seem to be there (Slicer starts ok).</p>

---

## Post #3 by @pieper (2018-03-14 19:27 UTC)

<p><a class="mention" href="/u/ihnorton">@ihnorton</a>  Can you check which version the dmg you are using?  There are two with the same name/data in midas:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0aee37e9df39cc29de74088270a86ebc27b49df4.png" data-download-href="/uploads/short-url/1yH9CY7MNd4VIMCsNMlv1y7tWJu.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0aee37e9df39cc29de74088270a86ebc27b49df4.png" alt="image" data-base62-sha1="1yH9CY7MNd4VIMCsNMlv1y7tWJu" width="690" height="96" data-dominant-color="EDEDED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">725×101 15.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The one with the (1) postfix is the one with the missing frameworks while the other one (from yesterday) does have the frameworks.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd90f9fb545ee0f71c2b14bf86dcb9a426dd01c0.png" data-download-href="/uploads/short-url/vC48a8scfq1VYpXWR6bfDt0kBlm.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd90f9fb545ee0f71c2b14bf86dcb9a426dd01c0_2_690x312.png" alt="image" data-base62-sha1="vC48a8scfq1VYpXWR6bfDt0kBlm" width="690" height="312" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd90f9fb545ee0f71c2b14bf86dcb9a426dd01c0_2_690x312.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd90f9fb545ee0f71c2b14bf86dcb9a426dd01c0_2_1035x468.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd90f9fb545ee0f71c2b14bf86dcb9a426dd01c0.png 2x" data-dominant-color="F0F1F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1131×512 84.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @ihnorton (2018-03-14 19:29 UTC)

<p>The one I have is reported as 295 MB on-disk, so must be the first one.</p>
<p>edit: not sure what happened last time I tried, but just double-clicked the .dmg again, and the <code>open</code> dialog popped right up.</p>

---

## Post #5 by @pieper (2018-03-14 19:30 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> Maybe one of the changes to the dashboard scripts yesterday changed the packaging of Qt frameworks…</p>

---

## Post #6 by @jcfr (2018-03-15 02:35 UTC)

<aside class="quote no-group" data-username="pieper" data-post="5" data-topic="2313">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Maybe one of the changes to the dashboard scripts yesterday changed the packaging of Qt frameworks…</p>
</blockquote>
</aside>
<p>Good point.</p>
<p><strong>Prior</strong> to the update of the scripts, a custom  build of Qt 5.10.0 was used (with complete run time paths). See <a href="https://github.com/Slicer/DashboardScripts/blob/a4b631f3e9b819dbc47acf8a4794cb33b62b8cf0/factory-south-macos-slicer_release_nightly.cmake#L29">here</a>. <strong>After</strong>, a regular install of 5.9.1 was used. See <a href="https://github.com/Slicer/DashboardScripts/blob/5ab84211a80ff3d51eadfd3965cfb068688d54be/factory-south-macos-slicer_preview_nightly.cmake#L32-L33">here</a> (with fixed references to library using <code>@rpath</code>).</p>
<p>This was an oversight that is now <strong>fixed</strong> in  <a href="https://github.com/Slicer/DashboardScripts/commit/877c0ceb7796b33bbfad67b51f469ee21391cae5">Slicer/DashboardScripts@877c0ce</a></p>
<p>Until the improvements of <a class="mention" href="/u/ihnorton">@ihnorton</a> (<a href="https://github.com/Slicer/Slicer/pull/889">Slicer PR#889</a>) are finalized and integrated, on macOS we need to package Slicer using a custom build of Slicer.</p>
<p>In the mean time, anyone can build Qt 5.10.0 on macOS using <a href="https://github.com/jcfr/qt-easy-build" class="inline-onebox">GitHub - jcfr/qt-easy-build: Scripts allowing to easily build Qt with OpenSSL support on Linux, macOS or Windows</a></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e513557841149468f575832806a1adfd2f22964.png" alt="image" data-base62-sha1="8ThAEVbx7P61N4sNm8jPzWFxfzC" width="391" height="105"></p>

---

## Post #7 by @jcfr (2018-03-15 08:25 UTC)

<p>2 posts were split to a new topic: <a href="/t/macos-build-on-the-factory-failed-with-no-java-runtime-present-alarm-clock-14/2321">macOS build on the factory failed with “No Java runtime present … Alarm clock: 14”</a></p>

---
