---
topic_id: 8850
title: "Igt Volume Reslice Driver Saving Images"
date: 2019-10-21
url: https://discourse.slicer.org/t/8850
---

# IGT Volume Reslice Driver - saving images

**Topic ID**: 8850
**Date**: 2019-10-21
**URL**: https://discourse.slicer.org/t/igt-volume-reslice-driver-saving-images/8850

---

## Post #1 by @aptirumalai (2019-10-21 17:59 UTC)

<p>I use the Endoscopy module to define a “flythrough” path and the IGT-&gt;VolumeResliceDriver to generate resliced images along the path, typically showing them on the Axial plane. This works fine and I am able to generate a flythrough. Is there a way to save the resliced images along with the transform associated with each resliced image? I would like to able to stack the resliced images together to visualize them and also have the ability to transform them back to the original coordinate system.</p>
<p>I am able to screen capture the images themselves during the flythrough - but I am interested in the capturing the underlying voxel data - before it has been mapped to RGB for displaying on the screen.</p>

---

## Post #2 by @lassoan (2019-10-22 13:09 UTC)

<p>Here is a complete script that saves the resliced images (and even projects them into a single 2D image to show X-ray or MIP view):</p>
<aside class="onebox githubgist">
  <header class="source">
      <a href="https://gist.github.com/lassoan/b445c734f118a5fb7643f3fb05f98b07" target="_blank" rel="nofollow noopener">gist.github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://gist.github.com/lassoan/b445c734f118a5fb7643f3fb05f98b07" target="_blank" rel="nofollow noopener">https://gist.github.com/lassoan/b445c734f118a5fb7643f3fb05f98b07</a></h4>
<h5>CurvedPlanarReformatting.py</h5>
<pre><code class="Python"># Get a dental CT scan
import SampleData
volumeNode = SampleData.SampleDataLogic().downloadDentalSurgery()[1]

# Define curve
curveNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsCurveNode')
curveNode.CreateDefaultDisplayNodes()
curveNode.GetCurveGenerator().SetNumberOfPointsPerInterpolatingSegment(25) # add more curve points between control points than the default 10
curveNode.AddControlPoint(vtk.vtkVector3d(-45.85526315789473,	-104.59210526315789,	74.67105263157896))
curveNode.AddControlPoint(vtk.vtkVector3d(-50.9078947368421,	-90.06578947368418,	66.4605263157895))</code></pre>
This file has been truncated. <a href="https://gist.github.com/lassoan/b445c734f118a5fb7643f3fb05f98b07" target="_blank" rel="nofollow noopener">show original</a>

<p>
</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>You can also save each sliceToWorldTransform in an array and use them to transform back from the warped space to the original image space.</p>
<p>What is your end goal? Dental panoramic X-ray, vessel analysis, …?</p>

---

## Post #3 by @ckolluru (2019-10-22 17:00 UTC)

<p>I’m interested in doing this for my dataset as well. I’m new to Slicer, so can someone explain what the process is to run a python script within it?</p>
<p>Can we also save the transformation so we can do the inverse operation on a different dataset? (let’s say we create segmentation labels for the formatted images and want to reformat them back to the original coordinates).</p>

---

## Post #4 by @lassoan (2019-10-22 20:59 UTC)

<aside class="quote no-group" data-username="ckolluru" data-post="3" data-topic="8850">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/ecccb3/48.png" class="avatar"> ckolluru:</div>
<blockquote>
<p>can someone explain what the process is to run a python script within it?</p>
</blockquote>
</aside>
<p>Press “Ctrl-3” and copy-paste the script to the console. See more information here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Tutorials_for_software_developers" class="inline-onebox">Documentation/Nightly/Training - Slicer Wiki</a></p>
<aside class="quote no-group" data-username="ckolluru" data-post="3" data-topic="8850">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/ecccb3/48.png" class="avatar"> ckolluru:</div>
<blockquote>
<p>Can we also save the transformation so we can do the inverse operation on a different dataset?</p>
</blockquote>
</aside>
<p>Yes, you can save the transforms in a Python list. It is a <code>vtkTransform</code> object, so you can easily get the inverse transform (<code>transform.GetInverse()</code>).</p>
<p>To transform an entire 3D object, you would probably want to have a single non-linear warping transform. You should be able to construct it by putting original and reformatted slice corners as control points in a grid or bspline transform. I think <a class="mention" href="/u/pieper">@pieper</a> implemented something like this.</p>

