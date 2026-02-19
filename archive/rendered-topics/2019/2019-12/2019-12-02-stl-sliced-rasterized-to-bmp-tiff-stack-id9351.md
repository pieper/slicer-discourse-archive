---
topic_id: 9351
title: "Stl Sliced Rasterized To Bmp Tiff Stack"
date: 2019-12-02
url: https://discourse.slicer.org/t/9351
---

# STL sliced/rasterized to BMP/TIFF stack

**Topic ID**: 9351
**Date**: 2019-12-02
**URL**: https://discourse.slicer.org/t/stl-sliced-rasterized-to-bmp-tiff-stack/9351

---

## Post #1 by @FLjosh (2019-12-02 03:42 UTC)

<p>Hi There,<br>
I want to import an STL file and slice at a layer height of 0.1mm and generate a folder of TIFF images corresponding to a each fully dense layer. Is this possible?<br>
I have seen many people here trying to do the opposite (create an STL from a stack of images) so surely the reverse is possible! I just can’t quite figure out how to do that yet. Any tips greatly appreciated<br>
Thanks</p>

---

## Post #2 by @lassoan (2019-12-02 04:50 UTC)

<p>Yes, you can do these kinds of conversions using Slicer. I’ve added an example to the script repository that does what you need (with customizable margin size and output label value):</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Rasterize_a_model_and_save_it_to_a_series_of_image_files" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Rasterize_a_model_and_save_it_to_a_series_of_image_files</a></p>
<p>You can copy-paste the code above to the Python console (Ctrl-3). You can of course do the same steps using GUI, let us know if you would prefer to do that instead of scripting.</p>

---

## Post #3 by @FLjosh (2019-12-02 21:09 UTC)

<p>Thanks for that script! Looks just like what I need. Though having a bit of trouble implementing it.<br>
At line &gt;&gt;&gt; inputModel.GetBounds(bounds)<br>
I get an error AttributeError: ‘bool’ object has no attribute ‘GetBounds’<br>
Something I’m missing here?</p>

---

## Post #4 by @lassoan (2019-12-02 21:26 UTC)

<p>The script is to be used with recent Slicer Preview Releases. In latest stable, <code>loadModel</code> returns a bool flag (succes/fail) and you need to specify an additional argument to make it return the mode node as well. I would recommend you to use the latest preview release.</p>

---

## Post #5 by @FLjosh (2019-12-02 22:01 UTC)

<p>Great thanks, I got to the bottom of the script. I assume in line<br>
outputLabelmapVolumeArray = (slicer.util.arrayFromVolume(outputLabelmapVolumeNode) * labelValue).astype(‘int8’)<br>
That labelValue is meant to be declared outputVolumeLabelValue<br>
For a 55x40x40mm part I get 126 images which are all just black 128x131 pixels. Was expecting to get black silhouette of slice on white background right? Sorry - learning and asking at the same time.</p>

---

## Post #6 by @FLjosh (2019-12-02 22:32 UTC)

<p>O got it to work! Just figured out the SpacingMm and MarginMm variables. Thanks for that!<br>
Is there a way to increase resolution to around 600dpi and assign colours to background and sliced image? Thanks</p>

---

## Post #7 by @lassoan (2019-12-03 03:48 UTC)

<aside class="quote no-group" data-username="FLjosh" data-post="6" data-topic="9351">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/58f4c7/48.png" class="avatar"> FLjosh:</div>
<blockquote>
<p>increase resolution to around 600dpi</p>
</blockquote>
</aside>
<p>You can set any resolution by adjusting outputVolumeSpacingMm values (first two values are image spacing within a slice, third value is image spacing between slices).</p>
<aside class="quote no-group" data-username="FLjosh" data-post="6" data-topic="9351">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/58f4c7/48.png" class="avatar"> FLjosh:</div>
<blockquote>
<p>assign colours to background and sliced image</p>
</blockquote>
</aside>
<p>It is an indexed image, so it has no colors. You can create an RGB image by defining a lookup table and running through <code>np.take</code> (e.g, something like this: <code>outputVolumeLabelValue=1; ... lut=[[255,0,0],[0,255,0]]; imageRGB = np.take(lut, imageIndexed)</code>). If you are doing this for 3D printing colored bitmaps on polyjet printers then you may consider using <a href="https://github.com/SlicerFab/SlicerFab">SlicerFab extension</a>.</p>

---

