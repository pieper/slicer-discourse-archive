---
topic_id: 23626
title: "Dynamicmodeler Transform Maker"
date: 2022-05-29
url: https://discourse.slicer.org/t/23626
---

# DynamicModeler Transform Maker

**Topic ID**: 23626
**Date**: 2022-05-29
**URL**: https://discourse.slicer.org/t/dynamicmodeler-transform-maker/23626

---

## Post #1 by @mau_igna_06 (2022-05-29 14:04 UTC)

<p>I already started implementing.</p>
<p>The idea is a transformComposer that would get as input any number of: oneFiducialLists, angles, planes and linearTransforms. It would concatenate the transform for all of them.<br>
And output some or all of a point, an angle, a plane or a linear transform according to the concatenated transformations corresponding to the inputs.</p>
<p>This will highly improve the workflow of scientists that have to measure or make transforms according to some anatomical axis. It would also ease on the creation of surgical guides with the relative difference that transforms will be highly accesible in contrast with Blender</p>
<p>Please let me know your thoughts</p>

---

## Post #2 by @mau_igna_06 (2022-05-29 16:54 UTC)

<p>Here is the current working implementation:</p><aside class="onebox githubfolder" data-onebox-src="https://github.com/mauigna06/SlicerSurfaceToolbox/tree/AddGeometryFeatureV2">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/mauigna06/SlicerSurfaceToolbox/tree/AddGeometryFeatureV2" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/mauigna06/SlicerSurfaceToolbox/tree/AddGeometryFeatureV2" target="_blank" rel="noopener nofollow ugc">GitHub - mauigna06/SlicerSurfaceToolbox at AddGeometryFeatureV2</a></h3>

  <p><a href="https://github.com/mauigna06/SlicerSurfaceToolbox/tree/AddGeometryFeatureV2" target="_blank" rel="noopener nofollow ugc">AddGeometryFeatureV2</a></p>

  <p><span class="label1">Supports various cleanup and optimization processes on surface models</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>(don’t pay attention to the branch name)</p>
<p>For example you can concatenate angles and create a bigger angle with live feedback:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/ebe28568ab9cd97e0258aaebfc4cc43a03bd7f97.png" data-download-href="/uploads/short-url/xEJwxsPX6yulJPsgKBxWICPQhHp.png?dl=1" title="dynamicModelerTransformMaker" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/ebe28568ab9cd97e0258aaebfc4cc43a03bd7f97_2_690x387.png" alt="dynamicModelerTransformMaker" data-base62-sha1="xEJwxsPX6yulJPsgKBxWICPQhHp" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/ebe28568ab9cd97e0258aaebfc4cc43a03bd7f97_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/ebe28568ab9cd97e0258aaebfc4cc43a03bd7f97_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/ebe28568ab9cd97e0258aaebfc4cc43a03bd7f97.png 2x" data-dominant-color="D7D8EB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">dynamicModelerTransformMaker</span><span class="informations">1366×768 80.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I think it’s a quite powerful tool, you can compose frames also. And the interaction of markups is still there if you want to use it.</p>

---

## Post #3 by @mau_igna_06 (2022-05-29 19:00 UTC)

