---
topic_id: 7270
title: "Simplifying Slicer Util Load Functions"
date: 2019-06-20
url: https://discourse.slicer.org/t/7270
---

# Simplifying slicer.util.load... functions

**Topic ID**: 7270
**Date**: 2019-06-20
**URL**: https://discourse.slicer.org/t/simplifying-slicer-util-load-functions/7270

---

## Post #1 by @lassoan (2019-06-20 22:28 UTC)

<p>Currently, it is very complicated to load a volume and get the result as a node:</p>
<pre><code>volumeNode = slicer.util.loadVolume('path/to/volume.nrrd', returnNode=True)[1]
</code></pre>
<p>I would propose to make the change of the API to make it work like this:</p>
<pre><code>volumeNode = slicer.util.loadVolume('path/to/volume.nrrd')
</code></pre>
<p>If volume loading failed (file not found, etc.) then function would throw an exception. There are a couple of similar functions, for loading transforms, segmentations, markups, etc.</p>
<p>This would be a backward-incompatible change, but since it would simplify Python scripts so much, I think it could worth the trouble. Alternatively, we could invent new names for these functions (slicer.util.readVolume, slicer.util.readTransform, …) that would use this simpler API and we could just leave the old slicer.util.load… functions unchanged. This would allow a smooth transition, but a more redundant API.</p>
<p>Any thoughts, preferences?</p>

---

## Post #2 by @jamesobutler (2019-06-20 23:01 UTC)

<p>If I didn’t look at the source code for loadVolume then I would expect it to return the volume node which is what you’ve proposed. I likely would use and check success based on the output variable being none or a node instead of needing a separate Boolean variable.</p>
<p>If the next release is to be called Slicer 5, then I would be fine with the API incompatible change. I’m not sure how prevalent the usage is throughout extensions, but it would be an easy fix.</p>

---

## Post #3 by @lassoan (2019-06-20 23:12 UTC)

<p>The change would affect Slicer-4.11.x preview versions ans Slicer-5.x stable versions.</p>

---

## Post #4 by @jcfr (2019-06-21 05:08 UTC)

