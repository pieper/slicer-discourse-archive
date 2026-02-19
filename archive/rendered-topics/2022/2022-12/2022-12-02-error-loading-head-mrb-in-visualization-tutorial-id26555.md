---
topic_id: 26555
title: "Error Loading Head Mrb In Visualization Tutorial"
date: 2022-12-02
url: https://discourse.slicer.org/t/26555
---

# Error Loading Head MRB in visualization tutorial

**Topic ID**: 26555
**Date**: 2022-12-02
**URL**: https://discourse.slicer.org/t/error-loading-head-mrb-in-visualization-tutorial/26555

---

## Post #1 by @Erin (2022-12-02 15:37 UTC)

<p>I have been trying to follow tutorial [Slicer 5.0 Basics of data loading and visualization tutorial].(<a href="https://spujol.github.io/SlicerVisualizationTutorial/" class="inline-onebox" rel="noopener nofollow ugc">SlicerVisualizationTutorial</a>)</p>
<p>However, I kept getting error as shown below and cannot manipulate the model. Could you please kindly help point out what I have done wrong?</p>
<ul>
<li>Error: Loading /Slicer Tutorial/3DVisualizationDataset/dataset2_Head/Head_Scene.mrb - ERROR: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLStorableNode.cxx, line 322</li>
</ul>
<p>vtkMRMLSceneViewNode (0x7f8757e6d730): vtkMRMLStorableNode::UpdateScene failed: Failed to read node Axial (vtkMRMLSceneViewNode11) using storage node vtkMRMLSceneViewStorageNode11.</p>
<ul>
<li>Error: Loading /Slicer Tutorial/3DVisualizationDataset/dataset2_Head/Head_Scene.mrb - ERROR: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLStorableNode.cxx, line 322</li>
</ul>
<p>vtkMRMLSceneViewNode (0x7f8757ee3fd0): vtkMRMLStorableNode::UpdateScene failed: Failed to read node Sagittal (vtkMRMLSceneViewNode12) using storage node vtkMRMLSceneViewStorageNode12.</p>
<ul>
<li>Error: Loading /Slicer Tutorial/3DVisualizationDataset/dataset2_Head/Head_Scene.mrb - ERROR: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLStorableNode.cxx, line 322</li>
</ul>
<p>vtkMRMLSceneViewNode (0x7f8745d5ea20): vtkMRMLStorableNode::UpdateScene failed: Failed to read node Coronal (vtkMRMLSceneViewNode13) using storage node vtkMRMLSceneViewStorageNode13.</p>
<p>Thanks a lot.<br>
Best,<br>
Erin</p>

---

## Post #2 by @pieper (2022-12-02 19:56 UTC)

<p>Thanks for reporting <a class="mention" href="/u/erin">@Erin</a>.  The errors you are seeing are due to this data coming from an older Slicer version and can be ignored.</p>
<p>However when testing this I realized that after loading this scene into Slicer 5.0.3 or 5.2.1 the 3D view is no longer responsive.  The full log is linked below, but I believe the key error is this one:</p>
<pre><code class="lang-auto">[Qt] virtual int ctkVTKAbstractView::resumeRender() Cannot resume rendering, pause render count is already 0!
</code></pre>
<p><a class="mention" href="/u/lassoan">@lassoan</a> or <a class="mention" href="/u/jcfr">@jcfr</a> do you recognize this?  I started and issue here: <a href="https://github.com/Slicer/Slicer/issues/6717" class="inline-onebox">3D View stops responding when loading tutorial scene · Issue #6717 · Slicer/Slicer · GitHub</a></p>
<p><a class="mention" href="/u/spujol">@spujol</a> fyi.  Maybe the easiest is to try recreating the scene file with a newer Slicer and re-uploading.</p>
<pre><code class="lang-auto">Python 3.9.10 (main, Nov 24 2022, 03:09:05)

[Clang 10.0.0 (clang-1000.11.45.5)] on darwin

&gt;&gt;&gt;

Loading Slicer RC file [/Users/pieper/.slicerrc.py]

/Applications/Slicer-5.2.1.app/Contents/bin/Python/slicer/util.py:2506: UserWarning: already has observer

