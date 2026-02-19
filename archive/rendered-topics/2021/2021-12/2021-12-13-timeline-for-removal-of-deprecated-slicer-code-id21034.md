---
topic_id: 21034
title: "Timeline For Removal Of Deprecated Slicer Code"
date: 2021-12-13
url: https://discourse.slicer.org/t/21034
---

# Timeline for removal of deprecated Slicer code

**Topic ID**: 21034
**Date**: 2021-12-13
**URL**: https://discourse.slicer.org/t/timeline-for-removal-of-deprecated-slicer-code/21034

---

## Post #1 by @chribaue (2021-12-13 15:51 UTC)

<p>The Slicer core team is working towards Slicer 5.0 and in the process removing functionality marked as deprecated. Generally, this is very much appreciated! I am maintaining some of our older extensions and want to make sure that they remain functional. Is there somewhere a list of all deprecated code pieces and a timeline by what date they will be removed?</p>
<p>I am asking because of the following two issues:</p>
<ul>
<li>
<p>A few weeks ago the the <code>vtkMRMLFiducialListNode</code> was removed from Slicer, which broke one of our extensions (<code>PETTumorSegmentation</code>). I’m currently re-working the code to use the <code>vtkMRMLAnnotationControlPointsNode</code> instead, but as of right now, the extension is not functional.</p>
</li>
<li>
<p>I also found that <code>DICOMLoadable</code> is marked as deprecated:<br>
<a href="https://github.com/Slicer/Slicer/blob/4483cc0e6f288b0816b6329f1829d9ef8c5aa81a/Modules/Scripted/DICOMLib/DICOMPlugin.py#L29" class="inline-onebox" rel="noopener nofollow ugc">Slicer/DICOMPlugin.py at 4483cc0e6f288b0816b6329f1829d9ef8c5aa81a · Slicer/Slicer · GitHub</a>. Removing it will affect our <code>Slicer-PETDICOMExtension</code> for loading SUV normalized PET datasets and DICOM RWVM files.<br>
And it will also affect the <code>QuantitativeReporting</code> Extension <a class="mention" href="/u/fedorov">@fedorov</a> which we use for loading DICOM SEG files and TID1500.</p>
</li>
</ul>
<p>I try to avoid any further issues.</p>
<p>Thank you!</p>

---

## Post #2 by @pieper (2021-12-13 16:01 UTC)

<p>Hi Christian -</p>
<p>Thanks for brining this up - we do need to get a better handle on the deprecation process and also communicate how to migrate so that extensions can be better maintained.  It has also happened to me that I found that an <a href="https://github.com/SlicerProstate/SlicerProstate/commit/52b2e04d866fef3fb369486ed63fe95d6a96648f">extension needed to be updated</a>, but there were no documents I could find that described how to migrate (just a note to “use class XX instead”).  Definitely let’s post when such things come up so there’s a record.</p>
<p>For your first issue, I hope it’s just a matter of renaming to follow <a href="https://github.com/Slicer/Slicer/issues/5989">this commit</a>.</p>
<p>For the second, that appears to be a <a href="https://github.com/Slicer/Slicer/commit/2ed907d3eb7b2e57b11bb7dc91f464becda96cce">7 year old comment</a>, so maybe it was pre-mature - I don’t think that code is likely to change soon.  But maybe others can comment.</p>

---

## Post #3 by @jcfr (2021-12-13 16:26 UTC)

<p>Thanks for communicating about this.</p>
<p>Giving sufficient time to extension maintainers is important for the health and sanity of the community.</p>
<p>In  the short term, should we consider re-integrating the <code>vtkMRMLFiducialListNode</code> ?</p>
<h3><a name="p-71095-background-1" class="anchor" href="#p-71095-background-1" aria-label="Heading link"></a>Background</h3>
<p>We aim to communicate about it by:</p>
<ul>
<li>documenting removal of feature on the <a href="https://github.com/Slicer/Slicer/wiki/Roadmap">Roadmap</a>  (also linked from Slicer mediawiki <a href="https://www.slicer.org/wiki/Roadmap">here</a>)</li>
<li>creating issue identifying which extensions need to be updated. For example, see <a href="https://github.com/Slicer/Slicer/pull/4904#issuecomment-622156948">here</a> for removal of  “Editor” and “Charts” legacy modules</li>
</ul>
<p>The removal of the Slicer3 MRML nodes without identifying which extension would be impacted was an oversight (only relying on the fact the class was <a href="https://github.com/Slicer/Slicer/commit/22456c5fc21881b806ed517630c78762470a989c#diff-5ef67e5e1d6de401547ae5fd9d238c0fb65c83cca22280d359b55df04efd5728">marked</a> deprecated in June 2012) was probably not sufficient.</p>

---

## Post #4 by @jamesobutler (2021-12-13 16:38 UTC)

