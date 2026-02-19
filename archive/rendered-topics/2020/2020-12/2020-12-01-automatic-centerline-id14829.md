---
topic_id: 14829
title: "Automatic Centerline"
date: 2020-12-01
url: https://discourse.slicer.org/t/14829
---

# Automatic centerline

**Topic ID**: 14829
**Date**: 2020-12-01
**URL**: https://discourse.slicer.org/t/automatic-centerline/14829

---

## Post #1 by @Daniele_Morbidelli (2020-12-01 15:55 UTC)

<p>Hi All,</p>
<p>is there a way to generate the centerline automatically?<br>
In my case I have a geometry with always one input and 4 outputs.</p>

---

## Post #2 by @pieper (2020-12-01 18:46 UTC)

<p>Hi - you can use the VMTK extension for that.</p>

---

## Post #3 by @lassoan (2020-12-03 06:39 UTC)

<p>This short video should get you started:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="yi07mjr3JeU" data-video-title="New vessel branch extraction module for 3D Slicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=yi07mjr3JeU" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/yi07mjr3JeU/maxresdefault.jpg" title="New vessel branch extraction module for 3D Slicer" width="" height="">
  </a>
</div>

<p>If everything works well from the GUI but you need automated processing then you can switch to Python to use the underlying VMTK package directly.</p>

---

## Post #4 by @jeffc (2021-01-27 14:41 UTC)

<p>To follow on from Daniele’s question, is there a VMTK package with Python which allows you to calculate the centreline completely automatically, without setting seed points? So far I’ve been unable to find an approach to do this.</p>
<p>Thanks,</p>
<p>Jeff.</p>

---

## Post #5 by @lassoan (2021-01-27 14:44 UTC)

<p>Yes, centerline extraction works completely automatically. It requires two clicks (click “Auto-detect” then click “Apply”), so that you have a chance to add/remove endpoints, but if you don’t want this then just click the two buttons and you are done.</p>

---

## Post #6 by @chir.set (2021-01-27 15:14 UTC)

<p>While not replying directly to your question, I wish to know why is it felt so cumbersome to place a few endpoints on a model to extract the exact centerline of a targeted portion of a segment ? This allows you to be in control of what you’re doing.</p>

---

## Post #7 by @jeffc (2021-01-27 15:39 UTC)

<p>Thanks Andras. So far I’ve been using vmtkcenterlines via PypePad so am excited to try this. Thanks</p>

---

## Post #8 by @jeffc (2021-01-27 15:42 UTC)

<p>Hey, great question and I do agree that that would be ideal.<br>
I’m making a fully automated clinician-oriented tool where the clinician can input raw CT images and we output useful metrics for the medical conditions we’re interested in. I’ve got the segmentation fully automated and would be ideal to automate this portion of the work too. I have my vmtk pipeline working great with just this one stage of intervention so we’ll see how well the fully-automated version can compare <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #9 by @jeffc (2021-01-28 14:27 UTC)

<p>Hi Andras, I’m pleased to now have my workflow now working as a .py script. At the centreline extraction stage I’m using “vmtkcenterlines” but I don’t see any kind of “Auto-detect” prompt or button appearing? Can you please confirm if I’m using the wrong command or otherwise missing something? Thanks</p>

---

## Post #10 by @lassoan (2021-01-28 14:29 UTC)

<p>It is in Extract Centerline module:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3ffa2b86004d0425b243b090cb120fcb813e31bc.png" alt="image" data-base62-sha1="97Y4ba6PQBNR9cgra8VBFhcLApS" width="543" height="402"></p>

---

## Post #11 by @jeffc (2021-01-28 14:33 UTC)

<p>Thanks so much for such a quick reply! I think perhaps I misunderstood the capabilities: I was hoping to run a script from the command line, completely avoiding the need to use 3DSlicer or other programs. Is this not possible?</p>
<p>I have my script working (without needing to enter 3DSlicer) but there a few points which require manual intervention which I’m currently trying to remove. Is it possible using pypes to use this kind of auto-detect functionality or must that be done in 3DSlicer? Thanks</p>

