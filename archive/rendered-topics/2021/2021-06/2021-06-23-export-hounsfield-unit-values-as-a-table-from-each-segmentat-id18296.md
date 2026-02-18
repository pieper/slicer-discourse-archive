# Export Hounsfield Unit values as a table from each segmentation

**Topic ID**: 18296
**Date**: 2021-06-23
**URL**: https://discourse.slicer.org/t/export-hounsfield-unit-values-as-a-table-from-each-segmentation/18296

---

## Post #1 by @Somayeh (2021-06-23 12:33 UTC)

<p>Hi everyone,</p>
<p>I am a beginner at using 3D Slicer. Before that, I used to work with Mimics. I was wondering is it possible to extract/export the whole set of Hounsfield Unit values from a segmentation performed via threshold tool? I want to use them for calculating bone density. There is a possibility in Mimics that can export a 4 columns table (XYZ and HU value for each element that was created in Mimics after making the mask) and I am looking for the same function in 3D Slicer.</p>
<p>Thanks in advance,</p>
<p>Best,<br>
Somayeh</p>

---

## Post #2 by @lassoan (2021-06-24 16:07 UTC)

<p>Yes, of course, getting intensities of voxels in a segmented region is very simple, and the best is that you don’t even need to export the file, then load it into your own Python script for analysis and display, but you can do everything using a small Python code snippet within Slicer (copy-paste the code into the built-in Python console, use a Jupyter notebook, or create a small Python-scripted module with a custom GUI).</p>
<p>For example, to get all voxel values of the master volume corresponding to a segment:</p>
<pre><code class="lang-python"># Get segmentation as labelmap volume node
labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, labelmapVolumeNode, masterVolumeNode)

# Extract all voxels of the segment as numpy array
volumeArray = slicer.util.arrayFromVolume(masterVolumeNode)
labelArray = slicer.util.arrayFromVolume(labelmapVolumeNode)
segmentVoxels = volumeArray[labelArray==labelValue]
</code></pre>
<p>See a complete example (that includes generating sample data, extracting voxel values of a segment, computing histogram, and plotting the results) <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-histogram-of-a-segmented-region">here</a>.</p>

---

## Post #3 by @Somayeh (2021-06-25 15:00 UTC)

<p>Dear Andras,</p>
<p>Thanks for your answer.</p>
<p>I did not work with Python, so I am a very beginner in this area.<br>
I tried to copy-paste the code that you sent. I renamed the “masterVolumeNode”, “segmentationNode” and “labelmapVolumeNode” but it did not work. I was wondering could you please edit the code based on my model’s subhierarchy?</p>
<p>Thanks in advance,</p>
<p>Best,<br>
Somayeh<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/94526a15b4a8fe5c9ba7d5b772f32b8c41750ee5.png" alt="image" data-base62-sha1="la7eJwNvvVK9NQ3AeUW7vALwCzz" width="624" height="192"></p>

---

## Post #4 by @lassoan (2021-06-25 18:41 UTC)

<p>You can set <code>segmentationNode</code> like this:</p>
<pre><code class="lang-python">segmentationNode = getNode('P3-L4')
</code></pre>

---

## Post #5 by @Somayeh (2021-06-28 09:25 UTC)

<p>Thank you for your answer.<br>
I tried this code and it ran without any error, but I did not see any results:<br>
<em>segmentationNode = getNode(‘P3-L4’)</em><br>
<em>labelmapVolumeNode = getNode(‘P3-L4’)</em><br>
<em>masterVolumeNode = getNode(‘P3-whole’)</em></p>
<p><em># Get segmentation as labelmap volume node</em><br>
<em>labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLLabelMapVolumeNode”)</em><br>
<em>slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, labelmapVolumeNode, masterVolumeNode)</em></p>
<p><em># Extract all voxels of the segment as numpy array</em><br>
<em>volumeArray = slicer.util.arrayFromVolume(masterVolumeNode)</em><br>
<em>labelArray = slicer.util.arrayFromVolume(labelmapVolumeNode)</em><br>
<em>labelValue = getNode(‘LabelMapVolume’)</em><br>
*<em>sgmentVoxels = volumeArray[labelArray==labelValue]</em></p>
<p>After that, I added two parts to the code (based on the webpage which you sent it):<br>
<em># Compute histogram</em><br>
<em>import numpy as np</em><br>
<em>histogram = np.histogram(segmentVoxels, bins=50)</em></p>
<p><em># Plot histogram</em><br>
<em>################################################</em></p>
<p>And I just got this table that does not make sense and can not be true:<br>
<em><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/0849b7bdb237905c4fa780cdc25932b9588ea7c1.png" data-download-href="/uploads/short-url/1bjL4HW7BlJA7IYFZvy1KvSjbfb.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/0849b7bdb237905c4fa780cdc25932b9588ea7c1.png" alt="image" data-base62-sha1="1bjL4HW7BlJA7IYFZvy1KvSjbfb" width="173" height="500" data-dominant-color="F6F5F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">284×818 7.41 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></em></p>
<p>Thanks in advance,</p>
<p>Best,<br>
Somayeh</p>

