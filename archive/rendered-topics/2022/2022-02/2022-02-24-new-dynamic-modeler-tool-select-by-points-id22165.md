---
topic_id: 22165
title: "New Dynamic Modeler Tool Select By Points"
date: 2022-02-24
url: https://discourse.slicer.org/t/22165
---

# New Dynamic Modeler Tool: Select by Points

**Topic ID**: 22165
**Date**: 2022-02-24
**URL**: https://discourse.slicer.org/t/new-dynamic-modeler-tool-select-by-points/22165

---

## Post #1 by @mau_igna_06 (2022-02-24 20:08 UTC)

<div class="youtube-onebox lazy-video-container" data-video-id="Klsi6x3F5D4" data-video-title="Select By Points Tool, Dynamic Modeler, 3D Slicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=Klsi6x3F5D4" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/Klsi6x3F5D4/maxresdefault.jpg" title="Select By Points Tool, Dynamic Modeler, 3D Slicer" width="" height="">
  </a>
</div>

<p>Select by points tool is available on the Dynamic Modeler module since end of October 2021 Slicer Preview Release</p>
<p>This tools allows you to create 2 types of output models from an input model, a fiducial list, a selection-distance and a selection-algorithm.</p>
<p>One of the possible outputs is copy of the input model with selection scalars (unselected=0, selected=1) according to the selection-algorithm and selection-distance using the fiducial points as seeds.</p>
<p>The other possible output crops out the part of the input model that is selected.</p>
<p>This tool was developed ad-honorem by:</p>
<ul>
<li>Mauro I. Dominguez</li>
<li>Andras Lasso (Perklab)</li>
</ul>
<p>This tool allows partial mesh registration workflows like weight-painting ICP on Blender.</p>
<p>Related: <a href="https://discourse.slicer.org/t/partial-surface-registration-tutorial/21118" class="inline-onebox">Partial Surface Registration Tutorial</a></p>

---

## Post #2 by @Moh_d_Al-Watary (2022-06-12 13:38 UTC)

<p>Hi dear, thank you so much for sharing. Actually I am conducting a project to measure the distance of zygoma bone between T1 (taken after a week of operation) and T2 (taken after 6 months of operation).<br>
I want to know if there is a displacement and if yes how much was in mm and in which direction.</p>
<p>My questions:</p>
<ol>
<li>I am using Pick’n paint, model to model distance, and mesh statistics to export the value in excel file: in the new release of the 3d slicer, I can not use pick’n paint properly: as when trying to add a fiducial point: automatically a lot of points are added!!! previously you send me this answer of using dynamic modeler tool: when I have watched this demo, it is on the same bone not in two models as my case! so how can I solve this problem?<br>
Thank you again and sorry to bother you.</li>
</ol>

---

## Post #3 by @mau_igna_06 (2022-06-12 13:42 UTC)

<p>You can consider your two bones at different timestamps as two different models</p>

---

## Post #4 by @Moh_d_Al-Watary (2022-06-12 13:49 UTC)

<p>actually they are, I am doing the followings:</p>
<ol>
<li>import both DICOM, transformation, rigid registration with Elastix module, then segment each one as volume, saved each one independently.</li>
<li>open again both models to start doing the steps mentioned in previous message.</li>
</ol>
<p>My question:<br>
how to solve the problem of automatic many points addition that I am facing with the new release version of the 3D Slicer?’<br>
How dynamic modeler could be used to add fiducial points on T1 model then measure the distance between these points and their matching ones on T2 model? as you mentioned in previous answer.<br>
Thank you</p>

---

## Post #5 by @Moh_d_Al-Watary (2022-06-12 13:54 UTC)

<p>thank you, but what do you mean by (at different timestampes)!</p>

---

## Post #6 by @mau_igna_06 (2022-06-12 14:04 UTC)

<p>Please see this link</p><aside class="quote quote-modified" data-post="1" data-topic="21118">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/partial-surface-registration-tutorial/21118">Partial Surface Registration Tutorial</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi devs. 
I have made a tutorial for Partial Surface Registration, something similar to weight-painting ICP that is done in Blender. 
Here you can access it: 

If there are no suggestions for corrections I’ll later upload it to Youtube. 
Mauro
  </blockquote>
</aside>

<p>You just need to replace the deformed and normal bone from the video for your T1 and T2 bone models…</p>
<p>If it is not clear enough please let me know</p>

---

## Post #7 by @Moh_d_Al-Watary (2022-06-12 14:18 UTC)

<p>Thank you so much for your rapid reply.<br>
Actually it is so clear and this is to do registration of two models.<br>
My question actually was how to calculate the displacement amount after doing the registration step of the two models in regard to the ROI which is in my case the zygoma bone?</p>

---

## Post #8 by @mau_igna_06 (2022-06-12 14:21 UTC)

<p><a class="mention" href="/u/manjula">@manjula</a> could you help?</p>
<p>I think you need to use the model2model distance extension</p>

---

