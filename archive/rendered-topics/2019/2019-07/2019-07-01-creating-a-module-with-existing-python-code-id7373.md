# Creating a module with existing python code

**Topic ID**: 7373
**Date**: 2019-07-01
**URL**: https://discourse.slicer.org/t/creating-a-module-with-existing-python-code/7373

---

## Post #1 by @Jesse (2019-07-01 20:55 UTC)

<p>Hi all</p>
<p>I’m new to 3D slicer and I’m looking for ways to create a plug-in (extension) in this software which can utilize already existing python codes. I can’t really find anything helpful online about this. Anybody here who can help me out?</p>
<p>Thanks,<br>
Jesse</p>

---

## Post #2 by @fedorov (2019-07-01 20:56 UTC)

<p>I think this resource is supposed to be the extension developer starting point: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/BuildTestPackageDistributeExtensions" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/BuildTestPackageDistributeExtensions</a></p>
<p>Did you see it? Or you did see it, but it was not helpful?</p>

---

## Post #3 by @Jesse (2019-07-02 16:31 UTC)

<p>I did see it, but I still don’t quite understand. I have never used slicer before.<br>
I also don’t quite understand the difference between a scripted module (which is written in python) and a python based CLI. Which would be the best choice for my application?</p>

---

## Post #4 by @fedorov (2019-07-02 18:48 UTC)

<p>It depends on what your application is. CLIs are suitable for non-interactive and batch processing tools.</p>

---

## Post #5 by @fedorov (2019-07-02 20:52 UTC)

<p>It can help if you start with an extension that has similar functionality. If you share the details of what you are trying to do, we may be able to point you to similar extensions/modules, or give more specific advice.</p>

---

## Post #6 by @Jesse (2019-07-02 21:15 UTC)

<p>Hi fedorov. The idea is to manually delineate tumors in some MRI slices and then the extension should delineate the remaining slices resulting in a complete delineation. A first version of the python code to do this is already available. I’m looking if it is feasible to implement this existing python code in a plugin/extension, so basically an implementation of the code. Thanks.</p>

---

## Post #7 by @fedorov (2019-07-02 22:45 UTC)

<p>Take a look at Segment Editor: <a href="https://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html" rel="nofollow noopener">https://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html</a></p>
<p>There is already “Fill between slices” effect. This should be a good place to start.</p>

---

## Post #8 by @lassoan (2019-07-02 22:49 UTC)

<p>As <a class="mention" href="/u/fedorov">@fedorov</a> suggested above, you would normally implement such features as an effect in Segment Editor module. You can see an example of an extension that adds several new effects <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects" rel="nofollow noopener">here</a>. You can fork this extension and then use “Extension Wizard” module in Slicer to add a new module of <em>scriptedsegmenteditoreffect</em> type.</p>

---

## Post #9 by @Jesse (2019-07-03 06:39 UTC)

<p>So if I’m understanding correctly, I can use the Segment Editor module to delineate some slices and add my own python code as an extra module to propagate the delineations to the other remaining slices? And so create an extension.</p>

---

## Post #10 by @lassoan (2019-07-03 13:09 UTC)

<p>Yes. Slicer’s Segment Editor module already has a number of effects that require an approximate segmentation as input (“Grow from seeds” effect requires seeds inside segments as input; “Fill between slices” requires accurate segmentation in a few slices) and generates full segmentation from that.</p>
<p>You can add modules (implemented in Python) that add similar effects to the Segment Editor. For example, SegmentEditorExtraEffects extension adds Watershed and Fast marching effects to the Segment Editor, which takes seed regions and generate full segmentation from it.</p>
<p>Probably a good way to start is to <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation" rel="nofollow noopener">learn what Segment Editor can do</a>, check out <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Tutorials_for_software_developers" rel="nofollow noopener">Slicer programming tutorials</a>, have a look at existing <a href="https://github.com/Slicer/Slicer/tree/master/Modules/Loadable/Segmentations/EditorEffects/Python" rel="nofollow noopener">Segment Editor effect implementations in Slicer core</a> and in <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects" rel="nofollow noopener">SegmentEditorExtraEffects</a> and then create a new effect using Extension Wizard and put your code into it.</p>
<p>If you want Slicer users to easily access your new tool, you can submit your extension to the Slicer appstore where people can download and install by a few clicks.</p>