## Post #8 by @FLjosh (2019-12-04 00:50 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>. It is for 3D printing but just inverted the matrix as I just needed black on white.<br>
I have considerably increased the “resolution” by changing SpacingMm and have a high quality STL. However curves and diagonals are represented very coarse (45deg line steps up in 5x5pix increments).<br>
Does one of the functions quantize the model heavily?</p>

---

## Post #9 by @lassoan (2019-12-04 07:55 UTC)

<p>If you import a model into segmentation without specifying reference geometry then a default resolution is chosen automatically. You can force the segmentation’s internal labelmap representation geometry to be the same as the output geometry by calling <code> seg.SetReferenceImageGeometryParameterFromVolumeNode(referenceVolumeNode)</code> after <code>AddNewNodeByClass('vtkMRMLSegmentationNode')</code></p>
<p>Do you use a Stratasys printer? Can you write a bit about your application? My understanding is that voxel printing’s main advantages are that you can use voxel intensity of original images (and/or information extracted from them), you can generate 3D prints with regions of non-uniform color/opacity/stiffness, save time on segmentation, and create more detailed prints (e.g., using SlicerFab or similar methods), but you cannot really benefit from these if the bitmap just contains uniform regions defined by STL files. Or you just want to use these to validate your workflow vs. directly printing an STL file?</p>

---

## Post #10 by @FLjosh (2019-12-04 21:28 UTC)

<p>Thanks that worked, though I placed the call earlier, just after creating the seg object.<br>
It is for a DIY binder-jetting printer (only jetting binder not color). But another person designed the printhead interface which takes bitmap images layer by layer. I couldn’t find any software which generates these images except 3DSlicer.</p>

---

## Post #11 by @lassoan (2019-12-04 21:32 UTC)

<p>Sounds very exciting project. It’s great that you could make it all work.</p>

---

## Post #12 by @JSchnecke (2020-06-08 08:19 UTC)

<p>I am also new to the programm and community.<br>
Thank you for the code! I need the code for my masterthesis.<br>
I use the code you wrote, but when I am copying it into the python command box, 3D Slicer crashes and closes the window without saying something. I used the versions 4.10.2 and 4.11.0.</p>
<p>Maybe you have an idea, what I am doing wrong.</p>

---

## Post #13 by @Heimdal (2020-08-10 17:48 UTC)

<p>I have the same trouble as JSchnecke. When I am copying the code in the command box 3D Slicer chrashes down.<br>
I need TIFF-files from an STL for a 3D printing job.<br>
Can you help me please?</p>

---

## Post #14 by @lassoan (2020-08-10 21:43 UTC)

<p>What command exactly?</p>
<p>For tiff to STL conversion you don’t have to write any code but you can load the TIFF stack as a label volume, right-click in Data module to convert to segmentation, then use “Export to files” to save as STL. If the TIFF images are not yet segmented then you can segment using Segment Editor module.</p>

---

## Post #15 by @Heimdal (2020-08-12 21:27 UTC)

<p>Thank you Andras for the great tool. Now it is running.<br>
I have one question more. Everything in the tif-file is grey and everything outside is black. For my printing job I need the reagions inside black and outside white. Can I configure something in your code that I get tif-files out in the form I need.<br>
Thanks for your help.</p>

---

## Post #16 by @Heimdal (2020-08-13 07:11 UTC)

<p>I shouldn’t be writing messages late at night. Sorry for the errors in the above text.<br>
What I want to say is that everything inside the object in the tiff file is grey and everything outside is black. For my printer I need black inside and white outside. Can I change something in your code to get the Tiff in the desired format?<br>
Thanks for your help.</p>

---

## Post #17 by @lassoan (2020-08-13 13:15 UTC)

<p>Can you attach a few screenshots that show what you have now and mark on it what you would like to be different?</p>

---

## Post #18 by @Heimdal (2020-08-13 14:57 UTC)

