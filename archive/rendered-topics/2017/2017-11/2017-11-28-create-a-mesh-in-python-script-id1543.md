---
topic_id: 1543
title: "Create A Mesh In Python Script"
date: 2017-11-28
url: https://discourse.slicer.org/t/1543
---

# Create a mesh in python script

**Topic ID**: 1543
**Date**: 2017-11-28
**URL**: https://discourse.slicer.org/t/create-a-mesh-in-python-script/1543

---

## Post #1 by @Frederic (2017-11-28 16:31 UTC)

<p>Hi all,<br>
Is-it possible since a “head_T1.nii” to mesh only the scalp by “Segment editor tool” from Python scripts?<br>
Thanks in advance,<br>
Frederic</p>

---

## Post #2 by @cpinter (2017-11-28 16:49 UTC)

<p>You need to be able to come up with a quasi-automatic way of doing it first. Do you know what effects would you use, in what order, and with what parameters?</p>
<p>Then it will be possible to automatize it from python, yes.</p>

---

## Post #3 by @lassoan (2017-11-28 20:48 UTC)

<p>Once you know what effects you’ll use and how, follow these examples for running Segment Editor effects from script: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script</a></p>

---

## Post #4 by @Frederic (2017-11-30 17:17 UTC)

<p>Thanks to both of you.<br>
I would like to use 1/ threshold effect, with range from 110 to 400 and with default to other parameters and 2/ Smoothing with Gaussian with 2 mm sd.<br>
So It would be:<br>
segmentEditorWidget.setActiveEffectByName(“Threshold”, 110,400)<br>
segmentEditorWidget.setActiveEffectByName(“Smmoting”,"Gaussian ", 2)</p>
<p>Two more question, please.<br>
Is there in 3dslicer, a RAS to MNI coordinate conversion function?<br>
Is there a button to trigger the shift key linked motion?</p>
<p>Thanks, once again.</p>

---

## Post #5 by @lassoan (2017-11-30 17:45 UTC)

<aside class="quote no-group" data-username="Frederic" data-post="4" data-topic="1543">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/frederic/48/4907_2.png" class="avatar"> Frederic:</div>
<blockquote>
<p>So It would be:</p>
<p>segmentEditorWidget.setActiveEffectByName(“Threshold”, 110,400)</p>
<p>segmentEditorWidget.setActiveEffectByName(“Smmoting”,"Gaussian ", 2)</p>
</blockquote>
</aside>
<p>It’s a couple of more lines (setActiveEffectByName only activates an effect). See the examples that I linked above.</p>
<aside class="quote no-group" data-username="Frederic" data-post="4" data-topic="1543">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/frederic/48/4907_2.png" class="avatar"> Frederic:</div>
<blockquote>
<p>Is there in 3dslicer, a RAS to MNI coordinate conversion function?</p>
</blockquote>
</aside>
<p>RAS is anatomical coordinate system (right-anterior-superior). What is MNI coordinate system?</p>
<aside class="quote no-group" data-username="Frederic" data-post="4" data-topic="1543">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/frederic/48/4907_2.png" class="avatar"> Frederic:</div>
<blockquote>
<p>Is there a button to trigger the shift key linked motion?</p>
</blockquote>
</aside>
<p>You can easily add a shortcut for jump to a current cursor position, just open the Python console and copy-paste these lines to make Ctrl+M jump to current slice position:</p>
<pre><code>def jumpToCursor():
  ras=[0,0,0]
  slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLCrosshairNode').GetCursorPositionRAS(ras)
  slicer.modules.markups.logic().JumpSlicesToLocation(ras[0], ras[1], ras[2], slicer.vtkMRMLCrosshairNode.JumpSlice)

shortcut = qt.QShortcut(slicer.util.mainWindow())
shortcut.setKey(qt.QKeySequence("Ctrl+M"))
shortcut.connect( 'activated()', jumpToCursor )
</code></pre>
<p>If you want this feature permanently then add it to your application startup script (edit it in menu: Edit /  Application settings / Application startup script).</p>

---

## Post #6 by @Frederic (2017-12-01 14:53 UTC)