---

## Post #11 by @Jesse (2019-07-03 17:19 UTC)

<p>Thank you for this information, I think this will be helpful! This morning, I also stumbled upon <a href="https://docs.google.com/presentation/d/1JXIfs0rAM7DwZAho57Jqz14MRn2BIMrjB17Uj_7Yztc/edit#slide=id.g41f90baec_028" rel="nofollow noopener">https://docs.google.com/presentation/d/1JXIfs0rAM7DwZAho57Jqz14MRn2BIMrjB17Uj_7Yztc/edit#slide=id.g41f90baec_028</a><br>
I was following it and I think this is a template to create your own extension, is that correct?</p>

---

## Post #12 by @lassoan (2019-07-03 19:24 UTC)

<p>Although the presentation is 5 years old, it is still mostly valid. There have been a number of important improvements in Slicer, so my recommendations would be somewhat different in these details:</p>
<ul>
<li>I would not recommend using the simple “scripted” template type for new modules but use “scripteddesigner” for general-purpose modules and “scriptedsegmenteditoreffect” for Segment Editor effects.</li>
<li>I would not use the legacy chart infrastructure for 2D diagrams but use the new <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Plots" rel="nofollow noopener">plots</a> infrastructure instead.</li>
</ul>
<p>You can find updated tutorial for scripteddesigner template based projects <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials" rel="nofollow noopener">here</a>.</p>

---

## Post #13 by @Jesse (2019-07-04 16:37 UTC)

<p>I still find it difficult to understand the codes behind the segment editor modules, may be due to my lack of experience in python. What would you recommend me to due to try to understand these codes?</p>

---

## Post #14 by @lassoan (2019-07-04 17:35 UTC)

<p>It is certainly not simple task to implement such features. You need to be somewhat familiar with VTK and Qt libraries and have a basic understanding of MRML. I would recommend to study the source code of existing segment editor effects, find one that does something similar to what you would need, and modify that. You can implement effects either in C++ or Python. If you have any specific question then we are here to help.</p>

---

## Post #15 by @Jesse (2019-07-04 19:28 UTC)

<p>Do you know a good place where I can get familiar with VTK and Qt libraries?<br>
I also already looked a bit into MRML because it seemed important but I couldn’t find something immediately that made clear what it is<br>
I also looked at the source code of “Fill in between slices” because the concept is quite similar but to my surprice this was only 46 lines long. To me this seems very short.</p>

---

## Post #16 by @lassoan (2019-07-04 19:47 UTC)

<aside class="quote no-group" data-username="Jesse" data-post="15" data-topic="7373">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/c77e96/48.png" class="avatar"> Jesse:</div>
<blockquote>
<p>Do you know a good place where I can get familiar with VTK and Qt libraries?</p>
</blockquote>
</aside>
<p>VTK and other medical image computing related libraries: see <a href="https://discourse.slicer.org/t/a-free-biomedical-image-analysis-and-visualization-2-day-course/2584/10">this post</a>.<br>
Qt: there are many online tutorials and examples.</p>
<aside class="quote no-group" data-username="Jesse" data-post="15" data-topic="7373">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/c77e96/48.png" class="avatar"> Jesse:</div>
<blockquote>
<p>I also looked at the source code of “Fill in between slices” because the concept is quite similar but to my surprice this was only 46 lines long. To me this seems very short.</p>
</blockquote>
</aside>
<p>That’s the point. If you already have a method that computes missing segmentation between segmented slices, then you need to write a few ten lines of code to make it available in Slicer.</p>

---
