# DICOM volume orientation may be bad

**Topic ID**: 10068
**Date**: 2020-02-02
**URL**: https://discourse.slicer.org/t/dicom-volume-orientation-may-be-bad/10068

---

## Post #1 by @chir.set (2020-02-02 10:15 UTC)

<p>A DICOM volume loaded in the DICOM module shows up rightly.</p>
<p>When loaded via the ‘Load data’ menu, its orientation is bad. That’s my preferred method, good or bad.</p>
<p>Please see attached images.</p>
<p>Can it be fixed ?</p>
<p>Thanks.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8e6400076a88c417466fd3a9fbb3e15363ded26.png" data-download-href="/uploads/short-url/o69wrWZm8VSCYwtFIj37pTaTKDQ.png?dl=1" title="good" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8e6400076a88c417466fd3a9fbb3e15363ded26_2_690x485.png" alt="good" data-base62-sha1="o69wrWZm8VSCYwtFIj37pTaTKDQ" width="690" height="485" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8e6400076a88c417466fd3a9fbb3e15363ded26_2_690x485.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8e6400076a88c417466fd3a9fbb3e15363ded26_2_1035x727.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8e6400076a88c417466fd3a9fbb3e15363ded26.png 2x" data-dominant-color="0F0F0D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">good</span><span class="informations">1334×939 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2020-02-02 14:51 UTC)

<p><a class="mention" href="/u/chir.set">@chir.set</a>: Are you able to share a dataset with this behavior?</p>
<p>The DICOM module add several checks and organizes the data before loading, so it will always be the recommended method.  But it would be good to know why this data fails to load correctly and perhaps it could be reported/fixed in the ITK IO code.</p>

---

## Post #3 by @lassoan (2020-02-02 15:13 UTC)

<p>I’ve noticed this, too. This is a regression in ITK-v5.1rc01.</p>
<p><a class="mention" href="/u/dzenanz">@dzenanz</a> <a class="mention" href="/u/thewtex">@thewtex</a></p>

---

## Post #4 by @chir.set (2020-02-02 17:29 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="10068">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Are you able to share a dataset with this behavior?</p>
</blockquote>
</aside>
<p>For anonimity, I must export the affected DICOM series in a directory. But when loading the anonymized volume via the ‘Load data’ menu, it is rightly oriented.</p>
<p>Not much I can do to provide sample data.</p>
<p>Regards.</p>

---

## Post #5 by @lassoan (2020-02-02 19:04 UTC)

<p>I’ve filed an ITK bug report: <a href="https://github.com/InsightSoftwareConsortium/ITK/issues/1587">https://github.com/InsightSoftwareConsortium/ITK/issues/1587</a></p>
<p>This minor ITK version upgrade has caused us so much headache already - build failures in all components that uses ITK (Slicer core, BRAINS, Elastix, etc.), DICOM errors (<a href="https://github.com/InsightSoftwareConsortium/ITK/issues/1586">1</a>, <a href="https://github.com/InsightSoftwareConsortium/ITK/issues/1587">2</a>), SimpleITK failure on all operating systems with various reasons (Windows issue is fixed now but we still don’t have solution for the <a href="https://discourse.slicer.org/t/sitkutils-pullvolumefromslicer-makes-slicer-crash/9781/8">MacOS error</a>), <a href="https://discourse.itk.org/t/no-progress-reporting-in-itk5/2630">lack of filter progress updates</a>, etc. The ITK team is very responsive but it is still quite frustrating that we need to spend so much time with investigating these regressions.</p>

---

## Post #6 by @pieper (2020-02-02 19:26 UTC)

