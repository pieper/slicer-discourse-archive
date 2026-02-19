---
topic_id: 18726
title: "Segment Comparison Tables More Than One Comparison In A Sing"
date: 2021-07-14
url: https://discourse.slicer.org/t/18726
---

# Segment Comparison Tables: more than one comparison in a single table

**Topic ID**: 18726
**Date**: 2021-07-14
**URL**: https://discourse.slicer.org/t/segment-comparison-tables-more-than-one-comparison-in-a-single-table/18726

---

## Post #1 by @liam-stubbington (2021-07-14 10:41 UTC)

<p>Hi,</p>
<p>I’m hugely impressed with SlicerRT’s segment comparison module.<br>
We are fortunate enough to have two independent clinical automatic segmentation algorithms - i’d like to use SlicerRT to compare the homologous structures as part of the commissioning.</p>
<p>At the moment I can only compare one set of structures at a time and copy and paste the results into Excel. I’d like to be able to add subsequent comparisons to the same table.</p>
<p>Or better yet create an extension to compare multiple segments at once - this would have to do some sort of match based on the structure name, then export the results as CSV.</p>
<p>Some advice to get me started would be hugely appreciated.</p>
<p>Thanks.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76ec18b4c12b2265837b6a8abb8f0dae1431b262.jpeg" data-download-href="/uploads/short-url/gY2aUlv6ReDiIGnfiaEZeE1wBMu.jpeg?dl=1" title="NewTableCols.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/76ec18b4c12b2265837b6a8abb8f0dae1431b262_2_690x364.jpeg" alt="NewTableCols.PNG" data-base62-sha1="gY2aUlv6ReDiIGnfiaEZeE1wBMu" width="690" height="364" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/76ec18b4c12b2265837b6a8abb8f0dae1431b262_2_690x364.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/76ec18b4c12b2265837b6a8abb8f0dae1431b262_2_1035x546.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/76ec18b4c12b2265837b6a8abb8f0dae1431b262_2_1380x728.jpeg 2x" data-dominant-color="B0BCAE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">NewTableCols.PNG</span><span class="informations">1465×773 226 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Operating system: Windows 10<br>
Slicer version: 29738</p>

---

## Post #2 by @lassoan (2021-07-15 16:52 UTC)

