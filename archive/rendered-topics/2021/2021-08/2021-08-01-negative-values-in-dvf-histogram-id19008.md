# Negative Values in DVF Histogram

**Topic ID**: 19008
**Date**: 2021-08-01
**URL**: https://discourse.slicer.org/t/negative-values-in-dvf-histogram/19008

---

## Post #1 by @toyama (2021-08-01 03:44 UTC)

<p>We are looking for a histogram of the DVF.<br>
The DVF should not have any negative values, but when I calculated the histogram from the DVF created by the transform module, it took negative values.<br>
What do these negative values mean?<br>
Also, I am converting a REG file created by MIMmaestro into a vector field by the transform module.<br>
Will this procedure create the same creation in 3DSlicer as the one created in MIMmaestro?<br>
I hope you can answer my question.</p>

---

## Post #2 by @lassoan (2021-08-01 21:35 UTC)

<p>It is expected that the displacement vector field contains negative values. Only the displacement magnitude is always postitive.</p>
<p>You can compare the difference between two displacement fields by loading them as transforms, invert one of them and apply it on the other.</p>

---

## Post #3 by @toyama (2021-08-02 08:08 UTC)

<p>Thank you for your answer.<br>
Is it correct to say that the DVF is transformed correctly in the transform module?<br>
I am sorry for my lack of knowledge, but I would like to know about the negative value of DVF.<br>
I didn’t have an image of DVF having a negative value because it is a vector shift amount.<br>
I would like to know how DVF is defined in 3DSlicer and how negative values are generated.<br>
I hope you can answer my question.</p>

---

## Post #4 by @pieper (2021-08-02 11:46 UTC)

<aside class="quote no-group" data-username="toyama" data-post="3" data-topic="19008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/82dd89/48.png" class="avatar"> toyama:</div>
<blockquote>
<p>Is it correct to say that the DVF is transformed correctly in the transform module?</p>
</blockquote>
</aside>
<p>We believe so, yes.</p>
<aside class="quote no-group" data-username="toyama" data-post="3" data-topic="19008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/82dd89/48.png" class="avatar"> toyama:</div>
<blockquote>
<p>I would like to know how DVF is defined in 3DSlicer and how negative values are generated.</p>
</blockquote>
</aside>
<p>Deformation vector fields are represented as “grid transforms” in Slicer, a special case of <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/transforms.html">general transforms</a> where there is an image-like set of regularly spaced vectors defining the deformation field.  Each vector defines a local displacement in patient space, the components of which can be positive or negative to indicate the local displacement.</p>

---

## Post #5 by @toyama (2021-08-03 09:09 UTC)

<p>Thank you for your answer.<br>
It was helpful because I was not sure if the method of converting the grid to DVF in the transform module was correct.<br>
What do you mean by “the components of which can be positive or negative to indicate the local displacement.” I know that DVF takes 0 if nothing changes, but I don’t know what negative DVF means.<br>
Please let me know if you can help me.<br>
I hope you can answer my question.</p>

---

## Post #6 by @pieper (2021-08-03 12:37 UTC)

<p>The key point is what Andras mentioned above.  The deformation vector field itself can have positive or negative components (three values: left/right, front/back, up/down) but the magnitude, or length of the vector or amount of movement, is a single value that is always positive or zero if there is no displacement.</p>

---

## Post #7 by @toyama (2021-08-04 09:08 UTC)

<p>Thank you for your answer.<br>
I see that 3DSlicer determines the positive and negative values for left/right, front/back, and up/down.<br>
If so, I think the voxel value displayed in the histogram will be the sum of the three positive and negative values, but what does the negative value mean when the three are combined?<br>
I do not understand the idea of the negative value of the three elements combined.<br>
fig:DVFhistogram<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac7bc145a2bdcb635e6c3503ff175927bdc21bdc.png" alt="image" data-base62-sha1="oBRgEWkeMz0BNXgk1oPtz38qJU8" width="674" height="449"></p>

---

## Post #8 by @lassoan (2021-08-04 13:11 UTC)

<p>Slicer just provide all the vectors in a numpy array and you combine the values. So, the behavior is whatever you implement.</p>
<p>If you are interested in plotting the displacement magnitude then you can compute the norm of the vectors before computing the histogram. Since the processing of numpy arrays using numpy is unrelated to Slicer, you should be able to find solution on Stackoverflow or various generic Python tutorials and forums.</p>

---

## Post #9 by @toyama (2021-08-04 14:07 UTC)

<p>Thank you for your answer.<br>
So you are saying that the result of summing the three axes of the numpy array, not just one axis of the histogram, is a positive or negative value.<br>
Out of the blue, clinically speaking, does a negative value of DVF represent volume shrinkage and a positive value represent expansion?<br>
If you know, please let me know.</p>

---

## Post #10 by @pieper (2021-08-04 14:19 UTC)

<p>No, the positive or negative elements of the displacement vector do not individually tell you about shrinking or expansion in a clinical sense.</p>
<p>For that you would use the <a href="https://en.wikipedia.org/wiki/Jacobian_matrix_and_determinant#Jacobian_determinant">determinant of the Jacobian</a> matrix to give you a localized measurement.  But that signal is probably very noisy in clinical images so people typically use overall volume change from a segmented image or a change in length of the maximum diameter.</p>

---

## Post #11 by @toyama (2021-08-04 15:27 UTC)

