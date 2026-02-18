# Creating a screenshot by script

**Topic ID**: 15328
**Date**: 2021-01-04
**URL**: https://discourse.slicer.org/t/creating-a-screenshot-by-script/15328

---

## Post #1 by @Justin (2021-01-04 11:25 UTC)

<p>Dear all,</p>
<p>I have a question concerning creating a screenshot using ScreenCapture.<br>
I found the relevant script on the repository on the website</p>
<pre><code>viewNodeID = 'vtkMRMLSliceNodeRed'
import ScreenCapture
cap = ScreenCapture.ScreenCaptureLogic()
view = cap.viewFromNode(slicer.mrmlScene.GetNodeByID(viewNodeID))
cap.captureImageFromView(view,sceneSaveDirectory + "/segmentation export.png")
</code></pre>
<p>(<code>sceneSaveDirectory</code> is defined previously to this section of the script)</p>
<p>When I paste this script in the interactor it works as expected<br>
However when I run this script as a part of a larger script (copy-pasted in the Python Interactor) it does not work.<br>
No error is shown, the screenshot is just not generated.</p>
<p>I tried running a <code>time.sleep(3)</code> before and after this section, but this does not fix the problem.<br>
If I paste each section of the script separately into the Python Interactor it <em>does</em> work, just not when I paste it as a whole.</p>
<p>Do you have a suggestion how to fix this?</p>
<p>Thanks in advance,<br>
Justin</p>

---

## Post #2 by @pieper (2021-01-04 13:58 UTC)

<p>You can try <code>slicer.app.processEvents()</code> instead.</p>

---

## Post #3 by @cpinter (2021-01-04 14:06 UTC)

<p>I find this quite strange. The script works for me in 4.11.20200930 and a recent preview as well on Windows. What Slicer version and operating system do you use?</p>

---

## Post #4 by @Justin (2021-01-04 14:51 UTC)

<p>Thanks for your reply!</p>
<p><a class="mention" href="/u/pieper">@pieper</a>: I tried switching the <code>time.sleep(3)</code> to <code>slicer.app.processEvents()</code> both before and after this script but that didn’t work. Was that a correct interpretation of your suggestion? (so that the script waits until it is finished processing, rather than just 3 seconds?)</p>
<p><a class="mention" href="/u/cpinter">@cpinter</a></p>
<p>I use Windows 10 and the Nightly slicer version of 2020-12-07<br>
As said above, this part of the script on its own works fine, but not as a part of a bigger script:</p>
<p>I load a CT-scan from the dicom library<br>
Then I use a script to rename the volume, create a segmentation. It then pauses so that I can manually segment everything and then the script continues to process the segmentations, save the scene and close. So basically I can process each scan by just pasting in the whole script.</p>
<p>I inserted the above script to be able to export a view of the segmentations, but it does not work as part of my bigger ‘workhorse’ script. (but does work when I just paste the lines above).</p>
<p>Hopefully that’s a better explanation of the situation.</p>

---

## Post #5 by @cpinter (2021-01-04 14:54 UTC)

<aside class="quote no-group" data-username="Justin" data-post="4" data-topic="15328">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/3ab097/48.png" class="avatar"> Justin:</div>
<blockquote>
<p>but not as a part of a bigger script</p>
</blockquote>
</aside>
<p>In this case a self-contained test case would help a lot.</p>

---

## Post #6 by @Justin (2021-01-04 17:56 UTC)

<p>This is an example where it does not work</p>
<pre><code>import time
import os

## Selecting and renaming the volume
masterVolumeNode=slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLScalarVolumeNode')

# Get patient's Name and rename the volume
instUids=masterVolumeNode.GetAttribute('DICOM.instanceUIDs').split()
filename=slicer.dicomDatabase.fileForInstance(instUids[0])
patientName=slicer.dicomDatabase.fileValue(filename,'0010,0010')
masterVolumeNode.SetName(patientName + '_CWK') 

