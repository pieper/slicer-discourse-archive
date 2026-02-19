---
topic_id: 8251
title: "Vtkitkimagethresholdcalculator Failure Due To Itk Update"
date: 2019-09-01
url: https://discourse.slicer.org/t/8251
---

# vtkITKImageThresholdCalculator failure - due to ITK update?

**Topic ID**: 8251
**Date**: 2019-09-01
**URL**: https://discourse.slicer.org/t/vtkitkimagethresholdcalculator-failure-due-to-itk-update/8251

---

## Post #1 by @lassoan (2019-09-01 14:06 UTC)

<p>vtkITKImageThresholdCalculator fails with errors like this recently (and crashes or just provides invalid result):</p>
<pre><code class="lang-auto">Failed to compute threshold value using method Shanbhag. Details: 
itk::ExceptionObject (00000076F88F6C90)
Location: "void __cdecl itk::ImageConstIterator&lt;class itk::Image&lt;int,3&gt; &gt;::SetRegion(const class itk::ImageRegion&lt;3&gt; &amp;)" 
File: c:\d\s4d\itk\modules\core\common\include\itkImageConstIterator.h
Line: 210
Description: itk::ERROR: Region ImageRegion (00000076F88F6E68)
  Dimension: 3
  Index: [0, 0, 0]
  Size: [512, 512, 9]
 is outside of buffered region ImageRegion (0000019E5F947430)
  Dimension: 3
  Index: [0, 0, 0]
  Size: [0, 0, 0]
</code></pre>
<p>It still worked fine in Slicer 4.11.0-2019-08-11 (revision 28433), so I guess it is due to recent ITK updates.</p>
<p>How to reproduce: Load a volume, go to segment editor, select Threshold effect, click on left or right arrow buttons in “Automatic threshold” row.</p>
<p><strong>Does anyone have a clue why could this happen? I don’t see anything special in <a href="https://github.com/Slicer/Slicer/blob/master/Libs/vtkITK/vtkITKImageThresholdCalculator.cxx" rel="nofollow noopener">vtkITKImageThresholdCalculator.cxx</a> that I would expect to break due to an ITK update.</strong></p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> <a class="mention" href="/u/pieper">@pieper</a>  <a class="mention" href="/u/hjmjohnson">@hjmjohnson</a></p>

---

## Post #2 by @pieper (2019-09-01 15:04 UTC)

<p>I have no idea.  Adding <a class="mention" href="/u/thewtex">@thewtex</a> and <a class="mention" href="/u/blowekamp">@blowekamp</a> to the list of people who might be able to help.</p>

---

## Post #3 by @thewtex (2019-09-02 00:27 UTC)

<p><a class="mention" href="/u/blowekamp">@blowekamp</a> may know – this change may be involved:</p>
<aside class="onebox githubcommit">
  <header class="source">
      <a href="https://github.com/InsightSoftwareConsortium/ITK/commit/9bb0f0cc4bc65b80461ca0027c252dc6d16440b4#diff-b6070cacd90df4d5a68edbaa6b688db4" target="_blank" rel="nofollow noopener">github.com/InsightSoftwareConsortium/ITK</a>
  </header>
  <article class="onebox-body">
      <a href="https://github.com/blowekamp" target="_blank" rel="nofollow noopener">
    <img alt="blowekamp" src="https://avatars1.githubusercontent.com/u/321061?v=4" class="thumbnail onebox-avatar" width="90" height="90">
  </a>

<h4>
  <a href="https://github.com/InsightSoftwareConsortium/ITK/commit/9bb0f0cc4bc65b80461ca0027c252dc6d16440b4" target="_blank" rel="nofollow noopener">ENH: Use streaming sink base class for image to histogram filters</a>
</h4>

  <pre class="message" style="white-space: normal;">Change the base class from ImageTransformer to ImageSink and expose
SetNumberOfStreamDivisions method to enable streamed generation of
Histograms. Also updated the way decorated...</pre>

<div class="date">
  by <a href="https://github.com/blowekamp" target="_blank" rel="nofollow noopener">blowekamp</a>
  on <a href="https://github.com/InsightSoftwareConsortium/ITK/commit/9bb0f0cc4bc65b80461ca0027c252dc6d16440b4" target="_blank" rel="nofollow noopener">06:39PM - 14 May 19 UTC</a>
</div>

<div class="github-commit-stats">
  changed <strong>4 files</strong>
  with <strong>73 additions</strong>
  and <strong>63 deletions</strong>.
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #4 by @blowekamp (2019-09-03 20:32 UTC)

<p>As Matt pointed out in the PR the base class of the <code>ImageToHistogramFilter</code> was changed to a the new <code>ImageSink</code> which add streaming pipelining support. So the method called in the ITK pipeline may be a little different from ITKv4.</p>
<p>I expect the quick solution is to add <code>itkImporter-&gt;UpdateLargestPossibleRegion()</code> after it’s connected to VTK.</p>
<p>What is wrong with the pipeline connectivity to cause this to be needed is a harder question.</p>

---

## Post #5 by @lassoan (2019-09-04 03:53 UTC)

<p><a class="mention" href="/u/blowekamp">@blowekamp</a> <a class="mention" href="/u/thewtex">@thewtex</a> <a class="mention" href="/u/pieper">@pieper</a> Thanks for your help!</p>
<p>Adding <code>UpdateLargestPossibleRegion()</code> indeed <a href="https://github.com/Slicer/Slicer/commit/f45acbfddaae5d356c8b1523351a4545f48ac05b">fixed the problem</a>.</p>
<p>It would be useful if the filter would run on the largest possible region by default.</p>

---

## Post #6 by @blowekamp (2019-09-04 14:16 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="8251">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It would be useful if the filter would run on the largest possible region by default.</p>
</blockquote>
</aside>
<p>Of course it should work without this extra call. I narrowed down the issue to streamed execution and the computation of the extrema with the <code>AutoMinimumMaximum</code> option enabled. So it’s not related to the VTK/ITK pipeline interaction as first susspected. I will work on a patch to fix this in ITK.</p>

---
