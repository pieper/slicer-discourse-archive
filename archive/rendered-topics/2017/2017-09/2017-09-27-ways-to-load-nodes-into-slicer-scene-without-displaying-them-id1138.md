---
topic_id: 1138
title: "Ways To Load Nodes Into Slicer Scene Without Displaying Them"
date: 2017-09-27
url: https://discourse.slicer.org/t/1138
---

# Ways to load nodes into Slicer scene WITHOUT displaying them immediately

**Topic ID**: 1138
**Date**: 2017-09-27
**URL**: https://discourse.slicer.org/t/ways-to-load-nodes-into-slicer-scene-without-displaying-them-immediately/1138

---

## Post #1 by @che85 (2017-09-27 20:57 UTC)

<p>Hi Developers,</p>
<p>I am wondering, if it’s possible to load nodes (volume, fiducial) into a Slicer scene without having them displayed immediately within the slice views.</p>
<p>I am asking this, because I want to load a bunch of data programmatically but I don’t want the slice views to flicker for each loaded volume.</p>
<p>Are there any properties that can be set on</p>
<pre><code>slicer.util.loadVolume(...)
slicer.util.loadLabelVolume(...)
slicer.util.load...(...)</code></pre>

---

## Post #2 by @pieper (2017-09-27 21:46 UTC)

