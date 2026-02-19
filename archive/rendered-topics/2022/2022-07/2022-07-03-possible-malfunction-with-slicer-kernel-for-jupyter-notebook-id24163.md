---
topic_id: 24163
title: "Possible Malfunction With Slicer Kernel For Jupyter Notebook"
date: 2022-07-03
url: https://discourse.slicer.org/t/24163
---

# Possible malfunction with Slicer kernel for Jupyter notebook?

**Topic ID**: 24163
**Date**: 2022-07-03
**URL**: https://discourse.slicer.org/t/possible-malfunction-with-slicer-kernel-for-jupyter-notebook/24163

---

## Post #1 by @KateDelb (2022-07-03 15:00 UTC)

<p>Hi!</p>
<p>I’m trying to import the sitkUtils package in Jupyter notebook, I’m using the 3dSlicer kernel, which has worked perfectly for me before:</p>
<pre><code class="lang-auto">import sitkUtils as su
</code></pre>
<p>In a following cell I check if su is imported, which gives a correct output:</p>
<pre><code class="lang-auto">su
&gt;&gt; &lt;module 'sitkUtils' from 'C:\\Users\\user\\AppData\\Local\\NA-MIC\\Slicer 4.11.20210226\\bin\\Python\\sitkUtils.py'&gt;
</code></pre>
<p>A few cells later, I use a function in the su library and get the error</p>
<pre><code class="lang-auto">InputVolumeNode = su.PushVolumeToSlicer(input_volume)
&gt;&gt;NameError: name 'su' is not defined
</code></pre>
<p>However, rerunning this cell then says that other random packages and variables are not defined (which, again, were functioning well in other notebook cells):</p>
<pre><code class="lang-auto">&gt;&gt;NameError: name 'patient_list' is not defined
&gt;&gt;NameError: name 'sitk' is not defined
</code></pre>
<p>All of this is happening in 1 Jupyter notebook so I have no clue what could be wrong, but my guess is that the kernel is malfunctioning somehow?<br>
Everything worked fine this morning.</p>
<p>I have tried restarting the kernel and restarting the terminal from which I am running the jupyter notebook. Running other pieces of code in different kernels seems to work fine as well.</p>
<p>Other than this, idk how to proceed, any advice?</p>

---