<p><code>vtkMRMLFiducialListNode</code> was removed based on the deprecation from June 2012 which means it had been deprecated for 11.5 years which seems reasonable to assume it has been a long enough period for developers to transition to the replacement.</p>
<p>It was removed from Slicer at this point because it was making development of the most recent replacement, the “Markups” module, more difficult. It seems at a point when maintaining very old code becomes a hindrance of latest development is a good point for removal to reduce burden of developers.<br>
Latest efforts have been marking methods deprecated with runtime warnings to make it clear to developers that the used method should be replaced by the suggested method. Providing deprecation for <code>vtkMRMLFiducialListNode</code> was difficult because the replacement <code>vtkMRMLAnnotationFiducialNode</code> is itself deprecated as of Sept 2013. The latest node object that should be used is the <code>vtkMRMLMarkupsFiducialNode</code>.</p>
<p>Although the recent work makes it clearer to developers what methods are deprecated and provides a suggestion about what methods should be used instead, it doesn’t specify a time when it will be removed from the code.  I’m not aware of a code convention to predefine when something is going to be removed after being deprecated. Usually it seems that once deprecated it is subject for removal at any point in the future. Some deprecated items in Slicer have potential removal dates as stated in <a href="https://github.com/Slicer/Slicer/wiki/Roadmap" class="inline-onebox" rel="noopener nofollow ugc">Roadmap · Slicer/Slicer Wiki · GitHub</a> such as the Annotations module which includes <code>vtkMRMLAnnotationFiducialNode</code> to be removed in May 2023. Do we need to add more dates to everything deprecated to this Slicer roadmap, or do we need insert dates into the code where it automatically goes from being say a runtime warning to a runtime error once it reaches a certain date?</p>

---

## Post #5 by @chribaue (2021-12-13 17:12 UTC)

<p>The Slicer developer team is generally doing a great job communicating changes affecting others ahead of time. Like the heads-up about removing the <code>Legacy Editor</code> was excellent. It was posted as part of the Roadmap and we even received an email that this is coming soon and affecting our extension. We had plenty of time to plan when to transition our code. I can see that the Slicer team is taking this seriously.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a></p>
<blockquote>
<p>In the short term, should we consider re-integrating the <code>vtkMRMLFiducialListNode</code> ?</p>
</blockquote>
<p>I am almost done transitioning our code to vtkMRMLAnnotationControlPointsNode. But I don’t know if this change also affected others or not. Generally, I also agree that this class should get removed from Slicer.</p>
<p>Regarding the deprecated <code>DICOMLoadable</code>. It has also been marked deprecated for 7 years or so already, but it’s not listed for removal in the <a href="https://github.com/Slicer/Slicer/wiki/Roadmap" rel="noopener nofollow ugc">Roadmap</a>. Can I assume that it won’t get removed in the next couple months?</p>
<p>Do you plan to remove any other deprecated code before releasing Slicer 5.0 that is not mentioned in the Roadmap?</p>
<p>Thanks again!</p>

---

## Post #6 by @jamesobutler (2021-12-13 17:38 UTC)

<aside class="quote no-group" data-username="chribaue" data-post="5" data-topic="21034">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chribaue/48/1373_2.png" class="avatar"> chribaue:</div>
<blockquote>
<p>I am almost done transitioning our code to vtkMRMLAnnotationControlPointsNode.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/chribaue">@chribaue</a> Is there a reason you have decided to transition from <code>vtkMRMLFiducialListNode</code> to <code>vtkMRMLAnnotationControlPointsNode</code> which is also deprecated and scheduled for removal in a year? You will probably get many runtime warnings using that method which are pointing you to use <code>vtkMRMLMarkupsFiducialNode</code> instead. I wouldn’t want you to waste effort transitioning to another deprecated object that will have to be fixed again shortly (maybe 1 year timeframe).</p>

---

## Post #7 by @chribaue (2021-12-13 17:44 UTC)

<blockquote>
<p><code>vtkMRMLAnnotationControlPointsNode</code> which is also deprecated and scheduled for removal in a year?</p>
</blockquote>
<p>Thank you for pointing this out. How did I miss that? I’ll transition to the <code>vtkMRMLMarkupsFiducialNode</code>.</p>

---

## Post #8 by @cpinter (2021-12-14 11:09 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="21034">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>For the second, that appears to be a <a href="https://github.com/Slicer/Slicer/commit/2ed907d3eb7b2e57b11bb7dc91f464becda96cce">7 year old comment</a>, so maybe it was pre-mature - I don’t think that code is likely to change soon. But maybe others can comment.</p>
</blockquote>
</aside>
<p>Yes, the second point can be ignored <a class="mention" href="/u/chribaue">@chribaue</a> . My memories from when I added that note are a bit blurry after so many years, but I think in that early stage of the DICOM export / SH work we intended moving the core of the DICOM examine infrastructure to C++. Then we realized that there are Python-only usages and very different scenarios, and we never removed it. Instead, as far as I remember, we added both Qt and VTK counterparts for this Python class and converters among them.</p>
<p>I can remove this note to prevent future confusion because as I see now the Python DICOMLoadable class is not intended to be deprecated.</p>

---

## Post #9 by @chribaue (2021-12-14 14:30 UTC)

<blockquote>
<p>the Python DICOMLoadable class is not intended to be deprecated</p>
</blockquote>
<p><a class="mention" href="/u/cpinter">@cpinter</a> Thank you for clarifying this!</p>

---

## Post #10 by @lassoan (2021-12-14 15:09 UTC)

<p>We added qSlicerDICOMLoadable to have a class that can be conveniently used from both C++ and Python and this meant that the Python-only DICOMLoadable could be removed. Removing the Python class would have reduced code duplication, but it would also have taken away the ability of Python scripted DICOM importers to save arbitrary Python objects into the DICOMLoadable class (no members can be added dynamically to a C++ class). This extra flexibility has been proven to be useful, so it is worth having the duplicate Python and C++ code and therefore the Python class should not be deprecated. <a class="mention" href="/u/cpinter">@cpinter</a> it would be great if you could update the documentation of the class, explaining the rationale for duplication.</p>
<p>If such needs arise often then we should introduce a design for dual-personality Python/C++ classes, which are implemented in C++ but can be monkey-patched like Python classes. Having a <code>self()</code> member to store a Python implementation class (as we do it in many Python scripted C++ class implementation) works, but is somewhat cumbersome to use in Python.</p>

---
