---
topic_id: 490
title: "Model Undercuts Removal By Label Map Addition"
date: 2017-06-13
url: https://discourse.slicer.org/t/490
---

# Model Undercuts Removal by Label Map Addition

**Topic ID**: 490
**Date**: 2017-06-13
**URL**: https://discourse.slicer.org/t/model-undercuts-removal-by-label-map-addition/490

---

## Post #1 by @patmo141 (2017-06-13 02:36 UTC)

<p>Operating system: Win 10 64 Bit<br>
Slicer version: 4.7 Nightly</p>
<p>Background:  Undercuts are important in dental CAD because for two rigidly mating objects (for example teeth and an appliance), a path of insertion is necessary or else the parts will bind.  This is also useful in many other applications outside of dentistry</p>
<p>Goal:  I would like to create a Module which takes as input a closed STL or other model surface, and outputs a closed surface which has all undercuts from a given direction removed.</p>
<p>Overall Plan:  Create a label map from the model, and add layers above to all layers below it, ensuring that the model is always monotonically widening wrt to the desired insertion axis.<br>
-Import the model<br>
-Transform the model so that Z axis is aligned with desired insertion axis<br>
-Create volume based on desired slice thickness<br>
-Create label map from the model<br>
-Modify the label map by adding the layers “downward” across the volume<br>
-Recompute surface representation<br>
-Export</p>
<p>I’ll report back here as progress continues. Any tips appreciated!</p>

---

## Post #2 by @lassoan (2017-06-13 15:44 UTC)

<p>This sounds like a good approach. You may use Crop Volume module (even from your own module, programmatically) to create a reference volume with any size, axis directions (you can rotate the ROI by applying a transform to it), and any resolution.</p>
<p>You may use Segmentations module to convert between labelmap and closed surface representations: you can import your model, Segmentations can automatically create a labelmap representation; make it the master representation; process it; and at the end you can export the segment back to a model.</p>

---

## Post #3 by @patmo141 (2017-06-19 03:07 UTC)

<p>Progress Update 1 (Should I edit original post or keep adding replies?)</p>
<p>-A simple UI with a model select node, and a push button (More parameters to be added later)</p>
<p>On Push Button Code:</p>
<ul>
<li>The model bounding box is calculated</li>
<li>Slice thickness, and number of slices are calculated</li>
<li>A new volume is added to the MRML Scene</li>
<li>A transform node is added that translates volume to fit the model</li>
</ul>
<p>I verify this by going to the crop volume Module after I run my script and creating a new annotation ROI and fit ROI to volume.</p>
<aside class="onebox githubgist">
  <header class="source">
      <a href="https://gist.github.com/patmo141/1878acf70d45e4048699417a1238f053#file-modelundercutremoval-py" target="_blank" rel="nofollow noopener">gist.github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://gist.github.com/patmo141/1878acf70d45e4048699417a1238f053#file-modelundercutremoval-py" target="_blank" rel="nofollow noopener">https://gist.github.com/patmo141/1878acf70d45e4048699417a1238f053#file-modelundercutremoval-py</a></h4>

<p>
</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #4 by @lassoan (2017-06-19 05:03 UTC)

