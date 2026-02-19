---
topic_id: 41099
title: "Vmtk Slicerextension Multiprocessing"
date: 2025-01-15
url: https://discourse.slicer.org/t/41099
---

# VMTK SlicerExtension Multiprocessing

**Topic ID**: 41099
**Date**: 2025-01-15
**URL**: https://discourse.slicer.org/t/vmtk-slicerextension-multiprocessing/41099

---

## Post #1 by @Tracy (2025-01-15 21:57 UTC)

<p>Hi,</p>
<p>I have a python pipeline that utilizes several functions, such as ExtractCenterline and ClipVessel, from the SlicerExtension-VMTK (<a href="https://github.com/vmtk/SlicerExtension-VMTK" class="inline-onebox" rel="noopener nofollow ugc">GitHub - vmtk/SlicerExtension-VMTK</a>) for analyzing vessel segmentation. Since I need to process each segment in the segmentation, I am interested in using multiprocessing to speed up the analysis.</p>
<p>I’ve tried using SlicerParallelProcessing (<a href="https://github.com/pieper/SlicerParallelProcessing/tree/master" class="inline-onebox" rel="noopener nofollow ugc">GitHub - pieper/SlicerParallelProcessing: Slicer modules for running subprocesses to operate on data in parallel</a>), but it doesn’t seem to work, possibly due to the presence of vtkMRMLNode in SlicerExtension-VMTK.</p>
<p>Is there any suggestion or other method to implement multiprocessing in this context?<br>
BTW, I am working with SlicerJupyter and the Slicer 5.6 environment.</p>
<p>Thank you so much!</p>
<p>Best,<br>
Tracy</p>

---

## Post #2 by @pieper (2025-01-15 22:04 UTC)

<p>By default the SlicerParallelProcessing just <a href="https://github.com/pieper/SlicerParallelProcessing/blob/master/Processes/Processes.py#L227">launches PythonSlicer</a> which is the same python shell as Slicer but without the modules or extensions.</p>
<p>You should be able to create a subshell that has all the paths defined so that VMTK logic libraries are included and can be used.  Perhaps <a href="https://github.com/Slicer/Slicer/blob/main/Base/Python/slicer/util.py#L3787"><code>lauchConsoleProcess</code></a>, but I haven’t tried.</p>

---

## Post #3 by @Tracy (2025-01-21 20:37 UTC)

<p>Hi Pieper,</p>
<p>Thanks for your advice.</p>
<p>I’m encountering an issue (which I believe is related to the environment) when trying to use launchConsoleProcess.</p>
<p>Here is the command</p>
<p>command = [<br>
‘PythonSlicer’, ‘test_script.py’,        # The Python interpreter and the script name<br>
‘–segmentationName’, ‘segment_merge.nii.gz’,<br>
‘–segmentName’, ‘Segment_1’,<br>
‘–centerlineName’, ‘test’,<br>
‘–point’, ‘145.66666666666666, 315.3333333333333, 301.6666666666667’     # Second 3D coordinate<br>
]</p>
<p>process = slicer.util.launchConsoleProcess(command)<br>
slicer.util.logProcessOutput(process)</p>
<p>When I use ‘python3’ as the executable, I get the error:<br>
<strong>ModuleNotFoundError: No module named numpy</strong><br>
Additionally, all the SlicerExtension-VMTK modules seem to be missing.</p>
<p>On the other hand, if I use ‘PythonSlicer’, I encounter this error:<br>
<strong>FileNotFoundError: [Errno 2] No such file or directory: ‘PythonSlicer’</strong></p>
<p>Do you have any suggestions for resolving these issues?<br>
If you need any further information, please let me know.<br>
Thanks a lot.</p>
<p>Best,<br>
Tracy</p>

---

## Post #4 by @pieper (2025-01-21 21:01 UTC)

<p>Try <code>launchConsoleProcess(["PythonSlicer"], useStartupEnvironment=False)</code></p>

---

## Post #5 by @Tracy (2025-01-21 21:25 UTC)

