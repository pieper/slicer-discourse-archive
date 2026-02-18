# Can customized layouts, such as 5 by 4, be possible?

**Topic ID**: 26816
**Date**: 2022-12-19
**URL**: https://discourse.slicer.org/t/can-customized-layouts-such-as-5-by-4-be-possible/26816

---

## Post #1 by @Jinhee_Jang (2022-12-19 04:55 UTC)

<p>Hi!, I am using slicer as an end-user for a while and I like it.<br>
The reason why I am using slicer is that I could see many nifti files at once, and I could save the entire working environment.<br>
By the way, as increasing the numbers of images I browse, I need customized layout such as 5 b 4 or more.<br>
On GUI, 4 by 3 looks maximum.<br>
Is there any way to customize this?<br>
Thank you for your time!</p>

---

## Post #2 by @lassoan (2022-12-19 16:24 UTC)

<p>You can choose any number and types of views in any arrangement by specifying a simple XML string. See example and some more information in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-view-layout">script repository</a>. If you need any further clarifications then let us know.</p>

---

## Post #3 by @pieper (2022-12-19 17:51 UTC)

<p>You may also want to try the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/CompareVolumes">Compare Volumes</a> module, which will generate a layout based on selected volumes and also let you pick a reference volume to superimpose on all for crossfading and a few other features.</p>

---

## Post #4 by @Jinhee_Jang (2022-12-20 02:16 UTC)