## part 1: creating segments
# Create segmentation
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.SetName('test segmentation')
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)

# Create segments by thresholding
segmentsFromHounsfieldUnits = [
    ["A", -29, 150],
    ["B", -29, 150],
    ["C", -29, 150] ]
for segmentName, thresholdMin, thresholdMax in segmentsFromHounsfieldUnits:
    # Create segment
    addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment(segmentName)

# Delete temporary segment editor
segmentEditorWidget = None

# Select SegmentEditor
m = slicer.util.mainWindow()
m.moduleSelector().selectModule('SegmentEditor')
layoutManager = slicer.app.layoutManager()
layoutManager.setLayout(6)

# wait for segmentation
try:
    input("Now perform your segmentation and press ENTER. If you push ENTER the screen will look unresponsive for a few seconds.")
except EOFError: pass

slicer.app.processEvents()

# Create a new directory where the scene will be saved into
sceneSaveDirectory = "D:/Slicer/test/" + patientName
if not os.access(sceneSaveDirectory, os.F_OK):
  os.makedirs(sceneSaveDirectory)

slicer.app.processEvents()

viewNodeID = 'vtkMRMLSliceNodeRed'
import ScreenCapture
cap = ScreenCapture.ScreenCaptureLogic()
view = cap.viewFromNode(slicer.mrmlScene.GetNodeByID(viewNodeID))
cap.captureImageFromView(view,sceneSaveDirectory + "/segmentation export.png")

#time.sleep(3)
slicer.app.processEvents()

# Save the scene
if slicer.app.applicationLogic().SaveSceneToSlicerDataBundleDirectory(sceneSaveDirectory, None):
  logging.info("Scene saved to: {0}".format(sceneSaveDirectory))
else:
  logging.error("Scene saving failed")   

slicer.mrmlScene.Clear(0)
m.moduleSelector().selectModule('DICOM')
</code></pre>
<p>If I comment out (or remove) the last two lines and paste this after running the above script:</p>
<pre><code>viewNodeID = 'vtkMRMLSliceNodeRed'
import ScreenCapture
cap = ScreenCapture.ScreenCaptureLogic()
view = cap.viewFromNode(slicer.mrmlScene.GetNodeByID(viewNodeID))
cap.captureImageFromView(view,sceneSaveDirectory + "/segmentation export.png")
</code></pre>
<p>then the exported screenshot does appear</p>

---

## Post #7 by @cpinter (2021-01-05 08:59 UTC)

<p>I was able to spend a little time on this. Indeed, using your script the screenshot is not saved for some reason. I noticed that if the scene is not saved after capturing the screenshot, then the screenshot is saved alright, which is strange.</p>
<p>If the order of the commands does not matter, then I suggest simply saving the screenshot after saving the scene. However, I don’t have an explanation about the screenshot not being saved with your snippet without some more serious debugging.</p>

---

## Post #8 by @Justin (2021-01-05 10:50 UTC)

<p>Thanks for taking the time looking into this, I agree that changing the order of the script is the easiest way to go. For now the order of the commands do not matter, so I can work with it!</p>
<p>I’ve just taken another look and added a pause after saving the screenshot.<br>
It appears that the screenshot is written, but it is then deleted by the ‘save scene’ part of the script.<br>
That is <code>SaveSceneToSlicerDataBundleDirectory()</code></p>
<p>When I look it up in the APIdocs I do not see a means to prevent overwriting the entire folder.<br>
To me this is a problem, as I might want to add other segmentations to this folder later on.<br>
Do you know if it is possible to save the files without overwriting the entire folder contents?</p>

---

## Post #9 by @cpinter (2021-01-05 12:50 UTC)

<p>OK makes sense, so the scene saving function clears the folder.</p>
<p>What is your goal with the screenshot in the same folder? I’m asking because usually people save scenes in an MRB file, which is self-contained, much easier to manage because it’s a single file, and can be loaded in Slicer the same way as a MRML file that has a Data folder.</p>