<p>Thanks once again.</p>
<ol>
<li>Ok for the “setActiveEffectByName”, I will try as soon as possible.</li>
<li>MNI coordinates is a normalized coordinates (explain here: <a href="http://neuroimage.usc.edu/brainstorm/CoordinateSystems" rel="nofollow noopener">http://neuroimage.usc.edu/brainstorm/CoordinateSystems</a>)</li>
<li>Thanks for this script!</li>
</ol>

---

## Post #7 by @lassoan (2017-12-01 16:53 UTC)

<p>From <a href="http://neuroimage.usc.edu/brainstorm/CoordinateSystems#MNI_coordinates" class="inline-onebox">CoordinateSystems - Brainstorm</a> website:</p>
<blockquote>
<p>To be able to get “MNI coordinates” for individual brains, an extra step of normalization is required.<br>
The method we use in Brainstorm is based on an affine co-registration with the MNI ICBM152 template from the SPM software.</p>
</blockquote>
<p>This means you can easily get these coordinates in Slicer. You just have to download MNI ICBM152 image and register it to your volume in Slicer. You can either use “General registration (BRAINS)” module or install SlicerElastix extension and use “General registration (Elastix)” module. For Elastix, I think default configuration file are available for rigid or b-spline transforms, so you need to change ElastixParameterSetDatabase.xml to create a preset that uses Parameters_Affine.txt (you can copy-paste the “generic rigid” preset and change Parameters_Rigid.txt to Parameters_Affine.txt).</p>

---

## Post #8 by @Frederic (2017-12-04 17:44 UTC)

<p>Thanks Andras,<br>
It works fine, but the registration is very rigid.</p>

---

## Post #9 by @lassoan (2017-12-04 18:11 UTC)

<p>“generic rigid” preset uses rigid transform. If you need affine or warping transform then you have to modify registration parameter files as I described above.</p>

---

## Post #10 by @Frederic (2017-12-05 16:36 UTC)

<p>Perfect thanks Andras.<br>
is-it possible to make this procedure by a Python script?</p>

---

## Post #11 by @lassoan (2017-12-05 17:06 UTC)

<p>Python scripting is not needed. You can edit preset files directly using a text editor.</p>
<p>Of course, everything is exposed to Python, so if you need to run registration from your module then you can do that. An example for that is <a href="https://github.com/moselhy/SlicerSequenceRegistration">Sequence Registration</a> module, which uses SlicerElastix internally for registering different time points of a 4D volume to each other.</p>

---

## Post #12 by @Frederic (2017-12-06 11:52 UTC)

<p>Yes, I have change manually the xml file. <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=5" title=":wink:" class="emoji" alt=":wink:"><br>
My python script does no work and I do not understand why, could you help me please?</p>
<pre><code>import Elastix
FixedVolume= slicer.util.loadVolume('avg152T1.nii')
MovingVolume= slicer.util.loadVolume('t0697_t1_s03.nii')
outputVolume = slicer.vtkMRMLScalarVolumeNode()
slicer.mrmlScene.AddNode(outputVolume)
outputVolume.CreateDefaultDisplayNodes()
logic = Elastix.ElastixLogic()
RegistrationPresets_ParameterFilenames = 5
parameterFilenames = logic.getRegistrationPresets()[0][RegistrationPresets_ParameterFilenames]
logic.registerVolumes(FixedVolume, MovingVolume, parameterFilenames = parameterFilenames, outputVolumeNode = outputVolume)</code></pre>

---

## Post #13 by @lassoan (2017-12-06 12:28 UTC)

<p>What happens? Do you get any error message?</p>

---

## Post #14 by @Frederic (2017-12-06 12:54 UTC)

<p>The error is:</p>
<pre><code class="lang-auto">&gt; Traceback (most recent call last):
&gt;   File "&lt;console&gt;", line 1, in &lt;module&gt;
&gt;   File "C:/Users/briend/AppData/Roaming/NA-MIC/Extensions-26489/SlicerElastix/lib/Slicer-4.8/qt-scripted-modules/Elastix.py", line 554, in registerVolumes
&gt;     slicer.util.saveNode(volumeNode, filePath, {"useCompression": False})
&gt;   File "C:\Program Files\Slicer 4.8.0\bin\Python\slicer\util.py", line 433, in saveNode
&gt;     properties["nodeID"] = node.GetID();
&gt; AttributeError: 'bool' object has no attribute 'GetID'
</code></pre>

---

## Post #15 by @lassoan (2017-12-06 14:55 UTC)

<p>The problem is that <code>loadVolume</code> by default returns success=True/False. See an example for getting the loaded volume node here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Load_volume_from_file">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Load_volume_from_file</a></p>

---

## Post #16 by @Frederic (2017-12-06 15:21 UTC)

<p>Thanks Andras.<br>
The correct scipt (which works well) is thus:</p>
<blockquote>
<p>import Elastix<br>
FixedVolume= slicer.util.loadVolume(‘L:/briend/Olivier_Slicer_try1/avg152T1.nii’, returnNode=True)<br>
n=slicer.util.getNode(‘avg15*’)<br>
MovingVolume= slicer.util.loadVolume(‘L:/briend/Olivier_Slicer_try1/t0697_t1_s03.nii’, returnNode=True)<br>
m=slicer.util.getNode(‘t06*’)<br>
outputVolume = slicer.vtkMRMLScalarVolumeNode()<br>
slicer.mrmlScene.AddNode(outputVolume)<br>
outputVolume.CreateDefaultDisplayNodes()<br>
logic = Elastix.ElastixLogic()<br>
RegistrationPresets_ParameterFilenames = 5<br>
parameterFilenames = logic.getRegistrationPresets()[0][RegistrationPresets_ParameterFilenames]<br>
logic.registerVolumes(n, m, parameterFilenames = parameterFilenames, outputVolumeNode = outputVolume)</p>
</blockquote>

---

## Post #17 by @Frederic (2017-12-07 15:09 UTC)

<p>I am confuse to ask you all theses questions, but I do not arrive to create my mesh.<br>
Nothing happen after my script:</p>
<pre><code class="lang-auto">import SampleData
sampleDataLogic = SampleData.SampleDataLogic()
masterVolumeNode = sampleDataLogic.downloadMRBrainTumor1()

# Create segmentation
segmentationNode = slicer.vtkMRMLSegmentationNode()
slicer.mrmlScene.AddNode(segmentationNode)
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)
#segmentationNode.AddSegmentFromClosedSurfaceRepresentation(masterVolumeNode, "skin", [1,0,1]) **# I do not understand how to assign my volume here**