<p>You can write a short Python script that iterates through the segments and puts the results into a table. There is only a <a href="https://github.com/SlicerRt/SlicerRT/blob/a6e21f17a832d25621b10bac8b02de60a373398b/SegmentComparison/Testing/Cxx/vtkSlicerSegmentComparisonModuleLogicTest1.cxx#L376-L389">C++ example to do this</a>, but you can run the same in Python, just need to change the syntax (see hints <a href="https://slicer.readthedocs.io/en/latest/developer_guide/api.html#doxygen-style-documentation">here</a>, you can find lots of Python examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">script repository</a>, and you can ask questions here if you get stuck at any point).</p>
<p>Just a quick example to get you started:</p>
<pre><code class="lang-python">referenceSegmentationNode = getNode('Segmentation')
referenceSegmentID = referenceSegmentationNode.GetSegmentation().GetSegmentIdBySegmentName("Segment_1")
compareSegmentationNode = getNode('Segmentation')
compareSegmentID = referenceSegmentationNode.GetSegmentation().GetSegmentIdBySegmentName("Segment_2")

paramNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentComparisonNode")
paramNode.SetAndObserveReferenceSegmentationNode(referenceSegmentationNode)
paramNode.SetReferenceSegmentID(referenceSegmentID)
paramNode.SetAndObserveCompareSegmentationNode(compareSegmentationNode)
paramNode.SetCompareSegmentID(compareSegmentID)

segmentComparisonLogic = slicer.modules.segmentcomparison.logic()
segmentComparisonLogic.ComputeDiceStatistics(paramNode)
segmentComparisonLogic.ComputeHausdorffDistances(paramNode)

maxHD = paramNode.GetMaximumHausdorffDistanceForBoundaryMm()
averageHD = paramNode.GetAverageHausdorffDistanceForBoundaryMm()
print(f"Maximum Hausdorff distance: {maxHD}")
print(f"Average Hausdorff distance: {averageHD}")
</code></pre>
<p>You can add a loop that iterates through all the segments and puts the result into a table node. See example of creating and populating a table node <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#measure-distance-of-points-from-surface">here</a> and <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/blob/a5700e941d7a2efe3b96a3d721dd4207bbdf12ac/LungCTAnalyzer/LungCTAnalyzer.py#L1222-L1278">here</a> (create columns, add values to columns, then add the columns to the table).</p>

---

## Post #3 by @Melanie (2023-06-23 03:06 UTC)

<p>Didnt want to create a new topic, as it is an extension of the same.<br>
How do I add ‘dice statistics’ to the same code.</p>
<p>diceStatistics = paramNode.GetDiceStatistics()<br>
does not seem to work</p>

---

## Post #4 by @lassoan (2023-06-23 03:12 UTC)

<p>Type <code>paramNode.</code> in the Python console and hit the Tab key to see the available methods. You can also type <code>help(paramNode)</code> to get the list and documentation of all available methods; or look them up in <a href="https://github.com/SlicerRt/SlicerRT/blob/master/SegmentComparison/Logic/vtkMRMLSegmentComparisonNode.h">github</a>.</p>

---

## Post #5 by @Melanie (2023-06-23 03:23 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="18726">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>help(paramNode)</p>
</blockquote>
</aside>
<p>Thanks very much for the reply. Did that I get a long list which I cant decode, sorry I am not an engineer. Is there anything I should particularly look at pls</p>
<details>
<summary>
OUTPUT</summary>
<blockquote>
<blockquote>
<blockquote>
<p>help(paramNode)<br>
Help on vtkMRMLSegmentComparisonNode object:</p>
</blockquote>
</blockquote>
</blockquote>
<p>class vtkMRMLSegmentComparisonNode(MRMLCorePython.vtkMRMLNode)<br>
|  vtkMRMLSegmentComparisonNode - \ingroup<br>
|  SlicerRt_QtModules_SegmentComparison<br>
|<br>
|  Superclass: vtkMRMLNode<br>
|<br>
|  Method resolution order:<br>
|      vtkMRMLSegmentComparisonNode<br>
|      MRMLCorePython.vtkMRMLNode<br>
|      vtkCommonCorePython.vtkObject<br>
|      vtkCommonCorePython.vtkObjectBase<br>
|      builtins.object<br>
|<br>
|  Methods defined here:<br>
|<br>
|  Copy(…)<br>
|      V.Copy(vtkMRMLNode)<br>
|      C++: void Copy(vtkMRMLNode *node) override;<br>
|<br>
|      Copy the node’s attributes to this object<br>
|<br>
|  CreateNodeInstance(…)<br>
|      V.CreateNodeInstance() → vtkMRMLNode<br>
|      C++: vtkMRMLNode *CreateNodeInstance() override;<br>
|<br>
|      Create instance of a GAD node.<br>
|<br>
|  DiceResultsValidOff(…)<br>
|      V.DiceResultsValidOff()<br>
|      C++: virtual void DiceResultsValidOff()<br>
|<br>
|  DiceResultsValidOn(…)<br>
|      V.DiceResultsValidOn()<br>
|      C++: virtual void DiceResultsValidOn()<br>
|<br>
|  GetAverageHausdorffDistanceForBoundaryMm(…)<br>
|      V.GetAverageHausdorffDistanceForBoundaryMm() → float<br>
|      C++: virtual double GetAverageHausdorffDistanceForBoundaryMm()<br>
|<br>
|      Get average Hausdorff distance for the boundary voxels<br>
|<br>
|  GetAverageHausdorffDistanceForVolumeMm(…)<br>
|      V.GetAverageHausdorffDistanceForVolumeMm() → float<br>
|      C++: virtual double GetAverageHausdorffDistanceForVolumeMm()<br>
|<br>
|      Get average Hausdorff distance for the whole volume<br>
|<br>
|  GetCompareCenter(…)<br>
|      V.GetCompareCenter() → (float, float, float)<br>
|      C++: double *GetCompareCenter()<br>
|<br>
|  GetCompareSegmentID(…)<br>
|      V.GetCompareSegmentID() → string<br>
|      C++: virtual char *GetCompareSegmentID()<br>
|<br>
|      Get compare segment ID<br>
|<br>
|  GetCompareSegmentationNode(…)<br>
|      V.GetCompareSegmentationNode() → vtkMRMLSegmentationNode<br>
|      C++: vtkMRMLSegmentationNode *GetCompareSegmentationNode()<br>
|<br>
|      Get compare segmentation node<br>
|<br>
|  GetCompareVolumeCc(…)<br>
|      V.GetCompareVolumeCc() → float<br>
|      C++: virtual double GetCompareVolumeCc()<br>
|<br>
|      Get volume of the compare structure<br>
|<br>
|  GetDiceCoefficient(…)<br>
|      V.GetDiceCoefficient() → float<br>
|      C++: virtual float GetDiceCoefficient()<br>
|<br>
|      Get result dice coefficient<br>
|<br>
|  GetDiceResultsValid(…)<br>
|      V.GetDiceResultsValid() → bool<br>
|      C++: virtual bool GetDiceResultsValid()<br>
|<br>
|      Get/Set Dice results valid flag<br>
|<br>
|  GetDiceTableNode(…)<br>
|      V.GetDiceTableNode() → vtkMRMLTableNode<br>
|      C++: vtkMRMLTableNode *GetDiceTableNode()<br>
|<br>
|      Get Dice table node<br>
|<br>
|  GetFalseNegativesPercent(…)<br>
|      V.GetFalseNegativesPercent() → float<br>
|      C++: virtual double GetFalseNegativesPercent()<br>
|<br>
|      Get percentage of false negative labelmap voxels<br>
|<br>
|  GetFalsePositivesPercent(…)<br>
|      V.GetFalsePositivesPercent() → float<br>
|      C++: virtual double GetFalsePositivesPercent()<br>
|<br>
|      Get percentage of false positive labelmap voxels<br>
|<br>
|  GetHausdorffResultsValid(…)<br>
|      V.GetHausdorffResultsValid() → bool<br>
|      C++: virtual bool GetHausdorffResultsValid()<br>
|<br>
|      Get/Set results Hausdorff valid flag<br>
|<br>
|  GetHausdorffTableNode(…)<br>
|      V.GetHausdorffTableNode() → vtkMRMLTableNode<br>
|      C++: vtkMRMLTableNode *GetHausdorffTableNode()<br>
|<br>
|      Get Hausdorff table node<br>
|<br>
|  GetMaximumHausdorffDistanceForBoundaryMm(…)<br>
|      V.GetMaximumHausdorffDistanceForBoundaryMm() → float<br>
|      C++: virtual double GetMaximumHausdorffDistanceForBoundaryMm()<br>
|<br>
|      Get maximum Hausdorff distance for the boundary voxels<br>
|<br>
|  GetMaximumHausdorffDistanceForVolumeMm(…)<br>
|      V.GetMaximumHausdorffDistanceForVolumeMm() → float<br>
|      C++: virtual double GetMaximumHausdorffDistanceForVolumeMm()<br>
|<br>
|      Get maximum Hausdorff distance for the whole volume<br>
|<br>
|  GetNodeTagName(…)<br>
|      V.GetNodeTagName() → string<br>
|      C++: const char *GetNodeTagName() override;<br>
|<br>
|      Get unique node XML tag name (like Volume, Model)<br>
|<br>
|  GetPercent95HausdorffDistanceForBoundaryMm(…)<br>
|      V.GetPercent95HausdorffDistanceForBoundaryMm() → float<br>
|      C++: virtual double GetPercent95HausdorffDistanceForBoundaryMm()<br>
|<br>
|      Get 95% Hausdorff distance for the boundary voxels<br>
|<br>
|  GetPercent95HausdorffDistanceForVolumeMm(…)<br>
|      V.GetPercent95HausdorffDistanceForVolumeMm() → float<br>
|      C++: virtual double GetPercent95HausdorffDistanceForVolumeMm()<br>
|<br>
|      Get 95% Hausdorff distance for whole volume<br>
|<br>
|  GetRasterizationReferenceVolumeNode(…)<br>
|      V.GetRasterizationReferenceVolumeNode() → vtkMRMLScalarVolumeNode<br>
|      C++: vtkMRMLScalarVolumeNode *GetRasterizationReferenceVolumeNode(<br>
|          )<br>
|<br>
|      Get rasterization reference volume node<br>
|<br>
|  GetReferenceCenter(…)<br>
|      V.GetReferenceCenter() → (float, float, float)<br>
|      C++: double *GetReferenceCenter()<br>
|<br>
|  GetReferenceSegmentID(…)<br>
|      V.GetReferenceSegmentID() → string<br>
|      C++: virtual char *GetReferenceSegmentID()<br>
|<br>
|      Get reference segment ID<br>
|<br>
|  GetReferenceSegmentationNode(…)<br>
|      V.GetReferenceSegmentationNode() → vtkMRMLSegmentationNode<br>
|      C++: vtkMRMLSegmentationNode *GetReferenceSegmentationNode()<br>
|<br>
|      Get reference segmentation node<br>
|<br>
|  GetReferenceVolumeCc(…)<br>
|      V.GetReferenceVolumeCc() → float<br>
|      C++: virtual double GetReferenceVolumeCc()<br>
|<br>
|      Get volume of the reference structure<br>
|<br>
|  GetTrueNegativesPercent(…)<br>
|      V.GetTrueNegativesPercent() → float<br>
|      C++: virtual double GetTrueNegativesPercent()<br>
|<br>
|      Get percentage of true negative labelmap voxels<br>
|<br>
|  GetTruePositivesPercent(…)<br>
|      V.GetTruePositivesPercent() → float<br>
|      C++: virtual double GetTruePositivesPercent()<br>
|<br>
|      Get percentage of true positive labelmap voxels<br>
|<br>
|  HausdorffResultsValidOff(…)<br>
|      V.HausdorffResultsValidOff()<br>
|      C++: virtual void HausdorffResultsValidOff()<br>
|<br>
|  HausdorffResultsValidOn(…)<br>
|      V.HausdorffResultsValidOn()<br>
|      C++: virtual void HausdorffResultsValidOn()<br>
|<br>
|  IsA(…)<br>
|      V.IsA(string) → int<br>
|      C++: vtkTypeBool IsA(const char *type) override;<br>
|<br>
|      Return 1 if this class is the same type of (or a subclass of) the<br>
|      named class. Returns 0 otherwise. This method works in<br>
|      combination with vtkTypeMacro found in vtkSetGet.h.<br>
|<br>
|  IsTypeOf(…)<br>
|      V.IsTypeOf(string) → int<br>
|      C++: static vtkTypeBool IsTypeOf(const char *type)<br>
|<br>
|      Return 1 if this class type is the same type of (or a subclass<br>
|      of) the named class. Returns 0 otherwise. This method works in<br>
|      combination with vtkTypeMacro found in vtkSetGet.h.<br>
|<br>
|  NewInstance(…)<br>
|      V.NewInstance() → vtkMRMLSegmentComparisonNode<br>
|      C++: vtkMRMLSegmentComparisonNode *NewInstance()<br>
|<br>
|  SafeDownCast(…)<br>
|      V.SafeDownCast(vtkObjectBase) → vtkMRMLSegmentComparisonNode<br>
|      C++: static vtkMRMLSegmentComparisonNode *SafeDownCast(<br>
|          vtkObjectBase *o)<br>
|<br>
|  SetAndObserveCompareSegmentationNode(…)<br>
|      V.SetAndObserveCompareSegmentationNode(vtkMRMLSegmentationNode)<br>
|      C++: void SetAndObserveCompareSegmentationNode(<br>
|          vtkMRMLSegmentationNode *node)<br>
|<br>
|      Set compare segmentation node<br>
|<br>
|  SetAndObserveDiceTableNode(…)<br>
|      V.SetAndObserveDiceTableNode(vtkMRMLTableNode)<br>
|      C++: void SetAndObserveDiceTableNode(vtkMRMLTableNode *node)<br>
|<br>
|      Set Dice table node<br>
|<br>
|  SetAndObserveHausdorffTableNode(…)<br>
|      V.SetAndObserveHausdorffTableNode(vtkMRMLTableNode)<br>
|      C++: void SetAndObserveHausdorffTableNode(vtkMRMLTableNode *node)<br>
|<br>
|      Set Hausdorff table node<br>
|<br>
|  SetAndObserveRasterizationReferenceVolumeNode(…)<br>
|      V.SetAndObserveRasterizationReferenceVolumeNode(<br>
|          vtkMRMLScalarVolumeNode)<br>
|      C++: void SetAndObserveRasterizationReferenceVolumeNode(<br>
|          vtkMRMLScalarVolumeNode *node)<br>
|<br>
|      Set rasterization reference volume node<br>
|<br>
|  SetAndObserveReferenceSegmentationNode(…)<br>
|      V.SetAndObserveReferenceSegmentationNode(vtkMRMLSegmentationNode)<br>
|      C++: void SetAndObserveReferenceSegmentationNode(<br>
|          vtkMRMLSegmentationNode *node)<br>
|<br>
|      Set reference segmentation node<br>
|<br>
|  SetAverageHausdorffDistanceForBoundaryMm(…)<br>
|      V.SetAverageHausdorffDistanceForBoundaryMm(float)<br>
|      C++: virtual void SetAverageHausdorffDistanceForBoundaryMm(<br>
|          double _arg)<br>
|<br>
|      Set average Hausdorff distance for the boundary voxels<br>
|<br>
|  SetAverageHausdorffDistanceForVolumeMm(…)<br>
|      V.SetAverageHausdorffDistanceForVolumeMm(float)<br>
|      C++: virtual void SetAverageHausdorffDistanceForVolumeMm(<br>
|          double _arg)<br>
|<br>
|      Set average Hausdorff distance for the whole volume<br>
|<br>
|  SetCompareCenter(…)<br>
|      V.SetCompareCenter(float, float, float)<br>
|      C++: void SetCompareCenter(double, double, double)<br>
|      V.SetCompareCenter((float, float, float))<br>
|      C++: void SetCompareCenter(double a[3])<br>
|<br>
|  SetCompareSegmentID(…)<br>
|      V.SetCompareSegmentID(string)<br>
|      C++: virtual void SetCompareSegmentID(const char *_arg)<br>
|<br>
|      Set compare segment ID<br>
|<br>
|  SetCompareVolumeCc(…)<br>
|      V.SetCompareVolumeCc(float)<br>
|      C++: virtual void SetCompareVolumeCc(double _arg)<br>
|<br>
|      Set volume of the compare structure<br>
|<br>
|  SetDiceCoefficient(…)<br>
|      V.SetDiceCoefficient(float)<br>
|      C++: virtual void SetDiceCoefficient(float _arg)<br>
|<br>
|      Set result dice coefficient<br>
|<br>
|  SetDiceResultsValid(…)<br>
|      V.SetDiceResultsValid(bool)<br>
|      C++: virtual void SetDiceResultsValid(bool _arg)<br>
|<br>
|  SetFalseNegativesPercent(…)<br>
|      V.SetFalseNegativesPercent(float)<br>
|      C++: virtual void SetFalseNegativesPercent(double _arg)<br>
|<br>
|      Set percentage of false negative labelmap voxels<br>
|<br>
|  SetFalsePositivesPercent(…)<br>
|      V.SetFalsePositivesPercent(float)<br>
|      C++: virtual void SetFalsePositivesPercent(double _arg)<br>
|<br>
|      Set percentage of false positive labelmap voxels<br>
|<br>
|  SetHausdorffResultsValid(…)<br>
|      V.SetHausdorffResultsValid(bool)<br>
|      C++: virtual void SetHausdorffResultsValid(bool _arg)<br>
|<br>
|  SetMaximumHausdorffDistanceForBoundaryMm(…)<br>
|      V.SetMaximumHausdorffDistanceForBoundaryMm(float)<br>
|      C++: virtual void SetMaximumHausdorffDistanceForBoundaryMm(<br>
|          double _arg)<br>
|<br>
|      Set maximum Hausdorff distance for the boundary voxels<br>
|<br>
|  SetMaximumHausdorffDistanceForVolumeMm(…)<br>
|      V.SetMaximumHausdorffDistanceForVolumeMm(float)<br>
|      C++: virtual void SetMaximumHausdorffDistanceForVolumeMm(<br>
|          double _arg)<br>
|<br>
|      Set maximum Hausdorff distance for the whole volume<br>
|<br>
|  SetPercent95HausdorffDistanceForBoundaryMm(…)<br>
|      V.SetPercent95HausdorffDistanceForBoundaryMm(float)<br>
|      C++: virtual void SetPercent95HausdorffDistanceForBoundaryMm(<br>
|          double _arg)<br>
|<br>
|      Set 95% Hausdorff distance for the boundary voxels<br>
|<br>
|  SetPercent95HausdorffDistanceForVolumeMm(…)<br>
|      V.SetPercent95HausdorffDistanceForVolumeMm(float)<br>
|      C++: virtual void SetPercent95HausdorffDistanceForVolumeMm(<br>
|          double _arg)<br>
|<br>
|      Set 95% Hausdorff distance for whole volume<br>
|<br>
|  SetReferenceCenter(…)<br>
|      V.SetReferenceCenter(float, float, float)<br>
|      C++: void SetReferenceCenter(double, double, double)<br>
|      V.SetReferenceCenter((float, float, float))<br>
|      C++: void SetReferenceCenter(double a[3])<br>
|<br>
|  SetReferenceSegmentID(…)<br>
|      V.SetReferenceSegmentID(string)<br>
|      C++: virtual void SetReferenceSegmentID(const char *_arg)<br>
|<br>
|      Set reference segment ID<br>
|<br>
|  SetReferenceVolumeCc(…)<br>
|      V.SetReferenceVolumeCc(float)<br>
|      C++: virtual void SetReferenceVolumeCc(double _arg)<br>
|<br>
|      Set volume of the reference structure<br>
|<br>
|  SetTrueNegativesPercent(…)<br>
|      V.SetTrueNegativesPercent(float)<br>
|      C++: virtual void SetTrueNegativesPercent(double _arg)<br>
|<br>
|      Set percentage of true negative labelmap voxels<br>
|<br>
|  SetTruePositivesPercent(…)<br>
|      V.SetTruePositivesPercent(float)<br>
|      C++: virtual void SetTruePositivesPercent(double _arg)<br>
|<br>
|      Set percentage of true positive labelmap voxels<br>
|<br>
|  <strong>delattr</strong>(self, name, /)<br>
|      Implement delattr(self, name).<br>
|<br>
|  <strong>getattribute</strong>(self, name, /)<br>
|      Return getattr(self, name).<br>
|<br>
|  <strong>new</strong>(*args, **kwargs) from builtins.type<br>
|      Create and return a new object.  See help(type) for accurate signature.<br>
|<br>
|  <strong>repr</strong>(self, /)<br>
|      Return repr(self).<br>
|<br>
|  <strong>setattr</strong>(self, name, value, /)<br>
|      Implement setattr(self, name, value).<br>
|<br>
|  <strong>str</strong>(self, /)<br>
|      Return str(self).<br>
|<br>
|  ----------------------------------------------------------------------<br>
|  Data descriptors defined here:<br>
|<br>
|  <strong>dict</strong><br>
|      Dictionary of attributes set by user.<br>
|<br>
|  <strong>this</strong><br>
|      Pointer to the C++ object.<br>
|<br>
|  ----------------------------------------------------------------------<br>
|  Data and other attributes defined here:<br>
|<br>
|  <strong>vtkname</strong> = ‘vtkMRMLSegmentComparisonNode’<br>
|<br>
|  ----------------------------------------------------------------------<br>
|  Methods inherited from MRMLCorePython.vtkMRMLNode:<br>
|<br>
|  AddAndObserveNodeReferenceID(…)<br>
|      V.AddAndObserveNodeReferenceID(string, string, vtkIntArray)<br>
|          → vtkMRMLNode<br>
|      C++: vtkMRMLNode *AddAndObserveNodeReferenceID(<br>
|          const char *referenceRole, const char *referencedNodeID,<br>
|          vtkIntArray *events=nullptr)<br>
|<br>
|      Add and observe a reference node from this node for a<br>
|          specificreferenceRole.<br>
|<br>
|      Observe Modified event by default, optionally takes array of<br>
|      events.<br>
|<br>
|  AddNodeReferenceID(…)<br>
|      V.AddNodeReferenceID(string, string) → vtkMRMLNode<br>
|      C++: vtkMRMLNode *AddNodeReferenceID(const char *referenceRole,<br>
|          const char *referencedNodeID)<br>
|<br>
|      Convenience method that adds a referencedNodeID at the end of the<br>
|      list.<br>
|<br>
|  AddNodeReferenceRole(…)<br>
|      V.AddNodeReferenceRole(string, string, vtkIntArray)<br>
|      C++: void AddNodeReferenceRole(const char *referenceRole,<br>
|          const char <em>mrmlAttributeName=nullptr,<br>
|          vtkIntArray <em>events=nullptr)<br>
|<br>
|      Add a referenceRole.<br>
|<br>
|      The referenceRole can be any unique string, for example<br>
|      “display”, “transform” etc. Optionally a MRML attribute name for<br>
|      storing the reference in the mrml scene file can be specified.<br>
|      For example “displayNodeRef”. If omitted the MRML attribute name<br>
|      will be the same as the role. If referenceRole ends with ‘/’, it<br>
|      is considered as a “template” reference role that can be used to<br>
|      generate attribute names dynamically by concatenation: If<br>
|      referenceRole is “unit/” and mrmlAttributeName is “UnitRef”, then<br>
|      the generated MRML attribute names for a node reference role of<br>
|      “unit/length” will be “lengthUnitRef”. Use this method to add new<br>
|      reference types to a node. This method is typically called in the<br>
|      constructors of each subclass. The optional events argument<br>
|      specifies what events should be observed by default (e.g., when<br>
|      loading the scene from file). If referenceRole ends with ‘/’<br>
|      character then events are used for all roles names begins with<br>
|      this role name (for example, events specified for<br>
|      referenceRole=‘unit/’ will be used for<br>
|      referenceRole=‘unit/length’, referenceRole=‘unit/area’, etc).<br>
|      \sa GetReferenceNodeFromMRMLAttributeName()<br>
|<br>
|  AddToSceneOff(…)<br>
|      V.AddToSceneOff()<br>
|      C++: virtual void AddToSceneOff()<br>
|<br>
|  AddToSceneOn(…)<br>
|      V.AddToSceneOn()<br>
|      C++: virtual void AddToSceneOn()<br>
|<br>
|  CopyContent(…)<br>
|      V.CopyContent(vtkMRMLNode, bool)<br>
|      C++: virtual void CopyContent(vtkMRMLNode <em>node,<br>
|          bool deepCopy=true)<br>
|<br>
|      Copy node contents from another node of the same type.<br>
|      Does not copy node ID, Scene, Name, SingletonTag,<br>
|      HideFromEditors, AddToScene, UndoEnabled, and node references. If<br>
|      deepCopy is set to false then a shallow copy of bulk data (such<br>
|      as image or mesh data) could be made; copying may be faster but<br>
|      the node may share some data with the source node instead of<br>
|      creating an independent copy.<br>
|<br>
|      ote If a class implements this then make sure CopyContent and<br>
|      HasCopyContent methods are implemented in all parent classes by<br>
|      adding vtkMRMLCopyContentMacro(ClassName) to the class headers.<br>
|<br>
|  CopyReferences(…)<br>
|      V.CopyReferences(vtkMRMLNode)<br>
|      C++: virtual void CopyReferences(vtkMRMLNode <em>node)<br>
|<br>
|      Copy the references of the node into this.<br>
|<br>
|      Existing references will be replaced if found in node, or removed<br>
|      if not in node.<br>
|<br>
|  CopyWithScene(…)<br>
|      V.CopyWithScene(vtkMRMLNode)<br>
|      C++: void CopyWithScene(vtkMRMLNode <em>node)<br>
|<br>
|      Copy everything (including Scene and ID) from another node of<br>
|      the same type.<br>
|<br>
|      ote The node is <strong>not</strong> added into the scene of node. You must do<br>
|      it manually <strong>after</strong> calling CopyWithScene(vtkMRMLNode</em>) using<br>
|      vtkMRMLScene::AddNode(vtkMRMLNode</em>). Only one<br>
|      vtkCommand::ModifiedEvent is invoked, after the copy is fully<br>
|      completed.<br>
|<br>
|      \bug Calling vtkMRMLScene::AddNode(vtkMRMLNode</em>) <strong>before</strong><br>
|      CopyWithScene(vtkMRMLNode</em>) is <strong>NOT</strong> supported, it will<br>
|      unsynchronize the node internal caches. See<br>
|      <a href="https://github.com/Slicer/Slicer/issues/4078" rel="noopener nofollow ugc">#4078</a><br>
|<br>
|      \sa vtkMRMLScene::AddNode(vtkMRMLNode</em>)<br>
|<br>
|  DisableModifiedEventOff(…)<br>
|      V.DisableModifiedEventOff()<br>
|      C++: void DisableModifiedEventOff()<br>
|<br>
|  DisableModifiedEventOn(…)<br>
|      V.DisableModifiedEventOn()<br>
|      C++: void DisableModifiedEventOn()<br>
|<br>
|  EndModify(…)<br>
|      V.EndModify(int) → int<br>
|      C++: virtual int EndModify(int previousDisableModifiedEventState)<br>
|<br>
|      End modifying the node.<br>
|<br>
|      Enable Modify events if the previous state ofDisableModifiedEvent<br>
|      flag is 0.<br>
|<br>
|      Return the number of pending events (even if<br>
|      InvokePendingModifiedEvent() is not called).<br>
|<br>
|  GetAddToScene(…)<br>
|      V.GetAddToScene() → int<br>
|      C++: virtual int GetAddToScene()<br>
|<br>
|      node added to MRML scene.<br>
|<br>
|  GetAttribute(…)<br>
|      V.GetAttribute(string) → string<br>
|      C++: const char *GetAttribute(const char *name)<br>
|<br>
|      Get value of a name value pair attribute.<br>
|<br>
|      Return nullptr if the name does not exists.<br>
|<br>
|  GetAttributeNames(…)<br>
|      V.GetAttributeNames() → Stvector_ISt6stringE<br>
|      C++: std::vector<a>std::string</a> GetAttributeNames()<br>
|      V.GetAttributeNames(vtkStringArray)<br>
|      C++: void GetAttributeNames(vtkStringArray *attributeNames)<br>
|<br>
|      Get all attribute names.<br>
|<br>
|  GetContentModifiedEvents(…)<br>
|      V.GetContentModifiedEvents() → vtkIntArray<br>
|      C++: virtual vtkIntArray *GetContentModifiedEvents()<br>
|<br>
|      Return list of events that indicate that content of the node is<br>
|      modified. For example, it is not enough to observe<br>
|      vtkCommand::ModifiedEvent to get notified when a transform stored<br>
|      in a transform node is modified, but<br>
|      vtkMRMLTransformableNode::TransformModifiedEvent must be observed<br>
|      as well.<br>
|<br>
|  GetDescription(…)<br>
|      V.GetDescription() → string<br>
|      C++: virtual char *GetDescription()<br>
|<br>
|  GetDisableModifiedEvent(…)<br>
|      V.GetDisableModifiedEvent() → int<br>
|      C++: virtual int GetDisableModifiedEvent()<br>
|<br>
|      Turn on/off generating InvokeEvent for set macros<br>
|<br>
|  GetHideFromEditors(…)<br>
|      V.GetHideFromEditors() → int<br>
|      C++: virtual int GetHideFromEditors()<br>
|<br>
|      Describes if the node is hidden.<br>
|<br>
|  GetID(…)<br>
|      V.GetID() → string<br>
|      C++: virtual char *GetID()<br>
|<br>
|      ID use by other nodes to reference this node in XML.<br>
|<br>
|  GetInMRMLCallbackFlag(…)<br>
|      V.GetInMRMLCallbackFlag() → int<br>
|      C++: virtual int GetInMRMLCallbackFlag()<br>
|<br>
|      Flags to avoid event loops.<br>
|<br>
|      \warning Do NOT use the SetMacro or it call modified on itself<br>
|          and<br>
|      generate even more events!<br>
|<br>
|  GetModifiedEventPending(…)<br>
|      V.GetModifiedEventPending() → int<br>
|      C++: virtual int GetModifiedEventPending()<br>
|<br>
|      Number of pending modified events.<br>
|<br>
|      \sa InvokePendingModifiedEvent()<br>
|      \sa Modified()<br>
|      \sa GetDisableModifiedEvent()<br>
|<br>
|  GetName(…)<br>
|      V.GetName() → string<br>
|      C++: virtual char *GetName()<br>
|<br>
|  GetNodeReference(…)<br>
|      V.GetNodeReference(string) → vtkMRMLNode<br>
|      C++: vtkMRMLNode *GetNodeReference(const char *referenceRole)<br>
|<br>
|      Utility function that returns the first referenced node.<br>
|      \sa GetNthNodeReference(int), GetNodeReferenceID()<br>
|<br>
|  GetNodeReferenceID(…)<br>
|      V.GetNodeReferenceID(string) → string<br>
|      C++: const char *GetNodeReferenceID(const char *referenceRole)<br>
|<br>
|      Utility function that returns the first node id for a<br>
|          specificreferenceRole.<br>
|<br>
|      \sa GetNthNodeReferenceID(int), GetNodeReference()<br>
|<br>
|  GetNodeReferenceRoles(…)<br>
|      V.GetNodeReferenceRoles(Stvector_ISt6stringE)<br>
|      C++: void GetNodeReferenceRoles(std::vector<a>std::string</a> &amp;roles)<br>
|<br>
|      Get reference roles of the present node references.<br>
|      \sa GetNodeReferenceRoles(), GetNodeReferenceRoles(),<br>
|          GetNthNodeReferenceRole()<br>
|<br>
|  GetNthNodeReference(…)<br>
|      V.GetNthNodeReference(string, int) → vtkMRMLNode<br>
|      C++: vtkMRMLNode *GetNthNodeReference(const char *referenceRole,<br>
|          int n)<br>
|<br>
|      Get referenced MRML node for a specific referenceRole.<br>
|<br>
|      Can be 0 in temporary states; e.g. if the referenced node has no<br>
|      scene, or if the referenced is not yet into the scene. If not<br>
|      cached, it tnternally scans (slow) the scene to search for the<br>
|      associated referenced node ID. If the referencing node is no<br>
|      longer in the scene (GetScene() == 0), it happens after the node<br>
|      is removed from the scene (scene-&gt;RemoveNode(dn), the returned<br>
|      referenced node is 0.<br>
|<br>
|  GetNthNodeReferenceID(…)<br>
|      V.GetNthNodeReferenceID(string, int) → string<br>
|      C++: const char *GetNthNodeReferenceID(const char *referenceRole,<br>
|          int n)<br>
|<br>
|      Return the string of the Nth node ID for a specific reference<br>
|          role.<br>
|<br>
|      Return 0 if no such node exist.<br>
|<br>
|      \warning A temporary char generated from a std::string::c_str()<br>
|      is returned.<br>
|<br>
|  GetNthNodeReferenceRole(…)<br>
|      V.GetNthNodeReferenceRole(int) → string<br>
|      C++: const char *GetNthNodeReferenceRole(int n)<br>
|<br>
|      Get a specific node reference role name.<br>
|      \sa GetNodeReferenceRoles(), GetNodeReferenceRoles(),<br>
|          GetNthNodeReferenceRole()<br>
|<br>
|  GetNumberOfNodeReferenceRoles(…)<br>
|      V.GetNumberOfNodeReferenceRoles() → int<br>
|      C++: int GetNumberOfNodeReferenceRoles()<br>
|<br>
|      Get number of node reference role names.<br>
|      \sa GetNodeReferenceRoles(), GetNodeReferenceRoles(),<br>
|          GetNthNodeReferenceRole()<br>
|<br>
|  GetNumberOfNodeReferences(…)<br>
|      V.GetNumberOfNodeReferences(string) → int<br>
|      C++: int GetNumberOfNodeReferences(const char *referenceRole)<br>
|<br>
|      Return the number of node IDs for a specific reference role (and<br>
|          nodes as they always<br>
|      have the same size).<br>
|<br>
|  GetSaveWithScene(…)<br>
|      V.GetSaveWithScene() → int<br>
|      C++: virtual int GetSaveWithScene()<br>
|<br>
|      Save node with MRML scene.<br>
|<br>
|  GetScene(…)<br>
|      V.GetScene() → vtkMRMLScene<br>
|      C++: virtual vtkMRMLScene *GetScene()<br>
|<br>
|      Get the scene this node has been added to.<br>
|<br>
|  GetSelectable(…)<br>
|      V.GetSelectable() → int<br>
|      C++: virtual int GetSelectable()<br>
|<br>
|      Describes if the node is selectable.<br>
|<br>
|  GetSelected(…)<br>
|      V.GetSelected() → int<br>
|      C++: virtual int GetSelected()<br>
|<br>
|      Get/Set for Selected<br>
|<br>
|  GetSingletonTag(…)<br>
|      V.GetSingletonTag() → string<br>
|      C++: virtual char *GetSingletonTag()<br>
|<br>
|  GetUndoEnabled(…)<br>
|      V.GetUndoEnabled() → bool<br>
|      C++: virtual bool GetUndoEnabled()<br>
|<br>
|      Specifies if the state of this node is stored in the scene’s undo<br>
|      buffer. False by default to make sure that undo can be enabled<br>
|      selectively, only for nodes that are prepared to work correctly<br>
|      when saved/restored. Nodes with different UndoEnabled value must<br>
|      not reference to each other, because restoring states could lead<br>
|      to unresolved node references. Therefore, when undo is enabled<br>
|      for a certain node, it must be enabled for nodes that it<br>
|      references (for example, if undo is enabled for vtkMRMLModelNode<br>
|      then it must be enabled for vtkMRMLModelDisplayNode and<br>
|      vtkMRMLModelStorageNode as well).<br>
|<br>
|  HasCopyContent(…)<br>
|      V.HasCopyContent() → bool<br>
|      C++: virtual bool HasCopyContent()<br>
|<br>
|      Returns true if the class supports deep and shallow copying node<br>
|          content.<br>
|<br>
|  HasNodeReferenceID(…)<br>
|      V.HasNodeReferenceID(string, string) → bool<br>
|      C++: bool HasNodeReferenceID(const char *referenceRole,<br>
|          const char *referencedNodeID)<br>
|<br>
|      Return true if referencedNodeID is in the node ID list for a<br>
|      specific referenceRole.<br>
|<br>
|      If nullptr is specified as role then all roles are checked.<br>
|<br>
|  HideFromEditorsOff(…)<br>
|      V.HideFromEditorsOff()<br>
|      C++: virtual void HideFromEditorsOff()<br>
|<br>
|  HideFromEditorsOn(…)<br>
|      V.HideFromEditorsOn()<br>
|      C++: virtual void HideFromEditorsOn()<br>
|<br>
|  InvokeCustomModifiedEvent(…)<br>
|      V.InvokeCustomModifiedEvent(int, void)<br>
|      C++: virtual void InvokeCustomModifiedEvent(int eventId,<br>
|          void *callData=nullptr)<br>
|<br>
|      This method allows the node to compress events.<br>
|<br>
|      Instead of invoking a certain event several times, the event is<br>
|      called only once, for all the invocations that are made between<br>
|      StartModify() and EndModify().<br>
|<br>
|      Typical usage is to group several <code>...Added</code>, <code>...Removed</code>,<br>
|      <code>...Modified</code> events into one, to improve performance.<br>
|<br>
|      callData is passed to InvokeEvent() if the event is invoked<br>
|      immediately.<br>
|<br>
|      If the event is not invoked immediately then it will be sent with<br>
|      <code>callData=nullptr</code>.<br>
|<br>
|  InvokePendingModifiedEvent(…)<br>
|      V.InvokePendingModifiedEvent() → int<br>
|      C++: virtual int InvokePendingModifiedEvent()<br>
|<br>
|      Invokes any modified events that are <code>pending</code>.<br>
|<br>
|      Pending modified events were generated while the<br>
|      DisableModifiedEvent flag was nonzero.<br>
|<br>
|      Returns the total number of pending modified events that have<br>
|      been replaced by the just invoked modified event(s).<br>
|<br>
|  IsSingleton(…)<br>
|      V.IsSingleton() → bool<br>
|      C++: bool IsSingleton()<br>
|<br>
|  Modified(…)<br>
|      V.Modified()<br>
|      C++: void Modified() override;<br>
|<br>
|      Customized version of Modified() allowing to compress<br>
|      vtkCommand::ModifiedEvent.<br>
|<br>
|      It overrides the vtkObject method so that all changes to the node<br>
|      which would normally generate a vtkCommand::ModifiedEvent can be<br>
|      grouped into an <code>atomic</code> operation.<br>
|<br>
|      Typical usage would be to disable modified events, call a series<br>
|      of <code>Set*</code> operations, and then re-enable modified events and call<br>
|      InvokePendingModifiedEvent() to invoke the event (if any of the<br>
|      <code>Set*</code> calls actually changed the values of the instance<br>
|      variables).<br>
|<br>
|      \sa GetDisableModifiedEvent()<br>
|<br>
|  OnNodeAddedToScene(…)<br>
|      V.OnNodeAddedToScene()<br>
|      C++: virtual void OnNodeAddedToScene()<br>
|<br>
|      Updates this node if it depends on other nodes when the scene is<br>
|      read in This method is called by scene when a node added to a<br>
|      scene.<br>
|<br>
|  ProcessChildNode(…)<br>
|      V.ProcessChildNode(vtkMRMLNode)<br>
|      C++: virtual void ProcessChildNode(vtkMRMLNode *)<br>
|<br>
|      Set dependencies between this node and a child node<br>
|      when parsing XML file.<br>
|<br>
|  ProcessMRMLEvents(…)<br>
|      V.ProcessMRMLEvents(vtkObject, int, void)<br>
|      C++: virtual void ProcessMRMLEvents(vtkObject *caller,<br>
|          unsigned long event, void *callData)<br>
|<br>
|      Propagate events generated in mrml.<br>
|<br>
|  RemoveAttribute(…)<br>
|      V.RemoveAttribute(string)<br>
|      C++: void RemoveAttribute(const char *name)<br>
|<br>
|      Remove attribute with the specified name.<br>
|<br>
|  RemoveNodeReferenceIDs(…)<br>
|      V.RemoveNodeReferenceIDs(string)<br>
|      C++: void RemoveNodeReferenceIDs(const char *referenceRole)<br>
|<br>
|      Remove all node IDs and associated nodes for a specific<br>
|          referenceRole.<br>
|<br>
|      If referenceRole is 0 remove references for all roles<br>
|<br>
|  RemoveNthNodeReferenceID(…)<br>
|      V.RemoveNthNodeReferenceID(string, int)<br>
|      C++: void RemoveNthNodeReferenceID(const char *referenceRole,<br>
|          int n)<br>
|<br>
|      Convenience method that removes the Nth node ID from the list.<br>
|<br>
|  Reset(…)<br>
|      V.Reset(vtkMRMLNode)<br>
|      C++: virtual void Reset(vtkMRMLNode *defaultNode)<br>
|<br>
|      Reset node attributes to the initial state as defined in the<br>
|      constructor or the passed default node.<br>
|<br>
|      It preserves values of the following dynamic attributes that may<br>
|      be set by an application:<br>
|      * SaveWithScene<br>
|      * HideFromEditors<br>
|      * Selectable<br>
|      * SingletonTag.<br>
|<br>
|      If a defaultNode pointer is passed then the values stored in that<br>
|      node will be used to set the node contents. If defaultNode is<br>
|      nullptr then the values set in the constructor of the class will<br>
|      be used to set the node contents.<br>
|<br>
|      ote Other attributes that needs to be preserved should be handled<br>
|      in the subclass.<br>
|<br>
|      \sa SetSaveWithScene()<br>
|      \sa SetHideFromEditors()<br>
|      \sa SetSelectable()<br>
|      \sa SetSingletonTag()<br>
|<br>
|  SaveWithSceneOff(…)<br>
|      V.SaveWithSceneOff()<br>
|      C++: virtual void SaveWithSceneOff()<br>
|<br>
|  SaveWithSceneOn(…)<br>
|      V.SaveWithSceneOn()<br>
|      C++: virtual void SaveWithSceneOn()<br>
|<br>
|  SelectableOff(…)<br>
|      V.SelectableOff()<br>
|      C++: virtual void SelectableOff()<br>
|<br>
|  SelectableOn(…)<br>
|      V.SelectableOn()<br>
|      C++: virtual void SelectableOn()<br>
|<br>
|  SelectedOff(…)<br>
|      V.SelectedOff()<br>
|      C++: virtual void SelectedOff()<br>
|<br>
|  SelectedOn(…)<br>
|      V.SelectedOn()<br>
|      C++: virtual void SelectedOn()<br>
|<br>
|  SetAddToScene(…)<br>
|      V.SetAddToScene(int)<br>
|      C++: virtual void SetAddToScene(int _arg)<br>
|<br>
|  SetAddToSceneNoModify(…)<br>
|      V.SetAddToSceneNoModify(int)<br>
|      C++: void SetAddToSceneNoModify(int value)<br>
|<br>
|  SetAndObserveNodeReferenceID(…)<br>
|      V.SetAndObserveNodeReferenceID(string, string, vtkIntArray)<br>
|          → vtkMRMLNode<br>
|      C++: vtkMRMLNode *SetAndObserveNodeReferenceID(<br>
|          const char *referenceRole, const char *referencedNodeID,<br>
|          vtkIntArray *events=nullptr)<br>
|<br>
|      Set and observe a reference node from this node for a<br>
|          specificreferenceRole.<br>
|<br>
|      Observe Modified event by default, optionally takes array of<br>
|      events<br>
|<br>
|  SetAndObserveNthNodeReferenceID(…)<br>
|      V.SetAndObserveNthNodeReferenceID(string, int, string,<br>
|          vtkIntArray) → vtkMRMLNode<br>
|      C++: vtkMRMLNode *SetAndObserveNthNodeReferenceID(<br>
|          const char *referenceRole, int n,<br>
|          const char <em>referencedNodeID, vtkIntArray <em>events=nullptr)<br>
|<br>
|      Set and observe the Nth node ID for a specific reference role.<br>
|<br>
|      If n is larger than the number of reference nodes, the node ID is<br>
|      added at the end of the list. If nodeReferenceID is 0, the node<br>
|      ID is removed from the list. When a node ID is set (added or<br>
|      changed), its corresponding node is searched (slow) into the<br>
|      scene and cached for fast future access. It is possible however<br>
|      that the node is not yet into the scene (due to some temporary<br>
|      state (at loading time for example). UpdateScene() can later be<br>
|      called to retrieve the nodes from the scene (automatically done<br>
|      when loading a scene). Get(Nth)NodeReference() also scan the<br>
|      scene if the node was not yet cached.<br>
|      \sa SetAndObserveNodeReferenceID(const char</em>)<br>
|      \sa AddAndObserveNodeReferenceID(const char</em>)<br>
|      \sa RemoveNthNodeReferenceID(int)<br>
|<br>
|  SetAttribute(…)<br>
|      V.SetAttribute(string, string)<br>
|      C++: void SetAttribute(const char *name, const char *value)<br>
|<br>
|      Set a name value pair attribute.<br>
|<br>
|      Fires a vtkCommand::ModifiedEvent.<br>
|<br>
|      Attributes are written in the XML. If value is 0, the attribute<br>
|      name is removed from the pair list.<br>
|<br>
|      This function is a no-op if name is null or empty.<br>
|<br>
|      \sa WriteXML()<br>
|<br>
|  SetDescription(…)<br>
|      V.SetDescription(string)<br>
|      C++: virtual void SetDescription(const char *_arg)<br>
|<br>
|      Text description of this node, to be set by the user.<br>
|<br>
|  SetDisableModifiedEvent(…)<br>
|      V.SetDisableModifiedEvent(int)<br>
|      C++: void SetDisableModifiedEvent(int onOff)<br>
|<br>
|  SetHideFromEditors(…)<br>
|      V.SetHideFromEditors(int)<br>
|      C++: virtual void SetHideFromEditors(int _arg)<br>
|<br>
|  SetInMRMLCallbackFlag(…)<br>
|      V.SetInMRMLCallbackFlag(int)<br>
|      C++: void SetInMRMLCallbackFlag(int flag)<br>
|<br>
|  SetName(…)<br>
|      V.SetName(string)<br>
|      C++: virtual void SetName(const char *_arg)<br>
|<br>
|      Name of this node, to be set by the user<br>
|<br>
|  SetNodeReferenceID(…)<br>
|      V.SetNodeReferenceID(string, string) → vtkMRMLNode<br>
|      C++: vtkMRMLNode *SetNodeReferenceID(const char *referenceRole,<br>
|          const char *referencedNodeID)<br>
|<br>
|      Set a reference to a node with specified nodeID from this node<br>
|          for a specific referenceRole.<br>
|<br>
|  SetNthNodeReferenceID(…)<br>
|      V.SetNthNodeReferenceID(string, int, string) → vtkMRMLNode<br>
|      C++: vtkMRMLNode *SetNthNodeReferenceID(const char *referenceRole,<br>
|           int n, const char *referencedNodeID)<br>
|<br>
|      Set a N-th reference from this node with<br>
|          specifiedreferencedNodeID for a specific referenceRole.<br>
|<br>
|  SetSaveWithScene(…)<br>
|      V.SetSaveWithScene(int)<br>
|      C++: virtual void SetSaveWithScene(int _arg)<br>
|<br>
|  SetScene(…)<br>
|      V.SetScene(vtkMRMLScene)<br>
|      C++: virtual void SetScene(vtkMRMLScene *scene)<br>
|<br>
|      This method is for internal use only.<br>
|      Use AddNode method of vtkMRMLScene to add a node to the scene.<br>
|<br>
|      Internally calls SetSceneReferences()<br>
|      \sa SetSceneReferences()<br>
|<br>
|  SetSceneReferences(…)<br>
|      V.SetSceneReferences()<br>
|      C++: virtual void SetSceneReferences()<br>
|<br>
|      Update the references of the node to the scene.<br>
|<br>
|      ote You must unsure that a valid scene is set before calling<br>
|      SetSceneReferences().<br>
|<br>
|  SetSelectable(…)<br>
|      V.SetSelectable(int)<br>
|      C++: virtual void SetSelectable(int _arg)<br>
|<br>
|  SetSelected(…)<br>
|      V.SetSelected(int)<br>
|      C++: virtual void SetSelected(int _arg)<br>
|<br>
|  SetSingletonOff(…)<br>
|      V.SetSingletonOff()<br>
|      C++: void SetSingletonOff()<br>
|<br>
|  SetSingletonOn(…)<br>
|      V.SetSingletonOn()<br>
|      C++: void SetSingletonOn()<br>
|<br>
|  SetSingletonTag(…)<br>
|      V.SetSingletonTag(string)<br>
|      C++: virtual void SetSingletonTag(const char *_arg)<br>
|<br>
|      Tag that make this node a singleton in the scene.<br>
|<br>
|      If set to nullptr, multiple instances of this node class are<br>
|      allowed.<br>
|<br>
|      If set to a non-nullptr string, the node will be a singleton and<br>
|      the scene will replace this node instead of adding new instances.<br>
|<br>
|      The SingletonTag is used by the scene to build a unique ID.<br>
|<br>
|      If the there can only be one instance of a given node class in<br>
|      the scene, then the singleton tag should be Singleton. For<br>
|      example, the interaction and selection nodes are named Selection<br>
|      and Interaction, with Singleton tags set to Singleton, and with<br>
|      IDs set to vtkMRMLSelectionNodeSingleton and<br>
|      vtkMRMLInteractionNodeSingleton. If the singleton node is<br>
|      associated with a specific module it should use the module name,<br>
|      which already needs to be unique, as the tag. The Editor module<br>
|      uses this naming convention, with a parameter node that has a<br>
|      singleton tag of Editor and a node ID of<br>
|      vtkMRMLScriptedModuleNodeEditor. If the there is more than one<br>
|      instance of the node class then the singleton tag should be<br>
|      Singleton post-pended with a unique identifier for that specific<br>
|      node (e.g. the name). Any new color nodes should use this<br>
|      convention, with a name of NewName, a Singleton tag of<br>
|      SingletonNewName, leading to an ID of<br>
|      vtkMRMLColorTableNodeSingletonNewName. The existing MRML nodes<br>
|      don’t always use these conventions but are kept unchanged for<br>
|      backward compatibility.<br>
|      \sa vtkMRMLScene::BuildID<br>
|<br>
|  SetUndoEnabled(…)<br>
|      V.SetUndoEnabled(bool)<br>
|      C++: virtual void SetUndoEnabled(bool _arg)<br>
|<br>
|  StartModify(…)<br>
|      V.StartModify() → int<br>
|      C++: virtual int StartModify()<br>
|<br>
|      Start modifying the node. Disable Modify events.<br>
|<br>
|      Returns the previous state of DisableModifiedEvent flag that<br>
|      should be passed to EndModify() method.<br>
|<br>
|      \sa EndModify()<br>
|<br>
|  URLDecodeString(…)<br>
|      V.URLDecodeString(string) → string<br>
|      C++: const char *URLDecodeString(const char *inString)<br>
|<br>
|      Decode a URL string.<br>
|<br>
|      Returns the string (null) if the input is null.<br>
|<br>
|      ote Currently only works on %, space, ', ", &lt;, &gt;<br>
|      \sa URLEncodeString()<br>
|<br>
|  URLEncodeString(…)<br>
|      V.URLEncodeString(string) → string<br>
|      C++: const char *URLEncodeString(const char *inString)<br>
|<br>
|      Encode a URL string.<br>
|<br>
|      Returns the string (null) if the input is null.<br>
|<br>
|      ote Currently only works on %, space, ', ", &lt;, &gt;<br>
|      \sa URLDecodeString()<br>
|<br>
|  UndoEnabledOff(…)<br>
|      V.UndoEnabledOff()<br>
|      C++: virtual void UndoEnabledOff()<br>
|<br>
|  UndoEnabledOn(…)<br>
|      V.UndoEnabledOn()<br>
|      C++: virtual void UndoEnabledOn()<br>
|<br>
|  UpdateReferenceID(…)<br>
|      V.UpdateReferenceID(string, string)<br>
|      C++: virtual void UpdateReferenceID(const char *oldID,<br>
|          const char *newID)<br>
|<br>
|      Update the stored reference to another node in the scene.<br>
|<br>
|  UpdateReferences(…)<br>
|      V.UpdateReferences()<br>
|      C++: virtual void UpdateReferences()<br>
|<br>
|      The method should remove all pointers and observations to all<br>
|          nodes<br>
|      that are not in the scene anymore.<br>
|<br>
|      This method is called when one or more referenced nodes are<br>
|      deleted from the scene.<br>
|<br>
|  UpdateScene(…)<br>
|      V.UpdateScene(vtkMRMLScene)<br>
|      C++: virtual void UpdateScene(vtkMRMLScene *)<br>
|<br>
|      Updates other nodes in the scene depending on this node or<br>
|      updates this node if it depends on other nodes when the scene is<br>
|      read in This method is called automatically by XML parser after<br>
|      all nodes are created<br>
|<br>
|  XMLAttributeDecodeString(…)<br>
|      V.XMLAttributeDecodeString(string) → string<br>
|      C++: std::string XMLAttributeDecodeString(<br>
|          const std::string &amp;inString)<br>
|<br>
|      Decode an XML attribute string.<br>
|<br>
|      Important: attributes that vtkMRMLNode::ReadXMLAttributes method<br>
|      receives are already decoded, therefore no XML attribute decoding<br>
|      must not be applied to those strings.<br>
|<br>
|      \sa XMLAttributeEncodeString()<br>
|<br>
|  XMLAttributeEncodeString(…)<br>
|      V.XMLAttributeEncodeString(string) → string<br>
|      C++: std::string XMLAttributeEncodeString(<br>
|          const std::string &amp;inString)<br>
|<br>
|      Encode an XML attribute string (replaces special characters by<br>
|          code sequences)<br>
|<br>
|      \sa XMLAttributeDecodeString()<br>
|<br>
|  ----------------------------------------------------------------------<br>
|  Data and other attributes inherited from MRMLCorePython.vtkMRMLNode:<br>
|<br>
|  HierarchyModifiedEvent = 16000<br>
|<br>
|  IDChangedEvent = 16001<br>
|<br>
|  ReferenceAddedEvent = 16002<br>
|<br>
|  ReferenceModifiedEvent = 16003<br>
|<br>
|  ReferenceRemovedEvent = 16004<br>
|<br>
|  ReferencedNodeModifiedEvent = 16005<br>
|<br>
|  ----------------------------------------------------------------------<br>
|  Methods inherited from vtkCommonCorePython.vtkObject:<br>
|<br>
|  AddObserver(…)<br>
|      V.AddObserver(int, function) → int<br>
|      C++: unsigned long AddObserver(const char *event,<br>
|          vtkCommand *command, float priority=0.0f)<br>
|<br>
|      Add an event callback function(vtkObject, int) for an event type.<br>
|      Returns a handle that can be used with RemoveEvent(int).<br>
|<br>
|  BreakOnError(…)<br>
|      V.BreakOnError()<br>
|      C++: static void BreakOnError()<br>
|<br>
|      This method is called when vtkErrorMacro executes. It allows the<br>
|      debugger to break on error.<br>
|<br>
|  DebugOff(…)<br>
|      V.DebugOff()<br>
|      C++: virtual void DebugOff()<br>
|<br>
|      Turn debugging output off.<br>
|<br>
|  DebugOn(…)<br>
|      V.DebugOn()<br>
|      C++: virtual void DebugOn()<br>
|<br>
|      Turn debugging output on.<br>
|<br>
|  GetCommand(…)<br>
|      V.GetCommand(int) → vtkCommand<br>
|      C++: vtkCommand *GetCommand(unsigned long tag)<br>
|<br>
|      Allow people to add/remove/invoke observers (callbacks) to any<br>
|      VTK object.  This is an implementation of the subject/observer<br>
|      design pattern. An observer is added by specifying an event to<br>
|      respond to and a vtkCommand to execute. It returns an unsigned<br>
|      long tag which can be used later to remove the event or retrieve<br>
|      the command. When events are invoked, the observers are called in<br>
|      the order they were added. If a priority value is specified, then<br>
|      the higher priority commands are called first. A command may set<br>
|      an abort flag to stop processing of the event. (See vtkCommand.h<br>
|      for more information.)<br>
|<br>
|  GetDebug(…)<br>
|      V.GetDebug() → bool<br>
|      C++: bool GetDebug()<br>
|<br>
|      Get the value of the debug flag.<br>
|<br>
|  GetGlobalWarningDisplay(…)<br>
|      V.GetGlobalWarningDisplay() → int<br>
|      C++: static int GetGlobalWarningDisplay()<br>
|<br>
|      This is a global flag that controls whether any debug, warning or<br>
|      error messages are displayed.<br>
|<br>
|  GetMTime(…)<br>
|      V.GetMTime() → int<br>
|      C++: virtual vtkMTimeType GetMTime()<br>
|<br>
|      Return this object’s modified time.<br>
|<br>
|  GlobalWarningDisplayOff(…)<br>
|      V.GlobalWarningDisplayOff()<br>
|      C++: static void GlobalWarningDisplayOff()<br>
|<br>
|      This is a global flag that controls whether any debug, warning or<br>
|      error messages are displayed.<br>
|<br>
|  GlobalWarningDisplayOn(…)<br>
|      V.GlobalWarningDisplayOn()<br>
|      C++: static void GlobalWarningDisplayOn()<br>
|<br>
|      This is a global flag that controls whether any debug, warning or<br>
|      error messages are displayed.<br>
|<br>
|  HasObserver(…)<br>
|      V.HasObserver(int, vtkCommand) → int<br>
|      C++: vtkTypeBool HasObserver(unsigned long event, vtkCommand *)<br>
|      V.HasObserver(string, vtkCommand) → int<br>
|      C++: vtkTypeBool HasObserver(const char *event, vtkCommand *)<br>
|      V.HasObserver(int) → int<br>
|      C++: vtkTypeBool HasObserver(unsigned long event)<br>
|      V.HasObserver(string) → int<br>
|      C++: vtkTypeBool HasObserver(const char *event)<br>
|<br>
|      Allow people to add/remove/invoke observers (callbacks) to any<br>
|      VTK object.  This is an implementation of the subject/observer<br>
|      design pattern. An observer is added by specifying an event to<br>
|      respond to and a vtkCommand to execute. It returns an unsigned<br>
|      long tag which can be used later to remove the event or retrieve<br>
|      the command. When events are invoked, the observers are called in<br>
|      the order they were added. If a priority value is specified, then<br>
|      the higher priority commands are called first. A command may set<br>
|      an abort flag to stop processing of the event. (See vtkCommand.h<br>
|      for more information.)<br>
|<br>
|  InvokeEvent(…)<br>
|      V.InvokeEvent(int, void) → int<br>
|      C++: int InvokeEvent(unsigned long event, void *callData)<br>
|      V.InvokeEvent(string, void) → int<br>
|      C++: int InvokeEvent(const char *event, void *callData)<br>
|      V.InvokeEvent(int) → int<br>
|      C++: int InvokeEvent(unsigned long event)<br>
|      V.InvokeEvent(string) → int<br>
|      C++: int InvokeEvent(const char *event)<br>
|<br>
|      This method invokes an event and return whether the event was<br>
|      aborted or not. If the event was aborted, the return value is 1,<br>
|      otherwise it is 0.<br>
|<br>
|  RemoveAllObservers(…)<br>
|      V.RemoveAllObservers()<br>
|      C++: void RemoveAllObservers()<br>
|<br>
|  RemoveObserver(…)<br>
|      V.RemoveObserver(vtkCommand)<br>
|      C++: void RemoveObserver(vtkCommand *)<br>
|      V.RemoveObserver(int)<br>
|      C++: void RemoveObserver(unsigned long tag)<br>
|<br>
|      Allow people to add/remove/invoke observers (callbacks) to any<br>
|      VTK object.  This is an implementation of the subject/observer<br>
|      design pattern. An observer is added by specifying an event to<br>
|      respond to and a vtkCommand to execute. It returns an unsigned<br>
|      long tag which can be used later to remove the event or retrieve<br>
|      the command. When events are invoked, the observers are called in<br>
|      the order they were added. If a priority value is specified, then<br>
|      the higher priority commands are called first. A command may set<br>
|      an abort flag to stop processing of the event. (See vtkCommand.h<br>
|      for more information.)<br>
|<br>
|  RemoveObservers(…)<br>
|      V.RemoveObservers(int, vtkCommand)<br>
|      C++: void RemoveObservers(unsigned long event, vtkCommand *)<br>
|      V.RemoveObservers(string, vtkCommand)<br>
|      C++: void RemoveObservers(const char *event, vtkCommand *)<br>
|      V.RemoveObservers(int)<br>
|      C++: void RemoveObservers(unsigned long event)<br>
|      V.RemoveObservers(string)<br>
|      C++: void RemoveObservers(const char *event)<br>
|<br>
|      Allow people to add/remove/invoke observers (callbacks) to any<br>
|      VTK object.  This is an implementation of the subject/observer<br>
|      design pattern. An observer is added by specifying an event to<br>
|      respond to and a vtkCommand to execute. It returns an unsigned<br>
|      long tag which can be used later to remove the event or retrieve<br>
|      the command. When events are invoked, the observers are called in<br>
|      the order they were added. If a priority value is specified, then<br>
|      the higher priority commands are called first. A command may set<br>
|      an abort flag to stop processing of the event. (See vtkCommand.h<br>
|      for more information.)<br>
|<br>
|  SetDebug(…)<br>
|      V.SetDebug(bool)<br>
|      C++: void SetDebug(bool debugFlag)<br>
|<br>
|      Set the value of the debug flag. A true value turns debugging on.<br>
|<br>
|  SetGlobalWarningDisplay(…)<br>
|      V.SetGlobalWarningDisplay(int)<br>
|      C++: static void SetGlobalWarningDisplay(int val)<br>
|<br>
|      This is a global flag that controls whether any debug, warning or<br>
|      error messages are displayed.<br>
|<br>
|  ----------------------------------------------------------------------<br>
|  Methods inherited from vtkCommonCorePython.vtkObjectBase:<br>
|<br>
|  FastDelete(…)<br>
|      V.FastDelete()<br>
|      C++: virtual void FastDelete()<br>
|<br>
|      Delete a reference to this object.  This version will not invoke<br>
|      garbage collection and can potentially leak the object if it is<br>
|      part of a reference loop.  Use this method only when it is known<br>
|      that the object has another reference and would not be collected<br>
|      if a full garbage collection check were done.<br>
|<br>
|  GetAddressAsString(…)<br>
|      V.GetAddressAsString(string) → string<br>
|      C++: const char *GetAddressAsString()<br>
|<br>
|      Get address of C++ object in format ‘Addr=%p’ after casting to<br>
|      the specified type.  You can get the same information from o.<strong>this</strong>.<br>
|<br>
|  GetClassName(…)<br>
|      V.GetClassName() → string<br>
|      C++: const char *GetClassName()<br>
|<br>
|      Return the class name as a string.<br>
|<br>
|  GetReferenceCount(…)<br>
|      V.GetReferenceCount() → int<br>
|      C++: int GetReferenceCount()<br>
|<br>
|      Return the current reference count of this object.<br>
|<br>
|  InitializeObjectBase(…)<br>
|      V.InitializeObjectBase()<br>
|      C++: void InitializeObjectBase()<br>
|<br>
|  Register(…)<br>
|      V.Register(vtkObjectBase)<br>
|      C++: virtual void Register(vtkObjectBase *o)<br>
|<br>
|      Increase the reference count by 1.<br>
|<br>
|  SetReferenceCount(…)<br>
|      V.SetReferenceCount(int)<br>
|      C++: void SetReferenceCount(int)<br>
|<br>
|      Sets the reference count. (This is very dangerous, use with<br>
|      care.)<br>
|<br>
|  UnRegister(…)<br>
|      V.UnRegister(vtkObjectBase)<br>
|      C++: virtual void UnRegister(vtkObjectBase *o)<br>
|<br>
|      Decrease the reference count (release by another object). This<br>
|      has the same effect as invoking Delete() (i.e., it reduces the<br>
|      reference count by</p>
<pre><code class="lang-auto"></code></pre>
</details>

---

## Post #6 by @lassoan (2023-06-23 03:58 UTC)

<p>This looks good, your can now search for <code>Dice</code> in this output to find the relevant methods.</p>

---

## Post #7 by @Melanie (2023-06-23 04:21 UTC)

<aside class="quote no-group" data-username="Melanie" data-post="5" data-topic="18726">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/35a633/48.png" class="avatar"> Melanie:</div>
<blockquote>
<p>class vtkMRMLSegmentComparisonNode(MRMLCorePython.vtkMRMLNode)<br>
| vtkMRMLSegmentComparisonNode - \ingroup<br>
| SlicerRt_QtModules_SegmentComparison<br>
|<br>
| Superclass: vtkMRMLNode<br>
|<br>
| Method resolution order:<br>
| vtkMRMLSegmentComparisonNode<br>
| MRMLCorePython.vtkMRMLNode<br>
| vtkCommonCorePython.vtkObject<br>
| vtkCommonCorePython.vtkObjectBase<br>
| builtins.object<br>
|<br>
| Methods defined here:<br>
|<br>
| Copy(…)<br>
| V.Copy(vtkMRMLNode)<br>
| C++: void Copy(vtkMRMLNode *node) override;<br>
|<br>
| Copy the node’s attributes to this object<br>
|<br>
| CreateNodeInstance(…)<br>
| V.CreateNodeInstance() → vtkMRMLNode<br>
| C++: vtkMRMLNode *CreateNodeInstance() override;<br>
|<br>
| Create instance of a GAD node.<br>
|<br>
| DiceResultsValidOff(…)<br>
| V.DiceResultsValidOff()<br>
| C++: virtual void DiceResultsValidOff()<br>
|<br>
| DiceResultsValidOn(…)<br>
| V.DiceResultsValidOn()<br>
| C++: virtual void DiceResultsValidOn()<br>
|<br>
| GetAverageHausdorffDistanceForBoundaryMm(…)<br>
| V.GetAverageHausdorffDistanceForBoundaryMm() → float<br>
| C++: virtual double GetAverageHausdorffDistanceForBoundaryMm()<br>
|<br>
| Get average Hausdorff distance for the boundary voxels<br>
|<br>
| GetAverageHausdorffDistanceForVolumeMm(…)<br>
| V.GetAverageHausdorffDistanceForVolumeMm() → float<br>
| C++: virtual double GetAverageHausdorffDistanceForVolumeMm()<br>
|<br>
| Get average Hausdorff distance for the whole volume<br>
|<br>
| GetCompareCenter(…)<br>
| V.GetCompareCenter() → (float, float, float)<br>
| C++: double *GetCompareCenter()<br>
|<br>
| GetCompareSegmentID(…)<br>
| V.GetCompareSegmentID() → string<br>
| C++: virtual char *GetCompareSegmentID()<br>
|<br>
| Get compare segment ID<br>
|<br>
| GetCompareSegmentationNode(…)<br>
| V.GetCompareSegmentationNode() → vtkMRMLSegmentationNode<br>
| C++: vtkMRMLSegmentationNode *GetCompareSegmentationNode()<br>
|<br>
| Get compare segmentation node<br>
|<br>
| GetCompareVolumeCc(…)<br>
| V.GetCompareVolumeCc() → float<br>
| C++: virtual double GetCompareVolumeCc()<br>
|<br>
| Get volume of the compare structure<br>
|<br>
| GetDiceCoefficient(…)<br>
| V.GetDiceCoefficient() → float<br>
| C++: virtual float GetDiceCoefficient()<br>
|<br>
| Get result dice coefficient<br>
|<br>
| GetDiceResultsValid(…)<br>
| V.GetDiceResultsValid() → bool<br>
| C++: virtual bool GetDiceResultsValid()<br>
|<br>
| Get/Set Dice results valid flag<br>
|<br>
| GetDiceTableNode(…)<br>
| V.GetDiceTableNode() → vtkMRMLTableNode<br>
| C++: vtkMRMLTableNode *GetDiceTableNode()<br>
|<br>
| Get Dice table node<br>
|<br>
| GetFalseNegativesPercent(…)<br>
| V.GetFalseNegativesPercent() → float<br>
| C++: virtual double GetFalseNegativesPercent()<br>
|<br>
| Get percentage of false negative labelmap voxels<br>
|<br>
| GetFalsePositivesPercent(…)<br>
| V.GetFalsePositivesPercent() → float<br>
| C++: virtual double GetFalsePositivesPercent()<br>
|<br>
| Get percentage of false positive labelmap voxels<br>
|<br>
| GetHausdorffResultsValid(…)<br>
| V.GetHausdorffResultsValid() → bool<br>
| C++: virtual bool GetHausdorffResultsValid()<br>
|<br>
| Get/Set results Hausdorff valid flag<br>
|<br>
| GetHausdorffTableNode(…)<br>
| V.GetHausdorffTableNode() → vtkMRMLTableNode<br>
| C++: vtkMRMLTableNode *GetHausdorffTableNode()<br>
|<br>
| Get Hausdorff table node<br>
|<br>
| GetMaximumHausdorffDistanceForBoundaryMm(…)<br>
| V.GetMaximumHausdorffDistanceForBoundaryMm() → float<br>
| C++: virtual double GetMaximumHausdorffDistanceForBoundaryMm()<br>
|<br>
| Get maximum Hausdorff distance for the boundary voxels<br>
|<br>
| GetMaximumHausdorffDistanceForVolumeMm(…)<br>
| V.GetMaximumHausdorffDistanceForVolumeMm() → float<br>
| C++: virtual double GetMaximumHausdorffDistanceForVolumeMm()<br>
|<br>
| Get maximum Hausdorff distance for the whole volume<br>
|<br>
| GetNodeTagName(…)<br>
| V.GetNodeTagName() → string<br>
| C++: const char *GetNodeTagName() override;<br>
|<br>
| Get unique node XML tag name (like Volume, Model)<br>
|<br>
| GetPercent95HausdorffDistanceForBoundaryMm(…)<br>
| V.GetPercent95HausdorffDistanceForBoundaryMm() → float<br>
| C++: virtual double GetPercent95HausdorffDistanceForBoundaryMm()<br>
|<br>
| Get 95% Hausdorff distance for the boundary voxels<br>
|<br>
| GetPercent95HausdorffDistanceForVolumeMm(…)<br>
| V.GetPercent95HausdorffDistanceForVolumeMm() → float<br>
| C++: virtual double GetPercent95HausdorffDistanceForVolumeMm()<br>
|<br>
| Get 95% Hausdorff distance for whole volume<br>
|<br>
| GetRasterizationReferenceVolumeNode(…)<br>
| V.GetRasterizationReferenceVolumeNode() → vtkMRMLScalarVolumeNode<br>
| C++: vtkMRMLScalarVolumeNode *GetRasterizationReferenceVolumeNode(<br>
| )<br>
|<br>
| Get rasterization reference volume node<br>
|<br>
| GetReferenceCenter(…)<br>
| V.GetReferenceCenter() → (float, float, float)<br>
| C++: double *GetReferenceCenter()<br>
|<br>
| GetReferenceSegmentID(…)<br>
| V.GetReferenceSegmentID() → string<br>
| C++: virtual char *GetReferenceSegmentID()<br>
|<br>
| Get reference segment ID<br>
|<br>
| GetReferenceSegmentationNode(…)<br>
| V.GetReferenceSegmentationNode() → vtkMRMLSegmentationNode<br>
| C++: vtkMRMLSegmentationNode *GetReferenceSegmentationNode()<br>
|<br>
| Get reference segmentation node<br>
|<br>
| GetReferenceVolumeCc(…)<br>
| V.GetReferenceVolumeCc() → float<br>
| C++: virtual double GetReferenceVolumeCc()<br>
|<br>
| Get volume of the reference structure<br>
|<br>
| GetTrueNegativesPercent(…)<br>
| V.GetTrueNegativesPercent() → float<br>
| C++: virtual double GetTrueNegativesPercent()<br>
|<br>
| Get percentage of true negative labelmap voxels<br>
|<br>
| GetTruePositivesPercent(…)<br>
| V.GetTruePositivesPercent() → float<br>
| C++: virtual double GetTruePositivesPercent()<br>
|<br>
| Get percentage of true positive labelmap voxels<br>
|<br>
| HausdorffResultsValidOff(…)<br>
| V.HausdorffResultsValidOff()<br>
| C++: virtual void HausdorffResultsValidOff()<br>
|<br>
| HausdorffResultsValidOn(…)<br>
| V.HausdorffResultsValidOn()<br>
| C++: virtual void HausdorffResultsValidOn()<br>
|<br>
| IsA(…)<br>
| V.IsA(string) → int<br>
| C++: vtkTypeBool IsA(const char *type) override;<br>
|<br>
| Return 1 if this class is the same type of (or a subclass of) the<br>
| named class. Returns 0 otherwise. This method works in<br>
| combination with vtkTypeMacro found in vtkSetGet.h.<br>
|<br>
| IsTypeOf(…)<br>
| V.IsTypeOf(string) → int<br>
| C++: static vtkTypeBool IsTypeOf(const char *type)<br>
|<br>
| Return 1 if this class type is the same type of (or a subclass<br>
| of) the named class. Returns 0 otherwise. This method works in<br>
| combination with vtkTypeMacro found in vtkSetGet.h.<br>
|<br>
| NewInstance(…)<br>
| V.NewInstance() → vtkMRMLSegmentComparisonNode<br>
| C++: vtkMRMLSegmentComparisonNode *NewInstance()<br>
|<br>
| SafeDownCast(…)<br>
| V.SafeDownCast(vtkObjectBase) → vtkMRMLSegmentComparisonNode<br>
| C++: static vtkMRMLSegmentComparisonNode *SafeDownCast(<br>
| vtkObjectBase *o)<br>
|<br>
| SetAndObserveCompareSegmentationNode(…)<br>
| V.SetAndObserveCompareSegmentationNode(vtkMRMLSegmentationNode)<br>
| C++: void SetAndObserveCompareSegmentationNode(<br>
| vtkMRMLSegmentationNode *node)<br>
|<br>
| Set compare segmentation node<br>
|<br>
| SetAndObserveDiceTableNode(…)<br>
| V.SetAndObserveDiceTableNode(vtkMRMLTableNode)<br>
| C++: void SetAndObserveDiceTableNode(vtkMRMLTableNode *node)<br>
|<br>
| Set Dice table node<br>
|<br>
| SetAndObserveHausdorffTableNode(…)<br>
| V.SetAndObserveHausdorffTableNode(vtkMRMLTableNode)<br>
| C++: void SetAndObserveHausdorffTableNode(vtkMRMLTableNode *node)<br>
|<br>
| Set Hausdorff table node<br>
|<br>
| SetAndObserveRasterizationReferenceVolumeNode(…)<br>
| V.SetAndObserveRasterizationReferenceVolumeNode(<br>
| vtkMRMLScalarVolumeNode)<br>
| C++: void SetAndObserveRasterizationReferenceVolumeNode(<br>
| vtkMRMLScalarVolumeNode *node)<br>
|<br>
| Set rasterization reference volume node<br>
|<br>
| SetAndObserveReferenceSegmentationNode(…)<br>
| V.SetAndObserveReferenceSegmentationNode(vtkMRMLSegmentationNode)<br>
| C++: void SetAndObserveReferenceSegmentationNode(<br>
| vtkMRMLSegmentationNode *node)<br>
|<br>
| Set reference segmentation node<br>
|<br>
| SetAverageHausdorffDistanceForBoundaryMm(…)<br>
| V.SetAverageHausdorffDistanceForBoundaryMm(float)<br>
| C++: virtual void SetAverageHausdorffDistanceForBoundaryMm(<br>
| double _arg)<br>
|<br>
| Set average Hausdorff distance for the boundary voxels<br>
|<br>
| SetAverageHausdorffDistanceForVolumeMm(…)<br>
| V.SetAverageHausdorffDistanceForVolumeMm(float)<br>
| C++: virtual void SetAverageHausdorffDistanceForVolumeMm(<br>
| double _arg)<br>
|<br>
| Set average Hausdorff distance for the whole volume<br>
|<br>
| SetCompareCenter(…)<br>
| V.SetCompareCenter(float, float, float)<br>
| C++: void SetCompareCenter(double, double, double)<br>
| V.SetCompareCenter((float, float, float))<br>
| C++: void SetCompareCenter(double a[3])<br>
|<br>
| SetCompareSegmentID(…)<br>
| V.SetCompareSegmentID(string)<br>
| C++: virtual void SetCompareSegmentID(const char *_arg)<br>
|<br>
| Set compare segment ID<br>
|<br>
| SetCompareVolumeCc(…)<br>
| V.SetCompareVolumeCc(float)<br>
| C++: virtual void SetCompareVolumeCc(double _arg)<br>
|<br>
| Set volume of the compare structure<br>
|<br>
| SetDiceCoefficient(…)<br>
| V.SetDiceCoefficient(float)<br>
| C++: virtual void SetDiceCoefficient(float _arg)<br>
|<br>
| Set result dice coefficient<br>
|<br>
| SetDiceResultsValid(…)<br>
| V.SetDiceResultsValid(bool)<br>
| C++: virtual void SetDiceResultsValid(bool _arg)<br>
|<br>
| SetFalseNegativesPercent(…)<br>
| V.SetFalseNegativesPercent(float)<br>
| C++: virtual void SetFalseNegativesPercent(double _arg)<br>
|<br>
| Set percentage of false negative labelmap voxels<br>
|<br>
| SetFalsePositivesPercent(…)<br>
| V.SetFalsePositivesPercent(float)<br>
| C++: virtual void SetFalsePositivesPercent(double _arg)<br>
|<br>
| Set percentage of false positive labelmap voxels<br>
|<br>
| SetHausdorffResultsValid(…)<br>
| V.SetHausdorffResultsValid(bool)<br>
| C++: virtual void SetHausdorffResultsValid(bool _arg)<br>
|<br>
| SetMaximumHausdorffDistanceForBoundaryMm(…)<br>
| V.SetMaximumHausdorffDistanceForBoundaryMm(float)<br>
| C++: virtual void SetMaximumHausdorffDistanceForBoundaryMm(<br>
| double _arg)<br>
|<br>
| Set maximum Hausdorff distance for the boundary voxels<br>
|<br>
| SetMaximumHausdorffDistanceForVolumeMm(…)<br>
| V.SetMaximumHausdorffDistanceForVolumeMm(float)<br>
| C++: virtual void SetMaximumHausdorffDistanceForVolumeMm(<br>
| double _arg)<br>
|<br>
| Set maximum Hausdorff distance for the whole volume<br>
|<br>
| SetPercent95HausdorffDistanceForBoundaryMm(…)<br>
| V.SetPercent95HausdorffDistanceForBoundaryMm(float)<br>
| C++: virtual void SetPercent95HausdorffDistanceForBoundaryMm(<br>
| double _arg)<br>
|<br>
| Set 95% Hausdorff distance for the boundary voxels<br>
|<br>
| SetPercent95HausdorffDistanceForVolumeMm(…)<br>
| V.SetPercent95HausdorffDistanceForVolumeMm(float)<br>
| C++: virtual void SetPercent95HausdorffDistanceForVolumeMm(<br>
| double _arg)<br>
|<br>
| Set 95% Hausdorff distance for whole volume<br>
|<br>
| SetReferenceCenter(…)<br>
| V.SetReferenceCenter(float, float, float)<br>
| C++: void SetReferenceCenter(double, double, double)<br>
| V.SetReferenceCenter((float, float, float))<br>
| C++: void SetReferenceCenter(double a[3])<br>
|<br>
| SetReferenceSegmentID(…)<br>
| V.SetReferenceSegmentID(string)<br>
| C++: virtual void SetReferenceSegmentID(const char *_arg)<br>
|<br>
| Set reference segment ID<br>
|<br>
| SetReferenceVolumeCc(…)<br>
| V.SetReferenceVolumeCc(float)<br>
| C++: virtual void SetReferenceVolumeCc(double _arg)<br>
|<br>
| Set volume of the reference structure<br>
|<br>
| SetTrueNegativesPercent(…)<br>
| V.SetTrueNegativesPercent(float)<br>
| C++: virtual void SetTrueNegativesPercent(double _arg)<br>
|<br>
| Set percentage of true negative labelmap voxels<br>
|<br>
| SetTruePositivesPercent(…)<br>
| V.SetTruePositivesPercent(float)<br>
| C++: virtual void SetTruePositivesPercent(double _arg)<br>
|<br>
| Set percentage of true positive labelmap voxels<br>
|<br>
| <strong>delattr</strong>(self, name, /)<br>
| Implement delattr(self, name).<br>
|<br>
| <strong>getattribute</strong>(self, name, /)<br>
| Return getattr(self, name).<br>
|<br>
| <strong>new</strong>(*args, **kwargs) from builtins.type<br>
| Create and return a new object. See help(type) for accurate signature.<br>
|<br>
| <strong>repr</strong>(self, /)<br>
| Return repr(self).<br>
|<br>
| <strong>setattr</strong>(self, name, value, /)<br>
| Implement setattr(self, name, value).<br>
|<br>
| <strong>str</strong>(self, /)<br>
| Return str(self).<br>
|<br>
| ----------------------------------------------------------------------<br>
| Data descriptors defined here:<br>
|<br>
| <strong>dict</strong><br>
| Dictionary of attributes set by user.<br>
|<br>
| <strong>this</strong><br>
| Pointer to the C++ object.<br>
|<br>
| ----------------------------------------------------------------------<br>
| Data and other attributes defined here:<br>
|<br>
| <strong>vtkname</strong> = ‘vtkMRMLSegmentComparisonNode’<br>
|<br>
| ----------------------------------------------------------------------<br>
| Methods inherited from MRMLCorePython.vtkMRMLNode:<br>
|<br>
| AddAndObserveNodeReferenceID(…)<br>
| V.AddAndObserveNodeReferenceID(string, string, vtkIntArray)<br>
| → vtkMRMLNode<br>
| C++: vtkMRMLNode *AddAndObserveNodeReferenceID(<br>
| const char *referenceRole, const char *referencedNodeID,<br>
| vtkIntArray *events=nullptr)<br>
|<br>
| Add and observe a reference node from this node for a<br>
| specificreferenceRole.<br>
|<br>
| Observe Modified event by default, optionally takes array of<br>
| events.<br>
|<br>
| AddNodeReferenceID(…)<br>
| V.AddNodeReferenceID(string, string) → vtkMRMLNode<br>
| C++: vtkMRMLNode *AddNodeReferenceID(const char *referenceRole,<br>
| const char *referencedNodeID)<br>
|<br>
| Convenience method that adds a referencedNodeID at the end of the<br>
| list.<br>
|<br>
| AddNodeReferenceRole(…)<br>
| V.AddNodeReferenceRole(string, string, vtkIntArray)<br>
| C++: void AddNodeReferenceRole(const char *referenceRole,<br>
| const char <em>mrmlAttributeName=nullptr,<br>
| vtkIntArray <em>events=nullptr)<br>
|<br>
| Add a referenceRole.<br>
|<br>
| The referenceRole can be any unique string, for example<br>
| “display”, “transform” etc. Optionally a MRML attribute name for<br>
| storing the reference in the mrml scene file can be specified.<br>
| For example “displayNodeRef”. If omitted the MRML attribute name<br>
| will be the same as the role. If referenceRole ends with ‘/’, it<br>
| is considered as a “template” reference role that can be used to<br>
| generate attribute names dynamically by concatenation: If<br>
| referenceRole is “unit/” and mrmlAttributeName is “UnitRef”, then<br>
| the generated MRML attribute names for a node reference role of<br>
| “unit/length” will be “lengthUnitRef”. Use this method to add new<br>
| reference types to a node. This method is typically called in the<br>
| constructors of each subclass. The optional events argument<br>
| specifies what events should be observed by default (e.g., when<br>
| loading the scene from file). If referenceRole ends with ‘/’<br>
| character then events are used for all roles names begins with<br>
| this role name (for example, events specified for<br>
| referenceRole=‘unit/’ will be used for<br>
| referenceRole=‘unit/length’, referenceRole=‘unit/area’, etc).<br>
| \sa GetReferenceNodeFromMRMLAttributeName()<br>
|<br>
| AddToSceneOff(…)<br>
| V.AddToSceneOff()<br>
| C++: virtual void AddToSceneOff()<br>
|<br>
| AddToSceneOn(…)<br>
| V.AddToSceneOn()<br>
| C++: virtual void AddToSceneOn()<br>
|<br>
| CopyContent(…)<br>
| V.CopyContent(vtkMRMLNode, bool)<br>
| C++: virtual void CopyContent(vtkMRMLNode <em>node,<br>
| bool deepCopy=true)<br>
|<br>
| Copy node contents from another node of the same type.<br>
| Does not copy node ID, Scene, Name, SingletonTag,<br>
| HideFromEditors, AddToScene, UndoEnabled, and node references. If<br>
| deepCopy is set to false then a shallow copy of bulk data (such<br>
| as image or mesh data) could be made; copying may be faster but<br>
| the node may share some data with the source node instead of<br>
| creating an independent copy.<br>
|<br>
| ote If a class implements this then make sure CopyContent and<br>
| HasCopyContent methods are implemented in all parent classes by<br>
| adding vtkMRMLCopyContentMacro(ClassName) to the class headers.<br>
|<br>
| CopyReferences(…)<br>
| V.CopyReferences(vtkMRMLNode)<br>
| C++: virtual void CopyReferences(vtkMRMLNode <em>node)<br>
|<br>
| Copy the references of the node into this.<br>
|<br>
| Existing references will be replaced if found in node, or removed<br>
| if not in node.<br>
|<br>
| CopyWithScene(…)<br>
| V.CopyWithScene(vtkMRMLNode)<br>
| C++: void CopyWithScene(vtkMRMLNode <em>node)<br>
|<br>
| Copy everything (including Scene and ID) from another node of<br>
| the same type.<br>
|<br>
| ote The node is <strong>not</strong> added into the scene of node. You must do<br>
| it manually <strong>after</strong> calling CopyWithScene(vtkMRMLNode</em>) using<br>
| vtkMRMLScene::AddNode(vtkMRMLNode</em>). Only one<br>
| vtkCommand::ModifiedEvent is invoked, after the copy is fully<br>
| completed.<br>
|<br>
| \bug Calling vtkMRMLScene::AddNode(vtkMRMLNode</em>) <strong>before</strong><br>
| CopyWithScene(vtkMRMLNode</em>) is <strong>NOT</strong> supported, it will<br>
| unsynchronize the node internal caches. See<br>
| <a href="https://github.com/Slicer/Slicer/issues/4078" rel="noopener nofollow ugc">#4078</a><br>
|<br>
| \sa vtkMRMLScene::AddNode(vtkMRMLNode</em>)<br>
|<br>
| DisableModifiedEventOff(…)<br>
| V.DisableModifiedEventOff()<br>
| C++: void DisableModifiedEventOff()<br>
|<br>
| DisableModifiedEventOn(…)<br>
| V.DisableModifiedEventOn()<br>
| C++: void DisableModifiedEventOn()<br>
|<br>
| EndModify(…)<br>
| V.EndModify(int) → int<br>
| C++: virtual int EndModify(int previousDisableModifiedEventState)<br>
|<br>
| End modifying the node.<br>
|<br>
| Enable Modify events if the previous state ofDisableModifiedEvent<br>
| flag is 0.<br>
|<br>
| Return the number of pending events (even if<br>
| InvokePendingModifiedEvent() is not called).<br>
|<br>
| GetAddToScene(…)<br>
| V.GetAddToScene() → int<br>
| C++: virtual int GetAddToScene()<br>
|<br>
| node added to MRML scene.<br>
|<br>
| GetAttribute(…)<br>
| V.GetAttribute(string) → string<br>
| C++: const char *GetAttribute(const char *name)<br>
|<br>
| Get value of a name value pair attribute.<br>
|<br>
| Return nullptr if the name does not exists.<br>
|<br>
| GetAttributeNames(…)<br>
| V.GetAttributeNames() → Stvector_ISt6stringE<br>
| C++: std::vectorstd::string GetAttributeNames()<br>
| V.GetAttributeNames(vtkStringArray)<br>
| C++: void GetAttributeNames(vtkStringArray *attributeNames)<br>
|<br>
| Get all attribute names.<br>
|<br>
| GetContentModifiedEvents(…)<br>
| V.GetContentModifiedEvents() → vtkIntArray<br>
| C++: virtual vtkIntArray *GetContentModifiedEvents()<br>
|<br>
| Return list of events that indicate that content of the node is<br>
| modified. For example, it is not enough to observe<br>
| vtkCommand::ModifiedEvent to get notified when a transform stored<br>
| in a transform node is modified, but<br>
| vtkMRMLTransformableNode::TransformModifiedEvent must be observed<br>
| as well.<br>
|<br>
| GetDescription(…)<br>
| V.GetDescription() → string<br>
| C++: virtual char *GetDescription()<br>
|<br>
| GetDisableModifiedEvent(…)<br>
| V.GetDisableModifiedEvent() → int<br>
| C++: virtual int GetDisableModifiedEvent()<br>
|<br>
| Turn on/off generating InvokeEvent for set macros<br>
|<br>
| GetHideFromEditors(…)<br>
| V.GetHideFromEditors() → int<br>
| C++: virtual int GetHideFromEditors()<br>
|<br>
| Describes if the node is hidden.<br>
|<br>
| GetID(…)<br>
| V.GetID() → string<br>
| C++: virtual char *GetID()<br>
|<br>
| ID use by other nodes to reference this node in XML.<br>
|<br>
| GetInMRMLCallbackFlag(…)<br>
| V.GetInMRMLCallbackFlag() → int<br>
| C++: virtual int GetInMRMLCallbackFlag()<br>
|<br>
| Flags to avoid event loops.<br>
|<br>
| \warning Do NOT use the SetMacro or it call modified on itself<br>
| and<br>
| generate even more events!<br>
|<br>
| GetModifiedEventPending(…)<br>
| V.GetModifiedEventPending() → int<br>
| C++: virtual int GetModifiedEventPending()<br>
|<br>
| Number of pending modified events.<br>
|<br>
| \sa InvokePendingModifiedEvent()<br>
| \sa Modified()<br>
| \sa GetDisableModifiedEvent()<br>
|<br>
| GetName(…)<br>
| V.GetName() → string<br>
| C++: virtual char *GetName()<br>
|<br>
| GetNodeReference(…)<br>
| V.GetNodeReference(string) → vtkMRMLNode<br>
| C++: vtkMRMLNode *GetNodeReference(const char *referenceRole)<br>
|<br>
| Utility function that returns the first referenced node.<br>
| \sa GetNthNodeReference(int), GetNodeReferenceID()<br>
|<br>
| GetNodeReferenceID(…)<br>
| V.GetNodeReferenceID(string) → string<br>
| C++: const char *GetNodeReferenceID(const char *referenceRole)<br>
|<br>
| Utility function that returns the first node id for a<br>
| specificreferenceRole.<br>
|<br>
| \sa GetNthNodeReferenceID(int), GetNodeReference()<br>
|<br>
| GetNodeReferenceRoles(…)<br>
| V.GetNodeReferenceRoles(Stvector_ISt6stringE)<br>
| C++: void GetNodeReferenceRoles(std::vectorstd::string &amp;roles)<br>
|<br>
| Get reference roles of the present node references.<br>
| \sa GetNodeReferenceRoles(), GetNodeReferenceRoles(),<br>
| GetNthNodeReferenceRole()<br>
|<br>
| GetNthNodeReference(…)<br>
| V.GetNthNodeReference(string, int) → vtkMRMLNode<br>
| C++: vtkMRMLNode *GetNthNodeReference(const char *referenceRole,<br>
| int n)<br>
|<br>
| Get referenced MRML node for a specific referenceRole.<br>
|<br>
| Can be 0 in temporary states; e.g. if the referenced node has no<br>
| scene, or if the referenced is not yet into the scene. If not<br>
| cached, it tnternally scans (slow) the scene to search for the<br>
| associated referenced node ID. If the referencing node is no<br>
| longer in the scene (GetScene() == 0), it happens after the node<br>
| is removed from the scene (scene-&gt;RemoveNode(dn), the returned<br>
| referenced node is 0.<br>
|<br>
| GetNthNodeReferenceID(…)<br>
| V.GetNthNodeReferenceID(string, int) → string<br>
| C++: const char *GetNthNodeReferenceID(const char *referenceRole,<br>
| int n)<br>
|<br>
| Return the string of the Nth node ID for a specific reference<br>
| role.<br>
|<br>
| Return 0 if no such node exist.<br>
|<br>
| \warning A temporary char generated from a std::string::c_str()<br>
| is returned.<br>
|<br>
| GetNthNodeReferenceRole(…)<br>
| V.GetNthNodeReferenceRole(int) → string<br>
| C++: const char *GetNthNodeReferenceRole(int n)<br>
|<br>
| Get a specific node reference role name.<br>
| \sa GetNodeReferenceRoles(), GetNodeReferenceRoles(),<br>
| GetNthNodeReferenceRole()<br>
|<br>
| GetNumberOfNodeReferenceRoles(…)<br>
| V.GetNumberOfNodeReferenceRoles() → int<br>
| C++: int GetNumberOfNodeReferenceRoles()<br>
|<br>
| Get number of node reference role names.<br>
| \sa GetNodeReferenceRoles(), GetNodeReferenceRoles(),<br>
| GetNthNodeReferenceRole()<br>
|<br>
| GetNumberOfNodeReferences(…)<br>
| V.GetNumberOfNodeReferences(string) → int<br>
| C++: int GetNumberOfNodeReferences(const char *referenceRole)<br>
|<br>
| Return the number of node IDs for a specific reference role (and<br>
| nodes as they always<br>
| have the same size).<br>
|<br>
| GetSaveWithScene(…)<br>
| V.GetSaveWithScene() → int<br>
| C++: virtual int GetSaveWithScene()<br>
|<br>
| Save node with MRML scene.<br>
|<br>
| GetScene(…)<br>
| V.GetScene() → vtkMRMLScene<br>
| C++: virtual vtkMRMLScene *GetScene()<br>
|<br>
| Get the scene this node has been added to.<br>
|<br>
| GetSelectable(…)<br>
| V.GetSelectable() → int<br>
| C++: virtual int GetSelectable()<br>
|<br>
| Describes if the node is selectable.<br>
|<br>
| GetSelected(…)<br>
| V.GetSelected() → int<br>
| C++: virtual int GetSelected()<br>
|<br>
| Get/Set for Selected<br>
|<br>
| GetSingletonTag(…)<br>
| V.GetSingletonTag() → string<br>
| C++: virtual char *GetSingletonTag()<br>
|<br>
| GetUndoEnabled(…)<br>
| V.GetUndoEnabled() → bool<br>
| C++: virtual bool GetUndoEnabled()<br>
|<br>
| Specifies if the state of this node is stored in the scene’s undo<br>
| buffer. False by default to make sure that undo can be enabled<br>
| selectively, only for nodes that are prepared to work correctly<br>
| when saved/restored. Nodes with different UndoEnabled value must<br>
| not reference to each other, because restoring states could lead<br>
| to unresolved node references. Therefore, when undo is enabled<br>
| for a certain node, it must be enabled for nodes that it<br>
| references (for example, if undo is enabled for vtkMRMLModelNode<br>
| then it must be enabled for vtkMRMLModelDisplayNode and<br>
| vtkMRMLModelStorageNode as well).<br>
|<br>
| HasCopyContent(…)<br>
| V.HasCopyContent() → bool<br>
| C++: virtual bool HasCopyContent()<br>
|<br>
| Returns true if the class supports deep and shallow copying node<br>
| content.<br>
|<br>
| HasNodeReferenceID(…)<br>
| V.HasNodeReferenceID(string, string) → bool<br>
| C++: bool HasNodeReferenceID(const char *referenceRole,<br>
| const char *referencedNodeID)<br>
|<br>
| Return true if referencedNodeID is in the node ID list for a<br>
| specific referenceRole.<br>
|<br>
| If nullptr is specified as role then all roles are checked.<br>
|<br>
| HideFromEditorsOff(…)<br>
| V.HideFromEditorsOff()<br>
| C++: virtual void HideFromEditorsOff()<br>
|<br>
| HideFromEditorsOn(…)<br>
| V.HideFromEditorsOn()<br>
| C++: virtual void HideFromEditorsOn()<br>
|<br>
| InvokeCustomModifiedEvent(…)<br>
| V.InvokeCustomModifiedEvent(int, void)<br>
| C++: virtual void InvokeCustomModifiedEvent(int eventId,<br>
| void *callData=nullptr)<br>
|<br>
| This method allows the node to compress events.<br>
|<br>
| Instead of invoking a certain event several times, the event is<br>
| called only once, for all the invocations that are made between<br>
| StartModify() and EndModify().<br>
|<br>
| Typical usage is to group several <code>...Added</code>, <code>...Removed</code>,<br>
| <code>...Modified</code> events into one, to improve performance.<br>
|<br>
| callData is passed to InvokeEvent() if the event is invoked<br>
| immediately.<br>
|<br>
| If the event is not invoked immediately then it will be sent with<br>
| <code>callData=nullptr</code>.<br>
|<br>
| InvokePendingModifiedEvent(…)<br>
| V.InvokePendingModifiedEvent() → int<br>
| C++: virtual int InvokePendingModifiedEvent()<br>
|<br>
| Invokes any modified events that are <code>pending</code>.<br>
|<br>
| Pending modified events were generated while the<br>
| DisableModifiedEvent flag was nonzero.<br>
|<br>
| Returns the total number of pending modified events that have<br>
| been replaced by the just invoked modified event(s).<br>
|<br>
| IsSingleton(…)<br>
| V.IsSingleton() → bool<br>
| C++: bool IsSingleton()<br>
|<br>
| Modified(…)<br>
| V.Modified()<br>
| C++: void Modified() override;<br>
|<br>
| Customized version of Modified() allowing to compress<br>
| vtkCommand::ModifiedEvent.<br>
|<br>
| It overrides the vtkObject method so that all changes to the node<br>
| which would normally generate a vtkCommand::ModifiedEvent can be<br>
| grouped into an <code>atomic</code> operation.<br>
|<br>
| Typical usage would be to disable modified events, call a series<br>
| of <code>Set*</code> operations, and then re-enable modified events and call<br>
| InvokePendingModifiedEvent() to invoke the event (if any of the<br>
| <code>Set*</code> calls actually changed the values of the instance<br>
| variables).<br>
|<br>
| \sa GetDisableModifiedEvent()<br>
|<br>
| OnNodeAddedToScene(…)<br>
| V.OnNodeAddedToScene()<br>
| C++: virtual void OnNodeAddedToScene()<br>
|<br>
| Updates this node if it depends on other nodes when the scene is<br>
| read in This method is called by scene when a node added to a<br>
| scene.<br>
|<br>
| ProcessChildNode(…)<br>
| V.ProcessChildNode(vtkMRMLNode)<br>
| C++: virtual void ProcessChildNode(vtkMRMLNode *)<br>
|<br>
| Set dependencies between this node and a child node<br>
| when parsing XML file.<br>
|<br>
| ProcessMRMLEvents(…)<br>
| V.ProcessMRMLEvents(vtkObject, int, void)<br>
| C++: virtual void ProcessMRMLEvents(vtkObject *caller,<br>
| unsigned long event, void *callData)<br>
|<br>
| Propagate events generated in mrml.<br>
|<br>
| RemoveAttribute(…)<br>
| V.RemoveAttribute(string)<br>
| C++: void RemoveAttribute(const char *name)<br>
|<br>
| Remove attribute with the specified name.<br>
|<br>
| RemoveNodeReferenceIDs(…)<br>
| V.RemoveNodeReferenceIDs(string)<br>
| C++: void RemoveNodeReferenceIDs(const char *referenceRole)<br>
|<br>
| Remove all node IDs and associated nodes for a specific<br>
| referenceRole.<br>
|<br>
| If referenceRole is 0 remove references for all roles<br>
|<br>
| RemoveNthNodeReferenceID(…)<br>
| V.RemoveNthNodeReferenceID(string, int)<br>
| C++: void RemoveNthNodeReferenceID(const char *referenceRole,<br>
| int n)<br>
|<br>
| Convenience method that removes the Nth node ID from the list.<br>
|<br>
| Reset(…)<br>
| V.Reset(vtkMRMLNode)<br>
| C++: virtual void Reset(vtkMRMLNode *defaultNode)<br>
|<br>
| Reset node attributes to the initial state as defined in the<br>
| constructor or the passed default node.<br>
|<br>
| It preserves values of the following dynamic attributes that may<br>
| be set by an application:<br>
| * SaveWithScene<br>
| * HideFromEditors<br>
| * Selectable<br>
| * SingletonTag.<br>
|<br>
| If a defaultNode pointer is passed then the values stored in that<br>
| node will be used to set the node contents. If defaultNode is<br>
| nullptr then the values set in the constructor of the class will<br>
| be used to set the node contents.<br>
|<br>
| ote Other attributes that needs to be preserved should be handled<br>
| in the subclass.<br>
|<br>
| \sa SetSaveWithScene()<br>
| \sa SetHideFromEditors()<br>
| \sa SetSelectable()<br>
| \sa SetSingletonTag()<br>
|<br>
| SaveWithSceneOff(…)<br>
| V.SaveWithSceneOff()<br>
| C++: virtual void SaveWithSceneOff()<br>
|<br>
| SaveWithSceneOn(…)<br>
| V.SaveWithSceneOn()<br>
| C++: virtual void SaveWithSceneOn()<br>
|<br>
| SelectableOff(…)<br>
| V.SelectableOff()<br>
| C++: virtual void SelectableOff()<br>
|<br>
| SelectableOn(…)<br>
| V.SelectableOn()<br>
| C++: virtual void SelectableOn()<br>
|<br>
| SelectedOff(…)<br>
| V.SelectedOff()<br>
| C++: virtual void SelectedOff()<br>
|<br>
| SelectedOn(…)<br>
| V.SelectedOn()<br>
| C++: virtual void SelectedOn()<br>
|<br>
| SetAddToScene(…)<br>
| V.SetAddToScene(int)<br>
| C++: virtual void SetAddToScene(int _arg)<br>
|<br>
| SetAddToSceneNoModify(…)<br>
| V.SetAddToSceneNoModify(int)<br>
| C++: void SetAddToSceneNoModify(int value)<br>
|<br>
| SetAndObserveNodeReferenceID(…)<br>
| V.SetAndObserveNodeReferenceID(string, string, vtkIntArray)<br>
| → vtkMRMLNode<br>
| C++: vtkMRMLNode *SetAndObserveNodeReferenceID(<br>
| const char *referenceRole, const char *referencedNodeID,<br>
| vtkIntArray *events=nullptr)<br>
|<br>
| Set and observe a reference node from this node for a<br>
| specificreferenceRole.<br>
|<br>
| Observe Modified event by default, optionally takes array of<br>
| events<br>
|<br>
| SetAndObserveNthNodeReferenceID(…)<br>
| V.SetAndObserveNthNodeReferenceID(string, int, string,<br>
| vtkIntArray) → vtkMRMLNode<br>
| C++: vtkMRMLNode *SetAndObserveNthNodeReferenceID(<br>
| const char *referenceRole, int n,<br>
| const char <em>referencedNodeID, vtkIntArray <em>events=nullptr)<br>
|<br>
| Set and observe the Nth node ID for a specific reference role.<br>
|<br>
| If n is larger than the number of reference nodes, the node ID is<br>
| added at the end of the list. If nodeReferenceID is 0, the node<br>
| ID is removed from the list. When a node ID is set (added or<br>
| changed), its corresponding node is searched (slow) into the<br>
| scene and cached for fast future access. It is possible however<br>
| that the node is not yet into the scene (due to some temporary<br>
| state (at loading time for example). UpdateScene() can later be<br>
| called to retrieve the nodes from the scene (automatically done<br>
| when loading a scene). Get(Nth)NodeReference() also scan the<br>
| scene if the node was not yet cached.<br>
| \sa SetAndObserveNodeReferenceID(const char</em>)<br>
| \sa AddAndObserveNodeReferenceID(const char</em>)<br>
| \sa RemoveNthNodeReferenceID(int)<br>
|<br>
| SetAttribute(…)<br>
| V.SetAttribute(string, string)<br>
| C++: void SetAttribute(const char *name, const char *value)<br>
|<br>
| Set a name value pair attribute.<br>
|<br>
| Fires a vtkCommand::ModifiedEvent.<br>
|<br>
| Attributes are written in the XML. If value is 0, the attribute<br>
| name is removed from the pair list.<br>
|<br>
| This function is a no-op if name is null or empty.<br>
|<br>
| \sa WriteXML()<br>
|<br>
| SetDescription(…)<br>
| V.SetDescription(string)<br>
| C++: virtual void SetDescription(const char *_arg)<br>
|<br>
| Text description of this node, to be set by the user.<br>
|<br>
| SetDisableModifiedEvent(…)<br>
| V.SetDisableModifiedEvent(int)<br>
| C++: void SetDisableModifiedEvent(int onOff)<br>
|<br>
| SetHideFromEditors(…)<br>
| V.SetHideFromEditors(int)<br>
| C++: virtual void SetHideFromEditors(int _arg)<br>
|<br>
| SetInMRMLCallbackFlag(…)<br>
| V.SetInMRMLCallbackFlag(int)<br>
| C++: void SetInMRMLCallbackFlag(int flag)<br>
|<br>
| SetName(…)<br>
| V.SetName(string)<br>
| C++: virtual void SetName(const char *_arg)<br>
|<br>
| Name of this node, to be set by the user<br>
|<br>
| SetNodeReferenceID(…)<br>
| V.SetNodeReferenceID(string, string) → vtkMRMLNode<br>
| C++: vtkMRMLNode *SetNodeReferenceID(const char *referenceRole,<br>
| const char *referencedNodeID)<br>
|<br>
| Set a reference to a node with specified nodeID from this node<br>
| for a specific referenceRole.<br>
|<br>
| SetNthNodeReferenceID(…)<br>
| V.SetNthNodeReferenceID(string, int, string) → vtkMRMLNode<br>
| C++: vtkMRMLNode *SetNthNodeReferenceID(const char *referenceRole,<br>
| int n, const char *referencedNodeID)<br>
|<br>
| Set a N-th reference from this node with<br>
| specifiedreferencedNodeID for a specific referenceRole.<br>
|<br>
| SetSaveWithScene(…)<br>
| V.SetSaveWithScene(int)<br>
| C++: virtual void SetSaveWithScene(int _arg)<br>
|<br>
| SetScene(…)<br>
| V.SetScene(vtkMRMLScene)<br>
| C++: virtual void SetScene(vtkMRMLScene *scene)<br>
|<br>
| This method is for internal use only.<br>
| Use AddNode method of vtkMRMLScene to add a node to the scene.<br>
|<br>
| Internally calls SetSceneReferences()<br>
| \sa SetSceneReferences()<br>
|<br>
| SetSceneReferences(…)<br>
| V.SetSceneReferences()<br>
| C++: virtual void SetSceneReferences()<br>
|<br>
| Update the references of the node to the scene.<br>
|<br>
| ote You must unsure that a valid scene is set before calling<br>
| SetSceneReferences().<br>
|<br>
| SetSelectable(…)<br>
| V.SetSelectable(int)<br>
| C++: virtual void SetSelectable(int _arg)<br>
|<br>
| SetSelected(…)<br>
| V.SetSelected(int)<br>
| C++: virtual void SetSelected(int _arg)<br>
|<br>
| SetSingletonOff(…)<br>
| V.SetSingletonOff()<br>
| C++: void SetSingletonOff()<br>
|<br>
| SetSingletonOn(…)<br>
| V.SetSingletonOn()<br>
| C++: void SetSingletonOn()<br>
|<br>
| SetSingletonTag(…)<br>
| V.SetSingletonTag(string)<br>
| C++: virtual void SetSingletonTag(const char *_arg)<br>
|<br>
| Tag that make this node a singleton in the scene.<br>
|<br>
| If set to nullptr, multiple instances of this node class are<br>
| allowed.<br>
|<br>
| If set to a non-nullptr string, the node will be a singleton and<br>
| the scene will replace this node instead of adding new instances.<br>
|<br>
| The SingletonTag is used by the scene to build a unique ID.<br>
|<br>
| If the there can only be one instance of a given node class in<br>
| the scene, then the singleton tag should be Singleton. For<br>
| example, the interaction and selection nodes are named Selection<br>
| and Interaction, with Singleton tags set to Singleton, and with<br>
| IDs set to vtkMRMLSelectionNodeSingleton and<br>
| vtkMRMLInteractionNodeSingleton. If the singleton node is<br>
| associated with a specific module it should use the module name,<br>
| which already needs to be unique, as the tag. The Editor module<br>
| uses this naming convention, with a parameter node that has a<br>
| singleton tag of Editor and a node ID of<br>
| vtkMRMLScriptedModuleNodeEditor. If the there is more than one<br>
| instance of the node class then the singleton tag should be<br>
| Singleton post-pended with a unique identifier for that specific<br>
| node (e.g. the name). Any new color nodes should use this<br>
| convention, with a name of NewName, a Singleton tag of<br>
| SingletonNewName, leading to an ID of<br>
| vtkMRMLColorTableNodeSingletonNewName. The existing MRML nodes<br>
| don’t always use these conventions but are kept unchanged for<br>
| backward compatibility.<br>
| \sa vtkMRMLScene::BuildID<br>
|<br>
| SetUndoEnabled(…)<br>
| V.SetUndoEnabled(bool)<br>
| C++: virtual void SetUndoEnabled(bool _arg)<br>
|<br>
| StartModify(…)<br>
| V.StartModify() → int<br>
| C++: virtual int StartModify()<br>
|<br>
| Start modifying the node. Disable Modify events.<br>
|<br>
| Returns the previous state of DisableModifiedEvent flag that<br>
| should be passed to EndModify() method.<br>
|<br>
| \sa EndModify()<br>
|<br>
| URLDecodeString(…)<br>
| V.URLDecodeString(string) → string<br>
| C++: const char *URLDecodeString(const char *inString)<br>
|<br>
| Decode a URL string.<br>
|<br>
| Returns the string (null) if the input is null.<br>
|<br>
| ote Currently only works on %, space, ', ", &lt;, &gt;<br>
| \sa URLEncodeString()<br>
|<br>
| URLEncodeString(…)<br>
| V.URLEncodeString(string) → string<br>
| C++: const char *URLEncodeString(const char *inString)<br>
|<br>
| Encode a URL string.<br>
|<br>
| Returns the string (null) if the input is null.<br>
|<br>
| ote Currently only works on %, space, ', ", &lt;, &gt;<br>
| \sa URLDecodeString()<br>
|<br>
| UndoEnabledOff(…)<br>
| V.UndoEnabledOff()<br>
| C++: virtual void UndoEnabledOff()<br>
|<br>
| UndoEnabledOn(…)<br>
| V.UndoEnabledOn()<br>
| C++: virtual void UndoEnabledOn()<br>
|<br>
| UpdateReferenceID(…)<br>
| V.UpdateReferenceID(string, string)<br>
| C++: virtual void UpdateReferenceID(const char *oldID,<br>
| const char *newID)<br>
|<br>
| Update the stored reference to another node in the scene.<br>
|<br>
| UpdateReferences(…)<br>
| V.UpdateReferences()<br>
| C++: virtual void UpdateReferences()<br>
|<br>
| The method should remove all pointers and observations to all<br>
| nodes<br>
| that are not in the scene anymore.<br>
|<br>
| This method is called when one or more referenced nodes are<br>
| deleted from the scene.<br>
|<br>
| UpdateScene(…)<br>
| V.UpdateScene(vtkMRMLScene)<br>
| C++: virtual void UpdateScene(vtkMRMLScene *)<br>
|<br>
| Updates other nodes in the scene depending on this node or<br>
| updates this node if it depends on other nodes when the scene is<br>
| read in This method is called automatically by XML parser after<br>
| all nodes are created<br>
|<br>
| XMLAttributeDecodeString(…)<br>
| V.XMLAttributeDecodeString(string) → string<br>
| C++: std::string XMLAttributeDecodeString(<br>
| const std::string &amp;inString)<br>
|<br>
| Decode an XML attribute string.<br>
|<br>
| Important: attributes that vtkMRMLNode::ReadXMLAttributes method<br>
| receives are already decoded, therefore no XML attribute decoding<br>
| must not be applied to those strings.<br>
|<br>
| \sa XMLAttributeEncodeString()<br>
|<br>
| XMLAttributeEncodeString(…)<br>
| V.XMLAttributeEncodeString(string) → string<br>
| C++: std::string XMLAttributeEncodeString(<br>
| const std::string &amp;inString)<br>
|<br>
| Encode an XML attribute string (replaces special characters by<br>
| code sequences)<br>
|<br>
| \sa XMLAttributeDecodeString()<br>
|<br>
| ----------------------------------------------------------------------<br>
| Data and other attributes inherited from MRMLCorePython.vtkMRMLNode:<br>
|<br>
| HierarchyModifiedEvent = 16000<br>
|<br>
| IDChangedEvent = 16001<br>
|<br>
| ReferenceAddedEvent = 16002<br>
|<br>
| ReferenceModifiedEvent = 16003<br>
|<br>
| ReferenceRemovedEvent = 16004<br>
|<br>
| ReferencedNodeModifiedEvent = 16005<br>
|<br>
| ----------------------------------------------------------------------<br>
| Methods inherited from vtkCommonCorePython.vtkObject:<br>
|<br>
| AddObserver(…)<br>
| V.AddObserver(int, function) → int<br>
| C++: unsigned long AddObserver(const char *event,<br>
| vtkCommand *command, float priority=0.0f)<br>
|<br>
| Add an event callback function(vtkObject, int) for an event type.<br>
| Returns a handle that can be used with RemoveEvent(int).<br>
|<br>
| BreakOnError(…)<br>
| V.BreakOnError()<br>
| C++: static void BreakOnError()<br>
|<br>
| This method is called when vtkErrorMacro executes. It allows the<br>
| debugger to break on error.<br>
|<br>
| DebugOff(…)<br>
| V.DebugOff()<br>
| C++: virtual void DebugOff()<br>
|<br>
| Turn debugging output off.<br>
|<br>
| DebugOn(…)<br>
| V.DebugOn()<br>
| C++: virtual void DebugOn()<br>
|<br>
| Turn debugging output on.<br>
|<br>
| GetCommand(…)<br>
| V.GetCommand(int) → vtkCommand<br>
| C++: vtkCommand *GetCommand(unsigned long tag)<br>
|<br>
| Allow people to add/remove/invoke observers (callbacks) to any<br>
| VTK object. This is an implementation of the subject/observer<br>
| design pattern. An observer is added by specifying an event to<br>
| respond to and a vtkCommand to execute. It returns an unsigned<br>
| long tag which can be used later to remove the event or retrieve<br>
| the command. When events are invoked, the observers are called in<br>
| the order they were added. If a priority value is specified, then<br>
| the higher priority commands are called first. A command may set<br>
| an abort flag to stop processing of the event. (See vtkCommand.h<br>
| for more information.)<br>
|<br>
| GetDebug(…)<br>
| V.GetDebug() → bool<br>
| C++: bool GetDebug()<br>
|<br>
| Get the value of the debug flag.<br>
|<br>
| GetGlobalWarningDisplay(…)<br>
| V.GetGlobalWarningDisplay() → int<br>
| C++: static int GetGlobalWarningDisplay()<br>
|<br>
| This is a global flag that controls whether any debug, warning or<br>
| error messages are displayed.<br>
|<br>
| GetMTime(…)<br>
| V.GetMTime() → int<br>
| C++: virtual vtkMTimeType GetMTime()<br>
|<br>
| Return this object’s modified time.<br>
|<br>
| GlobalWarningDisplayOff(…)<br>
| V.GlobalWarningDisplayOff()<br>
| C++: static void GlobalWarningDisplayOff()<br>
|<br>
| This is a global flag that controls whether any debug, warning or<br>
| error messages are displayed.<br>
|<br>
| GlobalWarningDisplayOn(…)<br>
| V.GlobalWarningDisplayOn()<br>
| C++: static void GlobalWarningDisplayOn()<br>
|<br>
| This is a global flag that controls whether any debug, warning or<br>
| error messages are displayed.<br>
|<br>
| HasObserver(…)<br>
| V.HasObserver(int, vtkCommand) → int<br>
| C++: vtkTypeBool HasObserver(unsigned long event, vtkCommand *)<br>
| V.HasObserver(string, vtkCommand) → int<br>
| C++: vtkTypeBool HasObserver(const char *event, vtkCommand *)<br>
| V.HasObserver(int) → int<br>
| C++: vtkTypeBool HasObserver(unsigned long event)<br>
| V.HasObserver(string) → int<br>
| C++: vtkTypeBool HasObserver(const char *event)<br>
|<br>
| Allow people to add/remove/invoke observers (callbacks) to any<br>
| VTK object. This is an implementation of the subject/observer<br>
| design pattern. An observer is added by specifying an event to<br>
| respond to and a vtkCommand to execute. It returns an unsigned<br>
| long tag which can be used later to remove the event or retrieve<br>
| the command. When events are invoked, the observers are called in<br>
| the order they were added. If a priority value is specified, then<br>
| the higher priority commands are called first. A command may set<br>
| an abort flag to stop processing of the event. (See vtkCommand.h<br>
| for more information.)<br>
|<br>
| InvokeEvent(…)<br>
| V.InvokeEvent(int, void) → int<br>
| C++: int InvokeEvent(unsigned long event, void *callData)<br>
| V.InvokeEvent(string, void) → int<br>
| C++: int InvokeEvent(const char *event, void *callData)<br>
| V.InvokeEvent(int) → int<br>
| C++: int InvokeEvent(unsigned long event)<br>
| V.InvokeEvent(string) → int<br>
| C++: int InvokeEvent(const char *event)<br>
|<br>
| This method invokes an event and return whether the event was<br>
| aborted or not. If the event was aborted, the return value is 1,<br>
| otherwise it is 0.<br>
|<br>
| RemoveAllObservers(…)<br>
| V.RemoveAllObservers()<br>
| C++: void RemoveAllObservers()<br>
|<br>
| RemoveObserver(…)<br>
| V.RemoveObserver(vtkCommand)<br>
| C++: void RemoveObserver(vtkCommand *)<br>
| V.RemoveObserver(int)<br>
| C++: void RemoveObserver(unsigned long tag)<br>
|<br>
| Allow people to add/remove/invoke observers (callbacks) to any<br>
| VTK object. This is an implementation of the subject/observer<br>
| design pattern. An observer is added by specifying an event to<br>
| respond to and a vtkCommand to execute. It returns an unsigned<br>
| long tag which can be used later to remove the event or retrieve<br>
| the command. When events are invoked, the observers are called in<br>
| the order they were added. If a priority value is specified, then<br>
| the higher priority commands are called first. A command may set<br>
| an abort flag to stop processing of the event. (See vtkCommand.h<br>
| for more information.)<br>
|<br>
| RemoveObservers(…)<br>
| V.RemoveObservers(int, vtkCommand)<br>
| C++: void RemoveObservers(unsigned long event, vtkCommand *)<br>
| V.RemoveObservers(string, vtkCommand)<br>
| C++: void RemoveObservers(const char *event, vtkCommand *)<br>
| V.RemoveObservers(int)<br>
| C++: void RemoveObservers(unsigned long event)<br>
| V.RemoveObservers(string)<br>
| C++: void RemoveObservers(const char *event)<br>
|<br>
| Allow people to add/remove/invoke observers (callbacks) to any<br>
| VTK object. This is an implementation of the subject/observer<br>
| design pattern. An observer is added by specifying an event to<br>
| respond to and a vtkCommand to execute. It returns an unsigned<br>
| long tag which can be used later to remove the event or retrieve<br>
| the command. When events are invoked, the observers are called in<br>
| the order they were added. If a priority value is specified, then<br>
| the higher priority commands are called first. A command may set<br>
| an abort flag to stop processing of the event. (See vtkCommand.h<br>
| for more information.)<br>
|<br>
| SetDebug(…)<br>
| V.SetDebug(bool)<br>
| C++: void SetDebug(bool debugFlag)<br>
|<br>
| Set the value of the debug flag. A true value turns debugging on.<br>
|<br>
| SetGlobalWarningDisplay(…)<br>
| V.SetGlobalWarningDisplay(int)<br>
| C++: static void SetGlobalWarningDisplay(int val)<br>
|<br>
| This is a global flag that controls whether any debug, warning or<br>
| error messages are displayed.<br>
|<br>
| ----------------------------------------------------------------------<br>
| Methods inherited from vtkCommonCorePython.vtkObjectBase:<br>
|<br>
| FastDelete(…)<br>
| V.FastDelete()<br>
| C++: virtual void FastDelete()<br>
|<br>
| Delete a reference to this object. This version will not invoke<br>
| garbage collection and can potentially leak the object if it is<br>
| part of a reference loop. Use this method only when it is known<br>
| that the object has another reference and would not be collected<br>
| if a full garbage collection check were done.<br>
|<br>
| GetAddressAsString(…)<br>
| V.GetAddressAsString(string) → string<br>
| C++: const char *GetAddressAsString()<br>
|<br>
| Get address of C++ object in format ‘Addr=%p’ after casting to<br>
| the specified type. You can get the same information from o.<strong>this</strong>.<br>
|<br>
| GetClassName(…)<br>
| V.GetClassName() → string<br>
| C++: const char *GetClassName()<br>
|<br>
| Return the class name as a string.<br>
|<br>
| GetReferenceCount(…)<br>
| V.GetReferenceCount() → int<br>
| C++: int GetReferenceCount()<br>
|<br>
| Return the current reference count of this object.<br>
|<br>
| InitializeObjectBase(…)<br>
| V.InitializeObjectBase()<br>
| C++: void InitializeObjectBase()<br>
|<br>
| Register(…)<br>
| V.Register(vtkObjectBase)<br>
| C++: virtual void Register(vtkObjectBase *o)<br>
|<br>
| Increase the reference count by 1.<br>
|<br>
| SetReferenceCount(…)<br>
| V.SetReferenceCount(int)<br>
| C++: void SetReferenceCount(int)<br>
|<br>
| Sets the reference count. (This is very dangerous, use with<br>
| care.)<br>
|<br>
| UnRegister(…)<br>
| V.UnRegister(vtkObjectBase)<br>
| C++: virtual void UnRegister(vtkObjectBase *o)<br>
|<br>
| Decrease the reference count (release by another object). This<br>
| has the same effect as invoking Delete() (i.e., it reduces the<br>
| reference count by</p>
</blockquote>
</aside>
<p>Thank you very much,<br>
I found 3 sections on ‘dice’ but then how do I use this to calculate pls.</p>
<p>Create instance of a GAD node. | | DiceResultsValidOff(…) | V.DiceResultsValidOff() | C++: virtual void DiceResultsValidOff() | | DiceResultsValidOn(…) | V.DiceResultsValidOn() | C++: virtual void DiceResultsValidOn() |</p>
<p>| | Get volume of the compare structure | | GetDiceCoefficient(…) | V.GetDiceCoefficient() → float | C++: virtual float GetDiceCoefficient() | | Get result dice coefficient | | GetDiceResultsValid(…) | V.GetDiceResultsValid() → bool | C++: virtual bool GetDiceResultsValid() | | Get/Set Dice results valid flag | | GetDiceTableNode(…) | V.GetDiceTableNode() → vtkMRMLTableNode | C++: vtkMRMLTableNode *GetDiceTableNode() | | Get Dice table node | | GetFalseNegativesPercent(…) | V.GetFalseNegativesPercent() → float | C++: virtual double GetFalseNegativesPercent() | | Get percentage of false negative labelmap voxels | | GetFalsePositivesPercent(…) | V.GetFalsePositivesPercent() → float | C++: virtual double GetFalsePositivesPercent() | | Get percentage of false positive labelmap voxels</p>
<p>| | Set compare segmentation node | | SetAndObserveDiceTableNode(…) | V.SetAndObserveDiceTableNode(vtkMRMLTableNode) | C++: void SetAndObserveDiceTableNode(vtkMRMLTableNode *node) | | Set Dice table node | | SetAndObserveHausdorffTableNode(…) | V.SetAndObserveHausdorffTableNode(vtkMRMLTableNode) | C++: void SetAndObserveHausdorffTableNode(vtkMRMLTableNode *node)</p>

---

## Post #8 by @Melanie (2023-06-23 04:25 UTC)

<aside class="quote no-group" data-username="Melanie" data-post="7" data-topic="18726">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/35a633/48.png" class="avatar"> Melanie:</div>
<blockquote>
<p>GetDiceCoefficient</p>
</blockquote>
</aside>
<p>All good, Thanks very much<br>
diceMetrics = paramNode.GetDiceCoefficient() worked</p>

---