<p>Thank you for your answer.<br>
So, are negative values of DVF in 3DSlicer just the result of the sum of the three axes and have no particular clinical significance?</p>

---

## Post #12 by @pieper (2021-08-04 15:59 UTC)

<aside class="quote no-group" data-username="toyama" data-post="11" data-topic="19008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/82dd89/48.png" class="avatar"> toyama:</div>
<blockquote>
<p>So, are negative values of DVF in 3DSlicer just the result of the sum of the three axes and have no particular clinical significance?</p>
</blockquote>
</aside>
<p>I don’t think so, no.  It’s not clear to me what you would use that kind of plot for.</p>

---

## Post #13 by @toyama (2021-08-05 05:59 UTC)

<p>I am trying to get a histogram of the DVF, which I think will help me understand how the segments were changed by the DIR (scaling up, down, translating).<br>
I thought about the Jacobian, but I started with the DVF, which is the result of the DIR itself.<br>
Then I thought that a negative value of DVF might represent a contraction of DIR.<br>
Doesn’t I make much sense to check the DVF?<br>
I am embarrassed to say this, but I would like to know if there is any mistake.<br>
I ask again, does this mean that the calculation of the 3 axes to find the DVF value is out of 3DSlicer’s jurisdiction?</p>

---

## Post #14 by @lassoan (2021-08-05 12:49 UTC)

<p>Average translation in a region of interest is easy to compute: it is simply the mean computed for each displacement component. “Scaling up/down” of a region is also easy to get, by using volume or bounding box metrics provided by <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html">Segment Statistics module</a>.</p>
<p>There are extensions for more detailed, quantitative analysis, including computing Jacobian determinant and various statistics. See for example <a href="https://github.com/gsi-biomotion/SlicerRegistrationQA/blob/master/Documentation.md">RegistrationQA extension</a>.</p>
<p>You can also do any custom quantitative analysis in a few lines of Python code, using any Python packages, numpy, ITK, VTK, etc.</p>

---

## Post #15 by @toyama (2021-08-05 14:41 UTC)

<p>Thanks for the answer.<br>
I used the segment statistics module to get the displacement field (DVF) statistics from Scalar volume statistics. Does this result show positive as expansion and negative as contraction?<br>
The bounding box says “Oriented bounding box: the non-axis aligned bounding box that encompasses the segment”. Is this also suitable for interpreting DVF changes?</p>
<p>Let me add a question to my previous answer.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60429e1f46d8956156fbad2436f96d96f43c55a3.png" data-download-href="/uploads/short-url/dJyz1hWCV2czL8zNCOhW2mQuqSn.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60429e1f46d8956156fbad2436f96d96f43c55a3_2_690x101.png" alt="image" data-base62-sha1="dJyz1hWCV2czL8zNCOhW2mQuqSn" width="690" height="101" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60429e1f46d8956156fbad2436f96d96f43c55a3_2_690x101.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60429e1f46d8956156fbad2436f96d96f43c55a3.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60429e1f46d8956156fbad2436f96d96f43c55a3.png 2x" data-dominant-color="F5F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">907×133 15.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I believe that the DVF value of a histogram is represented by the sum of the squares of the three axes.<br>
If negative values are generated during the calculation process, are the negatives meaningless?<br>
If you know anything about this, please let me know.</p>

---

## Post #16 by @lassoan (2021-08-05 14:58 UTC)

<aside class="quote no-group" data-username="toyama" data-post="15" data-topic="19008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/82dd89/48.png" class="avatar"> toyama:</div>
<blockquote>
<p>I used the segment statistics module to get the displacement field (DVF) statistics from Scalar volume statistics. Does this result show positive as expansion and negative as contraction?</p>
</blockquote>
</aside>
<p>Segment statistics only give meaningful information on scalar volumes, not on vector volumes.</p>
<aside class="quote no-group" data-username="toyama" data-post="15" data-topic="19008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/82dd89/48.png" class="avatar"> toyama:</div>
<blockquote>
<p>The bounding box says “Oriented bounding box: the non-axis aligned bounding box that encompasses the segment”. Is this also suitable for interpreting DVF changes?</p>
</blockquote>
</aside>
<p>Yes, by comparing the bounding box of the segments that you get with/without applying the displacement field transform.</p>
<aside class="quote no-group" data-username="toyama" data-post="15" data-topic="19008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/82dd89/48.png" class="avatar"> toyama:</div>
<blockquote>
<p>I believe that the DVF value of a histogram is represented by the sum of the squares of the three axes.</p>
</blockquote>
</aside>
<p>I don’t understand this sentence. A histogram does not have a DVF value.</p>
<p>You can compute histogram for one component at a time. You can use “Vector to scalar volume” module to extract a single scalar component from a vector volume.</p>
<p>You can export a DVF magnitude image from a transform using Transforms module’s Convert section.</p>
<hr>
<p>What is your overall goal? What is the clinical problem that you are trying to solve?</p>

---

## Post #17 by @toyama (2021-08-16 06:43 UTC)

<p>What does “I don’t understand this sentence. A histogram does not have a DVF value.” mean?<br>
I am trying to get a histogram of the DVF by contour to see how it changed before and after the DIR.<br>
So, I used the transform module to create a DVF and get the histogram for each contour of that VectorField.<br>
I thought the DVF was the square root of the sum of squares of the three axes x,y,z, so I don’t understand why the histogram showed negative values.</p>

