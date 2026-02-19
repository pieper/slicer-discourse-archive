---
topic_id: 29213
title: "3D Slicer Linked To Blender"
date: 2023-04-30
url: https://discourse.slicer.org/t/29213
---

# 3D Slicer linked to Blender

**Topic ID**: 29213
**Date**: 2023-04-30
**URL**: https://discourse.slicer.org/t/3d-slicer-linked-to-blender/29213

---

## Post #1 by @yun_zou (2023-04-30 08:16 UTC)

<p>I want to know how to make 3dslicer and blender connect and interact in real time. For example: if I drag any view in 3dslicer, the three view planes in blender will also move accordingly. The model in blender can also be synchronized to 3dslicer.<br>
I’m a novice and my English is not very good. Hope to get an answer. Thanks</p>

---

## Post #2 by @lassoan (2023-04-30 13:53 UTC)

<p>See this topic for some work on this:</p>
<aside class="quote quote-modified" data-post="1" data-topic="14818">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/talmazov/48/3966_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/openplan-linking-3d-slicer-with-blender/14818">openPlan (linking 3D Slicer with Blender)</a> <a class="badge-category__wrapper " href="/c/community/12"><span data-category-id="12" data-drop-close="true" class="badge-category " title="Community information and project/topic sub-forums."><span class="badge-category__name">Community</span></span></a>
  </div>
  <blockquote>
    <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8a4413733b9f261d914216f00537a80381aa9ee.jpeg" data-download-href="/uploads/short-url/uUv2XImiCXgiM9TrsH8VP747Rfg.jpeg?dl=1" title="image" rel="noopener nofollow ugc">[image]</a> 
Hello community members, 
I’ve been holding out making this post but I think our project is ready to reach a broader audience of users and developers alike. I hope with this post to expose openPlan to the community of users and developers, and hopefully drive some interest. openPlan is open source and will always will be, as its capabilities are made possible by the openness of the 3D Slicer and Blender communities alike. 
What is openPlan? 
This is an addon extension that bridges func…
  </blockquote>
</aside>

<p>How do you know envision using Blender with Slicer? For what purpose? What features of Blender you miss when you work in Slicer?</p>

---

## Post #3 by @yun_zou (2023-05-01 02:30 UTC)

<p>Thank you for your reply. I recently came to know that blender and 3dslicer can be used together. I am an engineering major, and I have a good understanding of industrial 3D software and medical 3D software such as mimics, and I can use them proficiently for creation.<br>
I am currently working in the medical industry, and I can see more possibilities from these two software, 3dslicer’s medical 3D reconstruction and blender’s open creation, which can bring many innovations in dentistry and orthopedics, for example.<br>
I also saw the link you sent about openplan. First of all, his GitHub link is invalid, and I can’t find it (or it may not be opened because of my region). Secondly, there is a GitHub link of linkSlicerBlender in the comment area of this link. I also tried it. There is no related function command button in my blender.<br>
I am focusing on blenderfordental recently, for me, I can use it to do many things, not only the digital design of dental care</p>

---

## Post #4 by @pieper (2023-05-01 12:26 UTC)

<p>It’s great that you are working on this <a class="mention" href="/u/yun_zou">@yun_zou</a> , and I agree there is great potential.  In my experience most of the links between Slicer and Blender have been very experimental, and may not have been maintained for easy use so you may need to study closely and fill in some missing pieces.  If you can find a way to make the connection robust and easy to use I think a lot of people will benefit.  It would be good to pick a specific task and try working through the detail.  As suggestion perhaps high quality Blender rendering or animation of models generated in Slicer would be a very useful utility.</p>

---

## Post #5 by @hherhold (2023-05-01 13:53 UTC)

<p>I use Blender for animations and print-resolution renderings. Right now my workflow is to segment, create models, export as PLY, import to blender, surface, and render. I’ve thought that the segment → blender step is currently a bottleneck (for me, at least); it would be nice to have some way of passing models easily to Blender.</p>
<p>Just a thought.</p>

---

## Post #6 by @lassoan (2023-05-01 22:21 UTC)

<p><a href="https://github.com/PerkLab/SlicerOpenAnatomy">SlicerOpenAnatomy extension</a> can export segmentation to files (OBJ or glTF) in bulk, with some additional post-processing, by a single click.</p>
<p>If there are any extras step that you usually perform (reorientation, scaling, coloring, …?) when you export then those could be added to the exporter as optional processing. Even starting Blender and loading the exported models could be an optional step in the end. <a href="https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html">Blender can accept a Python script that it runs at startup</a>, so if the import is not trivial (it require many clicks) then even that can be fully automated.</p>
<p>You probably only need a sophisticated link if you want real-time updates in Blender (e.g., updating already loaded models or transforms continuously) or you want two-way synchronization between Slicer and Blender. However, there are very few people who are familiar with both Blender and Slicer, so it could be hard to justify the investment into developing and maintaining such a link.</p>

