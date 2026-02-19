---
topic_id: 2378
title: "Cdash Build Test Failing For Windows Without Error Log"
date: 2018-03-20
url: https://discourse.slicer.org/t/2378
---

# Cdash build test failing for Windows without error log

**Topic ID**: 2378
**Date**: 2018-03-20
**URL**: https://discourse.slicer.org/t/cdash-build-test-failing-for-windows-without-error-log/2378

---

## Post #1 by @chribaue (2018-03-20 14:23 UTC)

<p>Hi,</p>
<p>one of the self tests I wrote for one of my extensions keeps failing on Cdash for the Windows build without giving me a reasonable error log:</p>
<p><a href="http://slicer.cdash.org/testDetails.php?test=8729220&amp;build=1223692" class="onebox" target="_blank" rel="nofollow noopener">http://slicer.cdash.org/testDetails.php?test=8729220&amp;build=1223692</a><br>
The test output is “vtkDebugLeaks has found no leaks.” and the test status is “Failed”</p>
<p>The same test passes on Mac and on my Linux machine.<br>
<a href="http://slicer.cdash.org/testDetails.php?test=8742239&amp;build=1223531" class="onebox" target="_blank" rel="nofollow noopener">http://slicer.cdash.org/testDetails.php?test=8742239&amp;build=1223531</a></p>
<p>When I download Slicer nighly build for Windows, install the extension and run the test inside of Slicer, the self test also passes without any issues. Just on cdash it seems to have issue.</p>
<p>Any idea how to debug and fix this?</p>
<p>Thanks in advance.</p>

---

## Post #2 by @adamrankin (2018-03-21 17:28 UTC)

<p>Hello all,</p>
<p>I was wondering what might cause an extension to not be built on the dashboard?</p>
<p>The SlicerVASST extension was built (and failed) on the mac build machine, but was not built for Windows.</p>
<p>Cheers,<br>
Adam</p>

---

## Post #3 by @jcfr (2018-03-21 17:32 UTC)

<p><a class="mention" href="/u/adamrankin">@adamrankin</a> <a class="mention" href="/u/chribaue">@chribaue</a> Thanks for the reports, we will follow up shortly with an update.</p>
<p>Cc: <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a></p>

---

## Post #4 by @lassoan (2018-03-21 19:23 UTC)

<aside class="quote no-group" data-username="adamrankin" data-post="2" data-topic="2378">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/adamrankin/48/155_2.png" class="avatar"> adamrankin:</div>
<blockquote>
<p>I was wondering what might cause an extension to not be built on the dashboard?</p>
</blockquote>
</aside>
<p>Does it depend on another extension?<br>
There is a known issue on Windows there are any <em>test</em> failures in any of the extensions that you depend on, your extension will not be attempted to be built, it will be just skipped.</p>

---

## Post #5 by @jcfr (2018-03-21 19:46 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="2378">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>known issue on Windows there are any test failures in any of the extensions that you depend on</p>
</blockquote>
</aside>
<p>This shouldn’t be the case anymore, we are also testing for this:</p>
<p><a href="https://github.com/Slicer/Slicer/blob/c38d9754c55c7615e59e4a045774455dcd416015/Extensions/CMake/Testing/SlicerExtensionBuildSystemTest.py#L284-L290" class="onebox" target="_blank" rel="noopener">https://github.com/Slicer/Slicer/blob/c38d9754c55c7615e59e4a045774455dcd416015/Extensions/CMake/Testing/SlicerExtensionBuildSystemTest.py#L284-L290</a></p>

---

