---
topic_id: 18604
title: "Slicer Convert Centerlines To A Graph V E"
date: 2021-07-09
url: https://discourse.slicer.org/t/18604
---

# Slicer - Convert centerlines to a graph {V,E}

**Topic ID**: 18604
**Date**: 2021-07-09
**URL**: https://discourse.slicer.org/t/slicer-convert-centerlines-to-a-graph-v-e/18604

---

## Post #1 by @som1197 (2021-07-09 15:55 UTC)

<p>Hello,</p>
<p>I want to convert the centerline network generated from the segmentations of the Circle of Willis into a graph data structure. Currently the only way to do it in vmtk is to use the <strong>‘vmtknetworkextraction’</strong> class to do so - <a href="http://www.vmtk.org/vmtkscripts/vmtknetworkextraction.html" rel="noopener nofollow ugc">VMTK network extraction</a>. However, it required the input to be a surface file.</p>
<p>In my case, I have a centerline tree hierarchical structure already generated in slicer as shown.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/309d7940e0e25a607e520c8acf651e1fb4fe339f.png" data-download-href="/uploads/short-url/6W4iRMcKbxjLc4evQCWxhFfYFyf.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/309d7940e0e25a607e520c8acf651e1fb4fe339f_2_690x361.png" alt="image" data-base62-sha1="6W4iRMcKbxjLc4evQCWxhFfYFyf" width="690" height="361" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/309d7940e0e25a607e520c8acf651e1fb4fe339f_2_690x361.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/309d7940e0e25a607e520c8acf651e1fb4fe339f_2_1035x541.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/309d7940e0e25a607e520c8acf651e1fb4fe339f_2_1380x722.png 2x" data-dominant-color="BCBEDD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1702×891 170 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I can use the .json files containing the centerline curve information to create a graph using the NetworkX library in Python. But is there a way to directly convert the Centerline model_1.vtk file into a graph using the connectivity information stored as an ordered dictionary?</p>
<p>I am using the following code to get numpy arrays from the vtk file.</p>
<pre><code class="lang-auto"># Using vmtk
filename = 'Centerline model_1.vtk'
centerlineReader = vmtkscripts.vmtkSurfaceReader()
centerlineReader.InputFileName = filename
centerlineReader.Execute()
clNumpyAdaptor = vmtkscripts.vmtkCenterlinesToNumpy()
clNumpyAdaptor.Centerlines = centerlineReader.Surface
clNumpyAdaptor.Execute()
numpyCenterlines = clNumpyAdaptor.ArrayDict
</code></pre>
<p>I get the following as an output:<br>
Points:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4bc40e657ffb82056aa1d7e073b36635dcf8248c.png" alt="image" data-base62-sha1="aOfRflRATh7qh6rR5HTFpbNykZm" width="599" height="191"></p>
<p>PointData:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f57b84fcdb882c18f9e1419e9038c8298955dbc.png" data-download-href="/uploads/short-url/4tgJVqYP70vet3gCbnQFUjaACao.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f57b84fcdb882c18f9e1419e9038c8298955dbc.png" alt="image" data-base62-sha1="4tgJVqYP70vet3gCbnQFUjaACao" width="690" height="233" data-dominant-color="212A34"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">758×257 5.92 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>What does ‘EdgeArray’ and ‘EdgePCoordarray’ mean here? How do they represent the edge connectivity of the 1D centerline tree?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/108ee57991b71b709b10068415458b9427b29c17.png" alt="image" data-base62-sha1="2mtNcGwunqs9oSkKhbgLujoQ5TN" width="490" height="189"></p>
<p>CellData:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/03707e309dc775430e0af16831e87ddb35bc68c8.png" data-download-href="/uploads/short-url/uqrJO9IIkJwkKya4MiWAAoUDVu.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/03707e309dc775430e0af16831e87ddb35bc68c8.png" alt="image" data-base62-sha1="uqrJO9IIkJwkKya4MiWAAoUDVu" width="690" height="413" data-dominant-color="2C353E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">824×494 14.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2021-07-11 15:54 UTC)

<p>You could easily add an option to the Extract Centerline module in Slicer to create the graph representation you need. See source code <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/ExtractCenterline/ExtractCenterline.py#L1068-L1110">here</a> that generates a hierarchy of curves, with a little change you can put the point lists into a Python dictionary instead. If you send a pull request with the proposed changes then we’ll be happy to merge it.</p>

---

