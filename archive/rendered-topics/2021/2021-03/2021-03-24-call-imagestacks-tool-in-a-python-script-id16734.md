---
topic_id: 16734
title: "Call Imagestacks Tool In A Python Script"
date: 2021-03-24
url: https://discourse.slicer.org/t/16734
---

# Call ImageStacks tool in a Python script

**Topic ID**: 16734
**Date**: 2021-03-24
**URL**: https://discourse.slicer.org/t/call-imagestacks-tool-in-a-python-script/16734

---

## Post #1 by @gnasello (2021-03-24 01:26 UTC)

<p>Hi everyone,</p>
<p>I am starting using 3D Slicer and I learnt how to load large image stack as 3D volume thanks to the ImageStacks tool provided by the SlicerMorph extension, following the <a href="https://www.youtube.com/watch?v=tjZUOqnrc_Y" rel="noopener nofollow ugc">Youtube tutorial</a>.</p>
<p>I was wondering if it is possible there is an ImageStacks function that would load the image stack from a Python script, something similar to:</p>
<p><code>loadedVolumeNode = slicer.util.loadVolume('c:/Users/abc/Documents/SomeImage/file001.png', {'singleFile': False})</code></p>
<p>But using the ImageStack module.</p>
<p>Thanks for your help!</p>
<p>Gabriele</p>

---

## Post #2 by @gnasello (2021-03-24 12:16 UTC)

<p>I solved it. As lassoan already mentioned in <a href="https://discourse.slicer.org/t/how-do-i-use-python-to-call-a-transform-module-to-another-module/16711/4">this answer</a>, you need MRML and module logic classes to interact with any other module (find more in <a href="https://www.slicer.org/w/img_auth.php/7/79/SlicerModulesProgrammingBeyondBasics.pdf" rel="noopener nofollow ugc">these slides</a>).</p>
<p>After looking at <a href="https://github.com/SlicerMorph/SlicerMorph/blob/d0d9371cc783da1900e5b0923aa877d5a1586397/ImageStacks/ImageStacks.py#L593" rel="noopener nofollow ugc">ImageStack code</a>, I ended up with the following script:</p>
<pre><code># filename is the first image path of the stack, eg "/opt/data/image-0001.tif"
filename = "/opt/data/image-0001.tif"

# Set "ImageStacks" as currently active module.
slicer.util.selectModule("ImageStacks")
# Python scripted modules
moduleWidget = slicer.modules.imagestacks.widgetRepresentation().self()

# load image stack
# User selects a file like "/opt/data/image-0001.tif"
moduleWidget.archetypeText.text = filename

# The populateFromArchetype method will populate the file list with all files 
# that match the numbering pattern in that directory
moduleWidget.populateFromArchetype()
# to check correct file loading
# print(moduleWidget.logic.filePaths)

# Instantiate and add a VolumeNode to the scene.
masterVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", "microCT_scan")

# Load the files in paths to outputNode.
moduleWidget.logic.loadVolume(outputNode = masterVolumeNode)</code></pre>

---

## Post #3 by @lassoan (2021-03-24 13:24 UTC)

<p>Thanks for sharing. You can further simplify this by not instantiating a widget class but creating and using the logic class directly:</p>
<pre><code class="lang-python">import ImageStacks
logic = ImageStacks.ImageStacksLogic()
logic.reverseSliceOrder = ...
logic.sliceSkip = ...
...
outputVolume = logic.loadVolume(None)
</code></pre>

---

## Post #4 by @hourglassnam (2022-03-27 03:56 UTC)

<p>Dear lassoan<br>
Thank you so much for sharing this information.<br>
I had a question as I followed your instruction.<br>
I had been getting ‘NoneType’ object has no attribute ‘shape’ error and I couldn’t figure out how to solve the problem.<br>
I tried adding a scalar volume node before loading the volume but it still did not worked.<br>
Could you please give me some advice?<br>
Thank you always for your help.</p>
<p>Below is the code I used</p>
<blockquote>
<p>file_dir = r"E:\CT_RAW\20211221\901377\901377_Rec\901377__rec00000028.bmp"<br>
bmp_file = <span class="chcklst-box fa fa-square-o fa-fw"></span><br>
bmp_file.append(file_dir)</p>
<p>import ImageStacks<br>
logic = ImageStacks.ImageStacksLogic()<br>
logic.filePaths = bmp_file<br>
logic.originalVolumeRecommendedSpacing = [0.006999972, 0.006999972, 0.006999972]<br>
logic.outputQuality = ‘preview’<br>
outputVolume = logic.loadVolume(None)</p>
</blockquote>
<p>This is the message I have been getting.</p>
<blockquote>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:/Users/njy95/AppData/Local/NA-MIC/Slicer 4.13.0-2022-02-25/NA-MIC/Extensions-30657/SlicerMorph/lib/Slicer-4.13/qt-scripted-modules/ImageStacks.py”, line 680, in loadVolume<br>
if len(volumeArray.shape) == 3:<br>
AttributeError: ‘NoneType’ object has no attribute ‘shape’</p>
</blockquote>

---

## Post #5 by @pieper (2022-03-27 13:47 UTC)

<p><a class="mention" href="/u/hourglassnam">@hourglassnam</a> when you get an error like that you need to trace through the code to identify where your use doesn’t match the expectations.  In this case you can find the <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/ImageStacks/ImageStacks.py#L680">source code</a> based on the information in the error message.  You can also edit your local copy to add <code>print</code> statements and then restart Slicer to figure out why your data doesn’t load.  If you are writing python scripts this is an important skill to develop.</p>

---
