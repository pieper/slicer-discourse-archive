# Threshold min and max values

**Topic ID**: 28643
**Date**: 2023-03-29
**URL**: https://discourse.slicer.org/t/threshold-min-and-max-values/28643

---

## Post #1 by @Contente (2023-03-29 04:50 UTC)

<p>I’m trying to create an automatic segment generator by using the threshold method for any given DICOM images.<br>
However, as it may seems, the values from the extremes of the range varies with distinct Volume Nodes provided in the Segmentation Editor.</p>
<p>Is there a way to calculate those values or to generalize them (making them constant to a given input)?</p>

---

## Post #2 by @muratmaga (2023-03-29 05:10 UTC)

<p>You can use the automated threshold algorithms (shanbhag, isodata, otsu, etc…) for reproducibility.</p>

---

## Post #3 by @Contente (2023-03-29 17:51 UTC)

<p>Yes, I’m attempting to do this.</p>
<p>However I’m not sure how to set the max and minimum values of the thresholdrange giving a certain DICOM image (and Volume Node consequently). I’m having a bad time to find this information in Slicer’s Github repo. Do you know where can I find it?</p>

---

## Post #4 by @muratmaga (2023-03-29 18:45 UTC)

<p>Automated threshold methods do not require min, max value of the volume. The calculate it based on the volume’s intensity distribution and the model they assume that to be (bimodal, trimodal etc).</p>
<p>You can obtain the min/max of the volume by reading the intensity values as a numpy array.  Using MRhead as an example data.</p>
<pre><code class="lang-auto">&gt;&gt;&gt; volumeNode = getNode("MRHead")
&gt;&gt;&gt; voxels = slicer.util.arrayFromVolume(volumeNode)
&gt;&gt;&gt; voxels.max()
279
&gt;&gt;&gt; voxels.min()
0
</code></pre>

---

## Post #5 by @Contente (2023-03-29 19:31 UTC)

<p>Thank you very much!</p>

---
