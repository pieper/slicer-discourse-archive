---
topic_id: 44361
title: "Use Of 3D Slicer For Creating Surface Meshes Of Wood From Mi"
date: 2025-09-05
url: https://discourse.slicer.org/t/44361
---

# Use of 3D slicer for creating surface meshes of wood from micro tomograph imagery

**Topic ID**: 44361
**Date**: 2025-09-05
**URL**: https://discourse.slicer.org/t/use-of-3d-slicer-for-creating-surface-meshes-of-wood-from-micro-tomograph-imagery/44361

---

## Post #1 by @franco_otaola (2025-09-05 16:56 UTC)

<p>Hello,<br>
I am not a current user of slicer3D but I am looking for a software to transform the output of a college doing microtomograph to, ideally a surface mesh of different sections of a scan of wood.</p>
<p>the scans are generated in .tiff format so they are a stack of images, I have experience in meshing but engineering models from CAD or from pre-existing surface meshes so, even thought it is a new world for me I have a slight understanding of it.</p>
<p>currently i am looking for ideally an open source solution to go from the stack of images up to a volumetric mesh for doing numerical simulations, FEM/FVM. as a long time user of paraview, i came across slicer 3D which looks like the correct tool for what i am looking for but i have some questions:<br>
the images looks like this:</p>
<p>                    <a href="https://ars.els-cdn.com/content/image/1-s2.0-S1047847710001139-gr3.jpg" target="_blank" rel="noopener nofollow ugc" class="onebox">
            <img src="https://ars.els-cdn.com/content/image/1-s2.0-S1047847710001139-gr3.jpg" width="383" height="500">
          </a>