<p>Thanks for the update. Nice progress. A couple of suggestions:</p>
<ul>
<li>It seems that you use some very old template for your extension. Download the latest nightly build of Slicer (it works well and there are many bugfixes and improvements compared to the latest stable version) and use its Extension Wizard module to generate an up-to-date module template.</li>
<li>Create a new project on github and keep updating that instead of sharing code in some temporary gists (make sure to include all the files that Extension Wizard generated - it will allow you to submit your module to the Slicer appstore when it’s ready)</li>
<li>As a next step, I would recommend to have a look at Segmentations, as it allows seamless conversion between labelmaps and models. See <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/SegmentStatistics/SegmentStatistics.py#L447-L459">self-test of Segment Statistics module</a> for an example of how to create segments from models.</li>
<li>You don’t need to create a linear transform to position your volume: a volume can be fully positioned, scaled, and rotated by <a href="http://apidocs.slicer.org/master/classvtkMRMLVolumeNode.html#a55550614d4cc322eed7bc9ed533dfed4">setting its IJK to RAS transform</a>. Once you have your volume, set it as reference geometry in your segmentation node (segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(…))</li>
<li>To update your segment with undercut:
<ul>
<li>Change master representation to binary labelmap (<a href="http://apidocs.slicer.org/master/classvtkMRMLSegmentationNode.html#a59f156080fdf87acd9d35f36056c928e">http://apidocs.slicer.org/master/classvtkMRMLSegmentationNode.html#a59f156080fdf87acd9d35f36056c928e</a>)</li>
<li>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_a_representation_of_a_segment">Get labelmap representation of a segment</a> by calling segmentationNode.GetBinaryLabelmapRepresentation(segmentID)</li>
<li>Modify the labelmap’s imagedata: go through slice by slice and combine them using numpy (see <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/EditorLib/WandEffect.py#L280-L286">how to access voxels as a numpy array here</a>), and finally</li>
<li>Export the processed segment to a model node, using <a href="http://apidocs.slicer.org/master/classvtkSlicerSegmentationsModuleLogic.html#a4ee8fb7834b01b8f06b41ccc7938570c">segmentations module logic’s ExportSegmentToRepresentationNode</a>).</li>
</ul>
</li>
</ul>

---

## Post #5 by @patmo141 (2017-06-19 12:05 UTC)

<p>Re:  Extension Wizard.  I have been following tutorial from Sonia Pujol and Steve Pieper for my Module Template.  I will use the wizard and re-package once I get the initial workflow</p>
<p>Re Git:  Absolutely.  Most of my projects are github repos.  In fact I just used Gist to get a quick show and tell <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Re:  Segmentation self test:<br>
I get an error with this line.  First I used inputModel.GetPolyData() using my own input model, then I tried using a vtk.vtkSphereSource() from the example to see if it was my model.  I’m using nightly from 6/11/2017 so I will download todays and try again but perhaps there is an error in that line?</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/SegmentStatistics/SegmentStatistics.py#L459" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/SegmentStatistics/SegmentStatistics.py#L459" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Modules/Scripted/SegmentStatistics/SegmentStatistics.py#L459</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="449" style="counter-reset: li-counter 448 ;">
<li>
</li>
<li>def getPluginByKey(self, key):</li>
<li>  """Get plugin responsible for obtaining measurement value for given key"""</li>
<li>  for plugin in self.plugins:</li>
<li>    if plugin.toShortKey(key) in plugin.keys:</li>
<li>      return plugin</li>
<li>  return None</li>
<li>
</li>
<li>def getMeasurementInfo(self, key):</li>
<li>  """Get information (name, description, units, ...) about the measurement for the given key"""</li>
<li class="selected">  plugin = self.getPluginByKey(key)</li>
<li>  if plugin:</li>
<li>    return plugin.getMeasurementInfo(plugin.toShortKey(key))</li>
<li>  return None</li>
<li>
</li>
<li>def getStatisticsValueAsString(self, segmentID, key):</li>
<li>  statistics = self.getStatistics()</li>
<li>  if statistics.has_key((segmentID, key)):</li>
<li>    value = statistics[segmentID, key]</li>
<li>    if isinstance(value, float):</li>
<li>      return "%0.3f" % value # round to 3 decimals</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Traceback (most recent call last):<br>
File “C:/Dev/slicer_scripts/ModelUndercutRemoval.py”, line 173, in onHelloWorldButtonClicked<br>
segmentationNode.AddSegmentFromClosedSurfaceRepresentation (sphereSource.GetOutput(), segmentationNode.GetSegmentation().GenerateUniqueSegmentID(“Test”))<br>
AttributeError: ‘vtkCommonCorePython.vtkObject’ object has no attribute ‘GenerateUniqueSegmentID’</p>
<p>Things are moving along nicely!  Thanks for you help and pointers.</p>
<p>-P</p>

---

## Post #6 by @lassoan (2017-06-19 15:50 UTC)

<aside class="quote no-group" data-username="patmo141" data-post="5" data-topic="490">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/ee7513/48.png" class="avatar"> patmo141:</div>
<blockquote>
<p>Traceback (most recent call last):<br>
File “C:/Dev/slicer_scripts/ModelUndercutRemoval.py”, line 173, in onHelloWorldButtonClicked<br>
segmentationNode.AddSegmentFromClosedSurfaceRepresentation (sphereSource.GetOutput(), segmentationNode.GetSegmentation().GenerateUniqueSegmentID(“Test”))<br>
AttributeError: ‘vtkCommonCorePython.vtkObject’ object has no attribute ‘GenerateUniqueSegmentID’</p>
</blockquote>
</aside>
<p>To avoid this error, you need to import vtkSegmentationCore:</p>
<pre><code>import vtkSegmentationCorePython as vtkSegmentationCore
</code></pre>
<p>Soon this import will be done automatically - see <a href="https://issues.slicer.org/view.php?id=4385" class="inline-onebox">Import vtkSegmentationCorePython and vtkAddonPython by default · Issue #4385 · Slicer/Slicer · GitHub</a>.</p>

---

## Post #7 by @patmo141 (2017-06-19 23:00 UTC)

<ol>
<li>
<p>I used the Extension Wizard to generate cmakelists.txt, a png file.</p>
</li>
<li>
<p>I have uploaded project to a github directory.  It is up to date with current code as seen in the video below.<br>
<a href="https://github.com/patmo141/SlicerModelUndercuts" rel="nofollow noopener">https://github.com/patmo141/SlicerModelUndercuts</a></p>
</li>
<li>
<p>Initial workflow is very close!  I seem to have a problem with the final step of generating a surface from the Label Map.  It’s like it uses the old surface and ignores the new lablel map?  Perhaps I need to delete the old surface model?  See video.</p>
</li>
</ol>
<div class="lazyYT" data-youtube-id="WhwuBuzlaOE" data-youtube-title="Model Undercut Removal in Slicer 3D" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<ol start="4">
<li>After this, i will do code cleanup, start to tweak parameters, and add adjustable direction, add adjustable resolutions, then create a pull request for inclusion with Slicer Modules</li>
</ol>
<p>So far a good time!</p>

---

## Post #8 by @lassoan (2017-06-19 23:53 UTC)

<p>It looks really nice! I think the only step you miss is calling modelLabelMap.Modified() after you’ve modified the modelLabelMap voxels using numpy (around line 175).</p>

---

## Post #9 by @lassoan (2017-06-19 23:58 UTC)

<p>Another small suggestion: instead of switching between Segmentations and Models modules to show/hide segments and models and export segment to model - you can use the Data module for all this. Click on the eye icon to show/hide a node. Right-click on a segmentation node to export to model.</p>

---

## Post #10 by @lassoan (2017-06-20 00:06 UTC)

<aside class="quote no-group" data-username="patmo141" data-post="7" data-topic="490">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/ee7513/48.png" class="avatar"> patmo141:</div>
<blockquote>
<p>I used the Extension Wizard to generate cmakelists.txt, a png file</p>
</blockquote>
</aside>
<p>Use the Extension wizard to create a complete skeleton for your extension and your module (adding just a CMakeListst.txt is not enough; you’ll need a separate subdirectory for your module, within that a Resources, Testing, etc. directory). Add a new module with identical name as your existing module and copy-paste content from your existing module.</p>

---

## Post #11 by @patmo141 (2017-06-20 00:27 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="490">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>modelLabelMap.Modified()</p>
</blockquote>
</aside>
<p>yes this fixed it!  The output model now reflects the label map changes</p>

---

## Post #12 by @lassoan (2019-03-16 18:04 UTC)

<p>A post was split to a new topic: <a href="/t/how-to-install-extensions/6164">How to install extensions?</a></p>

---

## Post #13 by @clement_laplace (2022-03-31 14:10 UTC)

<p>Hello Patrick,</p>
<p>I know it has been a while, but did you get the chance to finish your extension. The github repo does not seem to work as shown in the video. And I wasn’t able to find the option to choose the insertion axis.</p>
<p>Regardless thank you for the work, we are trying to create a module to produce dental surgical guide and this would be a key component.</p>

---
