---
topic_id: 46524
title: "Bug in ImportLabelmapToSegmentationNode if multiple parent transforms"
date: 2026-03-21
url: https://discourse.slicer.org/t/46524
last_bumped: 2026-03-26T22:30:19.398Z
---

# Bug in ImportLabelmapToSegmentationNode if multiple parent transforms

**Topic ID**: 46524
**Date**: 2026-03-21
**URL**: https://discourse.slicer.org/t/bug-in-importlabelmaptosegmentationnode-if-multiple-parent-transforms/46524

---

## Post #1 by @mikebind (2026-03-21 00:27 UTC)

<p>A labelmap imported to a segmentation using ImportLabelmapToSegmentationNode is transformed incorrectly if there are multiple parent transforms soft-applied. I have been using ImportLabelmapToSegmentationNode successfully for a long time with a transformed labelmap with no problem, but I just ran a case where there were multiple parent transforms (i.e. the parent transform had a parent transform applied) and the converted segmentation node put the segments in the wrong place.  With a little testing, it appears that each transform is at least partially applied, but the total transformation is incorrect.</p>
<p>I reproduced this effect with SampleData and saved the scene, it is available here: <a href="https://drive.google.com/file/d/1fXu8EHHY4jzL3COEn8sjXXz1FmgdGdiq/view?usp=sharing" rel="noopener nofollow ugc">https://drive.google.com/file/d/1fXu8EHHY4jzL3COEn8sjXXz1FmgdGdiq/view?usp=sharing</a></p>
<p>In that scene, I created a segmentation with 3 segments and exported that to a labelmap (these align perfectly). Then I created two transforms which each apply a rotation around the AP axis and a SI translation.  Then I soft-applied the first transform to the labelmap and the original segmentation, and then soft-applied the second transform to the first transform.  Lastly, I ran ImportLabelmapToSegmentationNode on the transformed labelmap, creating the segmentation node labeled SegmentationFromLabelMap in the scene.  With both the SegmentationFromLabelMap and LabelMapFromSegmentation shown, you can see that they do not align the way they should.  It looks like an equal amount of rotation has been applied, but not an equal total translation.  So, it’s not the case that only the first parent transform has been applied, because then the rotation amounts would not be equal. If I combine the two transforms into one (clone the first, apply the second, and harden) and use that, then the output segmentation is aligned with the transformed labelmap (correct behavior). Is it possible that the parent transforms are being applied in the wrong order?</p>
<p>Using Slicer 5.10.0 on Windows 11. The conversion was carried out using the following convenience wrapper around ImportLabelmapToSegmentationNode</p>
<pre data-code-wrap="python"><code class="lang-python">def labelMapToSeg(labelmapNode, createClosedSurfaces=True):
    """Converts an input labelmap node to a segmentation node"""
    segNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
    slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(
        labelmapNode, segNode
    )
    if createClosedSurfaces:
        segNode.CreateClosedSurfaceRepresentation()
    return segNode
</code></pre>
<p>To recreate:</p>
<pre data-code-wrap="python"><code class="lang-python"># Load scene linked above, then run
labelNode = getNode('LabelMapFromSegmentation')
segNode = labelMapToSeg(labelNode)
segNode.SetName('NewSegmentationFromLabelMap')
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2a397ebc08997f3c91a3f7e0bb981cae9663eb8.png" data-download-href="/uploads/short-url/u3oLuZ6cIoFxWPxME5i2Yav3CiI.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2a397ebc08997f3c91a3f7e0bb981cae9663eb8.png" alt="image" data-base62-sha1="u3oLuZ6cIoFxWPxME5i2Yav3CiI" width="570" height="491"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">570×491 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2026-03-25 12:51 UTC)

<p>Thanks for the detailed report.  Probably the underlying code is only taking the partent transform into account and not the full transform to world.  This should probably be a one-line change to use the right call.  Did you look at the code?  I’ll bet this is something fixable, either by looking at the code ones self or with the help of an LLM, probably easier with the slicer-skill.</p>

