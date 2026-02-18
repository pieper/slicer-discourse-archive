# Jupyter notebooks are now usable in 3D Slicer

**Topic ID**: 3438
**Date**: 2018-07-10
**URL**: https://discourse.slicer.org/t/jupyter-notebooks-are-now-usable-in-3d-slicer/3438

---

## Post #1 by @lassoan (2018-07-10 02:42 UTC)

<p>We worked hard with <a class="mention" href="/u/jcfr">@jcfr</a> during the during <a href="https://na-mic.github.io/ProjectWeek/PW28_2018_GranCanaria/">Slicer project week in Gran Canaria</a> and we are excited to share one of the newest developments: <strong><a href="https://jupyter.org/">Jupyter notebook</a> support</strong>.</p>
<p>You can create interactive Python notebooks to run Slicer code and show resulting text data or slicer/3D view content in the notebook. Great for experimenting and sharing code and results with others.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93d02fef499b55526161e0d4a621abf600263291.png" data-download-href="/uploads/short-url/l5Ce5D6TNkyVUEVQavYAh0nhKMh.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93d02fef499b55526161e0d4a621abf600263291_2_662x500.png" alt="image" data-base62-sha1="l5Ce5D6TNkyVUEVQavYAh0nhKMh" width="662" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93d02fef499b55526161e0d4a621abf600263291_2_662x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93d02fef499b55526161e0d4a621abf600263291_2_993x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93d02fef499b55526161e0d4a621abf600263291.png 2x" data-dominant-color="D6D5D7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1270×959 146 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>See an example notebook <a href="https://github.com/lassoan/SlicerNotebooks/blob/master/My%20second%20notebook.ipynb">here</a>, which shows loading of a sample data set, display of a slice view, creation and display of a surface model. See information about how to set up and use notebooks <a href="https://github.com/Slicer/SlicerJupyter">here</a>.</p>
<p>There are still a number of limitations (currently the extension is only available for Windows - will be fixed within a week; auto-complete is not implemented yet; display options are limited, etc.), but it would be great to hear from you, to keep us motivated and help us decide where to focus our efforts.</p>

---

## Post #2 by @Fernando (2018-07-14 20:19 UTC)

<p>This is awesome, looking forward to trying as soon as it’s ready for other platforms!</p>

---

## Post #3 by @lassoan (2018-08-21 11:14 UTC)

<p>A post was split to a new topic: <a href="/t/how-to-start-slicer-jupyter-kernel/3855">How to start Slicer Jupyter kernel?</a></p>

---

## Post #4 by @Saima (2018-08-29 12:56 UTC)

<p>Dear Andras,<br>
Could you please tell me why auto complete is not working for jupyter. I am using nightly version?</p>
<p>thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #5 by @lassoan (2018-08-29 16:23 UTC)

<p>In recent nightly builds, with great help from <a class="mention" href="/u/ihnorton">@ihnorton</a>, we added auto-complete (press Tab key):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b0bf76a6ac4f511fa6831158060cfc7ad7b3d8a.png" data-download-href="/uploads/short-url/jQ40oIF2ALjkxX8zdLqkYFsgll0.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b0bf76a6ac4f511fa6831158060cfc7ad7b3d8a.png" alt="image" data-base62-sha1="jQ40oIF2ALjkxX8zdLqkYFsgll0" width="690" height="366" data-dominant-color="ECEEEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">768×408 28.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>We also added inspection (press Shift-Tab) to get quick documentation on a Python methods. Currently, limitation is that documentation can only retrieved for native Python code, but we’ll work on extending this to wrapped C++ methods, too (you can track progress of this task <a href="https://github.com/Slicer/SlicerJupyter/issues/13">here</a>).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33fb389786bb75f8bd59027df981427b02211d35.png" data-download-href="/uploads/short-url/7pQAyyNGGSzFMzaJnqDFyUzeucl.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33fb389786bb75f8bd59027df981427b02211d35.png" alt="image" data-base62-sha1="7pQAyyNGGSzFMzaJnqDFyUzeucl" width="690" height="412" data-dominant-color="EFEFEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">769×460 29.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>To get these features:</p>
<ul>
<li>install a recent nightly version of Slicer</li>
<li>install SlicerJupyter extension from the extension manager</li>
<li>go to JupyterKernel module</li>
<li>click “Install Slicer kernel in Jupyter” button</li>
</ul>

---

## Post #6 by @lassoan (2018-10-17 19:59 UTC)

<p>5 posts were split to a new topic: <a href="/t/slicer-jupyter-notebooks-can-be-launched-using-just-a-web-browser/4445">Slicer Jupyter notebooks can be launched using just a web browser</a></p>

---
