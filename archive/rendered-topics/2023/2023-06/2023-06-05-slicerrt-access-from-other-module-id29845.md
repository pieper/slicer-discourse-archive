---
topic_id: 29845
title: "Slicerrt Access From Other Module"
date: 2023-06-05
url: https://discourse.slicer.org/t/29845
---

# SlicerRT access from other module

**Topic ID**: 29845
**Date**: 2023-06-05
**URL**: https://discourse.slicer.org/t/slicerrt-access-from-other-module/29845

---

## Post #1 by @frankkkss (2023-06-05 13:28 UTC)

<p>Hello</p>
<p>I am trying to create a module in 3D Slicer that needs access to the SlicerRT module to use the DoseVolumeHistogram functions, but I cannot do it. I think I would just need to enter the segmentation and dose volume from code. How is it done? I haven’t found documentation for that module.</p>

---

## Post #2 by @cpinter (2023-06-06 11:46 UTC)

<p>This is too little information to be able to say anything useful.</p>
<p>What programming language do you use? What functions of SlicerRT do you want to access and exactly how? Also please add any other information about the structure/deployment of your module that could be useful. Thanks</p>

---

## Post #3 by @frankkkss (2023-06-06 12:39 UTC)

<p>In a Python code I am opening a .txt file with transforms that are applied to already loaded Nodes in the scene. Then, I need to compute the dose volume histogram from a segmentation and a RT dose volume that are in the scene. Then I would need to show the DVH but I believe that would easily be done by using the AddDvhToChart function. I have tried to use the ComputeDvh() function from SlicerRT but I don’t know how to state the inputs, as it says that only one input is needed.</p>
<p>Thank you</p>

---

## Post #4 by @cpinter (2023-06-06 14:47 UTC)

<p>You can use the widgets to set the inputs like it happens in the test script</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerRt/SlicerRT/blob/master/Testing/Python/IGRTWorkflow_SelfTest.py#L591">
  <header class="source">

      <a href="https://github.com/SlicerRt/SlicerRT/blob/master/Testing/Python/IGRTWorkflow_SelfTest.py#L591" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerRT/blob/master/Testing/Python/IGRTWorkflow_SelfTest.py#L591" target="_blank" rel="noopener">SlicerRt/SlicerRT/blob/master/Testing/Python/IGRTWorkflow_SelfTest.py#L591</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="581" style="counter-reset: li-counter 580 ;">
          <li>    self.delayDisplay("Accumulate Day 1 dose with Day 2 dose registered with rigid registration finished",self.delayMs)
</li>
          <li>    self.DoseAccumulationUtility_SelectDoseVolume(self.day2DoseRigidName, False)
</li>
          <li>
</li>
          <li>  except Exception as e:
</li>
          <li>    import traceback
</li>
          <li>    traceback.print_exc()
</li>
          <li>    self.delayDisplay('Test caused exception!\n' + str(e),self.delayMs*2)
</li>
          <li>    raise Exception("Exception occurred, handled, thrown further to workflow level")
</li>
          <li>
</li>
          <li>#------------------------------------------------------------------------------
</li>
          <li class="selected">def TestSection_08_ComputeDvh(self):
</li>
          <li>  try:
</li>
          <li>    scene = slicer.mrmlScene
</li>
          <li>    slicer.util.selectModule('DoseVolumeHistogram')
</li>
          <li>    dvhWidget = slicer.modules.dosevolumehistogram.widgetRepresentation()
</li>
          <li>
</li>
          <li>    numOfTableNodesBeforeLoad = len( slicer.util.getNodes('vtkMRMLTableNode*') )
</li>
          <li>
</li>
          <li>    computeDvhButton = slicer.util.findChildren(widget=dvhWidget, text='Compute DVH')[0]
</li>
          <li>    segmentsCollapsibleGroupBox = slicer.util.findChildren(widget=dvhWidget, name='CollapsibleGroupBox_Segments')[0]
</li>
          <li>    segmentsTable = slicer.util.findChildren(widget=dvhWidget, name='SegmentsTableView')[0]
</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Or you can set the input to the parameter node (which is a nicer solution because it does not go through the widget, but the logic).</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerRt/SlicerRT/blob/master/DoseVolumeHistogram/MRML/vtkMRMLDoseVolumeHistogramNode.h#L100">
  <header class="source">

      <a href="https://github.com/SlicerRt/SlicerRT/blob/master/DoseVolumeHistogram/MRML/vtkMRMLDoseVolumeHistogramNode.h#L100" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerRT/blob/master/DoseVolumeHistogram/MRML/vtkMRMLDoseVolumeHistogramNode.h#L100" target="_blank" rel="noopener">SlicerRt/SlicerRT/blob/master/DoseVolumeHistogram/MRML/vtkMRMLDoseVolumeHistogramNode.h#L100</a></h4>



    <pre class="onebox"><code class="lang-h">
      <ol class="start lines" start="90" style="counter-reset: li-counter 89 ;">
          <li>  /// Copy the node's attributes to this object 
</li>
          <li>  void Copy(vtkMRMLNode *node) override;
</li>
          <li>
</li>
          <li>  /// Get unique node XML tag name (like Volume, Model) 
</li>
          <li>  const char* GetNodeTagName() override { return "DoseVolumeHistogram"; };
</li>
          <li>
</li>
          <li>public:
</li>
          <li>  /// Get dose volume node
</li>
          <li>  vtkMRMLScalarVolumeNode* GetDoseVolumeNode();
</li>
          <li>  /// Set and observe dose volume node
</li>
          <li class="selected">  void SetAndObserveDoseVolumeNode(vtkMRMLScalarVolumeNode* node);
</li>
          <li>
</li>
          <li>  /// Get segmentation node
</li>
          <li>  vtkMRMLSegmentationNode* GetSegmentationNode();
</li>
          <li>  /// Set and observe segmentation node
</li>
          <li>  void SetAndObserveSegmentationNode(vtkMRMLSegmentationNode* node);
</li>
          <li>
</li>
          <li>  /// Get DVH metrics table node
</li>
          <li>  vtkMRMLTableNode* GetMetricsTableNode();
</li>
          <li>
</li>
          <li>  /// Get chart node
</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
