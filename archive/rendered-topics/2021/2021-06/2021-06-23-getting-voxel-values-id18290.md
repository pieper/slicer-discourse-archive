# Getting Voxel Values

**Topic ID**: 18290
**Date**: 2021-06-23
**URL**: https://discourse.slicer.org/t/getting-voxel-values/18290

---

## Post #1 by @toyama (2021-06-23 07:01 UTC)

<p>We would like to get the values of all the voxels in a segment.<br>
However, the segment statics only gives me the maximum and minimum values for each contour.<br>
Is there any way to get the values of the voxels statistically?</p>

---

## Post #2 by @Juicy (2021-06-23 09:26 UTC)

<p>Whenever I use segment statistics it gives the mean, median, standard deviation etc. Have you tried scrolling across to see the whole table? You could ensure all the options are ticked under the “Advanced” drop down menu also?</p>

---

## Post #3 by @lassoan (2021-06-25 19:07 UTC)

<p>You can get all voxels of the segment and compute statistics as in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-histogram-of-a-segmented-region">this example</a>.</p>

---

## Post #4 by @toyama (2021-06-29 06:39 UTC)

<p>Thank you for your answer.<br>
I started with “# Compute histogram” in “Get histogram of a segmented region” based on the series and segments I had loaded beforehand.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/465d803df3536b2f5516b7f791edf9757f82d428.png" alt="image" data-base62-sha1="a2tKmtAk2SkPk0pmy1hBpSqwW2A" width="181" height="229"><br>
The label map for the volume was created with “labelValue = 1”.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d835daca77cc1272184eb2b897d110644fab7621.png" alt="image" data-base62-sha1="uQGw26uOije7h6kwxsDcxoadvK9" width="567" height="22"><br>
However, when I proceeded to the next “# Get segmentation as labelmap volume node”, I got an error message. changing the name of the segment to segmentation as in the Script repository example did not help.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/112c014bbda8f3667260987062c49ea3f108563a.png" alt="image" data-base62-sha1="2rUoDDteYjgYBdvsEUGLN0kj8nw" width="567" height="172"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/112c014bbda8f3667260987062c49ea3f108563a.png" alt="image" data-base62-sha1="2rUoDDteYjgYBdvsEUGLN0kj8nw" width="567" height="172"></p>

---

## Post #5 by @lassoan (2021-06-30 01:51 UTC)

<p>You need to set the <code>segmentationNode</code> variable. For example, if the name of your segmentation node is <code>Segmentation</code> then you can set the variable by calling:</p>
<pre><code class="lang-python">segmentationNode = getNode('Segmentation')
</code></pre>

---

## Post #6 by @toyama (2021-06-30 07:12 UTC)

<p>Thank you for your answer.<br>
I was able to get a histogram by specifying segmentationNode, labelmapVolumeNode, and masterVolumeNode.<br>
When I change the plot type of the histogram from “scatter plot”, the value of the X axis changes, why is this? Looking at the table, scatter seems to be correct.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/573eb408bc5bac3a9012bb429523bb676e6076b8.png" alt="image" data-base62-sha1="crNSCIAUf6zTFNx66C9j5Mj9wLK" width="567" height="395"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e27fb7b26321e804083facf1d331039230dec73f.png" alt="image" data-base62-sha1="wjHxBerzoMrrAWMQfKsSKS0WZCD" width="567" height="393"><br>
Also, when I try to save the plot chart as an svg file, I get a “file not found” message. Is there any other way to save it?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b855305bf0b742b350681284159519504920ae6.png" alt="image" data-base62-sha1="mbNExHwSwagY62yzWxPZFxmtVZA" width="351" height="113"><br>
I apologize for the inconvenience, but I would appreciate your response.</p>

---

## Post #7 by @toyama (2021-07-05 09:17 UTC)

<p>Let me ask you an additional question.<br>
It worked once, but when I entered the same code.<br>
I get an error like the one in the image.<br>
I think labelArray = slicer.util.arrayFromVolume(labelmapVolumeNode) is not invoked properly, is there any reason for this?<br>
Sorry I am not familiar with python.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d453a6ba7dae23d097c8323cca800ae08b491e49.png" alt="image" data-base62-sha1="uikrDAvrPVY8QEQMy36qrCKuk4h" width="605" height="451"></p>

---

## Post #8 by @pieper (2021-07-05 17:48 UTC)

<p>It’s cut off in your screenshot but it appears you left off the () and arguments at the end of ExportVisibleSegmentsToLabelmapNode so it’s never invoked and the labelmapVolumeNode is never populated.</p>

---

## Post #9 by @toyama (2021-07-06 09:04 UTC)

<p>Thank you very much for your answer.<br>
I managed to fix the error with this code.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e61542c1ebb5c2287261ca7e4d3e0e56850c876e.png" alt="image" data-base62-sha1="wPpmTbM6G0F94TzvQ64THcML1O6" width="567" height="362"><br>
Thank you very much.</p>

---

## Post #10 by @lassoan (2021-07-06 18:22 UTC)

<aside class="quote no-group" data-username="toyama" data-post="6" data-topic="18290">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/82dd89/48.png" class="avatar"> toyama:</div>
<blockquote>
<p>When I change the plot type of the histogram from “scatter plot”, the value of the X axis changes, why is this?</p>
</blockquote>
</aside>
<p>Scatter plot uses a specified table column as x axis values. Line plot uses point index (0, 1, 2, …) as x axis values.</p>
<aside class="quote no-group" data-username="toyama" data-post="6" data-topic="18290">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/82dd89/48.png" class="avatar"> toyama:</div>
<blockquote>
<p>Also, when I try to save the plot chart as an svg file, I get a “file not found” message. Is there any other way to save it?</p>
</blockquote>
</aside>
<p>Good catch, there was a small bug in how the filename was assembled and indeed saving failed. This will be fixed in tomorrow’s Slicer Preview Release.</p>
<p>Until then you can use this code snippet as a workaround:</p>
<pre data-code-wrap="python"><code class="lang-python">filename = "c:/tmp/test.svg"
plotWidgetIndex = 0
layoutManager = slicer.app.layoutManager()
renderWindow = layoutManager.plotWidget(plotWidgetIndex).plotView().renderWindow()
exp = vtk.vtkGL2PSExporter()
exp.SetRenderWindow(renderWindow)
exp.CompressOff()
exp.SetFileFormatToSVG()
exp.SetFilePrefix(filename[:-4]) # file prefix expects filename without extension
exp.Write()
</code></pre>

---

## Post #11 by @toyama (2021-07-07 07:26 UTC)

<p>Thank you for your answer.<br>
I have downloaded the latest version for July 7, 2021.<br>
However, when I tried to install RegistrationQA in this version, it was not in the extensions.<br>
Is RegistrationQA no longer covered in the latest version?<br>
If the latest version does not have RegistrationQA, I will use the code you gave me for the previous version.</p>

---

## Post #12 by @lassoan (2021-07-14 03:58 UTC)

<p>I’ve fixed an error that made the extension fail to build. Download the latest Slicer Preview Release tomorrow and let me know if the extension is still not available.</p>

---

## Post #13 by @lassoan (2023-01-12 17:45 UTC)

<p>2 posts were split to a new topic: <a href="/t/get-voxel-values-as-a-csv-file/27216">Get voxel values as a CSV file</a></p>

---
