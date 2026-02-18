# Creating Volume from Numpy

**Topic ID**: 658
**Date**: 2017-07-10
**URL**: https://discourse.slicer.org/t/creating-volume-from-numpy/658

---

## Post #1 by @hph10128 (2017-07-10 01:03 UTC)

<p>Hi all,</p>
<p>I have slicer version 4.7.0-2017-07-07 r26146 installed.</p>
<p>I am trying to convert a numpy 3d array into a new volume. I tried the following as listed in the nightly documentation:</p>
<blockquote>
<blockquote>
<blockquote>
<p>resultVolumeNode = getNode(‘fixed’)<br>
resultVtkArray = vtk.util.numpy_support.numpy_to_vtk(a, deep=True, array_type=vtk.VTK_SHORT)<br>
resultVolumeNode.GetImageData().SetScalars(resultVtkArray)</p>
</blockquote>
</blockquote>
</blockquote>
<p>I’m running into a couple of issues.</p>
<ol>
<li>
<p>numpy_to_vtk only seems to support 1 or 2d arrays. What is your recommended approach for 3d arrays?</p>
</li>
<li>
<p>SetScalars isn’t an available function on the (vtkCommonDataModelPython.vtkImageData) instance.</p>
</li>
</ol>
<p>If anyone has any suggestions on how to tackle these issues, I would greatly appreciate it!</p>
<p>Hailey</p>

---

## Post #2 by @pieper (2017-07-10 13:00 UTC)

<p>Hi Hailey -</p>
<p>If you are creating a new volume from scratch you need to create and initialize the vtkImageData as well as the vtkMRML nodes.</p>
<p>Here’s a fully worked out example in this <a href="https://github.com/pieper/SlicerWeb/blob/2e222917b7767ebe42caf1d50722316205a58459/WebServer/WebServer.py#L929">postNRRD</a> method which starts from a nrrd file in memory but it should give you the info you need to adapt to your use case.</p>
<p>Here are the key steps:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/pieper/SlicerWeb/blob/2e222917b7767ebe42caf1d50722316205a58459/WebServer/WebServer.py#L964-L966" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/pieper/SlicerWeb/blob/2e222917b7767ebe42caf1d50722316205a58459/WebServer/WebServer.py#L964-L966" target="_blank" rel="nofollow noopener">pieper/SlicerWeb/blob/2e222917b7767ebe42caf1d50722316205a58459/WebServer/WebServer.py#L964-L966</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="964" style="counter-reset: li-counter 963 ;">
<li>imageData = vtk.vtkImageData()</li>
<li>imageData.SetDimensions(map(int,fields['sizes'].split(' ')))</li>
<li>imageData.AllocateScalars(vtk.VTK_SHORT, 1)</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/pieper/SlicerWeb/blob/2e222917b7767ebe42caf1d50722316205a58459/WebServer/WebServer.py#L988-L1003" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/pieper/SlicerWeb/blob/2e222917b7767ebe42caf1d50722316205a58459/WebServer/WebServer.py#L988-L1003" target="_blank" rel="nofollow noopener">pieper/SlicerWeb/blob/2e222917b7767ebe42caf1d50722316205a58459/WebServer/WebServer.py#L988-L1003</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="988" style="counter-reset: li-counter 987 ;">
<li>node = slicer.util.getNode(volumeID)</li>
<li>if not node:</li>
<li>  node = slicer.vtkMRMLScalarVolumeNode()</li>
<li>  node.SetName(volumeID)</li>
<li>  slicer.mrmlScene.AddNode(node)</li>
<li>  node.CreateDefaultDisplayNodes()</li>
<li>node.SetAndObserveImageData(imageData)</li>
<li>node.SetIJKToRASMatrix(ijkToRAS)</li>
<li>
</li>
<li>pixels = numpy.frombuffer(requestBody[endOfHeader+2:],dtype=numpy.dtype('int16'))</li>
<li>array = slicer.util.array(node.GetID())</li>
<li>array[:] = pixels.reshape(array.shape)</li>
<li>imageData.GetPointData().GetScalars().Modified()</li>
<li>
</li>
<li>displayNode = node.GetDisplayNode()</li>
<li>displayNode.ProcessMRMLEvents(displayNode, vtk.vtkCommand.ModifiedEvent, "")</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>-Steve</p>