<p>For example, I would like to print the goose as you can see in the picture.  <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9e189c37fa9b9cb761da916f9880de0b83221d2.jpeg" data-download-href="/uploads/short-url/v5sP6H6AzLFFnKyBB8s0hymCQbE.jpeg?dl=1" title="Ente" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d9e189c37fa9b9cb761da916f9880de0b83221d2_2_194x250.jpeg" alt="Ente" data-base62-sha1="v5sP6H6AzLFFnKyBB8s0hymCQbE" width="194" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d9e189c37fa9b9cb761da916f9880de0b83221d2_2_194x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d9e189c37fa9b9cb761da916f9880de0b83221d2_2_291x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d9e189c37fa9b9cb761da916f9880de0b83221d2_2_388x500.jpeg 2x" data-dominant-color="ADADAF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Ente</span><span class="informations">581×748 21.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Therefore I slice the STL-file with your phyton code. <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4febcacce08999ff34ea26453914326cda5fe27.jpeg" alt="image_043" data-base62-sha1="wFMDm8XO1CP9vO3WX0NFpYmnsQT" width="151" height="215"><br>
In the black and white (I think in real it is grey) picture you can see one tiff-file (the feet of the goose) of the slicing result from your python code. So far so good. Unfortunately I need for my 3D printer the black areas in white and the white (grey) areas in black. That means that at the moment my printer would print the surrounding of the goose and the goose itself would not be printed.</p>
<p>What I need is shown in the picture below.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/12c9a57d3e977293d30878cad6321c4a42b55032.jpeg" alt="image_043_invert" data-base62-sha1="2GcCrcbzH7LP3tu4qKa18MaHZHc" width="151" height="215"></p>

---

## Post #19 by @lassoan (2020-08-13 15:52 UTC)

<p>You can use Simple Filters module’s IntensityWindowingImageFilter method to rescale and invert intensity (set Output minimum &gt; Output maximum to invert intensity).</p>

---

## Post #21 by @chris-is-pinbo (2020-10-21 17:24 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Thanks for sharing the STL to TIFF stack Python script. I’m running into an error when running the following line:</p>
<p>inputModel = slicer.util.loadModel(inputModelFile)</p>
<p>The error:</p>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\chris\AppData\Local\NA-MIC\Slicer 4.11.20200930\bin\Python\slicer\util.py”, line 719, in loadModel<br>
return loadNodeFromFile(filename, ‘ModelFile’, {}, returnNode)<br>
File “C:\Users\chris\AppData\Local\NA-MIC\Slicer 4.11.20200930\bin\Python\slicer\util.py”, line 598, in loadNodeFromFile<br>
raise RuntimeError(errorMessage)<br>
RuntimeError: Failed to load node from file: F:\APEP\Internal_CA_Project\Method_ValidationD_Sphereox_20x20x10.stl</p>
<p>The original filepath of my .stl was:</p>
<p>F:\APEP\Internal_CA_Project\Method_Validation\3D_Sphere\box_20x20x10.stl</p>
<p>which didn’t run into any issues. Any thoughts?</p>
<p>Thanks in advance!</p>

---

## Post #22 by @muratmaga (2020-10-21 17:44 UTC)

<aside class="quote no-group" data-username="chris-is-pinbo" data-post="21" data-topic="9351">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chris-is-pinbo/48/8541_2.png" class="avatar"> chris-is-pinbo:</div>
<blockquote>
<p>RuntimeError: Failed to load node from file: F:\APEP\Internal_CA_Project\Method_ValidationD_Sphereox_20x20x10.stl</p>
</blockquote>
</aside>
<p>You are missing a</p>
<blockquote>
<p>\</p>
</blockquote>
<p>between your Validation and 3DSphere.</p>

---

## Post #23 by @lassoan (2020-10-21 17:48 UTC)

<p>Also note that you need to be careful when using backslash in a string in Python:</p>
<aside class="quote quote-modified" data-post="14" data-topic="2837">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/subprocess-call-does-not-work/2837/14">Subprocess.call does not work!</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    FYI, since backslash (\) is an escape character in Python, you cannot simply use it in a string literal in Python. 
The easiest is to indicate that you specify a raw string by prepending an r character before the string. This is correct: 
somePath = r"F:\someFolder\python.exe"

If you need to use a regular string then backslash can be entered by typing double-backslash. This is correct: 
somePath = "F:\\someFolder\\python.exe"

You may also use Unix-type separators. This is correct: 
somePath = …
  </blockquote>
</aside>


---

## Post #24 by @chris-is-pinbo (2020-10-21 17:49 UTC)

<p>Hi <a class="mention" href="/u/muratmaga">@muratmaga</a>, thanks for the quick reply. I don’t understand how that has happened because</p>
<p>inputModelFile =  F:\APEP\Internal_CA_Project\Method_Validation\3D_Sphere\box_20x20x10.stl</p>
<p>and inputModelFile is the input to slicer.util.loadModel(), which generated the error. It seems like my file path is being altered in some way.</p>

