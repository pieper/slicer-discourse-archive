---
topic_id: 7109
title: "Tests Failing On Slicer Factory That Do Not Fail Locally"
date: 2019-06-10
url: https://discourse.slicer.org/t/7109
---

# Tests failing on Slicer factory that do not fail locally

**Topic ID**: 7109
**Date**: 2019-06-10
**URL**: https://discourse.slicer.org/t/tests-failing-on-slicer-factory-that-do-not-fail-locally/7109

---

## Post #1 by @cpinter (2019-06-10 13:48 UTC)

<p>I noticed a while ago that about a dozen tests keep failing on the Slicer dashboard both for Windows and Mac. I ran the tests that I think I’d be responsible for fixing (py_SubjectHierarchyGenericSelfTest, qSlicerModelsModuleWidgetTest*), and all of these pass on my computer. The dashboard does not show any output for these tests for neither platform.</p>
<p>All of these tests actually start Slicer and show the GUI. Can the reason for the failing tests be that the GUI cannot be oponed on the factory? Or any other ideas? Thanks! <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a></p>

---

## Post #2 by @jamesobutler (2019-06-11 02:33 UTC)

<p>For py_SubjectHierarchyGenericSelfTest I see some test output on the cdash dashboard such as:</p>
<pre><code class="lang-auto">Test directory: /var/folders/6y/zp9dkw5d5wg35y8qvn29hpww0000gn/T/Slicer-tmp-kitware/SubjectHierarchyGenericSelfTest
Clear scene
Switching to temporary DICOM database: /var/folders/6y/zp9dkw5d5wg35y8qvn29hpww0000gn/T/Slicer-tmp-kitware/SubjectHierarchyGenericSelfTest/CtkDicomDatabase
QSqlDatabasePrivate::removeDatabase: connection 'SLICER' is still in use, all queries will cease to work.
QSqlDatabasePrivate::addDatabase: duplicate connection name 'SLICER', old connection removed.
</code></pre>
<p>Do you not see this output for Mac tests?<br>
I’m also not sure why the Windows test output is usually less descriptive on cdash dashboard. That’s why I always look at the Mac output.</p>
<p>The test also appears to have been failing since <a href="http://slicer.cdash.org/testDetails.php?test=9571122&amp;build=1564613" rel="nofollow noopener">April 16th</a>. You seemed to have a <a href="https://github.com/Slicer/Slicer/commit/75fceb26fb40397eac1b06fb2030c7b040f861ad" rel="nofollow noopener">discussion</a> with JC about a DICOM browser commit but I can’t tell if anything was acted upon.</p>

---

## Post #3 by @cpinter (2019-06-11 03:05 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="7109">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>That’s why I always look at the Mac output.</p>
</blockquote>
</aside>
<p>Same here. Not sure why I didn’t see this.<br>
The log does not show much though, these messages are normal. It still seems to me that the GUI is not constructed.</p>

---

## Post #4 by @jcfr (2019-06-11 03:13 UTC)

<p>I suspect it if related to remaining files in temporary directory. I will confirm this tomorrow.</p>

---

## Post #5 by @lassoan (2019-06-11 13:58 UTC)

<aside class="quote no-group quote-modified" data-username="jamesobutler" data-post="2" data-topic="7109">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>connection ‘SLICER’ is still in use, all queries will cease to work</p>
</blockquote>
</aside>
<p>Just to clarify, this is not normal, it is an error, most probably because multiple database connections are created with the same name. The easiest solution is to not provide a connection name to ctkDICOMDatabase.openDatabase (and then a random connection name is generated).</p>

---

## Post #6 by @cpinter (2019-06-11 14:28 UTC)

<p>I remember getting this error message regularly in passing tests (an <a href="http://slicer.cdash.org/testDetails.php?test=9652239&amp;build=1612644" rel="nofollow noopener">example</a>). So in this sense it is normal.</p>
<p>The tests do not fail because of this, especially that most of these failing tests do not even use DICOM.</p>

---

## Post #7 by @jcfr (2019-06-11 18:34 UTC)

<p>The test timeout because of the message asking to update the database, as discussed <a href="https://github.com/Slicer/Slicer/commit/75fceb26fb40397eac1b06fb2030c7b040f861ad#r33215120">here</a> I suggest test automatically choose one or the other option.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/513d33483aec9c02c191fb3f9dc31d40a4260d9c.png" data-download-href="/uploads/short-url/bAFNmyaEcvfxrvq0oPJs190hIGE.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/513d33483aec9c02c191fb3f9dc31d40a4260d9c_2_690x211.png" alt="image" data-base62-sha1="bAFNmyaEcvfxrvq0oPJs190hIGE" width="690" height="211" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/513d33483aec9c02c191fb3f9dc31d40a4260d9c_2_690x211.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/513d33483aec9c02c191fb3f9dc31d40a4260d9c_2_1035x316.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/513d33483aec9c02c191fb3f9dc31d40a4260d9c.png 2x" data-dominant-color="B2B6C0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1204×369 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @cpinter (2019-06-11 18:48 UTC)

<p>Right, thanks for the reminder. I’ll fix this asap.</p>
<p>Some other tests that fail on the dashboard and pass on my computer (like the Models tests) don’t use DICOM, so they must fail for a different reason.</p>

---