---

## Post #6 by @lassoan (2021-06-28 14:04 UTC)

<p>There are a few small issues in your script, for example:</p>
<ul>
<li>remove <code>labelmapVolumeNode = getNode('P3-L4')</code> - you set the variable a few lines below</li>
<li>
<code>*sgmentVoxels</code> should be <code>segmentVoxels</code>
</li>
</ul>
<p>Always put code between triple-ticks:</p>
<pre><code class="lang-nohighlight">```python
your code is here
just another line
```
</code></pre>
<p>Otherwise, the code looks OK. I don’t see anything wrong in the output either. Why the tables do not make sense for you? What did you expect to see in the tables?</p>

---

## Post #7 by @DeweiLi (2021-06-28 14:41 UTC)

<p>I have the same issue and followed your post for a few days. Today I tried your code but the same as your result. Also I was prompted that I can try this plugin. Thanks to the experts who wrote it. Still can’t get the whole set of Hounsfield Unit values from a segmentation.  It was just enough for me<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7bc681024c9c384dfc30e7e454f1f6ddc6da86e.png" data-download-href="/uploads/short-url/zlzAQkeM933YAEdxV59sXzXj182.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7bc681024c9c384dfc30e7e454f1f6ddc6da86e.png" alt="1" data-base62-sha1="zlzAQkeM933YAEdxV59sXzXj182" width="690" height="80" data-dominant-color="F1F1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">872×102 9.07 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35b9cda15b4db572c2f7a0d3dd252c246a7664ff.png" data-download-href="/uploads/short-url/7Fho1Jf8AZrzKsdwaPRC57qxh7h.png?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35b9cda15b4db572c2f7a0d3dd252c246a7664ff_2_364x499.png" alt="2" data-base62-sha1="7Fho1Jf8AZrzKsdwaPRC57qxh7h" width="364" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35b9cda15b4db572c2f7a0d3dd252c246a7664ff_2_364x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35b9cda15b4db572c2f7a0d3dd252c246a7664ff_2_546x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35b9cda15b4db572c2f7a0d3dd252c246a7664ff.png 2x" data-dominant-color="F8F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">617×846 34.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @lassoan (2021-06-28 15:02 UTC)

<p>I’ve tested this <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-histogram-of-a-segmented-region">example script</a> and it works perfectly for both latest Slicer Stable Release and Slicer Preview Release.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1cd58e76ee8a8134bc8a155b8e9491364616989d.jpeg" data-download-href="/uploads/short-url/474UxdNdaRdNGAICgHXxAJHVyGx.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1cd58e76ee8a8134bc8a155b8e9491364616989d_2_690x421.jpeg" alt="image" data-base62-sha1="474UxdNdaRdNGAICgHXxAJHVyGx" width="690" height="421" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1cd58e76ee8a8134bc8a155b8e9491364616989d_2_690x421.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1cd58e76ee8a8134bc8a155b8e9491364616989d_2_1035x631.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1cd58e76ee8a8134bc8a155b8e9491364616989d_2_1380x842.jpeg 2x" data-dominant-color="B3B3B2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2254×1376 485 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>All you need to do is to replace the first part (that generates input data) with setting your data as <code>masterVolumeNode</code>, <code>segmentationNode</code>, <code>labelValue</code>.</p>

---

## Post #9 by @Somayeh (2021-06-29 10:45 UTC)

