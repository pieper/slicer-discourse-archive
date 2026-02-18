# Slicer Tractography ROI Selection Not Working

**Topic ID**: 7537
**Date**: 2019-07-11
**URL**: https://discourse.slicer.org/t/slicer-tractography-roi-selection-not-working/7537

---

## Post #1 by @cindy (2019-07-11 18:03 UTC)

<p>Hi. I’ve been following the Slicer tutorial: 5.1.6 Fiber Bundle Volume Measurement</p>
<p>When I try to run tractography ROI selection, I get the following error:</p>
<p>Tractography ROI Selection standard error:</p>
<p>dyld: Library not loaded: /Volumes/Dashboards/Support/qt-everywhere-build-5.10.0/lib/QtSql.framework/Versions/5/QtSql<br>
Referenced from: /Applications/Slicer.app/Contents/Extensions-28371/SlicerDMRI/lib/Slicer-4.11/cli-modules/libFiberBundleLabelSelectLib.dylib<br>
Reason: image not found</p>
<p>I’ve tried redownloading the SlicerDMRI extension, but nothing’s worked so far.</p>

---

## Post #2 by @ljod (2019-07-11 18:21 UTC)

<p>Hi. Could you please try SlicerDMRI in the Slicer release version (4.10.2) and let us know if this works for you?</p>
<p>There is some rapid development happening in the Nightly Preview version so it’s possible something has broken. It looks to be related to Qt, and possibly not directly caused by SlicerDMRI. Did any other modules not work for you in the Preview version?</p>

---

## Post #3 by @cindy (2019-07-11 18:28 UTC)

<p>Hi there! I tried it in the 4.10.2 version as well as the 4.11.0 version but I had the same error message.</p>

---

## Post #4 by @ljod (2019-07-11 18:45 UTC)

<p>Thank you. Could you please help us reproduce this by letting us know which page of the  tutorial you are on and what dataset you used?</p>

---

## Post #5 by @pieper (2019-07-11 18:49 UTC)

<p>I confirm that I got the same error running the CLI with SlicerDMRI on mac with 4.10.2.  It appears to be an extension linking/packaging issue (like SlicerDMRI links to the SQL library but that is not included in Slicer’s distribution).  <a class="mention" href="/u/jcfr">@jcfr</a> do you have any ideas?</p>

---

## Post #6 by @pieper (2019-07-11 19:12 UTC)

<p><a class="mention" href="/u/cindy">@cindy</a> if you have access to a windows machine the same module does work there (4.10.2 SlicerDMRI, probably works on linux too but I didn’t test).</p>

---

## Post #7 by @jcfr (2019-07-11 19:45 UTC)

<aside class="quote no-group" data-username="pieper" data-post="5" data-topic="7537">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>do you have any ideas?</p>
</blockquote>
</aside>
<p>Thanks for letting me know. Looking into it and will report back shortly.</p>

---

## Post #8 by @cindy (2019-07-11 20:23 UTC)

<p>It worked for me on Windows! Thanks <a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #10 by @jcfr (2019-07-11 23:02 UTC)

<p>A regression was introduced back in December. The following PR should fix the problem for Slicer preview build.</p>
<aside class="onebox githubpullrequest">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/pull/1174" target="_blank" rel="nofollow noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
      <a href="https://github.com/jcfr" target="_blank" rel="nofollow noopener">
    <img alt="jcfr" src="https://avatars0.githubusercontent.com/u/219043?v=4" class="thumbnail onebox-avatar" width="90" height="90">
  </a>

<h4>
  <a href="https://github.com/Slicer/Slicer/pull/1174" target="_blank" rel="nofollow noopener">Ensure CLI libraries are fixed up on macOS</a>
</h4>

<div class="date">
  by <a href="https://github.com/jcfr" target="_blank" rel="nofollow noopener">jcfr</a>
  on <a href="https://github.com/Slicer/Slicer/pull/1174" target="_blank" rel="nofollow noopener">10:35PM - 11 Jul 19 UTC</a>
</div>

<div class="github-commit-stats">
  <strong>2 commits</strong>
  changed <strong>2 files</strong>
  with <strong>10 additions</strong>
  and <strong>4 deletions</strong>.
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Once we confirm it works well for the Preview extensions, I will backport the fix into the Slicer 4.10 branch and locally apply the change on the build machine.</p>
<p>Update: Corresponding changes have been integrated into both Slicer and the maintenance branch for Slicer 4.10. Change to the extension build system for Slicer 4.10 have also been applied locally on the build machine.</p>
<p>Extensions made available tomorrow through the extension manager should be valid.</p>

---

## Post #11 by @pieper (2019-07-12 12:02 UTC)

<p>Thanks very much <a class="mention" href="/u/jcfr">@jcfr</a>!</p>

---

## Post #12 by @cindy (2019-07-12 15:02 UTC)

<p>thank you!! this worked for me this morning.</p>

---

## Post #13 by @zhangfanmark (2019-07-16 17:48 UTC)

<p>Hi <a class="mention" href="/u/jcfr">@jcfr</a>  thanks for the fix. The night version works form me, but the Stable Release 4.10 still has the issue: “dyld: Library not loaded: /Volumes/Dashboards/Support/qt-everywhere-build-5.10.0/lib/QtSql.framework/Versions/5/QtSql”.</p>
<p>Regards,<br>
Fan</p>

---

## Post #14 by @jcfr (2019-07-16 21:31 UTC)

<p>Could you check you are using 4.10.2 and not 4.10.1 ?</p>

---

## Post #15 by @zhangfanmark (2019-07-19 18:46 UTC)

<p>Hi <a class="mention" href="/u/jcfr">@jcfr</a></p>
<p>I confirm that I was using 4.10.2. I just installed Slicer 4.10.2 again. It gave me the same error.</p>
<p>But, after looking into the error, I found that the newly installed 4.10.2 was trying to call a lib from another Slicer (4.10.2) installed on my computer. After I removed the old 4.10.2, the tract selection module works now. Perhaps, this is an issue that you have noticed?</p>
<p>Thank you!!!</p>
<p><a class="mention" href="/u/ljod">@ljod</a></p>
<p>Regards,<br>
Fan</p>

---

## Post #16 by @lassoan (2019-07-19 19:12 UTC)

<p>All extensions are shared between all Slicer installations of the same version of the current user. You need to update (or uninstall and install) the <em>extension</em> to update it (Slicer install/uninstall will have no effect).</p>

---
