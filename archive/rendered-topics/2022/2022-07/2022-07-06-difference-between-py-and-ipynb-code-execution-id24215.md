# Difference between .py and .ipynb code execution

**Topic ID**: 24215
**Date**: 2022-07-06
**URL**: https://discourse.slicer.org/t/difference-between-py-and-ipynb-code-execution/24215

---

## Post #1 by @rbaheti (2022-07-06 22:59 UTC)

<p>Hi,<br>
I’ve been executing sitk commands using Jupyter Notebook (.ipynb) and it’s been working perfectly. As a next step I’ve to execute the python code on Matlab using pyrunfile() command. This requires the code to have a .py extension. But the same code doesn’t work on Spyder (.py). Any particular reason for this?</p>
<p>By best guess where the code fails is while executing Geodesic Active Contour.</p>

---

## Post #2 by @lassoan (2022-07-07 00:43 UTC)

<p>It seems that these questions are not related to Slicer. You may try to ask for help on Matlab forums.</p>

---

## Post #3 by @rbaheti (2022-07-07 16:18 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a><br>
The problem isn’t with matlab execution. The code fails on Spyder - with or without matlab being used.</p>

---

## Post #4 by @lassoan (2022-07-07 16:47 UTC)

<p>Any code that you can run in some stock Python environment (in the Python console, in Spyder, or in any other Python IDE) then it should work well in 3D Slicer’s virtual Python environment. If you encounter any problem doing this then let us know.</p>

---

## Post #5 by @rbaheti (2022-07-07 17:51 UTC)

<p>I’ve tried to look for a solution for this online but bore unfruitful results. The problem still remains: The same code works on Jupyter (.ipynb) but not on Spyder (.py). What can I do to fix this?</p>

---

## Post #6 by @jamesobutler (2022-07-07 17:52 UTC)

<p>What is the specific failure in the code execution? Is there a traceback? Are you trying to <code>import slicer</code> outside of the slicer python environment?</p>

---

## Post #7 by @lassoan (2022-07-07 18:16 UTC)

<aside class="quote no-group" data-username="rbaheti" data-post="5" data-topic="24215">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/b9bd4f/48.png" class="avatar"> rbaheti:</div>
<blockquote>
<p>The same code works on Jupyter (.ipynb) but not on Spyder (.py)</p>
</blockquote>
</aside>
<p>This is the forum of <code>Slicer</code> (medical image analysis and visualization software) not <code>Spyder</code> (Python IDE). Maybe you have mistakenly posted your question here.</p>
<p>If you think the problem is with SimpleITK then you can ask about it on the <a href="https://discourse.itk.org/">ITK forum</a>.</p>

---

## Post #8 by @rbaheti (2022-07-08 02:49 UTC)

<p>Solved the issue. It wasn’t an issue with Slicer or Spyder - I just rebooted the system and it worked.</p>

---
