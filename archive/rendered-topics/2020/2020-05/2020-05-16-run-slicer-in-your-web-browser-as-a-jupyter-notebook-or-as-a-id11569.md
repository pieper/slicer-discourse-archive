---
topic_id: 11569
title: "Run Slicer In Your Web Browser As A Jupyter Notebook Or As A"
date: 2020-05-16
url: https://discourse.slicer.org/t/11569
---

# Run Slicer in your web browser - as a Jupyter notebook or as a full application

**Topic ID**: 11569
**Date**: 2020-05-16
**URL**: https://discourse.slicer.org/t/run-slicer-in-your-web-browser-as-a-jupyter-notebook-or-as-a-full-application/11569

---

## Post #1 by @lassoan (2020-05-16 01:51 UTC)

<p>It has been possible to use Slicer from Jupyter notebooks but the most recent Slicer Preview Release takes this to a whole new level.</p>
<p><strong><a href="https://mybinder.org/v2/gh/slicer/SlicerNotebooks/master">Click here to try a few example interactive notebooks now</a></strong> - or see a short video demonstrating the new features:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="oZ3_cRXX2QM" data-video-title="Medical image processing in your web browser using Jupyter notebooks and 3D Slicer" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=oZ3_cRXX2QM" target="_blank" class="video-thumbnail" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/oZ3_cRXX2QM/maxresdefault.jpg" title="Medical image processing in your web browser using Jupyter notebooks and 3D Slicer" width="" height="">
  </a>
</div>

