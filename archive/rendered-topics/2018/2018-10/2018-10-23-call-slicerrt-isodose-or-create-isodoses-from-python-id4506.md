---
topic_id: 4506
title: "Call Slicerrt Isodose Or Create Isodoses From Python"
date: 2018-10-23
url: https://discourse.slicer.org/t/4506
---

# Call SlicerRT Isodose (or create isodoses) from python

**Topic ID**: 4506
**Date**: 2018-10-23
**URL**: https://discourse.slicer.org/t/call-slicerrt-isodose-or-create-isodoses-from-python/4506

---

## Post #1 by @dominicrushforth (2018-10-23 15:59 UTC)

<p>I have built a widget that calculates MRT doses and the SlicerRT Isodose widget does a great job creating isolines and volumes.</p>
<p>I would like to be able to call the Isodose process from within my python code so that the isodoses are displayed as soon as the doses have been calculated (and update when certain parameters are changed), however I have not been able to figure out how to do this. I have found no CLI. The help info for slicer.modules.isodose.logic do not reveal any obvious (to me) way to call it. I have also looked at the code on github…</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerRt/SlicerRT/blob/master/Isodose/Logic/vtkSlicerIsodoseModuleLogic.cxx" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerRT/blob/master/Isodose/Logic/vtkSlicerIsodoseModuleLogic.cxx" target="_blank" rel="noopener nofollow ugc">SlicerRt/SlicerRT/blob/master/Isodose/Logic/vtkSlicerIsodoseModuleLogic.cxx</a></h4>
<pre><code class="lang-cxx">/*==============================================================================

  Copyright (c) Radiation Medicine Program, University Health Network,
  Princess Margaret Hospital, Toronto, ON, Canada. All Rights Reserved.

  See COPYRIGHT.txt
  or http://www.slicer.org/copyright/copyright.txt for details.

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.

  This file was originally developed by Kevin Wang, Princess Margaret Cancer Centre 
  and was supported by Cancer Care Ontario (CCO)'s ACRU program 
  with funds provided by the Ontario Ministry of Health and Long-Term Care
  and Ontario Consortium for Adaptive Interventions in Radiation Oncology (OCAIRO).

==============================================================================*/
</code></pre>

  This file has been truncated. <a href="https://github.com/SlicerRt/SlicerRT/blob/master/Isodose/Logic/vtkSlicerIsodoseModuleLogic.cxx" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>…but I admit I’m not sure what it means (I’m pretty new to python and have never used C)</p>
<p>Is there a way to do what I want?</p>
<p>Should I try and create my own models instead (it seems a fairly complex thing to do) or go down a different path (perhaps using segmentation?). It feels like there should be a simple solution but I’ve been bashing away at it all day and am completely stumped. Any suggestions would be gratefully recieved.</p>

---

## Post #2 by @cpinter (2018-10-23 16:16 UTC)