---

## Post #18 by @lassoan (2021-08-25 02:12 UTC)

<aside class="quote no-group" data-username="toyama" data-post="17" data-topic="19008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/82dd89/48.png" class="avatar"> toyama:</div>
<blockquote>
<p>What does “I don’t understand this sentence. A histogram does not have a DVF value.” mean?</p>
</blockquote>
</aside>
<p>I asked this because you wrote that “I believe that the DVF value of a histogram is…”, but a histogram does not have a DVF (displacement vector field) value. Each histogram value contains the number of values that are in the corresponding value range.</p>
<p>If you pass all the coordinate values to the numpy histogram function then it will simply pool together the values of all three vector components (R, A, S). Probably your histogram above have 3 peaks because displacement vector components are mostly around -2, -0.6, and 0.4.</p>
<p>To give you an example, if you create a transform with a translation around RAS axes [0.5, -2, 3] and add a few tenth of a degree of rotation (just to have some variance in the translation) then you get a histogram like this if you pool all the components together:</p>
<pre data-code-wrap="python"><code class="lang-python">volumeNode = getNode('Displacement Field')
import numpy as np
histogram = np.histogram(arrayFromVolume(volumeNode), bins=100)
slicer.util.plot(histogram, xColumnIndex = 1)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b3664d862a0ad727327e1855fd58d1006522108.jpeg" data-download-href="/uploads/short-url/jRwUdU5SJiEtLPnBJVpwdatbp8Y.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8b3664d862a0ad727327e1855fd58d1006522108_2_690x419.jpeg" alt="image" data-base62-sha1="jRwUdU5SJiEtLPnBJVpwdatbp8Y" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8b3664d862a0ad727327e1855fd58d1006522108_2_690x419.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8b3664d862a0ad727327e1855fd58d1006522108_2_1035x628.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8b3664d862a0ad727327e1855fd58d1006522108_2_1380x838.jpeg 2x" data-dominant-color="9FA09E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1166 167 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Since statistics of all 3 vector components are pooled (thrown into one big list), you don’t know which peak correspond to which scalar component. So, you probably want to compute histogram for each component separately. You can then see the distribution of each vector component separately: R component’s peak is around 0.5, A component peaks around -2.0, S component around 3.0.</p>
<pre data-code-wrap="python"><code class="lang-python">range = [-5.0, 5.0]
bins = 100
histogramR, histogramBins = np.histogram(arrayFromVolume(volumeNode)[:,:,:,0], bins, range)
histogramA = np.histogram(arrayFromVolume(volumeNode)[:,:,:,1], bins, range)[0]
histogramS = np.histogram(arrayFromVolume(volumeNode)[:,:,:,2], bins, range)[0]
slicer.util.plot(np.vstack([histogramBins[:-1], histogramR, histogramA, histogramS]).T, xColumnIndex = 0, columnNames=['N', 'R', 'A', 'S'], title='Histogram')
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f937a7f41c8434112068cf88bf315b1c5def4746.jpeg" data-download-href="/uploads/short-url/zyG8eaC7vwHFEijNM8cx9qQnwjA.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f937a7f41c8434112068cf88bf315b1c5def4746_2_610x500.jpeg" alt="image" data-base62-sha1="zyG8eaC7vwHFEijNM8cx9qQnwjA" width="610" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f937a7f41c8434112068cf88bf315b1c5def4746_2_610x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f937a7f41c8434112068cf88bf315b1c5def4746_2_915x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f937a7f41c8434112068cf88bf315b1c5def4746_2_1220x1000.jpeg 2x" data-dominant-color="656662"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1486×1217 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If you want to compute the histogram of the displacement magnitude then you will ignore vector directions and just compute statistics for the length of each vector. These numbers will be all positive. Since vectors are all about [0.5, -2.0, 3.0], the peak will be around 3.6:</p>
<pre data-code-wrap="python"><code class="lang-python">magnitudes = np.linalg.norm(arrayFromVolume(volumeNode), axis=3)
histogram = np.histogram(magnitudes, bins=100)
slicer.util.plot(histogram, xColumnIndex = 1, columnNames=['magnitude', 'N'], title="displacement")
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b66c4873587de40280f49aaa61f900615759248.png" data-download-href="/uploads/short-url/aL1ZjRVUWP7m9KEZ00Ei53k8t84.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b66c4873587de40280f49aaa61f900615759248.png" alt="image" data-base62-sha1="aL1ZjRVUWP7m9KEZ00Ei53k8t84" width="690" height="386" data-dominant-color="E9EEEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">698×391 23.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Note that all that I described above are just standard numpy functions and basic linear algebra. The only Slicer-specific functions are <code>arrayFromVolume</code> to get the displacement field vectors as a numpy array, and <code>slicer.util.plot</code> to display a plot.</p>

---

## Post #19 by @toyama (2021-08-25 08:50 UTC)

<p>Thanks for the answer.<br>
I would like to evaluate each contour, where in the above code should I put the code you gave me before?<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-histogram-of-a-segmented-region" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-histogram-of-a-segmented-region</a><br>
I tried everything, but it didn’t work.<br>
I apologize for the inconvenience, but I would appreciate your advice.</p>

---

## Post #20 by @lassoan (2021-08-26 03:20 UTC)