---

## Post #3 by @lassoan (2017-07-10 14:46 UTC)

<p>I’ve added better numpy array adapter methods and added working examples to the wiki:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Accessing_Volume_data_as_numpy_array" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Accessing_Volume_data_as_numpy_array</a></p>
<p>The new methods will be available in tomorrow’s nightly build. If you don’t want to wait till then then you can get the updated <a href="http://util.py">util.py</a> from here:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L668-L740" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L668-L740" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L668-L740</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="668" style="counter-reset: li-counter 667 ;">
<li>def __init__(self, node):</li>
<li>  self.node = node</li>
<li>def __enter__(self):</li>
<li>  self.wasModifying = self.node.StartModify()</li>
<li>  return self.node</li>
<li>def __exit__(self, type, value, traceback):</li>
<li>  self.node.EndModify(self.wasModifying)</li>
<li>
</li>
<li>#</li>
<li># MRML-numpy</li>
<li>#</li>
<li>
</li>
<li>def array(pattern = "", index = 0):</li>
<li>"""Return the array you are "most likely to want" from the indexth</li>
<li>MRML node that matches the pattern.  Meant to be used in the python</li>
<li>console for quick debugging/testing.  More specific API should be</li>
<li>used in scripts to be sure you get exactly what you want.</li>
<li>"""</li>
<li>node = getNode(pattern=pattern, index=index)</li>
<li>import slicer</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L668-L740" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #4 by @lassoan (2018-09-04 18:40 UTC)

<p>A post was split to a new topic: <a href="/t/get-each-slice-of-a-volume-as-numpy-array/3986">Get each slice of a volume as numpy array</a></p>

---

## Post #5 by @timeanddoctor (2018-09-09 00:33 UTC)

<pre><code>import numpy as np
import math

def some_func(x, y, z):
  return 0.01*x*x + 0.01*y*y + 0.01*z*z

a = np.fromfunction(some_func,(512,512,512))

volumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLScalarVolumeNode')
volumeNode.CreateDefaultDisplayNodes()
updateVolumeFromArray(volumeNode, a)
setSliceViewerLayers(background=volumeNode)
</code></pre>
<p>I went created a empty volume with a 512 size, but I get a “Thread” map( the upper python code)</p>

---

## Post #6 by @lassoan (2018-09-09 04:29 UTC)

<p>Do you have any question related to this?</p>

---

## Post #7 by @timeanddoctor (2018-09-09 09:32 UTC)

<aside class="quote" data-post="1" data-topic="4030">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/timeanddoctor/48/5839_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/improve-the-resolution-of-segment-for-import-a-model/4030">Improve the resolution of segment for "import a model"</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    What I am doing is to have a boolean opertation between two cylinder created by MakerupToModel. 
But the segment resolution seems not very well even after “crop volume wih 0.01 spacing scale” just as suggestion: <a href="https://discourse.slicer.org/t/segmentation-resolution/1394/10">Segmentation resolution</a>.
  </blockquote>
</aside>
<p>
What I am doing is improve the resolution for “import model as segment”<br>
Firstly, I need create a volume by python script…<br>
Secondly, I will porform crop volume, and then the model could be imported as a segment…Finally, the resolution for 3d reconstruction will be higher<br>
So, would you like to gvie me some advice to such a script? Thanks<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/024ea20fdcbae106aba02f73f76e1beacc3ff9bb.jpeg" data-download-href="/uploads/short-url/kpqnyzJYvKo8Iyzk3ZlUJNVc1B.jpeg?dl=1" title="2018-09-09_172133" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/024ea20fdcbae106aba02f73f76e1beacc3ff9bb_2_690x442.jpeg" alt="2018-09-09_172133" data-base62-sha1="kpqnyzJYvKo8Iyzk3ZlUJNVc1B" width="690" height="442" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/024ea20fdcbae106aba02f73f76e1beacc3ff9bb_2_690x442.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/024ea20fdcbae106aba02f73f76e1beacc3ff9bb.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/024ea20fdcbae106aba02f73f76e1beacc3ff9bb.jpeg 2x" data-dominant-color="D7D2DF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2018-09-09_172133</span><span class="informations">758×486 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @lassoan (2018-09-09 12:07 UTC)