<p>I tested a deformity correction surgical planning workflow.</p>
<p>Basically the surgery is filling a wedge after a planar cut, or removing a wedge of bone and joining the bone faces.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fddb13f3af3672f030f8a7b30c39b4b6a7982215.png" data-download-href="/uploads/short-url/AdIaGtea6rnNiSvOZkeUR3Ioyb3.png?dl=1" title="correctedAndDefect1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fddb13f3af3672f030f8a7b30c39b4b6a7982215_2_690x458.png" alt="correctedAndDefect1" data-base62-sha1="AdIaGtea6rnNiSvOZkeUR3Ioyb3" width="690" height="458" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fddb13f3af3672f030f8a7b30c39b4b6a7982215_2_690x458.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fddb13f3af3672f030f8a7b30c39b4b6a7982215.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fddb13f3af3672f030f8a7b30c39b4b6a7982215.png 2x" data-dominant-color="968EB0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">correctedAndDefect1</span><span class="informations">863×573 137 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/069cd04a1f2b43c3b49a6a8f1f4373ffc4ab0dd7.png" data-download-href="/uploads/short-url/WuPRq2JB35inzgnT5pRl8N9ctp.png?dl=1" title="correctedAndDefect2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/069cd04a1f2b43c3b49a6a8f1f4373ffc4ab0dd7_2_690x458.png" alt="correctedAndDefect2" data-base62-sha1="WuPRq2JB35inzgnT5pRl8N9ctp" width="690" height="458" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/069cd04a1f2b43c3b49a6a8f1f4373ffc4ab0dd7_2_690x458.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/069cd04a1f2b43c3b49a6a8f1f4373ffc4ab0dd7.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/069cd04a1f2b43c3b49a6a8f1f4373ffc4ab0dd7.png 2x" data-dominant-color="9991B3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">correctedAndDefect2</span><span class="informations">863×573 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The only problem I found out to take care of all the planning using the Dynamic modeler tools is the unexpected result that output transforms are considered (inside the current tool and the inverse is applied to the polydata) while pipelining tools.<br>
I consider this to be unexpected behavior and it’s preventing me from achieving virtual surgical planning inside Slicer.<br>
Core devs please give your opinion for me at least this behavior should be optional by adding a boolean flag to Dynamic Modelers tools.<br>
Here are the lines I’m referring to:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/SlicerSurfaceToolbox/blob/b219fee5324002e7b6cb2765257cd088b6f8dae0/DynamicModeler/Logic/vtkSlicerDynamicModelerPlaneCutTool.cxx#L367-L374">
  <header class="source">

      <a href="https://github.com/Slicer/SlicerSurfaceToolbox/blob/b219fee5324002e7b6cb2765257cd088b6f8dae0/DynamicModeler/Logic/vtkSlicerDynamicModelerPlaneCutTool.cxx#L367-L374" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/SlicerSurfaceToolbox/blob/b219fee5324002e7b6cb2765257cd088b6f8dae0/DynamicModeler/Logic/vtkSlicerDynamicModelerPlaneCutTool.cxx#L367-L374" target="_blank" rel="noopener nofollow ugc">Slicer/SlicerSurfaceToolbox/blob/b219fee5324002e7b6cb2765257cd088b6f8dae0/DynamicModeler/Logic/vtkSlicerDynamicModelerPlaneCutTool.cxx#L367-L374</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="367" style="counter-reset: li-counter 366 ;">
          <li>if (outputPositiveModelNode &amp;&amp; outputPositiveModelNode-&gt;GetParentTransformNode())</li>
          <li>  {</li>
          <li>  outputPositiveModelNode-&gt;GetParentTransformNode()-&gt;GetTransformFromWorld(this-&gt;OutputPositiveWorldToModelTransform);</li>
          <li>  }</li>
          <li>if (outputNegativeModelNode &amp;&amp; outputNegativeModelNode-&gt;GetParentTransformNode())</li>
          <li>  {</li>
          <li>  outputNegativeModelNode-&gt;GetParentTransformNode()-&gt;GetTransformFromWorld(this-&gt;OutputNegativeWorldToModelTransform);</li>
          <li>  }</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/jcfr">@jcfr</a>, <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a>, <a class="mention" href="/u/pieper">@pieper</a>, <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a></p>

---

## Post #4 by @lassoan (2022-05-30 02:09 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="3" data-topic="23626">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>The only problem I found out to take care of all the planning using the Dynamic modeler tools is the unexpected result that output transforms are considered</p>
</blockquote>
</aside>
<p>Ignoring any transforms is generally not desirable and most users would consider it a bug.</p>
<p>However, I see that for your specific workflow it would be convenient if you could transform the output model without impacting the modeling result. The problem is that simply ignoring all output transforms would prevent computing the output model in the desired coordinate system, so it would only be useful for very few special cases.</p>
<p>What you actually need is the ability to specify an additional transform for the modeling tool’s output. This could be achieved in a much simpler, more elegant way, with a more general solution without complicating any existing tools: by simply adding a new <code>Transform</code> tool. This new tool would use a model and a transform node as inputs and on its output it would create a transformed copy of the input model. This new tool could be used for many other things, such as cloning a model, creating patterns, …</p>

---