## Post #9 by @Moh_d_Al-Watary (2022-06-12 14:26 UTC)

<p>exactly, so you mean after doing the registration the next step is to do partial surface registration ( formed by the zygomatic bone of T1, in my case) in the dynamic modeler module then using model to model distance and then mesh statistics to export the values?</p>

---

## Post #10 by @mau_igna_06 (2022-06-12 14:33 UTC)

<p>I think it is as you explained but I would only do the partial surface registration</p>

---

## Post #11 by @eliagre (2023-02-22 14:44 UTC)

<p>Hello,</p>
<p>Thank you for this function! Though, I found that there are only two possibilities for output nodes at the moment: “Model with selection scalars” and “Model of the selected cells”. Is there a way to obtain a “model of the unselected cells” as output? I tried multiple things, but can’t seem to obtain the required model.</p>
<p>What I tried: I can visualize the selection with the “Model with selection scalars” and even “remove (i.e. turn invisible)” the “Model of the selected cells” by lowering the scalar threshold under 1. So, it is only showing the unselected cells, but I don’t find how the export this visualisation/selection as a model.<br>
I also tried to subtract the “Model of the selected cells” from the input node with the “combine models” function from the Sandbox extension. This gives me an error message, the one that is discussed on this page: <a href="https://github.com/zippy84/vtkbool/issues/40" class="inline-onebox" rel="noopener nofollow ugc">Difference of meshes sometimes an empty mesh · Issue #40 · zippy84/vtkbool · GitHub</a>.</p>
<p>Is there another way to obtain this “Model of the unselected cells”?<br>
Thanks in advance!</p>

---

## Post #12 by @mau_igna_06 (2023-02-22 15:49 UTC)

<aside class="quote no-group" data-username="eliagre" data-post="11" data-topic="22165">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/eliagre/48/18509_2.png" class="avatar"> eliagre:</div>
<blockquote>
<p>Is there a way to obtain a “model of the unselected cells” as output?</p>
</blockquote>
</aside>
<p>Yes, you should use vtkThreshold and vtkGeometryFilter on the “Model with selection scalars” Polydata</p>

---

## Post #13 by @eliagre (2023-02-22 16:31 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="12" data-topic="22165">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>Yes, you should use vtkThreshold and vtkGeometryFilter on the “Model with selection scalars” Polydata</p>
</blockquote>
</aside>
<p>Thank you for your fast reply! Could you tell me how should I use these vtkThreshold and vtkGeometryFilter? (My apologies, I’m not familiar with coding in python and quite new to 3DSlicer).<br>
I found how to call on my model (see under), but do not know how to apply the mentioned functions.</p>
<pre><code class="lang-auto">modelNode = slicer.util.getNode("Model")

</code></pre>

---

## Post #14 by @eliagre (2023-02-22 22:41 UTC)

<p>I compilated this piece of code just now. While it gives me an output, this output is empty. Could you tell what I’m doing wrong, please?</p>
<pre><code class="lang-auto">modelNode = slicer.util.getNode("Model")
threshold = vtk.vtkThreshold()
threshold.SetInputConnection(modelNode.GetPolyDataConnection())
threshold.SetThresholdFunction(threshold.THRESHOLD_UPPER)
threshold.SetUpperThreshold(0.9)
surface = vtk.vtkGeometryFilter()
surface.SetInputConnection(threshold.GetOutputPort())
thresholdedModel = slicer.modules.models.logic().AddModel(surface.GetOutputPort())

</code></pre>

---

## Post #15 by @mau_igna_06 (2023-02-22 23:12 UTC)

<p>I think you need to do:</p>
<pre><code class="lang-auto">surface.SetInputConnection(threshold.GetOutputPort())
surface.Update() #This is needed on the last filter to chain execute them
thresholdedModel = slicer.modules.models.logic().AddModel(surface.GetOutput()) # GetOutput() returns Polydata while GetOutputPort() is a cable connection to the geometryFilter
</code></pre>
<p>Let me know how it goes</p>

---

## Post #16 by @eliagre (2023-02-22 23:27 UTC)

<p>Thank you for the advice, but it still doesn’t work. The script returns a new Surface Mesh (vtkPolyData), but it is empty (surface area and such are still 0).</p>

---

## Post #17 by @mau_igna_06 (2023-02-22 23:32 UTC)

<p>Please check here:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/SlicerSurfaceToolbox/blob/master/DynamicModeler/Logic/vtkSlicerDynamicModelerSelectByPointsTool.cxx">
  <header class="source">

      <a href="https://github.com/Slicer/SlicerSurfaceToolbox/blob/master/DynamicModeler/Logic/vtkSlicerDynamicModelerSelectByPointsTool.cxx" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/SlicerSurfaceToolbox/blob/master/DynamicModeler/Logic/vtkSlicerDynamicModelerSelectByPointsTool.cxx" target="_blank" rel="noopener nofollow ugc">Slicer/SlicerSurfaceToolbox/blob/master/DynamicModeler/Logic/vtkSlicerDynamicModelerSelectByPointsTool.cxx</a></h4>


      <pre><code class="lang-cxx">/*==============================================================================

  Copyright (c) Laboratory for Percutaneous Surgery (PerkLab)
  Queen's University, Kingston, ON, Canada. All Rights Reserved.

  See COPYRIGHT.txt
  or http://www.slicer.org/copyright/copyright.txt for details.

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.

  This file was originally developed by Mauro I. Dominguez.

==============================================================================*/