## Post #3 by @som1197 (2021-07-16 04:42 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a>  for the piece of code. Yes I will send out a pull request with the proposed changes soon.</p>
<p>Moreover, I also wanted to know if scalar values of <strong>‘GroupIDsarray’, ‘TortuosityArray’ , ‘BlankingArray’</strong> etc. can be incorporated in the centerline model. I generated the following plots by using the conventional vmtkscripts, but it does not always work correctly.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/882e1766835d9ccda430877ca40183bae29a5bd9.png" data-download-href="/uploads/short-url/jqHGyowNdWvgyzlPhTSWkm8WuLf.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/882e1766835d9ccda430877ca40183bae29a5bd9_2_690x303.png" alt="image" data-base62-sha1="jqHGyowNdWvgyzlPhTSWkm8WuLf" width="690" height="303" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/882e1766835d9ccda430877ca40183bae29a5bd9_2_690x303.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/882e1766835d9ccda430877ca40183bae29a5bd9_2_1035x454.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/882e1766835d9ccda430877ca40183bae29a5bd9.png 2x" data-dominant-color="FAFBFA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1261×554 92.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2bd69ea780065406186d299c62ef460f2e619001.jpeg" data-download-href="/uploads/short-url/6fOlOJI887Nb8UlKiJxOxgJHHeV.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2bd69ea780065406186d299c62ef460f2e619001_2_560x500.jpeg" alt="image" data-base62-sha1="6fOlOJI887Nb8UlKiJxOxgJHHeV" width="560" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2bd69ea780065406186d299c62ef460f2e619001_2_560x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2bd69ea780065406186d299c62ef460f2e619001.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2bd69ea780065406186d299c62ef460f2e619001.jpeg 2x" data-dominant-color="F6F7F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">764×682 93.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Currently there are only 3 ways to postprocess the centerline data as shown here.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/efab10cb0050f2cad8831bc139d9d91baabdd09b.png" data-download-href="/uploads/short-url/yccCy9UAA1AHL2FEqiE6fGXqCUj.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/efab10cb0050f2cad8831bc139d9d91baabdd09b_2_690x246.png" alt="image" data-base62-sha1="yccCy9UAA1AHL2FEqiE6fGXqCUj" width="690" height="246" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/efab10cb0050f2cad8831bc139d9d91baabdd09b_2_690x246.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/efab10cb0050f2cad8831bc139d9d91baabdd09b_2_1035x369.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/efab10cb0050f2cad8831bc139d9d91baabdd09b.png 2x" data-dominant-color="F1F3F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1230×439 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ul>
<li>
<p>However, can we make any changes here in the base code to store values of other arrays as well?</p>
</li>
<li>
<p>Also would it be possible to run this function independently in a separate python code given the vtkpolymesh surface data and the endpoint co ordinates?</p>
</li>
</ul>
<aside class="onebox githubblob" data-onebox-src="https://github.com/vmtk/SlicerExtension-VMTK/blob/995027f17f195d802134f799aab095ea31f3e6c5/ExtractCenterline/ExtractCenterline.py#L635-L723">
  <header class="source">

      <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/995027f17f195d802134f799aab095ea31f3e6c5/ExtractCenterline/ExtractCenterline.py#L635-L723" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/995027f17f195d802134f799aab095ea31f3e6c5/ExtractCenterline/ExtractCenterline.py#L635-L723" target="_blank" rel="noopener nofollow ugc">vmtk/SlicerExtension-VMTK/blob/995027f17f195d802134f799aab095ea31f3e6c5/ExtractCenterline/ExtractCenterline.py#L635-L723</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="635" style="counter-reset: li-counter 634 ;">
          <li>def extractCenterline(self, surfacePolyData, endPointsMarkupsNode, curveSamplingDistance=1.0):
</li>
          <li>    """Compute centerline.
</li>
          <li>    This is more robust and accurate but takes longer than the network extraction.
</li>
          <li>    :param surfacePolyData:
</li>
          <li>    :param endPointsMarkupsNode:
</li>
          <li>    :return:
</li>
          <li>    """
</li>
          <li>
</li>
          <li>    import vtkvmtkComputationalGeometryPython as vtkvmtkComputationalGeometry
</li>
          <li>    import vtkvmtkMiscPython as vtkvmtkMisc
</li>
          <li>
</li>
          <li>    # Cap all the holes that are in the mesh that are not marked as endpoints
</li>
          <li>    # Maybe this is not needed.
</li>
          <li>    capDisplacement = 0.0
</li>
          <li>    surfaceCapper = vtkvmtkComputationalGeometry.vtkvmtkCapPolyData()
</li>
          <li>    surfaceCapper.SetInputData(surfacePolyData)
</li>
          <li>    surfaceCapper.SetDisplacement(capDisplacement)
