# Show DICOM browser's folder import dialog

**Topic ID**: 9347
**Date**: 2019-12-01
**URL**: https://discourse.slicer.org/t/show-dicom-browsers-folder-import-dialog/9347

---

## Post #1 by @lausiv (2019-12-01 21:13 UTC)

<p>How Can i directly Call(or popup)  DICOM Browser → Import</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c5e4976c585042b0086bddfef1d5f3d477f2b97.png" data-download-href="/uploads/short-url/aTAiokCGDXZ5zcDueVHGaWHMzn9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c5e4976c585042b0086bddfef1d5f3d477f2b97_2_690x291.png" alt="image" data-base62-sha1="aTAiokCGDXZ5zcDueVHGaWHMzn9" width="690" height="291" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c5e4976c585042b0086bddfef1d5f3d477f2b97_2_690x291.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c5e4976c585042b0086bddfef1d5f3d477f2b97.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c5e4976c585042b0086bddfef1d5f3d477f2b97.png 2x" data-dominant-color="656466"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">733×310 77.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8add91ed4ff4381938dc82ae3cd5317518fd7e76.png" data-download-href="/uploads/short-url/jOsBm4u4xRxBiX933P79Q2zDEaO.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8add91ed4ff4381938dc82ae3cd5317518fd7e76.png" alt="image" data-base62-sha1="jOsBm4u4xRxBiX933P79Q2zDEaO" width="690" height="84" data-dominant-color="22303F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">808×99 3.52 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2019-12-01 21:20 UTC)

<p>In recent Slicer Preview releases, you can do this to show folder selector for DICOM import:</p>
<pre><code class="lang-python">slicer.util.selectModule('DICOM')
slicer.modules.DICOMInstance.browserWidget.dicomBrowser.openImportDialog()
</code></pre>

---

## Post #3 by @lausiv (2019-12-03 00:29 UTC)

<p>Thank you very much. Have a Nice Day <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #4 by @lausiv (2019-12-03 00:49 UTC)

<p>But i want to call in my qSlicerMainWindow.cxx file.</p>
<p>in other words.</p>
<p>i want to call python script in my c++ code</p>

---

## Post #5 by @lassoan (2019-12-03 03:55 UTC)

<p>You can run Python code from C++ using <a href="http://pythonManager-%3EexecuteString"><code>pythonManager-&gt;executeString</code></a>.</p>
<p>If you want to import DICOM files from a folder then you can create ctkDICOMIndexer independent from the one in the DICOM browser as shown in <a href="https://github.com/commontk/CTK/blob/master/Libs/DICOM/Core/Testing/Cpp/ctkDICOMIndexerTest1.cpp#L36-L51">this example</a>.</p>

---

## Post #6 by @lausiv (2019-12-03 11:35 UTC)

<p>Thank you. i will do it ^^</p>

---

## Post #7 by @lausiv (2019-12-06 13:19 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="2" data-topic="9347">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>slicer.util.selectModule(‘DICOM’) slicer.modules.DICOMInstance.browserWidget.dicomBrowser.openImportDialog()</p>
</blockquote>
</aside>
<p>I am making the source code but it is very hard to me to call python code in my c++ in slicer<br>
for showing DICOM browser’s folder import dialog</p>
<p><a href="http://pythonmanager-%3Eexecutestring/" rel="noopener nofollow ugc"> <code>pythonManager-&gt;executeString</code>  </a>.</p>
<p>slicer.util.selectModule(‘DICOM’)<br>
slicer.modules.DICOMInstance.browserWidget.dicomBrowser.openImportDialog()</p>
<p>i found similar code but not work for me<br>
<a href="https://discourse.slicer.org/t/show-dicom-browsers-folder-import-dialog/9347">Show DICOM browser’s folder import dialog</a></p>

---

## Post #8 by @lassoan (2019-12-06 15:05 UTC)

