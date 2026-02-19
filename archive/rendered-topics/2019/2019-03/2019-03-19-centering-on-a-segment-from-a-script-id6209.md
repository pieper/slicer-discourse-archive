---
topic_id: 6209
title: "Centering On A Segment From A Script"
date: 2019-03-19
url: https://discourse.slicer.org/t/6209
---

# Centering on a segment from a script

**Topic ID**: 6209
**Date**: 2019-03-19
**URL**: https://discourse.slicer.org/t/centering-on-a-segment-from-a-script/6209

---

## Post #1 by @fedorov (2019-03-19 14:34 UTC)

<p>I would like to invoke in a script “Jump slices” functionality of Segment Editor. I found <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/SubjectHierarchyPlugins/qSlicerSubjectHierarchySegmentsPlugin.cxx#L776" rel="nofollow noopener">jumpSlices()</a>, but have not figured out yet how to invoke it, given Segmentation node and ID of the segment that I need to jump to.</p>
<p><a class="mention" href="/u/cpinter">@cpinter</a> this must be trivial - can you help?</p>

---

## Post #2 by @fedorov (2019-03-19 14:57 UTC)

<p>Related to this, would it be possible to expose in python <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLSegmentationNode.h#L238-L244" rel="nofollow noopener">GetSegmentCenter()/GetSegmentCenterRAS()</a>?</p>
<p>Meanwhile, I will use the approach <a class="mention" href="/u/che85">@che85</a> implemented in QuantitativeReporting - calculate center outside of Segmentations/Segment logic, and use Markups logic to jump: <a href="https://github.com/QIICR/QuantitativeReporting/blob/master/QuantitativeReporting/QRCustomizations/CustomSegmentEditor.py#L65-L69" rel="nofollow noopener">https://github.com/QIICR/QuantitativeReporting/blob/master/QuantitativeReporting/QRCustomizations/CustomSegmentEditor.py#L65-L69</a>.</p>

---

## Post #3 by @cpinter (2019-03-19 15:11 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="2" data-topic="6209">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>would it be possible to expose in python <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLSegmentationNode.h#L238-L244">GetSegmentCenter()/GetSegmentCenterRAS()</a></p>
</blockquote>
</aside>
<p>Certainly. I think once this is done the script is indeed trivial. I’ll do this change now.</p>

---

## Post #4 by @cpinter (2019-03-19 15:33 UTC)

<p>It’s in. Do you need further help with the script?</p>

---

## Post #5 by @lassoan (2019-03-19 16:40 UTC)

<p>I’ve also added <a href="https://github.com/Slicer/Slicer/commit/913829638f45b7960af78c60c87ea88d65eebfe8" rel="nofollow noopener">VTK size hints</a> to the header file that makes the method return a Python tuple instead of a raw pointer.</p>
<p>We should use these hints everywhere where we return a <code>double*</code> to make the result more Python-friendly. VTK also has hints for range checks on inputs (to prevent crashes in Python caused by trying to get/set an out of range item in a data set).</p>

---

## Post #6 by @fedorov (2019-03-19 16:52 UTC)

<p>Thanks a lot guys! Unfortunately, to help me further, you might need a magic wand - now I need a mac binary with the new features, and also several extensions alongside.</p>
<p>I guess my main worry is that extension builds are completely broken on mac, as I noted in this post, which didn’t get any response: <a href="https://discourse.slicer.org/t/multiple-issues-with-extension-builds/6160" class="inline-onebox">Multiple issues with extension builds</a>.</p>
<p>I guess I should hope that I was wrong and just mis-interpreted the interface of the dashboard, and magically the extensions I need will be accessible tomorrow on mac when I open ExtensionManager…</p>

---

## Post #7 by @fedorov (2019-03-19 20:29 UTC)

