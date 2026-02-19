---
topic_id: 14962
title: "Problem With Viewinteractivewidget No Output Visible"
date: 2020-12-09
url: https://discourse.slicer.org/t/14962
---

# Problem with ViewInteractiveWidget - no output visible

**Topic ID**: 14962
**Date**: 2020-12-09
**URL**: https://discourse.slicer.org/t/problem-with-viewinteractivewidget-no-output-visible/14962

---

## Post #1 by @seaninko (2020-12-09 13:02 UTC)

<p>Hello,</p>
<p>I have a problem with ViewInteractiveWidget method. It works fine when I launch jupyter server within Slicer, but when I use an external jupyter server it just shows the empty output cell without any rendering. No error message is displayed (neither in the notebook nor Slicer). Do you have any suggestions on what might went wrong? I tied it with Slicer 4.11.2 and 4.13.0 (2020-12-07) with the same result.</p>
<p>Many thanks,<br>
Sebastian</p>

---

## Post #2 by @lassoan (2020-12-09 14:24 UTC)

<p>You need to install the prerequisite Python packages in the external Jupyter server. I’ve added more details here: <a href="https://github.com/Slicer/SlicerJupyter/blob/master/README.md#using-external-jupyter-server">https://github.com/Slicer/SlicerJupyter/blob/master/README.md#using-external-jupyter-server</a></p>

---

## Post #3 by @seaninko (2020-12-10 10:27 UTC)

<p>Dear Iassoan,</p>
<p>thank you very much for the reply. I checked it, and it seems I have installed all required prerequisite Python packages. The results is unfortunately as follows:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6ebde15f84bd12de0070b1c4325b45852407e939.png" data-download-href="/uploads/short-url/fNFkZoxyBsYKV7t3OlCy1ZRwSPn.png?dl=1" title="slicernb_problem" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6ebde15f84bd12de0070b1c4325b45852407e939.png" alt="slicernb_problem" data-base62-sha1="fNFkZoxyBsYKV7t3OlCy1ZRwSPn" width="672" height="500" data-dominant-color="FEFEFE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicernb_problem</span><span class="informations">1096×815 3.73 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Meanwhile, I noticed that there is probably sth wrong with my nbextensions configuration. I will appreciate any other suggestions on what else should I check to resolve the problem.</p>
<p>Have a nice day,<br>
Sebastian</p>

---

## Post #4 by @lassoan (2020-12-14 04:25 UTC)

<p>Have you installed pycanvas, etc. in your external Python environment (where you run the jupyter server)? Check if you get any errors in either the notebook server or in Slicer.</p>

---

## Post #5 by @seaninko (2020-12-22 09:01 UTC)

<p>I have installed all what is installed in the code: <a href="https://github.com/Slicer/SlicerJupyter/blob/master/JupyterNotebooks/JupyterNotebooks.py" rel="noopener nofollow ugc">https://github.com/Slicer/SlicerJupyter/blob/master/JupyterNotebooks/JupyterNotebooks.py</a>, lines 53 - 55. Unfortunately I got the described effect. Now I removed all extensions along with Slicer and try the clean installation. I hope I am able to identify what went wrong.</p>

---