---

## Post #5 by @pieper (2019-10-22 21:19 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="8850">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I think <a class="mention" href="/u/pieper">@pieper</a> implemented something like this.</p>
</blockquote>
</aside>
<p>Yes, this code makes a grid transform based on two sets of slice corners:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L555-L718">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L555-L718" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L555-L718" target="_blank" rel="noopener">Slicer/Slicer/blob/main/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L555-L718</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="555" style="counter-reset: li-counter 554 ;">
          <li>    volumeNode = self.loadFilesWithSeriesReader("DCMTK", loadable.files, loadable.name + "-dcmtk", loadable.grayscale)</li>
          <li>    self.setVolumeNodeProperties(volumeNode, loadable)</li>
          <li></li>
          <li>    return volumeNode</li>
          <li></li>
          <li>def load(self, loadable, readerApproach=None):</li>
          <li>    """Load the select as a scalar volume using desired approach"""</li>
          <li>    # first, determine which reader approach the user prefers</li>
          <li>    if not readerApproach:</li>
          <li>        readerIndex = slicer.util.settingsValue("DICOM/ScalarVolume/ReaderApproach", 0, converter=int)</li>
          <li>        readerApproach = DICOMScalarVolumePluginClass.readerApproaches()[readerIndex]</li>
          <li>    # second, try to load with the selected approach</li>
          <li>    if readerApproach == "Archetype":</li>
          <li>        volumeNode = self.loadFilesWithArchetype(loadable.files, loadable.name)</li>
          <li>    elif readerApproach == "GDCM with DCMTK fallback":</li>
          <li>        volumeNode = self.loadFilesWithSeriesReader("GDCM", loadable.files, loadable.name, loadable.grayscale)</li>
          <li>        if not volumeNode:</li>
          <li>            volumeNode = self.loadFilesWithSeriesReader("DCMTK", loadable.files, loadable.name, loadable.grayscale)</li>
          <li>    else:</li>
          <li>        volumeNode = self.loadFilesWithSeriesReader(readerApproach, loadable.files, loadable.name, loadable.grayscale)</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L555-L718" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Note that in general this is not invertible.</p>

---

## Post #6 by @aptirumalai (2019-10-22 23:43 UTC)

<p>Thanks. I understand this needs the 4.11 Preview release of Slicer as “curveNode” is not defined in 4.10. I ran it and it appears to work. I will likely have follow-up questions. For now, I just wanted to share the information with the community.</p>

---

## Post #7 by @aptirumalai (2019-10-23 00:50 UTC)

<p>Thanks. I understand this needs the 4.11 Preview release of Slicer as “curveNode” is not defined in 4.10. I ran it and it appears to work. I will likely have follow-up questions. For now, I just wanted to share the information with the community.</p>

---

## Post #8 by @aptirumalai (2019-10-23 00:52 UTC)