<p>We could decorate the current methods with the <code>deprecated</code>  decorator (could be copied from <a href="https://github.com/vrcmarcos/python-deprecated/blob/master/deprecated/__init__.py" rel="nofollow noopener">here</a>)</p>
<p>That said, the fix is indeed quite easy and the python API gains in usability.</p>
<p>The extensions making use of <code>returnNode=True</code> are the following:</p>
<pre><code class="lang-nohighlight">BoneTextureExtension
Chest_Imaging_Platform
DiffusionQC
GeodesicSlicer
iGyne
mpReview
Q3DC
QuantitativeReporting
ShapeRegressionExtension
SlicerCaseIterator
SlicerCervicalSpine
SlicerCochlea
SlicerMorphExtension
SlicerProstateAblation
SliceTracker
SPHARM-PDM
TOMAAT
ZFrameRegistration
</code></pre>
<details>
<summary>
Detailed Usage</summary>
<pre><code class="lang-nohighlight">./BoneTextureExtension/BoneTextureSerializer/BoneTextureSerializer.py:334:            inputScan = slicer.util.loadNodeFromFile(case.scanFilePath, 'VolumeFile', properties, returnNode=True)
./BoneTextureExtension/BoneTextureSerializer/BoneTextureSerializer.py:337:            inputSegmentation = slicer.util.loadNodeFromFile(case.segmentationFilePath, 'VolumeFile', properties, returnNode=True)
./BoneTextureExtension/BoneTextureSerializer/BoneTextureSerializer.py:406:            inputScan = slicer.util.loadNodeFromFile(case.scanFilePath, 'VolumeFile', properties, returnNode=True)
./BoneTextureExtension/BoneTextureSerializer/BoneTextureSerializer.py:409:            inputSegmentation = slicer.util.loadNodeFromFile(case.segmentationFilePath, 'VolumeFile', properties, returnNode=True)
./Chest_Imaging_Platform/Scripted/attic/CIP_GetImage/CIP_GetImage.py:409:                (code, vtkLabelmapVolumeNode) = slicer.util.loadLabelVolume(locPath, {}, returnNode=True)     # Braces are needed for Windows compatibility... No comments...
./Chest_Imaging_Platform/Scripted/attic/LoadSaveDataWidget.py:340:                    (success, vtkLabelmapVolumeNode) = slicer.util.loadLabelVolume(fileName, {}, returnNode=True)
./Chest_Imaging_Platform/Scripted/attic/LoadSaveDataWidget.py:350:                    (success, vtkVolumeNode) = slicer.util.loadVolume(fileName, {}, returnNode=True)
./Chest_Imaging_Platform/Scripted/CIP_/CIP/logic/SlicerUtil.py:871:            (loaded, volume) = slicer.util.loadVolume(localFilePath, returnNode=True)
./DiffusionQC/SlicerDiffusionQC/GradQC.py:270:    _, self.maskNode = slicer.util.loadLabelVolume(self.maskSelector.currentPath, returnNode=True)
./GeodesicSlicer/GeodesicSlicer/GeodesicSlicer.py:634:  slicer.util.loadModel((name2), returnNode=True)[1]
./GeodesicSlicer/GeodesicSlicer/GeodesicSlicer.py:726:  slicer.util.loadModel((name2), returnNode=True)[1]
./GeodesicSlicer/GeodesicSlicer/GeodesicSlicer.py:899:          model2 = slicer.util.loadModel(filename, returnNode=True)[1]
./iGyne/iGyne/iGyneWizard/iGyneLoadModelStep.py:244:    success, volumeNode = slicer.util.loadVolume(uri, properties = {'name' : name}, returnNode=True)
./mpReview/mpReview.py:990:      (success,label) = slicer.util.loadLabelVolume(fileName, returnNode=True)
./mpReview/mpReview.py:1219:      (success,volume) = slicer.util.loadVolume(fileName,returnNode=True)
./Q3DC/Q3DC/Q3DC.py:1831:            success, modelNodes[name] = slicer.util.loadModel(filePath, returnNode=True)
./QuantitativeReporting/DICOMPlugins/DICOMParametricMapPlugin.py:108:    (_,pmNode) = slicer.util.loadVolume(os.path.join(self.tempDir,"pmap.nrrd"), returnNode=True)
./QuantitativeReporting/DICOMPlugins/DICOMSegmentationPlugin.py:189:                                                           returnNode=True)
./QuantitativeReporting/Testing/QuantitativeReportingTests.py:247:        _, label = slicer.util.loadVolume(f, {'labelmap': True}, returnNode=True)
./ShapeRegressionExtension/RegressionComputation/RegressionComputation.py:735:      success, model1 = slicer.util.loadModel(os.path.join(outputDirectoryPath, comparison_filename), returnNode=True)
./ShapeRegressionExtension/RegressionComputation/RegressionComputation.py:737:      success, model2 = slicer.util.loadModel(output_filepath, returnNode=True)
./ShapeRegressionExtension/RegressionVisualization/RegressionVisualization.py:414:      success, model = slicer.util.loadModel(fullPath, returnNode=True)
./ShapeRegressionExtension/RegressionVisualization/RegressionVisualization.py:904:      success, model = slicer.util.loadModel(self.shapePaths[i], returnNode=True)
./SlicerCaseIterator/SlicerCaseIterator/SlicerCaseIteratorLib/CsvTableIterator.py:352:    load_success, im_node = slicer.util.loadVolume(im_path, returnNode=True)
./SlicerCaseIterator/SlicerCaseIterator/SlicerCaseIteratorLib/CsvTableIterator.py:378:      load_success, ma_node = slicer.util.loadSegmentation(ma_path, returnNode=True)
./SlicerCaseIterator/SlicerCaseIterator/SlicerCaseIteratorLib/CsvTableIterator.py:382:      load_success, ma_node = slicer.util.loadLabelVolume(ma_path, returnNode=True)
./SlicerCervicalSpine/CervicalSpineTools/CervicalSpineTools.py:533:      [success, inputVolumeNode]  = slicer.util.loadVolume(imgPath, returnNode=True)
./SlicerCervicalSpine/CervicalVertebraTools/CervicalVertebraTools.py:342:      [success, croppedNode] = slicer.util.loadVolume(self.vsc.vtVars['intputCropPath'], returnNode=True)
./SlicerCervicalSpine/CervicalVertebraTools/CervicalVertebraTools.py:472:      [success, inputVolumeNode]  = slicer.util.loadVolume(imgPath, returnNode=True)
./SlicerCochlea/CochleaReg/CochleaReg.py:327:      [success, croppedFixedNode] = slicer.util.loadVolume(self.vsc.vtVars['fixedCropPath'], returnNode=True)
./SlicerCochlea/CochleaReg/CochleaReg.py:331:      [success, croppedMovingNode] = slicer.util.loadVolume(self.vsc.vtVars['movingCropPath'], returnNode=True)
./SlicerCochlea/CochleaReg/CochleaReg.py:408:      [success, fixedVolumeNode]  = slicer.util.loadVolume(fixedImgPath, returnNode=True)
./SlicerCochlea/CochleaReg/CochleaReg.py:424:      [success, movingVolumeNode] = slicer.util.loadVolume(movingImgPath, returnNode=True)
./SlicerCochlea/CochleaSeg/CochleaSeg.py:339:      [success, croppedNode] = slicer.util.loadVolume(self.vsc.vtVars['intputCropPath'], returnNode=True)
./SlicerCochlea/CochleaSeg/CochleaSeg.py:490:      [success, inputVolumeNode]  = slicer.util.loadVolume(imgPath, returnNode=True)
./SlicerCochlea/VisSimCommon/VisSimCommon.py:289:            [success, inputImgNode] = slicer.util.loadVolume( inputImg, returnNode=True)
./SlicerCochlea/VisSimCommon/VisSimCommon.py:316:            [success, inputImgNode] = slicer.util.loadVolume( inputImg, returnNode=True)
./SlicerMorphExtension/ImportSurfaceToSegment/ImportSurfaceToSegment.py:184:    [success, modelNode] = slicer.util.loadModel(surfaceFileName, returnNode=True)
./SlicerMorphExtension/SkyscanReconImport/SkyscanReconImport.py:274:    [success, outputVolumeNode] = slicer.util.loadVolume(imageFileTemplate, returnNode=True)
./SlicerProstateAblation/ProstateAblation/ProstateAblationUtils/session.py:534:      success, volume = slicer.util.loadVolume(files[0], returnNode=True)
./SlicerProstateAblation/ProstateAblation/ProstateAblationUtils/sessionData.py:135:      _, data = loadFunction(os.path.join(directory, filename), returnNode=True)
./SlicerProstateAblation/ProstateAblation/ProstateAblationUtils/steps/zFrameRegistration.py:114:      _, self.zFrameModelNode = slicer.util.loadModel(zFrameModelPath, returnNode=True)
./SlicerProstateAblation/ProstateAblation/ProstateAblationUtils/steps/zFrameRegistration.py:158:    _, self.tempModelNode = slicer.util.loadModel(zFrameTemplateModelFile, returnNode=True)
./SlicerProstateAblation/ProstateAblation/ProstateAblationUtils/steps/zFrameRegistration.py:163:    _, self.pathModelNode = slicer.util.loadModel(needlePathModelFile, returnNode=True)
./SliceTracker/SliceTracker/SliceTrackerRegistration.py:311:    success, fixedLabel = slicer.util.loadLabelVolume(args.fixed_label, returnNode=True)
./SliceTracker/SliceTracker/SliceTrackerRegistration.py:312:    success, movingLabel = slicer.util.loadLabelVolume(args.moving_label, returnNode=True)
./SliceTracker/SliceTracker/SliceTrackerRegistration.py:313:    success, fixedVolume = slicer.util.loadVolume(args.fixed_volume, returnNode=True)
./SliceTracker/SliceTracker/SliceTrackerRegistration.py:314:    success, movingVolume = slicer.util.loadVolume(args.moving_volume, returnNode=True)
./SliceTracker/SliceTracker/SliceTrackerUtils/preopHandler.py:274:      success, self.data.initialLabel = slicer.util.loadLabelVolume(filename, returnNode=True)
./SliceTracker/SliceTracker/SliceTrackerUtils/preopHandler.py:282:    success, self.data.initialVolume = slicer.util.loadVolume(self.preopImagePath, returnNode=True)
./SliceTracker/SliceTracker/SliceTrackerUtils/preopHandler.py:296:      success, self.data.initialTargets = slicer.util.loadMarkupsFiducialList(filename, returnNode=True)
./SliceTracker/SliceTracker/SliceTrackerUtils/sessionData.py:219:      _, data = loadFunction(os.path.join(directory, filename), returnNode=True)
./SliceTracker/SliceTracker/SliceTrackerUtils/steps/zFrameRegistration.py:81:      _, self.zFrameModelNode = slicer.util.loadModel(zFrameModelPath, returnNode=True)
./SPHARM-PDM/Modules/Scripted/ShapeAnalysisModule/CommonUtilities/utility.py:23:      node = slicer.util.loadNodeFromFile(file_path, file_type, properties, returnNode=True)
./TOMAAT/TOMAAT/TOMAAT.py:447:    success, node = slicer.util.loadLabelVolume(tmp_segmentation_mha, properties={'show':False}, returnNode=True)
./TOMAAT/TOMAAT/TOMAAT.py:506:    success, node = slicer.util.loadTransform(tmp_transform, returnNode=True)
./ZFrameRegistration/ZFrameRegistrationWithROI/ZFrameRegistrationWithROI.py:323:    _, self.zFrameModelNode = slicer.util.loadModel(zFrameModelPath, returnNode=True)
./ZFrameRegistration/ZFrameRegistrationWithROI/ZFrameRegistrationWithROI.py:438:    _, imageDataNode = slicer.util.loadVolume(imageDataPath, returnNode=True)

