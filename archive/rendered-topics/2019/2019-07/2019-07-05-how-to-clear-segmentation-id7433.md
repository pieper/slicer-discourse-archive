---
topic_id: 7433
title: "How To Clear Segmentation"
date: 2019-07-05
url: https://discourse.slicer.org/t/7433
---

# How to clear segmentation?

**Topic ID**: 7433
**Date**: 2019-07-05
**URL**: https://discourse.slicer.org/t/how-to-clear-segmentation/7433

---

## Post #1 by @ungi (2019-07-05 14:20 UTC)

<p>Hi, is there an easy way to clear a segmentation from Python? (Or from the widget, by the way.) I’m now doing this in a module that automatically clears a segmentation after saving it. But this looks like a hack rather than the proper way to clear the segmentation contents.</p>
<pre><code>num_segments = selectedSegmentation.GetSegmentation().GetNumberOfSegments()
for i in range(num_segments):
  segmentId = selectedSegmentation.GetSegmentation().GetNthSegmentID(i)
  labelMapRep = selectedSegmentation.GetBinaryLabelmapRepresentation(segmentId)
  labelMapRep.Initialize()
  labelMapRep.Modified()
  selectedSegmentation.Modified()</code></pre>

---

## Post #2 by @cpinter (2019-07-05 14:56 UTC)

<p>I don’t think we ever had a use case where you have to actually clear a segmentation. The python code is fine I think - hack or not - in the absence of a way doing this in the UI.</p>
<p>What you could do is have a segmentation with the empty segments pre-populated (I think this is why you want to clear them so that you have the segments with the same name, color, etc.), then clone the segmentation for each segmenation run. You can clone in the Data module from the right-click menu.</p>

---

## Post #3 by @lassoan (2019-07-05 15:12 UTC)

<p>You can clear the segmentation in many different ways (remove segment, remove representation, make all voxels 0 value, make the extent empty, …). It would be interesting to know what is the use case so that we can find the most suitable solution.</p>

---

## Post #4 by @ungi (2019-07-05 15:49 UTC)

<p>I have a sequence of changing image, and I would like to create a matching sequence of segmentation. I go to the first item in the image sequence, paint a segmentation, then record it in another sequence browser. Then, I would like to iterate this process through items of the image sequence. But I have hundreds of items in a sequence, so I would like to automate the process. I cannot delete the segments or segmentation because I need to keep it in the segmentation sequence browser as a proxy node.<br>
Unfortunately I’m having issues with the code above. So I was hoping there is a more appropriate way to clear the segments.</p>

---

## Post #5 by @lassoan (2019-07-05 18:21 UTC)

<p>We ended up using code in “Logical operators” effect:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/344ced6b1d442275a04eae41029e62502c7a3f23/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorLogicalEffect.py#L251-L257" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/344ced6b1d442275a04eae41029e62502c7a3f23/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorLogicalEffect.py#L251-L257" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/344ced6b1d442275a04eae41029e62502c7a3f23/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorLogicalEffect.py#L251-L257</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="251" style="counter-reset: li-counter 250 ;">
<li>selectedSegmentLabelmap = self.scriptedEffect.selectedSegmentLabelmap()</li>
<li>vtkSegmentationCore.vtkOrientedImageDataResample.FillImage(selectedSegmentLabelmap, 1 if operation == LOGICAL_FILL else 0, selectedSegmentLabelmap.GetExtent())</li>
<li>if bypassMasking:</li>
<li>  slicer.vtkSlicerSegmentationsModuleLogic.SetBinaryLabelmapToSegment(</li>
<li>    selectedSegmentLabelmap, segmentationNode, selectedSegmentID, slicer.vtkSlicerSegmentationsModuleLogic.MODE_REPLACE)</li>
<li>else:</li>
<li>  self.scriptedEffect.modifySelectedSegmentByLabelmap(selectedSegmentLabelmap, slicer.qSlicerSegmentEditorAbstractEffect.ModificationModeSet)</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #6 by @ungi (2019-07-06 05:11 UTC)