<p>There’s a flag on the SliceCompositeNode to turn this off on a per-slice view basis.  It could be good to have some slicer.util or other place to turn them all on or off, but I don’t think that exists yet.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/703557e658c976f7d146ff4c8408ef43ec7dea00/Libs/MRML/Logic/vtkMRMLApplicationLogic.cxx#L124" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/703557e658c976f7d146ff4c8408ef43ec7dea00/Libs/MRML/Logic/vtkMRMLApplicationLogic.cxx#L124" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/703557e658c976f7d146ff4c8408ef43ec7dea00/Libs/MRML/Logic/vtkMRMLApplicationLogic.cxx#L124</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="114" style="counter-reset: li-counter 113 ;">
<li>char *secondID = this-&gt;SelectionNode-&gt;GetSecondaryVolumeID();</li>
<li>char *labelID = this-&gt;SelectionNode-&gt;GetActiveLabelVolumeID();</li>
<li>
</li>
<li>vtkMRMLSliceCompositeNode *cnode;</li>
<li>const int nnodes = this-&gt;External-&gt;GetMRMLScene()-&gt;GetNumberOfNodesByClass("vtkMRMLSliceCompositeNode");</li>
<li>
</li>
<li>for (int i = 0; i &lt; nnodes; i++)</li>
<li>  {</li>
<li>  cnode = vtkMRMLSliceCompositeNode::SafeDownCast (</li>
<li>    this-&gt;External-&gt;GetMRMLScene()-&gt;GetNthNodeByClass( i, "vtkMRMLSliceCompositeNode" ) );</li>
<li class="selected">  if(!cnode-&gt;GetDoPropagateVolumeSelection())</li>
<li>    {</li>
<li>    continue;</li>
<li>    }</li>
<li>  if (layer &amp; vtkMRMLApplicationLogic::BackgroundLayer)</li>
<li>    {</li>
<li>    cnode-&gt;SetBackgroundVolumeID( ID );</li>
<li>    }</li>
<li>  if (layer &amp; vtkMRMLApplicationLogic::ForegroundLayer)</li>
<li>    {</li>
<li>    cnode-&gt;SetForegroundVolumeID( secondID );</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2017-09-29 01:18 UTC)

<p>Background volume and FOV reset on volume loading has bothered me a couple of times, too. I’ve now added a new ‘show’ option (enabled by default) to the <code>Add data</code> dialog for volumes that can be unchecked if the user does not want the volume to be propagated to slice views. See pull request here: <a href="https://github.com/Slicer/Slicer/pull/800">https://github.com/Slicer/Slicer/pull/800</a></p>

---

## Post #4 by @che85 (2017-10-02 14:33 UTC)

<p>Great! Thanks for adding this option Andras.</p>

---

## Post #5 by @mschumaker (2017-10-13 18:15 UTC)

<p>Thank you, that’s a great feature. I had asked something very similar to this post a couple of months ago. If I load a volume with ‘show’ set to False, how would I then display it in one (and only one) of the slice views?</p><aside class="quote quote-modified" data-post="1" data-topic="846">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mschumaker/48/1395_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/override-automatic-display-of-newly-loaded-volume/846">Override automatic display of newly-loaded volume?</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Writing my first module. 
When I use the DICOM widget to load an image set, and use a qMRMLNodeComboBox, the newly-loaded node is automatically displayed in the Red, Yellow, and Green MRML slice views. I’m hoping to override this action, so that the newly-loaded volume is only displayed in either (but only one of) the Red or Yellow view. How would I do that? Thanks. 
Code is below: 
def setup(self):
    ScriptedLoadableModuleWidget.setup(self)

    #Link to image database for SSFP
    self.LoadS…
  </blockquote>
</aside>


---

## Post #6 by @lassoan (2017-10-13 19:40 UTC)

<p>You can use slicer.util.setSliceViewerLayers</p>

---

## Post #7 by @Saima (2019-08-15 11:06 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="1138">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>slicer.util.setSliceViewerLayers</p>
</blockquote>
</aside>
<p>Hi Andras,<br>
I am loading the model node and want it to be displayed automatically using scripting. I am loading it using python scripting. but I need to actually go to models and then click on it to display it but I need an automatic way.= thorugh scripting. how to? please suggest.</p>
<p>Thank you</p>

---

## Post #8 by @lassoan (2019-08-15 15:14 UTC)

<p>If you want to load a volume without showing it, add <code>show=False</code> argument to <code>slicer.util.loadVolume</code>. See list of all options <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.loadVolume" rel="nofollow noopener">here</a>.</p>

---

## Post #9 by @Saima (2019-08-16 07:49 UTC)

<p>loadNodeFromFile <code>returnNode</code> argument is deprecated. Loaded node is now returned directly if <code>returnNode</code> is not specified.</p>
<p>What does this mean I get this when runing the script for loading a modelnode</p>
<p>outputVolume = slicer.util.loadModel(filepath+"\simplification.ply",True)</p>
<p>Also please tell me how to change the 3d display representation of a modelnode in scripting. Example from surface to surface with edges</p>

---

## Post #10 by @lassoan (2019-08-16 11:47 UTC)

<aside class="quote no-group" data-username="Saima" data-post="9" data-topic="1138">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>loadNodeFromFile <code>returnNode</code> argument is deprecated. Loaded node is now returned directly if <code>returnNode</code> is not specified.</p>
<p>What does this mean I get this when runing the script for loading a modelnode</p>
</blockquote>
</aside>
<p>This means you don’t need to specify <code>returnNode=True</code> anymore. If you don’t specify it then only one value, the volume node is returned. This is just a small change in the API to make the syntax simpler.</p>
<aside class="quote no-group" data-username="Saima" data-post="9" data-topic="1138">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>Also please tell me how to change the 3d display representation of a modelnode in scripting. Example from surface to surface with edges</p>
</blockquote>
</aside>
<p>You can change it in the <a href="http://apidocs.slicer.org/master/classvtkMRMLSegmentationDisplayNode.html#aa3b52c05c86a143c9636bf26c8b2d41b">display node</a> of the segmentation node.</p>
<pre><code>segmentationNode.GetDisplayNode().SetOpacity2DOutline() 
</code></pre>
<p>By default outline is displayed, so if you don’t see it then it may be because it is occluded by some other content (for example, after you imported the segmentation from labelmap node, you did not hide or delete the  labelmap node).</p>

---

## Post #11 by @Saima (2019-08-22 04:47 UTC)

<p>Hi Andras,<br>
I need to do the following with scripting.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d4da30e9023ce23d3a084e19e002fa3ce1417f1.png" data-download-href="/uploads/short-url/1TGxHc0zZ0ZlsXQVL22tJlcUAhz.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d4da30e9023ce23d3a084e19e002fa3ce1417f1_2_690x371.png" alt="image" data-base62-sha1="1TGxHc0zZ0ZlsXQVL22tJlcUAhz" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d4da30e9023ce23d3a084e19e002fa3ce1417f1_2_690x371.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d4da30e9023ce23d3a084e19e002fa3ce1417f1_2_1035x556.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d4da30e9023ce23d3a084e19e002fa3ce1417f1_2_1380x742.png 2x" data-dominant-color="CFD1DD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1034 107 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>On the left side in the REpresentation I am selecting surface with edges. I need to do it through scripting on the model surface. Any suggestions?</p>
<p>nn = n.GetModelDisplayNode()<br>
nn.EdgeVisibilityOn()</p>
<p>I used the above it displays the edges. Is this true for every model either surface or volumetric mesh model.<br>
is  there any page online of scripting available for help?</p>

---

## Post #12 by @Alex_Vergara (2019-08-22 07:59 UTC)

<aside class="quote no-group" data-username="Saima" data-post="11" data-topic="1138">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>is there any page online of scripting available for help?</p>
</blockquote>
</aside>
<p>Use this <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/ScriptRepository - Slicer Wiki</a></p>

---

## Post #13 by @lassoan (2019-08-22 13:44 UTC)

<p>C++ API documentation is available here: <a href="https://apidocs.slicer.org/" rel="nofollow noopener">https://apidocs.slicer.org/</a></p>
<p>For example, documentation of model display node: <a href="https://apidocs.slicer.org/master/classvtkMRMLModelDisplayNode.html" rel="nofollow noopener">https://apidocs.slicer.org/master/classvtkMRMLModelDisplayNode.html</a></p>

---

## Post #14 by @ibro45 (2024-09-26 02:52 UTC)

<p>Thank you!</p>
<p><code>show=False</code> doesn’t seem to exist for <code>slicer.util.loadSegmentation</code>, is there any workaround?</p>

---

## Post #15 by @lassoan (2024-09-26 04:41 UTC)

<p>You can hide the segmentation immediately after loading. If it still shows up for a moment then you can pause rendering before you start loading and resume rendering after you completed loading and made the segmentation hidden.</p>
<p>Alternatively, you can save the segmentation and its display node into a scene (.mrml or .mrb file) and load that. Display properties that are specified in the display node are applied immediately. If the visibility is turned off in the display node then the segmentation will not be displayed upon loading the scene.</p>

---

## Post #16 by @ibro45 (2024-09-26 15:36 UTC)

<p>Thank you so much, <code>slicer.app.layoutManager().setRenderPaused(True)</code> was perfect!</p>

---
