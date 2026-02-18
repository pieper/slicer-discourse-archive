# User-friendlyness

**Topic ID**: 32334
**Date**: 2023-10-20
**URL**: https://discourse.slicer.org/t/user-friendlyness/32334

---

## Post #1 by @Melodicpinpon (2023-10-20 09:05 UTC)

<p>These are positive propositions aiming to make the software more intuitive:</p>
<p>1-Keeping the outliner visible in every module and allowing to do operations on the chosen volume/model/etc<br>
2-Displaying only the values that matter in the ‘Transforms’ module. (Slice thickness is lost between 11 other values).<br>
3-Saving all the data in a single scene/file. Recovering a scene is a real struggle.</p>

---

## Post #2 by @Deep_Learning (2023-10-20 15:21 UTC)

<p><span class="hashtag-raw">#1</span> do not understand<br>
<span class="hashtag-raw">#2</span> do not use transforms, but slicer does a lot…</p>
<p><span class="hashtag-raw">#3</span> save as .mrb</p>

---

## Post #3 by @lassoan (2023-10-20 19:15 UTC)

<p><a class="mention" href="/u/deep_learning">@Deep_Learning</a> addressed the last request. For the first two:</p>
<aside class="quote no-group" data-username="Melodicpinpon" data-post="1" data-topic="32334">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/melodicpinpon/48/3254_2.png" class="avatar"> Melodicpinpon:</div>
<blockquote>
<p>1-Keeping the outliner visible in every module and allowing to do operations on the chosen volume/model/etc</p>
</blockquote>
</aside>
<p>We can certainly try this. It should not take more than a 5-10 lines of code. Would you like to give it a try? To get started, you can ask Bing Chat or ChatGPT to “write Python code for 3D Slicer that displays subject hierarchy widget in a dockable widget”.</p>
<p>Actually, I’ve done this just to test and got perfectly working code using Bing Chat in 5 minutes, without need to actually write any code my self. First I got a code snippet that threw an error, but then told bing that I got an error and copied the error message; and it told which single line to change; I’ve changed that and it works perfectly now.</p>
<pre data-code-wrap="python"><code class="lang-python"># Create a new dockable widget
dockWidget = qt.QDockWidget()
dockWidget.setWindowTitle("Subject hierarchy")

# Create a subject hierarchy widget
shWidget = slicer.qMRMLSubjectHierarchyTreeView()
shWidget.setMRMLScene(slicer.mrmlScene)

# Add the subject hierarchy widget to the dockable widget
dockWidget.setWidget(shWidget)

# Add the dockable widget to the main window
slicer.util.mainWindow().addDockWidget(qt.Qt.RightDockWidgetArea, dockWidget)
</code></pre>
<aside class="quote no-group" data-username="Melodicpinpon" data-post="1" data-topic="32334">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/melodicpinpon/48/3254_2.png" class="avatar"> Melodicpinpon:</div>
<blockquote>
<p>Displaying only the values that matter in the ‘Transforms’ module. (Slice thickness is lost between 11 other values).</p>
</blockquote>
</aside>
<p>Slicer does don’t deal with slice thickness but only uses spacing between slices. I assume you mean image spacing. If you want to change the spacing in a volume then I would not use transforms module for it, but import the image stack using a much more convenient, robust, faster method: using <em>Image Stacks</em> module (in SlicerMorph extension).</p>
<p>It is slow, inconvenient, and error prone to store 3D images in series of 2D image files. I know that Morphosource and other databases still do it and so it is not going to change anytime soon. However, you can improve your workflows: once you imported the image stack, save into a proper 3D format, such as NRRD. Then you can quickly and easily load the file later. I would recommend to disable compression if you work with large images, because using 50% less disk space may not worth the 10x longer loading time.</p>

---
