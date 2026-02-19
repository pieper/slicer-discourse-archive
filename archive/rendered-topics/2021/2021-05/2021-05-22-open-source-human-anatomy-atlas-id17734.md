---
topic_id: 17734
title: "Open Source Human Anatomy Atlas"
date: 2021-05-22
url: https://discourse.slicer.org/t/17734
---

# Open source Human Anatomy Atlas

**Topic ID**: 17734
**Date**: 2021-05-22
**URL**: https://discourse.slicer.org/t/open-source-human-anatomy-atlas/17734

---

## Post #1 by @Melodicpinpon (2021-05-22 15:44 UTC)

<p>Hello everybody,</p>
<p>You may like to see the first steps towards what should become a full open source 3D human anatomy atlas; you can now download the .blend files (Blender offers great options to organize and visualize these files) at <a href="https://www.z-anatomy.com/" rel="noopener nofollow ugc">https://www.z-anatomy.com/</a>.</p>
<p>To be kept informed, you can follow the ‘z-anatomy’ linkedin and facebook pages.<br>
It is just the beginning; the files will be updated regularly.</p>
<p>All comments are welcome,</p>
<p>g.</p>

---

## Post #2 by @manjula (2021-05-22 18:03 UTC)

<p><a class="mention" href="/u/melodicpinpon">@Melodicpinpon</a> I think it was very good and a lot of hard work has been put into it. Thank you and I will share this with my colleagues. Congratulations to you and the team on your great work.</p>
<p>As a suggestion, moving forward may need to simplify the navigation for users not familiar with Blender. is there a Slicelet like an option for blender?</p>

---

## Post #3 by @Melodicpinpon (2021-05-24 08:12 UTC)

<p>Hi Manjula,</p>
<p>It is possible to import a .dicom converted into a pile of images (.jpg/.png) and to apply a boolean operation with a cube to get a similar effect, and even to reproduce the MPR effect with a simple node setup and a script. Using images on their original plane, definitely yes.</p>
<p>For the meshes, it is very different; although it is possible to reproduce something comparable to a slice-scroll function with orthographic views and the ‘clip start’ option of the view menu; every virtual plane created by the slicing through the mesh would be empty and let appear the inner side of the surface of the object; the system would be a hack and have several serious disadvantages compared to a regular .dicom viewer (glitchy, slow, heavy computing…).</p>
<p>Clipping border (Alt+B) allows to get a rapid slicing effect but it is not editable; each clipping box must be done one at a time. (<a href="https://www.linkedin.com/feed/update/urn:li:activity:6794333683412287488" class="inline-onebox" rel="noopener nofollow ugc">Z-Anatomy on LinkedIn: Demo fonctions de base</a>)</p>
<p>I take good note of your question and will investigate; it would be a great option.<br>
Maybe with nodes.</p>

---

## Post #4 by @Melodicpinpon (2021-05-24 08:43 UTC)

<p>I contacted Cicero Moraes that works much linking .dicoms and Blender to ask him the question.<br>
You can see his work when searching  ‘Orthogonblender’.</p>

---

## Post #5 by @Melodicpinpon (2021-08-23 19:26 UTC)

