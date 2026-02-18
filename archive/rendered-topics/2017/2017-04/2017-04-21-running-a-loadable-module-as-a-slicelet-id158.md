# Running a loadable module as a slicelet

**Topic ID**: 158
**Date**: 2017-04-21
**URL**: https://discourse.slicer.org/t/running-a-loadable-module-as-a-slicelet/158

---

## Post #1 by @lassoan (2017-04-21 02:29 UTC)

<p>(question posted by Samira on slicer-devel) I am looking into slicelet now and I want to run my loadable extension as a slicelet. What do I need to add to the extension code? And is there any guide on how to do that?</p>

---

## Post #2 by @lassoan (2017-04-21 02:30 UTC)

<p>This page should get you started:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets</a></p>
<p>Let us know if you have any specific questions or problems.</p>

---

## Post #3 by @timeanddoctor (2020-02-04 02:24 UTC)

<p>I used the 4.10 version. If I custom the slicer which way would be the best now?</p>

---

## Post #4 by @lassoan (2020-02-04 04:10 UTC)

<p>I would recommend to use latest master version. There are a few unresolved issues due to a recent ITK upgrade, but they should be fixed within a few weeks (SimpleITK does not work on Mac and there are some DICOM loading issues when you use Add data dialog instead of DICOM module). If you are impacted by these then you might want to use a master version from a few weeks ago.</p>

---

## Post #5 by @timeanddoctor (2020-02-04 04:13 UTC)

<p>I used ‘Slicer.exe --python-code “slicer.util.selectModule(‘QuickSegment’)”’ and get error:</p>
<pre><code class="lang-auto">Traceback (most recent call last):


  File "C:/Users/Desktop/QuickSegment/QuickSegment.py", line 65, in setup
    self.showSingleModule(True)
  File "C:/Users/Desktop/QuickSegment/QuickSegment.py", line 137, in showSingleModule
    slicer.util.setToolbarsVisible(not singleModule, keepToolbars)
AttributeError: module 'slicer.util' has no attribute 'setToolbarsVisible'
</code></pre>

---

## Post #6 by @lassoan (2020-02-04 04:22 UTC)

<aside class="quote no-group quote-modified" data-username="timeanddoctor" data-post="5" data-topic="158">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/timeanddoctor/48/5839_2.png" class="avatar"> timeanddoctor:</div>
<blockquote>
<p>AttributeError: module ‘slicer.util’ has no attribute ‘setToolbarsVisible’</p>
</blockquote>
</aside>
<p>You need to use a recent master version of Slicer.</p>

---

## Post #7 by @timeanddoctor (2020-02-04 04:23 UTC)

<p>Ok， Thanks.<br>
I will update my slicer.</p>

---