# Create segment editor to get access to effects
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()
slicer.mrmlScene.AddNode(segmentEditorNode)
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)

# Run segmentation
segmentEditorWidget.setActiveEffectByName("Threshold")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("MinimumThreshold",35)
effect.setParameter("MaximumThreshold",695)
segmentEditorWidget.setActiveEffectByName('Smooting')
effect.setParameter('Gaussian', 2)

effect.self().onPreview()
effect.self().onApply()

# Clean up
slicer.mrmlScene.RemoveNode(segmentEditorNode)

# Make segmentation results nicely visible in 3D
segmentationDisplayNode = segmentationNode.GetDisplayNode()
</code></pre>
<p><a class="mention" href="/u/lassoan">@lassoan</a> do you know why?<br>
Thanks in advance</p>

---

## Post #18 by @lassoan (2017-12-08 16:32 UTC)

<p>There were a couple of small issues. Here is a working version:</p>
<pre><code>import SampleData
sampleDataLogic = SampleData.SampleDataLogic()
masterVolumeNode = sampleDataLogic.downloadMRBrainTumor1()

# Create segmentation
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)
addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment("skin")

# Create segment editor to get access to effects
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)

# Thresholding
segmentEditorWidget.setActiveEffectByName("Threshold")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("MinimumThreshold","35")
effect.setParameter("MaximumThreshold","695")
effect.self().onApply()

segmentEditorWidget.setActiveEffectByName("Smoothing")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("SmoothingMethod", "MEDIAN")
effect.setParameter("KernelSizeMm", 11)
effect.self().onApply()

# Clean up
segmentEditorWidget = None
slicer.mrmlScene.RemoveNode(segmentEditorNode)