---

## Post #3 by @mikebind (2026-03-25 19:17 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="46524">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Probably the underlying code is only taking the partent transform into account</p>
</blockquote>
</aside>
<p>This was my initial guess also, but does not appear to be the case.  If that were so, the amount of rotation as well as translation would have been incorrect, since each of the two parent transforms apply a rotation.</p>
<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="46524">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Did you look at the code?</p>
</blockquote>
</aside>
<p>I didn’t.  I have more limited ability to follow the C++ code, and have never successfully set up a Slicer build environment (which would be needed to test a corrected solution, I think).  I was hoping that a clear, reproducible example with the bug report would be enough for someone with these things already set up to take a look and hopefully see the problem and fix. I too suspect that the fix will be straightforward once identified.</p>
<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="46524">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>help of an LLM, probably easier with the slicer-skill</p>
</blockquote>
</aside>
<p>I am looking forward to getting this working and trying it out for development and for problems such as these in the future. I can’t do it on my work computer because of sensible corporate security concerns, but I will be trying to get Claude with the slicer-skill set up on a home computer as soon as I can manage to get the time.</p>

---

## Post #4 by @mikebind (2026-03-25 19:29 UTC)

<p>The relevant section of the code appears to be:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/159a50752bcdbfa08fd4754bea75d906aaddddcb/Modules/Loadable/Segmentations/Logic/vtkSlicerSegmentationsModuleLogic.cxx#L1459">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/159a50752bcdbfa08fd4754bea75d906aaddddcb/Modules/Loadable/Segmentations/Logic/vtkSlicerSegmentationsModuleLogic.cxx#L1459" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/159a50752bcdbfa08fd4754bea75d906aaddddcb/Modules/Loadable/Segmentations/Logic/vtkSlicerSegmentationsModuleLogic.cxx#L1459" target="_blank" rel="noopener nofollow ugc">Modules/Loadable/Segmentations/Logic/vtkSlicerSegmentationsModuleLogic.cxx</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/Slicer/blob/159a50752bcdbfa08fd4754bea75d906aaddddcb/Modules/Loadable/Segmentations/Logic/vtkSlicerSegmentationsModuleLogic.cxx#L1459" rel="noopener nofollow ugc"><code>159a50752</code></a>
</div>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="1449" style="counter-reset: li-counter 1448 ;">
          <li></li>
          <li>// Split labelmap node into per-label image data</li>
          <li></li>
          <li>vtkNew&lt;vtkIntArray&gt; labelValues;</li>
          <li>vtkSlicerSegmentationsModuleLogic::GetAllLabelValues(labelValues.GetPointer(), labelmapNode-&gt;GetImageData());</li>
          <li></li>
          <li>vtkSmartPointer&lt;vtkOrientedImageData&gt; labelOrientedImageData = vtkSmartPointer&lt;vtkOrientedImageData&gt;::New();</li>
          <li>labelOrientedImageData-&gt;vtkImageData::DeepCopy(labelmapNode-&gt;GetImageData());</li>
          <li>labelOrientedImageData-&gt;SetGeometryFromImageToWorldMatrix(labelmapIjkToRasMatrix);</li>
          <li></li>
          <li class="selected">// Apply parent transforms if any</li>
          <li>if (labelmapNode-&gt;GetParentTransformNode() || segmentationNode-&gt;GetParentTransformNode())</li>
          <li>{</li>
          <li>  vtkSmartPointer&lt;vtkGeneralTransform&gt; labelmapToSegmentationTransform = vtkSmartPointer&lt;vtkGeneralTransform&gt;::New();</li>
          <li>  vtkSlicerSegmentationsModuleLogic::GetTransformBetweenRepresentationAndSegmentation(labelmapNode, segmentationNode, labelmapToSegmentationTransform);</li>
          <li>  vtkOrientedImageDataResample::TransformOrientedImage(labelOrientedImageData, labelmapToSegmentationTransform);</li>
          <li>}</li>
          <li></li>
          <li>MRMLNodeModifyBlocker blocker(segmentationNode);</li>
          <li>for (int labelIndex = 0; labelIndex &lt; labelValues-&gt;GetNumberOfValues(); ++labelIndex)</li>
          <li>{</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>So, something is going wrong with either getting the transform or applying it.  Both of those functions are clearly intended to handle general transformations, so they should be set up to properly handle a hierarchy of linear transforms.</p>

---

## Post #5 by @pieper (2026-03-26 20:51 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="3" data-topic="46524">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>I am looking forward to getting this working and trying it out for development and for problems such as these</p>
</blockquote>
</aside>
<p>This is an excellent example of where we are today in terms of coding tools.</p>
<p>Just to give you a sense of what you can expect, I prompted my local Claude to use the slicer-skill like so:</p>
<blockquote>
<p>Can you read this forum post and suggest an answer to Mike’s question?  <a href="https://discourse.slicer.org/t/bug-in-importlabelmaptosegmentationnode-if-multiple-parent-transforms/46524">https://discourse.slicer.org/t/bug-in-importlabelmaptosegmentationnode-if-multiple-parent-transforms/46524</a></p>
</blockquote>
<p>It too quite some time looking around, examining source code, git logs, etc.</p>
<p>The reasoning is quite interesting to skim.  It’s too long to post here but you can look at it here: <a href="https://gist.github.com/pieper/703d37355796cd876d84f866d10cdd2f" class="inline-onebox">reasoning for this question: https://discourse.slicer.org/t/bug-in-importlabelmaptosegmentationnode-if-multiple-parent-transforms/46524/3 · GitHub</a></p>
<p>In the end it came up with this suggested answer which I didn’t check but sounds awfully good to me.</p>
<blockquote>
<p><img src="https://emoji.discourse-cdn.com/twitter/robot.png?v=15" title=":robot:" class="emoji" alt=":robot:" loading="lazy" width="20" height="20"> This post contains AI-generated content.</p>
</blockquote>
<p>Now I have a clear picture of the bug. Here’s the answer I’d suggest posting to Mike’s forum question:</p>
<hr>
<p><strong>Root Cause Found</strong></p>
<p>The bug is in <code>vtkOrientedImageDataResample::IsTransformLinear</code> in <a href="https://github.com/Slicer/Slicer/blob/main/Libs/vtkSegmentationCore/vtkOrientedImageDataResample.cxx">vtkOrientedImageDataResample.cxx</a> around line 987.</p>
<p><strong>What happens:</strong></p>
<p>When <code>ImportLabelmapToSegmentationNode</code> handles parent transforms, it calls <code>GetTransformBetweenRepresentationAndSegmentation</code> → <code>vtkMRMLTransformNode::GetTransformBetweenNodes</code>, which correctly traverses the full transform hierarchy and builds a <code>vtkGeneralTransform</code> using <strong><code>PostMultiply</code></strong> mode. With PostMultiply, transforms are appended to the end of the pipeline and applied in order (T1 first, T2 second).</p>
<p>So for your setup (labelmapNode → T1 → T2 → world), <code>GetTransformBetweenNodes</code> correctly builds <code>T2 * T1</code> (T1 applied first, then T2).</p>
<p>Then <code>TransformOrientedImage</code> calls <code>IsTransformLinear</code>, which extracts the chained transforms into a <code>vtkTransform</code> using its <strong>default PreMultiply</strong> mode. In PreMultiply mode, each new <code>Concatenate(M)</code> does <code>T = T_old * M</code>, which reverses the effective application order. So it builds <code>T1 * T2</code> instead of <code>T2 * T1</code> — the transforms are applied backwards.</p>
<p><strong>Why single transforms work:</strong> With only one transform in the chain, there’s no ordering issue. The first (and only) transform is correct regardless of pre/post multiply mode.</p>
<p><strong>Why you see “equal rotations but wrong translations”:</strong> If T1 and T2 both rotate around the same axis, their rotations commute (<code>T1_rot * T2_rot = T2_rot * T1_rot</code>), so the rotation result looks the same either way. But translations do NOT commute under rotation, so the translation accumulation is incorrect with the reversed order.</p>
<p><strong>The Fix</strong></p>
<p>In <code>vtkOrientedImageDataResample.cxx</code>, in <code>IsTransformLinear</code> around line 1006, add one line to switch to PostMultiply before the concatenation loop:</p>
<pre><code class="lang-auto">vtkGeneralTransform* generalTransform = vtkGeneralTransform::SafeDownCast(inputTransform);
if (generalTransform)
{
  outputLinearTransform-&gt;PostMultiply();  // &lt;-- add this line
  for (int transformIndex = 0; transformIndex &lt; generalTransform-&gt;GetNumberOfConcatenatedTransforms(); ++transformIndex)
  {
    ...
    outputLinearTransform-&gt;Concatenate(currentLinearTransform);
  }
  return true;
}
</code></pre>
<p><strong>Immediate Workaround</strong></p>
<p>Until this is fixed, you can harden the transforms before importing:</p>
<pre><code class="lang-auto">labelmapNode.HardenTransform()
segNode = labelMapToSeg(labelmapNode)
</code></pre>
<p>This would be a good candidate for a PR against <code>Slicer/Libs/vtkSegmentationCore/vtkOrientedImageDataResample.cxx</code>. Note the fix would also affect <code>vtkSegmentation::ApplyLinearTransform</code> which uses the same function.</p>
<hr>
<p>Should I post this response or refine it further? I should mention this analysis is based on reading the code in your local Slicer checkout — it would be good to add a small Python test script to verify before submitting the PR.</p>

---

## Post #6 by @mikebind (2026-03-26 22:09 UTC)

<p>Much appreciated <a class="mention" href="/u/pieper">@pieper</a> !   I had wondered if transform order might have been the issue, but it might have taken me quite some time to realize that the the issue was that the default concatenation multiply order was pre-multiply and the missing piece was to specify post-multiplication. With it pointed out, I agree that this makes good sense, is a plausible way for the bug to have entered the code, and that this is the likely fix.</p>
<aside class="quote no-group" data-username="pieper" data-post="5" data-topic="46524">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Note the fix would also affect <code>vtkSegmentation::ApplyLinearTransform</code> which uses the same function.</p>
</blockquote>
</aside>
<p>If this diagnosis correct, does this mean that segmentations under two parent transforms will also appear in the wrong place?  That’s actually a more serious bug. I’m used to needing to think about whether an export or conversion process in Slicer is going to respect or ignore parent transforms, but I do not worry about arbitrary transform hierarchies soft-applied to basic MRML nodes like segmentation nodes. I assume those always “just work”</p>
<p>For moving forward, I can mark the AI solution as the solution for this thread, but that won’t get the fix into Slicer.  Should I make that change in the cxx file and submit a PR? Open an issue on github?  As mentioned earlier, I don’t have the build system set up, so I can’t actually compile and test the solution, it would just be based on the above “seeming reasonable”.  What would you (or others) recommend?</p>

---

## Post #7 by @pieper (2026-03-26 22:30 UTC)

<p>I agree we should file an issue on github with a link to this thread.  I also think we should have <a class="mention" href="/u/lassoan">@lassoan</a> weigh in since he knows this code well.  Then we can work on a PR to fix this and any related issues.  We can convert your example into a test that will confirm the behavior.  Thanks again for your careful analysis and report <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=15" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p>Regarding a local build, if you are on an apple silicon mac, even a macbook air, the builds are remarkably fast, like under an hour.  (They are still a bit buggy but would work for this kind of debugging).  I’m not sure what the compile times are these days on other platforms but be sure you have a fast disk.  Historically builds on windows were overnight processes.</p>

---
