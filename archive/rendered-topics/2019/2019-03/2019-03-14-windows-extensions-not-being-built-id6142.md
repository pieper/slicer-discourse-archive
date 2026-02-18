# Windows extensions not being built

**Topic ID**: 6142
**Date**: 2019-03-14
**URL**: https://discourse.slicer.org/t/windows-extensions-not-being-built/6142

---

## Post #1 by @jamesobutler (2019-03-14 11:04 UTC)

<p>I’ve noticed that Windows extensions for stable and preview weren’t built during the build process last night or the night before.<br>
<a href="http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2019-03-14" class="onebox" target="_blank" rel="nofollow noopener">http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2019-03-14</a></p>
<p>Also the preview Slicer package for Windows wasn’t uploaded either though the build passed.</p>

---

## Post #2 by @jamesobutler (2019-03-14 16:50 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> Is there an issue with the Windows build machine? Or was the packaging turned off to prioritize Mac/Linux extension builds in the short term?</p>

---

## Post #3 by @jamesobutler (2019-03-15 14:02 UTC)

<p><strong>Update:</strong> Windows related items were built, packaged, and uploaded with last night’s builds. <a href="http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2019-03-15" rel="nofollow noopener">http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2019-03-15</a></p>

---

## Post #4 by @jcfr (2019-03-15 15:43 UTC)

<blockquote>
<p>Is there an issue with the Windows build machine? Or was the packaging turned off to prioritize Mac/Linux extension builds in the short term?</p>
</blockquote>
<p>There are three difference build machine. More details at <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Factory" class="inline-onebox">Documentation/Nightly/Developers/Factory - Slicer Wiki</a></p>
<blockquote>
<p>with last night’s builds</p>
</blockquote>
<p>To follow up, you may also have notice that the revision number is not displayed on the dashboard.  This is because, the regular nightly built on macOS and Linux was disabled, source code manually updated to a version newer than <code>r28019</code> and build manually triggered.</p>
<p>By disabling automatic update, this allowed to make sure the nightly build on macOS would account for changes associated with <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=28020">r28020</a> done after the nightly cut-off time.</p>
<p>The linux failure is unrelated.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1b7932699212e302b204dc5b5066387a9732d2d.png" data-download-href="/uploads/short-url/yuknpsebXqvGEqMv37eBTMD1QE5.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1b7932699212e302b204dc5b5066387a9732d2d_2_690x78.png" alt="image" data-base62-sha1="yuknpsebXqvGEqMv37eBTMD1QE5" width="690" height="78" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1b7932699212e302b204dc5b5066387a9732d2d_2_690x78.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1b7932699212e302b204dc5b5066387a9732d2d_2_1035x117.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1b7932699212e302b204dc5b5066387a9732d2d_2_1380x156.png 2x" data-dominant-color="C7CEC3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1550×176 35.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
