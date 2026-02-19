---
topic_id: 10422
title: "Getting Vtkmrmlslicenodegreen Vtkmrmlslicenodered Vtkmrmlsli"
date: 2020-02-24
url: https://discourse.slicer.org/t/10422
---

# Getting vtkMRMLSliceNodeGreen, vtkMRMLSliceNodeRed, vtkMRMLSliceNodeYellow data into numpy array

**Topic ID**: 10422
**Date**: 2020-02-24
**URL**: https://discourse.slicer.org/t/getting-vtkmrmlslicenodegreen-vtkmrmlslicenodered-vtkmrmlslicenodeyellow-data-into-numpy-array/10422

---

## Post #1 by @dataminer (2020-02-24 23:42 UTC)

<p>Hello Everyone</p>
<p>I am new to slicer.<br>
I can import NRRD file and see the 3 views (sagittal, coronal and transverse), and I can use 3DSlicer to save them as png file for each of the 3 views (by using ScreenCapture.ScreenCaptureLogic().captureSliceSweep). But I do not know how to get these values into numpy array.  I think this is only giving me for one of the views,</p>
<pre><code>refNodeName = 'knee'
        refPath = os.path.join(refPath, refNodeName + ".nrrd")
        slicer.util.loadNodeFromFile(refPath, 'VolumeFile')
        node=slicer.util.getFirstNodeByName(refNodeName)
        array = slicer.util.array(refNodeName)
        print(array.shape, array.ndim)
</code></pre>
<p>Is there a way to access the 3 views/planes and get the data into Numpy Array.<br>
Hope I could explain it properly.</p>
<p>Thanks</p>
<p>dm</p>

---

## Post #2 by @lassoan (2020-02-25 03:00 UTC)

<p>The best approach depends on what you would like to achieve. Could you give a bit more information about your use case? What would you like to do with the numpy array?</p>

---

## Post #3 by @dataminer (2020-02-25 14:01 UTC)

<p>Hello,</p>
<p>I can save it in a text file for further processing.<br>
I have been looking for code snippets which does this, but have not come across any.<br>
Can you please guide me to the right direction. I feel like perhaps this is something very standard but I do not know how to do it yet.</p>
<p>Also I am looking into loading 3D volume from NRRD file into numpy array or merging slices to generate the 3D volume, but that can be a separate topic.</p>
<p>Thanks!</p>
<p>dm</p>

---

## Post #4 by @lassoan (2020-02-25 18:40 UTC)

<aside class="quote no-group" data-username="dataminer" data-post="3" data-topic="10422">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/f9ae1b/48.png" class="avatar"> dataminer:</div>
<blockquote>
<p>I can save it in a text file for further processing.</p>
</blockquote>
</aside>
<p>While it does not sound like a good idea (text representation for an image is extremely inefficient), you can certainly do this if you have your data in a numpy array. In my question I meant what you actually want to do (beyond writing to file).</p>
<aside class="quote no-group" data-username="dataminer" data-post="3" data-topic="10422">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/f9ae1b/48.png" class="avatar"> dataminer:</div>
<blockquote>
<p>Also I am looking into loading 3D volume from NRRD file into numpy array or merging slices to generate the 3D volume, but that can be a separate topic</p>
</blockquote>
</aside>
<p>This is already available. Check out <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">Slicer programming tutorials</a> and <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository">Slicer script repository</a>. If you have any questions then you can post them here.</p>

---