<p>I don’t know which code your are referring to and if you don’t provide the code that you tried and the error message you got then I cannot help figuring it what was wrong.</p>
<p>If you want to get displacement vectors in a specific segment then use the masked numpy array instead of the numpy array returned directly by <code>arrayFromVolume</code>.</p>

---

## Post #21 by @toyama (2021-08-26 06:48 UTC)

<p>I tried to get the histogram for each segment with this code.<br>
However, I got the same result for every segment.<br>
I apologize for the inconvenience. Please check.</p>
<pre><code class="lang-python">&gt;&gt;&gt; labelValue = 1
Loading with imageIOName: GDCM
&gt;&gt;&gt; labelmapVolumeNode =slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")
&gt;&gt;&gt; segmentationNode = getNode('segmentation')
&gt;&gt;&gt; volumeNode = getNode('Displacement Field')
&gt;&gt;&gt; labelmapVolumeNode = getNode('LabelMapVolume')
&gt;&gt;&gt; slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, labelmapVolumeNode, volumeNode)
True
&gt;&gt;&gt; volumeArray = slicer.util.arrayFromVolume(volumeNode)
&gt;&gt;&gt; labelArray = slicer.util.arrayFromVolume(labelmapVolumeNode)
&gt;&gt;&gt; segmentVoxels = volumeArray[labelArray==labelValue]
&gt;&gt;&gt; import numpy as np
&gt;&gt;&gt; histogram = np.histogram(arrayFromVolume(volumeNode), bins=100)
&gt;&gt;&gt; slicer.util.plot(histogram, xColumnIndex = 1)
(MRMLCorePython.vtkMRMLPlotChartNode)000002174751D408
&gt;&gt;&gt; range = [-5.0, 5.0]
&gt;&gt;&gt; bins = 100
&gt;&gt;&gt; histogramR, histogramBins = np.histogram(arrayFromVolume(volumeNode)[:,:,:,0], bins, range)
&gt;&gt;&gt; histogramA = np.histogram(arrayFromVolume(volumeNode)[:,:,:,1], bins, range)[0]
&gt;&gt;&gt; histogramS = np.histogram(arrayFromVolume(volumeNode)[:,:,:,2], bins, range)[0]
&gt;&gt;&gt; slicer.util.plot(np.vstack([histogramBins[:-1], histogramR, histogramA, histogramS]).T, xColumnIndex = 0, columnNames=['N', 'R', 'A', 'S'], title='Histogram')
(MRMLCorePython.vtkMRMLPlotChartNode)000002174751A3A8
&gt;&gt;&gt; magnitudes = np.linalg.norm(arrayFromVolume(volumeNode), axis=3)
&gt;&gt;&gt; histogram = np.histogram(magnitudes, bins=100)
&gt;&gt;&gt; slicer.util.plot(histogram, xColumnIndex = 1, columnNames=['magnitude', 'N'], title="displacement")
(MRMLCorePython.vtkMRMLPlotChartNode)000002174751AE88
&gt;&gt;&gt;
</code></pre>

---

## Post #22 by @lassoan (2021-08-27 02:17 UTC)

<p>You nicely computed <code>segmentVoxels</code> but did not use it when you computed the histogram.</p>

---

## Post #23 by @toyama (2021-08-27 11:28 UTC)

<blockquote>
<blockquote>
<blockquote>
<p>segmentVoxels = volumeArray[labelArray==labelValue]</p>
</blockquote>
</blockquote>
</blockquote>
<p>Is the above not correct?<br>
If you know, I would like to know more about the code to add and where to fix it.</p>

---

## Post #24 by @toyama (2021-08-30 07:03 UTC)

<blockquote>
<blockquote>
<blockquote>
<p>labelValue = 1<br>
Loading with imageIOName: GDCM<br>
labelmapVolumeNode =slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLLabelMapVolumeNode”)<br>
segmentationNode = getNode(‘segmentation’)<br>
volumeNode = getNode(‘Displacement Field’)<br>
labelmapVolumeNode = getNode(‘LabelMapVolume’)<br>
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, labelmapVolumeNode, volumeNode)<br>
True<br>
volumeArray = slicer.util.arrayFromVolume(volumeNode)<br>
labelArray = slicer.util.arrayFromVolume(labelmapVolumeNode)<br>
segmentVoxels = volumeArray[labelArray==labelValue]<br>
import numpy as np<br>
histogram = np.histogram(arrayFromVolume(volumeNode),segmentVoxels, bins=50)<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “&lt;<strong>array_function</strong> internals&gt;”, line 4, in histogram<br>
TypeError: _histogram_dispatcher() got multiple values for argument ‘bins’</p>
</blockquote>
</blockquote>
</blockquote>
<p>I changed the code a bit.</p>
<blockquote>
<blockquote>
<blockquote>
<p>histogram = np.histogram(arrayFromVolume(volumeNode), bins=100)</p>
</blockquote>
</blockquote>
</blockquote>
<p>Added a segment voxel to the above.</p>
<blockquote>
<blockquote>
<blockquote>
<p>histogram = np.histogram(arrayFromVolume(volumeNode),segmentVoxels, bins=100)</p>
</blockquote>
</blockquote>
</blockquote>
<p>But an error occurred.<br>
I’m sorry for the inconvenience, but please confirm.</p>

---

## Post #25 by @toyama (2021-08-31 08:58 UTC)