---

## Post #12 by @lassoan (2021-01-28 14:44 UTC)

<p>You can have a look at the source code of this module, it is a pure Python script. You can either cop-paste just the parts that you need into your current script or use the code as is.</p>
<p>If you want to use the entire module as is, then you need to use Slicer’s virtual Python environment, but you need to use <em>some</em> Python environment anyway, so why not use Slicer’s? You can pip install any Python packages into it the same way as into any other. The Python environment is available without showing any GUI, so you can run your Python script with <code>Slicer --no-main-window --python-script path/to/myscript.py</code> as you would do it with <code>python path/to/myscript.py</code> in another Python environment.</p>
<p>There are Slicer docker images that you can use (you may need to add a step to install SlicerVMTK, but probably that’s all), so it all becomes a single command on the command-line. You can also run Slicer as a web service, so that you can use any of its features remotely, from a web or mobile application via a REST API. If you are developing a desktop application then probably you could save enormous amount of software development, maintenance, and support time by building your application based on Slicer (replacing the top-level GUI with your custom UI layer - this is how most companies develop their Slicer-based medical imaging products).</p>
<p>Also note that automated processing workflows can never guarantee 100% success rate. In medical applications, the typical target for automated processing success rate is 95% because there are always variability between patients, in imaging, etc. In some cases, maybe you can achieve 99%. But you cannot afford to errors slip through for a few percent of your patients. Therefore, you always need a GUI (for approval/quality assurance) and a way to manually correct those 5% of cases where automation does not provide perfect results.</p>

---

## Post #13 by @jeffc (2021-01-28 15:33 UTC)

<p>Thanks again Andras, this is extremely useful and valuable advice.<br>
My background is not in coding so it’ll take me a little time to digest all of this information and put it into practice. I have a very simple script in pypepad which works great for my vmtk operations, I’m hoping I can get this working without too much trouble, either way I appreciate you being on hand to help!</p>
<p>Thanks also for the warning about automated workflows, I’m definitely taking that advice on board and we already plan to include a gui with the option for manual intervention if necessary.</p>

---

## Post #14 by @lassoan (2021-01-28 16:26 UTC)

<p>If you have not invested a lot of time into developing your application yet then it is a perfect time to make a decision about switching to a proper medical imaging application platform, which can drive your entire clinical workflow: getting the input images (via DICOM files or networking), specifying inputs, running processing, showing results, allowing users to make manual adjustments, generating structured reports and saving/sending it via DICOM or other formats. Slicer provides 99% of all these features, so you can focus on developing your custom processing workflow, underlying custom algorithms (if needed), and design a convenient custom GUI.</p>
<p>If you write a bit more about what your overall goal is then we can make recommendations about how to achieve it. We are of course all like Slicer so we will be somewhat biased towards recommending it in general, but we also friends with developers of other web and desktop medical imaging platforms (OHIF, MITK, Mevis, etc.) so if you tell us specific requirements then we may be able to guide you in the right direction.</p>

---

## Post #15 by @jeffc (2021-02-01 08:54 UTC)

