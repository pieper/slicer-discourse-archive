# Issue hiding shapeNodes in a folder via script

**Topic ID**: 44023
**Date**: 2025-08-08
**URL**: https://discourse.slicer.org/t/issue-hiding-shapenodes-in-a-folder-via-script/44023

---

## Post #1 by @bserrano (2025-08-08 13:16 UTC)

<p>Hi all,</p>
<p>I’m working with a script that generates several shape nodes, grouped inside a folder.</p>
<p>At a certain point in the execution, I want to hide all <strong>cylinders</strong> in that folder. I’m using the same code that works fine with other folders, but in this particular case, the cylinders remain with <code>visibility=True</code>.</p>
<p>Interestingly, if I copy and paste those exact same lines into the Python interactor, they work as expected.</p>
<p>Has anyone experienced something similar or knows what might be causing this behavior?</p>
<p>I’m using Slicer 5.6.2</p>
<p>Thanks in advance!</p>
<pre data-code-wrap="python"><code class="lang-python">    # Hide cylinders ------------------------------------------------------
    slicer.app.processEvents() 
    shNode = slicer.mrmlScene.GetSubjectHierarchyNode()
    sceneItemID = shNode.GetSceneItemID()
    folderCylID = shNode.GetItemChildWithName(sceneItemID, "Cylinders_Trim")
    shNode.SetItemDisplayVisibility(folderCylID, False)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/226d632a86f8ebdd7bef113669a1e7d4a8505ade.png" data-download-href="/uploads/short-url/4UyAUwu6aAaWfspagGUasAkxwnk.png?dl=1" title="imagen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/226d632a86f8ebdd7bef113669a1e7d4a8505ade_2_690x111.png" alt="imagen" data-base62-sha1="4UyAUwu6aAaWfspagGUasAkxwnk" width="690" height="111" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/226d632a86f8ebdd7bef113669a1e7d4a8505ade_2_690x111.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/226d632a86f8ebdd7bef113669a1e7d4a8505ade_2_1035x166.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/226d632a86f8ebdd7bef113669a1e7d4a8505ade.png 2x" data-dominant-color="4F515B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">imagen</span><span class="informations">1122×181 23.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @chir.set (2025-08-08 14:23 UTC)

<aside class="quote no-group" data-username="bserrano" data-post="1" data-topic="44023">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/bserrano/48/17034_2.png" class="avatar"> bserrano:</div>
<blockquote>
<p>the cylinders remain with <code>visibility=True</code></p>
</blockquote>
</aside>
<p>This observation is expected. When you say <code>visibility=true</code>, I understand <code>node.GetDisplayNode().GetVisibility()</code>. Do you mean <em>screen visibility</em>?</p>
<p>The folder can hide a child markups node on screen irrespective of its visibility from the display node.</p>
<p>If I run your code with fiducial nodes as child items of a folder, the same observations are made.</p>
<p>The folder item seems to set the screen visibility of its child items without modifying the visibility member of their display nodes.</p>
<p>This is the good implementation. If a folder has some child nodes explicitly hidden and others visible, toggling the visibility of the folder should not change the actual visibility property of the nodes. Only the screen visibility of visible nodes will change.</p>

---

## Post #3 by @bserrano (2025-08-11 08:23 UTC)

<p>The behavior I expect is that when I run <code>shNode.SetItemDisplayVisibility(folderCylID, False)</code>, the cylinders contained in the folder hide their display in both 2D and 3D views. This is the same as what happens when you click the “eye” icon for the folder.</p>
<p>I don’t understand why the same code, when executed in the terminal outside of the script, does show this behavior.</p>

---

## Post #4 by @chir.set (2025-08-11 08:50 UTC)

<aside class="quote no-group" data-username="bserrano" data-post="3" data-topic="44023">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/bserrano/48/17034_2.png" class="avatar"> bserrano:</div>
<blockquote>
<p>when executed in the terminal</p>
</blockquote>
</aside>
<p>You mean, outside of Slicer or Slicer’s environment? in an OS terminal?</p>

---

## Post #5 by @bserrano (2025-08-11 08:56 UTC)

<p>No, in the Python interactor in Slicer</p>

---

## Post #6 by @chir.set (2025-08-11 09:07 UTC)

<p>So, to recap:</p>
<ul>
<li>the nodes are not hidden when the code runs in your module/script</li>
<li>the nodes are hidden when the code runs in your Slicer’s python console.</li>
</ul>
<p>The immediate inference is that some processing in your module/script is preventing that. Without seeing more of your module/script, it would be hard to guess. May be your processing is not responsible, in which case, Slicer devs can be more helpful.</p>

---

## Post #7 by @bserrano (2025-08-11 09:43 UTC)

<p>That’s it.</p>
<p>In the earlier steps, the script creates a set of cylinders, converts them to models, and then to segments. These cylinder segments are then used for some processing with the <code>segmentEditor</code> module (<a href="https://discourse.slicer.org/t/crop-segment-using-shapenode/43822">see related topic</a>).</p>
<p>After that step, I want to hide the cylinders to continue the process.</p>
<p>I’ll try looping over the elements in the folder and hiding the cylinders individually instead.</p>

---

## Post #8 by @cpinter (2025-08-11 09:58 UTC)

<p>Please read this comment about how folder display node works</p>
<aside class="quote quote-modified" data-post="15" data-topic="29499">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/how-to-add-folder-in-scene/29499/15">How to add folder in scene?</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #000000;" data-drop-close="true" class="badge-category --style-square " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
    </div>
  </div>
  <blockquote>
    The folders have a special folder display node, but it is only created when you show/hide it in the Data module (you’ll notice because the color item will appear in its row). In theory you can create it programmatically, but as I see that function is not python wrapped. This is the code: 
pluginHandlerSingleton = slicer.qSlicerSubjectHierarchyPluginHandler.instance()
folderPlugin = pluginHandlerSingleton.pluginByName('Folder')
folderPlugin.createDisplayNodeForItem(folderItemID)

If you need to c…
  </blockquote>
</aside>

<p>Is it possible that when you paste the code in the Python console you already clicked the show/hide of the folder in the Data module, but when you had done this from your module you hadn’t?</p>
<p>By the way please use the latest Slicer, we cannot really help with old versions. 5.6.2 is a year and a half old now, and there have been quite a lot of changes since then.</p>

---

## Post #9 by @bserrano (2025-08-11 13:27 UTC)

<p>Now I understand…</p>
<p>I solved the problem using</p>
<pre data-code-wrap="python"><code class="lang-python">    slicer.app.processEvents() 
    shNode = slicer.mrmlScene.GetSubjectHierarchyNode()
    sceneItemID = shNode.GetSceneItemID()
    folderCylID = shNode.GetItemChildWithName(sceneItemID, "Cylinders")

   
    childrenItemIDs = []
    shNode.GetItemChildren(folderCylID, childrenItemIDs)
    
    for childID in childrenItemIDs:
        shNode.SetItemDisplayVisibility(childID, 0)  
</code></pre>
<p>Thanks</p>

---