---

## Post #10 by @Justin (2021-01-06 13:27 UTC)

<p>Thanks, my idea was that I want to create multiple 2D segmentations  (so at different axial levels of the body)<br>
I wanted to create a snapshot, so that I can preview each segmentation while not having to open the entire scene.</p>
<p>so the folder structure would be</p>
<p>Patient A<br>
– segmentation 1 preview.png<br>
– segmentation 2 preview.png<br>
– scene.mrml<br>
– “Data” folder containing all the data</p>
<p>Patient B<br>
– segmentation 1 preview.png<br>
– segmentation 2 preview.png<br>
– scene.mrml<br>
– “Data” folder containing all the data</p>
<p>I think I’ll work around this issue by saving all the screenshots in a separate folder (so not in the patient folder)</p>

---

## Post #11 by @lassoan (2021-01-06 14:16 UTC)

<aside class="quote no-group" data-username="Justin" data-post="8" data-topic="15328">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/3ab097/48.png" class="avatar"> Justin:</div>
<blockquote>
<p>It appears that the screenshot is written, but it is then deleted by the ‘save scene’ part of the script.<br>
That is <code>SaveSceneToSlicerDataBundleDirectory()</code></p>
</blockquote>
</aside>
<p>It is essential to clean the output folder before MRML scene bundle export because when MRB file is generated from the entire content of the folder. You do not want random files that pre-exist in that folder show up in your MRB file. Whatever you want to save into the MRB file, you can add it to the scene (for example, if you want to include an additional png file then you can load it into the scene as an image volume).</p>
<aside class="quote no-group" data-username="Justin" data-post="10" data-topic="15328">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/3ab097/48.png" class="avatar"> Justin:</div>
<blockquote>
<p>I wanted to create a snapshot, so that I can preview each segmentation while not having to open the entire scene.</p>
</blockquote>
</aside>
<p>Yes, if you have a custom folder structure then you can rearrange Slicer’s default output any way you want.</p>
<aside class="quote no-group" data-username="Justin" data-post="10" data-topic="15328">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/3ab097/48.png" class="avatar"> Justin:</div>
<blockquote>
<p>Thanks, my idea was that I want to create multiple 2D segmentations (so at different axial levels of the body)</p>
</blockquote>
</aside>
<p>I would strongly recommend to use a 3D viewer to review segmentations. Very often you don’t notice segmentation errors (or may think that a valid segmentation is incorrect), unless you review the segmentation along at least 3 orthogonal axes. Even if you export 3 image stacks, you will have trouble reviewing the data, because it is hard to find corresponding slice views for a specific 3D position.</p>
<p>Latest Slicer Preview Release is fully portable: you can just copy the application files to a USB stick along with the images extensions and provide a batch file that launches Slicer and iterates through all the images with a convenient user interface (for example, using <a href="https://github.com/JoostJM/SlicerCaseIterator">CaseIterator extension</a> or the DICOM browser).</p>
<p>If you want to avoid your users to run a desktop application then you can export segmentation as DICOM segmentation object and review along with the images in a DICOMweb browser in your web browser using <a href="https://kheops.online/">Kheops</a> or using your cloud services or your own server.</p>

---

## Post #12 by @Justin (2021-01-10 10:59 UTC)

<p>Thanks Andras for your explanation. If you explain it, it makes sense to keep the folder empty.<br>
And it is a useful suggestion to add the export to the scene!</p>
<p>I only have one more question: For the scans I use <code>controller.rotateSliceToBackground()</code> and when I add a .png to the scene, the image is not shown in one view, but is also rotated, so I have to scroll to see the entire image.<br>
And If I rotate the .png to be shown in one view, the scan is also rotated.</p>
<p>Is it possible that the .png is not rotated when I import it to the scene?</p>
<p>Thanks for your help so far! Justin</p>

---