</code></pre>
</details>

---

## Post #5 by @pieper (2019-06-21 13:58 UTC)

<p>Please let’s not break things without a really good reason.  I totally agree about wanting a cleaner API so let’s invent the new names (I like the readVolume names etc) and mark the others as deprecated with a decorator that tells people how to update their code.</p>
<p>There’s just so much example code and tutorials out there (not to mention non-public extensions).</p>

---

## Post #6 by @jamesobutler (2019-06-21 14:17 UTC)

<p>Having API changes always follow a path of deprecated for the next release (Slicer 5.0) and then removed (Slicer 5.1) sounds like an appropriate action. This would provide time for all the example code and tutorials to be updated.</p>

---

## Post #7 by @lassoan (2019-06-21 14:20 UTC)

<p>I’ve found a way to improve the API without breaking anything:</p>
<ul>
<li>
<code>returnNode=False</code> (default) -&gt; return <code>node</code>: almost the same as before. Instead of a True/False flag we return node; but since the node is automatically casted to a Boolean in logical operators, this should not cause any problem. Most of the cases the returned flag is not checked anyway.</li>
<li>
<code>returnNode=True</code> -&gt; return <code>[success, node]</code>: exactly the same as before. We deprecate this argument to allow simplifying the API in the future.</li>
</ul>
<p>See proposed change in this <a href="https://github.com/Slicer/Slicer/compare/master...lassoan:simple-loadnode-api?expand=1" rel="nofollow noopener">pull request</a>.</p>