---

## Post #7 by @hherhold (2023-05-03 12:04 UTC)

<p>Is there any particular reason for the emphasis on OBJ over PLY? I’ve found OBJ files a lot harder to work with.</p>

---

## Post #8 by @talmazov (2023-07-10 22:57 UTC)

<p>the github repo has been updated and made publicly available, enjoy this open source tech and feel free to learn and build upon it<br>
much was learned in the process and I hope it will serve as a good source of knowledge for everyone</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/dentsoft-foundation/openPlan">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/dentsoft-foundation/openPlan" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/277;"><img src="https://repository-images.githubusercontent.com/283867286/19de3b00-1098-11eb-9cfe-b6815f3d2188" class="thumbnail" width="690" height="277"></div>

<h3><a href="https://github.com/dentsoft-foundation/openPlan" target="_blank" rel="noopener nofollow ugc">GitHub - dentsoft-foundation/openPlan: openPlan is a comprehensive solution...</a></h3>

  <p>openPlan is a comprehensive solution for object linking and medical imaging visualization between Blender and 3D Slicer. - GitHub - dentsoft-foundation/openPlan: openPlan is a comprehensive solutio...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #9 by @lassoan (2023-07-12 03:50 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="7" data-topic="29213" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>Is there any particular reason for the emphasis on OBJ over PLY? I’ve found OBJ files a lot harder to work with.</p>
</blockquote>
</aside>
<p>I agree that PLY file format is better, but more people ask for OBJ. I think it is because OBJ file format is used more commonly for gaming, therefore game engines, such as Unity support it better. People who implement medical applications using gaming engines usually want OBJ.</p>

---

## Post #10 by @Young_Wang (2024-03-18 12:11 UTC)

<p>this is exactly what I’m looking for. I also came across a previous link <a href="https://discourse.slicer.org/t/openplan-linking-3d-slicer-with-blender/14818/16" class="inline-onebox">openPlan (linking 3D Slicer with Blender) - #16 by talmazov</a>, it included a youtube link which is now invalid. Anyone else found a valid link to view the demo.</p>

---

## Post #11 by @talmazov (2024-03-19 01:28 UTC)

<p>hey, much apologies for the broken youtube link.<br>
here is an updated link to the demo video <a href="https://youtu.be/TMCDoHegnAs" rel="noopener nofollow ugc">https://youtu.be/TMCDoHegnAs</a></p>
<p>in the demo i use blender addons: open dental cad, object alignment, openPlan</p>

---

## Post #12 by @Young_Wang (2024-03-19 04:30 UTC)

<p><a class="mention" href="/u/talmazov">@talmazov</a> wow, this is so cool and awesome, thanks for sharing. I wonder if this supports DICOM to blender? I tried a few options, so far no luck.</p>

---

## Post #13 by @talmazov (2024-03-19 18:20 UTC)

<p>openPlan/linkslicerblender allows you to link software so transformations are synced, it also allows cross-importing object data.<br>
you can segment the DICOM model in 3D Slicer and import it into blender - manually or using openPlan.<br>
alternatively, i know of one add-on that allows you to do DICOM work directly in Blender. It is <a href="https://www.blendernation.com/2019/04/06/ortogonblender-beta-for-blender-2-80-available-for-download/" class="inline-onebox" rel="noopener nofollow ugc">OrtogOnBlender beta for Blender 2.80 available for download - BlenderNation</a></p>

---

## Post #14 by @Young_Wang (2024-03-19 19:51 UTC)

<p><a class="mention" href="/u/talmazov">@talmazov</a> , thanks. I tried <a href="https://www.blendernation.com/2019/04/06/ortogonblender-beta-for-blender-2-80-available-for-download/" rel="noopener nofollow ugc">OrtogOnBlender beta for Blender 2.80 available for download - BlenderNation</a> but unfortunately, I had some difficulties running it.</p>

---

## Post #15 by @Young_Wang (2024-03-20 19:10 UTC)

<p>I also came across <a href="https://github.com/drmichaeldouglass/MedBlend" class="inline-onebox" rel="noopener nofollow ugc">GitHub - drmichaeldouglass/MedBlend: A Medical Visualisation Add-On for Blender</a>, it allows DICOM to be imported to blender for artistic changes.</p>

---
