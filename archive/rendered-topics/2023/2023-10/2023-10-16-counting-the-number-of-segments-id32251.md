---
topic_id: 32251
title: "Counting The Number Of Segments"
date: 2023-10-16
url: https://discourse.slicer.org/t/32251
---

# Counting the number of segments

**Topic ID**: 32251
**Date**: 2023-10-16
**URL**: https://discourse.slicer.org/t/counting-the-number-of-segments/32251

---

## Post #1 by @FraP (2023-10-16 14:17 UTC)

<p>I have a volume from which I have segmented several scattered isolated structures. These are the nuclei of a group of cells.<br>
I need to count the number of these segments (nuclei).</p>
<p>Is there a function to do this?</p>
<p>Thank you for the kind answer</p>

---

## Post #2 by @pieper (2023-10-16 15:04 UTC)

<p>You could use Identify Islands plus Segment Statistics for that.  It won’t be efficient if you have over 100 islands or so.  You could write a quick python script to calculate the answer.</p>

---

## Post #3 by @FraP (2024-04-09 09:30 UTC)

<p>Thank you very much for your answer pieper.</p>
<p>As you anticipated, I was able to use this method on small files for tests but no longer on large files with many objects.<br>
Can you suggest me where to read material that will enable me to start writing python scripts?<br>
Can I run these scripts directly in 3D Slicer?</p>
<p>Thank you</p>

---

## Post #4 by @pieper (2024-04-09 12:19 UTC)

<p>You can start by reading through the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">script repository</a> to see what’s possible and then do some of the programming tutorials linked from <a href="http://slicer.org">slicer.org</a>.</p>

---

## Post #5 by @lassoan (2024-04-10 04:10 UTC)

<p>The filter that counts cells is called <a href="https://apidocs.slicer.org/master/classvtkITKIslandMath.html#details">vtkITKIslandMath</a>. For example:</p>
<pre data-code-wrap="python"><code class="lang-python">segmentationNode = getNode('Segmentation')
segmentID = segmentationNode.GetSegmentation().GetNthSegmentID(0)

# Get segment binary labelmap representation as vtkOrientedImageData
image = slicer.vtkOrientedImageData()
segmentationNode.GetBinaryLabelmapRepresentation(segmentID, image)

# Get number of islands
import vtkITK
islands = vtkITK.vtkITKIslandMath()
islands.SetInputData(image)
islands.SetMinimumSize(10)
islands.Update()
print(f"Found {islands.GetNumberOfIslands()} islands")
</code></pre>

---

## Post #6 by @FraP (2024-04-12 08:02 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="32251">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<pre><code class="lang-auto">segmentationNode = getNode('Segmentation')
segmentID = segmentationNode.GetSegmentation().GetNthSegmentID(0)

# Get segment binary labelmap representation as vtkOrientedImageData
image = slicer.vtkOrientedImageData()
segmentationNode.GetBinaryLabelmapRepresentation(segmentID, image)

# Get number of islands
import vtkITK
islands = vtkITK.vtkITKIslandMath()
islands.SetInputData(image)
islands.SetMinimumSize(10)
islands.Update()
print(f"Found {islands.GetNumberOfIslands()} islands")
</code></pre>
</blockquote>
</aside>
<p>Dear pieper and lassoan,<br>
thank you for your answers.</p>
<p>I tried to copy and post the script from lassoan in the Python Console of 3D Slicer replacing the text  “segmentID” with the name of my segment (“Nuclei”).<br>
And i got this error:<br>
Traceback (most recent call last):<br>
File “”, line 6, in <br>
NameError: name ‘Nuclei’ is not defined</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9878972b15cb5de149cf7f32f87448c5870528b.png" alt="image" data-base62-sha1="obJ4TD9JiQ5bL7wfhIjCsCJFfXZ" width="452" height="108"></p>
<p>I also tried to convert the segment in a module. But I get the same message.</p>

---

## Post #7 by @FraP (2024-04-12 09:19 UTC)

<p>When I run the script without changing anything in it I get this error.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e58f4c0c52babac29d440ff2570680aff1d06084.png" alt="image" data-base62-sha1="wKMlTZc9xDBbo3XiUUud7Ki19Eo" width="567" height="237"></p>

---

## Post #8 by @FraP (2024-04-12 15:49 UTC)

<p>Zooming in heavily on my images, I realized that I have very small islands accidentally selected by the threshold function. This increases the number of islands and could be the problem.</p>
<p>I cut the segments with the Scissor function to test the script a on smaller volume. I rounded the segments with the Smoothing function and eliminated the smaller islands with Remove small islands. After several progressively more aggressive attempts, I obtained a number of islands small enough to be counted with the script. However, on the original files I will definitely have more than 255 objects.<br>
Is there a possibility of counting more objects with a different script? Can the “maximum output pixel type” be increased?<br>
Or, is there a possibility of analyzing sequentially adjacent portions of the volume automatically and then summing up the results of the individual portions analyzed?</p>

---

## Post #9 by @muratmaga (2024-04-12 16:44 UTC)

<p>What is your modality? If you are working with microscopy, did you try more cell specific NN for this task? I am not sure where they stand with 3D data, but cellpose seems to have been developed specifically for this purpose.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/MouseLand/cellpose">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/MouseLand/cellpose" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/388;"><img src="https://repository-images.githubusercontent.com/237686847/007d8780-460c-11ea-9a4e-2fed096278b5" class="thumbnail" width="690" height="388"></div>

<h3><a href="https://github.com/MouseLand/cellpose" target="_blank" rel="noopener">GitHub - MouseLand/cellpose: a generalist algorithm for cellular segmentation...</a></h3>

  <p>a generalist algorithm for cellular segmentation with human-in-the-loop capabilities - MouseLand/cellpose</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #10 by @pieper (2024-04-12 16:52 UTC)