<p>Thank you for your reply.</p>
<p>I tried two sugestions.</p>
<p>I made custom layout for 4 by 5 as follows, but it doesn’t work.</p>
<pre><code class="lang-auto">customLayout = """
  &lt;layout type=\vertical\&gt;
   &lt;item&gt;
    &lt;layout type=\horizontal\&gt;
     &lt;item&gt;
      &lt;view class=\vtkMRMLSliceNode\ singletontag=\Red\&gt;
       &lt;property name=\orientation\ action=\default\&gt;Axial&lt;/property&gt;
       &lt;property name=\viewlabel\ action=\default\&gt;R&lt;/property&gt;
       &lt;property name=\viewcolor\ action=\default\&gt;#F34A33&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;
     &lt;item&gt;
      &lt;view class=\vtkMRMLSliceNode\ singletontag=\Yellow\&gt;
       &lt;property name=\orientation\ action=\default\&gt;Axial&lt;/property&gt;
       &lt;property name=\viewlabel\ action=\default\&gt;Y&lt;/property&gt;
       &lt;property name=\viewcolor\ action=\default\&gt;#EDD54C&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;
     &lt;item&gt;
      &lt;view class=\vtkMRMLSliceNode\ singletontag=\Green\&gt;
       &lt;property name=\orientation\ action=\default\&gt;Axial&lt;/property&gt;
       &lt;property name=\viewlabel\ action=\default\&gt;G&lt;/property&gt;
       &lt;property name=\viewcolor\ action=\default\&gt;#6EB04B&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;
     &lt;item&gt;
      &lt;view class=\vtkMRMLSliceNode\ singletontag=\Slice4\&gt;
       &lt;property name=\orientation\ action=\default\&gt;Axial&lt;/property&gt;
       &lt;property name=\viewlabel\ action=\default\&gt;4&lt;/property&gt;
       &lt;property name=\viewcolor\ action=\default\&gt;#8C8C8C&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;
     &lt;item&gt;
      &lt;view class=\vtkMRMLSliceNode\ singletontag=\Slice5\&gt;
       &lt;property name=\orientation\ action=\default\&gt;Axial&lt;/property&gt;
       &lt;property name=\viewlabel\ action=\default\&gt;5&lt;/property&gt;
       &lt;property name=\viewcolor\ action=\default\&gt;#8C8C8C&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;
    &lt;/layout&gt;
   &lt;/item&gt;
   &lt;item&gt;
    &lt;layout type=\horizontal\&gt;
     &lt;item&gt;
      &lt;view class=\vtkMRMLSliceNode\ singletontag=\Slice6\&gt;
       &lt;property name=\orientation\ action=\default\&gt;Axial&lt;/property&gt;
       &lt;property name=\viewlabel\ action=\default\&gt;6&lt;/property&gt;
       &lt;property name=\viewcolor\ action=\default\&gt;#8C8C8C&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;
     &lt;item&gt;
      &lt;view class=\vtkMRMLSliceNode\ singletontag=\Slice7\&gt;
       &lt;property name=\orientation\ action=\default\&gt;Axial&lt;/property&gt;
       &lt;property name=\viewlabel\ action=\default\&gt;7&lt;/property&gt;
       &lt;property name=\viewcolor\ action=\default\&gt;#8C8C8C&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;
     &lt;item&gt;
      &lt;view class=\vtkMRMLSliceNode\ singletontag=\Slice8\&gt;
       &lt;property name=\orientation\ action=\default\&gt;Axial&lt;/property&gt;
       &lt;property name=\viewlabel\ action=\default\&gt;8&lt;/property&gt;
       &lt;property name=\viewcolor\ action=\default\&gt;#8C8C8C&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;
     &lt;item&gt;
      &lt;view class=\vtkMRMLSliceNode\ singletontag=\Slice9\&gt;
       &lt;property name=\orientation\ action=\default\&gt;Axial&lt;/property&gt;
       &lt;property name=\viewlabel\ action=\default\&gt;9&lt;/property&gt;
       &lt;property name=\viewcolor\ action=\default\&gt;#8C8C8C&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;
     &lt;item&gt;
      &lt;view class=\vtkMRMLSliceNode\ singletontag=\Slice10\&gt;
       &lt;property name=\orientation\ action=\default\&gt;Axial&lt;/property&gt;
       &lt;property name=\viewlabel\ action=\default\&gt;10&lt;/property&gt;
       &lt;property name=\viewcolor\ action=\default\&gt;#8C8C8C&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;
    &lt;/layout&gt;
   &lt;/item&gt;
   &lt;item&gt;
    &lt;layout type=\horizontal\&gt;
     &lt;item&gt;
      &lt;view class=\vtkMRMLSliceNode\ singletontag=\Slice11\&gt;
       &lt;property name=\orientation\ action=\default\&gt;Axial&lt;/property&gt;
       &lt;property name=\viewlabel\ action=\default\&gt;11&lt;/property&gt;
       &lt;property name=\viewcolor\ action=\default\&gt;#8C8C8C&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;
     &lt;item&gt;
      &lt;view class=\vtkMRMLSliceNode\ singletontag=\Slice12\&gt;
       &lt;property name=\orientation\ action=\default\&gt;Axial&lt;/property&gt;
       &lt;property name=\viewlabel\ action=\default\&gt;12&lt;/property&gt;
       &lt;property name=\viewcolor\ action=\default\&gt;#8C8C8C&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;
     &lt;item&gt;
      &lt;view class=\vtkMRMLSliceNode\ singletontag=\Slice13\&gt;
       &lt;property name=\orientation\ action=\default\&gt;Axial&lt;/property&gt;
       &lt;property name=\viewlabel\ action=\default\&gt;13&lt;/property&gt;
       &lt;property name=\viewcolor\ action=\default\&gt;#8C8C8C&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;
     &lt;item&gt;
      &lt;view class=\vtkMRMLSliceNode\ singletontag=\Slice14\&gt;
       &lt;property name=\orientation\ action=\default\&gt;Axial&lt;/property&gt;
       &lt;property name=\viewlabel\ action=\default\&gt;14&lt;/property&gt;
       &lt;property name=\viewcolor\ action=\default\&gt;#8C8C8C&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;
     &lt;item&gt;
      &lt;view class=\vtkMRMLSliceNode\ singletontag=\Slice15\&gt;
       &lt;property name=\orientation\ action=\default\&gt;Axial&lt;/property&gt;
       &lt;property name=\viewlabel\ action=\default\&gt;15&lt;/property&gt;
       &lt;property name=\viewcolor\ action=\default\&gt;#8C8C8C&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;   
    &lt;/layout&gt;
   &lt;/item&gt;
   &lt;item&gt;
    &lt;layout type=\horizontal\&gt;
     &lt;item&gt;
      &lt;view class=\vtkMRMLSliceNode\ singletontag=\Slice16\&gt;
       &lt;property name=\orientation\ action=\default\&gt;Axial&lt;/property&gt;
       &lt;property name=\viewlabel\ action=\default\&gt;16&lt;/property&gt;
       &lt;property name=\viewcolor\ action=\default\&gt;#8C8C8C&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;
     &lt;item&gt;
      &lt;view class=\vtkMRMLSliceNode\ singletontag=\Slice17\&gt;
       &lt;property name=\orientation\ action=\default\&gt;Axial&lt;/property&gt;
       &lt;property name=\viewlabel\ action=\default\&gt;17&lt;/property&gt;
       &lt;property name=\viewcolor\ action=\default\&gt;#8C8C8C&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;
     &lt;item&gt;
      &lt;view class=\vtkMRMLSliceNode\ singletontag=\Slice18\&gt;
       &lt;property name=\orientation\ action=\default\&gt;Axial&lt;/property&gt;
       &lt;property name=\viewlabel\ action=\default\&gt;18&lt;/property&gt;
       &lt;property name=\viewcolor\ action=\default\&gt;#8C8C8C&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;
     &lt;item&gt;
      &lt;view class=\vtkMRMLSliceNode\ singletontag=\Slice19\&gt;
       &lt;property name=\orientation\ action=\default\&gt;Axial&lt;/property&gt;
       &lt;property name=\viewlabel\ action=\default\&gt;19&lt;/property&gt;
       &lt;property name=\viewcolor\ action=\default\&gt;#8C8C8C&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;
     &lt;item&gt;
      &lt;view class=\vtkMRMLSliceNode\ singletontag=\Slice20\&gt;
       &lt;property name=\orientation\ action=\default\&gt;Axial&lt;/property&gt;
       &lt;property name=\viewlabel\ action=\default\&gt;20&lt;/property&gt;
       &lt;property name=\viewcolor\ action=\default\&gt;#8C8C8C&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;   
    &lt;/layout&gt;
   &lt;/item&gt;  
  &lt;/layout&gt;
  """


