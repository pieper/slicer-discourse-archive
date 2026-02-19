---
topic_id: 935
title: "Extension Build Failure On Mac Due To Error Copying Files"
date: 2017-08-24
url: https://discourse.slicer.org/t/935
---

# Extension build failure on Mac due to error copying files

**Topic ID**: 935
**Date**: 2017-08-24
**URL**: https://discourse.slicer.org/t/extension-build-failure-on-mac-due-to-error-copying-files/935

---

## Post #1 by @cpinter (2017-08-24 13:44 UTC)

<p>There is a strange error for some of the extensions on Mac stating that files could not be copied, such as<br>
<code>Error copying file "@rpath/libMRMLCore.dylib" to "/.../SlicerRT-build/inner-build/_CPack_Packages/Darwin/TGZ/26298-macosx-amd64-SlicerRT-svn3210-2017-08-21/Slicer.app/Contents/lib/Slicer-4.7/libMRMLCore.dylib".</code></p>
<p>This happens for SlicerRT, but for other extensions as well<br>
<a href="http://slicer.cdash.org/viewBuildError.php?buildid=1085258" class="onebox" target="_blank">http://slicer.cdash.org/viewBuildError.php?buildid=1085258</a><br>
<a href="http://slicer.cdash.org/viewBuildError.php?buildid=1085341">http://slicer.cdash.org/viewBuildError.php?buildid=1085341</a> (DCMQI)<br>
<a href="http://slicer.cdash.org/viewBuildError.php?buildid=1085316">http://slicer.cdash.org/viewBuildError.php?buildid=1085316</a> (PETDICOMExtension)<br>
<a href="http://slicer.cdash.org/viewBuildError.php?buildid=1085367">http://slicer.cdash.org/viewBuildError.php?buildid=1085367</a> (UKFTractography)<br>
<a href="http://slicer.cdash.org/viewBuildError.php?buildid=1085372">http://slicer.cdash.org/viewBuildError.php?buildid=1085372</a> (SPHARM-PDM)</p>
<p>Although this seems like a random error, it’s not only across extensions but happening in the last three days, suggesting this won’t go away by itself<br>
08.23: <a href="http://slicer.cdash.org/viewBuildError.php?buildid=1084455">http://slicer.cdash.org/viewBuildError.php?buildid=1084455</a><br>
08.22: <a href="http://slicer.cdash.org/viewBuildError.php?buildid=1083918">http://slicer.cdash.org/viewBuildError.php?buildid=1083918</a></p>

---

## Post #2 by @jcfr (2017-08-24 14:04 UTC)

<p>Hi Csaba,</p>
<p>That will be fixed by <a href="https://github.com/Slicer/Slicer/pull/780">https://github.com/Slicer/Slicer/pull/780</a></p>
<p>Jc</p>

---

## Post #3 by @cpinter (2017-08-24 14:07 UTC)

<p>Ahh, excellent, thanks <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #4 by @fedorov (2017-08-24 18:05 UTC)

<p>See earlier discussion here: <a href="https://discourse.slicer.org/t/interpreting-cdash-reporting-extension-is-packaged-despite-build-errors/856">Interpreting CDash reporting: extension is packaged despite build errors?</a></p>

---

## Post #5 by @jcfr (2017-08-24 18:41 UTC)

<p>This should be fixed in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26301">r26301</a></p>

---

## Post #6 by @jcfr (2017-08-25 17:57 UTC)

<p>And here is a follow up commit addressing the remaining issues in Slicer. See <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26305">r26305</a></p>
<p>Corresponding changes in upstream projects are here:</p>
<ul>
<li>ITK: <a href="http://review.source.kitware.com/#/c/22583/">http://review.source.kitware.com/#/c/22583/</a>
</li>
<li>CTK:  <a href="https://github.com/commontk/CTK/pull/745/commits/2b71958a424f7fff01b248aaebce0bcdb4dd25ed">https://github.com/commontk/CTK/pull/745/commits/2b71958a424f7fff01b248aaebce0bcdb4dd25ed</a>
</li>
<li>MINC: <a href="https://github.com/BIC-MNI/libminc/pull/87">https://github.com/BIC-MNI/libminc/pull/87</a>
</li>
</ul>

---