---

## Post #25 by @lassoan (2020-10-21 17:50 UTC)

<aside class="quote no-group" data-username="chris-is-pinbo" data-post="24" data-topic="9351">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chris-is-pinbo/48/8541_2.png" class="avatar"> chris-is-pinbo:</div>
<blockquote>
<p>It seems like my file path is being altered in some way.</p>
</blockquote>
</aside>
<p>See the explanation <a href="https://discourse.slicer.org/t/stl-sliced-rasterized-to-bmp-tiff-stack/9351/23">above</a>.</p>

---

## Post #26 by @chris-is-pinbo (2020-10-21 17:54 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>Thanks for the suggestion to use</p>
<pre><code class="lang-auto">somePath = r"F:\someFolder\python.exe"
</code></pre>
<p>That seemed to do the trick. Now I’m running into an issue during the last loop, where the script writes to the output directory.</p>
<p>(Note: I haven’t edited anything in the file but the input and output filepaths. The physical dimensions of the geometry I am looking to convert to a .tiff stack aren’t important as I am just interested in the curvature of the model.)</p>
<p>Here’s what the Python console is showing me:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; inputModelFile = r"F:\APEP\Internal_CA_Project\Method_Validation\3D_Sphere\box_20x20x10.stl"
&gt;&gt;&gt; outputDir = r"F:\APEP\Internal_CA_Project\Method_Validation\3D_Sphere\tiffs"
&gt;&gt;&gt; outputVolumeLabelValue = 100
&gt;&gt;&gt; outputVolumeSpacingMm = [0.5, 0.5, 0.5]
&gt;&gt;&gt; outputVolumeMarginMm = [10.0, 10.0, 10.0]
&gt;&gt;&gt; 
&gt;&gt;&gt; # Read model
&gt;&gt;&gt; inputModel = slicer.util.loadModel(inputModelFile)
&gt;&gt;&gt; 
&gt;&gt;&gt; # Determine output volume geometry and create a corresponding reference volume
&gt;&gt;&gt; import math
&gt;&gt;&gt; import numpy as np
&gt;&gt;&gt; bounds = np.zeros(6)
&gt;&gt;&gt; inputModel.GetBounds(bounds)
&gt;&gt;&gt; imageData = vtk.vtkImageData()
&gt;&gt;&gt; imageSize = [ int((bounds[axis*2+1]-bounds[axis*2]+outputVolumeMarginMm[axis]*2.0)/outputVolumeSpacingMm[axis]) for axis in range(3) ]
&gt;&gt;&gt; imageOrigin = [ bounds[axis*2]-outputVolumeMarginMm[axis] for axis in range(3) ]
&gt;&gt;&gt; imageData.SetDimensions(imageSize)
&gt;&gt;&gt; imageData.AllocateScalars(vtk.VTK_UNSIGNED_CHAR, 1)
&gt;&gt;&gt; imageData.GetPointData().GetScalars().Fill(0)
&gt;&gt;&gt; referenceVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode")
&gt;&gt;&gt; referenceVolumeNode.SetOrigin(imageOrigin)
&gt;&gt;&gt; referenceVolumeNode.SetSpacing(outputVolumeSpacingMm)
&gt;&gt;&gt; referenceVolumeNode.SetAndObserveImageData(imageData)
&gt;&gt;&gt; referenceVolumeNode.CreateDefaultDisplayNodes()
&gt;&gt;&gt; 
&gt;&gt;&gt; # Convert model to labelmap
&gt;&gt;&gt; seg = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSegmentationNode')
&gt;&gt;&gt; seg.SetReferenceImageGeometryParameterFromVolumeNode(referenceVolumeNode)
&gt;&gt;&gt; slicer.modules.segmentations.logic().ImportModelToSegmentationNode(inputModel, seg)
True
&gt;&gt;&gt; seg.CreateBinaryLabelmapRepresentation()
True
&gt;&gt;&gt; outputLabelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
&gt;&gt;&gt; slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(seg, outputLabelmapVolumeNode, referenceVolumeNode)
True
&gt;&gt;&gt; outputLabelmapVolumeArray = (slicer.util.arrayFromVolume(outputLabelmapVolumeNode) * outputVolumeLabelValue).astype('int8')
&gt;&gt;&gt; 
&gt;&gt;&gt; # Write labelmap volume to series of TIFF files
&gt;&gt;&gt; pip_install("imageio")
Requirement already satisfied: imageio in c:\users\chris\appdata\local\na-mic\slicer 4.11.20200930\lib\python\lib\site-packages (2.9.0)
Requirement already satisfied: pillow in c:\users\chris\appdata\local\na-mic\slicer 4.11.20200930\lib\python\lib\site-packages (from imageio) (7.2.0)
Requirement already satisfied: numpy in c:\users\chris\appdata\local\na-mic\slicer 4.11.20200930\lib\python\lib\site-packages (from imageio) (1.19.1)
WARNING: You are using pip version 20.1.1; however, version 20.2.4 is available.
You should consider upgrading via the 'C:\Users\chris\AppData\Local\NA-MIC\Slicer 4.11.20200930\bin\python-real.exe -m pip install --upgrade pip' command.
&gt;&gt;&gt; import imageio
&gt;&gt;&gt; for i in range(len(outputLabelmapVolumeArray)):
...     imageio.imwrite(f'{outputDir}/image_{i:03}.tiff', outputLabelmapVolumeArray[i])
... 
Traceback (most recent call last):
  File "&lt;console&gt;", line 2, in &lt;module&gt;
  File "C:\Users\chris\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Python\Lib\site-packages\imageio\core\functions.py", line 303, in imwrite
    writer = get_writer(uri, format, "i", **kwargs)
  File "C:\Users\chris\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Python\Lib\site-packages\imageio\core\functions.py", line 217, in get_writer
    request = Request(uri, "w" + mode, **kwargs)
  File "C:\Users\chris\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Python\Lib\site-packages\imageio\core\request.py", line 124, in __init__
    self._parse_uri(uri)
  File "C:\Users\chris\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Python\Lib\site-packages\imageio\core\request.py", line 265, in _parse_uri
    raise FileNotFoundError("The directory %r does not exist" % dn)