<p>Sorry for asking so many questions.<br>
Next, I tried to write such a code.<br>
I changed the arrayFromVolume(volumeNode) in the code you gave me to segmentVoxels.<br>
However, I got an error again.<br>
How can I get the histogram for each segment?</p>
<pre><code class="lang-python">&gt;&gt;&gt; labelValue = 1
Loading with imageIOName: GDCM
&gt;&gt;&gt; labelmapVolumeNode =slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")
&gt;&gt;&gt; segmentationNode = getNode('segmentation')
&gt;&gt;&gt; volumeNode = getNode('Displacement Field')
&gt;&gt;&gt; labelmapVolumeNode = getNode('LabelMapVolume')
&gt;&gt;&gt; slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, labelmapVolumeNode, volumeNode)
True
&gt;&gt;&gt; volumeArray = slicer.util.arrayFromVolume(volumeNode)
&gt;&gt;&gt; labelArray = slicer.util.arrayFromVolume(labelmapVolumeNode)
&gt;&gt;&gt; import numpy as np
&gt;&gt;&gt; histogram = np.histogram(arrayFromVolume(volumeNode), bins=100)
&gt;&gt;&gt; slicer.util.plot(histogram, xColumnIndex = 1)
(MRMLCorePython.vtkMRMLPlotChartNode)000001F95ACA9E88
&gt;&gt;&gt; segmentationNode = getNode('segmentation')
&gt;&gt;&gt; volumeNode = getNode('Displacement Field')
&gt;&gt;&gt; labelmapVolumeNode = getNode('LabelMapVolume')
&gt;&gt;&gt; slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, labelmapVolumeNode, volumeNode)
True
&gt;&gt;&gt; volumeArray = slicer.util.arrayFromVolume(volumeNode)
&gt;&gt;&gt; labelArray = slicer.util.arrayFromVolume(labelmapVolumeNode)
&gt;&gt;&gt; segmentVoxels = volumeArray[labelArray==labelValue]
&gt;&gt;&gt; import numpy as np
&gt;&gt;&gt; histogram = np.histogram(arrayFromVolume(volumeNode), bins=100)
&gt;&gt;&gt; slicer.util.plot(histogram, xColumnIndex = 1)
(MRMLCorePython.vtkMRMLPlotChartNode)000001F95ACA9408
&gt;&gt;&gt; segmentationNode = getNode('segmentation')
&gt;&gt;&gt; volumeNode = getNode('Displacement Field')
&gt;&gt;&gt; labelmapVolumeNode = getNode('LabelMapVolume')
&gt;&gt;&gt; slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, labelmapVolumeNode, volumeNode)
True
&gt;&gt;&gt; volumeArray = slicer.util.arrayFromVolume(volumeNode)
&gt;&gt;&gt; labelArray = slicer.util.arrayFromVolume(labelmapVolumeNode)
&gt;&gt;&gt; segmentVoxels = volumeArray[labelArray==labelValue]
&gt;&gt;&gt; import numpy as np
&gt;&gt;&gt; histogram = np.histogram(segmentVoxels, bins=100)
&gt;&gt;&gt; slicer.util.plot(histogram, xColumnIndex = 1)
(MRMLCorePython.vtkMRMLPlotChartNode)000001F95ACA9E28
&gt;&gt;&gt; range = [-5.0, 5.0]
&gt;&gt;&gt; bins = 100
&gt;&gt;&gt; histogramR, histogramBins = np.histogram(segmentVoxles[:,:,:,0], bins, range)
Traceback (most recent call last):
File "&lt;console&gt;", line 1, in &lt;module&gt;
NameError: name 'segmentVoxles' is not defined
</code></pre>

---

## Post #26 by @lassoan (2021-08-31 13:21 UTC)

<p>There is a typo in the variable name.</p>

---

## Post #27 by @toyama (2021-09-01 06:12 UTC)

<p>Where is the mistake?<br>
I changed arrayFromVolume(volumeNode) to segmentVoxels, but this did not give me a histogram for each segment.<br>
What should I do?</p>
<blockquote>
<blockquote>
<blockquote>
<p>labelValue = 1<br>
Loading with imageIOName: GDCM<br>
labelmapVolumeNode =slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLLabelMapVolumeNode”)<br>
segmentationNode = getNode(‘segmentation’)<br>
volumeNode = getNode(‘Displacement Field’)<br>
labelmapVolumeNode = getNode(‘LabelMapVolume’)<br>
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, labelmapVolumeNode, volumeNode)<br>
True<br>
volumeArray = slicer.util.arrayFromVolume(volumeNode)<br>
labelArray = slicer.util.arrayFromVolume(labelmapVolumeNode)<br>
segmentVoxels = volumeArray[labelArray==labelValue]<br>
import numpy as np<br>
histogram = np.histogram(segmentVoxels, bins=100)<br>
slicer.util.plot(histogram, xColumnIndex = 1)<br>
(MRMLCorePython.vtkMRMLPlotChartNode)0000024502908828<br>
histogram = np.histogram(arrayFromVolume(volumeNode), bins=100)<br>
slicer.util.plot(histogram, xColumnIndex = 1)<br>
(MRMLCorePython.vtkMRMLPlotChartNode)0000024502908408<br>
range = [-5.0, 5.0]<br>
bins = 100<br>
histogramR, histogramBins = np.histogram(segmentationVoxels[:,:,:,0], bins, range)<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
NameError: name ‘segmentationVoxels’ is not defined</p>
</blockquote>
</blockquote>
</blockquote>
<p>If you know how to get each contour, please let me know.</p>

