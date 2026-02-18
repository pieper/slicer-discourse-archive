# Batch script using ModelMaker

**Topic ID**: 9422
**Date**: 2019-12-07
**URL**: https://discourse.slicer.org/t/batch-script-using-modelmaker/9422

---

## Post #1 by @ButuiHu (2019-12-07 10:43 UTC)

<p>I have a lot of label map volume, and I would like to convert all to poly data vtk files. After googling, ITK-SNAP could help to export to vtk file, but could not run in batch script mode. 3D slicer’s ModelMaker could also do this, and it’s possible run a script. For now, what I have done:</p>
<pre><code class="lang-python">for seg_filename in seg_filenames:
    seg_nodename = seg_filename.split('/')[-1].split('.')[0]
    img_node = slicer.util.loadVolume(img_filename)
    label_node = slicer.util.loadLabelVolume(seg_filename)
    parameters = dict()
    parameters['InputVolume'] = label_node.GetID()
    result_model = slicer.vtkMRMLModelHierarchyNode()
    result_model.SetName(seg_nodename)
    slicer.mrmlScene.AddNode(result_model)
    parameters['ModelSceneFile'] = result_model.GetID()
    parameters['Name'] = seg_nodename
    modelmaker = slicer.modules.modelmaker
    slicer.cli.run(modelmaker, None, parameters)
</code></pre>
<p>I’m stuck at how to save the result. I can use <code>slicer.saveNode(node, filename, properties={})</code> to save a single node, but I don’t what to pass to <code>node</code>.<br>
It would be great how ModelMaker converts volume to model using VTK or ITK internally, then I could write python script using VTK or ITK directly.</p>

---

## Post #2 by @lassoan (2019-12-07 12:24 UTC)

<p>Probably the simplest is to export using segmentation module’s export to files feature. Set <code>inputLabelmapFile</code> and <code>outputFolder</code> and run this code:</p>
<pre><code class="lang-python">segmentationNode = slicer.util.loadSegmentation(inputLabelmapFile)
slicer.modules.segmentations.logic().ExportSegmentsClosedSurfaceRepresentationToFiles(outputFolder, segmentationNode)
</code></pre>
<p>This code works on recent Slicer Preview Releases. On latest Stable Releases this would be a few lines longer: labelmap need to be loaded as volume node and that has to be imported to segmentation node.</p>

---