<aside class="quote no-group" data-username="lausiv" data-post="7" data-topic="9347">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lausiv/48/4984_2.png" class="avatar"> lausiv:</div>
<blockquote>
<p>it is very hard to me to call python code in my c++</p>
</blockquote>
</aside>
<p>If you have any specific issue with calling Python from C++ then let us know. If you prefer staying in C++ then you can follow the example in CTK that I referred to <a href="https://discourse.slicer.org/t/show-dicom-browsers-folder-import-dialog/9347/5">above</a>.</p>

---

## Post #9 by @lausiv (2019-12-07 05:06 UTC)

<p>I will do it at Slicer Preview releases^^</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/efbe7a5d82c650cef334fbe523aea994845ebbf2.png" data-download-href="/uploads/short-url/ycSdbpPy2EpZejAuZETbZLM0Vpw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/efbe7a5d82c650cef334fbe523aea994845ebbf2.png" alt="image" data-base62-sha1="ycSdbpPy2EpZejAuZETbZLM0Vpw" width="690" height="136" data-dominant-color="F9F4F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1110×220 9.19 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @lassoan (2019-12-07 11:53 UTC)

<p>DICOM browser changed recently, so the code to show the it may be slightly different for the stable release.</p>

---

## Post #11 by @lausiv (2019-12-08 13:53 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="9347">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>w the it may be slightly different for the stable release.</p>
</blockquote>
</aside>
<p>i saw the source code but i think there’s many changes between stable vs. preview release.</p>
<p>it is now working for me;</p>
<p>similar situation,</p>
<p>i want to show DICOM browser’s folder export dialog<br>
preview release doesn’t support this.</p>
<p>would show me the sample code?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84ff73fc90748404ccbc0d50b7320b1789437972.png" data-download-href="/uploads/short-url/iYykzncRAyRsUBJUT7SXGeZWdsS.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84ff73fc90748404ccbc0d50b7320b1789437972.png" alt="image" data-base62-sha1="iYykzncRAyRsUBJUT7SXGeZWdsS" width="645" height="500" data-dominant-color="EEF1EF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">648×502 17.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>seconde question <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
after exporting DICOM Data, i want to delete previous data which is used for exporting. i want python script code example.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df94d5b926b279c1b2b0f3f4aa73e425eecc26c8.png" alt="image" data-base62-sha1="vTTlToeTwwE8fJlx0d5A61x1MaQ" width="277" height="64"></p>

---

## Post #12 by @lassoan (2019-12-09 05:32 UTC)

<aside class="quote no-group" data-username="lausiv" data-post="11" data-topic="9347">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lausiv/48/4984_2.png" class="avatar"> lausiv:</div>
<blockquote>
<p>i want to show DICOM browser’s folder export dialog<br>
preview release doesn’t support this.</p>
</blockquote>
</aside>
<p>Everything that the old DICOM browser could do, the new one can do, too. What code did you use previously to show the export dialog?</p>
<aside class="quote no-group" data-username="lausiv" data-post="11" data-topic="9347">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lausiv/48/4984_2.png" class="avatar"> lausiv:</div>
<blockquote>
<p>i want to delete previous data which is used for exporting</p>
</blockquote>
</aside>
<p>You can use <a href="http://www.commontk.org/docs/html/classctkDICOMDatabase.html#a817e5e86cf586de30300857342d778a2">removePatient</a>/removeStudy/removeSeries to delete selected items or <a href="http://www.commontk.org/docs/html/classctkDICOMDatabase.html#a6dee54db9ca85225bb495815851eb10e">cleanup</a> to remove all database content. But a more common approach is to create a temporary DICOM database and then remove it completely (using openTemporaryDatabase/closeTemporaryDatabase - see <a href="https://github.com/Slicer/Slicer/blob/0abd1fa219628f0dfd5166e430afeb1598b6fcf8/Applications/SlicerApp/Testing/Python/RSNAVisTutorial.py#L194-L292">example</a>).</p>

---

## Post #13 by @lausiv (2019-12-09 05:42 UTC)

