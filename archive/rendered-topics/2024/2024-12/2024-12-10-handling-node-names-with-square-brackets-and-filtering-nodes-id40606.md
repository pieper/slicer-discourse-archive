# Handling Node Names with Square Brackets and Filtering Nodes of RTDose Type Exported from TPS in 3DSlicer

**Topic ID**: 40606
**Date**: 2024-12-10
**URL**: https://discourse.slicer.org/t/handling-node-names-with-square-brackets-and-filtering-nodes-of-rtdose-type-exported-from-tps-in-3dslicer/40606

---

## Post #1 by @shahrokh (2024-12-10 15:09 UTC)

<p>Hello Dear Developers and Users,</p>
<p>I am facing two issues:</p>
<p><strong>First issue:</strong> Running <code>getNode</code> on a node whose name contains square brackets with a number inside.</p>
<p>I noticed that if a node’s name contains square brackets with a number or expression inside (for example [11]), I get the following error when using the Python Interactor. Let’s assume that when reading a DICOM RTDose file using the DICOM Module, I see a node with the name:</p>
<blockquote>
<p>2: RTDOSE: DOSIsoft:RTDOSE:Phase <span class="hashtag-raw">#1</span> Dosi Dosi 1: Beam setup 1 (GY) [11]: Beam setup 1</p>
</blockquote>
<p>in the Data Module. Now, if I try to read it with <code>getNode</code>, the following error occurs:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; rtDose = getNode('2: RTDOSE: DOSIsoft:RTDOSE:Phase #1 Dosi Dosi 1: Beam setup 1 (GY) [11]: Beam setup 1');
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "/home/sn/Slicer-5.0.2-linux-amd64/bin/Python/slicer/util.py", line 1436, in getNode
    raise MRMLNodeNotFoundException("could not find nodes in the scene by name or id '%s'" % (pattern if (isinstance(pattern, str)) else ""))
slicer.util.MRMLNodeNotFoundException: could not find nodes in the scene by name or id '2: RTDOSE: DOSIsoft:RTDOSE:Phase #1 Dosi Dosi 1: Beam setup 1 (GY) [11]: Beam setup 1'
&gt;&gt;&gt; 
</code></pre>
<p>However, if I manually rename the node to (removing 11 from [11]):</p>
<blockquote>
<p>2: RTDOSE: DOSIsoft:RTDOSE:Phase <span class="hashtag-raw">#1</span> Dosi Dosi 1: Beam setup 1 (GY) <span class="chcklst-box fa fa-square-o fa-fw"></span>: Beam setup 1</p>
</blockquote>
<p>then the error does not occur, and I can get the node with this code:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; rtDose = getNode('2: RTDOSE: DOSIsoft:RTDOSE:Phase #1 Dosi Dosi 1: Beam setup 1 (GY) []: Beam setup 1');
&gt;&gt;&gt;
</code></pre>
<p>With this explanation, how can I read a node with a name that has this property using <code>getNode</code>?<br>
The figure below shows this error.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/424ad3fd2ba12ffb57072da06cdbcb8ea9ff6edf.png" data-download-href="/uploads/short-url/9srPybUkcAWuxXxSQgyfUUszXUX.png?dl=1" title="0" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/424ad3fd2ba12ffb57072da06cdbcb8ea9ff6edf_2_690x313.png" alt="0" data-base62-sha1="9srPybUkcAWuxXxSQgyfUUszXUX" width="690" height="313" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/424ad3fd2ba12ffb57072da06cdbcb8ea9ff6edf_2_690x313.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/424ad3fd2ba12ffb57072da06cdbcb8ea9ff6edf_2_1035x469.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/424ad3fd2ba12ffb57072da06cdbcb8ea9ff6edf_2_1380x626.png 2x" data-dominant-color="949C82"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">0</span><span class="informations">1847×840 222 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>Second issue:</strong> Filtering nodes in a ComboBox based on their type.<br>
Is it possible to have a <em>ComboBox</em> where only nodes of the type <code>RTDose</code> are listed, and other nodes, such as those related to CT images, are not shown?</p>
<p>In the following figure, I have two nodes with the names of <strong>2: Unnamed Series</strong> and <strong>2: RTDOSE: DOSIsoft:RTDOSE:Phase <span class="hashtag-raw">#1</span> Dosi Dosi 1: Beam setup 1 (GY) []: Beam setup 1</strong>, both of which are of the type vtkMRMLScalarVolumeNode. However, for example, in the Isodose module, I can only see the node of type RTDOSE, not the other one.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b6bb4049a86ea26645dd6cefd7211c410481b64f.png" data-download-href="/uploads/short-url/q4w5adNr0ob1S61b7OEZpCV90RN.png?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6bb4049a86ea26645dd6cefd7211c410481b64f_2_690x388.png" alt="2" data-base62-sha1="q4w5adNr0ob1S61b7OEZpCV90RN" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6bb4049a86ea26645dd6cefd7211c410481b64f_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6bb4049a86ea26645dd6cefd7211c410481b64f_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6bb4049a86ea26645dd6cefd7211c410481b64f_2_1380x776.png 2x" data-dominant-color="B8BDAB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1920×1080 402 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Please guide me.<br>
Best regards.<br>
Shahrokh</p>

