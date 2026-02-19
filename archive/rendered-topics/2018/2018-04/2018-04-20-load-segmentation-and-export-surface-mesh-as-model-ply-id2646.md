---
topic_id: 2646
title: "Load Segmentation And Export Surface Mesh As Model Ply"
date: 2018-04-20
url: https://discourse.slicer.org/t/2646
---

# Load segmentation and export surface mesh as model .ply

**Topic ID**: 2646
**Date**: 2018-04-20
**URL**: https://discourse.slicer.org/t/load-segmentation-and-export-surface-mesh-as-model-ply/2646

---

## Post #1 by @ladybug (2018-04-20 12:57 UTC)

<p>Hello,<br>
I’m new to creating modules and my programming skills are rather basic, so I encountered problems in loading segmentation from subdirectories, and in exporting and saving the mesh models.<br>
The first issue looks like following: I want to load segmentations named ‘_repair.seg.nrrd’ from multiple subdirectories. What I got so far is:</p>
<pre><code class="lang-auto">  def onExportButtonClicked(self):
    dir_path = qt.QFileDialog.getExistingDirectory(None, 'Open folder', '/home/', qt.QFileDialog.ShowDirsOnly)
    dir_path = dir_path.replace("\\", "/")
    for filename in os.listdir(dir_path):
      self.exportMesh(dir_path, filename)
    print("Finished.")
    
  def exportMesh(self, dir_path, filename):
    whichOP= "preop"
	# Load segmentation (repair .seg.nrrd)
    file_complete = dir_path + "/" + filename + "/" + whichOP + "/CT/" + filename + "_" + whichOP + "_repair.seg.nrrd"
    print("Loading {}".format(file_complete))
    slicer.app.processEvents()
    MasterModelNode = slicer.util.loadNodeFromFile(file_complete, "_repair.seg.nrrd", {}, returnNode=True)
    modelNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLModelHierarchyNode')
    slicer.modules.segmentations.logic().ExportAllSegmentsToModelHierarchy(MasterModelNode, modelNode) 
</code></pre>
<p>I can’t get further, because I get an error:</p>
<pre><code class="lang-auto">TypeError: ExportAllSegmentsToModelHierarchy argument 1: method requires a VTK object. 
</code></pre>
<p>I would be really grateful for your help, as I lack knowledge to fix this (probably really trivial) problem.  I have a next piece of code that looks as below. However, I don’t even know if it works, because of the previous error I mentioned.</p>
<pre><code class="lang-auto">    # Make sure surface mesh cells are consistently oriented
    surfaceMesh = MasterModelNode.GetClosedSurfaceRepresentation(segmentID)
    normals = vtk.vtkPolyDataNormals()
    normals.AutoOrientNormalsOn()
    normals.ConsistencyOn()
    normals.SetInputData(surfaceMesh)
    normals.Update()
    surfaceMesh = normals.GetOutput()
    # Save as PLY file
    writer = vtk.vtkSTLWriter()
    writer.SetInputData(surfaceMesh)
    #### name should be: name of segmentation .ply
    file_new = dir_path + "/" + filename + "/" + whichOP + "/CT/" + filename + segmentName + ".ply"
    writer.SetFileName(file_new) # set file name
    writer.Update()
    # Clean up
    segmentEditorWidget = None
    slicer.mrmlScene.RemoveNode(file_complete)
    slicer.mrmlScene.RemoveNode(segmentEditorNode)
</code></pre>
<p>Best regards!</p>

---

## Post #2 by @pieper (2018-04-21 16:20 UTC)

<aside class="quote no-group quote-modified" data-username="ladybug" data-post="1" data-topic="2646">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/46a35a/48.png" class="avatar"> ladybug:</div>
<blockquote>
<p>MasterModelNode = slicer.util.loadNodeFromFile(file_complete, “_repair.seg.nrrd”, {}, returnNode=True)</p>
</blockquote>
</aside>
<p>Probably this line is not working as you expect leading to the error message about needing a vtk object.  Try printing out the result to debug.</p>

---

## Post #3 by @lassoan (2018-04-21 19:20 UTC)

<p>Yes, that line is incorrect. If <code>returnNode=True</code> is specified then <code>slicer.util.loadNodeFromFile</code> returns <code>(success, MasterModelNode)</code> pair and not just <code>MasterModelNode</code>.</p>

---

## Post #4 by @ladybug (2018-05-14 15:03 UTC)

<p>Hello again,<br>
Thank you so much for your reply. So after debug the code seems to work until it reaches:</p>
<p>slicer.modules.segmentations.logic().ExportAllSegmentsToModelHierarchy(MasterModelNode, modelNode)</p>
<p>Can there be a problem with my file type, namely what I wrote as: “_repair.seg.nrrd” in</p>
<p>MasterModelNode = slicer.util.loadNodeFromFile(file_complete, “_repair.seg.nrrd”, {}, returnNode=True) ?</p>
<p>I tried also “.seg.nrrd” and separately “.seg” or “.nrrd” but it makes no difference at all. It still shows the same error.</p>
<p>Best</p>

---

## Post #5 by @lassoan (2018-05-14 20:54 UTC)

