# Cannot import JupyterNotebooksLib

**Topic ID**: 11967
**Date**: 2020-06-09
**URL**: https://discourse.slicer.org/t/cannot-import-jupyternotebookslib/11967

---

## Post #1 by @Ponyo2311 (2020-06-09 18:25 UTC)

<p>Hi,</p>
<p>To install the JupyterNotebook extension on Slicer and to add a Slicer kernel on Jupyter I followed the steps on <a href="https://github.com/Slicer/SlicerJupyter/blob/master/README.md#setup" rel="nofollow noopener">https://github.com/Slicer/SlicerJupyter/blob/master/README.md#setup</a>.</p>
<p>After I tried in the new Slicer kernel <em><strong>import JupyterNotebooksLib</strong> as slicernb</em>, I got <em>ModuleNotFoundError: No module named ‘JupyterNotebooksLib’</em>.</p>
<p>I’m using Slicer 4.11, Windows10, Anaconda with different version of Python (3.7) than which is used by Slicer (3.6).</p>
<p>During the installation steps I encountered a problem with installing the jupyter lab:<br>
<em>PS C:\User&gt; conda install -c conda-forge nodejs<br>
Traceback (most recent call last):<br>
File “C:\ProgramData\Anaconda3\Scripts\conda-script.py”, line 11, in <br>
from conda.cli import main<br>
ModuleNotFoundError: No module named ‘conda’</em></p>
<p>Is this a Python version or a path problem?</p>

---

## Post #2 by @lassoan (2020-06-09 21:15 UTC)

<aside class="quote no-group" data-username="Ponyo2311" data-post="1" data-topic="11967">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ponyo2311/48/7078_2.png" class="avatar"> Ponyo2311:</div>
<blockquote>
<p>After I tried in the new Slicer kernel <em><strong>import JupyterNotebooksLib</strong> as slicernb</em> , I got</p>
</blockquote>
</aside>
<p>Can you post a screenshot?<br>
Make sure you select “Slicer-4.11” as Jupyter kernel.</p>
<aside class="quote no-group" data-username="Ponyo2311" data-post="1" data-topic="11967">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ponyo2311/48/7078_2.png" class="avatar"> Ponyo2311:</div>
<blockquote>
<p>During the installation steps I encountered a problem with installing the jupyter lab:<br>
<em>PS C:\User&gt; conda install -c conda-forge nodejs<br>
Traceback (most recent call last):<br>
File “C:\ProgramData\Anaconda3\Scripts\conda-script.py”, line 11, in<br>
from conda.cli import main<br>
ModuleNotFoundError: No module named ‘conda’</em></p>
</blockquote>
</aside>
<p>This error is not related to Slicer, but to your conda install. Make sure you activate your virtual environment before you attempt to run any script (simply starting a command prompt in the Scripts folder is not enough).</p>

---

## Post #3 by @Ponyo2311 (2020-06-10 10:14 UTC)

<p>Thanks for the reply.</p>
<p>I created and activated a python virtual environment via command prompt (run as admin) and have run all lines from the tutorial, including:</p>
<p>conda install -c conda-forge nodejs<br>
pip install ipywidgets ipyevents ipycanvas<br>
jupyter labextension install <span class="mention">@jupyter-widgets</span>/jupyterlab-manager<br>
jupyter labextension install <span class="mention">@jupyter-widgets</span>/jupyterlab-manager ipycanvas<br>
jupyter labextension install <span class="mention">@jupyter-widgets</span>/jupyterlab-manager ipyevents</p>
<p>This time it seemed to be installed, but I still get the same error message when trying to import the module in a new kernel:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/186900e60485972bb13df11c8eca6f5534d8a3be.jpeg" data-download-href="/uploads/short-url/3tWqyhr8vQ67yaLGcgwL0IdTztk.jpeg?dl=1" title="error_message" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/186900e60485972bb13df11c8eca6f5534d8a3be_2_690x184.jpeg" alt="error_message" data-base62-sha1="3tWqyhr8vQ67yaLGcgwL0IdTztk" width="690" height="184" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/186900e60485972bb13df11c8eca6f5534d8a3be_2_690x184.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/186900e60485972bb13df11c8eca6f5534d8a3be_2_1035x276.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/186900e60485972bb13df11c8eca6f5534d8a3be_2_1380x368.jpeg 2x" data-dominant-color="F8F8F8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error_message</span><span class="informations">1548×415 66.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2020-06-10 12:29 UTC)

