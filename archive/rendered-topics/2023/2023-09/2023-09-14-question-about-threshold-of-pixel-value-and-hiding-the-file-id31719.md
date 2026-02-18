# Question about threshold of pixel value and hiding the file name while saving 

**Topic ID**: 31719
**Date**: 2023-09-14
**URL**: https://discourse.slicer.org/t/question-about-threshold-of-pixel-value-and-hiding-the-file-name-while-saving/31719

---

## Post #1 by @jp_jp_jp (2023-09-14 15:51 UTC)

<p>Hi, I have a picture like this<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a6a9f41d384b02d22a346b4df2b21675eaa3797.jpeg" alt="image" data-base62-sha1="fbp312TLDWi0K9y048ngzDZt1wb" width="638" height="447"></p>
<ol>
<li>From the view of the value of the pixel, there are some places that look white, and they should have a higher pixel value, so my question is how to set a threshold value so that those parts can be hidden.</li>
<li>Now I am using annotation screenshot to save as jpg, how to hide the white file name at left bottom, and is there any way to save high dpi pictures?</li>
<li>How to only show the green line in this figure, they are intersection lines</li>
</ol>
<p>Thank you!</p>

---

## Post #2 by @muratmaga (2023-09-14 16:01 UTC)

<p>Under the volumes module, if you scroll down to the threshold tab, you can control what’s being displayed in the slice view.</p>
<p>I am not sure it is possible to volume name not to be displayed in the slice view. You might have to edit that after the capture.</p>

---

## Post #4 by @jp_jp_jp (2023-09-14 16:06 UTC)

<p>Thanks! It can be hidden using a right click, configure slice view with annotanation…<br>
do you know how to only show the green line? Thanks!</p>

---

## Post #5 by @mikebind (2023-09-14 17:44 UTC)

<p>If you create a custom layout with only the red slice and green slice (no yellow slice in the layout), and then turn on slice intersections, only the green line should show up. Here is some example code from the script repository showing how to create and use a custom layout: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-view-layout" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a></p>

---

## Post #6 by @Sunderlandkyl (2023-09-14 19:37 UTC)

<aside class="quote no-group" data-username="jp_jp_jp" data-post="1" data-topic="31719">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/c77e96/48.png" class="avatar"> jp_jp_jp:</div>
<blockquote>
<p>Now I am using annotation screenshot to save as jpg, how to hide the white file name at left bottom, and is there any way to save high dpi pictures?</p>
</blockquote>
</aside>
<p>To hide the text, you can go to the DataProbe module and uncheck the active corners:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/6638ba219dfa1ac287a9fb03921247cee4ff3e4e.png" alt="image" data-base62-sha1="eAiePqlIKaW1TJFteUyZIWdlcfk" width="520" height="152"></p>

---

## Post #7 by @jp_jp_jp (2023-09-14 21:54 UTC)

<p>Hi, is there a way to do the custom layout using GUI?</p>

---

## Post #8 by @mikebind (2023-09-14 22:16 UTC)

<p>I don’t believe so, but you could paste the below code (which is just a slightly modified version of the code from the repository) into the python interactor to achieve this.</p>
<pre><code class="lang-auto">customLayout = """
&lt;layout type="horizontal" split="true"&gt;
  &lt;item&gt;
  &lt;view class="vtkMRMLSliceNode" singletontag="Red"&gt;
    &lt;property name="orientation" action="default"&gt;Axial&lt;/property&gt;
    &lt;property name="viewlabel" action="default"&gt;R&lt;/property&gt;
    &lt;property name="viewcolor" action="default"&gt;#F34A33&lt;/property&gt;
  &lt;/view&gt;
  &lt;/item&gt;
&lt;item&gt;
  &lt;view class=\"vtkMRMLSliceNode\" singletontag=\"Green\"&gt;
   &lt;property name=\"orientation\" action=\"default\"&gt;Coronal&lt;/property&gt;
   &lt;property name=\"viewlabel\" action=\"default\"&gt;G&lt;/property&gt;
   &lt;property name=\"viewcolor\" action=\"default\"&gt;#6EB04B&lt;/property&gt;
  &lt;/view&gt;
&lt;/item&gt;
&lt;/layout&gt;
"""

# Built-in layout IDs are all below 100, so you can choose any large random number
# for your custom layout ID.
customLayoutId=511

layoutManager = slicer.app.layoutManager()
layoutManager.layoutLogic().GetLayoutNode().AddLayoutDescription(customLayoutId, customLayout)

# Switch to the new custom layout
layoutManager.setLayout(customLayoutId)
</code></pre>

---
