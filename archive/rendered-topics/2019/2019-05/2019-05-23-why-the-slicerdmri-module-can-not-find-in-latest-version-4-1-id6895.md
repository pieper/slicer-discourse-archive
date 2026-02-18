# Why the "slicerDMRI" module can not find in latest version(4.10.2)

**Topic ID**: 6895
**Date**: 2019-05-23
**URL**: https://discourse.slicer.org/t/why-the-slicerdmri-module-can-not-find-in-latest-version-4-10-2/6895

---

## Post #1 by @Jin (2019-05-23 10:45 UTC)

<p>why the “slicerDMRI” module can not find in latest version(4.10.2), thanks! I can not get the DTI volume and tractography?</p>

---

## Post #2 by @ljod (2019-05-23 11:22 UTC)

<p>Thank you for bringing this to our attention! This should be fixed in the next few days. You can try the nightly version if needed in the meantime.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> Our s4ext  says master version in the ExtensionsIndex but there are old errors in the Slicer4 cdash. How do I make sure 4.10 gets the appropriate updates that we’ve made?</p>

---

## Post #3 by @jamesobutler (2019-05-23 11:45 UTC)

<p>You should update your <a href="https://github.com/Slicer/ExtensionsIndex/blob/4.10/SlicerDMRI.s4ext" rel="nofollow noopener">s4ext</a> in the “4.10” branch of the ExtensionsIndex and probably specify a new branch such as “4.10” within Slicer DMRI that can be used to maintain updates for Slicer 4.10.</p>
<p>The SlicerDMRI master branch currently includes commits related to the new markups API, python 3, etc which will be part of Slicer 5 and not included in the recent Slicer 4.10.2 release. It looks like you will need to start from <a href="https://github.com/SlicerDMRI/SlicerDMRI/commit/9d3e244dcbf2b0222587c0420c1ddcad4c9095d9" rel="nofollow noopener">this commit</a> and pick any later commits that are compatible as part of your new 4.10 branch.</p>
<p>You can <a href="https://github.com/Slicer/ExtensionsIndex/commit/cb5cda2b1ef267de53287918e1c01998115450c1" rel="nofollow noopener">see</a> how MarkupsToModel extension had to create a separate 4.10 branch to stay API compatible.</p>

---

## Post #4 by @ljod (2019-05-23 12:00 UTC)

<p>Of course! Thanks! At first glance I thought it was old fixed markups errors but it’s actually the fixes causing the issue. Thanks for the help.</p>

---

## Post #5 by @Jin (2019-05-23 13:09 UTC)

<p>Thanks a lot! Did you mean the nightly version contains the “slicerDMRI” module?</p>

---

## Post #6 by @ljod (2019-05-23 14:01 UTC)

<p>Yes the nightly contains SlicerDMRI.</p>

---

## Post #7 by @Jin (2019-05-23 14:26 UTC)

<p>Get it! Thanks very much!</p>

---

## Post #8 by @ljod (2019-05-27 10:57 UTC)

<p>Hi! This should be fixed now in 4.10.2.</p>

---
