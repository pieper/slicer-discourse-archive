# Handle additional images as numpy arrays in Slicer

**Topic ID**: 3310
**Date**: 2018-06-26
**URL**: https://discourse.slicer.org/t/handle-additional-images-as-numpy-arrays-in-slicer/3310

---

## Post #1 by @virginia_fgc (2018-06-26 21:13 UTC)

<p>Hello,</p>
<p>In order to work on my imported MR image, I need to create a Python script in which I need to import as well (separately):</p>
<ul>
<li>A txt file with numeric data</li>
<li>An image that should be handled as an array<br>
Would it be possible to do that in Slicer with Python? I’ve seen that to work with Images, you need to import at least cv2 or Image and they both aren’t available through the execution of “import &amp;”. That leads me to the problem I already reported in a different topic with the importation of “medpy” module (<a href="https://discourse.slicer.org/t/import-medpy-fails/3206">Import medpy fails</a>).</li>
</ul>
<p>In particular, I’d like to know whether:</p>
<ul>
<li>It’d be possible to perform the importation through a button, and add several filters that control the validity of the imported data i.e.: the size of the image</li>
<li>It’d be possible to convert the image (a JPG image) to an array with the available modules, and without that image being the volume added to Slicer</li>
</ul>
<p>The reason why that image needs to be imported through the script is that it’s a fixed image (fixed folder and name) and I only want it to extract some coordinates. I don’t need to process it as an image, nor displaying it.</p>
<p>Thank you in advance for any input about this.</p>
<p>Virginia Fernández</p>

---

## Post #2 by @pieper (2018-08-13 15:03 UTC)

<p>Hi <a class="mention" href="/u/virginia_fgc">@virginia_fgc</a> I see there was never a reply to this (sorry about that)  - were you able to find the information you needed?</p>

---

## Post #3 by @virginia_fgc (2018-08-26 22:44 UTC)

<p>Hi Steve,</p>
<p>The processing I had to apply to the other image I was talking about was far too complex to be programmed in Python/Slicer, thus I decided to handle that process in Matlab to get an output .txt file with coordinates. Basically, I would like to import numeric data from two .txt files into Slicer so that I can tag the voxels from my volume with the coordinates / values stored in the .txt.</p>
<p>I still haven’t found out how to do it. If I do I will update this issue. Any help is kindly appreciated.</p>
<p>Thank you for the reply, and best regards</p>
<p>Virginia</p>

---

## Post #4 by @lassoan (2018-08-27 04:40 UTC)

<p>I’m not exactly sure what you would like to do, but setting voxel coordinates listed in a file to specific value is a single-line operation in Python:</p>
<pre><code># Specify some input data

import SampleData
volume=SampleData.SampleDataLogic().downloadMRHead()
volumeArray=slicer.util.arrayFromVolume(volume)

coords_KJI=[(47,58,60,65),(127,127,127,127),(142,142,142,142)]
voxelValue = 250

# Set voxel values at specified coordinates
volumeArray[coords_KJI] = voxelValue

# Update display (see 4 voxels near the center of the red slice view becoming very bright as a result)
slicer.util.arrayFromVolumeModified(volume)
</code></pre>
<p>It should not be much more complicated if you need to set different value for each point.</p>
<p>If you need to fill a complete volume (interpolate between known points) then you can use VTK: create a point set with associated point scalar data, apply Delaunay triangulation, and use probe filter to create a volume. This would be probably a few ten lines of code.</p>

---

## Post #5 by @virginia_fgc (2018-08-28 19:13 UTC)

<p>Hello,</p>
<p>Thank you very much for that valuable answer.<br>
However, I am more concerned with the importing itself. I need to create a loadable module, that needs to have a volume selector (I have seen how to do that in the Slicer tutorials), as well as two buttons that load the content of .txt files into two different arrays. One of thes texts is the one containing the coordinates.<br>
I know how to do process that information (in Python, with open, readline etc.), but not how to do it in an ‘interactive’ way.</p>
<p>The workflow would be:</p>
<ol>
<li>User selects the "Import TEXT FILE 1 Button’</li>
<li>A window opens with a File Explorer that enables the user to select a txt</li>
<li>The .txt is copied into a variable (I guess that this can be done with ‘open’ if step 2 provides the path).</li>
</ol>
<p>Is there a way to perform step 2 and get the path so that 3 can be executed thereafter?</p>
<p>Thank you</p>

---

## Post #6 by @lassoan (2018-08-28 19:17 UTC)

<p>You can use <code>ctk.ctkPathLineEdit()</code> widget to get input paths. See for example how it is done in the <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMPatcher/DICOMPatcher.py#L49-L52">DICOM Patcher module</a>.</p>

---

## Post #7 by @virginia_fgc (2018-09-30 23:55 UTC)

<p>Dear Andras,</p>
<p>Apologises for not having replied to this before. Thank you very much for the answer. It solved my issue. Instead of using the directories, I used the Files directly.</p>
<p><span class="hashtag">#create</span> input selector for Files<br>
self.inputFileSelector_myIS = ctk.ctkPathLineEdit()<br>
self.inputFileSelector_myIS = ctk.ctkPathLineEdit.Files</p>
<p><span class="hashtag">#And</span> then was able to get the path (directory+name) on the function with:<br>
path =  self.inputFileSelector_myIS.currentPath<br>
<span class="hashtag">#And</span> open it with:<br>
my_file =  open(path)</p>
<p>Only one additional question. I have noticed that there’s a <strong>default value</strong> for the file that is always displayed when I run Slicer. That default value has not been defined in the code, yet it is always appearing and can be confusing. Is there a way to leave the space blank?</p>
<p>Thank you very much and kind regards,</p>
<p>Virginia</p>

---

## Post #8 by @lassoan (2018-10-01 12:51 UTC)

<aside class="quote no-group" data-username="virginia_fgc" data-post="7" data-topic="3310">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/virginia_fgc/48/3309_2.png" class="avatar"> virginia_fgc:</div>
<blockquote>
<p><strong>default value</strong> for the file that is always displayed</p>
</blockquote>
</aside>
<p>File history is a very useful feature, so I would recommend that you keep it. You have full control over it - see documentation of <a href="http://www.commontk.org/docs/html/classctkPathLineEdit.html#a801ae30d651d4e24bc73398d05464f6e">settingKey</a> property.</p>

---

## Post #9 by @Saima (2019-01-07 11:42 UTC)

<p>Hi Andras,<br>
I want to display the array data in the red slice view. The outputArrayImage is an np multidimensional array with floating data. I need to display it. I am pasting the code here. I see blank output in slicer.</p>
<p>volumeNode = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLScalarVolumeNode’)<br>
volumeNode.CreateDefaultDisplayNodes()<br>
updateVolumeFromArray(volumeNode, outputArrayImage)<br>
setSliceViewerLayers(background=volumeNode)</p>
<pre><code>red_logic = slicer.app.layoutManager().sliceWidget("Red").sliceLogic()
red_cn = red_logic.GetSliceCompositeNode()
red_logic.GetSliceCompositeNode().SetBackgroundVolumeID(volumeNode.GetID())
slicer.app.layoutManager().setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutOneUpRedSliceView)
display()</code></pre>

---

## Post #10 by @lassoan (2019-01-07 15:11 UTC)

<p>You can use <code>slicer.util.updateVolumeFromArray</code> to set voxels of a volume node from a numpy array.</p>

---
