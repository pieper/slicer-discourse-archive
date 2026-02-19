---
topic_id: 20677
title: "The Layout Is Inconsistent"
date: 2021-11-18
url: https://discourse.slicer.org/t/20677
---

# The layout is inconsistent

**Topic ID**: 20677
**Date**: 2021-11-18
**URL**: https://discourse.slicer.org/t/the-layout-is-inconsistent/20677

---

## Post #1 by @LuPingChina (2021-11-18 08:52 UTC)

<p>I have a question where does the interface code of the dicom module be in the project and why can’t I find it?Also why is the layout of the retrieval form in the compiled 4.13 version dicom module be different from that in the release and how should I debug the code.See the picture.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/79c3b4160310a9c4af988befaa6e95556cd90bd8.png" data-download-href="/uploads/short-url/hnb48dS8zSWv1VdNgmnTRlRxNzO.png?dl=1" title="001" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79c3b4160310a9c4af988befaa6e95556cd90bd8_2_258x500.png" alt="001" data-base62-sha1="hnb48dS8zSWv1VdNgmnTRlRxNzO" width="258" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79c3b4160310a9c4af988befaa6e95556cd90bd8_2_258x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79c3b4160310a9c4af988befaa6e95556cd90bd8_2_387x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79c3b4160310a9c4af988befaa6e95556cd90bd8_2_516x1000.png 2x" data-dominant-color="F8F9F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">001</span><span class="informations">887×1718 72.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92f37254a92672e552672c9f40dafb4d9eddbeb6.png" alt="002" data-base62-sha1="kXZi8RSmP6LteSYT8xETMDo5ciO" width="666" height="421"></p>

---

## Post #2 by @pieper (2021-11-18 13:16 UTC)

<p>Slicer uses commontk for much of the dicom infrastructure: <a href="http://www.commontk.org/index.php/Main_Page" class="inline-onebox">Commontk</a></p>

---

## Post #3 by @LuPingChina (2021-11-19 02:09 UTC)

<p>Thanks for the answer.Although I know if dicom is a module from ctk it cannot explain why the interface layout of my compiled version is not consistent with the official release version</p>

---

## Post #4 by @rbumm (2021-11-19 20:31 UTC)

<p>The DICOM interface can not be found directly in the Slicer source, but in the <a href="https://github.com/commontk/CTK" rel="noopener nofollow ugc">Commontk sources</a>. You probably need to create a fresh Slicer fork and build that to receive the latest DICOM interface, which indeed improved in important detail: being able to receive selected series from studies.</p>
<p>If that does not answer your question please describe what you want to achieve.</p>

---

## Post #5 by @LuPingChina (2021-11-20 01:24 UTC)

<p>I mean, why is the interface of the software I compiled inconsistent with the interface of the officially released version? Is it because of the version problem or where I have a problem</p>

---

## Post #6 by @lassoan (2021-11-20 03:59 UTC)

<p>Slicer Preview Releases are built from the latest version on the master branch every night. If you build the same version then you will get exactly the same user interface.</p>

---

## Post #7 by @LuPingChina (2021-11-20 10:54 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60e40093cc50f75498aa0f734d6c849671e17518.png" data-download-href="/uploads/short-url/dP8krwKNN31glA24ajSwsV6nAx2.png?dl=1" title="QQ图片20211120185227" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/60e40093cc50f75498aa0f734d6c849671e17518_2_690x427.png" alt="QQ图片20211120185227" data-base62-sha1="dP8krwKNN31glA24ajSwsV6nAx2" width="690" height="427" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/60e40093cc50f75498aa0f734d6c849671e17518_2_690x427.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/60e40093cc50f75498aa0f734d6c849671e17518_2_1035x640.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/60e40093cc50f75498aa0f734d6c849671e17518_2_1380x854.png 2x" data-dominant-color="F7F7F7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">QQ图片20211120185227</span><span class="informations">1812×1122 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
It’s not my problem, it’s the version</p>

---

## Post #8 by @lassoan (2021-11-20 13:38 UTC)

<p>Can you copy/paste here the application log (menu: Help → Report a bug)?</p>

---

## Post #9 by @LuPingChina (2021-11-20 16:06 UTC)

