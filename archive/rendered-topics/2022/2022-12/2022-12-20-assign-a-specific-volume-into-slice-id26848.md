# Assign a specific volume into slice

**Topic ID**: 26848
**Date**: 2022-12-20
**URL**: https://discourse.slicer.org/t/assign-a-specific-volume-into-slice/26848

---

## Post #1 by @Jinhee_Jang (2022-12-20 13:52 UTC)

<p>Hi, I have a short question.</p>
<p>I am browsing multiple MR images at the same time.<br>
After loading multiple images (usually done by drag and drop), I want to assign a specific volume using its IDs (such as ‘vtkMRMLScalarVolumeNode11’) into a particular slice( such as ‘slicer5’ or ‘Red’).</p>
<p>I googled it here and there, but I could not find a good answer, so I am posting it here.</p>
<p>Thank you for your time!</p>

---

## Post #2 by @pieper (2022-12-20 14:11 UTC)

<p>These instructions should help:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#iterate-over-current-visible-slice-views-and-set-foreground-and-background-images" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#iterate-over-current-visible-slice-views-and-set-foreground-and-background-images</a></p>
<p>If you need something finer grained, see the implementation of <code>setSliceViewerLayers</code> here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/5a3f3381d16c7151b695d2597695951869c9981d/Base/Python/slicer/util.py#L514-L571">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/5a3f3381d16c7151b695d2597695951869c9981d/Base/Python/slicer/util.py#L514-L571" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/5a3f3381d16c7151b695d2597695951869c9981d/Base/Python/slicer/util.py#L514-L571" target="_blank" rel="noopener">Slicer/Slicer/blob/5a3f3381d16c7151b695d2597695951869c9981d/Base/Python/slicer/util.py#L514-L571</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="514" style="counter-reset: li-counter 513 ;">
          <li>def setSliceViewerLayers(background='keep-current', foreground='keep-current', label='keep-current',</li>
          <li>                         foregroundOpacity=None, labelOpacity=None, fit=False, rotateToVolumePlane=False):</li>
          <li>    """ Set the slice views with the given nodes.</li>
          <li>
          </li>
<li>    If node ID is not specified (or value is 'keep-current') then the layer will not be modified.</li>
          <li>
          </li>
<li>    :param background: node or node ID to be used for the background layer</li>
          <li>    :param foreground: node or node ID to be used for the foreground layer</li>
          <li>    :param label: node or node ID to be used for the label layer</li>
          <li>    :param foregroundOpacity: opacity of the foreground layer</li>
          <li>    :param labelOpacity: opacity of the label layer</li>
          <li>    :param rotateToVolumePlane: rotate views to closest axis of the selected background, foreground, or label volume</li>
          <li>    :param fit: fit slice views to their content (position&amp;zoom to show all visible layers)</li>
          <li>    """</li>
          <li>    import slicer</li>
          <li>
          </li>
<li>    def _nodeID(nodeOrID):</li>
          <li>        nodeID = nodeOrID</li>
          <li>        if isinstance(nodeOrID, slicer.vtkMRMLNode):</li>
          <li>            nodeID = nodeOrID.GetID()</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/5a3f3381d16c7151b695d2597695951869c9981d/Base/Python/slicer/util.py#L514-L571" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Jinhee_Jang (2022-12-20 14:35 UTC)

<p>Thanks, Steve.<br>
I read the instructions and tried it.<br>
But it is about overlaying images, not assigning a specific image node into a specific location of slices, such as a Red or Green panel.<br>
Maybe the setSliceViewerLayers function could do the job that I want to do, and I am trying to read the suggested github page.</p>
<p>Thank you again!</p>

---

## Post #4 by @pieper (2022-12-20 14:58 UTC)

<p>I’m not sure, but it sounds like you want this:</p>
<pre><code class="lang-auto">n =  slicer.util.getNode("YourVolumeNode")
for color in ["Red", "Yellow", "Green"]:
  slicer.app.layoutManager().sliceWidget(color).sliceLogic().GetSliceCompositeNode().SetForegroundVolumeID(n.GetID())
</code></pre>
<p>From <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#iterate-over-current-visible-slice-views-and-set-foreground-and-background-images:~:text=Show%20volume%20in%20selected%20views%3A">here</a>.</p>

---

## Post #5 by @Jinhee_Jang (2022-12-20 22:22 UTC)

<p>Yes, it works!<br>
Thank you <a class="mention" href="/u/pieper">@pieper</a></p>
<p>Here is what I used.</p>
<pre><code class="lang-auto">ID = "vtkMRMLScalarVolumeNode1" # node ID for image volume
Panel = "Red" # node name for panel view (slice)
slicer.app.layoutManager().sliceWidget(Panel).sliceLogic().GetSliceCompositeNode().SetBackgroundVolumeID(ID)

</code></pre>
<p>Thank you again!</p>

---

