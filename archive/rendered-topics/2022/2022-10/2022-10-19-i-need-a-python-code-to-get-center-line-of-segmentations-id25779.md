# I need a python code to get center line of segmentations

**Topic ID**: 25779
**Date**: 2022-10-19
**URL**: https://discourse.slicer.org/t/i-need-a-python-code-to-get-center-line-of-segmentations/25779

---

## Post #1 by @hbr (2022-10-19 15:17 UTC)

<p>i wanna write a code to get center of seg and dont know how do it. please help</p>

---

## Post #2 by @lassoan (2022-10-19 16:21 UTC)

<p>You can use Extract Centerline module logic. See the source code and how it is used from the widget class <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/913e0f9a7a4a085b80d877ff3730e98374b9ee98/ExtractCenterline/ExtractCenterline.py">here</a>.</p>

---

## Post #3 by @hbr (2022-10-20 03:53 UTC)

<p>thank you lassoan. i have a problem to install slicer on vs code and test my code and use the widgets class.</p>
<p>Do you have any solution to help me?</p>

---

## Post #4 by @jcfr (2022-10-20 04:02 UTC)

<p>As a first step, we suggest you follow the <code>Tutorials for software developers</code> available on tutorial pages referenced at <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#tutorials">https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#tutorials</a>.</p>
<p>These should help you understand how to create a new module and edit its code.</p>

---

## Post #5 by @hbr (2022-10-20 04:20 UTC)

<p>thank you jean.</p>
<p>But it is not my problem. I could not run my code in vscode. slicer not recognized true and their mudules not loaded in vscode.</p>

---

## Post #6 by @jcfr (2022-10-20 05:19 UTC)

<p>Considering Slicer modules written in python are expected to be discovered and loaded by the Slicer application, you can not “run” the corresponding python code in an editor like <code>vscode</code>.</p>
<p>Such code editor is  helpful to write the code by leveraging syntax coloring, linting, …</p>
<p>The execution of the corresponding code happen in Slicer itself.</p>
<p>To further understand these concept, I still recommend you review the tutorials I referenced above. More may start by reviewing <a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx">this tutorial</a>.</p>

---

## Post #7 by @hbr (2022-10-20 05:31 UTC)

<p>thanks.</p>
<p>i think that i could not specify my problem correctly.</p>
<p>as an example when i import slicer there is not any module in it. there are nothings to use as modules.</p>

---

## Post #8 by @jcfr (2022-10-20 05:52 UTC)

<p>Assuming you are running the code in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#application-menu">python interpreter</a> available in the application, modules are available in <code>silcer.modules</code>.</p>
<p>For example, see <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-color-legend-for-a-volume-node" class="inline-onebox">Script repository — 3D Slicer documentation</a></p>
<p>To be able to help you more effectively, consider including screenshot to illustrate your problem.</p>

---

## Post #9 by @hbr (2022-10-20 06:00 UTC)

<p>Exactly my problem is here. <code>silcer.modules</code> not working.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b79d30d7af6057dce381c7329ef9b80cde33cc15.png" data-download-href="/uploads/short-url/qck9ILWIYzqxE24QhiN5BuZB5KR.png?dl=1" title="Screenshot from 2022-10-20 09-28-49" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b79d30d7af6057dce381c7329ef9b80cde33cc15_2_690x365.png" alt="Screenshot from 2022-10-20 09-28-49" data-base62-sha1="qck9ILWIYzqxE24QhiN5BuZB5KR" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b79d30d7af6057dce381c7329ef9b80cde33cc15_2_690x365.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b79d30d7af6057dce381c7329ef9b80cde33cc15_2_1035x547.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b79d30d7af6057dce381c7329ef9b80cde33cc15.png 2x" data-dominant-color="212222"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2022-10-20 09-28-49</span><span class="informations">1090×578 38.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @jcfr (2022-10-20 06:08 UTC)

<p>Since <code>PythonSlicer</code> is a launcher starting regular python interpreter, the Slicer modules are not available. These are loaded by the Slicer application.</p>
<p>Instead, you should consider:</p>
<ul>
<li>copy/past the code in the Slicer python console</li>
<li>writing Slicer module (see tutorial above) and then click on a <code>Reload &amp; Test</code>
</li>
</ul>

---

## Post #11 by @lassoan (2022-10-20 20:44 UTC)

<p>You can also attach Visual Studio code to the Slicer application once the application is running and set up its Python environments. See instructions <a href="https://slicer.readthedocs.io/en/latest/developer_guide/debugging/python.html">here</a>. You can then see all modules, have auto-complete, method documentation, etc.</p>
<p>You can also use Jupyter notebooks, using Slicer as the kernel (using <a href="https://github.com/Slicer/SlicerJupyter">SlicerJupyter extension</a>).</p>

---

## Post #12 by @hbr (2022-10-22 04:44 UTC)

<p>thank you Andras</p>
<p>it is very useful for me.</p>

---