<p>Thank you Andras!<br>
I have already developed the segmentation algorithm workflow so now it is just the centreline and geometry analysis I definitely need to tackle. The project I am working on is just a pilot study so it doesn’t need to be perfect or flashy but of course it would be good to build a solid foundation using the best tools available. I appreciate your comment about using slicer or similar as the platform, I’d certainly like to explore the capabilities if it could be quick to try. Quite easily I could likely wrap up what I’ve got and incorporate it in, though again I am not a programming-whizz!</p>
<p>The workflow is as follows:</p>
<ul>
<li>Import images</li>
<li>Use segmentation script I’ve already fine-tuned and want to continue using. Exports segmented .nii.gz</li>
<li>Then the bit I’ve been working on recently: using vmtk to extract a .dat of the vessel diameter fully automatically. More details on that further down.</li>
<li>Finally to create a report with visuals and stating the maximum diameter of the segmented anatomy. Again I’ve already got a basic version of this but would be great to use some of what slicer may have available.</li>
</ul>
<p>So I’d be interested potentially in using the slicer platform but equally for now simply want to get the bit I’ve been doing in vmtk working automatically so that I have at least a basic version of whole automated pipeline. There are just two manual intervention steps I’d like to solve in the first instance, one of them (thresholding) should be I can select the same settings each time, whereas the centreline seed points was the more difficult step and the reason for my initial post.</p>
<p>My vmtk script is quite simple and could be further streamlined but here are the steps I’m carrying out:<br>
<span class="hashtag">#Threshold</span> &amp; create surface mesh:<br>
vmtklevelsetsegmentation -ifile “data_file” --pipe vmtkmarchingcubes -i @.o -ofile Sx_1thresh.vtp</p>
<p><span class="hashtag">#Computer</span> centrelines combined with viewer:<br>
vmtksurfacereader -ifile Sx_1thresh.vtp --pipe vmtkcenterlines --pipe vmtkrenderer --pipe vmtksurfaceviewer -opacity 0.25 --pipe vmtksurfaceviewer -i <span class="mention">@vmtkcenterlines.o</span> -array MaximumInscribedSphereRadius -ofile Sx_2centrelines.vtp</p>
<p><span class="hashtag">#Compute</span> centre-line geometry<br>
vmtkcenterlinegeometry -ifile Sx_2centrelines.vtp -smoothing 1 -ofile Sx_3clgeo.vtp<br>
vmtkcenterlinegeometry -ifile Sx_2centrelines.vtp -smoothing 1 -ofile Sx_3clgeodat.dat</p>
<p>This week I want to try your suggestions from earlier in the thread but again must state that I’m trying to at least give the option for a fully-automated script with no user intervention necessary.</p>
<p>Thanks in advance, I very much appreciate your help!!</p>

---

## Post #16 by @lassoan (2021-02-01 15:13 UTC)

<p>You can find the automatic endpoint detection implementation in <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/3787ea4a300da28ec5f0824f0715f2713b631155/ExtractCenterline/ExtractCenterline.py#L323">onAutoDetectEndPoints</a> method. It has some code to get/put VTK data objects from/to MRML nodes, but you can ignore those and just work with the VTK data objects.</p>

---

## Post #17 by @jeffc (2021-10-20 16:49 UTC)

<p>Hi Andras,<br>
I’m starting to pick up this piece of work again and have been running some tests within Slicer’s python environment. I can load volumes and models, carry out thresholds etc all with the centralised Slicer functions but I am now stuck at how to access/use the vmtk functions as mentioned in this thread within the slicer environment.</p>
<p>For example I can load my model with:<br>
slicer.util.loadModel(file)</p>
<p>But I can’t for the life of me figure out the equivilant command to use, for example, the extract centreline and autodetect end points functions as discussed earlier in this thread? It is certainly my lack of coding experience letting me down. Any help you can provide would be very much appreciated. Thanks in advance</p>

---

## Post #18 by @lassoan (2021-10-20 18:22 UTC)

<p>You can use the automatic test of the Extract Centerline module as an example of how to use the module from a Python script:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/vmtk/SlicerExtension-VMTK/blob/7da69e6134a974be14482463c573e6aacac1cd5e/ExtractCenterline/ExtractCenterline.py#L1157-L1188">
  <header class="source">

      <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/7da69e6134a974be14482463c573e6aacac1cd5e/ExtractCenterline/ExtractCenterline.py#L1157-L1188" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/7da69e6134a974be14482463c573e6aacac1cd5e/ExtractCenterline/ExtractCenterline.py#L1157-L1188" target="_blank" rel="noopener">vmtk/SlicerExtension-VMTK/blob/7da69e6134a974be14482463c573e6aacac1cd5e/ExtractCenterline/ExtractCenterline.py#L1157-L1188</a></h4>



  <pre class="onebox">    <code class="lang-py">
      <ol class="start lines" start="1157" style="counter-reset: li-counter 1156 ;">
          <li>import SampleData