<p>Aha! I was in a rush, and glossed over Christian’s code too quickly to realize I could use it easily, since the centroid getter function is static. I can easily solve my jumpSlices() problem with just a few lines, using my existing Slicer binary and extensions. Here’s the recipe in case anyone else needs this too (assumes that the <a href="https://qiicr.gitbooks.io/quantitativereporting-guide/" rel="nofollow noopener">QuantitativeReporting</a> extension is installed!):</p>
<pre><code class="lang-python">from QRCustomizations import CustomSegmentEditor
csl=CustomSegmentEditor.CustomSegmentEditorLogic()
segNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLSegmentationNode")
segmentNode = segNode.GetSegmentation().GetNthSegment(0)
centroid = csl.getSegmentCentroid(segNode, segmentNode)
markupsLogic = slicer.modules.markups.logic()
markupsLogic.JumpSlicesToLocation(centroid[0],centroid[1],centroid[2], False)
</code></pre>
<p><a class="mention" href="/u/cpinter">@cpinter</a> maybe the jumpSlices() function I referenced in the initial post should reuse Markups logic to jump slices to reduce code redundancy? I didn’t look carefully whether there is anything extra done that requires a custom implementation.</p>

---

## Post #8 by @cpinter (2019-03-19 20:46 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="7" data-topic="6209">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>maybe the jumpSlices() function I referenced in the initial post should reuse Markups logic</p>
</blockquote>
</aside>
<p>The gist of the jump slices method in Markups logic is just one line of code. The jumpSlices code in the SH plugin also considers in which views the segmentation is visible, while the Markups one does not (and cannot). Other than that the rest of the code that makes that function long is getting the item, the segmentation, and the segment.</p>

---

## Post #9 by @lassoan (2019-03-19 21:01 UTC)

<p>Using a custom extension is certainly a solution, but in the long term I would recommend developers to use Slicer core functions if available.</p>
<p>Slicer-4.10 returning a swig pointer (such as <code>_000001bfd4897340_p_void</code>) is a minor inconvenience. You can still access the values using the helper function below (in the nightly version the VTK hint is there so the position is directly returned as a Python tuple).</p>
<pre><code class="lang-auto">def getListFromPointer(bufferPtr, scalarType=vtk.VTK_DOUBLE, numberOfElements=3):
  """Convert swig pointer (_..._p_void) to list object"""
  bufferArray = vtk.vtkAbstractArray.CreateArray(vtk.VTK_DOUBLE)
  bufferArray.SetVoidArray(bufferPtr, numberOfElements, True)
  buffer = [bufferArray.GetValue(i) for i in range(numberOfElements)]
  return buffer
</code></pre>
<p>Example usage:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; ptr=getNode('Segmentation').GetSegmentCenter("Segment_1")
&gt;&gt;&gt; ptr
'_000001bfd4897340_p_void'
&gt;&gt;&gt; getListFromPointer(ptr)
[8.254768371581932, -18.07139587402301, -10.214302062987997]
</code></pre>

---

## Post #10 by @fedorov (2019-03-20 02:06 UTC)

<p>Yes, but if an experienced Slicer engineer, such as <a class="mention" href="/u/che85">@che85</a>, made the decision to re-implement this functionality for one reason or another, then maybe there’s a need to revisit something. What are the chances that a beginner developer will figure this out.</p>

---

## Post #11 by @fedorov (2019-03-20 02:11 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="6209">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Slicer-4.10 returning a swig pointer (such as <code>_000001bfd4897340_p_void</code> ) is a minor inconvenience.</p>
</blockquote>
</aside>
<p>Andras, can you share your thought process? I guess it is a minor inconvenience when you know what is going on. I just didn’t want my previous post to make it look as if it was a minor inconvenience for me. I simply had no clue what it means when I saw that p_void.</p>

---

