# How to save slicer scene with both slicer data and with "self.variables" within custom widget

**Topic ID**: 9830
**Date**: 2020-01-16
**URL**: https://discourse.slicer.org/t/how-to-save-slicer-scene-with-both-slicer-data-and-with-self-variables-within-custom-widget/9830

---

## Post #1 by @jdp (2020-01-16 01:45 UTC)

<p>I am using Slicer to create a widget for an application in which I would like to save my work. I see in slicer there is saveScene() in which I can do an mrml or a mrb file - which I can get to work. However, the widget also includes variables and structures as such as “self.variable1, self.variable2.subvariable2, etc.” These “self.variables” are important to my GUI’s widget and logic classes. The issue is when I save the scene I am successful in saving the fiducial nodes and image that was brought into slicer because they are slicer nodes (I believe) but the :self.variables" associated with the widget do not save. In other words, when I try to re-open my saved scene the program fails because the self.A and other variables are not saved within the scene.</p>
<p>Is there an easy way to save these “self.variables” so I can reopen slicer after closing it to where I was last with the values back in my variables? Is there a suggested solution to reopening slicer with reimporting these self.variables back into the program quickly if slicer can not save the variables?</p>

---

## Post #2 by @lassoan (2020-01-16 02:16 UTC)

<p>You raise a very important point. It is easy to write a scripted module that “works” and it is very tempting to stop there - and not spend time with implementing automatic tests, saving of module state to the scene, etc.</p>
<p>Developers are supposed to save all information that is necessary to recreate the current state of the module in nodes in the MRML scene. You can find some useful general information about this in the first part of <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">PerkLab Scripted Module Development tutorial</a>. This practice is strictly followed in all Slicer core modules, but since they are mostly implemented in C++ they are not useful examples for scripted module developers.</p>
<p>For scripted modules, we added <a href="http://apidocs.slicer.org/master/classvtkMRMLScriptedModuleNode.html">vtkMRMLScriptedModuleNode</a>, a generic MRML node to store data persistently in the scene. There is a <code>getParameterNode</code> helper function in scripted module logic class to retrieve a parameter node. The parameter node can be chosen to be a singleton (one instance per scene) or a non-singleton node (in that case a <code>isSingletonParameterNode</code> member has to be set to False in module logic and parameter node selector has to be added to the module widget). See <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/VectorToScalarVolume/VectorToScalarVolume.py">VectorToScalarVolume</a> module as an example of a scripted module with non-singleton parameter node.</p>

---

## Post #3 by @jdp (2020-01-16 17:38 UTC)

<p>This point makes a lot of sense now and I did start to use the “vtkMRMLScriptedModuleNode”. However, it appears that you can only pass in a string value when using GetParameter()? In looking at the documentation it seems like you can only pass in strings with this method. Is there a way to pass in a structure array such as “A” with variables like A.x1 = some number, A.x2 = some string, A.x3 = some node, and variables containing sub variables like A.y.z1 = some number, A.y.z2 = some string, A.y.z3 = some node? I would like to pass “A” into a node like “vtkMRMLScriptedModuleNode” so the slicer scene can re-import. Or do I need to break this structure array up and put the parameters (strings, numbers, nodes, etc.) into specific slicer nodes?</p>

---

## Post #4 by @lassoan (2020-01-16 18:39 UTC)

<p>In Python, you can very easily serialize any values to/from string. You can even just dump everything in a json string. However, it is a bit nicer and safer to break up the information to smaller, individually named chunks.</p>

---

## Post #5 by @pieper (2020-01-16 19:01 UTC)

<p>I actually prefer the json approach as used <a href="https://github.com/pieper/SlicerAnimator/blob/master/Animator/Animator.py#L854-L861">here</a> since it lets you create a very natural mapping between your mrml node and a data structure of arbitrary complexity.  Whatever approach you use, you’ll need to take care about the performance if you have lots and lots of state data.</p>

---

## Post #6 by @jdp (2020-01-16 22:38 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/pieper">@pieper</a>, thank you for your inputs. This has helped me greatly on both understanding slicer/slicer documentation. I did run into an issue with the serializing recommendations because my structure does contain items that are of the “qt.QStandardItemModel()” structure. I plan on modifying my code to read in the strings from json and then placing them into the variable that is of the qt.QStandardItemModel() structure at widget initiation, e.g., will have my program see if the json file exist first before defaulting to blank. I assume there are no good ways to serialize qt items like qt.QStandardItemModel() or is there?</p>

---

## Post #7 by @lassoan (2020-01-16 23:18 UTC)

<p>QStandardItemModel is a GUI class, so you cannot rely on it for implementing essential features, such as data storage. You have to make your module fully functional without a GUI just using logic and MRML classes (in case if another module or a batch processing script wants to use its features).</p>

---