## Post #6 by @sulaimanvesal (2023-06-22 23:44 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a></p>
<p>I have the following code and I want to show an MRI and US images side by side with their corresponding labels. The code does partially the job but still these two parts are not working:</p>
<ul>
<li>The Yellow panel does not show the axial plane, even though I set it in the custom layout.</li>
<li>I want each panel show the segmentation of that image only, not overlapping between the panel.</li>
</ul>
<p>Thank you for the help.</p>
<p>P.S. You may ask why not manually doing this, well we have around 2000 pairs of US and MRI images, and we need to do this somehow automated using python for a multi-reader study.</p>
<pre><code class="lang-auto">      customLayout = """
      &lt;layout type="horizontal" split="true"&gt;
        &lt;item&gt;
        &lt;view class="vtkMRMLSliceNode" singletontag="Red"&gt;
          &lt;property name="orientation" action="default"&gt;Axial&lt;/property&gt;
          &lt;property name="viewlabel" action="default"&gt;R&lt;/property&gt;
          &lt;property name="viewcolor" action="default"&gt;#F34A33&lt;/property&gt;
        &lt;/view&gt;
        &lt;/item&gt;
        &lt;item&gt;
        &lt;view class="vtkMRMLSliceNode" singletontag="Yellow"&gt;
          &lt;property name="orientation" action="default"&gt;Axial&lt;/property&gt;
          &lt;property name="viewlabel" action="default"&gt;Y&lt;/property&gt;
          &lt;property name="viewcolor" action="default"&gt;#F34A33&lt;/property&gt;
        &lt;/view&gt;
        &lt;/item&gt;
      &lt;/layout&gt;
      """
      # Built-in layout IDs are all below 100, so you can choose any large random number
      # for your custom layout ID.
      customLayoutId=501

      layoutManager = slicer.app.layoutManager()
      layoutManager.layoutLogic().GetLayoutNode().AddLayoutDescription(customLayoutId, customLayout)

      # Switch to the new custom layout
      layoutManager.setLayout(customLayoutId)
      slicer.mrmlScene.Clear(0)
      
      # Input nodes
      # layoutManager.sliceWidget('Red').sliceLogic().GetSliceCompositeNode().SetForegroundVolumeID(volumeNode.GetID())
      # Setvolume node as the foreground volume of the Red slice widget.
      # layoutManager.sliceWidget('Yellow').sliceLogic().GetSliceCompositeNode().SetForegroundVolumeID(trusvloumeNode.GetID()) 
      mriVolumeNode = slicer.util.loadVolume(mri_path)
      trusVolumeNode = slicer.util.loadVolume(trus_path)
      
      mriSegmentationNode = slicer.util.loadSegmentation(mri_seg_path)           
      trusSegmentationNode = slicer.util.loadSegmentation(trus_seg_path)
      
      layoutManager.sliceWidget('Red').sliceLogic().GetSliceCompositeNode().SetBackgroundVolumeID(mriVolumeNode.GetID())
      layoutManager.sliceWidget('Yellow').sliceLogic().GetSliceCompositeNode().SetBackgroundVolumeID(trusVolumeNode.GetID())
      
      layoutManager.sliceWidget('Red')
      displayNode = mriSegmentationNode.GetDisplayNode()
      displayNode.SetOpacity3D(0.4)  # Set overall opacity of the segmentation
      displayNode.SetSegmentOpacity3D('Segment_1', 0.2)  # Set opacity of a single segment
      segment_prostate = mriSegmentationNode.GetSegmentation().GetSegment('Segment_1')
      # Segment color is not just a display property, but it is stored in the segment itself (and stored in the segmentation file)
      displayNode.SetSegmentOverrideColor('Segment_1', 1, 0, 0)  # blue
      displayNode.SetSegmentVisibility2DFill('Segment_1', 0)  # blue

      layoutManager.sliceWidget('Yellow')
      displayNode = trusSegmentationNode.GetDisplayNode()
      displayNode.SetOpacity3D(0.4)  # Set overall opacity of the segmentation
      displayNode.SetSegmentOpacity3D('Segment_1', 0.2)  # Set opacity of a single segment
      segment_prostate = trusSegmentationNode.GetSegmentation().GetSegment('Segment_1')
      # Segment color is not just a display property, but it is stored in the segment itself (and stored in the segmentation file)
      displayNode.SetSegmentOverrideColor('Segment_1', 1, 0, 0)  # blue
      displayNode.SetSegmentVisibility2DFill('Segment_1', 0)  # blue
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f2fb6fa4cdd151fd561c29b10bed984d10dfc0fe.jpeg" data-download-href="/uploads/short-url/yFwfkl19C9PdO5t4dRETtxhxW5U.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f2fb6fa4cdd151fd561c29b10bed984d10dfc0fe_2_690x343.jpeg" alt="image" data-base62-sha1="yFwfkl19C9PdO5t4dRETtxhxW5U" width="690" height="343" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f2fb6fa4cdd151fd561c29b10bed984d10dfc0fe_2_690x343.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f2fb6fa4cdd151fd561c29b10bed984d10dfc0fe_2_1035x514.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f2fb6fa4cdd151fd561c29b10bed984d10dfc0fe_2_1380x686.jpeg 2x" data-dominant-color="515050"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×957 113 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @pearsonm (2023-06-23 01:05 UTC)

<aside class="quote no-group" data-username="sulaimanvesal" data-post="6" data-topic="26848">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sulaimanvesal/48/10463_2.png" class="avatar"> sulaimanvesal:</div>
<blockquote>
<p><code>layoutManager.sliceWidget('Yellow')</code></p>
</blockquote>
</aside>
<p>For Axial display you can do</p>
<blockquote>
<p>sliceNode = layoutManager.sliceWidget(“Yellow”).mrmlSliceNode()<br>
sliceNode.SetOrientation(“Axial”)</p>
</blockquote>

---