<p>See the script repository for an example how to create a new volume: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_a_new_volume">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_a_new_volume</a></p>
<p>In recent Slicer nightly builds, there is a feature introduced exactly for this, as explained in this post:  <a href="https://discourse.slicer.org/t/improve-the-resolution-of-segment-for-import-a-model/4030/2?u=lassoan">Improve the resolution of segment for "import a model"</a></p>

---

## Post #9 by @Alex_Vergara (2019-01-17 17:13 UTC)

<p>This is not thread safe, I have tried to process several volumes independently at the same time but it does not work. The linear code works good but when trying to use some parallelization technique the calls to slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLScalarVolumeNode”, nodeName) breaks the flow with silly errors such as: module slicer does not contain member mrmlScene. even the call to slicer.util.getNode(‘MRHead’) which is read only breaks the flow.<br>
Sadly one has to do this volume by volume, I am dealing with 15 volumes here, so it would be nice some way to parallelize the code.<br>
I use joblib that can be installed easily.</p>

---

## Post #10 by @lassoan (2019-01-19 12:47 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="9" data-topic="658">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>This is not thread safe</p>
</blockquote>
</aside>
<p>Yes, of course it is not thread-safe. Thread safety has enormous overhead in complexity of development and also has significant performance impact, so no software component is ever developed thread-safe unless there is a strong reason to do so. You always need to add your own thread-safe synchronization and communication mechanisms around general-purpose code to make it thread-safe.</p>

---

## Post #11 by @Alex_Vergara (2019-01-21 10:37 UTC)

<p>I dont need synchronization/communication in my problem, I just want to modify one volume with some calculations, then the next, and so on. Therefore there are no interactions between them. Basically this is parallelization, not multi-threading. Slicer should be able to handle this, I mean several calls to its mrmlscene and util.<br>
Minimum example</p>
<pre><code class="lang-python">def calculate(name):
    node = slicer.util.getNode(name)
    volumeNode = slicer.vtkSlicerVolumesLogic().CloneVolume(slicer.mrmlScene,node,name.replace('ACSC', 'DOSE'),True)
    print('Node '+name.replace('ACSC', 'DOSE')+' created...')

nodes = slicer.util.getNodesByClass('vtkMRMLScalarVolumeNode')
nodenames = [node.GetName() for node in nodes]
nodenames = [name for name in nodenames if 'ACSC' in name]

for name in nodenames: # this works fine
    calculate(name)

from joblib import Parallel, delayed  # install joblib first using internal pip
Parrallel(n_jobs=4)(delayed(calculate)(name) for name in nodenames) # This launches the above error
</code></pre>

---

## Post #12 by @lassoan (2019-01-21 18:06 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="11" data-topic="658">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>Basically this is parallelization, not multi-threading.</p>
</blockquote>
</aside>
<p>Multi-threading is parallelization. Read up a bit more on this <a href="https://joblib.readthedocs.io/en/latest/parallel.html">here</a>.</p>
<aside class="quote no-group" data-username="Alex_Vergara" data-post="11" data-topic="658">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>I just want to modify one volume with some calculations, then the next, and so on. Therefore there are no interactions between them</p>
</blockquote>
</aside>
<p>Operations that may seem independent may often interfere with each other. For example, many Slicer modules observe node modification events, so any node code that triggers node modifications must be run from the main thread (cannot be run from worker threads).</p>
<aside class="quote no-group" data-username="Alex_Vergara" data-post="11" data-topic="658">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>I dont need synchronization/communication in my problem</p>
</blockquote>
</aside>
<p>You actually do need them and use them if you use joblib. Joblib can hide some of the low-level details and choose reasonable defaults, so you may get performance improvement and correct results without thinking for some very simple cases. However, in general, you cannot just blindly accept defaults expect that any functions that you put in <code>calculate</code> will work correctly.</p>
<p>I would suggest to use only a very restricted set of operations within <code>calculate</code>. For example, only use simple native python and numpy calls (and carefully study joblib and numpy documentation about what operations and parallelization options are permitted). Do all MRML method calls before/after the parallel processing.</p>

---

## Post #13 by @timp (2019-07-18 16:04 UTC)