<p>You can use <code>slicer.util.loadSegmentation</code> for loading a segmentation from file.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/a99595c98da13f87d16705ea5370edb3521179e2/Base/Python/slicer/util.py#L352-L354" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/a99595c98da13f87d16705ea5370edb3521179e2/Base/Python/slicer/util.py#L352-L354" target="_blank">Slicer/Slicer/blob/a99595c98da13f87d16705ea5370edb3521179e2/Base/Python/slicer/util.py#L352-L354</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="352" style="counter-reset: li-counter 351 ;">
<li>def loadSegmentation(filename, returnNode=False):</li>
<li>filetype = 'SegmentationFile'</li>
<li>return loadNodeFromFile(filename, filetype, {}, returnNode)</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Note that in recent nightly versions of Slicer, you can export segmentation directly to stl or obj files. See <a href="https://discourse.slicer.org/t/save-segmentation-directly-to-stl-or-obj-files/2428">Save segmentation directly to STL or OBJ files</a> post for details and <a href="http://apidocs.slicer.org/master/classvtkSlicerSegmentationsModuleLogic.html#a9578121589a3b5e20a05aa8dce33c642">API documentation</a> for description how it can be used from script.</p>

---

## Post #6 by @ladybug (2018-05-15 14:26 UTC)

<p>So I used slicer.util.loadSegmentation(filename, returnNode=False) as you suggested but the error remains - ‘method requires a VTK object’.<br>
Also I need to export the mesh surface as .ply file.<br>
Is it possible that I miss a line about a node, like getNode(‘Segmentation’)?<br>
Best!</p>

---

## Post #7 by @lassoan (2018-05-16 20:11 UTC)

<aside class="quote no-group" data-username="ladybug" data-post="6" data-topic="2646">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/46a35a/48.png" class="avatar"> ladybug:</div>
<blockquote>
<p>So I used slicer.util.loadSegmentation(filename, returnNode=False) as you suggested but the error remains - ‘method requires a VTK object’.</p>
</blockquote>
</aside>
<p>What error, where? What command do you type exactly?</p>
<aside class="quote no-group" data-username="ladybug" data-post="6" data-topic="2646">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/46a35a/48.png" class="avatar"> ladybug:</div>
<blockquote>
<p>Also I need to export the mesh surface as .ply file.</p>
</blockquote>
</aside>
<p>If you need .ply export you cannot use the direct export feature but you need to use VTK writers. You can add a feature request to the <a href="https://issues.slicer.org">Slicer issue tracker</a> to implement .ply format export.</p>

---

## Post #8 by @ladybug (2018-05-17 09:31 UTC)

<p>This is my piece of code until it works:</p>
<pre><code>  def onExportButtonClicked(self):
    qt.QFileDialog.ShowDirsOnly)
    filename = qt.QFileDialog.getOpenFileName(self.parent, 'Open file', 'D:\\SlicerTest\\THA\\001\\preop\\CT', "All Files (*.nrrd)")
    print filename
    self.exportMesh(filename)
    print("Finished.")
    
  def exportMesh(self, filename):
    # Load segmentation (repair.seg.nrrd)
    slicer.app.processEvents()
    MasterModelNode = slicer.util.loadSegmentation(filename, returnNode=False)
    modelNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLModelHierarchyNode')
    slicer.modules.segmentations.logic().ExportAllSegmentsToModelHierarchy(MasterModelNode, modelNode)  
</code></pre>
<p>The error I get in Python Interactor in Slicer is as follows:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/3459359a8eda80f4f1cce12b5133716468c36f31.jpeg" data-download-href="/uploads/short-url/7t5XreQo6UybSRrfbRFtDN72xln.jpg?dl=1" title="error%20slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3459359a8eda80f4f1cce12b5133716468c36f31_2_690x91.jpg" alt="error%20slicer" data-base62-sha1="7t5XreQo6UybSRrfbRFtDN72xln" width="690" height="91" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3459359a8eda80f4f1cce12b5133716468c36f31_2_690x91.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/3459359a8eda80f4f1cce12b5133716468c36f31.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/3459359a8eda80f4f1cce12b5133716468c36f31.jpeg 2x" data-dominant-color="F3E8E8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error%20slicer</span><span class="informations">763×101 35.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Best</p>

---

## Post #9 by @pieper (2018-05-17 12:12 UTC)

<p>In cases like this you need to confirm line-by-line that you are getting the data you expect from the API, for example by adding print statements or executing the calls in the python console.</p>
<p>Here, you have the returnNode=False argument to the loadSegmentation call, but then try to use the MasterModelNode as a node, when it’s a boolean.</p>
<p>HTH,<br>
Steve</p>

---

## Post #10 by @lassoan (2018-05-17 13:46 UTC)

<p>This code snippet should do what you need:</p>
<pre><code>def onExportButtonClicked(self):
  filename = qt.QFileDialog.getOpenFileName(self.parent, 'Open file', 'D:\\SlicerTest\\THA\\001\\preop\\CT', "All Files (*.nrrd)")
  self.exportMesh(filename)

def exportMesh(self, filename):
  [success, segmentationNode] = slicer.util.loadSegmentation(filename, returnNode=True)
  segmentationNode.CreateClosedSurfaceRepresentation()
  segmentation=segmentationNode.GetSegmentation()
  for segmentIndex in range(segmentation.GetNumberOfSegments()):
    segmentID = segmentation.GetNthSegmentID(segmentIndex)
    polydata = segmentationNode.GetClosedSurfaceRepresentation(segmentID)
    writer = vtk.vtkPLYWriter()
    writer.SetInputData(polydata)
    writer.SetFileName(os.path.split(filename)[0]+"/"+segmentationNode.GetName()+"_"+segmentID)
    writer.Update()</code></pre>

---

## Post #11 by @ladybug (2018-05-18 11:36 UTC)

<p>Thank you so much for your help <a class="mention" href="/u/lassoan">@lassoan</a> ! Of course everything works perfectly now.<br>
Best regards</p>

---
