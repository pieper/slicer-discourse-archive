# Radiomics Library

**Topic ID**: 28996
**Date**: 2023-04-18
**URL**: https://discourse.slicer.org/t/radiomics-library/28996

---

## Post #1 by @katienefoa_soro (2023-04-18 21:06 UTC)

<p>Hello everyone, i amnew here and i am doing a master’s degree in Data science. i need help with radiomic lib, I did setup an environment for Python and I want to install radio mic in the env for my project.</p>
<ol>
<li>List item</li>
</ol>

---

## Post #2 by @curtislisle (2023-04-19 00:01 UTC)

<p>Hello,<br>
This forum is particularly for supporting the uses of the 3D Slicer application , but I have done some work with PyRadiomics before. You will find installation and use examples here: <a href="https://pyradiomics.readthedocs.io/en/latest/" rel="noopener nofollow ugc">https://pyradiomics.readthedocs.io/en/latest/</a>. Good luck!</p>

---

## Post #3 by @katienefoa_soro (2023-05-27 13:22 UTC)

<p>But I see that Slicer can do the work I want to do. Pyradiomics project…I need help too if possible.</p>

---

## Post #4 by @curtislisle (2023-05-28 03:08 UTC)

<p>If you can be more specific about your needs regarding the use of py radiomics, we can offer more detailed suggestions. Do you have a certain set of medical images you need to analyze? For example, PyRadiomics can be run on a set of images using a Python/Juoyter notebook , but Slicer has many capabilities to prepare the images. What is the goal you would like to achieve?</p>

---

## Post #5 by @katienefoa_soro (2023-05-29 13:40 UTC)

<p>Thanks for replying. I have a project that I am working on, combining images and numerical data(lung) to detect lung cancer, and the mentor asked me to install pyradiomics<br>
1-Install via pip<br>
2-install via Conda(I think this is the best option for me because I used Miniconda for plenty of projects).<br>
3-install from source<br>
4-use docker etc,<br>
but none of them are working yet for me. I am using Windows 11.</p>

---

## Post #6 by @curtislisle (2023-05-29 18:20 UTC)

<p>I replied to you via a direct message.  I’ll try to help, but this forum is focused on 3D Slicer.  Please contact me through email (address sent via direct message) instead of using this forum.  Thank you.</p>

---

## Post #7 by @rbumm (2023-06-01 19:30 UTC)

<p>The TotalSegmentator tool provides <a href="https://github.com/wasserth/TotalSegmentator#advanced-settings">Radiomics and statistical output</a> for its segments.</p>

---

## Post #8 by @rbumm (2023-06-01 19:32 UTC)

<p>Or you segment lungs and lobes with LungCTSegmenter and use the “Lung Segmentation” as input for the Pyradioics extension</p>

---

## Post #9 by @fedorov (2023-06-01 20:09 UTC)

<p><a class="mention" href="/u/katienefoa_soro">@katienefoa_soro</a> if you want to be able to use <a href="https://github.com/AIM-Harvard/pyradiomics">pyradiomics</a> from Slicer, you should do the following:</p>
<ol>
<li>Navigate to Slicer ExtensionManager and install <a href="https://github.com/AIM-Harvard/SlicerRadiomics">“Radiomics” extension</a>
</li>
<li>Restart Slicer</li>
<li>Open “Radiomics” extension (this is needed to install some of the dependencies, which are installed on the first launch of the extension)</li>
</ol>
<p>Assuming everything went well, after those steps you should be able to import the package from your python code in Slicer or in the python console as follows and start using that package:</p>
<pre><code class="lang-python">import radiomics
</code></pre>

---

## Post #10 by @katienefoa_soro (2023-06-03 11:48 UTC)

<p>Yes i wanted to but i am more comfortable with Jupyter</p>

---