## Post #5 by @mau_igna_06 (2022-05-30 07:39 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="23626">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Ignoring any transforms is generally not desirable and most users would consider it a bug.</p>
</blockquote>
</aside>
<p>Yes, maybe but it’s a flag. The flag is there because I think users would like to do recursive use of this tool. Let say this tool is called T and each T use is called T_i and there are In_1_i till In_1_n inputs and one output called Out_i.<br>
The ignore flag implementation is useful when you want that use T_i+1 receives as input the output of T_i.</p>
<p>The argument was pretty but I found it doesn’t justifies the ignore parentTransforms flag so we may remove it.</p>
<blockquote>
<p>The problem is that simply ignoring all output transforms would prevent computing the output model in the desired coordinate system</p>
</blockquote>
<p>Please consider that in the school of thought I was trained on, an algorithm can be considered a system. Let’s say the PlaneCut tool is a system, it receives some inputs and it produces an output, then on the systems chain of the same pipeline there is a OutputTransformNode, let’s consider it a system too, it transforms polydata at it’s input.<br>
In the current implementation there is a feedback loop that assures the output polydata is the same with any OutputTransformsNode’s matrix. In other words, the output of PlaneCut is not transformable in fact.<br>
In my proposed change, the PlaneCut tool output would be transformable.<br>
Between the two behaviours and considering users would like to design things with the Dynamic Modeler I think we should do the second.<br>
My argument is that having a pipeline without feedback loops is easier to analyse and more desirable that one that has them. So default behaviour should be to not do the feedback loop.</p>
<blockquote>
<p>so it would only be useful for very few special cases.</p>
</blockquote>
<p>What are the most common use cases? Why do they need the feedback loop?</p>
<p>I believe Blender is used more for surgical planning and creation of surgical guides in MSK surgeries than Slicer but with some improvements we could gather all those users with the benefit that in Slicer surgical planning is easier to validate and surgcal guides creation is repeatable because transforms to the model components are accessible</p>
<p>What do you think about the TransformMaker? Have you tested it yet?</p>

---

## Post #6 by @mau_igna_06 (2022-05-30 11:47 UTC)

<p>There are some math bugs I’m correcting</p>

---

## Post #7 by @lassoan (2022-05-30 12:51 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="5" data-topic="23626">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>let’s consider it a system too, it transforms polydata at it’s input</p>
</blockquote>
</aside>
<p>Everything happens in the correct physical location, wherever the applied transforms placed the input or output nodes.</p>
<aside class="quote no-group" data-username="mau_igna_06" data-post="5" data-topic="23626">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>In my proposed change, the PlaneCut tool output would be transformable.</p>
</blockquote>
</aside>
<p>Yes, I see that you need an option to transform a node to a different coordinate system after the processing is completed; and I think this would be a useful feature.</p>
<p>This could be implemented in each tool, for each input and output node. But this would mean that we would need to have transformation selection options (e.g., choose between local, world, or a custom transform node) everywhere. This would complicate the implementation and GUI of all input and output nodes selection in all tools.</p>
<p>A similar approach was chosen with CLI modules: all applied transforms are ignored and you need to specify transforms that will be applied to input/output nodes. It did not work out well. Users don’t expect that applied transforms are ignored and it is not obvious what transform selectors are used for what nodes. You could make things a bit more intuitive with better GUI. For example, transform selectors could be placed next to node selectors they apply to. But it would not always be optimal, because sometimes you want to apply the same transform to multiple nodes.</p>
<p>The solution I recommend instead is much simpler to implement. Does not increase complexity in any of the tools, as it is a separate transform tool. The only disadvantage compared to what you propose (i.e., built-in transformation feature in every tool) is that end-users need to add one more tool if they want to have transformed input/output node. However, this could be addressed by improving the GUI, making it easier to add/configure tools.</p>
<p>This GUI improvement is in our mid/long-term plans: we plan to have a Model Editor, which will use the Dynamic modeler as processing engine for editing models similarly to the Segment Editor can edit segmentations. We could make model editing to be immediate (as in Segment Editor, MeshMixer, and in Blender sculpting tools), or parametric (as parametric CAD modeling tools and Blender modifiers).</p>
<aside class="quote no-group quote-modified" data-username="mau_igna_06" data-post="5" data-topic="23626">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<blockquote>
<p>so it would only be useful for very few special cases.</p>
</blockquote>
<p>What are the most common use cases? Why do they need the feedback loop?</p>
</blockquote>
</aside>
<p>There are no feedback loops of any kind, simply everything happens in the world coordinate system. All we do is to take into account applied transforms the same way as if they were hardened.</p>
<aside class="quote no-group" data-username="mau_igna_06" data-post="5" data-topic="23626">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>I believe Blender is used more for surgical planning and creation of surgical guides in MSK surgeries than Slicer but with some improvements we could gather all those users with the benefit that in Slicer surgical planning is easier to validate and surgcal guides creation is repeatable because transforms to the model components are accessible</p>
</blockquote>
</aside>
<p>I would think magnitudes more people use Slicer for surgical planning than Blender, just because Blender is so extremely complicated. But we don’t have data, so there is no way to tell. I agree that those very few users (maybe a few groups in the whole world) may switch to Slicer if we have better tools.</p>
<p>However, majority of people use much simpler, single-purpose commercial tools; and the few percentage of clinicians who use research software prefer simple tools (such as MeshMixer), and only a tiny fraction of advanced clinical research users may choose Mimics or CAD tools. Slicer could compete with all these tools, but probably we could make the biggest impact by offering single-purpose tools (such as your BoneReconstructionPlanner extension, to offer alternative to single-purpose commercial software) and simple editing tools (to compete with MeshMixer and some of the simpler Materialize tools).</p>
<aside class="quote no-group" data-username="mau_igna_06" data-post="5" data-topic="23626">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>What do you think about the TransformMaker? Have you tested it yet?</p>
</blockquote>
</aside>
<p>Please remind me what it is and where I can find it. The name reminds me of the <a href="https://github.com/SlicerIGT/SlicerIGT/tree/master/TransformProcessor">TransformProcessor</a> module in SlicerIGT. Does it have a similar purpose?</p>

