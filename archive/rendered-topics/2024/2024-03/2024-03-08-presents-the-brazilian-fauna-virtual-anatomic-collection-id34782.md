# Presents the 'Brazilian Fauna Virtual Anatomic Collection'

**Topic ID**: 34782
**Date**: 2024-03-08
**URL**: https://discourse.slicer.org/t/presents-the-brazilian-fauna-virtual-anatomic-collection/34782

---

## Post #1 by @Rafael_V_Monteiro (2024-03-08 15:22 UTC)

<p>Operating system: Ubuntu 22.04.3 LTS (GNU/Linux 6.5.0-21-generic x86_64)<br>
Slicer version: 5.6.0</p>
<p>Greetings Slicer community!</p>
<p>I am here to share the success of using Slicer3D to build our Brazilian Fauna Virtual Anatomic Collection, from University Federal of Juiz de Fora (UFJF) - MG, Brazil, hosted at:</p>
<p><a href="https://www2.ufjf.br/anatovirtualbrasil/" rel="noopener nofollow ugc">CAVFB institutional page</a> (in Brazilian Portuguese).</p>
<p><a href="http://200.17.71.18/" rel="noopener nofollow ugc">Collection access</a> (English/Brazilian Portuguese)</p>
<p>There are many Brazilian wild animls species threatened by agricultural production, deforestation, chemical pollution, diseases and human intervention. However, such huge species diversity lacks proper documentation in the scientific literature, as many species are unknown in their simplest aspects, as anatomic bone features. In many cases, skeletons and bones are available in Biological Collections, maintained by numerous institutions, in Brazil or abroad. To consult or handle these collections’ valuable biological samples in person, visits are required, as well the authorization from the collections’ curators. Both requirements might be difficult to fulfill, as long expensive travels and/or absence of a considered proper purpose may hinder such access.</p>
<p>Our virtual collection was designed to meet these requirements for anyone who wants to know, study or simply hold bones and skeletons of Brazilian fauna: we exibhit these osteological structures online as 3D models, which are created from wild animals carcasses officially handed over to us by Brazilian governamental environment agencies. Such 3D models are freely downloadable as files fit to be printed.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a06a34f86eee74e2d40c27d41050dbe6c2ab7a0e.jpeg" data-download-href="/uploads/short-url/mT5Wr7yhgobTjkbo3qXqnF0yVaK.jpeg?dl=1" title="2024-03-08 (1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a06a34f86eee74e2d40c27d41050dbe6c2ab7a0e_2_690x470.jpeg" alt="2024-03-08 (1)" data-base62-sha1="mT5Wr7yhgobTjkbo3qXqnF0yVaK" width="690" height="470" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a06a34f86eee74e2d40c27d41050dbe6c2ab7a0e_2_690x470.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a06a34f86eee74e2d40c27d41050dbe6c2ab7a0e_2_1035x705.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a06a34f86eee74e2d40c27d41050dbe6c2ab7a0e.jpeg 2x" data-dominant-color="E8EBEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2024-03-08 (1)</span><span class="informations">1272×867 280 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>All this would be unatainable if wasn’t by Slicer3D and other companion apps. Our collection project started as an idea without tools. In the course of the last two and a half years I had become acquainted with Slicer3D software. Although I knew about it, internet research has made clear for me that it was the right tool to the task ahead: 3D bone modelling and segmentation. After this, the challenge was how to properly show 3D models online in a pleasing and scientific way.</p>
<p>It was all sorted out when I learned about OpenAnatomyExport module and Online3Dviewer website, which I am adapting to our purposes. These two tools were a game changer for displaying our models. I also adapted scripts from Slicer script repository for generating models of the topographic features of the bones. Such acomplishments would not be achieved without Slicer3D community, whose help is most thanked.</p>
<p>Today, our research team includes me, four professors from University Federal de Juiz de Fora, and three graduate students. Past those almost three years of project, five other students had participated on this research project. We are presenting a paper in a national engineering congress in Brazil, and expect produce and help others to produce good scientific data about Brazilian wild fauna.</p>
<p>Best regards,</p>
<p>Prof. PhD. DVM Rafael V Monteiro</p>
<p>CAVFB Curator</p>

---

## Post #2 by @muratmaga (2024-03-09 03:47 UTC)

<p>Thanks for sharing this. Looks like you guys have done a great start, looking forward to seeing the increased diversity. I do have couple comments/suggestions.</p>
<ol>
<li>If you can please register your server, and provide a fully qualified domain name. IP address only servers may cause issue with firewalls and proxies in unexpected ways.</li>
<li>It would be great if you can provide some specimen collection information, as well as imaging modality used and the underlying data (since these all appear as segmented models).</li>
<li>Some of the samples are fairly heavily decimated, which I believe is done to increase the interactivity of the 3D scene. But unfortunately it caused holes and rips (eg. scapula and ischium in the marmoset). You may want to selectively decimate the models.</li>
</ol>
<p>While these interactive models are useful as teaching aids/visuals, and can possibly used for 3D printing, the label data (segmentation), is probably far more high resolution than these. We are starting a new project to make exchanging such label data more easily. Would you be interested in contributing your segmentation to that?</p>
<p>Again, great work. Glad that Slicer and other open-source tools have been useful for your project.</p>

---

## Post #3 by @tsehrhardt (2024-03-09 18:28 UTC)

<p>Love this! One thing you can do is add hierarchies so users can toggle the visibility of groups of bones as well–this works well with 3Dviewer. I have done this by adding “empties” to the glb/gltf in Blender and parenting each empty to the relevant bones. You can even have nested empties as shown in my attached image.</p>
<p>Happy to help you out with that if you’re interested.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/eee5e2aa7147086d3a5ffce51ec496fcb62a86f0.jpeg" data-download-href="/uploads/short-url/y5oaf0aRuFd7g50dYZSh0wQbeCs.jpeg?dl=1" title="2024-03-09_13-23-45" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eee5e2aa7147086d3a5ffce51ec496fcb62a86f0_2_690x438.jpeg" alt="2024-03-09_13-23-45" data-base62-sha1="y5oaf0aRuFd7g50dYZSh0wQbeCs" width="690" height="438" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eee5e2aa7147086d3a5ffce51ec496fcb62a86f0_2_690x438.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eee5e2aa7147086d3a5ffce51ec496fcb62a86f0_2_1035x657.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eee5e2aa7147086d3a5ffce51ec496fcb62a86f0_2_1380x876.jpeg 2x" data-dominant-color="2E2F33"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2024-03-09_13-23-45</span><span class="informations">2400×1526 209 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2024-03-09 18:37 UTC)

<p>Indeed, hierarchy is very useful! OpenAnatomy export module preserves the subject hierarchy in the exported model, so you can create the hierarchy in Slicer (right-click to create folders and drag-and-drop models into them in the Data module) and export glTF with hierarchy by a single click.</p>

---

## Post #5 by @rkikinis (2024-03-09 18:37 UTC)

<p><a href="https://ta2viewer.openanatomy.org/?id=3932" class="onebox" target="_blank" rel="noopener nofollow ugc">https://ta2viewer.openanatomy.org/?id=3932</a><br>
This is an example using TA2 human anatomy</p>

---

## Post #6 by @tsehrhardt (2024-03-09 21:47 UTC)

<p>That’s good to know. Thanks!</p>

---

## Post #7 by @Rafael_V_Monteiro (2024-03-10 12:59 UTC)

<p>Thank you, sir, for your kind message, compliments and comments.<br>
Regarding your suggestions:</p>
<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="34782">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>If you can please register your server, and provide a fully qualified domain name. IP address only servers may cause issue with firewalls and proxies in unexpected ways.</p>
</blockquote>
</aside>
<p>I am aware of those issues you mentioned, and I am ensuring that the University IT department registers the domain, as this IP number is a governamental one.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="34782">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>It would be great if you can provide some specimen collection information, as well as imaging modality used and the underlying data (since these all appear as segmented models).</p>
</blockquote>
</aside>
<p>I am gradually adapting the 3Dviewer template to display such data, as well statistics about the segments. I am confident that I will achieve this soon .</p>
<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="34782">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Some of the samples are fairly heavily decimated, which I believe is done to increase the interactivity of the 3D scene. But unfortunately it caused holes and rips (eg. scapula and ischium in the marmoset). You may want to selectively decimate the models.</p>
</blockquote>
</aside>
<p>We define a minimum Hounsfield Unit (HU) for each specimen’s DICOM images to be segmented. This minimum HU range around 150-200 HU units, above which everything will be considered bone. The holes and rips are due to presence of cancellous bone in those regions. If we lower the HU limit, many non-bone structures will bem included in the ‘skeleton’, such as tendons, salivary glands, stomach content and so on. Thus, we decided to allow these ‘failures’ as a demonstration of how calcification may vary among the species.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="34782">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Would you be interested in contributing your segmentation to that?</p>
</blockquote>
</aside>
<p>Absolutely! You may message me in private, perhaps?</p>
<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="34782">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Glad that Slicer and other open-source tools have been useful for your project.</p>
</blockquote>
</aside>
<p>As a researcher from a developing country I strongly believe in FOSS, which use allow me to try to level the game. This project is a result of this.</p>
<p>Best regards!</p>

---

## Post #8 by @Rafael_V_Monteiro (2024-03-10 13:11 UTC)

<p>Than you for your message, compliments and suggestions.<br>
I would like to add hierarchy to the segmentations, but I could not do that.<br>
My unsuccesful steps:</p>
<ol>
<li>In the data module, right-click over the segmentation name, select ‘Add child folder’.</li>
<li>However, the added folder does not allow any segment to be dragged in, as shown bellow (blue folder).</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/890409afdb64f99d0d73364bc87ef56ba35c272e.png" data-download-href="/uploads/short-url/jy63ZS6qUAFBXF0IQCIv304ctYi.png?dl=1" title="2024-03-10" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/890409afdb64f99d0d73364bc87ef56ba35c272e_2_471x500.png" alt="2024-03-10" data-base62-sha1="jy63ZS6qUAFBXF0IQCIv304ctYi" width="471" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/890409afdb64f99d0d73364bc87ef56ba35c272e_2_471x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/890409afdb64f99d0d73364bc87ef56ba35c272e_2_706x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/890409afdb64f99d0d73364bc87ef56ba35c272e.png 2x" data-dominant-color="DFE0DF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2024-03-10</span><span class="informations">936×993 77.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>What am  I doing wrong?</p>
<p>Again, thank you, best regards,</p>

---

## Post #9 by @Rafael_V_Monteiro (2024-03-10 13:13 UTC)

<p>Thank you for your suggestion. I tried it, but had no success. Please see previous reply, the added child folder does not allow any segment to be dragged in it.</p>
<p>What am I doing wrong?<br>
Best regards,</p>

---

## Post #10 by @Rafael_V_Monteiro (2024-03-10 13:14 UTC)

<p>Thank you, I´ll try to accomplish that.<br>
Best regards,</p>

---

## Post #11 by @pieper (2024-03-10 15:43 UTC)

<p>Thank you <a class="mention" href="/u/rafael_v_monteiro">@Rafael_V_Monteiro</a> for sharing this valuable project <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<aside class="quote no-group" data-username="Rafael_V_Monteiro" data-post="7" data-topic="34782">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rafael_v_monteiro/48/16558_2.png" class="avatar"> Rafael_V_Monteiro:</div>
<blockquote>
<p>The holes and rips are due to presence of cancellous bone in those regions.</p>
</blockquote>
</aside>
<p>Yes, this is a very interesting aspect of the data and worth visualizing.  I think the new ColorizeVolume method would be good with this data and you could use it to make movies to accompany the 3D surface models.  If we like it, it should also be possible at some point to port this method to run natively in the browser.</p>
<aside class="quote quote-modified" data-post="6" data-topic="26689">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/volume-rendering-colorized-with-segmentation/26689/6">Volume rendering colorized with segmentation</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Yes, exactly. 
This image uses the CT as alpha, so you get nice detail with the coloring, but we should also do the option where the segmentation opacity controls the alpha channel.  We’ll need to do the local smoothing / surface fitting in the GPU using the segmentation and the color from the lookup table.  This should be effectively the same as building a surface model but faster and with some extra options. 
I agree we should think about how we should handle volume rendering from a UI perspe…
  </blockquote>
</aside>

<aside class="quote quote-modified" data-post="22" data-topic="31981">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/vtk-multivolume-cinematic-volume-rendering/31981/22">VTK multivolume/cinematic volume rendering</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    OMG! This is a game changer for us. 
We just now a way to adjust TF per segment basis somehow… And regular shadows/lights work great, just need the ambient shadows as <a class="mention" href="/u/lassoan">@lassoan</a> mentioned. 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c5a532f77905930b10be6ff74d8539992e8f41f.jpeg" data-download-href="/uploads/short-url/fsx5oPUeuKWjMlnEJT2FAT5MqlN.jpeg?dl=1" title="image" rel="noopener nofollow ugc">[image]</a>
  </blockquote>
</aside>


---

## Post #12 by @lassoan (2024-03-11 03:17 UTC)

<aside class="quote no-group" data-username="Rafael_V_Monteiro" data-post="9" data-topic="34782">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rafael_v_monteiro/48/16558_2.png" class="avatar"> Rafael_V_Monteiro:</div>
<blockquote>
<p>Thank you for your suggestion. I tried it, but had no success. Please see previous reply, the added child folder does not allow any segment to be dragged in it.</p>
</blockquote>
</aside>
<p>Unfortunately, you cannot create folders within a segmentation node. Instead you can export the segmentation to models (by two clicks in Data module, using the right-click menu) and you can then drag-and-drop those models.</p>
<aside class="quote no-group" data-username="Rafael_V_Monteiro" data-post="7" data-topic="34782">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rafael_v_monteiro/48/16558_2.png" class="avatar"> Rafael_V_Monteiro:</div>
<blockquote>
<p>The holes and rips are due to presence of cancellous bone in those regions</p>
</blockquote>
</aside>
<p>I agree with <a class="mention" href="/u/pieper">@pieper</a> that there are much, much better ways to indicate bone density than corrupting the segmentation with artifacts. The good news is that if you still have the segmentations then you may be able to fix some of these segmentation errors automatically using Wrap Solidify effect.</p>
<p>You can decide later if you want to show bone density and how (changing surface mesh transparncy, colors, etc., or use colored volume rendering when visualizing the scene in capable software, such as Slicer). You can show surface models in the browser by default but you could add an “Open in 3D Slicer” button that opens the 3D model directly in Slicer on your computer (using <code>slicer://</code> custom URL protocol, as implemented during the last project week, or by simply adding a download link to a .mrb file).</p>

---

## Post #13 by @muratmaga (2024-03-11 05:19 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="34782">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>se segmentation errors automatically using Wrap Solidify effect.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/rafael_v_monteiro">@Rafael_V_Monteiro</a><br>
Here is an example how Colorize Volumes module can be used in junction with segmentation to give better rendering. You can find the <code>Colorize Volume</code> in Sandbox extension:</p>
<p>Unlike its segmentation, you can control how much of the bone resorption in the mandible to be visible in the volume rendering.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/354744520c893b58555cffaf66ea891a90a84074.jpeg" data-download-href="/uploads/short-url/7BjZEUpNDIZ61lVhdExYhXqVqug.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/354744520c893b58555cffaf66ea891a90a84074_2_690x432.jpeg" alt="image" data-base62-sha1="7BjZEUpNDIZ61lVhdExYhXqVqug" width="690" height="432" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/354744520c893b58555cffaf66ea891a90a84074_2_690x432.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/354744520c893b58555cffaf66ea891a90a84074_2_1035x648.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/354744520c893b58555cffaf66ea891a90a84074_2_1380x864.jpeg 2x" data-dominant-color="AEB3C2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1203 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>vs</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5cb329839eb2736c92ae95078f2b2aebb96f77d0.jpeg" data-download-href="/uploads/short-url/de3Mo2LUtaq7wh688NOFcf3ZcUE.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cb329839eb2736c92ae95078f2b2aebb96f77d0_2_690x463.jpeg" alt="image" data-base62-sha1="de3Mo2LUtaq7wh688NOFcf3ZcUE" width="690" height="463" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cb329839eb2736c92ae95078f2b2aebb96f77d0_2_690x463.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cb329839eb2736c92ae95078f2b2aebb96f77d0_2_1035x694.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cb329839eb2736c92ae95078f2b2aebb96f77d0_2_1380x926.jpeg 2x" data-dominant-color="AFB3B7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1289 160 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #14 by @Rafael_V_Monteiro (2024-03-11 21:41 UTC)

<p>Hi Steve, thank you for your great remarks.<br>
I will experiment with ColorizeVolume to see if I reach a so nice model you posted in the link. I agree that alpha values (i.e. opacity) should be used to express bone density, if I understood correctly the proposal.<br>
I believe that is related to what causes the 3Dviewer measure tool to not work properly when I use transparency in the segments, with the objective of allowing bones’ canals and sinuses to be seen. The measure tool set the markers behind the structures and not in front.<br>
I have much to learn of Slicer, and your comments and links will help me to go in the right direction, thank you.</p>
<p>Best regards,</p>

---

## Post #15 by @Rafael_V_Monteiro (2024-03-11 21:45 UTC)

<p>Hi Andras, I will follow your hints. Thank you for the help to put me in the right direction.<br>
Best regards,</p>

---

## Post #16 by @Rafael_V_Monteiro (2024-03-11 21:46 UTC)

<p>Great hint Murat! I will explore that. Let´s keep in touch.<br>
Best,</p>

---

## Post #17 by @lassoan (2024-03-12 12:22 UTC)

<aside class="quote no-group" data-username="Rafael_V_Monteiro" data-post="14" data-topic="34782">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rafael_v_monteiro/48/16558_2.png" class="avatar"> Rafael_V_Monteiro:</div>
<blockquote>
<p>I believe that is related to what causes the 3Dviewer measure tool to not work properly when I use transparency in the segments, with the objective of allowing bones’ canals and sinuses to be seen</p>
</blockquote>
</aside>
<p>It is not well defined what should be the behavior when you click on a transparent surface - whether you want to pick the 3D position on the first surface (regardless of transparency), the first surface above a certain transparency threshold, the first surface where a certain cumulative opacity is reached, the first opaque surface, etc.</p>
<p>If you want to do measurements in a surface mesh based software then the best is not to use transparency (just clip or hide objects that occlude the view).</p>
<p>If you use 3D Slicer then you can do the same - measure on surfaces, or you can use colorized volume rendering. In volume rendering, opacity is continuously accumulated along each viewing ray - not just object boundaries - and the picked 3D position us where this opacity reaches 50%, which usually picks the 3D position you would expect.</p>

---

## Post #18 by @Rafael_V_Monteiro (2024-03-13 13:09 UTC)

<p>Got the problems. I have to think if it is functional to reopen a no-transparency model when user click on measure tool.<br>
But I certainly will have a try in the ColorizeModel to address these questions.<br>
Thank you very much, best regards,<br>
Rafa</p>

---
