---
topic_id: 17727
title: "Numpy Array What Is That"
date: 2021-05-21
url: https://discourse.slicer.org/t/17727
---

# Numpy array, what is that?

**Topic ID**: 17727
**Date**: 2021-05-21
**URL**: https://discourse.slicer.org/t/numpy-array-what-is-that/17727

---

## Post #1 by @NoobForSlicer (2021-05-21 20:06 UTC)

<p>So I was reading a lot about things in scripts depository. I just learned how to change the background color to white and I am interested to learn more about python in general.</p>
<p>I read a lot and a word 'numpy array" keeps coming up.</p>
<p>What is a “numpy array”?</p>
<h3><a name="p-59991-get-axial-slice-as-numpy-array-1" class="anchor" href="#p-59991-get-axial-slice-as-numpy-array-1" aria-label="Heading link"></a>Get axial slice as numpy array</h3>
<pre><code>import SampleData
volumeNode = SampleData.SampleDataLogic().downloadMRHead()
sliceIndex = 12

voxels = slicer.util.arrayFromVolume(volumeNode)  # Get volume as numpy array
slice = voxels[sliceIndex:,:]  # Get one slice of the volume as numpy array
</code></pre>

---

## Post #2 by @lassoan (2021-05-21 22:03 UTC)

<p>Numpy array is the de facto standard for storing n-dimensional array data in Python. You can process these arrays using functions implemented in <a href="https://numpy.org/">numpy</a> and in hundreds of thousands of other Python packages.</p>

---