## Post #6 by @cpinter (2018-03-21 20:00 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="5" data-topic="2378">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>This shouldn’t be the case anymore, we are also testing for this</p>
</blockquote>
</aside>
<p>Unfortunately it’s still a problem. It’s enough to take a look at the latest dashboard (see <a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;display=project&amp;filtercombine=and&amp;filtercombine=and&amp;filtercombine=or&amp;filtercombine=or&amp;filtercombine=or&amp;filtercombine=or&amp;filtercombine=or&amp;filtercombine=or&amp;filtercount=4&amp;showfilters=1&amp;filtercombine=or&amp;field1=label&amp;compare1=63&amp;value1=SlicerRT&amp;field2=label&amp;compare2=63&amp;value2=GelDosimetry&amp;field3=label&amp;compare3=63&amp;value3=FilmDosimetry&amp;field4=label&amp;compare4=63&amp;value4=SegmentRegistration">this one</a> with convenient filters). You can see that none of the dependent extensions build on Windows.</p>

---

## Post #7 by @jcfr (2018-03-21 20:14 UTC)

<p>Just to say that I think the assumption <em>it is failing because dependent extension tests fails</em> is invalid. Few days ago, it look like they all got built as expected:</p>
<ul>
<li><a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2018-03-18&amp;filtercount=4&amp;showfilters=1&amp;filtercombine=or&amp;field1=label&amp;compare1=63&amp;value1=SlicerRT&amp;field2=label&amp;compare2=63&amp;value2=GelDosimetry&amp;field3=label&amp;compare3=63&amp;value3=FilmDosimetry&amp;field4=label&amp;compare4=63&amp;value4=SegmentRegistration">2018-03-18</a></li>
<li><a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2018-03-17&amp;filtercount=4&amp;showfilters=1&amp;filtercombine=or&amp;field1=label&amp;compare1=63&amp;value1=SlicerRT&amp;field2=label&amp;compare2=63&amp;value2=GelDosimetry&amp;field3=label&amp;compare3=63&amp;value3=FilmDosimetry&amp;field4=label&amp;compare4=63&amp;value4=SegmentRegistration">2018-03-17</a></li>
</ul>
<p>I think the problem is different. Most likely a regression introduced with the recent refactoring of dashboard script and associated driver scripts.</p>

---

## Post #8 by @adamrankin (2018-03-21 20:22 UTC)

<p>Oh… Yup that’s it. I’ll start fixing tests!</p>
<p>Thanks!</p>

---

## Post #9 by @chribaue (2018-03-21 20:24 UTC)

<p>My extension also depends on another extension. cdash builds it for Windows. Just that the test fails without any output telling me why.</p>

---

## Post #10 by @lassoan (2018-03-21 21:46 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="7" data-topic="2378">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Just to say that I think the assumption it is failing because dependent extension tests fails is invalid.</p>
</blockquote>
</aside>
<p>Sounds promising! We have been struggling with the issue of dependent extensions not building and the only factor we could identify was failing tests, but maybe it was just coincidence.</p>

---

## Post #11 by @lassoan (2018-03-21 21:49 UTC)

<aside class="quote no-group" data-username="chribaue" data-post="9" data-topic="2378">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chribaue/48/1373_2.png" class="avatar"> chribaue:</div>
<blockquote>
<p>Just that the test fails without any output telling me why</p>
</blockquote>
</aside>
<p>That may indicate that the application crashes during shutdown. Also note that on Windows, the application may be built without console support. In that case, console output does not appear on the dashboard.</p>

---

## Post #12 by @chribaue (2018-03-22 13:04 UTC)

<p>Hi Andras,</p>
<p>Thank you for the feedback.</p>
<p>According to: <a href="http://slicer.cdash.org/testSummary.php?project=11&amp;name=py_PETLiverUptakeMeasurementQR&amp;date=2018-03-20" rel="nofollow noopener">http://slicer.cdash.org/testSummary.php?project=11&amp;name=py_PETLiverUptakeMeasurementQR&amp;date=2018-03-20</a><br>
the test for the Windows nightly only takes 15 seconds before it fails.<br>
The Mac version runs for 255 seconds until the end.</p>
<p>What is the quickest way to figure out what’s going on?</p>

---

## Post #13 by @lassoan (2018-03-22 20:15 UTC)

<p>I’ve checked what’s happening on perklab-factory.</p>
<p>The problem with PETLiverUptakeMeasurement extension test on Windows is that DEPENDENCIES_ADDITIONAL_MODULE_PATHS is set incorrectly. On Windows, binaries are within Release, Debug, RelWithDebInfo, or MinSizeRel subfolder. You can find a working example <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Testing/Python/CMakeLists.txt#L11-L29">here</a>.</p>
<p>I would also recommend to use DICOMUtils.LoadDICOMFilesToDatabase for downloading, importing, and loading DICOM data set. It is more robust and faster than what the module does. See usage example <a href="https://github.com/Slicer/Slicer/blob/e6878b0065778a56d2e7f182f4c9abba20f4ca88/Applications/SlicerApp/Testing/Python/SubjectHierarchyGenericSelfTest.py#L164-L184">here</a>.</p>

---

## Post #14 by @chribaue (2018-03-22 20:20 UTC)

<p>That’s helpful! Thank you Andras!</p>
<p>I’ll start working on it.</p>

---

## Post #15 by @adamrankin (2018-03-23 15:10 UTC)

<p>Does the factory.perklab experience the same glitches as overload.kitware?</p>
<p>If so, I will setup my own build configuration and debug from there.</p>
<p>Thanks <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/lassoan">@lassoan</a> for the knowledge</p>

---

## Post #16 by @lassoan (2018-03-23 22:37 UTC)

<p>Building all extensions is really simple, so I would recommend to set it up on a computer so that you can debug extension build failures.</p>
<aside class="quote no-group" data-username="adamrankin" data-post="15" data-topic="2378">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/adamrankin/48/155_2.png" class="avatar"> adamrankin:</div>
<blockquote>
<p>Does the factory.perklab experience the same glitches as overload.kitware?</p>
</blockquote>
</aside>
<p>If the same error occurs on factory.perklab and overload.kitware then most likely it is not a glitch. Is there any particular issue that you are investigating?</p>

---

## Post #17 by @adamrankin (2018-03-24 00:02 UTC)

<p>Yes, the SlicerVASST extension is still not being built on windows.</p>
<p>I am setting up a build.</p>

---