---

## Post #28 by @lassoan (2021-09-01 16:52 UTC)

<aside class="quote no-group" data-username="toyama" data-post="25" data-topic="19008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/82dd89/48.png" class="avatar"> toyama:</div>
<blockquote>
<pre><code class="lang-auto">Traceback (most recent call last):
File "&lt;console&gt;", line 1, in &lt;module&gt;
NameError: name 'segmentVoxles' is not defined
</code></pre>
</blockquote>
</aside>
<aside class="quote no-group" data-username="lassoan" data-post="26" data-topic="19008" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>There is a typo in the variable name.</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="toyama" data-post="27" data-topic="19008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/82dd89/48.png" class="avatar"> toyama:</div>
<blockquote>
<p>Where is the mistake?</p>
</blockquote>
</aside>
<p><code>segmentVoxles</code> is mistyped. The name is not the same as the <code>segmentVoxels</code> variable that you created above.</p>

---

## Post #29 by @toyama (2021-09-02 08:24 UTC)

<p>Thank you for letting me know.<br>
I’ve modified the code.<br>
Is it now possible to get the DVF histogram for each segment?</p>
<blockquote>
<blockquote>
<blockquote>
<p>labelValue = 1<br>
Loading with imageIOName: GDCM<br>
labelmapVolumeNode =slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLLabelMapVolumeNode”)<br>
segmentationNode = getNode(‘segmentation’)<br>
volumeNode = getNode(‘Displacement Field’)<br>
labelmapVolumeNode = getNode(‘LabelMapVolume’)<br>
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, labelmapVolumeNode, volumeNode)<br>
True<br>
volumeArray = slicer.util.arrayFromVolume(volumeNode)<br>
labelArray = slicer.util.arrayFromVolume(labelmapVolumeNode)<br>
segmentVoxels = volumeArray[labelArray==labelValue]<br>
import numpy as np<br>
histogram = np.histogram(segmentVoxels, bins=100)<br>
slicer.util.plot(histogram, xColumnIndex = 1)<br>
(MRMLCorePython.vtkMRMLPlotChartNode)0000015B0A709EE8<br>
range = [-5.0, 5.0]<br>
bins = 100<br>
histogramR, histogramBins = np.histogram(segmentVoxels[:,0], bins, range)<br>
histogramA = np.histogram(segmentVoxels[:,1], bins, range)[0]<br>
histogramS = np.histogram(segmentVoxels[:,2], bins, range)[0]<br>
slicer.util.plot(np.vstack([histogramBins[:-1], histogramR, histogramA, histogramS]).T, xColumnIndex = 0, columnNames=[‘N’, ‘R’, ‘A’, ‘S’], title=‘Histogram’)<br>
(MRMLCorePython.vtkMRMLPlotChartNode)0000015B0A709468<br>
magnitudes = np.linalg.norm(segmentVoxels, axis=1)<br>
histogram = np.histogram(magnitudes, bins=100)<br>
slicer.util.plot(histogram, xColumnIndex = 1, columnNames=[‘magnitude’, ‘N’], title=“displacement”)<br>
(MRMLCorePython.vtkMRMLPlotChartNode)0000015B0DBC3F48</p>
</blockquote>
</blockquote>
</blockquote>
<p>The code you gave me before gave me this error.</p>
<blockquote>
<blockquote>
<blockquote>
<p>histogramR, histogramBins = np.histogram(segmentVoxels[:,:,:,0], bins, range)<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
IndexError: too many indices for array: array is 2-dimensional, but 4 were indexed</p>
</blockquote>
</blockquote>
</blockquote>
<blockquote>
<blockquote>
<blockquote>
<p>magnitudes = np.linalg.norm(segmentVoxels, axis=3)<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “&lt;<strong>array_function</strong> internals&gt;”, line 6, in norm<br>
return sqrt(add.reduce(s, axis=axis, keepdims=keepdims))<br>
numpy.AxisError: axis 3 is out of bounds for array of dimension 2</p>
</blockquote>
</blockquote>
</blockquote>
<p>I modified this part, but is the code at the top correct?</p>

---

## Post #30 by @lassoan (2021-09-02 18:06 UTC)

<p>The code snippets that I provided <a href="https://discourse.slicer.org/t/negative-values-in-dvf-histogram/19008/18">above</a> all work correctly and you only need a little Python and numpy knowledge to apply them to your data. You may try to complete Python and numpy tutorials or find someone locally who can help you out with this.</p>

---

## Post #31 by @toyama (2021-09-03 10:44 UTC)

<p>Is it wrong to change [:,:,:,0] and axis=3 to fit the segment?<br>
I was able to get the DVF for each axis and the total DVF with this code, but was the code wrong?<br>
Is it impossible to get the DVF for each segment?<br>
Is it possible to calculate only by volume?<br>
I would like your answer.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3abddb725a6407e72238ada519a1be5451cf9369.png" alt="image" data-base62-sha1="8nEsy7J4kJ9Jz5vDGaoTgd9Lg0N" width="656" height="456"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/eeffd87274baab629ee557cc0f91fb534fde547e.png" alt="image" data-base62-sha1="y6hMDi3P3dopUab4o8iZ7Wov6sm" width="655" height="457"></p>

---

## Post #32 by @lassoan (2021-09-05 02:26 UTC)