warn('already has observer')

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd9778fc6d0): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897b2c720): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897b2d7b0): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897b2e9f0): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897b2fc30): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897b30e70): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897b320b0): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897b77f90): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897ba2870): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897ba3b50): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897ba4d90): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897ba61c0): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897ba75a0): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897ba89d0): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897bee9c0): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897c1d380): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897c1e660): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897c1f8a0): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897c20cd0): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897c220b0): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897c234e0): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897c69600): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897c93ee0): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897c951c0): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897c96400): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897c97830): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897c98c10): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897c9a040): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897ce11e0): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897d0fc70): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897d10f50): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897d12190): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897d133d0): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897d14610): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897d15850): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897d17f90): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897d19570): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897d67530): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897d91d30): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897d6bc70): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897d94140): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897d953a0): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897d96600): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897d97860): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLCameraNode.cxx, line 414

[VTK] vtkMRMLCameraNode (0x7fd897d98ac0): vtkMRMLCameraNode::SetActiveTag() is deprecated. Use vtkMRMLCameraNode::SetLayoutName() instead.

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLScene.cxx, line 1856

[VTK] vtkMRMLScene (0x7fd977bca390): The vtkMRMLCameraNode2 ID belongs to a singleton, therefore it will be treated as a singleton

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLScene.cxx, line 1856

[VTK] vtkMRMLScene (0x7fd977bca390): The vtkMRMLCameraNode3 ID belongs to a singleton, therefore it will be treated as a singleton

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLScene.cxx, line 1856

[VTK] vtkMRMLScene (0x7fd977bca390): The vtkMRMLCameraNode4 ID belongs to a singleton, therefore it will be treated as a singleton

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLScene.cxx, line 1856

[VTK] vtkMRMLScene (0x7fd977bca390): The vtkMRMLCameraNode5 ID belongs to a singleton, therefore it will be treated as a singleton

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLScene.cxx, line 1856

[VTK] vtkMRMLScene (0x7fd977bca390): The vtkMRMLCameraNode6 ID belongs to a singleton, therefore it will be treated as a singleton

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLScene.cxx, line 1856

[VTK] vtkMRMLScene (0x7fd977bca390): The vtkMRMLCameraNode7 ID belongs to a singleton, therefore it will be treated as a singleton

[VTK] Warning: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLScene.cxx, line 1856

[VTK] vtkMRMLScene (0x7fd977bca390): The vtkMRMLCameraNode8 ID belongs to a singleton, therefore it will be treated as a singleton

[VTK] ReadDataInternal: file does not exist: /Users/pieper/Library/Caches/NA-MIC/Slicer/SlicerIO/__BundleLoadTemp-2022-12-02_144254_374/MRHead_Scene/Data/Axial.png

[VTK] vtkMRMLStorageNode::ReadData: Failed to read node Axial (vtkMRMLSceneViewNode1) from filename='/Users/pieper/Library/Caches/NA-MIC/Slicer/SlicerIO/__BundleLoadTemp-2022-12-02_144254_374/MRHead_Scene/Data/Axial.png'

[VTK] ReadDataInternal: file does not exist: /Users/pieper/Library/Caches/NA-MIC/Slicer/SlicerIO/__BundleLoadTemp-2022-12-02_144254_374/MRHead_Scene/Data/Sagittal%20.png

[VTK] vtkMRMLStorageNode::ReadData: Failed to read node Sagittal (vtkMRMLSceneViewNode2) from filename='/Users/pieper/Library/Caches/NA-MIC/Slicer/SlicerIO/__BundleLoadTemp-2022-12-02_144254_374/MRHead_Scene/Data/Sagittal%20.png'

[VTK] ReadDataInternal: file does not exist: /Users/pieper/Library/Caches/NA-MIC/Slicer/SlicerIO/__BundleLoadTemp-2022-12-02_144254_374/MRHead_Scene/Data/Coronal%20.png

[VTK] vtkMRMLStorageNode::ReadData: Failed to read node Coronal (vtkMRMLSceneViewNode3) from filename='/Users/pieper/Library/Caches/NA-MIC/Slicer/SlicerIO/__BundleLoadTemp-2022-12-02_144254_374/MRHead_Scene/Data/Coronal%20.png'

[Qt] virtual int ctkVTKAbstractView::resumeRender() Cannot resume rendering, pause render count is already 0!

[Qt] virtual int ctkVTKAbstractView::resumeRender() Cannot resume rendering, pause render count is already 0!

[Qt] virtual int ctkVTKAbstractView::resumeRender() Cannot resume rendering, pause render count is already 0!

