---
topic_id: 19318
title: "Change Interpolation Method"
date: 2021-08-23
url: https://discourse.slicer.org/t/19318
---

# Change interpolation method

**Topic ID**: 19318
**Date**: 2021-08-23
**URL**: https://discourse.slicer.org/t/change-interpolation-method/19318

---

## Post #1 by @riep (2021-08-23 14:53 UTC)

<p>Hi everyone,</p>
<p>Is there a  way to interactively change the interpolation method of a volume node. I have tried the following withtout success.</p>
<blockquote>
<p>volumeNode=getNode(“my_volume_name”)<br>
volumeNode.GetDisplayNode().SetInterpolation(2)</p>
</blockquote>
<p>But nothing changed. So I then tried.</p>
<blockquote>
<p>volumeNode.GetDisplayNode().UpdateImageDataPipeline()<br>
volumeNode.GetDisplayNode().Modifed()</p>
</blockquote>
<p>Nothing changed.</p>
<p>Thanks for your help,<br>
Pierre</p>

---

## Post #2 by @jamesobutler (2021-08-23 15:29 UTC)

<p>It appears you are trying to use PhongInterpolation for more realistic shading?</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Libs/MRML/Core/vtkMRMLDisplayNode.h#L54-L57">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Libs/MRML/Core/vtkMRMLDisplayNode.h#L54-L57" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Libs/MRML/Core/vtkMRMLDisplayNode.h#L54-L57" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Libs/MRML/Core/vtkMRMLDisplayNode.h#L54-L57</a></h4>



    <pre class="onebox"><code class="lang-h">
      <ol class="start lines" start="54" style="counter-reset: li-counter 53 ;">
          <li>typedef enum {</li>
          <li>  FlatInterpolation = 0,</li>
          <li>  GouraudInterpolation,</li>
          <li>  PhongInterpolation</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Have you tried the “Lights” module for various interactive lighting techniques for shading?</p><aside class="quote" data-post="1" data-topic="8804">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-module-to-customize-lighting-in-3d-view/8804">New module to customize lighting in 3D view</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    A new experimental module, “Lights”, was added to “Sandbox” extension that allows you to change lightkit parameters with a simple GUI. See a short demo video here: 

If we get the feedback that this module is useful then we’ll consider adding it to the Slicer core.
  </blockquote>
</aside>


---

## Post #3 by @riep (2021-08-23 15:38 UTC)

<p>I was probably misled by the name, sorry this is not what I wanted to do. I would like to change the interpolation in the MPR views of a particular volumeNode</p>

---

## Post #4 by @riep (2021-08-23 15:57 UTC)

<p>it seems that interpolation is hard-coded to linear if interpolate is on or nearest neighbor if interpolate is off</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Libs/MRML/Logic/vtkMRMLSliceLayerLogic.cxx#L671">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Libs/MRML/Logic/vtkMRMLSliceLayerLogic.cxx#L671" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Libs/MRML/Logic/vtkMRMLSliceLayerLogic.cxx#L671" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Libs/MRML/Logic/vtkMRMLSliceLayerLogic.cxx#L671</a></h4>



  <pre class="onebox">    <code class="lang-cxx">
      <ol class="start lines" start="661" style="counter-reset: li-counter 660 ;">
          <li>
          </li>
<li>vtkMTimeType oldReSliceMTime = this-&gt;Reslice-&gt;GetMTime();</li>
          <li>vtkMTimeType oldReSliceUVWMTime = this-&gt;ResliceUVW-&gt;GetMTime();</li>
          <li>vtkMTimeType oldAssign = this-&gt;AssignAttributeTensorsToScalars-&gt;GetMTime();</li>
          <li>vtkMTimeType oldLabel = this-&gt;LabelOutline-&gt;GetMTime();</li>
          <li>vtkMTimeType oldLabelUVW = this-&gt;LabelOutlineUVW-&gt;GetMTime();</li>
          <li>
          </li>
<li>if ( (this-&gt;VolumeNode-&gt;GetImageData() &amp;&amp; labelMapVolumeDisplayNode) ||</li>
          <li>     (scalarVolumeDisplayNode &amp;&amp; scalarVolumeDisplayNode-&gt;GetInterpolate() == 0))</li>
          <li>  {</li>
          <li class="selected">  this-&gt;Reslice-&gt;SetInterpolationModeToNearestNeighbor();</li>
          <li>  this-&gt;ResliceUVW-&gt;SetInterpolationModeToNearestNeighbor();</li>
          <li>  }</li>
          <li>else</li>
          <li>  {</li>
          <li>  this-&gt;Reslice-&gt;SetInterpolationMode(this-&gt;InterpolationMode);</li>
          <li>  this-&gt;ResliceUVW-&gt;SetInterpolationMode(this-&gt;InterpolationMode);</li>
          <li>  }</li>
          <li>
          </li>
<li>// for tensors reassign scalar data</li>
          <li>if ( volumeNode &amp;&amp; volumeNode-&gt;IsA("vtkMRMLDiffusionTensorVolumeNode") )</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @lassoan (2021-08-23 16:02 UTC)

<p>Volume interpolation in slice views is controlled by the <a href="https://apidocs.slicer.org/master/classvtkMRMLScalarVolumeDisplayNode.html#ac524f069eead3bf4414eadfc3e563483">Interpolate</a> flag. However, the flag is already enabled by default, so I would not recommend touching it. If you disable it then you introduce artifacts in the image reconstruction. See more details <a href="https://discourse.slicer.org/t/volume-display-interpolate-turned-off-by-default-in-newest-stable/13918/17">here</a>.</p>
<p>If you just want to show boundaries of voxels then don’t use nearest neighbor interpolation, because it would ruin the image by aliasing artifacts and by the increased image contrast that is needed to make the random noise between neighbor voxels large enough so that your eye can make out individual voxels. Instead you can use <a href="https://discourse.slicer.org/t/volume-display-interpolate-turned-off-by-default-in-newest-stable/13918/10">this small Python code snippet</a> to show the voxel grid in slice views.</p>
<p>If you want to have higher-order interpolation then you can enable it like this for a specific view (it is not exposed on the GUI, as the feature remained in an experimental stage; see some more information <a href="https://discourse.vtk.org/t/vtkimageactor-interpolation-limited-to-linear/4858/4?u=lassoan">here</a>):</p>
<pre><code class="lang-python">sliceNode = slicer.mrmlScene.GetNodeByID('vtkMRMLSliceNodeRed')
slicer.app.applicationLogic().GetSliceLogic(sliceNode).GetBackgroundLayer().SetInterpolationMode(vtk.VTK_RESLICE_CUBIC)
slicer.util.forceRenderAllViews()
</code></pre>

---

## Post #6 by @riep (2021-08-23 16:08 UTC)

<p>Exactly what I was looking for thanks Andras !<br>
Pierre</p>

---

## Post #7 by @lassoan (2021-08-23 16:10 UTC)

<p>Which solution did you choose?</p>

---

## Post #8 by @riep (2021-08-23 16:12 UTC)

<p>the last one, but for now I do not see any change between linear and cubic</p>

---

## Post #9 by @riep (2021-08-23 16:15 UTC)

<p>Sorry, I should have zoomed more to see differences. So this is working.</p>

---

## Post #10 by @lassoan (2021-08-23 16:32 UTC)

<p>Great!</p>
<p>Probably it would not have any downsides to add an application setting to choose between linear and cubic interpolation. If you find that cubic interpolation works better and you don’t want to maintain a custom solution then it would be great if you could submit a pull request that adds this option (a combobox in application settings that sets an InterpolationType enum in vtkMRMLSliceNode and vtkMRMLSliceLayerLogic uses that value to set interpolation type in the reslice filter). Probably cubic could be the default but the user could change it in the application settings to linear.</p>

---