# Make segmentation results visible in 3D
segmentationNode.CreateClosedSurfaceRepresentation()

# Write to STL file
surfaceMesh = segmentationNode.GetClosedSurfaceRepresentation(addedSegmentID)
writer = vtk.vtkSTLWriter()
writer.SetInputData(surfaceMesh)
writer.SetFileName("c:/tmp/something.stl")
writer.Update()
</code></pre>
<p>For future reference: I’ve saved this example and will maintain it on <a href="https://gist.github.com/lassoan/1673b25d8e7913cbc245b4f09ed853f9">this page</a>.</p>

---

## Post #19 by @Frederic (2017-12-08 17:40 UTC)

<p>Once again, thanks <a class="mention" href="/u/lassoan">@lassoan</a>. Your generosity makes me blush.<br>
Little problem however, nothing happen by the smoothing parameter.</p>
<p>Then, how save this volume segmented (after Model Maker) in .stl format in python?<br>
Thanks in advance!</p>

---

## Post #20 by @lassoan (2017-12-08 18:30 UTC)

<p>If you use Segmentations, “model making” (and real-time updates to the generated 3D mesh) are done automatically. I’ve updated the code sample above to smooth with the correct parameter names and added STL export at the end.</p>

---

## Post #21 by @Frederic (2017-12-11 10:05 UTC)

<p>Thanks Andras, I owe you so much.</p>

---

## Post #22 by @Frederic (2017-12-12 17:50 UTC)

<p>Hi,<br>
Sorry for these 2 new questions:</p>
<ol>
<li>How to save fiducial (F.fcsv) in python?</li>
<li>With the wonderful <a href="https://gist.github.com/lassoan/1673b25d8e7913cbc245b4f09ed853f9" rel="noopener nofollow ugc">script</a> of <a class="mention" href="/u/lassoan">@lassoan</a>, I obtain great segmentation of my data (cf. my picture, left part), but I don’t know why there is some mistake during the saving of the stl (cf. my picture, rigth part). This mistake just occur with my data. Does someone have any idea what may cause this?</li>
</ol>
<p>Thanks in advance.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b6d4a3f495a4606a2a5ab363a2a3f36b12e5472.jpeg" data-download-href="/uploads/short-url/maY9XPhCutu7wiZGlQPnjjiCw0y.jpg?dl=1" title="problem_slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/9b6d4a3f495a4606a2a5ab363a2a3f36b12e5472_2_690x342.jpg" alt="problem_slicer" data-base62-sha1="maY9XPhCutu7wiZGlQPnjjiCw0y" width="690" height="342" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/9b6d4a3f495a4606a2a5ab363a2a3f36b12e5472_2_690x342.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/9b6d4a3f495a4606a2a5ab363a2a3f36b12e5472_2_1035x513.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/9b6d4a3f495a4606a2a5ab363a2a3f36b12e5472_2_1380x684.jpg 2x" data-dominant-color="5C6170"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">problem_slicer</span><span class="informations">1423×706 202 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #23 by @cpinter (2017-12-12 18:30 UTC)

<ol>
<li>You can use this function from slicer.util <a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L423-L439">https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L423-L439</a>
</li>
<li>There are holes in your segmentation. You’ll need to adjust the threshold parameters (likely reducing MinimumThreshold would help)</li>
</ol>

---

## Post #24 by @lassoan (2017-12-12 18:36 UTC)

<aside class="quote no-group" data-username="Frederic" data-post="22" data-topic="1543">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/frederic/48/4907_2.png" class="avatar"> Frederic:</div>
<blockquote>
<p>why there is some mistake</p>
</blockquote>
</aside>
<p>What mistake you are referring to?</p>

---

## Post #25 by @Frederic (2017-12-12 19:09 UTC)