<p>Hello,</p>
<p>I have slicer version 4.10.2 r28257 installed on an iMac</p>
<p>I am trying to convert two volume nodes into a numpy 3d arrays, do some processing to them, and then convert the numpy arrays back into a volume.  I tried the method as listed in the nightly documentation that Andras posted:</p>
<blockquote>
<p>import numpy as np<br>
import math<br>
a = arrayFromVolume(input1Volume)<br>
b = arrayFromVolume(input2Volume)</p>
<p>def some_func(x, y):<br>
return y(x-y)</p>
<p>a = np.fromfunction(some_func,(30,20,15))</p>
<p>volumeNode = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLScalarVolumeNode’)<br>
volumeNode.CreateDefaultDisplayNodes()<br>
updateVolumeFromArray(volumeNode, a)<br>
setSliceViewerLayers(background=volumeNode)</p>
</blockquote>
<p>But for that, I got the error that “arrayFromVolume” global name not defined.</p>
<p>Then, I put slicer.util before what I took to be the slicer related commands, like so:</p>
<blockquote>
<p>import numpy as np<br>
import slicer.util<br>
import math<br>
a = slicer.util.arrayFromVolume(input1Volume)<br>
b = slicer.util.arrayFromVolume(input2Volume)</p>
<p>def some_func(x, y):<br>
return y(x-y)</p>
<p>a = np.fromfunction(some_func,(30,20,15))</p>
<p>volumeNode = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLScalarVolumeNode’)<br>
volumeNode.CreateDefaultDisplayNodes()<br>
slicer.util.updateVolumeFromArray(volumeNode, a)<br>
setSliceViewerLayers(background=volumeNode)</p>
</blockquote>
<p>After that, though, I got the error that ‘only integer scalar arrays can be converted to a scalar index’</p>
<p>The volumes are from DICOM files, but I (think?) I have them as mrml volume nodes in my script, since I used the Qt GUI to treat the DICOM files I select as inputs as volume nodes.<br>
I tried the methods listed on this page, but I they either didn’t work or I implemented them incorrectly.  Could you please advise me on how to fix this problem?</p>
<p>Thanks,<br>
Timothy</p>

---

## Post #14 by @lassoan (2019-07-18 16:13 UTC)

<aside class="quote no-group" data-username="timp" data-post="13" data-topic="658">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/timp/48/4186_2.png" class="avatar"> timp:</div>
<blockquote>
<p>got the error that ‘only integer scalar arrays can be converted to a scalar index’</p>
</blockquote>
</aside>
<p>You correctly retrieve the volume from Slicer and you get the error message in the part where you manipulate the arrays using numpy functions. I’ve Google for the error message and found this solution: <a href="https://stackoverflow.com/questions/46902367/numpy-array-typeerror-only-integer-scalar-arrays-can-be-converted-to-a-scalar-i" class="inline-onebox">python - numpy array TypeError: only integer scalar arrays can be converted to a scalar index - Stack Overflow</a></p>

---

## Post #15 by @timp (2019-07-18 18:01 UTC)

<p>Hi Andras,<br>
I don’t think that solution applies here, since I’m not trying to simply make a three dimensional array from two arrays, and I tried the alternative solution of flattening the arrays, but I’m not sure exactly how that is supposed to help; and I got the same error message when I put it in my script.</p>
<pre><code class="lang-python">import numpy as np
import slicer.util
import math
a = slicer.util.arrayFromVolume(input1Volume)
b = slicer.util.arrayFromVolume(input2Volume)

a.reshape((1, -1))
b.reshape((1, -1))

def subtract_mult(x, y):
  return y(x-y)

c = np.fromfunction(some_func,(a,b))

volumeNode = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLScalarVolumeNode’)
volumeNode.CreateDefaultDisplayNodes()
slicer.util.updateVolumeFromArray(volumeNode, c)
setSliceViewerLayers(background=volumeNode)
</code></pre>
<p>Do I have to somehow transform the arrays obtained with slicer.util into numpy arrays?  I thought they already were numpy arrays, at least it seemed that way from the documentation on the wiki.<br>
Thank you for your help,<br>
Timothy</p>

---

## Post #16 by @lassoan (2019-07-19 00:36 UTC)