## Post #12 by @lassoan (2019-03-20 04:52 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="11" data-topic="6209">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>Andras, can you share your thought process?</p>
</blockquote>
</aside>
<p>Do you mean how did I know how to access the buffer content? I remembered that someone asked this already on Slicer or VTK mailing list and there was a positive answer, so I knew that it was possible. I google searched for <em>VTK p_void</em> and found a test in VTK source code that showed how to get the values.</p>
<aside class="quote no-group" data-username="fedorov" data-post="10" data-topic="6209">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>Yes, but if an experienced Slicer engineer, such as <a class="mention" href="/u/che85">@che85</a>, made the decision to re-implement this functionality</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/che85">@che85</a> implemented this first, we added it to Slicer core later. I checked how he implemented and probably even used some code from his implementation.</p>
<aside class="quote no-group" data-username="fedorov" data-post="10" data-topic="6209">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>What are the chances that a beginner developer will figure this out.</p>
</blockquote>
</aside>
<p>I agree that it is not easy. I would say a good assumption is that anything that is not super-specific to a project has come up already in some other projects, so there is at least something to start from and the task is to find it. If a Google web search and local search in all Slicer’s source code (including VTK, CTK, ITK, …) does not bring up anything then I would recommend to ask on the Slicer forum.</p>
<p>It would be nice to proactively document things, but it would be a lot of work, not very exciting kind, and would be hard to know what topics we should focus on. In contrast, answering questions on the forum helps people immediately and it also generates an indexed, searchable knowledge base to supplement other forms of documentations. Not perfect system, but considering that we have limited amount of time, it is reasonable.</p>

---

## Post #13 by @fedorov (2019-03-20 13:44 UTC)

<p>Thanks Andras, this is helpful, and I agree with you.</p>
<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="6209">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I would say a good assumption is that anything that is not super-specific to a project has come up already in some other projects, so there is at least something to start from and the task is to find it.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/che85">@che85</a> has been through the experience of implementing things that he thought are of general interest, and abstracted them out into <a href="https://github.com/QIICR/SlicerDevelopmentToolbox">Slicer Development Toolbox</a>. I thought it might be nice to consider this as a central place for the functionality of general interest, which is either not ready for the core, or there are no resources to move it to the core.</p>

---

## Post #14 by @lassoan (2019-03-20 14:13 UTC)

<p>I agree that there are lots of useful features in that toolbox, and the plan is to <a href="https://github.com/QIICR/SlicerDevelopmentToolbox/issues/34" rel="nofollow noopener">gradually move the most useful features into Slicer core</a>. It can indeed serve as a staging area in general.</p>
<p>I also like the approach of testing concepts in a single extension(not in a shared utility extension) then send a pull request to Slicer core. This allows reviewing the code earlier and dealing with smaller chunks of code at once. The disadvantage is that the API is not widely tested, so the API often has to be tuned later to support all important use cases.</p>

---

## Post #15 by @zapaishchykova (2023-05-24 20:24 UTC)

<p>This works as it should; I wonder if by chance there were any recent movements towards moving this into Slicer Core? Or if there is a way to find a centroid without <a href="https://qiicr.gitbooks.io/quantitativereporting-guide/" rel="noopener nofollow ugc">QuantitativeReporting</a> installed?</p>

---

## Post #16 by @rbumm (2023-05-24 21:05 UTC)

<p>You can find a centroid function by using the Segmentstatistics module or calling it from a script.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8a7a9c69b2c2362e6f8e3083939fb1c71a30dc5.png" data-download-href="/uploads/short-url/xc9Zn2z0qerUQ1uaWUHGVikJNlj.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8a7a9c69b2c2362e6f8e3083939fb1c71a30dc5_2_690x461.png" alt="image" data-base62-sha1="xc9Zn2z0qerUQ1uaWUHGVikJNlj" width="690" height="461" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8a7a9c69b2c2362e6f8e3083939fb1c71a30dc5_2_690x461.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8a7a9c69b2c2362e6f8e3083939fb1c71a30dc5.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8a7a9c69b2c2362e6f8e3083939fb1c71a30dc5.png 2x" data-dominant-color="D6D6D3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">939×628 187 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #17 by @zapaishchykova (2023-05-24 21:11 UTC)

<p>is there an example python code for that? is the Segmentstatistics build into core Slicer?</p>

---

## Post #18 by @rbumm (2023-05-25 07:58 UTC)

<p>Yes, please <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-centroid-of-each-segment">see this example </a> in the script repository.</p>

---

## Post #19 by @lassoan (2023-05-25 15:56 UTC)

<p>Since last time this issue was discussed, we added segment center computation method to the segmentation node. This center computation provides a visible part of the largest piece of the segment (while centroid may be in an empty area if the segment consists of multiple islands), so it is ideal for refocusing views to show a segment to the user. See <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#center-all-views-on-a-segment">example in the script repository</a> on how to use it.</p>

---