<p>Just for completeness of information, I started this thread because I has problems with the cleared segments. I couldn’t repaint on them. But I figured out later that the issue was not in the code that cleared the segments. I’m now use the code Andras quoted, but just FYI the first code also works.</p>

---

## Post #7 by @Sunderlandkyl (2019-07-23 14:42 UTC)

<p>In the latest nightly, there is now an option to clear selected segments from the context menu in the segments table:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a295e0ff91881595115a15ba1c30ef28c272fef8.png" alt="image" data-base62-sha1="ncisMFzjFxQz4mEUep2kB4rpXXq" width="367" height="173"></p>

---

## Post #8 by @ungi (2019-07-23 19:19 UTC)

<p>Great, thanks! Can I be lazy and ask you to please paste here a link to the code that other modules and scripts can call to use this function?</p>

---

## Post #9 by @Sunderlandkyl (2019-07-24 17:18 UTC)

<p>I used the same approach as you to reset the segment from the GUI:</p>
<pre><code class="lang-auto">masterRepresentation.Initialized();
masterRepresentation.Modified();
</code></pre>
<p>I could add a helper method to the module logic that would expose the same function to python if you think it would be useful.</p>

---

## Post #10 by @ungi (2019-07-24 20:05 UTC)

<p>That’s OK. I was just wondering if there is another function that would be preferred. This works fine.</p>

---

## Post #11 by @MLDawn (2023-10-06 20:10 UTC)

<p>Hi Lassoan. I am an absolute beginner with 3DSlicer. Is there a way to clear ONLY the content of a segment node without removing the node itself, using Python? All of the solutions I have found so far, remove the node and the content altogether, as a result, the user will have to keep creating the segmentation nodes in the GUI over and over!  Many thanks for your help. Here is how I get access to the segmentation node, the content of which I would like to clear:</p>
<blockquote>
<p>segmentationNode = slicer.util.getNode(‘Segmentation’)</p>
</blockquote>

---

## Post #12 by @muratmaga (2023-10-06 21:42 UTC)

<p>I tried bing chat with the question <code>how can I clear the contents of a segmentation node in 3D Slicer via python without removing the node</code> and suggested answer seems to work?</p>
<pre><code class="lang-auto">segmentationNode = getNode('Segmentation')
segmentationNode.GetSegmentation().RemoveAllSegments()
</code></pre>
<p>Is this what you want to do?</p>

---

## Post #13 by @MLDawn (2023-10-06 22:27 UTC)

<p>This solution removes the entire segmentation node! I just need to clear the content of it and keep the node itself in the GUI of 3DSlicer. Does this make sense? Thanks</p>

---

## Post #14 by @muratmaga (2023-10-07 03:50 UTC)

<p>No, this only removes all the segments within the segmentation node. Does not remove the segmentation node. Give it a try.</p>

---

## Post #15 by @MLDawn (2023-10-07 03:57 UTC)

<p>I did give it a try but it removed the node completely. I tried it in the Python console of 3DSlicer. The segmentation node disappeared altogether.</p>
<p>Regards<br>
Mehran</p>

---

## Post #16 by @muratmaga (2023-10-07 04:44 UTC)

<p>Thats not what I see on my end. Here is what I did:</p>
<p>I loaded MRHead and created a segmentation with 4 segments as shown.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/67a1e6a463fe02cab36cf0bb6510c5271c5a09db.png" data-download-href="/uploads/short-url/eMM38DhBlLKx4cjKptRCCWI5f3d.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67a1e6a463fe02cab36cf0bb6510c5271c5a09db_2_690x424.png" alt="image" data-base62-sha1="eMM38DhBlLKx4cjKptRCCWI5f3d" width="690" height="424" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67a1e6a463fe02cab36cf0bb6510c5271c5a09db_2_690x424.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67a1e6a463fe02cab36cf0bb6510c5271c5a09db_2_1035x636.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67a1e6a463fe02cab36cf0bb6510c5271c5a09db_2_1380x848.png 2x" data-dominant-color="C3C0BF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2320×1426 585 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>then when I executed the code,</p>
<pre><code class="lang-python">segmentationNode = getNode('MR-head_Seg*')
segmentationNode.GetSegmentation().RemoveAllSegments()
</code></pre>
<p>it simply removed the four segments, but the segmentation node called (MR-head-segmentation) remained (see the output of <code>print(segmentatioNode))</code>. Is this not what you want? If not, I am not sure if I am following what you are trying to do.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f01856f36096cb7326636118915bdfa3a4336c7b.jpeg" data-download-href="/uploads/short-url/yfYJTYRAFFMAPFegc7ZXTb8dgKv.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f01856f36096cb7326636118915bdfa3a4336c7b_2_690x416.jpeg" alt="image" data-base62-sha1="yfYJTYRAFFMAPFegc7ZXTb8dgKv" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f01856f36096cb7326636118915bdfa3a4336c7b_2_690x416.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f01856f36096cb7326636118915bdfa3a4336c7b_2_1035x624.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f01856f36096cb7326636118915bdfa3a4336c7b_2_1380x832.jpeg 2x" data-dominant-color="C0BFBF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2338×1412 375 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #17 by @MLDawn (2023-10-08 02:33 UTC)