## Post #8 by @jdp (2020-01-16 23:26 UTC)

<p>Thank you for that note - and the earlier comments - as it explains a lot of what I was seeing in the documentation but wasn’t fully understanding as I was learning to work with slicer scripting. I saw GUI/widget needed to be sperate from the logic class and MRML data in the literature. However, I didn’t put those facts together with Qt being for GUI and shouldn’t be used for storage. Thank you.</p>

---

## Post #9 by @Juicy (2020-02-02 08:20 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>I am trying to get my head around this ScriptedModuleNode thing. In the Perklab slides (on slide 10) it says ‘include a parameter node selector at the top (or use a singleton paratmeter node)’</p>
<p>I see that Vector to Scalar Volume and SegmentStatistics seem to have parameter node selectors at the top of the module GUI. What is the advantage of using a singleton vs non singleton scripted module node? What would be more appropriate for use in the module I have been working on <a href="https://github.com/ReynoldsJ20/SlicerFiducialsToModelDistance" rel="nofollow noopener">(FiducialToModelDistance)</a></p>
<p>Are there scripted modules you can think of which use a singleton parameter node which I can look through? I tried looking through the other scripted modules in the slicer core code but cant seem to find anything.</p>

---

## Post #10 by @lassoan (2020-02-04 04:04 UTC)

<aside class="quote no-group" data-username="Juicy" data-post="9" data-topic="9830">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/74df32/48.png" class="avatar"> Juicy:</div>
<blockquote>
<p>What is the advantage of using a singleton vs non singleton scripted module node?</p>
</blockquote>
</aside>
<p>Singleton parameter node:</p>
<ul>
<li>Pro: no need to complicate the GUI with a parameter node selector</li>
<li>Con: you can only store one set of parameters in the scene (if you load a scene that had a parameter set node in it, it overwrites the parameter node in the current scene)</li>
</ul>
<aside class="quote no-group" data-username="Juicy" data-post="9" data-topic="9830">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/74df32/48.png" class="avatar"> Juicy:</div>
<blockquote>
<p>What would be more appropriate for use in the module I have been working on <a href="https://github.com/ReynoldsJ20/SlicerFiducialsToModelDistance">(FiducialToModelDistance)</a></p>
</blockquote>
</aside>
<p>There are a couple of input parameters, so I think using a non-singleton parameter node would be more appropriate.</p>

---

## Post #11 by @Juicy (2020-02-04 04:24 UTC)

<p>Thanks for the reply. So will the parameter node save the inputs which were in the input boxes when the apply button is pressed?</p>
<p>Then when the scene is loaded again it repopulates the input boxes with the same nodes somehow?</p>
<p>I will read through the code in segment statstics module etc and try and figure out how to store the data and retreive it again. It is a bit difficult to understand with my non programming brain <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #12 by @lassoan (2020-02-04 04:35 UTC)

<aside class="quote no-group" data-username="Juicy" data-post="11" data-topic="9830">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/74df32/48.png" class="avatar"> Juicy:</div>
<blockquote>
<p>So will the parameter node save the inputs which were in the input boxes when the apply button is pressed?</p>
<p>Then when the scene is loaded again it repopulates the input boxes with the same nodes somehow?</p>
</blockquote>
</aside>
<p>No, of course nothing is saved or repopulated automatically. You implement these in <code>updateGUIFromParameterNode</code> and <code>updateParameterNodeFromGUI</code> methods. This module should be a relatively straightforward example that you can follow: <a href="https://github.com/PerkLab/SlicerVolumeClip/blob/master/VolumeClipWithModel/VolumeClipWithModel.py#L252-L288" class="inline-onebox">SlicerVolumeClip/VolumeClipWithModel/VolumeClipWithModel.py at master · PerkLab/SlicerVolumeClip · GitHub</a></p>

---

## Post #13 by @Suhaim (2025-07-30 11:42 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="9830">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Developers are supposed to save all information that is necessary to recreate the current state of the module in nodes in the MRML scene.</p>
</blockquote>
</aside>
<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>, thanks for the great work done by you and your team.</p>
<p>Could you please direct me to an implementation of a loadable module that is doing this? That is, saving it’s relevant parameter set into a node which is added to the scene to save it’s state.<br>
To provide you with some context, I was able to persist relevant state for my scripted module using json. I am now trying to figure out how to do it for my loadable module as well.</p>
<p>Thank you.</p>

---