<p>Hi everyone!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f875a2941b957faaa91770f8e54fa2b6239e6be4.jpeg" data-download-href="/uploads/short-url/zrYrzeXcSaXEkGP8XrC3fUbbzUM.jpeg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f875a2941b957faaa91770f8e54fa2b6239e6be4_2_500x500.jpeg" alt="2" data-base62-sha1="zrYrzeXcSaXEkGP8XrC3fUbbzUM" width="500" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f875a2941b957faaa91770f8e54fa2b6239e6be4_2_500x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f875a2941b957faaa91770f8e54fa2b6239e6be4_2_750x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f875a2941b957faaa91770f8e54fa2b6239e6be4.jpeg 2x" data-dominant-color="E3D6D2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">960×960 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a56a6fd4d86914345f726da18ef6ab304b882290.png" data-download-href="/uploads/short-url/nBkOZI32ZmMefZkqHc1QtxBnkmQ.png?dl=1" title="5" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a56a6fd4d86914345f726da18ef6ab304b882290_2_500x500.png" alt="5" data-base62-sha1="nBkOZI32ZmMefZkqHc1QtxBnkmQ" width="500" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a56a6fd4d86914345f726da18ef6ab304b882290_2_500x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a56a6fd4d86914345f726da18ef6ab304b882290_2_750x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a56a6fd4d86914345f726da18ef6ab304b882290.png 2x" data-dominant-color="976B47"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">5</span><span class="informations">960×960 1.16 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/709f1fdf5b02f2b2ad1321cfe706e5900f3ac7c2.png" data-download-href="/uploads/short-url/g4ioL9rLqQkrhEoWVrpN3rg3H1g.png?dl=1" title="11" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/709f1fdf5b02f2b2ad1321cfe706e5900f3ac7c2_2_500x500.png" alt="11" data-base62-sha1="g4ioL9rLqQkrhEoWVrpN3rg3H1g" width="500" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/709f1fdf5b02f2b2ad1321cfe706e5900f3ac7c2_2_500x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/709f1fdf5b02f2b2ad1321cfe706e5900f3ac7c2_2_750x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/709f1fdf5b02f2b2ad1321cfe706e5900f3ac7c2.png 2x" data-dominant-color="977651"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">11</span><span class="informations">960×960 822 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8bfe8b44be717c170cc56291dd03430897c01edb.png" data-download-href="/uploads/short-url/jYrJ2pQdhLt58lVAS3W8fXDWH91.png?dl=1" title="20" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8bfe8b44be717c170cc56291dd03430897c01edb_2_500x500.png" alt="20" data-base62-sha1="jYrJ2pQdhLt58lVAS3W8fXDWH91" width="500" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8bfe8b44be717c170cc56291dd03430897c01edb_2_500x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8bfe8b44be717c170cc56291dd03430897c01edb_2_750x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8bfe8b44be717c170cc56291dd03430897c01edb.png 2x" data-dominant-color="9A745A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20</span><span class="informations">960×960 574 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I write back about this project because the file is improving regularly:<br>
<a href="https://www.z-anatomy.com/" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.z-anatomy.com/</a><br>
It is worth downloading the latest version from time to time.</p>
<p>To be kept informed of the updates, the linkedin page can be followed:<br>
<a href="https://www.linkedin.com/company/z-anatomy" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.linkedin.com/company/z-anatomy</a></p>

---

## Post #6 by @lassoan (2021-08-23 19:54 UTC)

<p>Thanks for sharing, this looks really nice!</p>
<p>Blender file format is not a data archival or exchange file format. There is not even a formal specification of the this file format, it is subject to change any time, any way without notice, it is just whatever is currently implemented in Blender (very much the same way as Slicer’s scene file format). It would be important to make the models available in a standard file format, such as glTF, PLY, OBJ, or even VRML so that it can be used in other software, such as Slicer, OpenAnatomy, OpenSim, …</p>
<p>For example, we could easily import the atlas from any of the standard file formats into Slicer (but not from Blender), including textures, and register that to real patient images, even with non-linear warping. Or, we could edit the atlas to be able to create models from the most common normal and pathological variations from patient images.</p>

---

## Post #7 by @pieper (2021-08-23 20:08 UTC)

<p>I agree, the anatomy data looks great <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=10" title=":+1:" class="emoji" alt=":+1:"></p>
<p>I’d suggest exporting them <a href="https://graphics.pixar.com/usd/docs/index.html">in USD format</a>, which will be easy since there already <a href="https://docs.blender.org/manual/en/latest/files/import_export/usd.html">an exporter for Blender</a>.  USD is becoming very popular for this kind of data for content creation.  We should look into making USD import/export tools for Slicer.  It might be possible to put some of the functionality in VTK, but probably it’s cleanest to work at the application level.</p>
<p>USD is also the basis for Nvidia’s <a href="https://developer.nvidia.com/nvidia-omniverse-platform">Omniverse</a>.  We may or may not want to use Omniverse but it indicates momentum behind USD and at least some level of maturity across platforms.</p>

---

## Post #8 by @lassoan (2021-08-23 21:31 UTC)

