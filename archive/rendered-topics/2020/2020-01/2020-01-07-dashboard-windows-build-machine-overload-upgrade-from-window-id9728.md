# Dashboard: windows build machine overload upgrade from Windows 7 to Windows 10

**Topic ID**: 9728
**Date**: 2020-01-07
**URL**: https://discourse.slicer.org/t/dashboard-windows-build-machine-overload-upgrade-from-windows-7-to-windows-10/9728

---

## Post #1 by @jcfr (2020-01-07 17:51 UTC)

<p>Later today, we will put the associated server offline and update the operating system from Windows 7 to Windows 10.</p>
<p>If for some reason the update is not completed before the nightly build are expected to start, we will post update here.</p>

---

## Post #2 by @jamesobutler (2020-01-07 18:21 UTC)

<p>Feel free to mark complete the Windows 7 to Windows 10 To-Do action in <a href="https://github.com/Slicer/DashboardScripts/pull/25" rel="nofollow noopener">https://github.com/Slicer/DashboardScripts/pull/25</a> whenever the transition is finished.</p>

---

## Post #3 by @jcfr (2020-01-07 21:35 UTC)

<p>The upgrade has being delayed by some unforeseen error (see below)</p>
<p>After backing up the system, Kitware system administrators will apply relevant workarounds.</p>
<p>This means <strong>tonight windows build may be delayed or skipped.</strong></p>
<p>Thanks for your patience,</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bbab03ba65caaefa1bd1b95c3267f9a27cd11c38.png" data-download-href="/uploads/short-url/qMbGpeQvgo1ZhoQbpesguBVqPIA.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bbab03ba65caaefa1bd1b95c3267f9a27cd11c38.png" alt="image" data-base62-sha1="qMbGpeQvgo1ZhoQbpesguBVqPIA" width="625" height="500" data-dominant-color="E1E3E5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">752×601 13.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @jcfr (2020-01-09 00:33 UTC)

<p>We were not able to do an upgrade from Windows 7 to Windows 10, we are currently backing up some of the data and will proceed to clean install tomorrow.</p>
<p>Tonight windows build should happen as expected.</p>

---

## Post #5 by @lassoan (2020-01-13 17:28 UTC)

<p>I still don’t see any dashboard submission from Windows. Can it be still due to the server upgrade or other reasons (ITK5 or other recent changes)?</p>

---

## Post #6 by @Sam_Horvath (2020-01-13 17:48 UTC)

<p>The server upgrade is in progress, regular windows dashboard build have not resumed yet.</p>

---

## Post #7 by @muratmaga (2020-01-20 21:53 UTC)

<p>Any updates on this? The windows preview version is still from 1/9.</p>

---

## Post #8 by @jcfr (2020-01-20 22:05 UTC)

<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> and I discussed today while attending the project week, and we should have update shortly.</p>

---

## Post #9 by @Sam_Horvath (2020-01-21 12:40 UTC)

<p>The factory machine update is complete, and barring any errors, we should have a new Windows build by the end of the day.</p>
<p>Build in progress:  <a href="http://slicer.cdash.org/buildSummary.php?buildid=1803380" rel="nofollow noopener">http://slicer.cdash.org/buildSummary.php?buildid=1803380</a></p>

---

## Post #10 by @jamesobutler (2020-01-21 19:52 UTC)

<p>There was package errors seen <a href="http://slicer.cdash.org/viewBuildError.php?buildid=1803380" rel="nofollow noopener">here</a> which seem to read as NSIS isn’t installed on the build machine. Likely wasn’t reinstalled following the upgrade to Windows 10.</p>

---