---

## Post #2 by @cpinter (2024-12-10 16:08 UTC)

<p>First issue:</p>
<p>I confirm that <code>getNode</code> does not work with square brackets in the latest. I think it used to work, because I regularly accessed beam nodes and they have these brackets in the name. This may be due to the new translation features? Not sure.</p>
<p>For the time being you can use <code>slicer.mrmlScene.GetFirstNodeByName('MRHead [11]')</code></p>
<p>Second issue:</p>
<p>Please look at the comboboxes in Isodose or DoseVolumeHistogram modules in SlicerRT, they can filter to show only RTDose volumes.</p>

---

## Post #3 by @shahrokh (2024-12-11 02:31 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="40606">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Please look at the comboboxes in Isodose or DoseVolumeHistogram modules in SlicerRT, they can filter to show only RTDose volumes.</p>
</blockquote>
</aside>
<p>Thank you very much for your answers and guidance. I understand that the Isodose or DoseVolumeHistogram modules have the filtering feature based on the type of node. I was wondering which property has been used in the RTDose type nodes that allows these modules to list only this type of node?</p>
<p>Best regards.<br>
Shahrokh</p>

---

## Post #4 by @shahrokh (2024-12-22 12:27 UTC)

<p>Unfortunately, I still haven’t been able to implement the UI that is similar to the comboboxes in the <strong>DoseVolumeHistogram</strong> or <strong>Isodose</strong> modules, where they can filter and only show RTDose volumes. However, I found some interesting points. One of these is the presence of an Attribute called <code>DicomRtImport.DoseVolume</code> with a value of <code>1</code> in RTDose volumes. Based on this, I can identify and separate the nodes with this attribute from the ones in the Data module using the following commands:</p>
<pre><code class="lang-auto">import slicer
listVolumeNodes = list(slicer.mrmlScene.GetNodesByClass('vtkMRMLScalarVolumeNode'))
strClass = 'vtkMRMLScalarVolumeNode'

for nodeNumber in range(len(listVolumeNodes)):
 nodeID = strClass + str(nodeNumber+1)
 print(nodeID)
 slicer.mrmlScene.GetNodeByID(nodeID).GetAttributeNames()

strAttributeDoseVolume = 'DicomRtImport.DoseVolume'

for nodeNumber in range(len(listVolumeNodes)):
 nodeID = strClass + str(nodeNumber+1)
 if strAttributeDoseVolume == slicer.mrmlScene.GetNodeByID(nodeID).GetAttributeNames()[0]:
  print('Attribute Node: ', slicer.mrmlScene.GetNodeByID(nodeID).GetAttributeNames())
  nodeDoseVolume = slicer.mrmlScene.GetNodeByID(nodeID)
</code></pre>
<p>However, I couldn’t reach my goal in the UI, which is to only show RTDose Volume in the ComboBox. Still, the code I have written so far is as follows:<br>
import os</p>
<pre><code class="lang-auto">

import unittest
from __main__ import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import qt
parametersCollapsibleButton = ctk.ctkCollapsibleButton()
parametersCollapsibleButton.text = "Parameters"
parametersCollapsibleButton.show()
parametersFormLayout = qt.QFormLayout(parametersCollapsibleButton)
inputSelector0 = slicer.qMRMLNodeComboBox()
inputSelector0.nodeTypes = ["vtkMRMLScalarVolumeNode"]
inputSelector0.addEnabled = False
inputSelector0.removeEnabled = False
inputSelector0.noneEnabled = False
inputSelector0.showHidden = False
inputSelector0.showChildNodeTypes = False
inputSelector0.setMRMLScene( slicer.mrmlScene )
#inputSelector0.setCurrentNodeID(slicer.mrmlScene.GetNodeByID(nodeID))
#inputSelector0.setCurrentNode(slicer.mrmlScene.GetNodeByID(nodeID))
#inputSelector0.setCurrentNodeIndex(slicer.mrmlScene.GetNodeByID(nodeID))
#inputSelector0.setNodeTypeLabel(slicer.mrmlScene.GetNodeByID(nodeID))
inputSelector0.setToolTip( "Pick the input to the algorithm." )
parametersFormLayout.addRow("Dose Volume: ", inputSelector0)
#parametersFormLayout.addRow("Dose Volume: ", inputSelector0.setCurrentNodeID(nodeID))
</code></pre>
<p>Screenshot:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0ae031f5f4f6620d97f9440392a85d5bfb58e47.png" data-download-href="/uploads/short-url/tM48ghgismXwTwaDPQWczqfkm8L.png?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d0ae031f5f4f6620d97f9440392a85d5bfb58e47_2_690x388.png" alt="2" data-base62-sha1="tM48ghgismXwTwaDPQWczqfkm8L" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d0ae031f5f4f6620d97f9440392a85d5bfb58e47_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d0ae031f5f4f6620d97f9440392a85d5bfb58e47_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d0ae031f5f4f6620d97f9440392a85d5bfb58e47_2_1380x776.png 2x" data-dominant-color="CBCDC9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1920×1080 433 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As you can see from the commands above, I used various “Get” functions from <code>slicer.mrmlScene</code>, but none of them gave the desired result.<br>
As you suggested, I studied the module code from <strong>DoseVolumeHistogram</strong> on <em>GitHub</em>. Although it seemed like the <code>nodeType</code> was assigned the value <code>vtkMRMLScalarVolumeNode</code>, I couldn’t figure out what other condition was added to make the combobox work correctly.</p>
<p>In any case, I will keep reading through this code to see if I can find a solution to my issue. I believe that when someone is looking for an answer to their problem on GitHub, StackOverflow, or in forums, they inevitably come across many other problems and solutions. Still, I would be happy if you could guide me.</p>
<p>Best regards.<br>
Shahrokh</p>