<p>You can use standard Python array indexing to filter voxels that are in a selected segment. For example:</p>
<pre><code class="lang-python">volumeNode = getNode('Displacement Field')
segmentationNode = getNode('Segmentation')
segmentId = 'Segment_3'

magnitudes = np.linalg.norm(arrayFromVolume(volumeNode), axis=3)
magnitudesInSegment = magnitudes[arrayFromSegmentBinaryLabelmap(segmentationNode, segmentId) != 0]
histogram = np.histogram(magnitudesInSegment, bins=100)
slicer.util.plot(histogram, xColumnIndex = 1, columnNames=['magnitude', 'N'], title="displacement")
</code></pre>

---

## Post #33 by @toyama (2021-09-06 08:38 UTC)

<p>Thank you for your answer.<br>
I tried, but I got an error.<br>
I apologize for the inconvenience, but I would appreciate your advice.</p>
<pre><code class="lang-auto">&gt;&gt;&gt; labelValue = 1
Loading with imageIOName: GDCM
&gt;&gt;&gt; labelmapVolumeNode =slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")
&gt;&gt;&gt; volumeNode = getNode('Displacement Field')
&gt;&gt;&gt; segmentationNode = getNode('segmentation')
&gt;&gt;&gt; segmentId = 'patient'
&gt;&gt;&gt; labelmapVolumeNode = getNode('LabelMapVolume')
&gt;&gt;&gt; slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, labelmapVolumeNode, volumeNode)
True
&gt;&gt;&gt; volumeArray = slicer.util.arrayFromVolume(volumeNode)
&gt;&gt;&gt; labelArray = slicer.util.arrayFromVolume(labelmapVolumeNode)
&gt;&gt;&gt; segmentVoxels = volumeArray[labelArray==labelValue]
&gt;&gt;&gt; import numpy as np
&gt;&gt;&gt; histogram = np.histogram(arrayFromVolume(volumeNode), bins=100)
&gt;&gt;&gt; slicer.util.plot(histogram, xColumnIndex = 1)
(MRMLCorePython.vtkMRMLPlotChartNode)00000222A95B87C8
&gt;&gt;&gt; range = [-5.0, 5.0]
&gt;&gt;&gt; bins = 100
&gt;&gt;&gt; histogramR, histogramBins = np.histogram(arrayFromVolume(volumeNode)[:,:,:,0], bins, range)
&gt;&gt;&gt; histogramA = np.histogram(arrayFromVolume(volumeNode)[:,:,:,1], bins, range)[0]
&gt;&gt;&gt; histogramS = np.histogram(arrayFromVolume(volumeNode)[:,:,:,2], bins, range)[0]
&gt;&gt;&gt; slicer.util.plot(np.vstack([histogramBins[:-1], histogramR, histogramA, histogramS]).T, xColumnIndex = 0, columnNames=['N', 'R', 'A', 'S'], title='Histogram')
(MRMLCorePython.vtkMRMLPlotChartNode)00000222A95B86A8
&gt;&gt;&gt; magnitudes = np.linalg.norm(arrayFromVolume(volumeNode), axis=3)
&gt;&gt;&gt; magnitudesInSegment = magnitudes[arrayFromSegmentBinaryLabelmap(segmentationNode, segmentId) != 0]
Traceback (most recent call last):
File "&lt;console&gt;", line 1, in &lt;module&gt;
IndexError: boolean index did not match indexed array along dimension 0; dimension is 128 but corresponding boolean dimension is 130
</code></pre>

---

## Post #34 by @toyama (2021-09-07 07:04 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="32" data-topic="19008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<pre><code class="lang-auto">histogram = np.histogram(magnitudesInSegment, bins=100)
slicer.util.plot(histogram, xColumnIndex = 1, columnNames=['magnitude', 'N'], title="displacement")
</code></pre>
</blockquote>
</aside>
<p>I’ve tried drawing other code, but I still get this error.<br>
I apologize for the inconvenience, but I would appreciate your advice.</p>
<pre><code class="lang-auto">&gt;&gt;&gt; labelValue = 1
Loading with imageIOName: GDCM
&gt;&gt;&gt; labelmapVolumeNode =slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")
&gt;&gt;&gt; volumeNode = getNode('Displacement Field')
&gt;&gt;&gt; labelmapVolumeNode = getNode('LabelMapVolume')
&gt;&gt;&gt; segmentationNode = getNode('segmentation')
&gt;&gt;&gt; segmentId = 'GTV'
&gt;&gt;&gt; slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, labelmapVolumeNode, volumeNode)
True
&gt;&gt;&gt; volumeArray = slicer.util.arrayFromVolume(volumeNode)
&gt;&gt;&gt; labelArray = slicer.util.arrayFromVolume(labelmapVolumeNode)
&gt;&gt;&gt; import numpy as np
&gt;&gt;&gt; histogram = np.histogram(arrayFromVolume(volumeNode), bins=100)
&gt;&gt;&gt; slicer.util.plot(histogram, xColumnIndex = 1)
(MRMLCorePython.vtkMRMLPlotChartNode)000001D612619E88
&gt;&gt;&gt; range = [-5.0, 5.0]
&gt;&gt;&gt; bins = 100
&gt;&gt;&gt; histogramR, histogramBins = np.histogram(arrayFromVolume(volumeNode)[:,:,:,0], bins, range)
&gt;&gt;&gt; histogramA = np.histogram(arrayFromVolume(volumeNode)[:,:,:,1], bins, range)[0]
&gt;&gt;&gt; histogramS = np.histogram(arrayFromVolume(volumeNode)[:,:,:,2], bins, range)[0]
&gt;&gt;&gt; slicer.util.plot(np.vstack([histogramBins[:-1], histogramR, histogramA, histogramS]).T, xColumnIndex = 0, columnNames=['N', 'R', 'A', 'S'], title='Histogram')
(MRMLCorePython.vtkMRMLPlotChartNode)000001D612619DC8
&gt;&gt;&gt; magnitudes = np.linalg.norm(arrayFromVolume(volumeNode), axis=3)
&gt;&gt;&gt; histogram = np.histogram(magnitudes, bins=100)
&gt;&gt;&gt; slicer.util.plot(histogram, xColumnIndex = 1, columnNames=['magnitude', 'N'], title="displacement")
(MRMLCorePython.vtkMRMLPlotChartNode)000001D612619EE8
&gt;&gt;&gt; magnitudes = np.linalg.norm(arrayFromVolume(volumeNode), axis=3)
&gt;&gt;&gt; magnitudesInSegment = magnitudes[arrayFromSegmentBinaryLabelmap(segmentationNode, segmentId) != 0]
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
IndexError: boolean index did not match indexed array along dimension 0; dimension is 128 but corresponding boolean dimension is 123
&gt;&gt;&gt; histogram = np.histogram(magnitudesInSegment, bins=100)
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
NameError: name 'magnitudesInSegment' is not defined
&gt;&gt;&gt; slicer.util.plot(histogram, xColumnIndex = 1, columnNames=['magnitude', 'N'], title="displacement")
(MRMLCorePython.vtkMRMLPlotChartNode)000001D612619E28
</code></pre>

