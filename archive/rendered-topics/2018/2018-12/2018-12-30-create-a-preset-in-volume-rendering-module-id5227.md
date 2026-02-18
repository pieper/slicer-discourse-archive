# Create a preset in volume rendering module

**Topic ID**: 5227
**Date**: 2018-12-30
**URL**: https://discourse.slicer.org/t/create-a-preset-in-volume-rendering-module/5227

---

## Post #1 by @maxaerosat.co.za (2018-12-30 14:02 UTC)

<p>Just started on slicer and manage to do volume rendering of data<br>
I would like to have an additional preset(s} to be created and available<br>
with all the colours set to white and shading set “off”<br>
that will make it easier to color the images in my liking in my next step<br>
How do i do it  / can it be built</p>

---

## Post #2 by @lassoan (2018-12-30 14:09 UTC)

<p>See instructions here:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/VolumeRendering#How_to_register_custom_volume_rendering_presets" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/VolumeRendering#How_to_register_custom_volume_rendering_presets</a></p>
<p>You can add the script to your <em>.slicerrc</em> file or do it in the startup of a scripted module.</p>

---

## Post #3 by @maxaerosat.co.za (2018-12-30 17:37 UTC)

<p>Thank you verry mutch</p>
<p>Will try it immediately once i get to my office in the morning</p>
<p>greatly appreciated</p>
<p>slicer is great</p>

---

## Post #4 by @maxaerosat.co.za (2018-12-30 21:58 UTC)

<p>Thanks : not as easy as i thought it will be</p>
<p>tried to follow the example to the letter with appropriate modifications</p>
<p>running Linux (Fedora )</p>
<p>strange could not find an .slicerrc file anywhere</p>
<p>so i experimented …</p>
<p>created one in my slicer directory</p>
<p>when that did not work made one in my home directory</p>
<p>… and when that did not work</p>
<p>made one in my  /  directory</p>
<p>with the code ( modified )</p>
<pre><code class="lang-auto">
presetsScenePath = "/home/maxwell/slicer.mypresets/MyPresets.mrml"
# Read presets scene
customPresetsScene = slicer.vtkMRMLScene()
vrPropNode = slicer.vtkMRMLVolumePropertyNode()
customPresetsScene.RegisterNodeClass(vrPropNode)
customPresetsScene.SetURL("/home/maxwell/slicer/mypresets/MyPresets.mrml")

##** slicer is in "/home/maxwell/slicer" directory and the presets are in a /home/maxwell/slicer/mypresets/" directory customPresetsScene.Connect()
# Add presets to volume rendering logic
vrLogic = slicer.modules.volumerendering.logic()
presetsScene = vrLogic.GetPresetsScene()
vrNodes = customPresetsScene.GetNodesByClass("vtkMRMLVolumePropertyNode")
vrNodes.UnRegister(None)
for itemNum in range(vrNodes.GetNumberOfItems()):
node = vrNodes.GetItemAsObject(itemNum)
vrLogic.AddPreset(node)
</code></pre>
<p>did not have the desired outcome</p>
<p>something is not right</p>
<p>or more simple</p>
<p>how do i run / load the code as per page instructions</p>
<p>hopefully will still have the baseline presets available to use</p>
<p>Greatly appreciated</p>

---

## Post #5 by @lassoan (2018-12-31 02:04 UTC)

<aside class="quote no-group" data-username="maxaerosat.co.za" data-post="4" data-topic="5227">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/8797f3/48.png" class="avatar"> maxaerosat.co.za:</div>
<blockquote>
<p>did not have the desired outcome<br>
something is not right</p>
</blockquote>
</aside>
<p>We would be happy to help, but we need much better error reports than this.</p>
<aside class="quote no-group" data-username="maxaerosat.co.za" data-post="4" data-topic="5227">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/8797f3/48.png" class="avatar"> maxaerosat.co.za:</div>
<blockquote>
<p>strange could not find an .slicerrc file anywhere<br>
so i experimented …</p>
</blockquote>
</aside>
<p>You may also just use Google. Since all Slicer discussions, supports requests, and documentation are indexed, you should be able to find answers to many questions. If you Google slicerrc then this link comes up on the first page:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_to_systematically_execute_custom_python_code_at_startup_.3F" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_to_systematically_execute_custom_python_code_at_startup_.3F</a></p>

---

## Post #6 by @maxaerosat.co.za (2021-06-17 17:36 UTC)

<p>Thank you .<br>
Actully the directions you gave me works perfectly . And can add presets  - or more accurately managed to load predefined presets in a session without to restart slicer  - thanks .</p>
<p>problem now :i am able to remove the preset in the slicer session ( to edit and reload ) but the icon does not disappear from the drop down menu - so if i reload the preset file it just get added to the icons . need to remove the icons from the list of icons also . can see that the removed icon has functionally been removed , as when i use it - end up with a black screen  3d rendering screen<br>
code i used<br>
node = vrNodes.GetItemAsObject(0);print(node);vrLogic.RemovePreset(node)<br>
=&gt; need the icon to be removed from the drop down menu also in same session</p>

---

## Post #7 by @lassoan (2021-06-18 04:08 UTC)

<p>You can remove a volume rendering preset like this:</p>
<pre><code class="lang-python">vrLogic.RemovePreset(vrLogic.GetPresetByName('MyPreset1'))
</code></pre>

---

## Post #8 by @Juergen (2023-10-26 23:47 UTC)

<p>Hi Andras,<br>
How can I remove the default presets. I never use them but they take up a lot of screen space. As an alternative I would like to replace all the presets with my own preset only.<br>
Thanks, Juergen</p>

---