<p>Did you choose the “Slicer-4.11” kernel in the notebook?</p>

---

## Post #5 by @Ponyo2311 (2020-06-10 12:31 UTC)

<p>Yes, I did.</p>
<p>Could it be that my python virtual environment wasn’t in the Slicer directory?</p>

---

## Post #6 by @lassoan (2020-06-10 12:34 UTC)

<p>Are other Slicer features available? For example, do you have access to <code>slicer.util.getNode</code> function? When you started the kernel, did a Slicer application instance start? Can you post a screenshot of your entire browser window (not just a single cell)?</p>

---

## Post #7 by @Ponyo2311 (2020-06-10 15:04 UTC)

<p>Slicer application does start with kernel.<br>
I have access to multiple Slicer features (including slicer.util.getNode) too:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0da95d25c2edd44bbc84750a34740e470393bdc.png" alt="other_modules" data-base62-sha1="w59gKgkXlW8WAHDxr9uMPEDJyTW" width="510" height="297"></p>

---

## Post #8 by @lassoan (2020-06-10 15:25 UTC)

<p>Which Slicer version are you using? Can you copy here the full application log (menu: Help / Report a bug) here?</p>

---

## Post #9 by @Ponyo2311 (2020-06-10 15:50 UTC)

<p>[DEBUG][Qt] 10.06.2020 17:37:35 [] (unknown:0) - Session start time …: 2020-06-10 17:37:35<br>
[DEBUG][Qt] 10.06.2020 17:37:35 [] (unknown:0) - Slicer version …: 4.11.0-2020-05-04 (revision 29031 / 88bff56) win-amd64 - installed release<br>
[DEBUG][Qt] 10.06.2020 17:37:35 [] (unknown:0) - Operating system …: Windows /  Personal / (Build 18362, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 10.06.2020 17:37:35 [] (unknown:0) - Memory …: 4001 MB physical, 11169 MB virtual<br>
[DEBUG][Qt] 10.06.2020 17:37:35 [] (unknown:0) - CPU …: GenuineIntel , 4 cores, 4 logical processors<br>
[DEBUG][Qt] 10.06.2020 17:37:35 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 10.06.2020 17:37:35 [] (unknown:0) - Qt configuration …: version 5.10.1, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 10.06.2020 17:37:35 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 10.06.2020 17:37:35 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 10.06.2020 17:37:35 [] (unknown:0) - Application path …: C:/Users/Domi/AppData/Local/NA-MIC/Slicer 4.11.0-2020-05-04/bin<br>
[DEBUG][Qt] 10.06.2020 17:37:35 [] (unknown:0) - Additional module paths …: C:/Users/Domi/AppData/Roaming/NA-MIC/Extensions-29031/SlicerJupyter/lib/Slicer-4.11/qt-loadable-modules<br>
[DEBUG][Python] 10.06.2020 17:38:08 [Python] (C:\Users\Domi\AppData\Local\NA-MIC\Slicer 4.11.0-2020-05-04\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 10.06.2020 17:38:10 [Python] (C:\Users\Domi\AppData\Local\NA-MIC\Slicer 4.11.0-2020-05-04\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 10.06.2020 17:38:10 [Python] (C:\Users\Domi\AppData\Local\NA-MIC\Slicer 4.11.0-2020-05-04\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 10.06.2020 17:38:11 [] (unknown:0) - Switch to module:  “Welcome”</p>

---

## Post #10 by @lassoan (2020-06-10 16:31 UTC)

<p>Can you do this in the Slicer instance that Jupyter started? (it shows a read message in the status bar that this instance is controlled by Jupyter)</p>
<p>Does this file exist on your computer?<br>
<code>c:\Users\Domi\AppData\Roaming\NA-MIC\Extensions-29031\SlicerJupyter\Lib\Slicer-4.11\qt-scripted-modules\JupyterNotebooksLib\__init__.py</code></p>
<p>You may also try to reinstall SlicerJupyter and extension and make sure that installation is completed (do not press “Close” button while the extension is being installed but wait for the “Restart” button to appear and click that).</p>

---

## Post #11 by @Ponyo2311 (2020-06-10 17:11 UTC)

<p>I reinstalled the extension properly waiting for the restart button to pop up when I tried to figure out what was wrong.</p>
<p>On the other hand the whole <strong>qt-scripted-modules</strong> folder is missing.<br>
Should I reinstall Slicer?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13eace2f24fdf53617572f70744ea0f16c68ff22.jpeg" data-download-href="/uploads/short-url/2Qc8GWd1YtFu2okCA1LV73B5jIC.jpeg?dl=1" title="missing_folder" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/13eace2f24fdf53617572f70744ea0f16c68ff22_2_345x158.jpeg" alt="missing_folder" data-base62-sha1="2Qc8GWd1YtFu2okCA1LV73B5jIC" width="345" height="158" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/13eace2f24fdf53617572f70744ea0f16c68ff22_2_345x158.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/13eace2f24fdf53617572f70744ea0f16c68ff22_2_517x237.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/13eace2f24fdf53617572f70744ea0f16c68ff22_2_690x316.jpeg 2x" data-dominant-color="F7F7F7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">missing_folder</span><span class="informations">888×408 79.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The bug report with the Kernel open:<br>
[DEBUG][Python] 10.06.2020 19:05:18 [Python] (C:\Users\Domi\AppData\Local\NA-MIC\Slicer 4.11.0-2020-05-04\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 10.06.2020 19:05:21 [Python] (C:\Users\Domi\AppData\Local\NA-MIC\Slicer 4.11.0-2020-05-04\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 10.06.2020 19:05:21 [Python] (C:\Users\Domi\AppData\Local\NA-MIC\Slicer 4.11.0-2020-05-04\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 10.06.2020 19:05:00 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 2020-06-10 19:05:00<br>
[DEBUG][Qt] 10.06.2020 19:05:00 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 4.11.0-2020-05-04 (revision 29031 / 88bff56) win-amd64 - installed release<br>
[DEBUG][Qt] 10.06.2020 19:05:01 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: Windows /  Personal / (Build 18362, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 10.06.2020 19:05:01 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 4001 MB physical, 11169 MB virtual<br>
[DEBUG][Qt] 10.06.2020 19:05:01 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: GenuineIntel , 4 cores, 4 logical processors<br>
[DEBUG][Qt] 10.06.2020 19:05:01 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 10.06.2020 19:05:01 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Qt configuration …: version 5.10.1, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 10.06.2020 19:05:01 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 10.06.2020 19:05:01 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 10.06.2020 19:05:01 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Application path …: C:/Users/Domi/AppData/Local/NA-MIC/Slicer 4.11.0-2020-05-04/bin<br>
[DEBUG][Qt] 10.06.2020 19:05:01 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths …: C:/Users/Domi/AppData/Roaming/NA-MIC/Extensions-29031/SlicerJupyter/lib/Slicer-4.11/qt-loadable-modules<br>
[DEBUG][Qt] 10.06.2020 19:05:22 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Welcome”<br>
[INFO][Stream] 10.06.2020 19:05:24 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Jupyter connection file: [C:\Users\Domi\AppData\Roaming\jupyter\runtime\kernel-41b84ba5-d377-4f67-8d20-c9f56752253c.json]<br>
[DEBUG][Qt] 10.06.2020 19:05:29 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Starting Jupyter kernel server</p>

---

## Post #12 by @lassoan (2020-06-10 17:23 UTC)

<p>Yes, please install the latest Slicer Preview Release, I cannot check it anymore what the extension package contained in the 2020-05-04 version, there might have been some problem with the nightly build that day.</p>

---

## Post #13 by @Ponyo2311 (2020-06-10 20:33 UTC)

<p>I installed the latest Slicer 4.11 release and the problem’s solved!</p>
<p>Thank you so much for your help.</p>

---
