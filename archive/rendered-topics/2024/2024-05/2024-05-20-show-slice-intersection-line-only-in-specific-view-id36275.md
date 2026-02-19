---
topic_id: 36275
title: "Show Slice Intersection Line Only In Specific View"
date: 2024-05-20
url: https://discourse.slicer.org/t/36275
---

# Show slice intersection line only in specific view

**Topic ID**: 36275
**Date**: 2024-05-20
**URL**: https://discourse.slicer.org/t/show-slice-intersection-line-only-in-specific-view/36275

---

## Post #1 by @park (2024-05-20 09:52 UTC)

<p>Hi all,</p>
<p>I would like to show intersection line of 2D view only in Axial view.<br>
I tried codes below, but it still remain other view.</p>
<p>Could I get sloution about this ?</p>
<pre><code class="lang-auto">    def intersectionOnOff(self, flag):
        sliceDisplayNode9 = slicer.app.layoutManager().sliceWidget("Slice9").sliceLogic().GetSliceDisplayNode()
        sliceDisplayNode10 = slicer.app.layoutManager().sliceWidget("Slice10").sliceLogic().GetSliceDisplayNode()
        
        for sliceDisplayNode in [sliceDisplayNode9, sliceDisplayNode10]:
            sliceDisplayNode.SetIntersectingSlicesVisibility(flag)
            sliceDisplayNode.SetSliceIntersectionThickness(10)

        sliceNode = slicer.util.getNode('Slice8')
        sliceNode.Modified()

</code></pre>

---

## Post #2 by @cpinter (2024-05-20 11:29 UTC)

<p>If the views are linked, then changing one will affect all the rest. Make sure linking is off when you set this.</p>

---

## Post #3 by @park (2024-05-20 13:34 UTC)

<p>Hi Casba</p>
<p>Thank you for your reply</p>
<p>Could you give a advise more specific (plz with codes snippet) ?</p>
<p>I would like to remove the lines in Yellow and Green view showed in below figure</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27febf3a3706255324bcd5ca1eeb46d2469d6bd6.gif" data-download-href="/uploads/short-url/5HOpGkQ0yimiqOeJklRrDOKdN6C.gif?dl=1" title="스크린샷 2024-05-20 오후 10.31.46" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27febf3a3706255324bcd5ca1eeb46d2469d6bd6_2_690x210.gif" alt="스크린샷 2024-05-20 오후 10.31.46" data-base62-sha1="5HOpGkQ0yimiqOeJklRrDOKdN6C" width="690" height="210" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27febf3a3706255324bcd5ca1eeb46d2469d6bd6_2_690x210.gif, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27febf3a3706255324bcd5ca1eeb46d2469d6bd6_2_1035x315.gif 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27febf3a3706255324bcd5ca1eeb46d2469d6bd6.gif 2x" data-dominant-color="3F3D37"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">스크린샷 2024-05-20 오후 10.31.46</span><span class="informations">1158×353 64 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @cpinter (2024-05-20 13:59 UTC)

<p>You need the opposite of this one<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#set-all-slice-views-linked-by-default" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#set-all-slice-views-linked-by-default</a></p>

---

## Post #5 by @park (2024-05-21 07:09 UTC)

<p>Hi Csaba</p>
<p>I tried codes like below</p>
<p>When the Slicer first start the lines only on ‘Slice8’ (what I want), but start moving the slice, the other lines showed up in “Slice9” and “Slice10”</p>
<pre><code class="lang-auto">  for view in ["Slice9", "Slice10"]:
  
      sliceLogic = slicer.app.layoutManager().sliceWidget(view).sliceLogic()
      sliceDisplayNode = sliceLogic.GetSliceDisplayNode()
      sliceDisplayNode.SetIntersectingSlicesVisibility(flag)
      sliceDisplayNode.SetIntersectingSlicesLineThicknessMode(1)
      
  sliceCompositeNodes = slicer.util.getNodesByClass("vtkMRMLSliceCompositeNode")
  defaultSliceCompositeNode = slicer.mrmlScene.GetDefaultNodeByClass("vtkMRMLSliceCompositeNode")
  if not defaultSliceCompositeNode:
      defaultSliceCompositeNode = slicer.mrmlScene.CreateNodeByClass("vtkMRMLSliceCompositeNode")
      defaultSliceCompositeNode.UnRegister(None)  # CreateNodeByClass is factory method, need to unregister the result to prevent memory leaks
      slicer.mrmlScene.AddDefaultNode(defaultSliceCompositeNode)
  
  sliceCompositeNodes.append(defaultSliceCompositeNode)
  for sliceCompositeNode in sliceCompositeNodes:
      sliceCompositeNode.SetLinkedControl(False)
      sliceCompositeNode.SetHotLinkedControl(False)
          
  sliceNode = slicer.util.getNode('Slice8')
  sliceNode.Modified()
</code></pre>

---

## Post #6 by @park (2024-05-28 11:20 UTC)

<p>Hi all,</p>
<p>I posted a question last time but did not get solution, so I’m posting it again.</p>
<p>I created four 2D slice views looks like the video below.<br>
<strong>Among these, I only want to display the intersection view in the axial window.</strong></p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af4c4d6513e518d871ed9652d527b774a8f976bb.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba2b4b33518942a010496c80ca91fc55d9eda924.png">
  </div><p></p>
<p>To achieve this, I tried changing the visibility to 0 or modifying the LinkedControl as shown below, but I observed that the intersection line reappeared when I moved the slice.</p>
<ol>
<li>
<p><code>sliceDisplayNode.SetIntersectingSlicesVisibility(0)</code></p>
</li>
<li>
<p><code>sliceCompositeNode.SetLinkedControl(False)</code></p>
</li>
</ol>
<p>Additionally, I performed SlabReconstruction on the leftmost panoramic view, but the line corresponding to the slab appeared, which interferes with the visualization.</p>
<p>Therefore, my questions are as follows:</p>
<ul>
<li>
<p>How can I display the intersection line only in the axial view?</p>
</li>
<li>
<p>How can I remove the lines related to the slab?<br>
(When I enable slab reconstruction with <code>sliceNode.SetSlabReconstructionEnabled(True)</code>, the line is generated, and I couldn’t find a way to turn it off.)</p>
</li>
</ul>
<hr>
<ul>
<li>In addition, How can I change the thickness of the intersection line?<br>
(<code>sliceDisplayNode.SetIntersectingSlicesLineThicknessMode(2)</code> does not work.)</li>
</ul>

---

## Post #7 by @pieper (2024-05-28 18:46 UTC)

<p>I suspect nobody has tried these exact features before so nobody has an out-of-the-box answer for you.  But I think you can figure this out by digging into the code a bit - what you describe shouldn’t be that much different from other view-specific visibility controls.  It would be best if you find a way to generalize the implementation in Slicer so these are easy to control, so if you can find a good architectures please contribute back, but since you are building your own custom app, you can even control these in an application-specific way that you keep in your codebase.</p>

---
