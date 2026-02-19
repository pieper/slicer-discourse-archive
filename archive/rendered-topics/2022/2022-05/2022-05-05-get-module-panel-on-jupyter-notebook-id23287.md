---
topic_id: 23287
title: "Get Module Panel On Jupyter Notebook"
date: 2022-05-05
url: https://discourse.slicer.org/t/23287
---

# Get Module Panel on Jupyter Notebook

**Topic ID**: 23287
**Date**: 2022-05-05
**URL**: https://discourse.slicer.org/t/get-module-panel-on-jupyter-notebook/23287

---

## Post #1 by @Tiago_Guiomar (2022-05-05 13:27 UTC)

<p>I’m doing a small project using 3DSlicer and jupyter notebook and I needed some help with the GUI. I’m using some script I got and it ain’t work. I was wondering if there’s any way I get all the GUI on jupyter notebook so I can segment inside the notebook and not having to go to 3DSlicer to do the segmentation.</p>
<p>I have this code:</p>
<pre><code class="lang-auto"># Only available if jupyter desktop server is configured.
# "404 : Not Found" error is displayed if Jupyter desktop server is not configured,
# in that case, switch to the application window if Slicer is running locally.
app = slicernb.AppWindow(contents="full", windowScale=1)

slicer.util.selectModule("SegmentEditor")
segmentEditorWidget = slicer.modules.segmenteditor.widgetRepresentation().self().editor
segmentEditorNode = segmentEditorWidget.mrmlSegmentEditorNode()
segmentationNode=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setMasterVolumeNode(volumeNode)


display(app)
</code></pre>

---

## Post #2 by @Tiago_Guiomar (2022-05-05 13:30 UTC)

<p>I was assuming (contents=“full”) would solve it but it just opens a new slicer tab and won’t run on my notebook.</p>

---

## Post #3 by @lassoan (2022-05-06 01:06 UTC)

<p>Do you use the <a href="https://github.com/Slicer/SlicerDocker/blob/master/README.rst#usage-of-slicer-notebook-image">slicer-notebook docker image</a> or you just run Slicer directly on your computer?</p>

---

## Post #4 by @Tiago_Guiomar (2022-05-10 13:37 UTC)

<p>I just use it on my computer</p>

---

## Post #5 by @lassoan (2022-05-10 23:16 UTC)

<p><code>slicernb.AppWindow</code> offers GUI access to the Slicer application when Slicer runs on a remote server or within a docker container. If you run Slicer locally then remote desktop access is not necessary but you can just split your screen between the notebook and Slicer. You can still include views into your notebook various ways - see all the other examples above <code>AppWindow</code> examples.</p>

---

## Post #6 by @Tiago_Guiomar (2022-05-11 12:00 UTC)

<p>I would like to do the segmentation inside the notebook and not having to go to slicer, just to make it faster and all in one place,<br>
I’ll check slicernb.AppWindow.<br>
Thank you.</p>

---

## Post #7 by @Tiago_Guiomar (2022-05-11 15:54 UTC)

<p>I’ve been searching all around and I can’t find any documentation on <code>slicernb.AppWindow</code>. Where can I find it?</p>

---

## Post #8 by @lassoan (2022-05-11 20:03 UTC)

<p><code>JupyterNotebooksLib</code> is a tiny set of convenience classes. We haven’t set up a readthedocs site for it,. You can type the classname and press Shift-Tab for documentation:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd5303ad683db7a94dab15e521096945ecfdb839.png" data-download-href="/uploads/short-url/r0Q69YTViY080paBOjYwX0J9xXz.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd5303ad683db7a94dab15e521096945ecfdb839_2_645x500.png" alt="image" data-base62-sha1="r0Q69YTViY080paBOjYwX0J9xXz" width="645" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd5303ad683db7a94dab15e521096945ecfdb839_2_645x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd5303ad683db7a94dab15e521096945ecfdb839_2_967x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd5303ad683db7a94dab15e521096945ecfdb839_2_1290x1000.png 2x" data-dominant-color="ECEDED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1493×1157 125 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can also browse the documented source code here: <a href="https://github.com/Slicer/SlicerJupyter/blob/master/JupyterNotebooks/JupyterNotebooksLib/widgets.py#L145" class="inline-onebox">SlicerJupyter/JupyterNotebooks/JupyterNotebooksLib/widgets.py at master · Slicer/SlicerJupyter · GitHub</a></p>
<p>If anything is not clear or incomplete then feel free to ask here. If you figure out something or your questions are answered then it would be great if you could send pull requests with your suggested changes to the documentation.</p>

---

## Post #9 by @Tiago_Guiomar (2022-05-12 14:20 UTC)

<p>Thank you for the information, really helped me out. I just have one more question, how can I setup my jupyter desktop server? I’m doing this project with a professor, he never heard about this and we can’t seem to find a solution.</p>

---

## Post #10 by @lassoan (2022-06-13 14:14 UTC)

<p>The simplest way to get <code>slicernb.AppWindow</code> command to work is to run Slicer in a docker container.</p>

---