<p>Highlights:</p>
<ol>
<li>Improved interactive use</li>
</ol>
<p>You can now use IPython widgets (sliders, buttons, etc.) to control Slicer or adjust processing and visualization parameters. For example, CLI module parameters can be adjusted using slider widgets and results are computed and displayed autoamtically in the notebook:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5afc2fa862bc323a736372a591eac1040f9d046d.jpeg" data-download-href="/uploads/short-url/cYThhkJoDhykwfx7tf87zT1zVOl.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5afc2fa862bc323a736372a591eac1040f9d046d_2_690x480.jpeg" alt="image" data-base62-sha1="cYThhkJoDhykwfx7tf87zT1zVOl" width="690" height="480" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5afc2fa862bc323a736372a591eac1040f9d046d_2_690x480.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5afc2fa862bc323a736372a591eac1040f9d046d_2_1035x720.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5afc2fa862bc323a736372a591eac1040f9d046d_2_1380x960.jpeg 2x" data-dominant-color="8D8D8D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1455×1014 242 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>3D Slicer views are in notebooks are now interactive. You can zoom/rotate 3D views, browse slices, place points, or edit segmentations - right in the notebook:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/890d6996000371ed8f1c5904cc51f194eba0679e.jpeg" data-download-href="/uploads/short-url/jyq9gBSpu5xRLrFv8mpy6vzqUEe.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/890d6996000371ed8f1c5904cc51f194eba0679e_2_690x477.jpeg" alt="image" data-base62-sha1="jyq9gBSpu5xRLrFv8mpy6vzqUEe" width="690" height="477" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/890d6996000371ed8f1c5904cc51f194eba0679e_2_690x477.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/890d6996000371ed8f1c5904cc51f194eba0679e_2_1035x715.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/890d6996000371ed8f1c5904cc51f194eba0679e.jpeg 2x" data-dominant-color="DEDFE6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1309×905 297 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can display and control selected viewers, all viewers, or the entire application in notebook cells. This allows users to implement complete data processing workflows in a notebook, even if certain steps require manual user inputs (3D regions, seed points, etc.).</p>
<ol start="2">
<li>Data node visualization directly in the notebook</li>
</ol>
<p>Slicer takes advantage of rich data visualization capabilities of Jupyter notebooks. For example, markup fiducial list node is displayed as a nicely formatted table, model node is rendered as a 3D object, etc. New visualizers can be added for all MRML node types, if this proves to be useful.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/144fc08e8f6c98983a639b314a1de43dbbc22fa1.png" data-download-href="/uploads/short-url/2TGpTtf38kiyVjRvbEpmNtq5O7f.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/144fc08e8f6c98983a639b314a1de43dbbc22fa1_2_690x392.png" alt="image" data-base62-sha1="2TGpTtf38kiyVjRvbEpmNtq5O7f" width="690" height="392" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/144fc08e8f6c98983a639b314a1de43dbbc22fa1_2_690x392.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/144fc08e8f6c98983a639b314a1de43dbbc22fa1_2_1035x588.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/144fc08e8f6c98983a639b314a1de43dbbc22fa1_2_1380x784.png 2x" data-dominant-color="F4F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1428×812 158 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="3">
<li>Available on the web</li>
</ol>
<p>Since now the full application user interface is available interactively in Jupyter, it is possible to use Slicer remotely, in a web browser, without installing any software locally. For example, <strong><a href="https://mybinder.org/v2/gh/slicer/SlicerNotebooks/master?filepath=SlicerWeb.ipynb">click here to launch Slicer in your web browser using <em>binder</em></a></strong> - a free Jupyter web hosting service. They allocate quite limited computational resources to each instance, but it still sufficient to run Slicer.</p>
<p>[<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45f43a9f0fa6435553d6c36d642574ebe80f181d.jpeg" data-download-href="/uploads/short-url/9YQcCRnQsZVmvgdQRGYJQ9Mkip7.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/45f43a9f0fa6435553d6c36d642574ebe80f181d_2_690x388.jpeg" alt="image" data-base62-sha1="9YQcCRnQsZVmvgdQRGYJQ9Mkip7" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/45f43a9f0fa6435553d6c36d642574ebe80f181d_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/45f43a9f0fa6435553d6c36d642574ebe80f181d_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/45f43a9f0fa6435553d6c36d642574ebe80f181d_2_1380x776.jpeg 2x" data-dominant-color="757374"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 325 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<hr>
<p>Many thanks to Jupyter/xeus team, and especially to Sylvain Corlay and Martin Renou for their excellent work of creating a robust and flexible Jupyter kernel for C++ applications with embedded Python; and to <a class="mention" href="/u/jcfr">@jcfr</a> for setting up the new Slicer docker container.</p>
<p>More information, instructions for local installation: <a href="https://github.com/Slicer/SlicerJupyter" class="inline-onebox">GitHub - Slicer/SlicerJupyter: Extension for 3D Slicer that allows the application to be used from Jupyter notebook</a></p>
<p>Any comments and suggestions are welcome.</p>

---

## Post #2 by @muratmaga (2020-05-16 16:13 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> this is great. COngrats to everyone who helped to develop.</p>
<p>I don’t know much about binder, would the backend benefit from GPU and GPU accelerated rendering for large volumes (that typically our users work with)?</p>

---

## Post #3 by @lassoan (2020-05-16 18:55 UTC)

<p>Yes, you can configure your docker container to use GPU.</p>

---

## Post #4 by @samsonaie (2020-05-22 08:46 UTC)

<p>great to know !!! Thanks a lot for the efforts!</p>

---

## Post #5 by @Fernando (2020-11-20 19:01 UTC)

<p>I want to 1) emphasize how cool this is and 2) ask: is there a way to open Slicer in a new tab using the whole extent of the screen? I have forked the repo to give access to users to a demo of our module:<br>
<a href="https://mybinder.org/v2/gh/fepegar/SlicerNotebooks/9577bab?filepath=SVT-web.ipynb" rel="noopener nofollow ugc"><img src="https://mybinder.org/badge_logo.svg" alt="Binder" width="" height=""></a></p>
<p>At the moment, it looks like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f56cf39c9de1248a983726e854bcc06042043923.jpeg" data-download-href="/uploads/short-url/z18pimX7lakRI4L1YGmZ0yrCz7B.jpeg?dl=1" title="Screen Shot 2020-11-20 at 18.56.05" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f56cf39c9de1248a983726e854bcc06042043923_2_690x381.jpeg" alt="Screen Shot 2020-11-20 at 18.56.05" data-base62-sha1="z18pimX7lakRI4L1YGmZ0yrCz7B" width="690" height="381" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f56cf39c9de1248a983726e854bcc06042043923_2_690x381.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f56cf39c9de1248a983726e854bcc06042043923_2_1035x571.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f56cf39c9de1248a983726e854bcc06042043923_2_1380x762.jpeg 2x" data-dominant-color="989999"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-11-20 at 18.56.05</span><span class="informations">2560×1414 474 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>As you can see, a lot of space is wasted around each side of the window.</p>
<p>I tried <code>slicer.util.mainWindow().setFixedWidth(width)</code> but the window just went “behind” the gray margins.</p>

---

## Post #6 by @lassoan (2020-11-20 19:18 UTC)

<p>It is great that you like it! (it is not obvious that it just how powerful this infrastructure is)</p>
<p>You can open a new browser tab automatically like this:</p>
<pre><code>display(Javascript('window.open("../desktop", "_blank");'))
</code></pre>
<p>You have a couple of options for controlling window size, resolution, and scaling. One option is to display noVNC manual controls (we decided to remove it for sake of simplicity). The other is to configure noVNC and the window manager to automatically resize (it is not so trivial, because you may not want to have very high resolution because rendering may slow down, so above a certain size you would rather scale; and you probably also want to support certain range of screen aspect ratio). noVNC is used very widely and all kinds of automatic resizing/rescaling solutions are already available if you search on the web.</p>

---

## Post #7 by @Fernando (2020-11-20 19:23 UTC)