---

## Post #8 by @mau_igna_06 (2022-05-30 13:26 UTC)

<p>Hi Andras.</p>
<p>I’ll take time to give a full answer on the afternoon but here you have a preview video:<br>
</p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b5c8d73924bf00df20475abb67cfe89f0c4f3e47.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b5c8d73924bf00df20475abb67cfe89f0c4f3e47.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b5c8d73924bf00df20475abb67cfe89f0c4f3e47.mp4</a>
    </source></video>
  </div><p></p>
<p>And here is the branch, thanks for testing:</p><aside class="onebox githubfolder" data-onebox-src="https://github.com/mauigna06/SlicerSurfaceToolbox/tree/AddGeometryFeatureV2">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/mauigna06/SlicerSurfaceToolbox/tree/AddGeometryFeatureV2" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/mauigna06/SlicerSurfaceToolbox/tree/AddGeometryFeatureV2" target="_blank" rel="noopener nofollow ugc">GitHub - mauigna06/SlicerSurfaceToolbox at AddGeometryFeatureV2</a></h3>

  <p><a href="https://github.com/mauigna06/SlicerSurfaceToolbox/tree/AddGeometryFeatureV2" target="_blank" rel="noopener nofollow ugc">AddGeometryFeatureV2</a></p>

  <p><span class="label1">Supports various cleanup and optimization processes on surface models</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Please don’t be confused by the name of the branch, the idea of the transform maker came while I was developing the AddGeometries tool so it’s on this branch</p>
<p>Best regards,<br>
Mauro</p>

---

## Post #9 by @lassoan (2022-05-30 15:33 UTC)

<p>Thank you for the information. It seems that TransformMaker indeed does the same kind of processing (combining transforms in various ways to create new transforms) as TransformProcessor.</p>
<p>There are some advantages of adding new derived transform computations to the existing TransformProcessor module (it is a small, simple module, with a good name, with a well-defined scope, new modes can be added with little amount of code in a few existing classes; it is easier to modify the module because it is in an extension and not bundled with the Slicer core), but there are also some disadvantages (it is harder to find the module because it is in an extension; it does not use pluggable infrastructure, so if a new transformation mode is added then the changes are dispersed across a couple of files). But main main worries are:</p>
<ol>
<li>Having the same kind of features available in two completely different places means more code maintenance, documentation, user education workload.</li>
<li>Widening of Dynamic Modeler module’s scope from model editing to all kinds of processing would mean that we would effectively introduce a new module type. If we find that existing module types are too complicated/have too much overhead then we should address that issue instead of just adding yet another type.</li>
</ol>

---

## Post #10 by @mau_igna_06 (2022-05-30 16:03 UTC)

<p>Lately I’m replicating so much functionalities that already exist on Slicer… xD</p>
<p>Talking seriously, I think the ability to output markups according to the final transform appears very useful</p>

---