<p>There is an automatic test that does this by interacting with the UI elements directly (to test the UI):<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerRt/SlicerRT/blob/master/Testing/Python/IGRTWorkflow_SelfTest.py#L299-L316" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerRT/blob/master/Testing/Python/IGRTWorkflow_SelfTest.py#L299-L316" target="_blank">SlicerRt/SlicerRT/blob/master/Testing/Python/IGRTWorkflow_SelfTest.py#L299-L316</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="299" style="counter-reset: li-counter 298 ;">
<li>isodoseWidget = slicer.modules.isodose.widgetRepresentation()
</li>
<li>doseVolumeMrmlNodeCombobox = slicer.util.findChildren(widget=isodoseWidget, className='qMRMLNodeComboBox', name='MRMLNodeComboBox_DoseVolume')[0]
</li>
<li>applyButton = slicer.util.findChildren(widget=isodoseWidget, className='QPushButton', text='Apply')[0]
</li>
<li>
</li>
<li># Compute isodose for day 1 dose
</li>
<li>day1Dose = slicer.util.getNode(self.day1DoseName)
</li>
<li>doseVolumeMrmlNodeCombobox.setCurrentNodeID(day1Dose.GetID())
</li>
<li>applyButton.click()
</li>
<li>
</li>
<li>self.assertEqual( len( slicer.util.getNodes('vtkMRMLModelNode*') ), numOfModelNodesBeforeLoad + 6 )
</li>
<li>
</li>
<li># Show day 1 isodose
</li>
<li>day1CT = slicer.util.getNode(self.day1CTName)
</li>
<li>self.TestUtility_ShowVolumes(day1CT)
</li>
<li>
</li>
<li>day1IsodoseShItemID = shNode.GetItemByDataNode(slicer.util.getNode(self.day1IsodosesName))
</li>
<li>self.assertIsNotNone( day1IsodoseShItemID )
</li>
<li>shNode.SetDisplayVisibilityForBranch(day1IsodoseShItemID, 1)
</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>This is not the way I’d suggest using it because it’s always better to call the logic classes. I don’t have time to write the code for you now, but you’ll have to create an isodose parameter node and set the inputs, such as<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerRt/SlicerRT/blob/master/Isodose/Logic/vtkMRMLIsodoseNode.h#L63" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerRT/blob/master/Isodose/Logic/vtkMRMLIsodoseNode.h#L63" target="_blank">SlicerRt/SlicerRT/blob/master/Isodose/Logic/vtkMRMLIsodoseNode.h#L63</a></h4>
<pre class="onebox"><code class="lang-h"><ol class="start lines" start="53" style="counter-reset: li-counter 52 ;">
<li>/// Copy the node's attributes to this object 
</li>
<li>virtual void Copy(vtkMRMLNode *node) VTK_OVERRIDE;
</li>
<li>
</li>
<li>/// Get unique node XML tag name (like Volume, Model) 
</li>
<li>virtual const char* GetNodeTagName() VTK_OVERRIDE { return "Isodose"; };
</li>
<li>
</li>
<li>public:
</li>
<li>/// Get dose volume node
</li>
<li>vtkMRMLScalarVolumeNode* GetDoseVolumeNode();
</li>
<li>/// Set and observe dose volume node
</li>
<li class="selected">void SetAndObserveDoseVolumeNode(vtkMRMLScalarVolumeNode* node);
</li>
<li>
</li>
<li>/// Get color table node
</li>
<li>vtkMRMLColorTableNode* GetColorTableNode();
</li>
<li>/// Set and observe color table node
</li>
<li>void SetAndObserveColorTableNode(vtkMRMLColorTableNode* node);
</li>
<li>
</li>
<li>/// Get/Set show Gy for D metrics checkbox state
</li>
<li>vtkGetMacro(ShowIsodoseLines, bool);
</li>
<li>vtkSetMacro(ShowIsodoseLines, bool);
</li>
<li>vtkBooleanMacro(ShowIsodoseLines, bool);
</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
Then you’ll have to call this function in the logic:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerRt/SlicerRT/blob/master/Isodose/Logic/vtkSlicerIsodoseModuleLogic.h#L60" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerRT/blob/master/Isodose/Logic/vtkSlicerIsodoseModuleLogic.h#L60" target="_blank">SlicerRt/SlicerRT/blob/master/Isodose/Logic/vtkSlicerIsodoseModuleLogic.h#L60</a></h4>
<pre class="onebox"><code class="lang-h"><ol class="start lines" start="50" style="counter-reset: li-counter 49 ;">
<li>
</li>
<li>public:
</li>
<li>static vtkSlicerIsodoseModuleLogic *New();
</li>
<li>vtkTypeMacro(vtkSlicerIsodoseModuleLogic,vtkSlicerModuleLogic);
</li>
<li>void PrintSelf(ostream&amp; os, vtkIndent indent) VTK_OVERRIDE;
</li>
<li>
</li>
<li>/// Set number of isodose levels
</li>
<li>void SetNumberOfIsodoseLevels(vtkMRMLIsodoseNode* parameterNode, int newNumberOfColors);
</li>
<li>
</li>
<li>/// Accumulates dose volumes with the given IDs and corresponding weights
</li>
<li class="selected">void CreateIsodoseSurfaces(vtkMRMLIsodoseNode* parameterNode);
</li>
<li>
</li>
<li>/// Get dose volume node
</li>
<li>vtkMRMLModelHierarchyNode* GetRootModelHierarchyNode(vtkMRMLIsodoseNode* parameterNode);
</li>
<li>
</li>
<li>public:
</li>
<li>/// Creates default isodose color table. Gets and returns if already exists
</li>
<li>static vtkMRMLColorTableNode* CreateDefaultIsodoseColorTable(vtkMRMLScene* scene);
</li>
<li>
</li>
<li>/// Creates default dose color table (which is the default isodose color table stretched.
</li>
<li>/// Gets and returns if already exists
</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
Here’s how you can access the logic:</p>
<pre><code>slicer.modules.isodose.logic()
</code></pre>
<p>Hope this helps!</p>

---

## Post #3 by @dominicrushforth (2018-11-08 16:47 UTC)

<p>Thanks it was useful just to know it was possible and that I wasn’t chasing a wild goose. I’ve go it all working nicely now althouth it took me a while to figure out how to turn submodels on and off using the subject hierachy.</p>
<p>Unfortunatly having got it working I’ve installed the new version 4.10 and the isolines are not rendering correctly <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=6" title=":frowning:" class="emoji" alt=":frowning:"></p>

---

## Post #4 by @lassoan (2018-11-08 17:00 UTC)

<aside class="quote no-group" data-username="dominicrushforth" data-post="3" data-topic="4506">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/97f17d/48.png" class="avatar"> dominicrushforth:</div>
<blockquote>
<p>isolines are not rendering correctly</p>
</blockquote>
</aside>
<p>What do you mean? Can you post a screenshot?</p>

---

## Post #5 by @dominicrushforth (2018-11-08 17:18 UTC)

<p>Thanks for getting back to me - you did so while I was creating a new topic about the rendering issues (it seemed like a different matter to me).</p>
<p>I have included some screenshots of the images.</p>
<p>Dominic</p>

---

## Post #6 by @cpinter (2018-11-08 17:25 UTC)

<p>Please provide information about the incorrect isodose lines. I cannot fix it unless I know what is the problem exactly. Thanks</p>

---

## Post #7 by @dominicrushforth (2018-11-09 09:19 UTC)

<p>I created a new topic as it seemed to me the problem was due do rendering in 4.10 rather than with isodose itself (as I was having similar problems with the segment editor module) the new topic is listed as…</p>
<h1><a href="https://discourse.slicer.org/t/model-and-segment-rendering-issues-with-4-10-and-4-11/4685">Model and Segment rendering issues with 4.10 (and 4.11)</a></h1>
<p>Thanks</p>

---