<p>USD looks great. I wanted to like glTF but always remained somewhat uncomfortable with how rigid the format is and much the hardware representation and efficient implementation dictates everything. USD seems to operate at higher level concepts and supports references, layers, inheritance, user-level metadata, temporary hiding of primitives, etc. - all things that are extremely valuable for anatomical atlases. I’ve just read that Blender got a USD importer, too, so now you can do round-trip editing not just in Blender but other software, too.</p>

---

## Post #9 by @lassoan (2021-08-24 01:41 UTC)

<p><a class="mention" href="/u/melodicpinpon">@Melodicpinpon</a> FYI, I’ve tried the atlas and it was a bit hard for me to use it. Maybe my feedback can be useful for you:</p>
<ul>
<li>Higher than expected hardware requirements: It needs desktop computer or gaming laptop. My relatively strong Intel i7 ultrabook with 16GB RAM, and Intel Iris Plus Graphics could not handle it (I could barely rotate the viewin Blender, physical memory usage was near 100%). My desktop with an i7 CPU, 32GB RAM, RTX 2080 could load the model without problems, but everything was still sluggish. =&gt; For authoring/editing it could be OK to require 32 GB RAM and desktop class GPU, but for users you would need to create decimated models (preferable by about a factor of 10x).</li>
<li>There are a number of extra setup steps to adjust the application preferences. Some of them persistently change the preferences, so it somebody uses Blender for other purposes then he has to switch between the regular settings and the Z-anatomy recommended settings. Loading and setup of an atlas should be simpler.</li>
<li>Hard to navigate. Keyboard shortcuts help (without that I could not do anything), but not granular enough (just show/hide 6-8 major categories). I also found it hard (could not really figure out even in the end) why items does not show up if I open the eye icon (and all parents’ eye icons). When I right-clicked and choose to show all items inside then it worked. I also found that it was almost impossible to use it with a touchpad (I would have needed the middle button or reconfigure keyboard shortcuts). It is mostly just the complexity of Blender, which is justified if you want to edit the model, but just for viewing feels too difficult. =&gt; Instead of using Blender for distribution, it would be better to use a simpler viewer. Virtual reality support in the viewer is essential, interacting in with a mouse and keyboard on a 2D screen is just painful compared to having two 6-DOF controllers in an immersive 3D environment. You can get a standalone Oculus Quest for $300, which should easily handle visualization of surface meshes and image cross-sections. A simple application that shows meshes and images like the <a href="https://www.openanatomy.org/atlas-pages/">OpenAnatomy web viewer</a> would be sufficient, but it with virtual reality support.</li>
<li>I was not able to show labels with callouts, as I saw it on some screenshots.</li>
<li>Some anatomy seem to be missing. For example, I could not visualize the lymphatic system. =&gt; It would be nice to document the list of known issues/missing parts clearly, near the download link, so that users know what to expect.</li>
<li>Scalability: Management of even this single specimen is quite complicated. I don’t know how would you incorporate anatomical variations, pathologies, different taxonomies, coordinate systems, manage versioning, accept additions or change requests from others, keeping the models in sync with various other anatomical atlases, how could you correlate the meshes with ground truth data (CT, MRI, ultrasound, cryosections, etc.). =&gt; This is obviously very difficult, would take a lot of work, but coordinating with OpenAnatomy project or other open efforts should help. Projects could share common data model (USD?), desktop and web viewer, authoring tools (Blender, 3D Slicer), etc.</li>
</ul>

---

## Post #10 by @Melodicpinpon (2021-08-25 03:42 UTC)

