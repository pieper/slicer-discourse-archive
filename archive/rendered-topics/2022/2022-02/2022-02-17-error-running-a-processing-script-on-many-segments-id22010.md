# Error running a processing script on many segments

**Topic ID**: 22010
**Date**: 2022-02-17
**URL**: https://discourse.slicer.org/t/error-running-a-processing-script-on-many-segments/22010

---

## Post #1 by @hourglassnam (2022-02-17 06:12 UTC)

<p>Dear community,<br>
I have problem writing for loop.<br>
When I try the script, it works just fine but it would not work as soon as I try to loop.<br>
There must be something wrong with my script, but I can’t figure it out.<br>
Here is part of my script with 3 segments rather than all 20 I usually use.</p>
<pre><code class="lang-python">&gt; # Create segmentation Node
&gt; segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
&gt; segmentationNode.CreateDefaultDisplayNodes()
&gt;  
&gt; #make new segment with custom color
&gt; s=getNode('vtkMRMLSegmentationNode1')
&gt; se=s.GetSegmentation()
&gt;  
&gt; Seg01 = slicer.vtkSegment()
&gt; Seg01 .SetName("Seg_01")
&gt; Seg01 .SetColor([1.0,0.0,0.0])
&gt; se.AddSegment(Seg01 ,"Seg_01 ")
&gt;  
&gt; Seg02= slicer.vtkSegment()
&gt; Seg02.SetName("Seg_02")
&gt; Seg02.SetColor([1.0,0.7,0.2])
&gt; se.AddSegment(Seg02,"Seg_02")
&gt;  
&gt; Seg03= slicer.vtkSegment()
&gt; Seg03.SetName("Seg_03")
&gt; Seg03.SetColor([1.0,1.0,0.0])
&gt; se.AddSegment(Seg03,"Seg_03")
&gt;  
&gt;  
&gt; segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
&gt; segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
&gt; segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
&gt; segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
&gt;  
&gt; segmentEditorWidget.setSegmentationNode(s)
&gt;  
&gt; # Set overwrite mode: 0/1/2 -&gt; overwrite all/visible/none
&gt; segmentEditorNode.SetOverwriteMode(2)
&gt;  
&gt; # Get the segment IDs
&gt; Seg01 = se.GetSegmentIdBySegmentName('Seg_01')
&gt; Seg02 = se.GetSegmentIdBySegmentName('Seg_02')
&gt; Seg03 = se.GetSegmentIdBySegmentName('Seg_03')
&gt;  
&gt;# This is the part that does not work properly
&gt; segIDs=['Seg01','Seg02','Seg03']
&gt; 
&gt;  for segID in segIDs:
&gt;&gt; segmentEditorNode.SetSelectedSegmentID(segID)
&gt;&gt; segmentEditorWidget.setActiveEffectByName("Threshold")
&gt;&gt; effect = segmentEditorWidget.activeEffect()
&gt;&gt; effect.setParameter("MinimumThreshold","80")
&gt;&gt; effect.self().onApply()
</code></pre>
<p>In my actual script with all 20 segments, the python interpreter returns the below messages.</p>
<pre><code class="lang-python">&gt; r,g,b = segmentationNode.GetSegmentation().GetSegment(segmentID).GetColor()
&gt; AttributeError: ‘NoneType’Object has no attribute ‘GetColor’
</code></pre>
<p>I will be grateful to hear any pieces of advice.<br>
Thank you always.</p>

---

## Post #2 by @mikebind (2022-02-17 17:28 UTC)

<p>Your error message means that <code>segmentationNode.GetSegmentation().GetSegment(segmentID)</code> at that point is returning <code>None</code>.  This is likely because there is no segment with the given <code>segmentID</code> in the segmentation.  Check that the segment ID’s are correct (and are not <code>None</code> themselves).</p>

---

## Post #3 by @hourglassnam (2022-02-18 06:07 UTC)

<p>Thank you for your reply!<br>
After your advice, I looked back in to the segment names and was able to make the for loop to work by fixing below!</p>
<pre><code class="lang-auto">&gt; segIDs=[‘Seg01’,‘Seg02’,‘Seg03’]
</code></pre>
<p>to</p>
<pre><code class="lang-auto">&gt; segIDs=[Seg01,Seg02,Seg03]
</code></pre>
<p>I still have one more question though.<br>
This works with other modules such as Logical Operators but when I tried thresholding, it keep gives a error message saying that the Master volume is not set as either the forground or background.</p>
<pre><code class="lang-auto">&gt; segmentEditorNode.SetSelectedSegmentID(Seg01)
&gt; segmentEditorWidget.setActiveEffectByName("Threshold")
&gt; effect = segmentEditorWidget.activeEffect()
&gt; effect.setParameter("MinimumThreshold","80")
&gt; effect.self().onApply()
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c0a20880858e019bdd6ccf3de80b66a9683d5db.jpeg" data-download-href="/uploads/short-url/fpLgmGZo7F1sShhntjpBtTjOCjF.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6c0a20880858e019bdd6ccf3de80b66a9683d5db_2_690x369.jpeg" alt="image" data-base62-sha1="fpLgmGZo7F1sShhntjpBtTjOCjF" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6c0a20880858e019bdd6ccf3de80b66a9683d5db_2_690x369.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6c0a20880858e019bdd6ccf3de80b66a9683d5db_2_1035x553.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6c0a20880858e019bdd6ccf3de80b66a9683d5db_2_1380x738.jpeg 2x" data-dominant-color="C2A9AD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1028 272 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I thought this may happened because I did not set the master volume so I added below but it did not worked as well.</p>
<pre><code class="lang-auto">&gt; segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)
</code></pre>
<p>Can you please give me advice on this situation?</p>

---

## Post #4 by @lassoan (2022-02-18 16:40 UTC)

<p>To avoid seeing the warning above, set the master volume as either the foreground or background volume as shown <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#iterate-over-current-visible-slice-views-and-set-foreground-and-background-images">here</a>.</p>

---

## Post #5 by @hourglassnam (2022-02-21 02:19 UTC)

<p>Thank you for your help!<br>
It works fine now.<br>
I followed the link you showed and set my master volume as forground and background using below</p>
<blockquote>
<p>slicer.util.setSliceViewerLayers(background=masterVolumeNode, foreground=masterVolumeNode)</p>
</blockquote>

---