<p>How do I set the size of each slice that is generated to a fixed size like 512x512? I would like the straightened volume to have a size of 512x512x(<span class="hashtag">#samplePointsAlongCurve</span>).</p>

---

## Post #9 by @lassoan (2019-10-23 04:46 UTC)

<p>Image is resliced using the vtkImageReslice filter built into the slice view pipeline, therefore the output image will match the slice view size. If this is not suitable for you then you need to instantiate a vtkImageReslice filter and set the inputs similarly as it is done <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Logic/vtkMRMLSliceLayerLogic.cxx" rel="nofollow noopener">here</a>.</p>

---

## Post #10 by @aptirumalai (2019-10-23 17:32 UTC)

<p>Can I use a similar approach with the Endoscopy module through Python to capture the underlying image data? I have done this but with a screen capture that gives me RGB data instead of the underlying voxel data. It appears that CurveNode does not sample the curve at equidistant intervals which would be desirable. I am guessing (or hoping) that the Endoscopy module’s “Create path” option does indeed produce sample points that are uniformly sampled by distance along the curve.</p>

---

## Post #11 by @pieper (2019-10-23 17:50 UTC)

<aside class="quote no-group" data-username="aptirumalai" data-post="10" data-topic="8850">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aptirumalai/48/6198_2.png" class="avatar"> aptirumalai:</div>
<blockquote>
<p>I am guessing (or hoping) that the Endoscopy module’s “Create path” option does indeed produce sample points that are uniformly sampled by distance along the curve.</p>
</blockquote>
</aside>
<p>Yes, the endoscopy path points are equally spaced, but it’s not integrated with the rest of the infrastructure describe here, so some programming would be required to make use of it.</p>

---

## Post #12 by @lassoan (2019-10-23 18:12 UTC)

<aside class="quote no-group" data-username="aptirumalai" data-post="10" data-topic="8850">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aptirumalai/48/6198_2.png" class="avatar"> aptirumalai:</div>
<blockquote>
<p>It appears that CurveNode does not sample the curve at equidistant intervals which would be desirable.</p>
</blockquote>
</aside>
<p>Since I wrote the example, an equidistant resampling functions have been implemented (see <a href="https://apidocs.slicer.org/master/classvtkMRMLMarkupsCurveNode.html#a9fa13674b9e92ab0b79abcbed4c84cb8">here</a>).</p>
<p>We should update Endoscopy module to use curve node (and probably also rename it to something more generic, as it is usable for many more things than just virtual endoscopy).</p>

---

## Post #13 by @pieper (2019-10-23 18:29 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="8850">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We should update Endoscopy module</p>
</blockquote>
</aside>
<p>Agreed - it was the very first python scripted module!</p>

---

## Post #14 by @aptirumalai (2019-10-30 17:31 UTC)

<p>What is the X,Y resolution (I mean mm/pixel) of the straightened volume in your sample code? Do they match the X,Y resolution of the input volume? So if my input volume had X,Y image spacing of 0.3 mm each, would the “axial” slices of the straightened volume have this same image spacing? This would mean I could make measurements on the “axial” slices and they would be correct.</p>

---

## Post #15 by @lassoan (2019-10-31 04:13 UTC)

<p>The resolution is just whatever is set in the slice viewer (what is the resolution of your monitor, how large is the slice view, and how much you zoom in). It has nothing to do with the volume’s spacing. If you want to control the resolution then you can use a separate vtkImageReslice filter.</p>

---

## Post #16 by @aptirumalai (2019-10-31 18:14 UTC)

<p>In your code, you are doing reslicing using:<br>
reslice = sliceLayerLogic.GetReslice()<br>
…<br>
tempSlice = vtk.vtkImageData()<br>
tempSlice.DeepCopy(reslice.GetOutput())<br>
…</p>
<p>My question has to do with this tempSlice. What is the pixel resolution of this vtiImage? I presume it has a resolution in mm/pixel that takes into the factors you mentioned - the size of the window, zoom etc.</p>
<p>To elaborate, let’s say I set my curveNode to be a straight line passing right through the middle of the volume along the Z-axis. So when I now reslice along the curveNode, I basically generate images that are the same as the Axial slices of the input volume (possibly zoomed in or out). So is there a notion of a pixel scale on these resliced images obtained this way? Can I make ruler measurements on one of these resliced images between two targets and get the same value that I would get on the same Axial slice from the input volume?</p>
<p>Thanks!</p>

---

## Post #17 by @lassoan (2019-10-31 18:36 UTC)

<p>You can get the field of view size (in mm) from the slice node. Pixel spacing is the field of view (in mm) divided by the size of the image (in pixels).</p>

---