FileNotFoundError: The directory 'F:\\APEP\\Internal_CA_Project\\Method_Validation\\3D_Sphere\\tiffs' does not exist
&gt;&gt;&gt; 
</code></pre>

---

## Post #27 by @lassoan (2020-10-21 18:53 UTC)

<p>The output directory (<code>F:\\APEP\\Internal_CA_Project\\Method_Validation\\3D_Sphere\\tiffs</code>) must exist. You need to create it either by adding a line to the Python script or manually (using Windows File Explorer, etc).</p>

---

## Post #28 by @chris-is-pinbo (2020-10-21 19:25 UTC)

<p><img src="https://emoji.discourse-cdn.com/twitter/flushed.png?v=9" title=":flushed:" class="emoji" alt=":flushed:"> what a simple issue. Thanks for the help <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #29 by @lassoan (2020-11-01 15:40 UTC)

<p>A post was split to a new topic: <a href="/t/using-slicer-via-web-api/14368">Using Slicer via web API</a></p>

---

## Post #30 by @heimlifeiss (2022-01-12 17:54 UTC)

<p>Hello<br>
I’m absolutly new to slicer and I downloaded it mainly because of the problem discussed here.</p>
<p>I want to do the same thing: slice an STL and then save each layer as a bpm or pdf or something else. This problem here is solved with a script. My skills in programming and similar stuff are quite limited. So, is it also possible to slice the STL in the GUI/slicer program and save each layer? Right away I didn’t find such a function so I wanted to ask.</p>
<p>Would be great if I could get some help here. I also need these layers for 3d printing.<br>
Thanks <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #31 by @Jack-Waghorne (2022-05-04 09:52 UTC)

<p>Hello,</p>
<p>I am following this script but Slicer crash whenever the following line is entered:<br>
slicer.modules.segmentations.logic().ImportModelToSegmentationNode(inputModel, seg)<br>
If you can provide any guidance on this it would be greatly appreciated.</p>
<p>Thanks in advance!</p>

---

## Post #32 by @robert (2023-03-28 03:15 UTC)

<p>Hi, It’s what I am looking for and I want to export one 3D tif file（contain all 2D tifs）. But I can’t find the link to get the script example. How do I get it?<br>
Besides, how to use GUI to realize it？ Great thanks!!! <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>

---

## Post #33 by @lassoan (2023-03-28 03:26 UTC)

<p>The script is now available <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#rasterize-a-model-and-save-it-to-a-series-of-image-files">here</a>.</p>

---
