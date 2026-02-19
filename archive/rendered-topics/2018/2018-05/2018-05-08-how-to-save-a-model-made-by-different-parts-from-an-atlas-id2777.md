---
topic_id: 2777
title: "How To Save A Model Made By Different Parts From An Atlas"
date: 2018-05-08
url: https://discourse.slicer.org/t/2777
---

# How to save a model made by different parts from an atlas?

**Topic ID**: 2777
**Date**: 2018-05-08
**URL**: https://discourse.slicer.org/t/how-to-save-a-model-made-by-different-parts-from-an-atlas/2777

---

## Post #1 by @marta (2018-05-08 15:26 UTC)

<p>Hello to everyone,<br>
I downloaded an atlas from the 3d slicer library and I selected the anatomical parts that interest me.</p>
<p>Now I need to save the model as an stl file. In this model every anatomical part has to be a different stl file (entity).<br>
I need this to export the model in Solidworks and see the whole model with the different anatomical parts I selected as different parts.</p>
<p>By now, I only managed to save the whole model as a single component and save every single anatomical part of interest as a model, but this is not what I need.</p>
<p>Please help me, thank you<br>
bye</p>

---

## Post #2 by @pieper (2018-05-08 22:14 UTC)

<p>Hi -</p>
<p>It’s not completely clear to me what you need, but it sounds like you want to combine multiple distinctly labeled parts of the atlas into a single stl file?  You can do this in the legacy Editor module with the Change Label effect, by changing all the label numbers of the structures of interest into the number you want them to be and then use the Model Maker to regenerate a model that you can save as stl.</p>
<p>If that’s not what you are looking for maybe you could include some screenshot images to explain.</p>
<p>Best,<br>
-Steve</p>

---

## Post #3 by @lassoan (2018-05-09 03:14 UTC)

<p>If you use Segment Editor module and a recent nightly version of Slicer then you can export all segments as a combined STL file directly - see <a href="https://discourse.slicer.org/t/save-segmentation-directly-to-stl-or-obj-files/2428">Save segmentation directly to STL or OBJ files</a></p>

---

## Post #4 by @marta (2018-05-09 07:21 UTC)

<p>Thank you Andras,<br>
the problem is that I am using an atlas and I don’t have any segmentation.</p>
<p>thank you,<br>
Bye</p>
<p>PS: the nigthly version doesn’t work in my pc. I am using the stable one.</p>

---

## Post #5 by @marta (2018-05-09 07:35 UTC)

<p>Thank you Steve!</p>
<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="2777">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>You can do this in the legacy Editor module with the Change Label effect, by changing all the label numbers of the structures of interest into the number you want them to be and then use the Model Maker to regenerate a model that you can save as stl.</p>
</blockquote>
</aside>
<p>In this way I think that the model is saved as a unique block. I need one model, but composed of different objects that are recognized by Solidworks as different “parts” of the assembly.</p>
<p>Thank you,<br>
bye</p>

---

## Post #6 by @lassoan (2018-05-09 13:23 UTC)

<aside class="quote no-group" data-username="marta" data-post="4" data-topic="2777">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/a183cd/48.png" class="avatar"> marta:</div>
<blockquote>
<p>the problem is that I am using an atlas and I don’t have any segmentation</p>
</blockquote>
</aside>
<p>If you have your segmentation in a model or labelmap node then you can convert it to a segmentation node using Segmentations module. However, from the rest of your message it seems that you actually don’t need to merge the data before exporting it, because if you do, then there is no way SolidWorks can separate them ever again.</p>
<aside class="quote no-group" data-username="marta" data-post="4" data-topic="2777">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/a183cd/48.png" class="avatar"> marta:</div>
<blockquote>
<p>the nigthly version doesn’t work in my pc. I am using the stable one</p>
</blockquote>
</aside>
<p>What operating system and graphics card do you have?</p>
<aside class="quote no-group" data-username="marta" data-post="5" data-topic="2777">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/a183cd/48.png" class="avatar"> marta:</div>
<blockquote>
<p>In this way I think that the model is saved as a unique block. I need one model, but composed of different objects that are recognized by Solidworks as different “parts” of the assembly.</p>
</blockquote>
</aside>
<p>For this, you need to export each model as a separate STL file and create your assembly in SolidWorks. Note that you might not be able to do much with imported surface meshes in SolidWorks, as by default they will not be considered solids. What is your end goal?</p>

---

## Post #7 by @marta (2018-05-09 13:55 UTC)

<p>Dear  Andras,</p>
<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="2777">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>However, from the rest of your message it seems that you actually don’t need to merge the data before exporting it, because if you do, then there is no way SolidWorks can separate them ever again.</p>
</blockquote>
</aside>
<p>This is exactly what happened when I had merged the models of the anatomical parts I am interested.</p>
<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="2777">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>you need to export each model as a separate STL file and create your assembly in SolidWorks</p>
</blockquote>
</aside>
<p>I also tried this way, but it’s impossible to position every single part in the place it belongs accurately in Solidworks.<br>
This is why I would like to know if it is possible to export a model which keeps the information about its single parts,  view them as separate.</p>
<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="2777">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What operating system and graphics card do you have?</p>
</blockquote>
</aside>
<p>I know I have some problems with my video card.</p>
<p>Thank you very much for your reply.<br>
bye</p>

---

## Post #8 by @lassoan (2018-05-09 15:15 UTC)

<aside class="quote no-group" data-username="marta" data-post="7" data-topic="2777">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/a183cd/48.png" class="avatar"> marta:</div>
<blockquote>
<p>I also tried this way, but it’s impossible to position every single part in the place it belongs accurately in Solidworks.</p>
</blockquote>
</aside>
<p>Slicer correctly exports all the models in the same coordinate system. If SolidWorks by default ignores this information then it has be resolved in SolidWorks. There might be import options or you may be able to specify that vertices of all the different parts are defined in a single coordinate system, etc. You may get answers on SolidWorks forums.</p>
<p>Have you tried if SolidWorks can do what you need after you imported parts? Can you convert the meshes to solid parts? What is the end goal? Modeling, 3D printing, or simulation? Depending on what is the end goal, you may need to generate volumetric meshes, which you export completely differently. If the goal is 3D printing, then you may do some more modeling in Slicer and finish up with more suitable modelers than SolidWorks, such as Autodesk Fusion 360, MeshMixer, Blender, etc.</p>

---

## Post #9 by @marta (2018-05-11 09:12 UTC)

<p>Dear Andras, thank you very much for your help.<br>
You’re right. The goal is 3d printing and I need to change modellation software.</p>
<p>Thank you again!<br>
bye</p>

---

## Post #10 by @lassoan (2018-05-13 13:37 UTC)

<p>You may find it useful that in recent nightly versions of Slicer, you can export segmentation directly to a single OBJ file, with correct colors: <a href="https://discourse.slicer.org/t/save-segmentation-directly-to-stl-or-obj-files/2428">Save segmentation directly to STL or OBJ files</a></p>

---

## Post #11 by @marta (2018-05-16 07:22 UTC)

<p>Thank you Andras! <img src="https://emoji.discourse-cdn.com/twitter/blush.png?v=5" title=":blush:" class="emoji" alt=":blush:"></p>

---

## Post #12 by @mukatyz (2018-05-16 14:23 UTC)

<p>Why Marta?</p>
<details>
<summary>
Spanish original</summary>
<p>por qué marta?</p>
</details>

---