---

## Post #8 by @jcfr (2019-06-21 15:21 UTC)

<p>Since a scene file can contain a lot of nodes, I don’t think we should systematically return a complete list of all nodes</p>
<pre><code class="lang-python">  loadedNodesCollection = vtkCollection()
  success = app.coreIOManager().loadNodes(filetype, properties, loadedNodesCollection)

  # Convert VTK collection to Python object (if no or 1 returned node) or list (if multiple nodes loaded)
  loadedNodes = []
  for i in range(loadedNodesCollection.GetNumberOfItems()):
    loadedNode = loadedNodesCollection.GetItemAsObject(i)
    loadedNodes.append(loadedNode)
  if len(loadedNodes) == 0:
    loadedNodes = None
  elif len(loadedNodes) == 1:
    loadedNodes = loadedNodes[0]

  # Deprecated way of returning status and node
  if returnNode:
    logging.warning("loadNodeFromFile `returnNode` argument is deprecated. Loaded node is now returned directly if `returnNode` is not specified.")
    return success, loadedNodes

  if not success:
    errorMessage = "Failed to load node from file: " + str(filename)
    raise RuntimeError(errorMessage)

  return loadedNodes
</code></pre>
<p>There are few things that could help, following <a href="https://github.com/Kitware/VTK/commit/7602a0ef7adc" rel="nofollow noopener">VTK@7602a0ef7adc</a>, <code>vtkCollection</code> are iterable. This the code could be simplified to:</p>
<pre><code class="lang-python">  loadedNodesCollection = vtkCollection()
  success = app.coreIOManager().loadNodes(filetype, properties, loadedNodesCollection)

  # Convert VTK collection to Python object (if no or 1 returned node) or list (if multiple nodes loaded)
  loadedNodes = [node for node in loadedNodesCollection]
  if len(loadedNodes) == 0:
    loadedNodes = None
  elif len(loadedNodes) == 1:
    loadedNodes = loadedNodes[0]

  [...]