</li>
          <li>inputVolume = SampleData.downloadFromURL(
</li>
          <li>  nodeNames='MRHead',
</li>
          <li>  fileNames='MR-Head.nrrd',
</li>
          <li>  uris='https://github.com/Slicer/SlicerTestingData/releases/download/MD5/39b01631b7b38232a220007230624c8e',
</li>
          <li>  checksums='MD5:39b01631b7b38232a220007230624c8e')[0]
</li>
          <li>self.delayDisplay('Finished with download and loading')
</li>
          <li>
</li>
          <li>inputScalarRange = inputVolume.GetImageData().GetScalarRange()
</li>
          <li>self.assertEqual(inputScalarRange[0], 0)
</li>
          <li>self.assertEqual(inputScalarRange[1], 279)
</li>
          <li>
</li>
          <li>outputVolume = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode")
</li>
          <li>threshold = 50
</li>
          <li>
</li>
          <li># Test the module logic
</li>
          <li>
</li>
          <li>logic = ExtractCenterlineLogic()
</li>
          <li>
</li>
          <li># Test algorithm with non-inverted threshold
</li>
      </ol>
    </code>
  </pre>

  This file has been truncated. <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/7da69e6134a974be14482463c573e6aacac1cd5e/ExtractCenterline/ExtractCenterline.py#L1157-L1188" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #19 by @jeffc (2021-10-21 09:03 UTC)

<p>Thanks as always for such a prompt response, Andras.<br>
I am still a little lost though, my background is not in coding!</p>
<p>When I enter</p>
<pre><code class="lang-auto">logic = ExtractCenterlineLogic()
</code></pre>
<p>I get:</p>
<pre><code class="lang-auto">NameError: name 'ExtractCenterlineLogic' is not defined 
</code></pre>
<p>I have used the module finder and see it states:<br>
Internal name: ExtractCenterline<br>
Type: Python Scripted Loadable</p>
<p>But I still for the life of me can’t figure out how I can access this within the slicer python environment. I have tried many combinations of " slicer." such as “slicer.ScriptedLoadableModule.” to then track it down but still have no luck. Could you please possibly provide an idiot-proof guidance?<br>
Thank you.</p>

---

## Post #20 by @lassoan (2021-10-22 05:55 UTC)

<p>In the test that I linked above, <code>ExtractCenterlineLogic</code> was in the same file, so there was no need to import it. However, if you want to use this class from another Python file then you need to import it, for example by adding this line:</p>
<pre><code>from ExtractCenterline import ExtractCenterlineLogic</code></pre>

---

## Post #21 by @jeffc (2021-10-22 09:28 UTC)

<p>Thanks Andras. For now I’m trying to use it from the Slicer python interactor and that line worked. It now works as expected with:</p>
<pre><code class="lang-auto">logic = ExtractCenterlineLogic()
</code></pre>
<p>But, once I enter:</p>
<pre><code class="lang-auto">logic.run(inputVolume, outputVolume, threshold, True)
</code></pre>
<p>I now get:</p>
<pre><code class="lang-auto">AttributeError: 'ExtractCenterlineLogic' object has no attribute 'run'
</code></pre>
<p>Any ideas?<br>
Apologies, I feel very feeble and don’t like having to ask for so much help but am otherwise completely lost and unable to make progress! My end goal is to simply feed in an already level set thresholded .vtp model and use the auto detect endpoints function to compute the centreline.<br>
Thanks</p>

---

## Post #22 by @jeffc (2021-10-28 14:07 UTC)

<p>Hi Andras, do you have any ideas for how to solve this current issue? I am hoping that what I want to do is quite simple but I’m struggling with the programmatic implementation.<br>
As before my end goal is to feed in an already level set thresholded .vtp model and use the auto detect endpoints function to find the endpoints then compute the centreline.<br>
I am able to feed in the .vtp model but I’m struggling with programming of the auto detect endpoints function.<br>
Any assistance you’re able to provide would be very much appreciated.</p>

---