<p>Thanks <a class="mention" href="/u/cpinter">@cpinter</a>.<br>
My data.stl was not like the segmentation mesh, they are all deformated (On my figure, the mesh and the data.stl are in the same point of view).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/677f06bdf711468707faf594c72c7993f90d2513.png" data-download-href="/uploads/short-url/eLzkAGZovUCazoJL65K1uagmWFJ.png?dl=1" title="77C3A3DB5AF54B56A741600A3E5A8000.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/677f06bdf711468707faf594c72c7993f90d2513.png" width="690" height="0" data-dominant-color="BFCDDB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">77C3A3DB5AF54B56A741600A3E5A8000.png</span><span class="informations">708×1 83 Bytes</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #26 by @cpinter (2017-12-12 19:29 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I think he’s referring to the artifacts in the grey model that are caused by the holes.</p>
<p><a class="mention" href="/u/frederic">@Frederic</a> In your screenshot it can be seen that the segmentation is not solid (see the holes I was talking about), and those show up inside the head, looking quite strange. Once you fill the holes by adjusting the threshold parameters (or just filling them manually first with a brush to test my theory), the mesh on the right should look fine.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d53f6a9d5c74243101fb56221e5c2e4f09932a4.jpeg" data-download-href="/uploads/short-url/hSHzDFPlzee0ZoNfaA3Y3JDMHwE.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/7d53f6a9d5c74243101fb56221e5c2e4f09932a4_2_690x342.jpg" alt="image" data-base62-sha1="hSHzDFPlzee0ZoNfaA3Y3JDMHwE" width="690" height="342" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/7d53f6a9d5c74243101fb56221e5c2e4f09932a4_2_690x342.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/7d53f6a9d5c74243101fb56221e5c2e4f09932a4_2_1035x513.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/7d53f6a9d5c74243101fb56221e5c2e4f09932a4_2_1380x684.jpg 2x" data-dominant-color="5D6070"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1423×706 214 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #27 by @Frederic (2017-12-13 11:23 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> I dont think that the cause is the holes, the segmentation of Andras script’s have holes too and the data.stl was fine.<br>
My script is the same that Andras, I have just change:</p>
<blockquote>
<p>effect.setParameter(“MinimumThreshold”,“100”)<br>
effect.setParameter(“MaximumThreshold”,“2000”)</p>
</blockquote>
<p>And one of my file was <a href="https://wetransfer.com/downloads/4dd4514bf5c74a3696387973e917d70720171213111128/f2ad0df71503377fea4807967eb4b46020171213111128/f8b608" rel="noopener nofollow ugc">here (link)</a>.</p>
<p>Could you try with this file please?</p>

---

## Post #28 by @cpinter (2017-12-13 16:03 UTC)

<p>The difference between the green and gray is that the green has full opacity, and the gray is semi-transparent, and full opacity hides the holes, semi-transparency lets them show. If you change the segmentation’s opacity to 50% or so, or change the model’s opacity to 100%, then they will look the same.</p>

---

## Post #29 by @Frederic (2017-12-13 16:36 UTC)

<p>Thanks <a class="mention" href="/u/cpinter">@cpinter</a> , but It’s not that. Below, on the left my data (opacity: 100%, the holes are always here), on the right, the data of the script of Andras (opacity: 70%, with holes too).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/17cd22c538d4fe7b9c803deca8e21dce8e8fc0be.jpeg" data-download-href="/uploads/short-url/3oytXLWT8UJPqtYQrPtajpNfQzY.jpg?dl=1" title="Sans titre" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/17cd22c538d4fe7b9c803deca8e21dce8e8fc0be_2_690x381.jpg" alt="Sans titre" data-base62-sha1="3oytXLWT8UJPqtYQrPtajpNfQzY" width="690" height="381" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/17cd22c538d4fe7b9c803deca8e21dce8e8fc0be_2_690x381.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/17cd22c538d4fe7b9c803deca8e21dce8e8fc0be_2_1035x571.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/17cd22c538d4fe7b9c803deca8e21dce8e8fc0be.jpeg 2x" data-dominant-color="515567"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Sans titre</span><span class="informations">1331×735 186 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #30 by @cpinter (2017-12-13 17:07 UTC)

<p>I see. The problem is the surface normals. If you change Visible Slides to “Back-facing” in the Models module, then it will show up the same way<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/acc77c135a6a6c2179963fb956c48742155162cb.png" alt="image" data-base62-sha1="oEtwat19JUa6Dlf0RcKaknj9n9V" width="387" height="128"></p>
<p>You can also fix the normals themselves in the Surface Toolbox module like this:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/9816bd4e056c72b070f5c93202c22caeede4da83.png" alt="image" data-base62-sha1="lHrigrRjPmHpps8Eno0S6y018BR" width="414" height="352"></p>