<p>[DEBUG][Qt] 21.11.2021 00:05:12 [] (unknown:0) - Session start time …: 2021-11-21 00:05:12<br>
[DEBUG][Qt] 21.11.2021 00:05:12 [] (unknown:0) - Slicer version …: 4.13.0-2021-11-19 (revision 30421 / 9f03a47) win-amd64 - installed release<br>
[DEBUG][Qt] 21.11.2021 00:05:12 [] (unknown:0) - Operating system …: Windows /  Professional / (Build 17763, Code Page 936) - 64-bit<br>
[DEBUG][Qt] 21.11.2021 00:05:12 [] (unknown:0) - Memory …: 24410 MB physical, 33626 MB virtual<br>
[DEBUG][Qt] 21.11.2021 00:05:12 [] (unknown:0) - CPU …: GenuineIntel , 12 cores, 12 logical processors<br>
[DEBUG][Qt] 21.11.2021 00:05:12 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 21.11.2021 00:05:12 [] (unknown:0) - Qt configuration …: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 21.11.2021 00:05:12 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 21.11.2021 00:05:12 [] (unknown:0) - Application path …: C:/ProgramData/NA-MIC/Slicer 4.13.0-2021-11-19/bin<br>
[DEBUG][Qt] 21.11.2021 00:05:12 [] (unknown:0) - Additional module paths …: (none)<br>
[DEBUG][Python] 21.11.2021 00:05:13 [Python] (C:\ProgramData\NA-MIC\Slicer 4.13.0-2021-11-19\lib\Slicer-4.13\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 21.11.2021 00:05:14 [Python] (C:\ProgramData\NA-MIC\Slicer 4.13.0-2021-11-19\lib\Slicer-4.13\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 21.11.2021 00:05:14 [Python] (C:\ProgramData\NA-MIC\Slicer 4.13.0-2021-11-19\lib\Slicer-4.13\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 21.11.2021 00:05:14 [] (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 21.11.2021 00:05:27 [] (unknown:0) - Switch to module:  “DICOM”<br>
[CRITICAL][Stream] 21.11.2021 00:05:27 [] (unknown:0) - Database folder does not contain ctkDICOM.sql file: C:/Users/Administrator/Documents/SlicerDICOMDatabase</p>

---

## Post #10 by @pieper (2021-11-20 16:11 UTC)

<aside class="quote no-group quote-modified" data-username="LuPingChina" data-post="9" data-topic="20677">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lupingchina/48/13183_2.png" class="avatar"> LuPingChina:</div>
<blockquote>
<p>[CRITICAL][Stream] 21.11.2021 00:05:27 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Database folder does not contain ctkDICOM.sql file: C:/Users/Administrator/Documents/SlicerDICOMDatabase</p>
</blockquote>
</aside>
<p>This indicates you need to pick a different database directory (this one may not be writable).</p>

---

## Post #11 by @LuPingChina (2021-11-20 16:13 UTC)

<p>The problem with this database directory will not affect the layout of the UI interface</p>

---

## Post #12 by @LuPingChina (2021-11-20 17:58 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af7452d24dc5250ed547a69fe9a5df4bc5287a8a.png" data-download-href="/uploads/short-url/p28MjIIEOccIsWZYYV6HLVvgwD8.png?dl=1" title="Form_224" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/af7452d24dc5250ed547a69fe9a5df4bc5287a8a_2_665x500.png" alt="Form_224" data-base62-sha1="p28MjIIEOccIsWZYYV6HLVvgwD8" width="665" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/af7452d24dc5250ed547a69fe9a5df4bc5287a8a_2_665x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af7452d24dc5250ed547a69fe9a5df4bc5287a8a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af7452d24dc5250ed547a69fe9a5df4bc5287a8a.png 2x" data-dominant-color="F3F2F2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Form_224</span><span class="informations">853×641 38.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I would like to ask, where can I modify this interface? I want to translate the interface into Chinese</p>

---

## Post #13 by @LuPingChina (2021-11-20 18:00 UTC)

<p>CTK contains DICOM components. What is the relationship between this and DCMTK</p>

---

## Post #14 by @pieper (2021-11-20 18:33 UTC)

<p>The layout difference are because the current code reflects a fairly recent redesign that happened since the latest release was made.</p>
<aside class="quote no-group" data-username="LuPingChina" data-post="13" data-topic="20677" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lupingchina/48/13183_2.png" class="avatar"> LuPingChina:</div>
<blockquote>
<p>CTK contains DICOM components. What is the relationship between this and DCMTK</p>
</blockquote>
</aside>
<p>You can read about this at the <a href="http://commontk.org">commontk.org</a> site.</p>
<aside class="quote no-group" data-username="LuPingChina" data-post="12" data-topic="20677">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lupingchina/48/13183_2.png" class="avatar"> LuPingChina:</div>
<blockquote>
<p>I would like to ask, where can I modify this interface? I want to translate the interface into Chinese</p>
</blockquote>
</aside>
<p>Did you see the response when you asked before?</p>
<aside class="quote" data-post="3" data-topic="20611">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lupingchina/48/13183_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-set-the-title-and-name-of-the-module/20611/3">How to set the title and name of the module</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    I want to translate the software interface into Chinese.
  </blockquote>
</aside>


---

## Post #15 by @lassoan (2021-11-22 19:01 UTC)

<p>Commit <a href="https://github.com/Slicer/Slicer/commit/9f03a47ed9a6c8cae1b242bf45259b6925f2a75b">9f03a47ed9a6c8cae1b242bf45259b6925f2a75b</a> is a very recent master version. That version uses this <a href="https://github.com/Slicer/Slicer/blob/master/SuperBuild/External_CTK.cmake#L78">CTK hash</a>, which renders the Query/Retrieve dialog like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c7284d2f10dcc9c22d1190d602110679d2e6f18.png" data-download-href="/uploads/short-url/43EIVBDLqJd0K3RdGwIrFMpxCpG.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c7284d2f10dcc9c22d1190d602110679d2e6f18_2_690x429.png" alt="image" data-base62-sha1="43EIVBDLqJd0K3RdGwIrFMpxCpG" width="690" height="429" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c7284d2f10dcc9c22d1190d602110679d2e6f18_2_690x429.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c7284d2f10dcc9c22d1190d602110679d2e6f18_2_1035x643.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c7284d2f10dcc9c22d1190d602110679d2e6f18_2_1380x858.png 2x" data-dominant-color="F6F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1682×1048 42.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If your Query/Retrieve dialog looks like the old version that you showed above it means that your CTK version is older. You either have not rebuilt CTK since you updated it or you specified an older CTK version manually.</p>
<aside class="quote no-group" data-username="LuPingChina" data-post="11" data-topic="20677" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lupingchina/48/13183_2.png" class="avatar"> LuPingChina:</div>
<blockquote>
<p>The problem with this database directory will not affect the layout of the UI interface</p>
</blockquote>
</aside>
<p>Appearance of the DICOM database tables (displayed columns, order of columns, column width, format, sorting, etc.) are stored in the database itself, so the database content actually affects the layout of the UI interface - but only inside the Patient/Study/Series table. The difference you see is due to using an older CTK version.</p>

---