## Post #23 by @mikebind (2021-10-28 18:52 UTC)

<p>It looks like the tests have not been updated since an earlier version of the module; the error message is correct that there is no run() method in ExtractCenterlineLogic.  There is an extractCenterline() method which takes as inputs surfacePolyData, endPointsMarkupsNode, and a curveSamplingDistance.  Here is what I think you need:</p>
<pre><code class="lang-auto">segmentationName = 'MySegmentationName' # replace with the name of your segmentation
segmentName = 'MySegmentName' # replace with the name of the segment you want to find the centerline of
segmentationNode = slicer.util.getNode(segmentationName)
segmentID = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName(segmentName)

import ExtractCenterline
extractLogic = ExtractCenterline.ExtractCenterlineLogic()

# Preprocess the surface
inputSurfacePolyData = extractLogic.polyDataFromNode(segmentationNode, segmentID)
targetNumberOfPoints = 5000.0
decimationAggressiveness = 4 # I had to lower this to 3.5 in at least one case to get it to work, 4 is the default in the module
subdivideInputSurface = False
preprocessedPolyData = extractLogic.preprocess(inputSurfacePolyData, targetNumberOfPoints, decimationAggressiveness, subdivideInputSurface)

# Auto-detect the endpoints
endPointsMarkupsNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode", "Centerline endpoints")
networkPolyData = extractLogic.extractNetwork(preprocessedPolyData, endPointsMarkupsNode)
startPointPosition=None
endpointPositions = extractLogic.getEndPoints(networkPolyData, startPointPosition)
endPointsMarkupsNode.RemoveAllMarkups()
for position in endpointPositions:
  endPointsMarkupsNode.AddControlPoint(vtk.vtkVector3d(position))

# Extract the centerline
centerlineCurveNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsCurveNode", "Centerline curve")
centerlinePolyData, voronoiDiagramPolyData = extractLogic.extractCenterline(preprocessedPolyData, endPointsMarkupsNode)
centerlinePropertiesTableNode = None
extractLogic.createCurveTreeFromCenterline(centerlinePolyData, centerlineCurveNode, centerlinePropertiesTableNode)