---

## Post #31 by @Frederic (2017-12-13 17:29 UTC)

<p>Great, you are right <a class="mention" href="/u/cpinter">@cpinter</a> ! really thanks!<br>
And how to access to is module in python (to perform that you say following the script of Andras) please?</p>

---

## Post #32 by @lassoan (2017-12-13 18:14 UTC)

<p>Surface Toolbox is a Python module, so you can copy-paste the <a href="https://github.com/Slicer/Slicer/blob/cb844150111d90c277843f46b3ea87f329fa216e/Modules/Scripted/SurfaceToolbox/SurfaceToolbox.py#L429-L436">few lines that updates the normal</a>.</p>

---

## Post #33 by @cpinter (2017-12-13 18:22 UTC)

<p>Yes. Unfortunately the module is poorly designed to be used more easily form the outside (for reference the “state” class is not exposed, and the UI widgets are not members).</p>
<p>Replace the last section of Andras’ code with this:</p>
<pre><code># Fix normals
surfaceMesh = segmentationNode.GetClosedSurfaceRepresentation(addedSegmentID)
normals = vtk.vtkPolyDataNormals()
normals.SetAutoOrientNormals(True)
normals.ConsistencyOn()
normals.SetInputData(surfaceMesh)
normals.Update()
surfaceMesh = normals.GetOutput()

# Write to STL file
writer = vtk.vtkSTLWriter()
writer.SetInputData(surfaceMesh)
writer.SetFileName("d:/something.stl")
writer.Update()</code></pre>

---

## Post #34 by @Frederic (2017-12-14 11:08 UTC)

<p>Thanks to both of you once again. <img src="https://emoji.discourse-cdn.com/twitter/clap.png?v=5" title=":clap:" class="emoji" alt=":clap:"></p>

---

## Post #35 by @Alexandra (2018-04-10 10:42 UTC)

<p>Hello,<br>
Thanks for thoses informations. Do you know how to get the model properties like volume, surface, etc. With a python script ?<br>
Is there a documentation for the python scripts?<br>
Thank you very much!</p>

---

## Post #36 by @cpinter (2018-04-10 13:47 UTC)

<p>You can use the Segment Statistics module to do that. See for example</p><aside class="quote quote-modified" data-post="1" data-topic="2140">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/brhoom/48/1228_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/using-segmentstatistics-module-in-python-script/2140">Using segmentstatistics module in python script</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Dear all, 
How can I call and use segmentstatistics module in a simple way. I tried this code but I get an error 
    volSeg  =  slicer.util.getNode('Segmentation')
    volInput =  self.inputSelector.currentNode() 

    segStat = slicer.modules.segmentstatistics.widgetRepresentation().self()
    segStat.grayscaleNode = volInput
    segStat.labelNode  = volSeg   
    segStat.onApply()
    segStat.onExportToTable()
    segTbl = slicer.util.getNode('Segmentation statistics*')

This is the error: 
S…
  </blockquote>
</aside>


---

## Post #37 by @Saima (2018-08-30 10:57 UTC)

<p>Hi Andras,<br>
I gone through the example segmention. I dont understand how to select the seed values? is it random selection? can it be automated as well?</p>
<p>tumorSeed.SetCenter(-6, 30, 28)<br>
backgroundSeedPositions = [[0,65,32], [1, -14, 30], [0, 28, -7], [0,30,64], [31, 33, 27], [-42, 30, 27]]</p>

---

## Post #38 by @lassoan (2018-08-30 11:36 UTC)

<p>You usually define seeds manually, using paint or draw effect. For fully automatic registration, you can define seeds on an atlas image; then you can transfer these seeds segments to a new image using registration (e. g., General registration (BRAINS) or General registration (Elastix) modules).</p>

---

## Post #39 by @lassoan (2019-04-11 13:58 UTC)

<p>A post was split to a new topic: <a href="/t/how-to-write-stl-from-dicom-slices/6468">How to write STL from dicom slices</a></p>

---