<p>Thanks for quick reply.</p>
<p>However, I face some other error (vtkMRMLNode)<br>
Please refer to the attached image.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/494f34f13d8d12361d0fc7bbccfc480d809769d6.png" data-download-href="/uploads/short-url/aswypXTILancs4zqmcyIekm3v4q.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/494f34f13d8d12361d0fc7bbccfc480d809769d6_2_690x294.png" alt="image" data-base62-sha1="aswypXTILancs4zqmcyIekm3v4q" width="690" height="294" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/494f34f13d8d12361d0fc7bbccfc480d809769d6_2_690x294.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/494f34f13d8d12361d0fc7bbccfc480d809769d6_2_1035x441.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/494f34f13d8d12361d0fc7bbccfc480d809769d6.png 2x" data-dominant-color="F7DDDD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1239×529 87.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here is my function if useful<br>
def centerline_extraction(segmentationName, segmentName, centerlineName, points=None):</p>
<pre><code>segmentationNode = slicer.util.getNode(segmentationName)
segmentID = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName(segmentName)

# Init the VMTK ExtracCenterline class
extractLogic = ExtractCenterline.ExtractCenterlineLogic()

# Preprocess the surface
inputSurfacePolyData = extractLogic.polyDataFromNode(segmentationNode, segmentID)
targetNumberOfPoints = 5000.0
decimationAggressiveness = 3.5
subdivideInputSurface = False
preprocessedPolyData = extractLogic.preprocess(inputSurfacePolyData, targetNumberOfPoints, decimationAggressiveness, subdivideInputSurface)

endPointsMarkupsNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode", "Centerline endpoints")
if not np.any(points):
    # Auto-detect the endpoints      
    networkPolyData = extractLogic.extractNetwork(preprocessedPolyData, endPointsMarkupsNode)
    startPointPosition=None
    endpointPositions = extractLogic.getEndPoints(networkPolyData, startPointPosition)
    endPointsMarkupsNode.RemoveAllMarkups()
    for position in endpointPositions:
      endPointsMarkupsNode.AddControlPoint(vtk.vtkVector3d(position))

else:
    assert points.shape[1] == 3
    # Self define start and end points
    endPointsMarkupsNode.RemoveAllMarkups()
    for p in points:
        endPointsMarkupsNode.AddControlPoint(vtk.vtkVector3d(p))
    
        #endPointsMarkupsNode.AddControlPoint(vtk.vtkVector3d(points[-1]))

# Extract the centerline
curveName = centerlineName+"Curve"
modelName = centerlineName+"Model"

centerlineCurveNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsCurveNode", curveName)

centerlinePolyData, voronoiDiagramPolyData = extractLogic.extractCenterline(preprocessedPolyData, endPointsMarkupsNode)
centerlinePropertiesTableNode = None
extractLogic.createCurveTreeFromCenterline(centerlinePolyData, centerlineCurveNode, centerlinePropertiesTableNode)

centerlineModelNode = slicer.modules.models.logic().AddModel(centerlinePolyData)
centerlineModelNode.SetName(modelName)

return centerlineCurveNode, centerlineModelNode
</code></pre>

---

## Post #6 by @pieper (2025-01-21 21:34 UTC)

<p>PythonSlicer is more just a python shell and not a full instance of Slicer.  Maybe for what you want you can use <code>Slicer --no-main-window</code>.  Since it runs the application you’ll need to explicitly <code>exit()</code> when you are done processing.</p>

---

## Post #7 by @Enkh-Orchlon_Batbaya (2025-01-22 00:54 UTC)

<p>Dear Steve Pieper,<br>
My writing is not belong to this conversation. Could you kindly review and approve my post request? I am new to the community and currently seeking assistance. Thank you for your time and understanding.</p>

---

## Post #8 by @Tracy (2025-01-28 20:40 UTC)

<p>Thanks for suggestion Pieper. It works with subprocess.Popen()<br>
Just sharing this for anyone else who might encounter the same issue.</p>
<p>command = [‘Slicer-5.6.2-linux-amd64/Slicer’, ‘–no-main-window’,<br>
‘–python-script’, ‘test.py’,<br>
‘–segmentation_path’, segmentation_path,<br>
‘–output_path’, output_path<br>
]</p>
<p>process_dic = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)</p>

---