<blockquote>
<p>i want to show DICOM browser’s folder export dialog<br>
preview release doesn’t support this.</p>
</blockquote>
<p>Everything that the old DICOM browser could do, the new one can do, too. What code did you use previously to show the export dialog?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d6fc78308efa02b3fa2c69d1d2a7eb9e61f84c5.png" data-download-href="/uploads/short-url/fC7wSVh48shFIJgVtytMnTmahY9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d6fc78308efa02b3fa2c69d1d2a7eb9e61f84c5.png" alt="image" data-base62-sha1="fC7wSVh48shFIJgVtytMnTmahY9" width="690" height="91" data-dominant-color="243140"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1021×136 8.05 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8ab2242fa5b2d15c6ddda26714565bdfd801cd51.png" data-download-href="/uploads/short-url/jMXyx8IAhMT3DVdG6LVN2Zeb3up.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8ab2242fa5b2d15c6ddda26714565bdfd801cd51.png" alt="image" data-base62-sha1="jMXyx8IAhMT3DVdG6LVN2Zeb3up" width="690" height="381" data-dominant-color="F8F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">875×484 35.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I just execute below python script.<br>
slicer.util.selectModule(‘DICOM’)<br>
slicer.modules.DICOMInstance.browserWidget.dicomBrowser.openExportDialog()</p>
<p><strong>i want to call <strong>directly</strong> export dialog like import dialog</strong><br>
ex)<br>
slicer.util.selectModule(‘DICOM’)<br>
slicer.modules.DICOMInstance.browserWidget.dicomBrowser.openImportDialog()</p>
<p>Thank you for your concern and effort^^</p>

---

## Post #14 by @lassoan (2019-12-09 18:21 UTC)

<p>You can show export dialog in recent Slicer versions like this:</p>
<pre><code class="lang-python">exportDialog = slicer.qSlicerDICOMExportDialog()
exportDialog.setMRMLScene(slicer.mrmlScene)
exportDialog.execDialog()
</code></pre>

---

## Post #15 by @lausiv (2019-12-10 02:50 UTC)

<p>Thanks Lasso^^, It workd now.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c118ed846b9245e93be0e1ff180e29f4c40439a.png" data-download-href="/uploads/short-url/fq1brGWpraWDEsI59TQ0Nqees78.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c118ed846b9245e93be0e1ff180e29f4c40439a.png" alt="image" data-base62-sha1="fq1brGWpraWDEsI59TQ0Nqees78" width="644" height="500" data-dominant-color="F8F9F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">656×509 15.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #16 by @lausiv (2019-12-10 10:37 UTC)

<p>I can’t find exact script code for this issue. in other words, exact function or call flow<br>
i already examine your related sample code and source code in slicer DICOMUtil.py<br>
Would you plz share sample script code to delete previous data which is used for exporting^^.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c3357ddae00050ae5a1a68f191b7a3ca5911b78d.png" data-download-href="/uploads/short-url/rQTI8XdhmB9LrN8j2LOH03sOAI5.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c3357ddae00050ae5a1a68f191b7a3ca5911b78d.png" alt="image" data-base62-sha1="rQTI8XdhmB9LrN8j2LOH03sOAI5" width="690" height="360" data-dominant-color="1F303D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">874×456 20.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e32e20b8bdeb9757fbe93c9d7c9885f20139ec0e.png" data-download-href="/uploads/short-url/wpJdhl33oihzxiajTy4BCI7UNxs.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e32e20b8bdeb9757fbe93c9d7c9885f20139ec0e.png" alt="image" data-base62-sha1="wpJdhl33oihzxiajTy4BCI7UNxs" width="690" height="451" data-dominant-color="E6EEF1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">924×604 25.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/bae2d72ca8563bee7427dc1c2f1d0029b0744b03.png" data-download-href="/uploads/short-url/qFgOpvsNDKXl3qhoQ2Dq1QlFnZp.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/bae2d72ca8563bee7427dc1c2f1d0029b0744b03_2_651x500.png" alt="image" data-base62-sha1="qFgOpvsNDKXl3qhoQ2Dq1QlFnZp" width="651" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/bae2d72ca8563bee7427dc1c2f1d0029b0744b03_2_651x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/bae2d72ca8563bee7427dc1c2f1d0029b0744b03_2_976x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/bae2d72ca8563bee7427dc1c2f1d0029b0744b03_2_1302x1000.png 2x" data-dominant-color="F7F5DF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1302×1000 76.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #17 by @lassoan (2019-12-10 20:04 UTC)