customLayoutId=501

layoutManager = slicer.app.layoutManager()
layoutManager.layoutLogic().GetLayoutNode().AddLayoutDescription(customLayoutId, customLayout)

layoutManager.setLayout(customLayoutId)
</code></pre>
<p>It just gone blank and I cannot see any images.</p>
<p>The second one works as I expected when I tried 4 by 4 layout.</p>
<p>When I tried 5 by 4, layout become 3 by 7 iIt is little bit awkward but I can browse all 20 images at the same time.</p>
<p>Thank you again!</p>

---

## Post #5 by @lassoan (2022-12-20 05:46 UTC)

<p>It’s all good, just use <code>"</code> instead of <code>\</code> character, as shown in the example in the script repository. This is the correct code for the 5x4 layout:</p>
<pre><code class="lang-python">customLayout = """
  &lt;layout type="vertical"&gt;
   &lt;item&gt;
    &lt;layout type="horizontal"&gt;
     &lt;item&gt;
      &lt;view class="vtkMRMLSliceNode" singletontag="Red"&gt;
       &lt;property name="orientation" action="default"&gt;Axial&lt;/property&gt;
       &lt;property name="viewlabel" action="default"&gt;R&lt;/property&gt;
       &lt;property name="viewcolor" action="default"&gt;#F34A33&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;
     &lt;item&gt;
      &lt;view class="vtkMRMLSliceNode" singletontag="Yellow"&gt;
       &lt;property name="orientation" action="default"&gt;Axial&lt;/property&gt;
       &lt;property name="viewlabel" action="default"&gt;Y&lt;/property&gt;
       &lt;property name="viewcolor" action="default"&gt;#EDD54C&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;
     &lt;item&gt;
      &lt;view class="vtkMRMLSliceNode" singletontag="Green"&gt;
       &lt;property name="orientation" action="default"&gt;Axial&lt;/property&gt;
       &lt;property name="viewlabel" action="default"&gt;G&lt;/property&gt;
       &lt;property name="viewcolor" action="default"&gt;#6EB04B&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;
     &lt;item&gt;
      &lt;view class="vtkMRMLSliceNode" singletontag="Slice4"&gt;
       &lt;property name="orientation" action="default"&gt;Axial&lt;/property&gt;
       &lt;property name="viewlabel" action="default"&gt;4&lt;/property&gt;
       &lt;property name="viewcolor" action="default"&gt;#8C8C8C&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;
     &lt;item&gt;
      &lt;view class="vtkMRMLSliceNode" singletontag="Slice5"&gt;
       &lt;property name="orientation" action="default"&gt;Axial&lt;/property&gt;
       &lt;property name="viewlabel" action="default"&gt;5&lt;/property&gt;
       &lt;property name="viewcolor" action="default"&gt;#8C8C8C&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;
    &lt;/layout&gt;
   &lt;/item&gt;
   &lt;item&gt;
    &lt;layout type="horizontal"&gt;
     &lt;item&gt;
      &lt;view class="vtkMRMLSliceNode" singletontag="Slice6"&gt;
       &lt;property name="orientation" action="default"&gt;Axial&lt;/property&gt;
       &lt;property name="viewlabel" action="default"&gt;6&lt;/property&gt;
       &lt;property name="viewcolor" action="default"&gt;#8C8C8C&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;
     &lt;item&gt;
      &lt;view class="vtkMRMLSliceNode" singletontag="Slice7"&gt;
       &lt;property name="orientation" action="default"&gt;Axial&lt;/property&gt;
       &lt;property name="viewlabel" action="default"&gt;7&lt;/property&gt;
       &lt;property name="viewcolor" action="default"&gt;#8C8C8C&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;
     &lt;item&gt;
      &lt;view class="vtkMRMLSliceNode" singletontag="Slice8"&gt;
       &lt;property name="orientation" action="default"&gt;Axial&lt;/property&gt;
       &lt;property name="viewlabel" action="default"&gt;8&lt;/property&gt;
       &lt;property name="viewcolor" action="default"&gt;#8C8C8C&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;
     &lt;item&gt;
      &lt;view class="vtkMRMLSliceNode" singletontag="Slice9"&gt;
       &lt;property name="orientation" action="default"&gt;Axial&lt;/property&gt;
       &lt;property name="viewlabel" action="default"&gt;9&lt;/property&gt;
       &lt;property name="viewcolor" action="default"&gt;#8C8C8C&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;
     &lt;item&gt;
      &lt;view class="vtkMRMLSliceNode" singletontag="Slice10"&gt;
       &lt;property name="orientation" action="default"&gt;Axial&lt;/property&gt;
       &lt;property name="viewlabel" action="default"&gt;10&lt;/property&gt;
       &lt;property name="viewcolor" action="default"&gt;#8C8C8C&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;
    &lt;/layout&gt;
   &lt;/item&gt;
   &lt;item&gt;
    &lt;layout type="horizontal"&gt;
     &lt;item&gt;
      &lt;view class="vtkMRMLSliceNode" singletontag="Slice11"&gt;
       &lt;property name="orientation" action="default"&gt;Axial&lt;/property&gt;
       &lt;property name="viewlabel" action="default"&gt;11&lt;/property&gt;
       &lt;property name="viewcolor" action="default"&gt;#8C8C8C&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;
     &lt;item&gt;
      &lt;view class="vtkMRMLSliceNode" singletontag="Slice12"&gt;
       &lt;property name="orientation" action="default"&gt;Axial&lt;/property&gt;
       &lt;property name="viewlabel" action="default"&gt;12&lt;/property&gt;
       &lt;property name="viewcolor" action="default"&gt;#8C8C8C&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;
     &lt;item&gt;
      &lt;view class="vtkMRMLSliceNode" singletontag="Slice13"&gt;
       &lt;property name="orientation" action="default"&gt;Axial&lt;/property&gt;
       &lt;property name="viewlabel" action="default"&gt;13&lt;/property&gt;
       &lt;property name="viewcolor" action="default"&gt;#8C8C8C&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;
     &lt;item&gt;
      &lt;view class="vtkMRMLSliceNode" singletontag="Slice14"&gt;
       &lt;property name="orientation" action="default"&gt;Axial&lt;/property&gt;
       &lt;property name="viewlabel" action="default"&gt;14&lt;/property&gt;
       &lt;property name="viewcolor" action="default"&gt;#8C8C8C&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;
     &lt;item&gt;
      &lt;view class="vtkMRMLSliceNode" singletontag="Slice15"&gt;
       &lt;property name="orientation" action="default"&gt;Axial&lt;/property&gt;
       &lt;property name="viewlabel" action="default"&gt;15&lt;/property&gt;
       &lt;property name="viewcolor" action="default"&gt;#8C8C8C&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;   
    &lt;/layout&gt;
   &lt;/item&gt;
   &lt;item&gt;
    &lt;layout type="horizontal"&gt;
     &lt;item&gt;
      &lt;view class="vtkMRMLSliceNode" singletontag="Slice16"&gt;
       &lt;property name="orientation" action="default"&gt;Axial&lt;/property&gt;
       &lt;property name="viewlabel" action="default"&gt;16&lt;/property&gt;
       &lt;property name="viewcolor" action="default"&gt;#8C8C8C&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;
     &lt;item&gt;
      &lt;view class="vtkMRMLSliceNode" singletontag="Slice17"&gt;
       &lt;property name="orientation" action="default"&gt;Axial&lt;/property&gt;
       &lt;property name="viewlabel" action="default"&gt;17&lt;/property&gt;
       &lt;property name="viewcolor" action="default"&gt;#8C8C8C&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;
     &lt;item&gt;
      &lt;view class="vtkMRMLSliceNode" singletontag="Slice18"&gt;
       &lt;property name="orientation" action="default"&gt;Axial&lt;/property&gt;
       &lt;property name="viewlabel" action="default"&gt;18&lt;/property&gt;
       &lt;property name="viewcolor" action="default"&gt;#8C8C8C&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;
     &lt;item&gt;
      &lt;view class="vtkMRMLSliceNode" singletontag="Slice19"&gt;
       &lt;property name="orientation" action="default"&gt;Axial&lt;/property&gt;
       &lt;property name="viewlabel" action="default"&gt;19&lt;/property&gt;
       &lt;property name="viewcolor" action="default"&gt;#8C8C8C&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;
     &lt;item&gt;
      &lt;view class="vtkMRMLSliceNode" singletontag="Slice20"&gt;
       &lt;property name="orientation" action="default"&gt;Axial&lt;/property&gt;
       &lt;property name="viewlabel" action="default"&gt;20&lt;/property&gt;
       &lt;property name="viewcolor" action="default"&gt;#8C8C8C&lt;/property&gt;
      &lt;/view&gt;
     &lt;/item&gt;   
    &lt;/layout&gt;
   &lt;/item&gt;  
  &lt;/layout&gt;
  """


customLayoutId=502

layoutManager = slicer.app.layoutManager()
layoutManager.layoutLogic().GetLayoutNode().AddLayoutDescription(customLayoutId, customLayout)

layoutManager.setLayout(customLayoutId)
</code></pre>
<p>Note that having 20 viewers requires considerable resources. If you just want to have a static lightbox view of many slices of the same volume then you can generate it using <code>Screen Capture</code> module (choose <code>Output type</code> → <code>lightbox image</code>).</p>

---

## Post #6 by @Jinhee_Jang (2022-12-20 05:50 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Thank you for your kind help, and it works!<br>
I used the python command in slicer for the first time. It is interesting and useful.<br>
Thank you again!</p>

---