---

## Post #35 by @lassoan (2021-09-08 18:09 UTC)

<aside class="quote no-group" data-username="toyama" data-post="33" data-topic="19008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/82dd89/48.png" class="avatar"> toyama:</div>
<blockquote>
<p><code>IndexError: boolean index did not match indexed array along dimension 0; dimension is 128 but corresponding boolean dimension is 130</code></p>
</blockquote>
</aside>
<p>This indicates that the size of the scalar volume and the segmentation labelmap is not the same. Using the latest Slicer Preview Release probably fixes this already, but if not then specify the displacement field as reference volume in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.arrayFromSegmentBinaryLabelmap">arrayFromSegmentBinaryLabelmap</a>.</p>

---

## Post #36 by @toyama (2021-09-09 08:31 UTC)

<p>Thank you very much.<br>
After installing the preview version, the code also worked correctly and I was able to get the histogram successfully.</p>
<pre><code class="lang-auto">&gt;&gt;&gt; labelValue = 1
Loading with imageIOName: GDCM
&gt;&gt;&gt; labelmapVolumeNode =slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")
&gt;&gt;&gt; volumeNode = getNode('Displacement Field')
&gt;&gt;&gt; labelmapVolumeNode = getNode('LabelMapVolume')
&gt;&gt;&gt; segmentationNode = getNode('segmentation')
&gt;&gt;&gt; segmentId = 'patient'
&gt;&gt;&gt; slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, labelmapVolumeNode, volumeNode)
True
&gt;&gt;&gt; volumeArray = slicer.util.arrayFromVolume(volumeNode)
&gt;&gt;&gt; labelArray = slicer.util.arrayFromVolume(labelmapVolumeNode)
&gt;&gt;&gt; import numpy as np
&gt;&gt;&gt; magnitudes = np.linalg.norm(arrayFromVolume(volumeNode), axis=3)
&gt;&gt;&gt; magnitudesInSegment = magnitudes[arrayFromSegmentBinaryLabelmap(segmentationNode, segmentId) != 0]
&gt;&gt;&gt; histogram = np.histogram(magnitudesInSegment, bins=100)
&gt;&gt;&gt; slicer.util.plot(histogram, xColumnIndex = 1, columnNames=['magnitude', 'N'], title="displacement")
(MRMLCore.vtkMRMLPlotChartNode)000001BA99908E88
&gt;&gt;&gt; segmentId = 'GTV'
&gt;&gt;&gt; slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, labelmapVolumeNode, volumeNode)
True
&gt;&gt;&gt; volumeArray = slicer.util.arrayFromVolume(volumeNode)
&gt;&gt;&gt; labelArray = slicer.util.arrayFromVolume(labelmapVolumeNode)
&gt;&gt;&gt; import numpy as np
&gt;&gt;&gt; magnitudes = np.linalg.norm(arrayFromVolume(volumeNode), axis=3)
&gt;&gt;&gt; magnitudesInSegment = magnitudes[arrayFromSegmentBinaryLabelmap(segmentationNode, segmentId) != 0]
&gt;&gt;&gt; histogram = np.histogram(magnitudesInSegment, bins=100)
&gt;&gt;&gt; slicer.util.plot(histogram, xColumnIndex = 1, columnNames=['magnitude', 'N'], title="displacement")
(MRMLCore.vtkMRMLPlotChartNode)000001BA99908C48
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e4f92fcd6048744357c0e715a7fb7fd3d1da2b1.png" alt="image" data-base62-sha1="kiWhPPEHhrlbrJUzVu4bqckIAYV" width="650" height="436"></p>

---