<p>I see. That’s slightly different to the line I’m using to open the tab automatically:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/fepegar/SlicerNotebooks/blob/9577babf550bc965cb619c1b707ac4d1d44ca8fb/SVT-web.ipynb#L53" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/fepegar/SlicerNotebooks/blob/9577babf550bc965cb619c1b707ac4d1d44ca8fb/SVT-web.ipynb#L53" target="_blank" rel="noopener nofollow ugc">fepegar/SlicerNotebooks/blob/9577babf550bc965cb619c1b707ac4d1d44ca8fb/SVT-web.ipynb#L53</a></h4>
<pre class="onebox"><code class="lang-ipynb"><ol class="start lines" start="43" style="counter-reset: li-counter 42 ;">
<li>   "\n",</li><li>   "# Preload data\n",</li><li>   "say('Loading data...')\n",</li><li>   "slicer.semiologyVisualisation.loadDataButton.clicked()\n",</li><li>   "\n",</li><li>   "say('Done. Trying to open in a new tab...')\n",</li><li>   "html = \"\"\"&lt;a href=\"../desktop\" target=\"_blank\"&gt;&lt;img src=\"https://www.slicer.org/img/3DSlicerLogo-H-Color-218x144.png\"/&gt;\n",</li><li>   "&lt;h1&gt;&lt;center&gt;Click here to manually open 3D Slicer in a new tab&lt;/center&gt;&lt;/h1&gt;&lt;/a&gt;\"\"\"\n",</li><li>   "say(html, header=False)\n",</li><li>   "\n",</li><li class="selected">   "display(Javascript('window.open(\"../desktop\");'))"</li><li>  ]</li><li> }</li><li>],</li><li>"metadata": {</li><li> "kernelspec": {</li><li>  "display_name": "Slicer 4.11",</li><li>  "language": "python",</li><li>  "name": "slicer-4.11"</li><li> },</li><li> "language_info": {</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>But I see in the <a href="https://www.w3schools.com/jsref/met_win_open.asp" rel="noopener nofollow ugc">JavaScript docs</a> (are they?) that <code>"_blank"</code> is the default anyway. In the binder I shared above, with a single cell and a line at the end that opens the new tab, my Chrome blocked the new tab and asked if I wanted to allow pop-ups. But that’s not very important.</p>
<p>I’ll look into noVNC to improve the window size issues. Thanks, <a class="mention" href="/u/lassoan">@lassoan</a>!</p>

---

## Post #8 by @Jan_Alexander (2021-02-17 20:59 UTC)

<p>This is great!</p>
<p>Is there some kind of documentation page I can find somewhere?</p>

---

## Post #9 by @Zakragnos (2021-12-08 13:30 UTC)

<p>Is there a way to make use of a part of slicer’s function in a program? I’m trying to use my own method of segmentation and I want to use slicer’s 3d model generation/volume creation from a segmented arrays of image, to then export it as an stl file. Is there a way I could achieve this?</p>

---

## Post #10 by @pll_llq (2021-12-09 06:16 UTC)

<p>You can use the Slicer application headless to run scripts in the Slicer environment. This can run natively alongside your app or from a docker container (for example if you wish to make it a part of a web app.<br>
In addition to this there is a web server for slicer in the works. This will allow you to get access to functionality of Slicer using web requests.</p>
<p>Although if your segmentation method is python based and you are working with a desktop app I would suggest you consider using Slicer as a host platform and integrate the segmentation into it.</p>

---

## Post #11 by @mau_igna_06 (2021-12-09 10:20 UTC)

<blockquote>
<p>Is there a way to make use of a part of slicer’s function in a program? I’m trying to use my own method of segmentation and I want to use slicer’s 3d model generation/volume creation from a segmented arrays of image, to then export it as an stl file. Is there a way I could achieve this?</p>
</blockquote>
<p>Maybe you can create a python script for Slicer to execute on the console like this:<br>
<code>Slicer.exe --python-script "/full/path/to/myscript.py" --no-splash --no-main-window</code></p>
<p>Inside the script you need to read your segment data (e.g. from a numpy array, maybe like <a href="https://discourse.slicer.org/t/increased-loading-time-for-multiple-segments-from-numpy-array/11026">this</a>), then you need to create a closed surface representation of the segment (<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#create-a-segmentation-from-a-labelmap-volume-and-display-in-3d" rel="noopener nofollow ugc">like this</a>), you need change the storage of 3D models to stl (<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#change-default-output-file-type-for-new-nodes" rel="noopener nofollow ugc">like this</a>), then you need to export segments as models (like <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-model-nodes-from-segmentation-node" rel="noopener nofollow ugc">this</a>), then you can save your model as .stl maybe like this:<br>
<code>slicer.util.saveNode(modelNode, filepath)</code></p>
<p>I haven’t tested this workflow, but I think it should work</p>

---