#include "vtkSlicerDynamicModelerSelectByPointsTool.h"

</code></pre>



  This file has been truncated. <a href="https://github.com/Slicer/SlicerSurfaceToolbox/blob/master/DynamicModeler/Logic/vtkSlicerDynamicModelerSelectByPointsTool.cxx" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
And use it as example</p>

---

## Post #18 by @eliagre (2023-02-23 09:07 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="17" data-topic="22165">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>And use it as example</p>
</blockquote>
</aside>
<p>I’ve been trying to use your script as an example, but it is hard for me (I’m a newbie and not familiar with python or C++ (I think?) at all). So my apologies for the questions.</p>
<pre><code class="lang-auto">modelNode = slicer.util.getNode("Model")

#it seems these lines from your script may be useful here, but I don't know how to translate them to python
vtkPointData* pointScalars = vtkPointData::SafeDownCast(inputMesh_WorldWithSelection-&gt;GetPointData());
    pointScalars-&gt;AddArray(outputSelectionArray);
#inputMesh_WorldWithSelection should be replaced with modelNode

threshold = vtk.vtkThreshold()
threshold.SetInputConnection(modelNode.GetPolyDataConnection())
threshold.SetThresholdFunction(threshold.THRESHOLD_UPPER)
threshold.SetUpperThreshold(0.5)
threshold.Update() #added this line
surface = vtk.vtkGeometryFilter()
surface.SetInputConnection(threshold.GetOutputPort())
surface.Update()
thresholdedModel = slicer.modules.models.logic().AddModel(surface.GetOutput())

</code></pre>
<p>As this didn’t seem to work out (couldn’t figure out how to convert from one language to the other), I tried a different approach, but ran into another error message. Would this approach even be viable?</p>
<pre><code class="lang-auto">modelNode = slicer.util.getNode("Model")
scalars = arrayFromModelPointData(modelNode, 'Selection')
filter_arr = []
for element in scalars:
	if element &gt; 1: 
		filter_arr.append(True)
	else: 
		filter_arr.append(False)
filtered = modelNode[filter_arr]
thresholdedModel = slicer.modules.models.logic().AddModel(filtered.GetOutput())
</code></pre>
<pre><code class="lang-auto">Error message: 
Traceback (most recent call last):
  File "&lt;string&gt;", line 9, in &lt;module&gt;
TypeError: 'MRMLCore.vtkMRMLModelNode' object is not subscriptable
</code></pre>
<p>Could you please help me out with this code? I’m quite lost how to make this work.</p>

---

## Post #19 by @mau_igna_06 (2023-02-23 09:56 UTC)

<aside class="quote no-group" data-username="eliagre" data-post="18" data-topic="22165">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/eliagre/48/18509_2.png" class="avatar"> eliagre:</div>
<blockquote>
<p>I’ve been trying to use your script as an example, but it is hard for me (I’m a newbie and not familiar with python or C++ (I think?) at all).</p>
</blockquote>
</aside>
<p>I usually find vtk python examples here:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://python.hotexamples.com/">
  <header class="source">
      <img src="https://python.hotexamples.com/images/python/favicon-32x32.png" class="site-icon" width="" height="">

      <a href="https://python.hotexamples.com/" target="_blank" rel="noopener nofollow ugc">python.hotexamples.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://python.hotexamples.com/" target="_blank" rel="noopener nofollow ugc">Python Code Examples - HotExamples</a></h3>

  <p>This service was created to help programmers find real examples of using classes and methods as well as documentation. Our system automatically searches, retrieves and ranks examples of source code from more than 1 million opensource projects. A key...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #20 by @eliagre (2023-02-23 15:58 UTC)

<p>Thank you for the examples, they helped! Here is the updated code to get the ‘Model of the Unselected Cells’.</p>
<pre><code class="lang-auto">modelNode = slicer.util.getNode("Model")
threshold = vtk.vtkThreshold()
threshold.SetInputConnection(modelNode.GetPolyDataConnection())
threshold.SetThresholdFunction(threshold.THRESHOLD_LOWER)
threshold.SetLowerThreshold(0.5)
threshold.SetInputArrayToProcess(0,0,0, vtk.vtkDataObject.FIELD_ASSOCIATION_POINTS, "Selection")
threshold.Update()
surface = vtk.vtkGeometryFilter()
surface.SetInputConnection(threshold.GetOutputPort())
surface.Update() 
thresholdedModel = slicer.modules.models.logic().AddModel(surface.GetOutput())

</code></pre>

---