<p><code>vtkITKIslandMath</code> is probably just using the same scalar type as your input data.  So if you cast the data, wither in vtk or using the Cast Scalar Volume module you can use an integer type with more bits to support more islands.</p>

---

## Post #11 by @FraP (2024-04-18 15:57 UTC)

<p>thank you muratmaga. The segmentation of the cells into two dimensions has already been done by another method other than cellpose but which nevertheless worked adequately. Now I need to get the data out of the 3D files.</p>

---

## Post #12 by @FraP (2024-04-18 16:00 UTC)

<p>Thank you piper.<br>
I converted my volume in .vtk and performed again the segmentation as it was done before.</p>
<p>I used the code from <a href="https://discourse.slicer.org/u/lassoan">lassoan</a> and now I am stuck with this error:</p>
<blockquote>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\XX\AppData\Local\slicer.org\Slicer 5.6.2\bin\Python\slicer\util.py”, line 1566, in getNode<br>
raise MRMLNodeNotFoundException(“could not find nodes in the scene by name or id ‘%s’” % (pattern if (isinstance(pattern, str)) else “”))<br>
slicer.util.MRMLNodeNotFoundException: could not find nodes in the scene by name or id ‘Segmentation’</p>
</blockquote>
<p>Am I missing any steps in the segmentation?</p>

---

## Post #13 by @pieper (2024-04-18 17:00 UTC)

<p>The message is telling you that you need to use the name of the segmentation.  The first line of the script may need to be changed to say “Segmentation_1” or whatever the object in your scene is called.</p>

---

## Post #14 by @FraP (2024-04-19 08:38 UTC)

<p>In fact, that was the mistake. I corrected the code but now I get the same error as before.</p>
<blockquote>
<p>“Slicer has caught an application error, please save your work and restart.\n\nIf you have a repeatable sequence of steps that causes this message, please report the issue following instructions available at <a href="https://slicer.org" rel="noopener nofollow ugc">https://slicer.org</a>\n\n\nThe message detail is:\n\nException thrown in event: D:\D\S\S-0-build\ITK\Modules\Segmentation\ConnectedComponents\include\itkConnectedComponentImageFilter.hxx:144:\nITK ERROR: ConnectedComponentImageFilter(0000020DD9CDF300): Number of objects (836) greater than maximum of output pixel type (255).”</p>
</blockquote>
<p>With both .vtk and .nrrd volumes.</p>
<p>I have tried to use the “Cast Scalar Volume” module but the list of input volumes is empty even though I have loaded more than one volume with different formats.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d74b80f8f684d1d7e7d068714f7187e658b350b1.png" alt="image" data-base62-sha1="uIAqbhqElkhRaXDbcMW1P5IM0V3" width="578" height="157"></p>
<p>Do I need to do any steps beforehand?</p>

---

## Post #15 by @FraP (2024-04-19 14:18 UTC)

<p>The volume was not shown by Cast Scalar Volume because it had not been converted to scalar volume. I converted the volume with the Vector to Scalar Volume module and then used the Cast Scalar Volume module and tried to convert the volume to Int and to Float.<br>
I got the same error as before with both output types.</p>

---

## Post #16 by @pieper (2024-04-19 14:37 UTC)

<p>Looking closer, I see this line <code>segmentationNode.GetBinaryLabelmapRepresentation(segmentID, image) </code> is giving you the smallest datatype that can represent the number of input segments.</p>
<p>So you need to add this to the code after getting <code>image</code> from the <code>segmentationNode</code>:</p>
<pre><code class="lang-auto">cast = vtk.vtkImageCast()
cast.SetOutputScalarTypeToInt()
cast.SetInputData(image)
cast.Update()
#  to confirm
print(cast.GetOutputDataObject(0).GetScalarTypeAsString())
</code></pre>
<p>And then put <code>image</code> through <code>vtkITKIslandMath</code>.</p>

---

## Post #17 by @FraP (2024-04-19 16:47 UTC)

<p>This is the code I got now but I still get the same error.</p>
<pre><code class="lang-auto">segmentationNode = getNode('Segmentation')
segmentID = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName("Nuclei")

# Get segment binary labelmap representation as vtkOrientedImageData
image = slicer.vtkOrientedImageData()
segmentationNode.GetBinaryLabelmapRepresentation(segmentID, image)

#  cast vtk.vtkImageCast
cast = vtk.vtkImageCast()
cast.SetOutputScalarTypeToInt()
cast.SetInputData(image)
cast.Update()
#  to confirm
print(cast.GetOutputDataObject(0).GetScalarTypeAsString())


# Get number of islands
import vtkITK
islands = vtkITK.vtkITKIslandMath()
islands.SetInputData(image)
islands.SetMinimumSize(10)
islands.Update()
print(f"Found {islands.GetNumberOfIslands()} islands")

</code></pre>
<p>However, the part of the code you suggest to add works and prints “int” at the end of the code and before the error.</p>

---

## Post #18 by @pieper (2024-04-19 16:49 UTC)

<p>You need to also change <code>islands.SetInputData(image)</code> to <code>islands.SetInputData(cast.GetOutputDataObject(0))</code></p>

---

## Post #19 by @FraP (2024-04-22 10:15 UTC)

<aside class="quote no-group" data-username="pieper" data-post="16" data-topic="32251">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>vtkITKIslandMath</p>
</blockquote>
</aside>
<p>Thank you!!!<br>
Now it’s working perfectly <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=12" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20"></p>

---