<p>Thanks for your answer.<br>
The reason that I said the table does not make sense:<br>
As I mentioned before, the table which I need should contain 4 columns, like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7e813c8d6079577ca7779b19cb7544bcedd4333.png" data-download-href="/uploads/short-url/zn59PdVgiMZdB2B4c7NeGlme6pZ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7e813c8d6079577ca7779b19cb7544bcedd4333.png" alt="image" data-base62-sha1="zn59PdVgiMZdB2B4c7NeGlme6pZ" width="479" height="500" data-dominant-color="E7E7E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">492×513 8.48 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And considering the CT-scans that I used (0.3 mm) I expected around 250,000 data for this sample (something like the data that was exported for similar Vertebrae from Mimics).</p>

---

## Post #10 by @lassoan (2021-06-29 17:12 UTC)

<p>Since you have the volume and labels as numpy arrays, you already have all these tables. You just need to specify what you need.</p>
<p>For example, to get coordinates and HU at all segment voxel positions:</p>
<pre><code class="lang-python">coordinates = np.where(labelArray==labelValue)
hu = volumeArray[coordinates]
</code></pre>
<p>You can put together an array of i, j, k coordinates and HU values like this:</p>
<pre><code class="lang-python">coordinatesWithHU = np.zeros([len(coordinates[0]), 4])
coordinatesWithHU[:,0:3] = np.array(coordinates).T
coordinatesWithHU[:,3] = hu

# save the dataframe as a csv file
pip_install('pandas')  # needs to executed only once
import pandas as pd
pd.DataFrame(coordinatesWithHU).to_csv("c:/tmp/coordshu.csv")
</code></pre>
<p>Such representation would be extremely inefficient for any kind of processing. I’m just curious, why do you consider representing your data in such table?</p>

---

## Post #11 by @Somayeh (2021-06-30 10:06 UTC)

<p>Thank you for your answer dear Andras.<br>
I still can not get the table that I want, but I am working on it. <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=9" title=":frowning:" class="emoji" alt=":frowning:"><br>
I need to get density for each element in the sample, so I wrote a code in Matlab to obtain the density. One of the input data for that code is the Hu value based on CT images which I am currently struggling with it now.</p>

---

## Post #12 by @lassoan (2021-07-01 14:05 UTC)

<p>The code snippet above creates the table that you described you need.</p>
<p>What kind of processing do you plan to do?</p>
<p>I’m just curious, why do you consider using Matlab? In Python you have many more tools, you don’t need to deal with licensing hassles, and Python programming skills are highly valued (while Matlab programming skills are largely irrelevant in industry, and increasingly in academia, too).</p>

---

## Post #13 by @Somayeh (2021-07-02 10:06 UTC)

<p>Unfortunately I could not get the table which I wanted. In fact, I just decided to learn Python and I need time to write code with it.<br>
I worked with MATLAB because I was familiar with its functions and some of its rules.<br>
I would be appreciated if you could send me any tutorial on learning Python for beginners.</p>
<p>Best,<br>
Somayeh</p>

---

## Post #14 by @Alex_Vergara (2021-07-02 10:14 UTC)

<p>Function to convert HU values (calibrated HU) to density (g/cm3):</p>
<pre><code class="lang-auto">def HU2Dens(HU):
    if HU&gt;-1000 and HU&lt;0:
        return HU/1000+1
    elif HU&gt;0:
        return HU/1955+1
    else:
        return 0
</code></pre>
<p>And now you can use lassoan script replacing this line</p>
<pre><code class="lang-auto">coordinatesWithHU[:,3] = hu
</code></pre>
<p>by this one</p>
<pre><code class="lang-auto">coordinatesWithHU[:,3] = HU2Dens(hu)
</code></pre>

---

## Post #15 by @Somayeh (2021-07-02 10:23 UTC)

<p>Thank you so much.<br>
Could you get the table via that script (x, y, z, and Hu)?<br>
I want to get that table, but the scripts I used do not work. Could please send me your script?</p>
<p>Best,<br>
Somayeh</p>

---

## Post #16 by @lassoan (2021-08-30 05:55 UTC)

<p>A post was split to a new topic: <a href="/t/convert-between-ras-and-numpy-array-indices/19408">Convert between RAS and numpy array indices</a></p>

---