---

## Post #5 by @lassoan (2024-12-22 19:08 UTC)

<ol>
<li><code>getNode</code> behavior for some special characters</li>
</ol>
<p><code>getNode</code> is only intended for quick access to nodes for testing and troubleshooting. For convenience, it uses searching with wildcards in filename format (e.g., you can ask <code>getNode('something*')</code>), but it also means that some special characters (such as <code>*</code>, square brackets, etc.) need to be escaped. It has many other limitations, such as it only returns the first node by that name (while in scene you often have several nodes by the exact same name). So, it is a convenient shorthand for simple cases, use it when it works for you.</p>
<p>If you have several nodes by the same name or the node name contain special characters, I would recommend to use:</p>
<ul>
<li><code>getNode</code> with the node ID as argument (it does not contain special character and it is unique within a scene)</li>
<li><code>getFirstNodeByClassByName</code> function, which allows you to select the right node even when there are various other nodes of a different class by the same name. It also comes without filename search pattern matching, so you don’t need to worry about special characters. For example, try: <code>getFirstNodeByClassByName("vtkMRMLScalarVolumeNode", "2: RTDOSE: DOSIsoft:RTDOSE:Phase #1 Dosi Dosi 1: Beam setup 1 (GY) [11]: Beam setup 1"</code></li>
</ul>
<ol start="2">
<li>Filtering in node selector</li>
</ol>
<p>As <a class="mention" href="/u/cpinter">@cpinter</a> suggested, you can have a look how it is done in DoseVolumeHistogram module:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerRt/SlicerRT/blob/600a018d4eff7e682b4255024978bc5e6d6970e4/Isodose/qSlicerIsodoseModuleWidget.cxx#L267">
  <header class="source">

      <a href="https://github.com/SlicerRt/SlicerRT/blob/600a018d4eff7e682b4255024978bc5e6d6970e4/Isodose/qSlicerIsodoseModuleWidget.cxx#L267" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerRT/blob/600a018d4eff7e682b4255024978bc5e6d6970e4/Isodose/qSlicerIsodoseModuleWidget.cxx#L267" target="_blank" rel="noopener">SlicerRt/SlicerRT/blob/600a018d4eff7e682b4255024978bc5e6d6970e4/Isodose/qSlicerIsodoseModuleWidget.cxx#L267</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="257" style="counter-reset: li-counter 256 ;">
          <li>}
</li>
          <li>
</li>
          <li>//-----------------------------------------------------------------------------
</li>
          <li>void qSlicerIsodoseModuleWidget::setup()