<p>Oh my apologies! Apparently,</p>

---

## Post #18 by @MLDawn (2023-10-08 02:40 UTC)

<p>My previous in-complete message was sent by accident!</p>
<p>Many thanks for all the visuals and details. Please let me correct my question. What I am trying to do is to clear the content of the segments, without removing the segments themselves! Sorry for the incorrect question at the beginning, as I am new with 3DSlicer.</p>
<p>The reason I would like to erase the content, is that the user will push a button to save the segmentations, and then another set of DICOM files will be loaded automatically for the user’s annotation. If the segments from the previous round are fully removed, then the user is forced to re-create them from the GUI.</p>
<p>So, this is why I would like to keep the segments but ONLY clear their content.</p>
<p>It is interesting that from the GUI, you can easily do this by right-clicking on the segment and clear the content of the segment! But I cannot find, for the life of me, how I can do this using Python.</p>
<p>Your help will be much appreciated.</p>
<p>Regards<br>
Mehran</p>

---

## Post #19 by @muratmaga (2023-10-10 04:36 UTC)

<p>to clear the contents of a segment within a segmentation node, this seems to work</p>
<pre><code class="lang-python">segmentationNode = getNode('Segmentation')
segmentation = segmentationNode.GetSegmentation()
segmentId = segmentation.GetSegmentIdBySegmentName('Segment_1')
segment = segmentation.GetSegment(segmentId)
segment.RemoveAllRepresentations()
</code></pre>

---

## Post #20 by @MLDawn (2023-10-10 08:45 UTC)

<p>This works in so far as clearing the content. However, I cannot do any segmentation in the GUI after the content of the segmentation is cleared! The second I click on the brush to annotate the Dicom files I get the following error:</p>
<p>[VTK] vtkSegmentationModifier::SetBinaryLabelmapToSegment: Failed to get binary labelmap representation in segmentation</p>
<p>[Qt] void __cdecl qSlicerSegmentEditorAbstractEffect::modifySegmentByLabelmap(class vtkMRMLSegmentationNode *,const char *,class vtkOrientedImageData *,enum qSlicerSegmentEditorAbstractEffect::ModificationMode,const int <span class="chcklst-box fa fa-square-o fa-fw"></span>,bool) : Failed to add modifier labelmap to selected segment</p>

---

## Post #21 by @chir.set (2023-10-10 09:28 UTC)

<aside class="quote no-group" data-username="MLDawn" data-post="11" data-topic="7433">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mldawn/48/66882_2.png" class="avatar"> MLDawn:</div>
<blockquote>
<p>the user will have to keep creating the segmentation nodes in the GUI over and over</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="MLDawn" data-post="20" data-topic="7433">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mldawn/48/66882_2.png" class="avatar"> MLDawn:</div>
<blockquote>
<p>I get the following error:</p>
</blockquote>
</aside>
<p>Just a quick comment. The segments and segmentations are not designed to work the way you are exposing. May be you’ll end up with a working solution. My opinion is that you are writing code over and over again, so that someone does not recreate a deleted segment over and over again. Try to convince your users to follow the designed workflow.</p>
<p>Good luck and regards.</p>

---
