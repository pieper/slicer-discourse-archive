---
topic_id: 11483
title: "How To Get Help When Programming Extension With Slicer Using"
date: 2020-05-10
url: https://discourse.slicer.org/t/11483
---

# How to get help when programming extension with slicer using loadable module?

**Topic ID**: 11483
**Date**: 2020-05-10
**URL**: https://discourse.slicer.org/t/how-to-get-help-when-programming-extension-with-slicer-using-loadable-module/11483

---

## Post #1 by @sunshine_boycn (2020-05-10 09:01 UTC)

<p>Dear everybody:</p>
<p>I have tried a lot of tutorials on the website on how to programming the slicer extension using c++. I could built a very simple extension and load it successfully. However, what I found difficult is how to get the information and send the result from and to the slicer. Different information might have different names, nodes or data structures, how could I get this information? There seems no documents on it. Such as get the images of one CT scanned images, get the models of the 3D reconstructed models by programming and so on. Which data format is the slicer using? I thought there should be some manuals or tutorials on it.</p>
<p>Thank you very much</p>

---

## Post #2 by @pieper (2020-05-10 14:04 UTC)

<p>Hi -</p>
<p>It sounds like you are making progress.  It’s true that there many things you could do with Slicer that don’t have manuals or tutorials.  Slicer is free and supported by people who use it as part of their research work.  So while we are happy to help answer specific questions, a lot of the work for developers involves reading code and examples to learn how the pieces fit together.</p>
<p>Fortunately everything is open and transparent, so it’s possible to study everything and see how it works using standard computing tools like debuggers and IDEs.</p>

---

## Post #3 by @sunshine_boycn (2020-05-10 14:54 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="11483">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>examples</p>
</blockquote>
</aside>
<p>Thank you very much! Yes you are right, thank goodness that everything is open and transparent. Now I am trying to read the code and examples one by one.</p>
<p>I have one problem now. I noticed that there are three classes for a typical loadable module. Such as Module, Module Widget, and Module Logic. The Module Widget holds for the GUI. The slot function in this module should call the method from the Module Logic. However, how to obtain the handler/pointer of the Module Logic. I saw no variables in Module holding this pointer and createLogic() function would lead to memory leak. How to obtain the Module Logic pointer from Module Widget using c++ ?</p>
<p>Thank you very much.</p>

---

## Post #4 by @pieper (2020-05-10 16:04 UTC)

<p>The logic classes can be thought of like a utility library for the module, where algorithms and other non-user interface code can be kept.  By default a module’s gui code will create one instance of the logic <a href="https://github.com/Slicer/Slicer/search?p=5&amp;q=createLogic&amp;unscoped_q=createLogic">in the <code>createLogic</code> method</a> and re-use it (storing a pointer in the widget instance), but since they are typically very lightweight you’ll also see them created on the fly when needed.</p>
<p>One common use of a logic class is for other modules to make use of it, like <a href="https://github.com/Slicer/Slicer/blob/ac2e80cbd99b74ce646b912a2461eef17bcd6c5e/Modules/Loadable/CropVolume/Logic/vtkSlicerCropVolumeLogic.cxx#L178-L199">the CropVolume module using the Volumes module logic to clone a volume</a>.</p>
<p>I’m sure it looks messy, but it’s worth looking at the <a href="http://apidocs.slicer.org/master/index.html">inheritance structure</a> carefully to see how common functionality is factored out through the levels of the inheritance hierarchies.  There are distinct trees for widgets, data, logic, visualization, etc.</p>

---

## Post #5 by @pieper (2020-05-10 16:06 UTC)

<p>One other suggestion: we typically find that if people start with python scripted modules they learn some of the basics and then it’s easier get into the C++ code.</p>

---

## Post #6 by @sunshine_boycn (2020-05-11 15:13 UTC)

<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="11483">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>toring a pointer in the wid</p>
</blockquote>
</aside>
<p>Thank you very much. I firstly figure out the mechanism of Q_Q and Q_D. And found it useless with this problem and then go though all the base classes and found out the logic pointer could be obtained with appLogic() in Module and logic() in ModuleWidget.</p>
<p>Although current problem has been solved, it seems a long long way to go with slicer…</p>

---