</li>
          <li>{
</li>
          <li>  Q_D(qSlicerIsodoseModuleWidget);
</li>
          <li>  d-&gt;setupUi(this);
</li>
          <li>  this-&gt;Superclass::setup();
</li>
          <li>
</li>
          <li>  // Show only dose volumes in the dose volume combobox by default
</li>
          <li class="selected">  d-&gt;MRMLNodeComboBox_DoseVolume-&gt;addAttribute( QString("vtkMRMLScalarVolumeNode"), vtkSlicerRtCommon::DICOMRTIMPORT_DOSE_VOLUME_IDENTIFIER_ATTRIBUTE_NAME.c_str());
</li>
          <li>
</li>
          <li>  // Make connections
</li>
          <li>  connect( d-&gt;MRMLNodeComboBox_ParameterSet, SIGNAL(currentNodeChanged(vtkMRMLNode*)), this, SLOT( setParameterNode(vtkMRMLNode*) ) );
</li>
          <li>  connect( d-&gt;MRMLNodeComboBox_DoseVolume, SIGNAL( currentNodeChanged(vtkMRMLNode*) ), this, SLOT( setDoseVolumeNode(vtkMRMLNode*) ) );
</li>
          <li>  connect( d-&gt;MRMLNodeComboBox_IsodoseModel, SIGNAL( currentNodeChanged(vtkMRMLNode*) ), this, SLOT( setIsodoseModelNode(vtkMRMLNode*) ) );
</li>
          <li>  connect( d-&gt;spinBox_NumberOfLevels, SIGNAL(valueChanged(int)), this, SLOT(setNumberOfLevels(int)));
</li>
          <li>
</li>
          <li>  connect( d-&gt;checkBox_ShowDoseVolumesOnly, SIGNAL( stateChanged(int) ), this, SLOT( showDoseVolumesOnlyCheckboxChanged(int) ) );
</li>
          <li>  connect( d-&gt;checkBox_Isoline, SIGNAL(toggled(bool)), this, SLOT( setIsolineVisibility(bool) ) );
</li>
          <li>  connect( d-&gt;checkBox_Isosurface, SIGNAL(toggled(bool)), this, SLOT( setIsosurfaceVisibility(bool) ) );
</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>In the future, please post unrelated questions as two separate topics. Thank you!</p>

---

## Post #6 by @shahrokh (2024-12-29 13:38 UTC)

<p>First of all, I would like to thank you for your excellent guidance and support. The point you mentioned at the end, I will definitely take into consideration.</p>
<p>I have learned some interesting points from the existing code, such as <code>vtkSlicerRtCommon.cxx</code>. For example, I learned how to determine whether a volume node is of type RTDose based on the attribute <code>DicomRtImport.DoseVolume</code>. To achieve this, I implemented a function called <code>doseVolumeFilter</code>:</p>
<pre><code class="lang-auto">def doseVolumeFilter(listVolumeNodes):
 strClass = 'vtkMRMLScalarVolumeNode'
 strAttributeDoseVolume = 'DicomRtImport.DoseVolume'
 for nodeNumber in range(len(listVolumeNodes)):
  nodeID = strClass + str(nodeNumber+1)
  if strAttributeDoseVolume == slicer.mrmlScene.GetNodeByID(nodeID).GetAttributeNames()[0]:
   attributesDoseNode = slicer.mrmlScene.GetNodeByID(nodeID).GetAttributeNames()
   nodeDoseVolume = slicer.mrmlScene.GetNodeByID(nodeID)
   return nodeID, nodeDoseVolume, attributesDoseNode
</code></pre>
<p>Execution of this function:</p>
<pre><code class="lang-auto">listVolumeNodes = list(slicer.mrmlScene.GetNodesByClass('vtkMRMLScalarVolumeNode'))
returns_doseVolumeFilter=doseVolumeFilter(listVolumeNodes)
print("node IDs:", returns_doseVolumeFilter[0])
print("Dose node ID:", returns_doseVolumeFilter[1])
print("Attribute Dose node:", returns_doseVolumeFilter[2])
</code></pre>
<p>I should mention, however, that after writing this function, I noticed that the <code>IsDoseVolumeNode</code> function in the <code>vtkSlicerRtCommon.cxx</code> file does the same thing.</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerRt/SlicerRT/blob/600a018d4eff7e682b4255024978bc5e6d6970e4/SlicerRtCommon/vtkSlicerRtCommon.cxx#L111">
  <header class="source">

      <a href="https://github.com/SlicerRt/SlicerRT/blob/600a018d4eff7e682b4255024978bc5e6d6970e4/SlicerRtCommon/vtkSlicerRtCommon.cxx#L111" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerRT/blob/600a018d4eff7e682b4255024978bc5e6d6970e4/SlicerRtCommon/vtkSlicerRtCommon.cxx#L111" target="_blank" rel="noopener nofollow ugc">SlicerRt/SlicerRT/blob/600a018d4eff7e682b4255024978bc5e6d6970e4/SlicerRtCommon/vtkSlicerRtCommon.cxx#L111</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="101" style="counter-reset: li-counter 100 ;">
          <li>    return true;
</li>
          <li>  }
</li>
          <li>  else if (strcmp(aString, "") == 0)
</li>
          <li>  {
</li>
          <li>    return true;
</li>
          <li>  }
</li>
          <li>  return false;
</li>
          <li>}
</li>
          <li>
</li>
          <li>//---------------------------------------------------------------------------
</li>
          <li class="selected">bool vtkSlicerRtCommon::IsDoseVolumeNode(vtkMRMLNode* node)