[Qt] virtual int ctkVTKAbstractView::resumeRender() Cannot resume rendering, pause render count is already 0!

[Qt] virtual int ctkVTKAbstractView::resumeRender() Cannot resume rendering, pause render count is already 0!

[Qt] virtual int ctkVTKAbstractView::resumeRender() Cannot resume rendering, pause render count is already 0!

[Qt] virtual int ctkVTKAbstractView::resumeRender() Cannot resume rendering, pause render count is already 0!

[Qt] virtual int ctkVTKAbstractView::resumeRender() Cannot resume rendering, pause render count is already 0!

[Qt] virtual int ctkVTKAbstractView::resumeRender() Cannot resume rendering, pause render count is already 0!

[Qt] virtual int ctkVTKAbstractView::resumeRender() Cannot resume rendering, pause render count is already 0!

[Qt] virtual int ctkVTKAbstractView::resumeRender() Cannot resume rendering, pause render count is already 0!

[Qt] virtual int ctkVTKAbstractView::resumeRender() Cannot resume rendering, pause render count is already 0!

[Qt] virtual int ctkVTKAbstractView::resumeRender() Cannot resume rendering, pause render count is already 0!

[Qt] virtual int ctkVTKAbstractView::resumeRender() Cannot resume rendering, pause render count is already 0!

[Qt] virtual int ctkVTKAbstractView::resumeRender() Cannot resume rendering, pause render count is already 0!

[Qt] virtual int ctkVTKAbstractView::resumeRender() Cannot resume rendering, pause render count is already 0!

[Qt] static void qSlicerIOManager::showLoadNodesResultDialog(bool, vtkMRMLMessageCollection *) Errors occurred while loading nodes: "- Error: Loading /private/tmp/3DVisualizationDataset/dataset2_Head/Head_Scene.mrb - ERROR: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLStorableNode.cxx, line 326\nvtkMRMLSceneViewNode (0x7fd897b33420): vtkMRMLStorableNode::UpdateScene failed: Failed to read node Axial (vtkMRMLSceneViewNode1) using storage node vtkMRMLSceneViewStorageNode3.\n- Error: Loading /private/tmp/3DVisualizationDataset/dataset2_Head/Head_Scene.mrb - ERROR: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLStorableNode.cxx, line 326\nvtkMRMLSceneViewNode (0x7fd897ba9e50): vtkMRMLStorableNode::UpdateScene failed: Failed to read node Sagittal (vtkMRMLSceneViewNode2) using storage node vtkMRMLSceneViewStorageNode4.\n- Error: Loading /private/tmp/3DVisualizationDataset/dataset2_Head/Head_Scene.mrb - ERROR: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLStorableNode.cxx, line 326\nvtkMRMLSceneViewNode (0x7fd897c24a90): vtkMRMLStorableNode::UpdateScene failed: Failed to read node Coronal (vtkMRMLSceneViewNode3) using storage node vtkMRMLSceneViewStorageNode5.\n"
</code></pre>

---

## Post #3 by @lassoan (2022-12-02 20:16 UTC)

<p>Our lab maintains an up-to-date version of the Slicer Basic Data Visualization tutorial:</p>
<ul>
<li><a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day1_2_DataLoadingAndVisualizationTutorial.pptx">slides</a></li>
<li><a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Data/VisualizationTutorial_HeadScene.mrb">data</a></li>
</ul>
<p>We already know that the training portal needs an overhaul (see <a href="https://github.com/Slicer/Slicer/issues/6676" class="inline-onebox">Improve Slicer training portal · Issue #6676 · Slicer/Slicer · GitHub</a>). We also plan to develop and maintain Slicer core training materials more collaboratively - for this we recently got funding from CZI (<a href="https://chanzuckerberg.com/eoss/proposals/3d-slicer-for-latin-america-localization-and-outreach/" class="inline-onebox">3D Slicer for Latin America: Localization and Outreach - Chan Zuckerberg Initiative</a>).</p>
<p><a class="mention" href="/u/pieper">@pieper</a> The issue is due to how views were linked in old and new scenes. The warning messages are mostly harmless, but sometimes there are some problems, such as 3D view cannot be rotated (<a href="https://github.com/Slicer/Slicer/issues/6717">#6717</a>). I’ll add comments in the issue tracker about it.</p>

---

## Post #4 by @pieper (2022-12-02 23:15 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>, glad you are on top of this.</p>

---