<p>It is completely screwed up - I can reproduce with public data (this was series 7 from patient 0000 in <a href="https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=61081171">this TCIA collection</a>.  I’ll follow up on the ITK tracker.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/5261958b97c3e99d44ec4b034e9bb00012fd889e.png" data-download-href="/uploads/short-url/bKMdZvptX9sCKpuIK9nO1mu2yAe.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/5261958b97c3e99d44ec4b034e9bb00012fd889e_2_690x340.png" alt="image" data-base62-sha1="bKMdZvptX9sCKpuIK9nO1mu2yAe" width="690" height="340" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/5261958b97c3e99d44ec4b034e9bb00012fd889e_2_690x340.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/5261958b97c3e99d44ec4b034e9bb00012fd889e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/5261958b97c3e99d44ec4b034e9bb00012fd889e.png 2x" data-dominant-color="252524"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">827×408 65.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In this image the volume on the left was loaded via the DICOM module, and the volume on the right was loaded via Add Data.</p>

---

## Post #7 by @pieper (2020-02-03 20:41 UTC)

<p>This ITK example seems to work right on the same data.  I’ll see if I can single step to see what Slicer does differently (there’s some very old code in vtkITK that could be the source of the issue).</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/master/Examples/IO/DicomSeriesReadGaussianImageWrite.cxx" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/InsightSoftwareConsortium/ITK/blob/master/Examples/IO/DicomSeriesReadGaussianImageWrite.cxx" target="_blank">InsightSoftwareConsortium/ITK/blob/master/Examples/IO/DicomSeriesReadGaussianImageWrite.cxx</a></h4>
<pre><code class="lang-cxx">/*=========================================================================
 *
 *  Copyright Insight Software Consortium
 *
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *         http://www.apache.org/licenses/LICENSE-2.0.txt
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 *
 *=========================================================================*/

#include "itkGDCMImageIO.h"
#include "itkGDCMSeriesFileNames.h"
</code></pre>

  This file has been truncated. <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/master/Examples/IO/DicomSeriesReadGaussianImageWrite.cxx" target="_blank">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #8 by @pieper (2020-02-07 18:29 UTC)

<p>We looked into this and it does appear to be a regression related to the new ITK version.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> and I discussed that using Add Data to load dicom is never going to be robust, so we are thinking to disable even allowing it.  Hopefully <a href="https://github.com/Slicer/Slicer/commit/b1a593a8a7b7cc889f890a1c89b653d3b8e060f8">his new chagne</a> to streamline dropping files on the DICOM module directly will address sort of the same use case.</p>
<p>If anyone feels very strongly about this, another option could be to add another reader option to the Add Data mechanism that tries to be smarter about files that have .dcm or .IMA extensions since those are very likely to be DICOM.  That loader path could use the same logic as in the ITK example linked above.  This approach isn’t especially difficult, but it would take a developer some time to implement and test (volunteers?).</p>

---

## Post #9 by @chir.set (2020-02-08 08:29 UTC)

<aside class="quote no-group" data-username="pieper" data-post="8" data-topic="10068">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>so we are thinking to disable even allowing it</p>
</blockquote>
</aside>
<p>I may end up using the DICOM module then.</p>
<p>It has these disadvantages :</p>
<ul>
<li>Volume information is printed in the 4 corners of 2Dviews, consuming some  screen estate.</li>
<li>Study name is imposed by the study, and not really intuitive to select in combo boxes. They may be changed, with a few clicks. Many times a day, it becomes tedious.</li>
<li>All studies must be scanned by the DICOM module before we can load one.</li>
<li>A database must be managed, transparently though. But that’s good for the vast majority of users. In my workflow however, I prefer data to be independent of the application.</li>
</ul>
<p>With the Load Data module</p>
<ul>
<li>A personalized string may be typed right away before loading.</li>
<li>2D views are not overloaded with corner annotations.</li>
<li>As an inconvenience, we don’t know what study we are loading.</li>
</ul>
<p>Regards.</p>

---

## Post #10 by @chir.set (2020-02-08 10:14 UTC)

<aside class="quote no-group" data-username="pieper" data-post="8" data-topic="10068">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>files that have .dcm or .IMA extensions since those are very likely to be DICOM</p>
</blockquote>
</aside>
<p>I may add that DICOM files on 99% of CT angioscans on DVDs, from many institutions, do not have any extension, and sometimes end with just a dot.</p>
<p>Now if it’s not possible to maintain the Add Data module for serial study loading, I’ll just use the DICOM module.</p>

---

## Post #11 by @pieper (2020-02-08 19:33 UTC)

<p>Yes, that’s why the DICOM module is the right way to go in general, and it makes sense to try to make it more efficient to use.</p>
<p>A lot of the complexity of the Add Data approach is that it tries to use file extensions to determine what’s in the files, but these don’t fully define what’s in the data.  Then under the hood it looks inside the files and tries to discover what’s in the file and load it as well as possible.</p>

---

## Post #12 by @lassoan (2020-02-08 20:51 UTC)

<p>Thanks for the specific feedback, it is very useful and it shows that we are on right track but we should do a couple of things to improve the user experience.</p>
<aside class="quote no-group" data-username="chir.set" data-post="9" data-topic="10068">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<ul>
<li>Volume information is printed in the 4 corners of 2Dviews, consuming some screen estate.</li>
</ul>
</blockquote>
</aside>
<p>You can configure how much (if any) image details you want to show in “DataProbe” module. We can improve things if you have specific suggestions.</p>
<aside class="quote no-group" data-username="chir.set" data-post="9" data-topic="10068">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<ul>
<li>Study name is imposed by the study, and not really intuitive to select in combo boxes. They may be changed, with a few clicks. Many times a day, it becomes tedious.</li>
</ul>
</blockquote>
</aside>
<p>The node name is created from series name/description. In recent Slicer versions, you can see study description and patient name in the DICOM module and you can change it by one double-click. At some point we will replace the current node selector by the subject hierarchy node selector (it is already used at a few places and you can show one by typing this in the Python console:</p>
<pre><code>c = slicer.qMRMLSubjectHierarchyComboBox()
c.setMRMLScene(slicer.mrmlScene)
c.show()
</code></pre>
<aside class="quote no-group" data-username="chir.set" data-post="9" data-topic="10068">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<ul>
<li>All studies must be scanned by the DICOM module before we can load one.</li>
</ul>
</blockquote>
</aside>
<p>This is inevitable if you want to load the data correctly. This happens automatically, in the background now (without blocking the user interface). We’ll add thumbnail display to shorten “time to first image”.</p>
<aside class="quote no-group" data-username="chir.set" data-post="9" data-topic="10068">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<ul>
<li>A database must be managed, transparently though. But that’s good for the vast majority of users. In my workflow however, I prefer data to be independent of the application.</li>
</ul>
</blockquote>
</aside>
<p>I don’t understand this point.</p>

---

## Post #13 by @chir.set (2020-02-08 21:39 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="10068">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I don’t understand this point.</p>
</blockquote>
</aside>
<p>Well, I mean everytime the DICOM module is loaded, it shows a long list of previously loaded studies. Because I manage data outside Slicer, what’s saved in the SQLite DB is of little interest to me and in effect, I always cleared the list whenever (rarely) I happened to used the DICOM module. Most users won’t do that obviously. How about providing a checkbox below the ‘Import’ button,<br>
labelled ‘Don’t save to DB’ ? I just expect data to be loaded, not imported to a database.</p>
<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="10068">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>you can change it by one double-click.</p>
</blockquote>
</aside>
<p>This solves one problem easily.</p>
<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="10068">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can configure how much (if any) image details you want to show in “DataProbe” module</p>
</blockquote>
</aside>
<p>An this solves another one.</p>

---