<aside class="quote no-group" data-username="timp" data-post="15" data-topic="658">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/timp/48/4186_2.png" class="avatar"> timp:</div>
<blockquote>
<p>Do I have to somehow transform the arrays obtained with slicer.util into numpy arrays?</p>
</blockquote>
</aside>
<p>slicer.util.array and slicer.util.arrayFromVolume already return numpy array.</p>
<p>You can Subtract an array from the other by calling <code>d = a - b</code>. If the geometry of the two volumes are different then you need to resample one to have the same geometry as the other using one of the volume resampling modules.</p>

---

## Post #17 by @timp (2019-07-19 00:54 UTC)

<p>Hi Andras,<br>
The volumes have the same geometry.  One is a Dixon fat image, and the other is a Dixon water image; both acquired simultaneously and they must have the same geometry.  I assumed they did return numpy arrays, but I am still having the same error with ‘only integer scalar arrays can be converted to a scalar index’.  I think this error means that the arrays I am getting from calling</p>
<blockquote>
<p>slicer.util.arrayFromVolume(volumeNode)</p>
</blockquote>
<p>must somehow not be integer scalar arrays.  Would you happen to know if this is the case, or if</p>
<blockquote>
<p>slicer.util.updateVolumeFromArray(volume2Node,a)</p>
</blockquote>
<p>does not accept the numpy arrays generated from the volume nodes?</p>
<p>Am I oversimplifying this? Because from the above thread I can see that the process of creating a volume array seems much more complicated than it does in the documentation.</p>
<p>Thanks again,<br>
Timothy Pinkhassik</p>

---

## Post #18 by @lassoan (2019-07-19 01:12 UTC)

<p>This works well for me:</p>
<pre><code class="lang-python">import SampleData
[input1Volume, input2Volume] = SampleData.SampleDataLogic().downloadDentalSurgery()

import slicer.util
a = slicer.util.arrayFromVolume(input1Volume)
b = slicer.util.arrayFromVolume(input2Volume)

c = b-a

volumeNode = slicer.modules.volumes.logic().CloneVolume(input1Volume, "Difference")
slicer.util.updateVolumeFromArray(volumeNode, c)
setSliceViewerLayers(background=volumeNode)
</code></pre>

---

## Post #19 by @timp (2019-07-19 13:20 UTC)

<p>Hi Andras,<br>
Thank you so much!  That worked perfectly.<br>
-Timothy</p>

---

## Post #20 by @Saima (2020-12-08 07:17 UTC)

<p>Hi Andras,<br>
I get new volumes but its empty. It has same dimensions as the one I have and its created but its all black.</p>
<p>I am using fuzzy classification to get two classes. whenI create volume its empty. Ithink I need to set scalars or is there anything I am doing wrong. Please help the code is below.</p>
<p>import numpy as np<br>
import skfuzzy as fuzz<br>
# Compute the thresholded output volume using the Threshold Scalar Volume CLI module<br>
“”“cliParams = {<br>
‘InputVolume’: inputVolume.GetID(),<br>
‘OutputVolume’: outputVolume.GetID(),<br>
‘ThresholdValue’ : imageThreshold,<br>
‘ThresholdType’ : ‘Below’ if invert else ‘Above’<br>
}<br>
cliNode = slicer.cli.run(slicer.modules.thresholdscalarvolume, None, cliParams, wait_for_completion=True)”""<br>
mriImage = slicer.util.getNode(inputVolume.GetID())<br>
brainImg = slicer.util.arrayFromVolume(mriImage)</p>
<pre><code>maskImage = slicer.util.getNode(outputVolume.GetID())
brainMask = slicer.util.arrayFromVolume(maskImage)

voxelIntensities = brainImg[brainMask &gt; 0]
print(voxelIntensities)

ncenters = 2
cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(voxelIntensities.reshape(1, voxelIntensities.size), ncenters, 2, error=0.005, maxiter=1000, init=None)
brain_ventricle_membership = np.zeros(brainImg.shape)
brain_ventricle_membership[brainMask &gt; 0] = u[0]

brain_parenchima_membership = np.ones(brainImg.shape)
brain_parenchima_membership[brainMask &gt; 0] = u[1]

volumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLScalarVolumeNode')
volumeNode.CreateDefaultDisplayNodes()
slicer.util.updateVolumeFromArray(volumeNode, brain_ventricle_membership)</code></pre>

---