</code></pre>
<p>After you run this, the centerline should be in <code>centerlineCurveNode</code>, and the auto-detected endpoints should be in <code>endPointsMarkupsNode</code>.  I don’t know if the preprocessing step is strictly necessary (it seems like you may know more about the inner workings of VMTK than I do), but it seems recommended. To get this code snippet, I tried to pull the relevant lines out of a few functions in the ExtractCenterlineLogic class (<a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/3787ea4a300da28ec5f0824f0715f2713b631155/ExtractCenterline/ExtractCenterline.py#L378" class="inline-onebox">SlicerExtension-VMTK/ExtractCenterline.py at 3787ea4a300da28ec5f0824f0715f2713b631155 · vmtk/SlicerExtension-VMTK · GitHub</a>).  I have not tried running the auto-detect endpoints this way, but I have done the centerline extraction with supplied endpoints using VMTK using the above methods in one of my own python modules.</p>

---

## Post #24 by @jeffc (2021-10-29 14:36 UTC)

<p>Mike, thank you so much!<br>
I’m having a few hiccups getting this to completely work but it is a very useful starting point and I’m much further along than I was before, so thank you. I’m working to get it all ironed out now and hopefully have my first automated centerlines produced soon <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"><br>
Thanks again</p>

---

## Post #25 by @kayarre (2021-11-04 20:57 UTC)

<p>Another approach I have used is with a surface mesh that is open at each place I would like there to be centerline seed. vmtk can detect the centroid of each open region and provide the seed location.</p>

---

## Post #26 by @Jebsta (2023-08-15 12:38 UTC)

<p>This discussion was quiet helpful for me.<br>
But i get stuck at the part where teh slicer environment is used.<br>
I already have a quiet sufisticated virtual environment for a project and i also need the automatic centerline extraction.</p>
<p>Is there a way to get “slicer” into a already existing venv, or just use parts of the extionsion?</p>
<p>or is it possible to pass the pype the point coordinates manually?</p>

---

## Post #27 by @pieper (2023-08-15 13:38 UTC)

<p>You can’t directly use Slicer’s python modules in another python interpreter, but it should be easy to move data back and forth through files or other methods.</p>

---

## Post #28 by @MuckYu (2024-02-20 18:44 UTC)

<p>Thanks! This is working quite well on my end.</p>
<p>I have one issue though.</p>
<p>In some test models - when I am using the “manual” centerline method with the Slicer UI. When I click the Auto-detect button for the points. The first time it will put the points at not so great locations. But when I press the button again it puts the endpoints at the correct locations.<br>
(And when I press again a few times - always the same location as the second one)</p>
<p>Now when I use the script - it puts the endpoints at the location as when I clicked the button the first time. How can I “repeat” the endpoint selection so that it puts them like the second button click?</p>
<p>I already tried to just repeat the code but that did not work.</p>

---

## Post #29 by @mikebind (2024-02-26 19:33 UTC)

<p>Sorry, I’m not sure why this happens.  I guess maybe the first time the endpoints are located on a non-preprocessed surface, and the pre-processed surface is also generated, then maybe for the second click the endpoints are located using the preprocessed surface?  If that were the case, then you might be able to get the result you want by doing the pre-processing step before finding the endpoints, and then making sure to include the pre-processed surface as an input.  If that’s not what is going on, then I don’t really have any other ideas about what might cause that behavior.</p>

---

## Post #30 by @MuckYu (2024-02-29 12:19 UTC)

<p>Okay understood - I will try around a bit more.</p>
<p>One other question - right now the script is using the autodetect points feature.<br>
How can I specify my own point coordinates in there?<br>
Do they need to be in a specific format?</p>

---

## Post #31 by @MuckYu (2024-02-29 17:21 UTC)

<p>I was able to place the endpoints like this now:</p>
<blockquote>
<p>endpoint1 = [16.676, 40.6308, 68.4079]<br>
endpoint2 = [-17.6128, -45.0295, -65.3733]</p>
<p>selected_endpointPositions = [endpoint1, endpoint2 ]</p>
<p>selectedEndPointsNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLMarkupsFiducialNode”, “Selected Endpoints”)</p>
<p>selectedEndPointsNode.RemoveAllControlPoints()<br>
for position in selected_endpointPositions:<br>
selectedEndPointsNode.AddControlPoint(vtk.vtkVector3d(position))</p>
<p>centerlinePolyData, voronoiDiagramPolyData = extractLogic.extractCenterline(preprocessedPolyData, selectedEndPointsNode)</p>
</blockquote>
<p>But I am getting the following error:</p>
<blockquote>
<p>[VTK] Warning: In vtkvmtkSteepestDescentLineTracer.cxx, line 213</p>
<p>[VTK] vtkvmtkSteepestDescentLineTracer (00000201FB689510): Can’t find a steepest descent edge. Target not reached.</p>
</blockquote>
<p>When I select points manually from the dropdown in the UI it works just fine.<br>
Is there something I am missing?</p>
<p>EDIT: Actually it seems it can only detect the network curve when I try it manually?<br>
(how can I do it with python?)</p>
<p>But not the “Tree curve”?</p>

---

## Post #32 by @mikebind (2024-02-29 19:33 UTC)

<p>I would recommend that you take a look at exactly how it is done in ExtractCenterline.py.  I know that the final centerline endpoints lie on the voronoi medial surface even when the input endpoints are not on this surface; perhaps there is a preprocessing step which finds the closest points on the voronoi medial surface to your selected endpoints and substitutes those before passing to extractLogic.extractCenterline().  All the steps in the processing that you can achieve via the GUI are definitely possible to achieve using python, because the module the GUI is running is a python scripted module. I don’t have time to dig into the code at the moment, so these are just suggestions from memory which I hope can be helpful to you.  I think the most productive path will be for you to examine ExtractCenterline.py in detail.  Good luck!</p>

---
