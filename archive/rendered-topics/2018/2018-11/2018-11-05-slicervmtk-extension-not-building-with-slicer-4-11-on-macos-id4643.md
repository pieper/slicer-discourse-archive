---
topic_id: 4643
title: "Slicervmtk Extension Not Building With Slicer 4 11 On Macos"
date: 2018-11-05
url: https://discourse.slicer.org/t/4643
---

# SlicerVMTK extension not building with Slicer 4.11 on MacOS

**Topic ID**: 4643
**Date**: 2018-11-05
**URL**: https://discourse.slicer.org/t/slicervmtk-extension-not-building-with-slicer-4-11-on-macos/4643

---

## Post #1 by @mschumaker (2018-11-05 18:46 UTC)

<p>On CDash, the SlicerVMTK extension stopped building after Slicer and VTK changes on Oct 1. All platforms are affected: <a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2018-11-05&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=VMTK" rel="nofollow noopener">http://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2018-11-05&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=VMTK</a></p>
<p>On Oct 1 and earlier, there were packaging problems with macOS: <a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2018-10-01&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=VMTK" rel="nofollow noopener">http://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2018-10-01&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=VMTK</a></p>
<p>This error looks similar to errors reported earlier: <a href="https://discourse.slicer.org/t/vmtk-vessel-filtering-not-working/1263/5?u=mschumaker">VMTK vessel filtering not working</a></p>
<p>I have a PR in SlicerExtension-VMTK, but it doesn’t address either of these issues. I don’t understand the build well enough yet to fix these. Help?</p>

---

## Post #2 by @lassoan (2018-11-06 04:09 UTC)

<p>I’ve fixed the build errors on Windows (probably it fixes the same issue on other platforms, too). I’ve submitted a pull request to upstream VMTK (<a href="https://github.com/vmtk/vmtk/pull/317">https://github.com/vmtk/vmtk/pull/317</a>), and until the changes are integrated, I’ve updated Slicer VMTK extension to use my fork of VMTK instead (that contains the fix).</p>

---

## Post #3 by @mschumaker (2018-11-06 19:02 UTC)

<p>Thank you very much for that, Andras. I’ll change my Sept4-application-superbuild-fix branch to use your VMTK fix, and try it.<br>
Looking at CDash, your VMTK fix has resolved the recent errors. The problem with accessing the VMTK shared object libraries on MacOS is still there, unfortunately.<br>
Thanks again!</p>

---

## Post #4 by @jcfr (2018-11-07 06:19 UTC)

<p>In the mean time, I merged <a href="https://github.com/vmtk/SlicerExtension-VMTK/pull/15">https://github.com/vmtk/SlicerExtension-VMTK/pull/15</a>, we can revisit after upstream vmtk is updated.</p>

---

## Post #5 by @mschumaker (2018-11-08 19:39 UTC)

<p>That’s excellent, thanks <a class="mention" href="/u/jcfr">@jcfr</a>.</p>
<p>Do you know what may be causing the build errors on Mac?<br>
<a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=VMTK" class="onebox" target="_blank" rel="nofollow noopener">http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=VMTK</a></p>

---

## Post #6 by @mschumaker (2018-11-16 21:24 UTC)

<p>I added an issue to SlicerExtension-VMTK.</p><aside class="onebox githubissue" data-onebox-src="https://github.com/vmtk/SlicerExtension-VMTK/issues/16">
  <header class="source">

      <a href="https://github.com/vmtk/SlicerExtension-VMTK/issues/16" target="_blank" rel="noopener nofollow ugc">github.com/vmtk/SlicerExtension-VMTK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/vmtk/SlicerExtension-VMTK/issues/16" target="_blank" rel="noopener nofollow ugc">Slicer extension fails on MacOS</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2018-11-16" data-time="21:22:56" data-timezone="UTC">09:22PM - 16 Nov 18 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2019-07-13" data-time="15:41:25" data-timezone="UTC">03:41PM - 13 Jul 19 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/mschumak" target="_blank" rel="noopener nofollow ugc">
          <img alt="mschumak" src="https://avatars.githubusercontent.com/u/3884360?v=4" class="onebox-avatar-inline" width="20" height="20">
          mschumak
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This issue may be similar to the previous issue https://github.com/vmtk/SlicerEx<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">tension-VMTK/issues/11 with building and packaging the Slicer extension for MacOS. The extension currently fails to build/package on MacOS. 
Before the move from Slicer 4.8 to 4.10, Oct 17, SlicerVMTK could build with MacOS, but not the others: http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2018-10-17&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=vmtk
Problems building for all OS for Slicer 4.10 from Oct 18 to Nov 5, then only build errors for MacOS: http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2018-11-06&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=vmtk</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