</li>
          <li>{
</li>
          <li>  if (!node)
</li>
          <li>  {
</li>
          <li>    return false;
</li>
          <li>  }
</li>
          <li>
</li>
          <li>  if (node-&gt;IsA("vtkMRMLScalarVolumeNode"))
</li>
          <li>  {
</li>
          <li>    const char* doseVolumeIdentifier = node-&gt;GetAttribute(vtkSlicerRtCommon::DICOMRTIMPORT_DOSE_VOLUME_IDENTIFIER_ATTRIBUTE_NAME.c_str());
</li>
          <li>    if (doseVolumeIdentifier != nullptr)
</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Execution of this funtion:</p>
<pre><code class="lang-auto">import vtkSlicerRtCommonPython as vtkSlicerRtCommon
rtDose = slicer.util.getFirstNodeByClassByName("vtkMRMLScalarVolumeNode", "2: RTDOSE: DOSIsoft:RTDOSE:Phase #1 Dosi Dosi 1: Beam setup 1 (GY) [11]: Beam setup 1")
vtkSlicerRtCommon.vtkSlicerRtCommon().IsDoseVolumeNode(rtDose)
#Output: True
</code></pre>
<p>Anyway, I am trying hard to write a combobox that only lists volumes of type RTDose. However, I haven’t been successful yet. As shown in the following lines:</p>
<pre><code class="lang-auto">import os
import unittest
from __main__ import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import qt

parametersCollapsibleButton = ctk.ctkCollapsibleButton()
parametersCollapsibleButton.text = "Parameters"
parametersCollapsibleButton.show()
parametersFormLayout = qt.QFormLayout(parametersCollapsibleButton)
inputSelector0 = slicer.qMRMLNodeComboBox()
inputSelector0.setMRMLScene( slicer.mrmlScene )
inputSelector0.enabled
inputSelector0.setToolTip( "Pick the input to the algorithm." )
parametersFormLayout.addRow("Dose Volume: ", inputSelector0)
</code></pre>
<p>The result of executing these commands is a combobox that lists different types of nodes. In these lines, the <code>nodeTypes</code> is not specified, as following figure:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/164682cd8b64172a2b1b6b371cc44a0a85d6fa0a.png" data-download-href="/uploads/short-url/3b3zy006lTqpO0yVMm4vtxB7QqS.png?dl=1" title="01" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/164682cd8b64172a2b1b6b371cc44a0a85d6fa0a_2_690x388.png" alt="01" data-base62-sha1="3b3zy006lTqpO0yVMm4vtxB7QqS" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/164682cd8b64172a2b1b6b371cc44a0a85d6fa0a_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/164682cd8b64172a2b1b6b371cc44a0a85d6fa0a_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/164682cd8b64172a2b1b6b371cc44a0a85d6fa0a_2_1380x776.png 2x" data-dominant-color="D5D8D5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">01</span><span class="informations">1920×1080 258 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Based on line 65 of the <code>vtkSlicerRtCommon.cxx</code> file, I thought perhaps an attribute named <strong>DICOMRTIMPORT_DOSE_VOLUME_IDENTIFIER_ATTRIBUTE_NAME</strong> with the value <strong>DicomRtImport.DoseVolume</strong> should be added to the combobox.</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerRt/SlicerRT/blob/600a018d4eff7e682b4255024978bc5e6d6970e4/SlicerRtCommon/vtkSlicerRtCommon.cxx#L64">
  <header class="source">

      <a href="https://github.com/SlicerRt/SlicerRT/blob/600a018d4eff7e682b4255024978bc5e6d6970e4/SlicerRtCommon/vtkSlicerRtCommon.cxx#L64" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerRT/blob/600a018d4eff7e682b4255024978bc5e6d6970e4/SlicerRtCommon/vtkSlicerRtCommon.cxx#L64" target="_blank" rel="noopener nofollow ugc">SlicerRt/SlicerRT/blob/600a018d4eff7e682b4255024978bc5e6d6970e4/SlicerRtCommon/vtkSlicerRtCommon.cxx#L64</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="54" style="counter-reset: li-counter 53 ;">
          <li>const char* vtkSlicerRtCommon::SLICERRT_EXTENSION_NAME = "SlicerRT";
</li>
          <li>const std::string vtkSlicerRtCommon::STORAGE_NODE_POSTFIX = "_Storage";
</li>
          <li>const std::string vtkSlicerRtCommon::DISPLAY_NODE_SUFFIX = "_Display";
</li>
          <li>
</li>
          <li>// Segmentation constants
</li>
          <li>const char* vtkSlicerRtCommon::SEGMENTATION_RIBBON_MODEL_REPRESENTATION_NAME = "Ribbon model";
</li>
          <li>
</li>
          <li>const double vtkSlicerRtCommon::COLOR_VALUE_INVALID[4] = {0.5, 0.5, 0.5, 1.0};
</li>
          <li>
</li>
          <li>// DicomRtImport constants
</li>
          <li class="selected">const std::string vtkSlicerRtCommon::DICOMRTIMPORT_ATTRIBUTE_PREFIX = "DicomRtImport.";
</li>
          <li>const std::string vtkSlicerRtCommon::DICOMRTIMPORT_DOSE_VOLUME_IDENTIFIER_ATTRIBUTE_NAME = vtkSlicerRtCommon::DICOMRTIMPORT_ATTRIBUTE_PREFIX + "DoseVolume"; // Identifier
</li>
          <li>const std::string vtkSlicerRtCommon::DICOMRTIMPORT_DOSE_UNIT_NAME_ATTRIBUTE_NAME = vtkSlicerRtCommon::DICOMRTIMPORT_ATTRIBUTE_PREFIX + "DoseUnitName";
</li>
          <li>const std::string vtkSlicerRtCommon::DICOMRTIMPORT_DOSE_UNIT_VALUE_ATTRIBUTE_NAME = vtkSlicerRtCommon::DICOMRTIMPORT_ATTRIBUTE_PREFIX + "DoseUnitValue";
</li>
          <li>const std::string vtkSlicerRtCommon::DICOMRTIMPORT_SOURCE_AXIS_DISTANCE_ATTRIBUTE_NAME = vtkSlicerRtCommon::DICOMRTIMPORT_ATTRIBUTE_PREFIX + "SourceAxisDistance";
</li>
          <li>const std::string vtkSlicerRtCommon::DICOMRTIMPORT_GANTRY_ANGLE_ATTRIBUTE_NAME = vtkSlicerRtCommon::DICOMRTIMPORT_ATTRIBUTE_PREFIX + "GantryAngle";
</li>
          <li>const std::string vtkSlicerRtCommon::DICOMRTIMPORT_COUCH_ANGLE_ATTRIBUTE_NAME = vtkSlicerRtCommon::DICOMRTIMPORT_ATTRIBUTE_PREFIX + "CouchAngle";
</li>
          <li>const std::string vtkSlicerRtCommon::DICOMRTIMPORT_COLLIMATOR_ANGLE_ATTRIBUTE_NAME = vtkSlicerRtCommon::DICOMRTIMPORT_ATTRIBUTE_PREFIX + "CollimatorAngle";
</li>
          <li>const std::string vtkSlicerRtCommon::DICOMRTIMPORT_BEAM_JAW_POSITIONS_ATTRIBUTE_NAME = vtkSlicerRtCommon::DICOMRTIMPORT_ATTRIBUTE_PREFIX + "JawPositions";
</li>
          <li>const std::string vtkSlicerRtCommon::DICOMRTIMPORT_BEAM_NUMBER_ATTRIBUTE_NAME = vtkSlicerRtCommon::DICOMRTIMPORT_ATTRIBUTE_PREFIX + "BeamNumber";
</li>
          <li>const std::string vtkSlicerRtCommon::DICOMRTIMPORT_ROI_REFERENCED_SERIES_UID_ATTRIBUTE_NAME = vtkSlicerRtCommon::DICOMRTIMPORT_ATTRIBUTE_PREFIX + "RoiReferencedSeriesUid"; // DICOM connection
</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Accordingly, I executed the following code:</p>
<pre><code class="lang-auto">import os
import unittest
from __main__ import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import qt

parametersCollapsibleButton = ctk.ctkCollapsibleButton()
parametersCollapsibleButton.text = "Parameters"
parametersCollapsibleButton.show()
parametersFormLayout = qt.QFormLayout(parametersCollapsibleButton)
inputSelector0 = slicer.qMRMLNodeComboBox()
inputSelector0.nodeTypes = ["vtkMRMLScalarVolumeNode"]
inputSelector0.addAttribute("vtkMRMLScalarVolumeNode", "DICOMRTIMPORT_DOSE_VOLUME_IDENTIFIER_ATTRIBUTE_NAME", "DicomRtImport.DoseVolume")
inputSelector0.setMRMLScene( slicer.mrmlScene )
inputSelector0.enabled
inputSelector0.setToolTip( "Pick the input to the algorithm." )
parametersFormLayout.addRow("Dose Volume: ", inputSelector0)
</code></pre>
<p>In these commands, the <code>nodeTypes</code> and <code>addAttribute</code> methods were used. However, as you can see in the figure below, contrary to my expectation, the node list in the combobox is empty.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78268431581d6b00e3b39988981cbed7b37f2d71.png" data-download-href="/uploads/short-url/h8TOG8pv9V7mrheL9g27Ws5Inf3.png?dl=1" title="02" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78268431581d6b00e3b39988981cbed7b37f2d71_2_690x388.png" alt="02" data-base62-sha1="h8TOG8pv9V7mrheL9g27Ws5Inf3" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78268431581d6b00e3b39988981cbed7b37f2d71_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78268431581d6b00e3b39988981cbed7b37f2d71_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78268431581d6b00e3b39988981cbed7b37f2d71_2_1380x776.png 2x" data-dominant-color="DDDEDC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">02</span><span class="informations">1920×1080 238 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Based on line 271 of the <code>qSlicerIsodoseModuleWidget.cxx</code> file, it occurred to me that perhaps the filtering should be done through the <strong>inputSelector0.connect</strong> function, as dear Andras Lasso has pointed out.</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerRt/SlicerRT/blob/600a018d4eff7e682b4255024978bc5e6d6970e4/Isodose/qSlicerIsodoseModuleWidget.cxx#L271">
  <header class="source">

      <a href="https://github.com/SlicerRt/SlicerRT/blob/600a018d4eff7e682b4255024978bc5e6d6970e4/Isodose/qSlicerIsodoseModuleWidget.cxx#L271" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerRT/blob/600a018d4eff7e682b4255024978bc5e6d6970e4/Isodose/qSlicerIsodoseModuleWidget.cxx#L271" target="_blank" rel="noopener nofollow ugc">SlicerRt/SlicerRT/blob/600a018d4eff7e682b4255024978bc5e6d6970e4/Isodose/qSlicerIsodoseModuleWidget.cxx#L271</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="261" style="counter-reset: li-counter 260 ;">
          <li>{
</li>
          <li>  Q_D(qSlicerIsodoseModuleWidget);
</li>
          <li>  d-&gt;setupUi(this);
</li>
          <li>  this-&gt;Superclass::setup();
</li>
          <li>
</li>
          <li>  // Show only dose volumes in the dose volume combobox by default
</li>
          <li>  d-&gt;MRMLNodeComboBox_DoseVolume-&gt;addAttribute( QString("vtkMRMLScalarVolumeNode"), vtkSlicerRtCommon::DICOMRTIMPORT_DOSE_VOLUME_IDENTIFIER_ATTRIBUTE_NAME.c_str());
</li>
          <li>
</li>
          <li>  // Make connections
</li>
          <li>  connect( d-&gt;MRMLNodeComboBox_ParameterSet, SIGNAL(currentNodeChanged(vtkMRMLNode*)), this, SLOT( setParameterNode(vtkMRMLNode*) ) );
</li>
          <li class="selected">  connect( d-&gt;MRMLNodeComboBox_DoseVolume, SIGNAL( currentNodeChanged(vtkMRMLNode*) ), this, SLOT( setDoseVolumeNode(vtkMRMLNode*) ) );
</li>
          <li>  connect( d-&gt;MRMLNodeComboBox_IsodoseModel, SIGNAL( currentNodeChanged(vtkMRMLNode*) ), this, SLOT( setIsodoseModelNode(vtkMRMLNode*) ) );
</li>
          <li>  connect( d-&gt;spinBox_NumberOfLevels, SIGNAL(valueChanged(int)), this, SLOT(setNumberOfLevels(int)));
</li>
          <li>
</li>
          <li>  connect( d-&gt;checkBox_ShowDoseVolumesOnly, SIGNAL( stateChanged(int) ), this, SLOT( showDoseVolumesOnlyCheckboxChanged(int) ) );
</li>
          <li>  connect( d-&gt;checkBox_Isoline, SIGNAL(toggled(bool)), this, SLOT( setIsolineVisibility(bool) ) );
</li>
          <li>  connect( d-&gt;checkBox_Isosurface, SIGNAL(toggled(bool)), this, SLOT( setIsosurfaceVisibility(bool) ) );
</li>
          <li>  connect( d-&gt;pushButton_Apply, SIGNAL(clicked()), this, SLOT(applyClicked()) );
</li>
          <li>  connect( d-&gt;groupBox_RelativeIsolevels, SIGNAL(toggled(bool)), this, SLOT(setRelativeIsolevelsFlag(bool)));
</li>
          <li>  connect( d-&gt;sliderWidget_ReferenceDose, SIGNAL(valueChanged(double)), this, SLOT(setReferenceDoseValue(double)));
</li>
          <li>
</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I think the issue lies in the implementation of this function. In my module, named RTDoseSelector.py, I implemented this function as follows:</p>
<pre><code class="lang-auto">    # connections
    self.inputSelector0.connect("currentNodeChanged(vtkMRMLNode*)", self.onSelect)
</code></pre>
<p>If possible, could you please guide me? In my opinion, acquiring the ability to filter nodes based on their type and attribute is very important. The attribute is particularly significant because the difference between <strong>RTDose</strong> and other <strong>volumeNode</strong> types lies in its attribute.</p>
<p>Best regards.<br>
Shahrokh</p>

---

## Post #7 by @shahrokh (2025-01-01 13:19 UTC)

<p>Excuse me, I think that in order for the combobox to have filtering capability (to pass volumes with the attribute equal to <code>DicomRtImport.DoseVolume</code> and reject other volumes, i.e., not display them in the list of combobox), it should use the concept of <strong>signal</strong>, <strong>slot</strong>, and <strong>connect</strong>. This understanding of mine is based on line 271 from the file qSlicerIsodoseModuleWidget.cxx.</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerRt/SlicerRT/blob/600a018d4eff7e682b4255024978bc5e6d6970e4/Isodose/qSlicerIsodoseModuleWidget.cxx#L271">
  <header class="source">

      <a href="https://github.com/SlicerRt/SlicerRT/blob/600a018d4eff7e682b4255024978bc5e6d6970e4/Isodose/qSlicerIsodoseModuleWidget.cxx#L271" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerRT/blob/600a018d4eff7e682b4255024978bc5e6d6970e4/Isodose/qSlicerIsodoseModuleWidget.cxx#L271" target="_blank" rel="noopener nofollow ugc">SlicerRt/SlicerRT/blob/600a018d4eff7e682b4255024978bc5e6d6970e4/Isodose/qSlicerIsodoseModuleWidget.cxx#L271</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="261" style="counter-reset: li-counter 260 ;">
          <li>{
</li>
          <li>  Q_D(qSlicerIsodoseModuleWidget);
</li>
          <li>  d-&gt;setupUi(this);
</li>
          <li>  this-&gt;Superclass::setup();
</li>
          <li>
</li>
          <li>  // Show only dose volumes in the dose volume combobox by default
</li>
          <li>  d-&gt;MRMLNodeComboBox_DoseVolume-&gt;addAttribute( QString("vtkMRMLScalarVolumeNode"), vtkSlicerRtCommon::DICOMRTIMPORT_DOSE_VOLUME_IDENTIFIER_ATTRIBUTE_NAME.c_str());
</li>
          <li>
</li>
          <li>  // Make connections
</li>
          <li>  connect( d-&gt;MRMLNodeComboBox_ParameterSet, SIGNAL(currentNodeChanged(vtkMRMLNode*)), this, SLOT( setParameterNode(vtkMRMLNode*) ) );
</li>
          <li class="selected">  connect( d-&gt;MRMLNodeComboBox_DoseVolume, SIGNAL( currentNodeChanged(vtkMRMLNode*) ), this, SLOT( setDoseVolumeNode(vtkMRMLNode*) ) );
</li>
          <li>  connect( d-&gt;MRMLNodeComboBox_IsodoseModel, SIGNAL( currentNodeChanged(vtkMRMLNode*) ), this, SLOT( setIsodoseModelNode(vtkMRMLNode*) ) );
</li>
          <li>  connect( d-&gt;spinBox_NumberOfLevels, SIGNAL(valueChanged(int)), this, SLOT(setNumberOfLevels(int)));
</li>
          <li>
</li>
          <li>  connect( d-&gt;checkBox_ShowDoseVolumesOnly, SIGNAL( stateChanged(int) ), this, SLOT( showDoseVolumesOnlyCheckboxChanged(int) ) );
</li>
          <li>  connect( d-&gt;checkBox_Isoline, SIGNAL(toggled(bool)), this, SLOT( setIsolineVisibility(bool) ) );
</li>
          <li>  connect( d-&gt;checkBox_Isosurface, SIGNAL(toggled(bool)), this, SLOT( setIsosurfaceVisibility(bool) ) );
</li>
          <li>  connect( d-&gt;pushButton_Apply, SIGNAL(clicked()), this, SLOT(applyClicked()) );
</li>
          <li>  connect( d-&gt;groupBox_RelativeIsolevels, SIGNAL(toggled(bool)), this, SLOT(setRelativeIsolevelsFlag(bool)));
</li>
          <li>  connect( d-&gt;sliderWidget_ReferenceDose, SIGNAL(valueChanged(double)), this, SLOT(setReferenceDoseValue(double)));
</li>
          <li>
</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Is my understanding correct?<br>
Best regards.<br>
Shahrokh</p>

---

## Post #8 by @lassoan (2025-01-01 16:10 UTC)

<p>Connection of signals and slots are nor related to filtering. The issue in the code above is that <code>DICOMRTIMPORT_DOSE_VOLUME_IDENTIFIER_ATTRIBUTE_NAME</code> is not a string literal. It is a variable name.</p>
<p>Instead of using the variable <em>name</em> as input, you need to use the variable <em>value</em>.</p>

---

## Post #9 by @shahrokh (2025-01-04 12:38 UTC)

<p>Thank you so much for the guidance. I’m sorry, but I’ve encountered a new error again.</p>
<pre><code class="lang-auto">&gt;&gt;&gt; import qt
&gt;&gt;&gt; inputSelector0.addAttribute(qt.QString(["vtkMRMLScalarVolumeNode"]), qt.QString(["DICOMRTIMPORT_DOSE_VOLUME_IDENTIFIER_ATTRIBUTE_NAME"]), qt.QString(["DicomRtImport.DoseVolume"]))
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
AttributeError: module 'qt' has no attribute 'QString'
&gt;&gt;&gt; inputSelector0.addAttribute(qt.QStringListModel(["vtkMRMLScalarVolumeNode"]), qt.QStringListModel(["DICOMRTIMPORT_DOSE_VOLUME_IDENTIFIER_ATTRIBUTE_NAME"]), qt.QStringListModel(["DicomRtImport.DoseVolume"]))
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
ValueError: Could not find matching overload for given arguments:
(QStringListModel (QStringListModel at: 0x7660300), QStringListModel (QStringListModel at: 0x8a71630), QStringListModel (QStringListModel at: 0x91629f0))
 The following slots are available:
addAttribute(QString nodeType, QString attributeName, QVariant attributeValue) -&gt; void
addAttribute(QString nodeType, QString attributeName) -&gt; void

&gt;&gt;&gt; 
</code></pre>
<p>Best regards.<br>
Shahrokh</p>

---

## Post #10 by @shahrokh (2025-01-08 08:14 UTC)

<p>Thank you very much for the support and assistance you are providing. You have guided me very well, but I was not able to understand the issue.<br>
line corrected:</p>
<pre><code class="lang-auto">...
inputSelector0 = slicer.qMRMLNodeComboBox()
inputSelector0.nodeTypes = ["vtkMRMLScalarVolumeNode"]
inputSelector0.addAttribute("vtkMRMLScalarVolumeNode", "DicomRtImport.DoseVolume")
...
</code></pre>
<p>However, as shown in the image below, the Combobox only contains nodes of type RTDose.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/eac545468cff19e946174d684a68533f5b053c6a.png" data-download-href="/uploads/short-url/xuSnsCpmyepcj4YGmhdf6O5gkDo.png?dl=1" title="Screenshot from 2025-01-08 11-56-41" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/eac545468cff19e946174d684a68533f5b053c6a_2_690x388.png" alt="Screenshot from 2025-01-08 11-56-41" data-base62-sha1="xuSnsCpmyepcj4YGmhdf6O5gkDo" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/eac545468cff19e946174d684a68533f5b053c6a_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/eac545468cff19e946174d684a68533f5b053c6a_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/eac545468cff19e946174d684a68533f5b053c6a_2_1380x776.png 2x" data-dominant-color="D9DBD9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2025-01-08 11-56-41</span><span class="informations">1920×1080 242 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Once again, I sincerely appreciate your guidance and support.<br>
Best regards.<br>
Shahrokh</p>

---
