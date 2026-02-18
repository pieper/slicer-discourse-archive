# Example Jupyter notebook not compatible with slicer 5.6

**Topic ID**: 35121
**Date**: 2024-03-27
**URL**: https://discourse.slicer.org/t/example-jupyter-notebook-not-compatible-with-slicer-5-6/35121

---

## Post #1 by @Matteboo (2024-03-27 10:07 UTC)

<p>Hello,<br>
I started to learn how to use slicer from Jupyter. I’ve used the example notebook provided here <a href="https://github.com/Slicer/SlicerNotebooks" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Slicer/SlicerNotebooks: Examples that illustrate how to use 3D Slicer via Jupyter notebooks in Python</a></p>
<p>However, some cells don’t work on my installation. For example, in the notebook 1.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a7fcd4335a402227fb783bde1e8267c1f8f1373.png" alt="image" data-base62-sha1="3Mqe9JN2VXFW9f37I3QUDQHNag3" width="597" height="397"><br>
I also get this error</p>
<blockquote>
<hr>
<p>AttributeError                            Traceback (most recent call last)<br>
File ~\AppData\Local\slicer.org\Slicer 5.6.0\lib\Python\Lib\site-packages\ipywidgets\widgets\interaction.py:240, in interactive.update(self, *args)<br>
238     value = widget.get_interact_value()<br>
239     self.kwargs[widget._kwarg] = value<br>
 → 240 self.result = self.f(**self.kwargs)<br>
241 show_inline_matplotlib_plots()<br>
242 if self.auto_display and self.result is not None:</p>
<p>Cell In[7], line 15, in update(roll, pitch, yaw, cropx, cropy, cropz)<br>
11 <span class="mention">@interact</span>(roll=(-90.0,90.0,5), pitch=(-90.0,90.0,5), yaw=(-180.0,180.0,5), cropx=(0,140,5), cropy=(0,240,5), cropz=(0,160,5))<br>
12 def update(roll=0, pitch=-10, yaw=30, cropx=140, cropy=240, cropz=160):<br>
13     <span class="hashtag-raw">#roiNode</span>.SetRadiusXYZ([cropx, cropy, cropz])<br>
14     roiNode.SetSizeWorld([cropx, cropy, cropz])<br>
—&gt; 15     return slicernb.View3DDisplay(0, orientation=[roll, pitch, yaw])</p>
<p>File ~\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerJupyter\lib\Slicer-5.6\qt-scripted-modules\JupyterNotebooksLib\display.py:218, in View3DDisplay.<strong>init</strong>(self, viewID, orientation)<br>
216 view = widget.threeDView()<br>
217 if orientation is not None:<br>
 → 218   camera = view.interactorStyle().GetCameraNode().GetCamera()<br>
219   cameraToWorld = vtk.vtkTransform()<br>
220   cameraToWorld.RotateX(90)</p>
<p>AttributeError: ‘vtkmodules.vtkRenderingCore.vtkInteractorStyle3D’ object has no attribute ‘GetCameraNode’</p>
</blockquote>
<p>The notebook 3 runs smoothly.<br>
I think it’s a version compatibility version because I couldn’t find anny other difference with the online version (that runs without error on slicer 5.0)</p>

---

## Post #2 by @Matteboo (2024-03-27 13:13 UTC)

<p>After some additionnal research, I think that the issue might come from my ipywidget that’s not enabled when I select slicer as a kernel in my notebook</p>
<p>I found this topic from several years ago but I have the same  as just_zzzzzz</p><aside class="quote" data-post="1" data-topic="11913">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vinny/48/7052_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/ipywidgets-and-slicerjupyter/11913">Ipywidgets and SlicerJupyter</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi, 
I downloaded the tutorial sets for SlicerJupyter and noticed that the interactive widgets were not showing up.  I had to enable them using: 
jupyter nbextension enable --py widgetsnbextension 
I want to make sure that I did not miss something in the installation instructions using Option 2 (note that I did not run the additional commands for Jupyter lab): <a href="https://github.com/Slicer/SlicerJupyter/blob/master/README.md#setup" rel="noopener nofollow ugc">https://github.com/Slicer/SlicerJupyter/blob/master/README.md#setup</a> 
Thanks, 
Vinny
  </blockquote>
</aside>


---