## Post #15 by @Suhaim (2025-08-02 15:44 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="9830">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Developers are supposed to save all information that is necessary to recreate the current state of the module in nodes in the MRML scene. You can find some useful general information about this in the first part of <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials" rel="noopener nofollow ugc">PerkLab Scripted Module Development tutorial</a>. This practice is strictly followed in all Slicer core modules, but since they are mostly implemented in C++ they are not useful examples for scripted module developers.</p>
</blockquote>
</aside>
<p>Hi <a href="https://discourse.slicer.org/u/lassoan">@lassoan</a>, as per what you have said here, what I understand is that, a core C++ MRML node is an example of how to create something like the vtkMRMLScriptedModuleNode for persisting state for a loadable module. A custom node similar to how the core MRML nodes are written will have to be created first. Then it would store as a member the relevant parameter set for the loadable module.</p>
<p>This custom node is created and added to the scene and stored with the scene, so that relevant module parameters can persist across scene loading/reloading. Please correct me if I am wrong.</p>
<p>Thank you.</p>
<p>PS : For anyone interested, I found the <a href="https://github.com/Slicer/Slicer/blob/main/Libs/MRML/Core/vtkMRMLTextNode.h" rel="noopener nofollow ugc">vtkMRMLTextNode</a> to be a useful example to understanding everything one needs to do while creating a custom MRML node. Slicer documentation - <a href="https://www.slicer.org/wiki/Documentation/4.2/Developers/MRML" rel="noopener nofollow ugc">creating custom MRML node classes</a>.</p>

---

## Post #16 by @mikebind (2025-08-04 17:07 UTC)

<p>Usually, there is no need to create your own MRML node type to enable load/save state functionality for a scripted module you are developing.  What is easier, and suggested above, is to use a parameter node (an instance of vtkMRMLScriptedModuleNode) to store parameter values and node selections. Because the parameter node is a MRML node in the Slicer scene, it will be saved and loaded when the scene is saved and loaded; therefore it can be used to store and bring back information that you want to persist.  There are only two types of things that can be stored in parameter nodes: character strings and node references.  Therefore, if you need to store something else (like a number) you need to translate it to a string before adding it to the parameter node, and you need to translate it back when accessing the parameter from the parameter node.</p>
<p>Node references are the preferred way to persist things like which MRML node was selected in your module when a scene was saved.  This is because the other usual way to uniquely identify MRML nodes, the string ID returned by node.GetID(), is NOT guaranteed to be preserved over a save/close/load cycle.</p>
<p>You only really need to create a new type of custom MRML node if you have a new type of data object that you want to add to Slicer and interact with in similar ways to other MRML nodes (for example like creating display nodes or storage nodes associated with it, or … actually, I’m not sure, I’ve never run into a case where it seemed like creating a whole new MRML node type seemed necessary).  This is definitely overkill if all you want to do is be able to restore your module state from a saved scene.</p>

---

## Post #17 by @Suhaim (2025-08-06 09:09 UTC)

<p>Thanks a lot <a class="mention" href="/u/mikebind">@mikebind</a> for the quick reply, I will try to do this. Would you have come across an example of a loadable module that is persisting states relevant to it? If so, could you share it?</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="9830">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>In Python, you can very easily serialize any values to/from string. You can even just dump everything in a json string. However, it is a bit nicer and safer to break up the information to smaller, individually named chunks.</p>
</blockquote>
</aside>
<p>I understand how to do this for a scripted module, which is mentioned here by <a class="mention" href="/u/lassoan">@lassoan</a> as well.</p>

---

## Post #18 by @cpinter (2025-08-06 11:16 UTC)

<p>This is a not very recent example but not much has changed in the C++ side since then</p><aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerRt/SlicerRT/tree/master/DoseComparison">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" alt="" width="32" height="32">

      <a href="https://github.com/SlicerRt/SlicerRT/tree/master/DoseComparison" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerRt/SlicerRT/tree/master/DoseComparison" target="_blank" rel="noopener">SlicerRT/DoseComparison at master · SlicerRt/SlicerRT</a></h3>


  <p><span class="label1">Open-source toolkit for radiation therapy research, an extension of 3D Slicer. Features include DICOM-RT import/export, dose volume histogram, dose accumulation, external beam planning (TPS), struc...</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #19 by @Suhaim (2025-08-08 04:08 UTC)

<p>Thank you <a class="mention" href="/u/cpinter">@cpinter</a>, this helps a lot!</p>

---

## Post #20 by @Suhaim (2025-08-08 11:34 UTC)

<p>Hi everyone, I needed some more help regarding this as the example mentioned here seems to be persisting state using a custom MRML node - <a href="https://github.com/SlicerRt/SlicerRT/blob/master/DoseComparison/Logic/vtkMRMLDoseComparisonNode.h" rel="noopener nofollow ugc">vtkMRMLDoseComparisonNode</a>. Would you prefer that I create a new post specifically asking about saving state for a loadable module as the user who made this current post was more focused on scripted modules. Or should I continue the discussion here itself?</p>

---

## Post #21 by @cpinter (2025-08-11 09:06 UTC)

<p>Hard to answer without knowing your actual question. Please describe the issue here, it seems quite related.</p>

---