</li>
          <li>    surfaceCapper.SetInPlaneDisplacement(capDisplacement)
</li>
          <li>    surfaceCapper.Update()
</li>
          <li>
</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/995027f17f195d802134f799aab095ea31f3e6c5/ExtractCenterline/ExtractCenterline.py#L635-L723" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>This has been done for the network curves but the centerline curves hold the real information.</p><aside class="onebox githubblob" data-onebox-src="https://github.com/vmtk/SlicerExtension-VMTK/blob/995027f17f195d802134f799aab095ea31f3e6c5/ExtractCenterline/ExtractCenterline.py#L616-L633">
  <header class="source">

      <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/995027f17f195d802134f799aab095ea31f3e6c5/ExtractCenterline/ExtractCenterline.py#L616-L633" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/995027f17f195d802134f799aab095ea31f3e6c5/ExtractCenterline/ExtractCenterline.py#L616-L633" target="_blank" rel="noopener nofollow ugc">vmtk/SlicerExtension-VMTK/blob/995027f17f195d802134f799aab095ea31f3e6c5/ExtractCenterline/ExtractCenterline.py#L616-L633</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="616" style="counter-reset: li-counter 615 ;">
          <li>if computeGeometry:
</li>
          <li>    centerlineGeometry = vtkvmtkComputationalGeometry.vtkvmtkCenterlineGeometry()
</li>
          <li>    centerlineGeometry.SetInputData(networkExtraction.GetOutput())
</li>
          <li>    centerlineGeometry.SetLengthArrayName(self.lengthArrayName)
</li>
          <li>    centerlineGeometry.SetCurvatureArrayName(self.curvatureArrayName)
</li>
          <li>    centerlineGeometry.SetTorsionArrayName(self.torsionArrayName)
</li>
          <li>    centerlineGeometry.SetTortuosityArrayName(self.tortuosityArrayName)
</li>
          <li>    centerlineGeometry.SetFrenetTangentArrayName(self.frenetTangentArrayName)
</li>
          <li>    centerlineGeometry.SetFrenetNormalArrayName(self.frenetNormalArrayName)
</li>
          <li>    centerlineGeometry.SetFrenetBinormalArrayName(self.frenetBinormalArrayName)
</li>
          <li>    # centerlineGeometry.SetLineSmoothing(0)
</li>
          <li>    # centerlineGeometry.SetOutputSmoothedLines(0)
</li>
          <li>    # centerlineGeometry.SetNumberOfSmoothingIterations(100)
</li>
          <li>    # centerlineGeometry.SetSmoothingFactor(0.1)
</li>
          <li>    centerlineGeometry.Update()
</li>
          <li>    return centerlineGeometry.GetOutput()
</li>
          <li>else:
</li>
          <li>    return networkExtraction.GetOutput()
</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @lassoan (2021-07-17 05:54 UTC)

<aside class="quote no-group" data-username="som1197" data-post="3" data-topic="18604">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/som1197/48/14945_2.png" class="avatar"> som1197:</div>
<blockquote>
<p>Moreover, I also wanted to know if scalar values of <strong>‘GroupIDsarray’, ‘TortuosityArray’ , ‘BlankingArray’</strong> etc. can be incorporated in the centerline model.</p>
</blockquote>
</aside>
<p>Yes, sure. These are cell data (one value for each branch) and the values are saved in the table where you can easily look them up (by cell ID) but feel free to add it to the centerline tree model as well. Send a pull request with the proposed changes.</p>
<aside class="quote no-group" data-username="som1197" data-post="3" data-topic="18604">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/som1197/48/14945_2.png" class="avatar"> som1197:</div>
<blockquote>
<p>However, can we make any changes here in the base code to store values of other arrays as well?</p>
</blockquote>
</aside>
<p>Yes, just send a pull request if you have any suggestion.</p>
<aside class="quote no-group" data-username="som1197" data-post="3" data-topic="18604">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/som1197/48/14945_2.png" class="avatar"> som1197:</div>
<blockquote>
<p>Also would it be possible to run this function independently in a separate python code given the vtkpolymesh surface data and the endpoint co ordinates?</p>
</blockquote>
</aside>
<p>You can use the module from anywhere (from a Python script, without a GUI; from Jupyter notebooks, etc.). See complete example here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/ExtractCenterline/ExtractCenterline.py#L1157-L1186">
  <header class="source">

      <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/ExtractCenterline/ExtractCenterline.py#L1157-L1186" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/ExtractCenterline/ExtractCenterline.py#L1157-L1186" target="_blank" rel="noopener">vmtk/SlicerExtension-VMTK/blob/master/ExtractCenterline/ExtractCenterline.py#L1157-L1186</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="1157" style="counter-reset: li-counter 1156 ;">
          <li>your test should break so they know that the feature is needed.