<p>If you want to add series to the database temporarily (only to allow loading), then I would recommend to create a temporary database as I described above.</p>
<p>Using <code>dicomDatabase.remove...</code> methods is more complicated: first you need to store all previously existing series in the database in a variable, then import data that you need, get all series in the database, remove all the series that did not exist previously, and finally remove all orphan studies and patients.</p>

---

## Post #18 by @lausiv (2019-12-11 00:12 UTC)

<p>If you want to add series to the database temporarily (only to allow loading), then I would recommend to create a temporary database as I described above.<br>
==&gt; I understand now. this approach is simple for my issue. just create database and add it to new database and delete existing old database.<br>
I will do it and let it shared in this page^^</p>

---

## Post #21 by @lausiv (2019-12-17 02:11 UTC)

<p>when i call pythonManager() in C++<br>
I found compiler can’t find pythonManager()<br>
(i already investigate related source codes)</p>
<p>in other words,<br>
qSlicerApplication::application()-&gt;layoutManager() &lt;== it is OK.<br>
<strong>qSlicerApplication::application()-&gt;pythonManager() &lt;== it is NO</strong></p>
<p>A type cannot be used until it is defined. To resolve the error, be sure the type is fully defined before referencing it.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bdf3a4916ba0e5a96b8ab815004634bc2f3637bb.png" data-download-href="/uploads/short-url/r6of95Fc3hmZIlACrOq3ZBaIAAj.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bdf3a4916ba0e5a96b8ab815004634bc2f3637bb.png" alt="image" data-base62-sha1="r6of95Fc3hmZIlACrOq3ZBaIAAj" width="593" height="500" data-dominant-color="262725"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">980×825 29 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/50889c89d3d560e19bc52fac6c42322ef84720ce.png" alt="image" data-base62-sha1="buqSXeERJYSNj4WM43KLpepbslg" width="498" height="33"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6c7a1faafd6acb7aad1b6ef0e0399bbaaac8b26.png" data-download-href="/uploads/short-url/uE1TavxUTIjzEKtYdVtLg0WkUw6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6c7a1faafd6acb7aad1b6ef0e0399bbaaac8b26.png" alt="image" data-base62-sha1="uE1TavxUTIjzEKtYdVtLg0WkUw6" width="690" height="323" data-dominant-color="1D2A39"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">971×455 17.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #22 by @lassoan (2019-12-17 02:45 UTC)

<p>In C++, to use a class that is implemented in another library, you need to <code>#include</code> the corresponding header file and add the include directory and library to the CMakeLists.txt file of the component that you are building. There are thousands of examples for this in Slicer source code (all classes are used like this).</p>

---

## Post #23 by @lausiv (2019-12-17 05:39 UTC)

<p>Thank you Adras,</p>
<p>After including below header file, i can now execute python script</p>
<h1><a name="p-33425-include-qslicerpythonmanagerh-1" class="anchor" href="#p-33425-include-qslicerpythonmanagerh-1" aria-label="Heading link"></a>include “qSlicerPythonManager.h”</h1>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5f8a256b1aeadf8cd1c5cc06b2f68fc543edce3.png" data-download-href="/uploads/short-url/wOq2hSVZTKbQv1jSRwcMWgdOMGT.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e5f8a256b1aeadf8cd1c5cc06b2f68fc543edce3_2_466x500.png" alt="image" data-base62-sha1="wOq2hSVZTKbQv1jSRwcMWgdOMGT" width="466" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e5f8a256b1aeadf8cd1c5cc06b2f68fc543edce3_2_466x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5f8a256b1aeadf8cd1c5cc06b2f68fc543edce3.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5f8a256b1aeadf8cd1c5cc06b2f68fc543edce3.png 2x" data-dominant-color="30302F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">627×672 96.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