<p>The .blend files are indeed meant to be used in Blender. They offer many interesting options (colors, complex organisation, between others that could be useful for anatomy). All versions of Blender are always available and the file that I share is adapted to the latest version. The whole file or parts of it can easily be exported into many other formats from the .blend if needed.</p>
<p>Pathological anatomy could be a further step, beyond all sane anatomy.</p>
<p>The memory needed to run the whole anatomy is indeed pushing the processor to their limits, I will maybe create other files containing only an arm, a leg etc. to alleviate the calculation needed.<br>
The attempt to optimize the file size is a priority, and Giorgio Luciano, a(nother) Medical 3D modeller proposed today to work on the file to retopo a fair part of it in order to use Normal maps. We’ll see if it helps. Although I achieved to lower the file size from 261 to 197Mb following the good advice from DNorman (<a href="https://blenderartists.org/t/open-source-anatomy-on-blender/1316160/13" class="inline-onebox" rel="noopener nofollow ugc">Open source anatomy on blender - #13 by DNorman - Works in Progress - Blender Artists Community</a>); the memory used keeps being very high.</p>
<p>Importing the shortcuts is quite straightforward but I requested an similar way to import/export user preferences; at the moment the way to change it in is to find the location of the program through a %appdata% search, then pasting the userprefs.blend into the scripts folder:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://blender.community/c/rightclickselect/pZz6/?sorting=hot">
  <header class="source">
      <img src="https://d3a2gvihmbqfjo.cloudfront.net/cache/70/12/70129cd159e57d165040904b6cd7d089.png" class="site-icon" width="128" height="128">

      <a href="https://blender.community/c/rightclickselect/pZz6/?sorting=hot" target="_blank" rel="noopener nofollow ugc">Blender Community</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/388;"><img src="https://blender.community/static/images/social.jpg" class="thumbnail" width="690" height="388"></div>

<h3><a href="https://blender.community/c/rightclickselect/pZz6/?sorting=hot" target="_blank" rel="noopener nofollow ugc">Import/Export User preferences as a '.py' file</a></h3>

  <p>If the shortcuts can be Imported and Exported through a '.py' file; would it be…</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The file is meant to be used with a full desktop computer with a 3 button mouse and a keyboard with numpad. The other devices will suffer severe limitations of the functionalities. On the other hand, for those who have the required material, it offers all the functions that he/she can dream of.</p>
<p>I agree about the eye icon issue, especially the fact that showing a collection should implicate to automatically show all the upper collection but understand also why they chose to do it this way. you can shift LMB the eye icon of a collection to show/hide all the underlying structures at once.<br>
I found that it was much easier to show/hide collection, selecting them with the customized shortcut ‘RMB’ that allow to chose the collections to which the selected structure belongs, and to hide with ‘H’. the outliner is still kept apparent as a glossary, but can be hidden.</p>
<p>I already contacted Michael Halle from the Open anatomy project to see if a collaboration was possible and wait for his answer.</p>
<p>The work has been started a few months ago and is under development. The best way to see what is missing is looking to the empty collections of the outliner (there are thousands of structures, trying to list them is a big work).</p>
<p>As for the last part, it leads me to macro-economic and political considerations that you probably share, since 3D Slicer is open source. I work without any subvention and will soon have to ‘find a job’. But of course, much could be (/have been) done with some will. The will seems to be missing within most decisions makers.</p>
<p>Thank you for these feedback, Andras, I appreciate much your work and would have loved to collaborate with you if there were more bridges between 3DSicer and Blender. I asked to ‘BodyPart3D’ for the RMI (there must be one somewhere) used to creates the models but did not get any answer. Would you like to insist with me? This point is quite important for the future of the project.</p>

---

## Post #11 by @lassoan (2021-08-25 05:10 UTC)

<aside class="quote no-group" data-username="Melodicpinpon" data-post="10" data-topic="17734">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/melodicpinpon/48/3254_2.png" class="avatar"> Melodicpinpon:</div>
<blockquote>
<p>would have loved to collaborate with you if there were more bridges between 3DSicer and Blender</p>
</blockquote>
</aside>
<p>If there is a good scene file format that both Slicer and Blender can import/export without losing any valuable information then this problem is solved. We hoped that glTF would work, but it is a bit too low-level and it seems quite hard to preserve all custom metadata during import/export operations. However, USD format looks quite promising. Blender can already read/write it and there seems to be official packages to read/write USD files in Python that may be usable in Slicer. I’ve also <a href="https://discourse.vtk.org/t/universal-scene-description-usd-scene-importer-exporter/6452">asked about USD on the VTK forum</a> and they seemed to be open to the idea. It is not an easy task to add support for this complex file format, but due to its flexibility and wide support in various tools, the investment would probably pay off in the long term.</p>
<aside class="quote no-group" data-username="Melodicpinpon" data-post="10" data-topic="17734">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/melodicpinpon/48/3254_2.png" class="avatar"> Melodicpinpon:</div>
<blockquote>
<p>I asked to ‘BodyPart3D’ for the RMI (there must be one somewhere) used to creates the models but did not get any answer. Would you like to insist with me? This point is quite important for the future of the project.</p>
</blockquote>
</aside>
<p>It took a while for me to figure out that by RMI you mean MRI. Yes, if there are no underlying anatomical images then it is quite limited what you can do with the atlas, as it is harder to correlate with other atlases, verify that the model is accurate, etc. I’m not sure how can I help with this. I think the issue is that people must prioritize projects that they are funded to do, so while they would like to help others, it may not be always possible. So, as you have probably realized, to get funding so that you and your collaborators can give enough attention to it.</p>

---

## Post #12 by @Melodicpinpon (2021-08-25 07:04 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="17734">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I was not able to show labels with callouts, as I saw it on some screenshots.</p>
</blockquote>
</aside>
<p>The labels that have been added for now use the ‘MeasureIt’ free default addon because Call out tiles is not free (about 1$ too expensive).</p>
<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="17734">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Yes, if there are no underlying anatomical images then it is quite limited what you can do with the atlas, as it is harder to correlate with other atlases, verify that the model is accurate, etc.</p>
</blockquote>
</aside>
<p>Most atlases do not share .dicoms and are still valuable learning tools. The one that I share is based on the great work of ‘BodyParts3D’ (that has been left as separated .obj with their names and relations contained in another file during then years) and I therefore depend on them to get or not a .dicom.</p>
<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="17734">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I’m not sure how can I help with this.</p>
</blockquote>
</aside>
<p>I only mean to write to the Author and ask for the MRI.</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://www.linkedin.com/feed/update/urn:li:activity:6797436892670500865">
  <header class="source">
      <img src="https://static.licdn.com/aero-v1/sc/h/al2o9zrvru7aqj8e1x2rzsrca" class="site-icon" width="" height="">

      <a href="https://www.linkedin.com/feed/update/urn:li:activity:6797436892670500865" target="_blank" rel="noopener nofollow ugc">linkedin.com</a>
  </header>

  <article class="onebox-body">
    <img width="" height="" src="https://media.licdn.com/dms/image/C5622AQHHTM5XxUWFqg/feedshare-shrink_2048_1536/0/1620635245001?e=1706140800&amp;v=beta&amp;t=3Fwv-08bUbMl55q12YakcmTeMPqbIMA2Odp8sUXW3f0" class="thumbnail">

<h3><a href="https://www.linkedin.com/feed/update/urn:li:activity:6797436892670500865" target="_blank" rel="noopener nofollow ugc">Z-Anatomy sur LinkedIn&nbsp;: Kousaku Okubo, l'auteur des deux modèles libres...</a></h3>

  <p>Kousaku Okubo, l'auteur des deux modèles libres d'anatomie humaine 'BodyParts3D', me confirme ce matin que la modification et la diffusion du contenu qu'il a…</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="17734">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I think the issue is that people must prioritize projects that they are funded to do</p>
</blockquote>
</aside>
<p>I will keep on doing what I can and does not depend on other’s help; fundings wouldn’t enhance the quality of what I do; although it may be useful to keep on working on the long term.</p>

---

## Post #13 by @Melodicpinpon (2022-01-26 12:34 UTC)

<p>Hi Pieper,<br>
I watched one or two videos but did not get what advantage(s) the USD format has over the .blend, or the .fbx that can also be used to import a model from Blender to Unity.</p>

---

## Post #14 by @pieper (2022-01-26 15:41 UTC)

<p>Probably the main advantages of USD are that it’s a modern, open, platform neutral format that’s designed as an interchange format rather than a document format for a given software.</p>

---

## Post #15 by @lassoan (2022-01-26 20:24 UTC)

<aside class="quote no-group" data-username="pieper" data-post="14" data-topic="17734">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>designed as an interchange format rather than a document format for a given software</p>
</blockquote>
</aside>
<p>Exactly!</p>
<p>I would also add that since we discussed this we spent some more time with gltf and available web viewers and improved the SlicerOpenAnatomy extension. As a result we now have a very good workflow for creating and share models:</p>
<ul>
<li>Create/edit segmentation using Segment Editor</li>
<li>Export segmentation to glTF format using SlicerOpenAnatomy extension. The glTF file stores segment names, hierarchy, and display properties. We use simple shading and no texture, but we could specify more interesting textures, too.</li>
<li>Upload the glTF file to GitHub or Dropbox (or use any custom file hosting).</li>
<li>Embed the model into your website or view on a computer/tablet/phone using a free glTF web viewer. For example, you can use <a href="http://3dviewer.net">3dviewer.net</a>, which can show/hide branches of the hierarchy, click on any model to get information on it, click on a structure in the model tree to see that in 3D, etc. <a href="https://3dviewer.net/#model=https://www.dropbox.com/s/38arwo2uhzu0ydg/SPL-Abdominal-Atlas.gltf?dl=0"><strong>Click here for an example.</strong></a></li>
</ul>
<p><a href="https://3dviewer.net/#model=https://www.dropbox.com/s/38arwo2uhzu0ydg/SPL-Abdominal-Atlas.gltf?dl=0"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c91c63b9c8d2cdb8e2a23b0f67d3c1a68ff2f143.jpeg" alt="image" data-base62-sha1="sH6NlqR03JaTDM2QLX7UPGAyXf5" width="660" height="500"></a></p>
<p>This workflow has many advantages:</p>
<ul>
<li>No software installation is needed for model viewing.</li>
<li>You can create high-quality yet lightweight, fast-loading models (glTF is a high-efficiency export format, not a document format such as .blend). See an <strong><a href="https://3dviewer.net/#model=https://raw.githubusercontent.com/lassoan/Test/master/DamagedHelmet.glb">example with nice textures and lighting here</a></strong>.</li>
<li>Everything is completely free. (not even $1)</li>
<li>The data does not have to be uploaded to third-party servers - just your own server or the cloud service provider to store your data.</li>
<li>You can share data privately: only those people can access your file on Dropbox who has received the link from you.</li>
</ul>
<p>You can find some more information in this topic:</p>
<aside class="quote quote-modified" data-post="11" data-topic="21082">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/is-there-any-way-to-export-the-model-by-fbx-format/21082/11">Is there any way to export the model by FBX format?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    I would just add that with this viewer it is very easy to share 3D models using Dropbox, to be viewed on desktop computer or on a phone: 

Copy the file into your Dropbox
Right-click on it and choose Copy dropbox link
Prepend the https://3dviewer.net/#model= to the link to create a link that you can send anyone to view the model anywhere, even on a phone

The model is not uploaded to any server when it is viewed (it remains on Dropbox) and only those people can access it who know the link. 
<a name="p-73010-example-1" class="anchor" href="#p-73010-example-1" aria-label="Heading link"></a>Exam…
  </blockquote>
</aside>


---

## Post #16 by @Melodicpinpon (2022-02-26 07:06 UTC)

<p>All this sounds interesting;<br>
I’ll take a close look at it soon.<br>
Meanwhile you may like to see the app made in Unity by Lluis Vinent,<br>
it’s already pretty cool:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://www.z-anatomy.com/atlas">
  <header class="source">
      <img src="https://static.wixstatic.com/media/8937f4_5c3c0c90ea9a44e9828d15487fb89c19%7Emv2.png/v1/fill/w_32%2Ch_32%2Clg_1%2Cusm_0.66_1.00_0.01/8937f4_5c3c0c90ea9a44e9828d15487fb89c19%7Emv2.png" class="site-icon" width="32" height="32">

      <a href="https://www.z-anatomy.com/atlas" target="_blank" rel="noopener nofollow ugc">Z-Anatomy</a>
  </header>

  <article class="onebox-body">
    <img src="https://static.wixstatic.com/media/8937f4_c935ec2c5ed844bcba8010cb4424b9f0~mv2.png/v1/fill/w_960,h_960,al_c/8937f4_c935ec2c5ed844bcba8010cb4424b9f0~mv2.png" class="thumbnail onebox-avatar" width="500" height="500">

<h3><a href="https://www.z-anatomy.com/atlas" target="_blank" rel="noopener nofollow ugc">ATLAS | Z-Anatomy</a></h3>

  <p>Download the open source 3D atlas of Human Anatomy for Windows, Mac or Linux.

-Human anatomy Atlas
-Biomechanics
-Veterinary anatomy</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
This videos shows the blend part of the project:</p><div class="youtube-onebox lazy-video-container" data-video-id="fAITXJE8ECA" data-video-title=" - YouTube" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=fAITXJE8ECA" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="" title=" - YouTube" width="" height="">
  </a>
</div>
<div class="youtube-onebox lazy-video-container" data-video-id="JIxJnw1ARhs" data-video-title="Z-Anatomy: The Blend-Tutorial" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=JIxJnw1ARhs" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/JIxJnw1ARhs/maxresdefault.jpg" title="Z-Anatomy: The Blend-Tutorial" width="" height="">
  </a>
</div>


---

## Post #17 by @Melodicpinpon (2022-02-26 11:25 UTC)

<p>The ‘Online 3D viewer’ is simple and easy, I like it.<br>
Nonetheless, the app made by Lluis Vinent for ‘Z-anatomy’ has more options and very useful tools to navigate, select, isolate, with the labels, the definitions and so on.<br>
Blender and the python script also provide a very rich environment to visualize these models.<br>
Therefor, I do not see much reason for me to convert the files to match the USD format.</p>
<p>Besides, the formats that you speak about may be more versatile, but when it comes to the edition of the models, a real 3D software will be needed anyway, and Blender is the open source option, and became really competitive technically.</p>
<p>The combination of Blender and Unity seem to be the best option today to create and share, for example, specific anatomical models, or an open source anatomical model of another animal.</p>
<p>What do you think about this analysis?<br>
Do you think that there is still a good reason to convert the files in USD and share them with the ‘Online 3D Viewer’?<br>
Would you like to join our efforts to share a powerful open visualizer solution?</p>
<p>I plan to go on working on the anatomical content during the next months.</p>

---

## Post #18 by @lassoan (2022-02-28 14:11 UTC)

<aside class="quote no-group" data-username="Melodicpinpon" data-post="17" data-topic="17734">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/melodicpinpon/48/3254_2.png" class="avatar"> Melodicpinpon:</div>
<blockquote>
<p>The combination of Blender and Unity seem to be the best option today to create and share, for example, specific anatomical models, or an open source anatomical model of another animal.</p>
<p>What do you think about this analysis?</p>
</blockquote>
</aside>
<p>If the goal is that a handful of anatomy and 3D modeling experts maintain a few mesh-only atlases that many people with average experience and computing hardware can view then what you described sounds like a good solution. Your previous attempt of using Blender as end-user viewer assumed that users could install Blender, had a computer that could load a full-quality anatomical model, and were able to learn to use Blender, which excluded many people; that’s why adding an easy-to-use viewer displaying simplified models is great.</p>
<aside class="quote no-group" data-username="Melodicpinpon" data-post="17" data-topic="17734">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/melodicpinpon/48/3254_2.png" class="avatar"> Melodicpinpon:</div>
<blockquote>
<p>Do you think that there is still a good reason to convert the files in USD and share them with the ‘Online 3D Viewer’?</p>
</blockquote>
</aside>
<p>If you want to support images (such as importing and displaying CT, MRI, etc. images along with 3D models), want to allow the end-users community to not just view but also edit/combine/create atlases, maintain many atlases in a sustainable way, etc. then you need to make the workflow more flexible and scalable. This is why using USD, glTF, or other simple but powerful standard open file format (with custom extensions or conventions) for storing your atlases would be essential. Blender’s .blend file format is a document file format with the goal of supporting all features of Blender and evolves with the application, and therefore it is not suitable for data exchange and archival.</p>
<aside class="quote no-group" data-username="Melodicpinpon" data-post="17" data-topic="17734">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/melodicpinpon/48/3254_2.png" class="avatar"> Melodicpinpon:</div>
<blockquote>
<p>Would you like to join our efforts to share a powerful open visualizer solution?</p>
</blockquote>
</aside>
<p>I’m mostly interested in utilizing imaging data for creating and editing anatomical models in Slicer and export/import them in standard file formats. I’m very happy if there are simple viewers that can display the created content, but I won’t be able to directly contribute to them (other than with occasional testing and giving advice).</p>

---

## Post #19 by @Tifoura_Sofiane (2023-06-27 15:49 UTC)

<p>Hello, does anyone have a valid link to download the Z anatomy models please?</p>

---

## Post #20 by @TylerChan (2023-06-28 03:00 UTC)

<p>Yea, I found out few days ago the site has suddenly gone for unknown reason.<br>
I have the file from March 2023 version 0.9.9.7.5 for both blender and Unity portable version.<br>
I put them on google drive:<br>
Blender Version:</p><aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1qiICVVR3XOCQH6PnCjDoBUQVuMADw_DX/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1qiICVVR3XOCQH6PnCjDoBUQVuMADw_DX/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1qiICVVR3XOCQH6PnCjDoBUQVuMADw_DX/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1qiICVVR3XOCQH6PnCjDoBUQVuMADw_DX/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">Z-Anatomy_Portable.7z</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
Unity Version:</p><aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1axtWp58_eRgWDPLZWLJiRhESKKXqQukd/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1axtWp58_eRgWDPLZWLJiRhESKKXqQukd/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1axtWp58_eRgWDPLZWLJiRhESKKXqQukd/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1axtWp58_eRgWDPLZWLJiRhESKKXqQukd/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">Z-Anatomy_W64_0.9.9.7.5_Portable.zip</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #21 by @Tifoura_Sofiane (2023-06-28 05:39 UTC)

<p>Oh thank you very much !</p>

---

## Post #22 by @Tifoura_Sofiane (2023-06-28 05:56 UTC)

<p>How can I have access to 3d models for blender ?</p>

---

## Post #23 by @TylerChan (2023-06-28 09:35 UTC)

<p>Just download both version, the blender version included portable version of blender and doesn’t require any installation. I prefer the Unity version for showcasing.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e839751fd263c2803de1577258c08f5c6235600.png" data-download-href="/uploads/short-url/6DtTze5NjR3ky5SnYH6rYv5m1Ms.png?dl=1" title="46F1CBA3D553420684C534FCD439D199.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e839751fd263c2803de1577258c08f5c6235600.png" alt="46F1CBA3D553420684C534FCD439D199.png" data-base62-sha1="6DtTze5NjR3ky5SnYH6rYv5m1Ms" width="690" height="0" data-dominant-color="000000"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">46F1CBA3D553420684C534FCD439D199.png</span><span class="informations">708×1 96 Bytes</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #24 by @Tifoura_Sofiane (2023-06-28 10:53 UTC)

<p>Ok , I didn’t download the first file.  Thank you very much !</p>

---

## Post #25 by @Bradley_Auerbach (2023-11-02 21:19 UTC)

<p>I got access to the files through a Google Drive link on YouTube, but without the website I can’t determine what the usage rights are!</p>

---

## Post #26 by @lassoan (2023-11-03 00:31 UTC)

<p>Z-anatomy was distributed with a copyleft license. You can use it internally without any restrictions. If you want to distribute it then you need to publicly make all your source code and data available publicly with a copyleft license.</p>

---

## Post #27 by @Bradley_Auerbach (2023-11-03 00:50 UTC)

<p>I guess I won’t use it for my commercial game then. I am making another (freeware) project that is CC-BY-SA 3.0 as it’s based on a creative writing website also licensed the same way; would that be compatible with the copyleft license?</p>

---

## Post #28 by @npelot (2024-02-21 00:56 UTC)

<p>Hello! I was just wondering if this project is still live, since the <a href="http://www.z-anatomy.com" rel="noopener nofollow ugc">www.z-anatomy.com</a> page doesn’t seem to be live – “Looks like this domain isn’t connected to a website yet”. Thanks!</p>

---

## Post #29 by @lassoan (2024-02-21 20:43 UTC)

<p>I think the z-anatomy project is not active anymore. You can probably still find the models online (e.g., <a href="https://github.com/LluisV/Z-Anatomy/tree/PC-Version/Z-Anatomy%20PC/Assets/Models/1.0%20Models">here</a>), but since it was distributed with a restrictive license (inherited from <a href="http://lifesciencedb.jp/bp3d/">bodyparts3d</a> source) and it does not have corresponding image data, it has quite limited use.</p>

---

## Post #30 by @npelot (2024-02-22 01:27 UTC)

<p>Noted, thank you for the information!</p>

---
