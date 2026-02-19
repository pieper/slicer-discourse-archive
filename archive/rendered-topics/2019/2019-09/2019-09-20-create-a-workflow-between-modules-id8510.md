---
topic_id: 8510
title: "Create A Workflow Between Modules"
date: 2019-09-20
url: https://discourse.slicer.org/t/8510
---

# Create a workflow between Modules

**Topic ID**: 8510
**Date**: 2019-09-20
**URL**: https://discourse.slicer.org/t/create-a-workflow-between-modules/8510

---

## Post #1 by @DzLeon (2019-09-20 17:36 UTC)

<p>Operating system: win10<br>
Slicer version: 4.10.0<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hi,everyone. I want to create a flow like this: DICOM → Segment editor -&gt;Segmentations-&gt;…<br>
by using /creating a button in each module instead of using the module list in toolbar.</p>
<p>I noticed that there is a button in Segment editor module can do the work like i mentioned above.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20d0123bb3ecdfbb58dd91447af82f8cecd21f4b.png" data-download-href="/uploads/short-url/4Gh4jwnfHssCZN3MkAtYxFKa16z.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20d0123bb3ecdfbb58dd91447af82f8cecd21f4b.png" alt="image" data-base62-sha1="4Gh4jwnfHssCZN3MkAtYxFKa16z" width="513" height="500" data-dominant-color="F6F5F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">555×540 21.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Can someone give me some suggestions about how to achieve this ?</p>
<p>Thanks in advance.</p>

---

## Post #2 by @lassoan (2019-09-20 17:39 UTC)

<p>See description of how to implement a “slicelet”, a custom workflow with simple and convenient user interface: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets</a></p>

---

## Post #3 by @pieper (2019-09-21 16:36 UTC)

<p>You could also look at the CaseIterator extension if you are working through a long list of similar subjects.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerCaseIterator" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerCaseIterator</a></p>

---

## Post #4 by @DzLeon (2019-09-23 02:20 UTC)

<p>Thanks for the reply.</p>
<p>A “slicelet” seems really good.</p>
<p>But i do not want to create another user interface and what i expect is that we do not change modules or extract functions from modules and we only set a fixed order for each module , for example, we load dicom iamges in DICOM module and  we click a “Next” button  (that we can create)  on DICOM UI, it will go directly to Segment editor module.</p>
<p>The function of this “Next” button is similar to the “Segmentation” button in above pic.</p>
<p>Can this be achieved ?</p>

---

## Post #5 by @DzLeon (2019-09-23 05:14 UTC)

<p>Thanks guys . I  have solved this problem by using the code below:</p>
<pre><code>// Switch to registration module and set selections
qSlicerAbstractModuleWidget* moduleWidget = qSlicerSubjectHierarchyAbstractPlugin::switchToModule("SegmentEditor");
QApplication::processEvents();</code></pre>

---

## Post #6 by @Alex_Vergara (2019-09-23 14:24 UTC)

<p>Thanks for this, it helped a lot!<br>
In python the code is easier</p>
<pre><code class="lang-python">def switchModule(self, moduleName):
    # Switch to another module
    pluginHandlerSingleton = slicer.qSlicerSubjectHierarchyPluginHandler.instance()
    pluginHandlerSingleton.pluginByName('Default').switchToModule(moduleName)
</code></pre>

---

## Post #7 by @lassoan (2019-09-23 14:41 UTC)

<aside class="quote no-group" data-username="DzLeon" data-post="4" data-topic="8510">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/bb73d2/48.png" class="avatar"> DzLeon:</div>
<blockquote>
<p>But i do not want to create another user interface and what i expect is that we do not change modules or extract functions from modules and we only set a fixed order for each module</p>
</blockquote>
</aside>
<p>Built-in module user interfaces expose almost all underlying features, which is ideal for free experimentation. However, this flexibility and complexity is not well suited for enforcing a fixed workflow. Depending on your users, they may be able to tolerate this.</p>
<p>In general, you can get much better results by creating your own module GUI by using Qt designer application. You just drag-and-drop the components you need and connect them in the designer and maybe a few ten or hundred lines of Python code. See details instructions in <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">this tutorial</a>.</p>
<p>Example of a module GUI edited in Qt designer, made of Qt, CTK, and high-level Slicer widgets:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84c0d08c88ae12a2e4a92e1882190274c874e031.png" data-download-href="/uploads/short-url/iWo8244xDaaud3jBHjByi45vKcV.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84c0d08c88ae12a2e4a92e1882190274c874e031_2_689x369.png" alt="image" data-base62-sha1="iWo8244xDaaud3jBHjByi45vKcV" width="689" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84c0d08c88ae12a2e4a92e1882190274c874e031_2_689x369.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84c0d08c88ae12a2e4a92e1882190274c874e031_2_1033x553.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84c0d08c88ae12a2e4a92e1882190274c874e031.png 2x" data-dominant-color="DDDDDC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1194×640 65.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Most modules provide reusable high-level components but if there are some features in a module GUI that you cannot replicate easily in your own module then let us know. Segment Editor is designed to be embedded into custom module GUIs. DICOM browser is not displayed in a view layout, so in your module you can simply switch to the DICOM browser view layout to browse/load DICOM files.</p>

---