</code></pre>
<p>Even better, it is also possible to get an iterator from a collection, meaning we could have the following and avoid evaluating the complete list of nodes if not needed:</p>
<pre><code class="lang-python">  loadedNodesCollection = vtkCollection()
  success = app.coreIOManager().loadNodes(filetype, properties, loadedNodesCollection)

  # Deprecated way of returning status and node
  if returnNode:
    logging.warning("loadNodeFromFile `returnNode` argument is deprecated. Loaded node is now returned directly if `returnNode` is not specified.")
    try:
      firstLoadedNode = next(iter(loadedNodesCollection))
    except StopIteration:
      firstLoadedNode = None
    return success, firstLoadedNode

  if not success:
    errorMessage = "Failed to load node from file: %s" % filename
    raise RuntimeError(errorMessage)

  return iter(loadedNodesCollection)
</code></pre>

---

## Post #9 by @lassoan (2019-06-21 15:44 UTC)

<p>Scene loader does not return nodes at all (returns an empty list) and all other loaders just return one or a few nodes, so there should be no perceivable performance impact. Anyway, iterating through the collection with an iter() is definitely nicer, and so let’s do that (but only when multiple nodes are returned). Could you update the pull request?</p>

---

## Post #10 by @jcfr (2019-06-21 15:47 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="7270">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Could you update the pull request?</p>
</blockquote>
</aside>
<p>I will not have the bandwith today … Though, I could help with this on Monday.</p>
<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="7270">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Anyway, iterating through the collection with an iter() is definitely nicer, and so let’s do that (but only when multiple nodes are returned).</p>
</blockquote>
</aside>
<p>Currently, the function always return one node. I do not think we should conditionally return a list or a node based on the loaded file. Instead I suggest adding:</p>
<pre><code class="lang-auto">loadNodesFromFile
</code></pre>
<p>Finally, in which case is there multiple node to be returned ?</p>

---

## Post #11 by @lassoan (2019-06-23 03:18 UTC)

<p>Updated loadNodeFromFile to always return only the first loaded node (as it was done before) and added loadNodesFromFile that returns an iterator.</p>
<aside class="onebox githubpullrequest">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/pull/1159" target="_blank" rel="nofollow noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
      <a href="https://github.com/lassoan" target="_blank" rel="nofollow noopener">
    <img alt="lassoan" src="https://avatars0.githubusercontent.com/u/307929?v=4" class="thumbnail onebox-avatar" width="90" height="90">
  </a>

<h4>
  <a href="https://github.com/Slicer/Slicer/pull/1159" target="_blank" rel="nofollow noopener">ENH: Simplify node loading methods API in slicer.util</a>
</h4>

<div class="date">
  by <a href="https://github.com/lassoan" target="_blank" rel="nofollow noopener">lassoan</a>
  on <a href="https://github.com/Slicer/Slicer/pull/1159" target="_blank" rel="nofollow noopener">03:13AM - 23 Jun 19 UTC</a>
</div>

<div class="github-commit-stats">
  <strong>1 commits</strong>
  changed <strong>3 files</strong>
  with <strong>136 additions</strong>
  and <strong>12 deletions</strong>.
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Since the only change is that we return the actual node instead of a True/False flag and node can be used in operators that require Boolean value, this change should not cause any issues. I’ll merge it on Monday if there are no objections.</p>

---