</p>
<p>some clarification for better understanding of anyone reading for better communication:</p>
<ul>
<li>surface mesh: a triangular (or quadrilateral) mesh of a 3D object, it is on 3D space but it is only the shell of the object.</li>
<li>watertight mesh: a surface mesh that one can define an inside and outside of it (closed volume).</li>
<li>conformal mesh: a mesh that does not have any non manifold elements, such as hanging elements of surfaces elements that do not close into a volume</li>
<li>volumetric mesh: a tetrahedral (or hexahedral/polyhedral) mesh of a 3D object, it is on 3D space but in difference to the surface mesh it is filled up with elements.</li>
</ul>
<p>my questions about the software are:</p>
<ol>
<li>
<p>from the tiff images can i generate 3D surfaces meshes?</p>
</li>
<li>
<p>as it can be seen in the image, there are different sections on a wood material, is it possible to divide it by grey scale to distinguish the different ‘materials’ inside the wood and generate separated meshes? (for example if the images are circular with half white half black, can i generate automatically (by setting some thresholds) 2 meshes where each of them will be half a cylinder?</p>
</li>
<li>
<p>surface meshes (ideally with separated regions question 2.) would allow me to develop the complete workflow, i have other tools to generate the volumetric mesh, but is it possible to generate them in 3D slicer directly? what are the algorithms integrated in case there exists?</p>
</li>
<li>
<p>is the procedure I mentioned in 1. multi-thread? or GPU accelerated or something similar, where i can speed it up with a workstation? the imagery is quite large in weight as the resolution is really fine</p>
</li>
<li>
<p>are the surfaces meshes generated, water tight? ideally conformal?</p>
</li>
<li>
<p>there are scans that are over time, to measure the penetration of liquid inside the material, is something that the software can work on? like deform the surface mesh/ remesh it at each time step?</p>
</li>
<li>
<p>how easy is the python scripting of slicer 3D? I use almost daily paraview with python, is it similar to it to program with?</p>
</li>
<li>
<p>to what extend would this kind of work fully automatizable with slicer 3D? (I mean up to the point of getting a watertight surface mesh for each region separately.)</p>
</li>
<li>
<p>is there any similar tutorials or applications that have been explored already in this kind of application? i saw only medical imagery, but slicer 3D looks quite promising for this kind of application</p>
</li>
</ol>
<p>sorry if i have not being clear enough about any of my questions please do not hesitate as i can complete them with more information if necessary. sadly right now i dont have a file to provide as it is a work i will do in the following months.</p>
<p>thanks in advance,</p>

---

## Post #2 by @pieper (2025-09-05 17:41 UTC)

<p>Big picture is yes, Slicer could be a good tool since many of the features you listed are standard.  But your domain is enough different that you may need to adapt things.  Slicer is quite configurable, finding application in topics from geology to astrology and many fields of medicine so probably it can do what you want but only you will be able to know the details by trying.</p>
<ol>
<li>from the tiff images can i generate 3D surfaces meshes?</li>
</ol>
<p>Yes, see, for example, the <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ImageStacks">ImageStacks</a> feature of SlicerMorph.</p>
<ol start="2">
<li>as it can be seen in the image, there are different sections on a wood material, is it possible to divide it by grey scale to distinguish the different ‘materials’ inside the wood and generate separated meshes? (for example if the images are circular with half white half black, can i generate automatically (by setting some thresholds) 2 meshes where each of them will be half a cylinder?</li>
</ol>
<p>Yes, see the Threshold effect in the Segment Editor.  Also the Islands too.</p>
<ol start="3">
<li>surface meshes (ideally with separated regions question 2.) would allow me to develop the complete workflow, i have other tools to generate the volumetric mesh, but is it possible to generate them in 3D slicer directly? what are the algorithms integrated in case there exists?</li>
</ol>
<p>See the <a href="https://github.com/lassoan/SlicerSegmentMesher">SegmentMesher extension</a>.  It’s not perfect at making volumetric meshes for all purposes but it’s a good start and you can compare with other tools.</p>
<ol start="4">
<li>is the procedure I mentioned in 1. multi-thread? or GPU accelerated or something similar, where i can speed it up with a workstation? the imagery is quite large in weight as the resolution is really fine</li>
</ol>
<p>Surface mesh generation in Slicer is multithreaded and the new SurfaceNets option is very fast.</p>
<ol start="5">
<li>are the surfaces meshes generated, water tight? ideally conformal?</li>
</ol>
<p>Segment surfaces are independent by default in Slicer are primarily for visualization so close but not assured to be watertight in the extreme (look up the JointSmoothing option for details).  The Cleaver tool in SegmentMesher will give you a single mesh with material labels.  Volumetric meshing in Slicer is an evolving topic, with lots of interest as more simulation tools are being integrated.</p>
<ol start="6">
<li>there are scans that are over time, to measure the penetration of liquid inside the material, is something that the software can work on? like deform the surface mesh/ remesh it at each time step?</li>
</ol>
<p>You can certainly do that with a script.</p>
<ol start="7">
<li>how easy is the python scripting of slicer 3D? I use almost daily paraview with python, is it similar to it to program with?</li>
</ol>
<p>Slicer python scripting is very powerful.  It’s different from Paraview but not hugely.  See <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">these examples.</a></p>
<ol start="8">
<li>to what extend would this kind of work fully automatizable with slicer 3D? (I mean up to the point of getting a watertight surface mesh for each region separately.)</li>
</ol>
<p>Yes, this shouldn’t be a problem.</p>
<ol start="9">
<li>is there any similar tutorials or applications that have been explored already in this kind of application? i saw only medical imagery, but slicer 3D looks quite promising for this kind of application</li>
</ol>
<p>Tons of different examples, too many to list here.  I think you can just browse <a href="http://slicer.org">slicer.org</a>, <a href="http://slicermorph.github.io">slicermorph.github.io</a>, and <a href="http://projectweek.na-mic.org">projectweek.na-mic.org</a> to get ideas.  Yes, mostly medical but really what you describe is not that much different.</p>
<p>Please do share example data and we can be much more specific about what might or might not be easy to do in Slicer.</p>

---

## Post #3 by @franco_otaola (2025-09-08 06:22 UTC)

<p>enormous thanks <a class="mention" href="/u/pieper">@pieper</a> , your answer is exactly what i was looking for, deep, and with a good insight on the capabilities (it happened to me so many times that the features were not clear in other softwares but the community was not really active and i spend a lot of time to realize it was not the good tool, well they help on other applications at the end <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> )</p>
<p>anyways, regarding your answer:</p>
<p>&gt;Segment surfaces are independent by default in Slicer are primarily for visualization so close but not assured to be watertight in the extreme (look up the JointSmoothing option for details). The Cleaver tool in SegmentMesher will give you a single mesh with material labels. Volumetric meshing in Slicer is an evolving topic, with lots of interest as more simulation tools are being integrated.</p>
<p>so if i understand correctly, the volumetric mesh (as everywhere i would say) is something in development (is it tetra? hexa? poly? is generated by octee from what i can see?.</p>
<p>&gt;Slicer python scripting is very powerful. It’s different from Paraview but not hugely. See <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html" rel="noopener nofollow ugc">these examples.</a></p>
<p>this is awsome, i will check when the time comes, just 2 small questions in this regards:</p>
<ol>
<li>
<p>would you say that it will be possible to fully script it, from a to z (i mean input tiff output surface mesh separated in regions or mesh with different regions in stl?) (i know that you commented that it was not a problem but just to be sure)</p>
</li>
<li>
<p>does slicer3D have a feature similar to for example paraview, trace tool? where you turn it on, you do whatever you want on the interface (lets say open the tiff file and extract the surface mehs), and then turn off the trace tool, you get a python script that will reproduce what ever you did in the GUI. this is an awsome tool in paraview that helps fast creation of script</p>
</li>
</ol>
<p>&gt;Yes, mostly medical but really what you describe is not that much different.</p>
<p>yeah is what i thought also!</p>
<p>&gt;Please do share example data and we can be much more specific about what might or might not be easy to do in Slicer.</p>
<p>I will try to get the data from my collegues and upload it, keep you in touch,</p>
<p>thanks a LOT!</p>

---

## Post #4 by @pieper (2025-09-08 12:36 UTC)

<aside class="quote no-group" data-username="franco_otaola" data-post="3" data-topic="44361">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/franco_otaola/48/80984_2.png" class="avatar"> franco_otaola:</div>
<blockquote>
<p>so if i understand correctly, the volumetric mesh (as everywhere i would say) is something in development (is it tetra? hexa? poly? is generated by octee from what i can see?.</p>
</blockquote>
</aside>
<p>Most work is on tetrahedera, since that’s what many solvers expect, but Slicer/VTK support hex as well. We have been generating meshes with the external tooling (e.g Cleaver and TetGen) but people have also been experimenting with gmsh and also just making the meshes directly in VTK.  Really many things are possible since you can bridge to almost any external software.</p>
<aside class="quote no-group" data-username="franco_otaola" data-post="3" data-topic="44361">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/franco_otaola/48/80984_2.png" class="avatar"> franco_otaola:</div>
<blockquote>
<p>would you say that it will be possible to fully script it, from a to z</p>
</blockquote>
</aside>
<p>I don’t see why not.  Sometimes people use external tools like Blender or MeshMixer for specialized tasks.  Most things are scriptable except often the segmentation and some mesh repair.</p>
<aside class="quote no-group" data-username="franco_otaola" data-post="3" data-topic="44361">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/franco_otaola/48/80984_2.png" class="avatar"> franco_otaola:</div>
<blockquote>
<p>does slicer3D have a feature similar to for example paraview, trace tool?</p>
</blockquote>
</aside>
<p>Unfortunately no, that’s not available.  Instead we rely on examples (lots of extensions and script snippets) and lately the AI tools are getting to be very useful but they do make mistakes.</p>

---

## Post #5 by @franco_otaola (2025-09-09 08:11 UTC)

<p>Thanks a lot for your insight, as you asked me before, here you can find what kind of input file i would have for the slicer3D</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://filesender.renater.fr/?s=download&amp;token=2497f23a-18e1-4c36-bb62-1971af7e9ed9">
  <header class="source">
      <img src="https://filesender.renater.fr/skin/favicon.png" class="site-icon" alt="" width="64" height="64">

      <a href="https://filesender.renater.fr/?s=download&amp;token=2497f23a-18e1-4c36-bb62-1971af7e9ed9" target="_blank" rel="noopener nofollow ugc">filesender.renater.fr</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://filesender.renater.fr/?s=download&amp;token=2497f23a-18e1-4c36-bb62-1971af7e9ed9" target="_blank" rel="noopener nofollow ugc">FileSender</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>if you have a minute or two to see and give me your opinion i would appreciate it.</p>
<p>regards,</p>

---

## Post #6 by @pieper (2025-09-09 19:32 UTC)

<p>That looks like nice data.  It loads fine from the multiframe tiff (it seems to get the spacing correct).  It’s clean and sharp, but depending one which structures exactly you are trying to segment you may need to experiment a bit.  I’ll bet nnInteractive would work to isolate the substructures, but you may also be able to come up with something fully automated.  Perhaps for your purposes you can get away with simple thresholding.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c7fa9c0bc7a996a9f2b669f5c9d5ca5b6b8ca66.jpeg" data-download-href="/uploads/short-url/8DcaeQ9qI12n8TwByjKRuE4lS3Y.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c7fa9c0bc7a996a9f2b669f5c9d5ca5b6b8ca66_2_523x500.jpeg" alt="image" data-base62-sha1="8DcaeQ9qI12n8TwByjKRuE4lS3Y" width="523" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c7fa9c0bc7a996a9f2b669f5c9d5ca5b6b8ca66_2_523x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c7fa9c0bc7a996a9f2b669f5c9d5ca5b6b8ca66_2_784x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c7fa9c0bc7a996a9f2b669f5c9d5ca5b6b8ca66.jpeg 2x" data-dominant-color="494A48"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">922×881 83.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @franco_otaola (2025-09-15 14:57 UTC)

<p>thanks a lot for taking your time, in two weeks i beging working in this subject and slicer3D will be on one of the top things to work on. I will try to do everything i asked in my first step, but also knowing how the data looks, i think a polycube method could spit out a great hexa mesh. will keep you update!</p>

---