</li>
          <li>"""
</li>
          <li>
</li>
          <li>self.delayDisplay("Starting the test")
</li>
          <li>
</li>
          <li># Get/create input data
</li>
          <li>
</li>
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
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/ExtractCenterline/ExtractCenterline.py#L1157-L1186" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @RomanStriker (2022-11-08 18:56 UTC)

<p>Hi, can you share your code for generating centerline curves colored by centerlineIDs. I am trying to separate the centerlines into different segments (branches).</p>

---

## Post #6 by @lassoan (2022-11-12 03:41 UTC)

<p>The code for splitting the tree to branches is here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/vmtk/SlicerExtension-VMTK/blob/437526ad4a097483d25b9591ab74548ab9ae0176/ExtractCenterline/ExtractCenterline.py#L832-L1013">
  <header class="source">

      <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/437526ad4a097483d25b9591ab74548ab9ae0176/ExtractCenterline/ExtractCenterline.py#L832-L1013" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/437526ad4a097483d25b9591ab74548ab9ae0176/ExtractCenterline/ExtractCenterline.py#L832-L1013" target="_blank" rel="noopener">vmtk/SlicerExtension-VMTK/blob/437526ad4a097483d25b9591ab74548ab9ae0176/ExtractCenterline/ExtractCenterline.py#L832-L1013</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="832" style="counter-reset: li-counter 831 ;">
          <li>def createCurveTreeFromCenterline(self, centerlinePolyData, centerlineCurveNode=None, centerlinePropertiesTableNode=None, curveSamplingDistance=1.0):
</li>
          <li>
</li>
          <li>    import vtkvmtkComputationalGeometryPython as vtkvmtkComputationalGeometry
</li>
          <li>
</li>
          <li>    branchExtractor = vtkvmtkComputationalGeometry.vtkvmtkCenterlineBranchExtractor()
</li>
          <li>    branchExtractor.SetInputData(centerlinePolyData)
</li>
          <li>    branchExtractor.SetBlankingArrayName(self.blankingArrayName)
</li>
          <li>    branchExtractor.SetRadiusArrayName(self.radiusArrayName)
</li>
          <li>    branchExtractor.SetGroupIdsArrayName(self.groupIdsArrayName)
</li>
          <li>    branchExtractor.SetCenterlineIdsArrayName(self.centerlineIdsArrayName)
</li>
          <li>    branchExtractor.SetTractIdsArrayName(self.tractIdsArrayName)
</li>
          <li>    branchExtractor.Update()
</li>
          <li>    centerlines = branchExtractor.GetOutput()
</li>
          <li>
</li>
          <li>    mergeCenterlines = vtkvmtkComputationalGeometry.vtkvmtkMergeCenterlines()
</li>
          <li>    mergeCenterlines.SetInputData(centerlines)
</li>
          <li>    mergeCenterlines.SetRadiusArrayName(self.radiusArrayName)
</li>
          <li>    mergeCenterlines.SetGroupIdsArrayName(self.groupIdsArrayName)
</li>
          <li>    mergeCenterlines.SetCenterlineIdsArrayName(self.centerlineIdsArrayName)
</li>
          <li>    mergeCenterlines.SetTractIdsArrayName(self.tractIdsArrayName)
</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/437526ad4a097483d25b9591ab74548ab9ae0176/ExtractCenterline/ExtractCenterline.py#L832-L1013" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @RomanStriker (2022-11-14 12:35 UTC)

<p>Thanks. I used the function to get the curve tree but I see that it is not very consistent with the centerline model near bifurcations. I was hoping I could just classify nodes and edges in the centerline model directly.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2c96ed48b9d7752d61603e727e537c604504612.jpeg" data-download-href="/uploads/short-url/rNacexri7c4k6YleTv3g3CWaQJc.jpeg?dl=1" title="Screenshot from 2022-11-14 13-30-38" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2c96ed48b9d7752d61603e727e537c604504612_2_687x500.jpeg" alt="Screenshot from 2022-11-14 13-30-38" data-base62-sha1="rNacexri7c4k6YleTv3g3CWaQJc" width="687" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2c96ed48b9d7752d61603e727e537c604504612_2_687x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2c96ed48b9d7752d61603e727e537c604504612_2_1030x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2c96ed48b9d7752d61603e727e537c604504612.jpeg 2x" data-dominant-color="8B93B7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2022-11-14 13-30-38</span><span class="informations">1182×860 124 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
