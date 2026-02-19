---
topic_id: 7918
title: "Manually Creating A Multivolume"
date: 2019-08-07
url: https://discourse.slicer.org/t/7918
---

# Manually creating a multiVolume

**Topic ID**: 7918
**Date**: 2019-08-07
**URL**: https://discourse.slicer.org/t/manually-creating-a-multivolume/7918

---

## Post #1 by @rbahegne (2019-08-07 14:44 UTC)

<p>Hello world,</p>
<p>I’m receiving dicom data from a websocket connection and i’m able to display it in a volume node. Thing is, now i’m receive dicom data from a temporal serie and i want to display it as a multiVolumeNode.</p>
<p>I suppose i need to fill a vtkMRMLMultiVolumeNode with several nodes and then create a  vtkMRMLMultiVolumeDisplayNode, but i did not found any documentation and the member functions available on those objects are not really what i expected.</p>
<p>Does anyone could give me some guidelines to proceed ?</p>
<p>Thanks a lot!</p>

---

## Post #2 by @pieper (2019-08-07 22:15 UTC)

<p>Hi -</p>
<p>Probably the best is to look at <a href="https://github.com/fedorov/MultiVolumeImporter" rel="nofollow noopener">the multivolume importer code</a> and follow that pattern.</p>
<p>Or you could consider using <a href="https://github.com/SlicerRt/Sequences" rel="nofollow noopener">Sequences</a> which can also handle time series volumes, but also time series transforms, fiducials, and other data types.</p>
<p>-Steve</p>

---

## Post #3 by @rbahegne (2019-08-08 15:08 UTC)

<p>Thanks for the information, after reading and re-reading  this code (the multivolume importer one) there is something i still don’t understand.</p>
<p>Seems to me that the point of the onImportButtonClicked function is to fill the mvImageArray with the data of each frame (and then put it in some node). This is done line 259 :</p>
<blockquote>
<p>for frameId in range(nFrames):<br>
# TODO: check consistent size and orientation!<br>
frame = frames[frameId]<br>
frameImage = frame.GetImageData()<br>
frameImageArray = vtk.util.numpy_support.vtk_to_numpy(frameImage.GetPointData().GetScalars())<br>
mvImageArray.T[frameId] = frameImageArray</p>
</blockquote>
<p>Once complete mvImageArray is not used anywhere else, how come ?</p>

---

## Post #4 by @pieper (2019-08-08 15:29 UTC)

<p>The mvImageArray is actually a numpy view of the vtkImageData that stores the multivolume, so when the image data is assigned into the frame it becomes available as part of the mrml scene.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/fedorov/MultiVolumeImporter/blob/master/MultiVolumeImporter.py#L241-L246" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/fedorov/MultiVolumeImporter/blob/master/MultiVolumeImporter.py#L241-L246" target="_blank" rel="nofollow noopener">fedorov/MultiVolumeImporter/blob/master/MultiVolumeImporter.py#L241-L246</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="241" style="counter-reset: li-counter 240 ;">
<li>extent = frame0.GetImageData().GetExtent()</li>
<li>numPixels = float(extent[1]+1)*(extent[3]+1)*(extent[5]+1)*nFrames</li>
<li>scalarType = frame0.GetImageData().GetScalarType()</li>
<li>print('Will now try to allocate memory for '+str(numPixels)+' pixels of VTK scalar type '+str(scalarType))</li>
<li>print('Memory allocated successfully')</li>
<li>mvImageArray = vtk.util.numpy_support.vtk_to_numpy(mvImage.GetPointData().GetScalars())</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #5 by @rbahegne (2019-08-09 09:31 UTC)

<p>Sorry but i’m not really good at python and i’m a doing a loadable module in C++</p>
<p>So i’m not sure of what does the line and what a c++ equivalent should be :</p>
<blockquote>
<p>mvImageArray = vtk.util.numpy_support.vtk_to_numpy(mvImage.GetPointData().GetScalars())</p>
</blockquote>
<p>The multivolume is stored in only one vtkImageData ? You don’t need a array of it to store the several volumes ?</p>
<pre><code class="lang-auto"></code></pre>

---

## Post #6 by @pieper (2019-08-09 20:47 UTC)

<p>The python VTK API code will translate directly to C++ and the numpy assignments need to become memcpy calls or similar, so you should be able to follow through the python code to get what you need.  A few lines up in the file you’ll see that part that sets the extent and allocates the memory for the vtkImageData based on the number of frames (yes, the frames are ‘components’ of the same image data).</p>

---

## Post #7 by @lassoan (2019-08-10 18:02 UTC)

<p>You can use Sequences extension’s recording capability for creating time sequences in real-time. We use it extensively for recording and replaying ultrasound images and tool positions in real-time.</p>
<p>All you need to do is to create a volume node, set it as a proxy node in “Sequence browser” module, and start recording. If you update the volume node, the new item will be automatically added to the sequence. You can start/stop recording, replay, save to nrrd or mkv file, etc. Compressed video streams are supported, too.</p>
<p>Note that Slicer can already receive images, transforms, models, points, strings, etc. through <a href="http://www.openigtlink.org" rel="nofollow noopener">OpenIGTLink</a>, a very simple socket-based protocol. If you choose this protocol then you don’t need to implement anything, you can already receive, display, record, replay, save real-time image and other data (using SlicerOpenIGTLink, SlicerIGSIO, and SlicerIGT modules).</p>
<p><a href="https://www.plustoolkit.org" rel="nofollow noopener">Plus toolkit</a> can connect to a wide range of devices and send data through OpenIGTLink protocol to Slicer. So, maybe a solution is already available for your needs. <strong>What kind of images do you receive, from what device?</strong></p>

---

## Post #8 by @rbahegne (2019-08-13 15:15 UTC)

<p>Thank you for your answer, I already dug out the IGT and Plus toolkit solution but I receive dicom files straight from a MRI via a specific API.</p>
<p>I think i’m almost there for the multiVolume solution. I may have a look to the sequence solution also.</p>
<p>For now i think, i correctly set up frames, image data, component and so on.</p>
<p>But i can’t access any specific function from the vtkMRMLMultiVolumeNode Class.<br>
For instance :</p>
<blockquote>
<pre><code>    mVolumeNode-&gt;CreateDefaultDisplayNodes();
    mVolumeNode-&gt;CreateDefaultStorageNode();
    mVolumeNode-&gt;SetNumberOfFrames(10); 
</code></pre>
</blockquote>
<p>got me a compilation error : undefined reference to `vtkMRMLMultiVolumeNode::SetNumberOfFrames(int)’</p>
<p>I correctly set  <span class="hashtag-raw">#include</span> &lt;vtkMRMLMultiVolumeNode.h&gt; and this file is located in the slicer-super-build as i think it should be. There is no problem or warning with the include so I’m quite helpless.</p>
<p>These functions are somehow private ? In the python example i did not notice any special thing with them.</p>

---

## Post #9 by @lassoan (2019-08-13 15:43 UTC)

<p>MultiVolume has very limited capabilities, does not work for IGT applications, and will be deprecated within 1-2 years, so instead of trying to fix the MultiVolume based solution, I would recommend use Sequences infrastructure for your project.</p>

---
