---
topic_id: 524
title: "Save Volume Rendering As Stl File"
date: 2017-06-19
url: https://discourse.slicer.org/t/524
---

# Save volume rendering as STL file

**Topic ID**: 524
**Date**: 2017-06-19
**URL**: https://discourse.slicer.org/t/save-volume-rendering-as-stl-file/524

---

## Post #1 by @jjb (2017-06-19 05:03 UTC)

<p>Hello, I am a new user on 3D slicer.</p>
<p>I was using the display preset feature under volume rendering, and I was wondering if there is a way to save what I was viewing as an .stl or 3D printable file.</p>
<p>For example, I was viewing a sample MRI using the CT-cardiac3 preset display.<br>
When I tried to save that specific 3D preset displayed sample in a .stl file, the option was unavailable.<br>
I was only able to see .vp (volume property), .txt formats.</p>
<p>Is there a way to accomplish what I desire in 3D slicer?</p>
<p>This is the image of the 3D preset that I would like to try converting into .stl file.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/8804631375f8f8716214e1e78534c9fb146dc0c0.jpg" data-download-href="/uploads/short-url/jpgkMccPNsrAPzfDfxuzo3Rvto4.jpg?dl=1" title="20170618_171241.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/8804631375f8f8716214e1e78534c9fb146dc0c0_2_400x500.jpg" width="400" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/8804631375f8f8716214e1e78534c9fb146dc0c0_2_400x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/8804631375f8f8716214e1e78534c9fb146dc0c0_2_600x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/8804631375f8f8716214e1e78534c9fb146dc0c0_2_800x1000.jpg 2x" data-dominant-color="79696A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20170618_171241.jpg</span><span class="informations">1878×2344 1.64 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2017-06-19 05:10 UTC)

<p>Volume rendering is just a display technique - to get an STL file you need to segment the volume using Segment Editor module.</p>
<ul>
<li>Tutorial: <a href="https://www.slicer.org/wiki/Documentation/4.6/Training#Segmentation_for_3D_printing">https://www.slicer.org/wiki/Documentation/4.6/Training#Segmentation_for_3D_printing</a>
</li>
<li>Reference: <a href="http://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html">http://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html</a>
</li>
</ul>

---

## Post #3 by @jjb (2017-06-19 17:20 UTC)

<p>Hi Andras,</p>
<p>Thank you for the response.</p>
<p>One thing I notice from the segmentation is the lack of details of the soft tissues within the 3D model.<br>
Is there a way to retain the details of the tissues in the 3D models in segmentation and save that as a .stl file?</p>

---

## Post #4 by @lassoan (2017-06-19 18:08 UTC)

<p>Volume rendering displays a semi-transparent cloud, but for 3D printing you need hard boundaries that exactly define what is inside/outside. Finding exact boundaries is often a difficult task - that’s why all the segmentation tools are developed.</p>
<p>Typically the issue is at low-contrast regions. You may need to apply smoothing, apply manual corrections, or use semi-automatic tools to have nice, smooth, and correct boundaries in these regions.</p>

---

## Post #5 by @jjb (2017-06-19 21:35 UTC)

<p>If I would like to retain the semi-transparent cloud for other purposes besides 3D printing, could that semi-transparent 3D display model be saved as a .stl file?</p>

---

## Post #6 by @lassoan (2017-06-19 22:04 UTC)

<p>Semi-transparent volumetric cloud = your image data, so you already have it. No processing is performed on the data, it is visualized directly using <a href="https://en.wikipedia.org/wiki/Volume_rendering">raycasting</a>. Volume rendering visualization parameters are mostly defined by transfer functions (opacity, color, gradient), which are saved in the Slicer scene.</p>
<p>STL file cannot store volumetric cloud, it only stores a surface mesh = hard boundary of your printed object.</p>
<p>What confuses most people that volume rendering may give the illusion that there is a distinct surface computed from the data, but actually what you see is a volumetric cloud.</p>

---

## Post #7 by @jjb (2017-06-20 01:53 UTC)

<p>Thank you for your very insightful response.</p>
<p>I have one final question.<br>
Is there a way to export the volume rendered 3D model so that it can be viewed outside of 3D slicer?<br>
In other words, can there be a way to save the 3D model (with volumetric cloud) so that it can be viewed in other 3D programs (ex. unity3D) ?</p>

---

## Post #8 by @lassoan (2017-06-20 02:31 UTC)

<p>No 3D model is generated for volume rendering. The input for volume rendering is the raw volume data, so the only thing you can export is the visualization settings (transfer functions). You may find a volume renderer for Unity and other software, but in general if you want to use your volumetric images in modeling software then you need to segment them.</p>

---

## Post #9 by @jjb (2017-06-20 02:36 UTC)

<p>Okay, thank you so much Andras!<br>
I really appreciate your help.</p>

---

## Post #10 by @maxabernathy (2017-07-13 22:25 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thanks for this thread and your explanations. I have looked into the results of segmentation procedures but I would like to rebound on this topic. I am currently developing mostly in Unity3d for VR&amp;AR platforms, inter alia for surgeons using detailed soft tissue models for decisionmaking. If I could bridge the output of the volumetric rendering results in 3dslicer to Unity3d, this could prove to be a great feature but as OP mentioned, I have the same export problem since I’m really interested in getting an .FBX, for example. To segment every part of an organ for example is tedious work and 3dslicer does not provide a lot of export paths I could work around. Do you know of any other pointers I could look into? The volumetric rendering does such a perfect job and I’d be a shame not to leverage those results into a widely usable format. Many thanks!</p>

---

## Post #11 by @pieper (2017-07-13 23:49 UTC)

<p>FYI we have a colleague visiting BWH from Basel who has a very nice volume renderer that runs at frame rates fast enough for virtual reality displays.  We are able to share some data from Slicer to his system but the connection (we can share volume data bur the transfer functions are independent).  Philippe’s system is not open source but he’s been interested in academic collaboration and may be able to share executables.  We’ve definitely discussed making his code into a Unity plugin.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.unibas.ch/en/News-Events/News/Uni-Research/Virtual-Reality-in-Medicine.html">
  <header class="source">
      <img src="https://www.unibas.ch/.resources/unibas-main/webresources/img/unibas.ico" class="site-icon" width="16" height="16">

      <a href="https://www.unibas.ch/en/News-Events/News/Uni-Research/Virtual-Reality-in-Medicine.html" target="_blank" rel="noopener">unibas.ch</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://www.unibas.ch/dam/jcr:1322adee-338c-4974-91e0-0ef95c061657/SpectoVive_1000x500.jpg" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://www.unibas.ch/en/News-Events/News/Uni-Research/Virtual-Reality-in-Medicine.html" target="_blank" rel="noopener">Virtual Reality in Medicine: New Opportunities for Diagnostics and Surgical...</a></h3>

  <p>Before an operation, surgeons have to obtain the most precise image possible of the anatomical structures of the part of the body undergoing surgery. University of Basel researchers have now developed a technology that uses computed tomography data...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Of course if there’s a way to leverage the VTK or other open source volume rendering directly in a VR headset that would be easier to integrate with Slicer, but that’s still a work in progress.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/171049f02ff97ade94d631856c66da958ea3d77b.jpg" data-download-href="/uploads/short-url/3i1SAtZDvY0M4bSpBd13YhWgQll.jpg?dl=1" title="image.jpg"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/171049f02ff97ade94d631856c66da958ea3d77b_2_690x345.jpg" width="690" height="345" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/171049f02ff97ade94d631856c66da958ea3d77b_2_690x345.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/171049f02ff97ade94d631856c66da958ea3d77b.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/171049f02ff97ade94d631856c66da958ea3d77b.jpeg 2x" data-dominant-color="B0A3A0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.jpg</span><span class="informations">1000×500 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><a href="https://www.unibas.ch/dam/jcr:1322adee-338c-4974-91e0-0ef95c061657/SpectoVive_1000x500.jpg">https://www.unibas.ch/dam/jcr:1322adee-338c-4974-91e0-0ef95c061657/SpectoVive_1000x500.jpg</a></p>

---

## Post #12 by @lassoan (2017-07-13 23:51 UTC)

<p>Volume rendering is equivalent to sculpting from colored semi-transparent material. Surface rendering is equivalent to painting on a semi-transparent surface. There is no conversion between them. Volume rendering does not even use a surface mesh while fbx file only stores a colored surface mesh. No matter how you process your data, surface rendering will not be able to reproduce the same look as volume rendering (except the special case when you only have 100% opaque objects with hard edges).</p>
<p>If you want to see volume rendering in Unity then you have to implement a volume renderer or find a volume renderer implementation for Unity (there are some, I don’t know how usable they are). If you don’t want to deal with volume rendering in Unity then you have to create a surface mesh by segmenting your image.</p>

---

## Post #13 by @maxabernathy (2017-07-17 08:41 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/pieper">@pieper</a> ! I had to do some reading but I get that it’s a display technique with no actual data transformation or vertex/shape operations/generations on Slicer’s part. I was confused because the module does such a good job at segmenting (if only visually) with one click whereas going through the segment editor is tedious and only semi-automatic. So obviously my brain wanted to take the easy road <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>I guess the alternative is then, like Andras wrote, to work on a pipeline which exports the segments in .stl and import them in Unity3d. Not a good solution however. Not being passive-aggressive but it’s ironic that Slicer implements stereoscopic viewing but no bridge to AR/VR platforms <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p><a class="mention" href="/u/pieper">@pieper</a> many thanks for the link to Spectovive. I don’t know if you have worked with SteamVR or a HTC Vive but this application, with identical functionalities, is a mini-game in a game called “The Lab” produced by Vive and shipped with the HTC Vive to showcase interactions. So I’m now wondering if the colleague you mentioned maybe had to do something with it. But please see for yourself, here’s a link at the correct time in the gameplay video (<a href="https://youtu.be/RtR-0waVOIA?t=452" rel="nofollow noopener">link</a>).</p>

---

## Post #14 by @maxabernathy (2017-07-17 09:05 UTC)

<p>FInally, I will leave a few links here if other people stumble on the thread in the future.</p>
<ul>
<li>
<a href="https://www.assetstore.unity3d.com/en/#!/content/83185" rel="nofollow noopener">Volume rendering Unity asset</a> (works with DICOMs)</li>
<li><a href="https://github.com/brianasu/unity-ray-marching/tree/volumetric-textures-depth" rel="nofollow noopener">Open source raymarching volume rendering library for Unity</a></li>
</ul>

---

## Post #15 by @cpinter (2017-07-17 13:14 UTC)

<aside class="quote no-group" data-username="maxabernathy" data-post="13" data-topic="524">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/maxabernathy/48/415_2.png" class="avatar"> maxabernathy:</div>
<blockquote>
<p>Not being passive-aggressive but it’s ironic that Slicer implements stereoscopic viewing but no bridge to AR/VR platforms</p>
</blockquote>
</aside>
<p>Please keep in mind that Slicer is an open-source platform with an enthusiastic community, and virtually no explicit funding for development any more. So contributions are welcome!</p>

---

## Post #16 by @maxabernathy (2017-07-17 13:34 UTC)

<p>I agree. I say this mainly because the software is at a quite sophisticated level while what I’m interested in is fairly trivial, not for me but in the greater picture. Would I be able to build this myself I would love to help!</p>

---

## Post #17 by @pieper (2017-07-17 13:40 UTC)

<p>Folks are working on OpenVR support in Slicer at the Project Week in London Ontario this week:</p>
<p><a href="http://wiki.imaging.robarts.ca/index.php/2017_Slicer_Western_Week/Virtual_Reality_and_Slicer" class="onebox" target="_blank">http://wiki.imaging.robarts.ca/index.php/2017_Slicer_Western_Week/Virtual_Reality_and_Slicer</a></p>

---

## Post #18 by @AveryCarter (2018-07-03 23:53 UTC)

<p>I made an account just to thank you all for this conversation. I’ve been messing around with unity and apple ARkit recently, and I was nearly tearing my hair out trying to figure out how to do this/ if it was possible. I’ve been bouncing back and fourth from InVesalius to Slicer with zero luck until I found this thread! So I’ll end my wild goosechase and settle on my boring stl for now. I completely agree with OP that this ability to somehow “export” that rendering (even though not possible) would streamline game development and applications within VR and AR. Cheers and thanks again!</p>

---

## Post #19 by @lassoan (2018-07-06 17:01 UTC)

<p>Note that augmented or virtual reality does not require STL. Slicer can already render beautiful volume rendered scenes without segmentation in virtual reality headsets, in color, in real-time, even in 4D, on any OpenVR-compatible headset (HTC Vive, any Windows mixed reality headsets, Oculus Rift, etc.), by a single click. Virtual reality provides solutions for many use cases that previously was only possible to address by 3D printing. Of course, for some cases 3D printing is still needed and the <a href="https://discourse.slicer.org/t/printing-volume-renderings-in-plastic/3017">volumetric printing</a> is a really nice option.</p>

---

## Post #20 by @avarghes23 (2018-11-09 15:47 UTC)

<p>Forgive me if I missed something here. But you’re basically saying that Volume Rendering works by generating a point cloud based on the intensities of the pixels from the input image stack (CT, MRI. US, etc.). Is there a way to export this point cloud to another program (like Meshlab) to generate a mesh and subsequently an STL?</p>
<p>Also, the Segment Editor is a fantastic tool in that it allows the user to define thresholds to filter out undesired noise. But in my experience, there are certain instances when both the thresholding and edge detection/fill between slices methods don’t capture all the necessary data, resulting in a segmented model that has to be further processed to achieve a manifold model. Personally, I think that the point cloud generated by the Volume Rendering module converts the input image stack to a rendered cloud perfectly and if there was a way that we could generate an STL, in theory it would have almost perfect contours that match the sample’s anatomy.</p>

---

## Post #21 by @lassoan (2018-11-09 16:16 UTC)

<aside class="quote no-group" data-username="avarghes23" data-post="20" data-topic="524">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/a9a28c/48.png" class="avatar"> avarghes23:</div>
<blockquote>
<p>Is there a way to export this point cloud to another program</p>
</blockquote>
</aside>
<p>Yes, of course! The point cloud is the 3D image volume file (usually saved in .nrrd file).</p>
<aside class="quote no-group" data-username="avarghes23" data-post="20" data-topic="524">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/a9a28c/48.png" class="avatar"> avarghes23:</div>
<blockquote>
<p>program (like Meshlab) to generate a mesh and subsequently an STL?</p>
</blockquote>
</aside>
<p>MeshLab and other mesh editors operate on meshes, they cannot load or display volumetric image data.</p>
<aside class="quote no-group" data-username="avarghes23" data-post="20" data-topic="524">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/a9a28c/48.png" class="avatar"> avarghes23:</div>
<blockquote>
<p>Rendering module converts the input image stack to a rendered cloud perfectly and if there was a way that we could generate an STL, i</p>
</blockquote>
</aside>
<p>STL is for storing surface mesh that you generate by segmenting a volume. Surface meshes can be printed using cheap plastic printers.</p>
<p>If you have access to a color voxel printer then <a href="https://discourse.slicer.org/t/printing-volume-renderings-in-plastic/3017">you can 3D print volume rendering directly, using images created by SlicerFab extension’s BitmapGenerator module</a>.</p>

---

## Post #22 by @muratmaga (2018-11-09 16:27 UTC)

<p>Volume rendering does not generate a point cloud. It visualizes surfaces based on the intensity range and opacity values user specified in the transfer function. For STL and likes you need to use the segment editor and extract the surface you desire to keep. If single threshold doesnt define the structure you want to generate the model for, you will need to use the additional tools to make a cleaner segmentation.</p>

---

## Post #23 by @sarvpriya1985 (2018-12-27 16:53 UTC)

<p>Hi,</p>
<p>I just came across this discussion of seeing volume rendered in virtual reality.<br>
For now I segment the heart and then see that in virtual reality.</p>
<ol>
<li>Can I do the same by simply converting 3D dataset into volume rendering and use in virtual reality.</li>
<li>Can I load multiple phases and convert them into volume render model and see that cardiac motion in real time under virtual reality. If yes, how.</li>
<li>I asked this another post as well. When I showed the virtual models to a surgeon, he had different requests. They are not that interested in seeing the inside of heart but rather fixing it. For that as I earlier asked, creating "accurate 3d patches for fixing holes, arterioplasties.</li>
</ol>
<p>I know these are lot of questions, but would appreciate thoughts and help.</p>
<p>Thanks,<br>
Sarv</p>

---

## Post #24 by @cpinter (2018-12-28 19:47 UTC)

<aside class="quote no-group" data-username="sarvpriya1985" data-post="23" data-topic="524">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sarvpriya1985/48/4094_2.png" class="avatar"> sarvpriya1985:</div>
<blockquote>
<p>Can I do the same by simply converting 3D dataset into volume rendering and use in virtual reality</p>
</blockquote>
</aside>
<p>There is nothing to convert, just go to the Volume Rendering module, show the volume you want, choose a fitting preset, and use the Shift slider to adjust the transfer function</p>
<aside class="quote no-group" data-username="sarvpriya1985" data-post="23" data-topic="524">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sarvpriya1985/48/4094_2.png" class="avatar"> sarvpriya1985:</div>
<blockquote>
<p>Can I load multiple phases and convert them into volume render model and see that cardiac motion in real time under virtual reality. If yes, how</p>
</blockquote>
</aside>
<p>You can show the proxy volume in volume rendering as I described above. When you’re playing the sequence, the volume will “animate”.</p>
<aside class="quote no-group" data-username="sarvpriya1985" data-post="23" data-topic="524">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sarvpriya1985/48/4094_2.png" class="avatar"> sarvpriya1985:</div>
<blockquote>
<p>They are not that interested in seeing the inside of heart but rather fixing it</p>
</blockquote>
</aside>
<p>Please elaborate.</p>

---

## Post #25 by @willyci (2019-01-31 18:36 UTC)

<p>for now are you just using surface rendering to build the 3d model to see in VR?</p>
<p>what kind dataset do you have to convert into volume rendering?</p>
<p>cardiac motion image just one slice, right? not sure how you can render 3D from that.</p>

---

## Post #26 by @sarvpriya1985 (2019-02-03 12:31 UTC)

<p>Hi,<br>
I did try using volume rendered CT to display as virtual reality but I was not able to do so for multiple phases. I had to shelf the project as I was unable to segment multiple phases of heart after multiple tries.</p>
<p>Sarv</p>

---

## Post #27 by @cpinter (2019-02-12 19:14 UTC)

<p>A post was split to a new topic: <a href="/t/show-volume-rendered-ct-in-vr/5745">Show volume rendered CT in VR</a></p>

---

## Post #28 by @nayanw775 (2021-03-24 10:48 UTC)

<p>Hi,<br>
Sorry for the silly question but I am totally new slicer and have been able to manage to make our own Neuronavigation, thanks for such an amazing software and community.</p>
<p>I was also having the same of exporting the volume rendering as a Model and cam across this amazing thread<br>
This thread do discuss about exporting the transfer functions of volume rendering, but  didn’t mention how to do that,<br>
Can anyone please help me that.</p>
<p>Thanks<br>
Nayan</p>

---

## Post #29 by @muratmaga (2021-03-24 15:04 UTC)

<aside class="quote no-group" data-username="nayanw775" data-post="28" data-topic="524">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/nayanw775/48/9963_2.png" class="avatar"> nayanw775:</div>
<blockquote>
<p>exporting the volume rendering as a Model</p>
</blockquote>
</aside>
<p>Volume rendering is a visualization technique not a segmentation method; it does not create a 3D surface that can be exported as a model. To do that you need to use the Segment Editor and Segmentations module. See this image that explains different data representaiton in slicer and how they relate to each other</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/176367250220ed2cf4be82ba41ba5a1b50bf6cb2.jpeg" data-download-href="/uploads/short-url/3kTWZPEnjZFKNlzfgKCZG2MIAjE.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/176367250220ed2cf4be82ba41ba5a1b50bf6cb2_2_690x368.jpeg" alt="image" data-base62-sha1="3kTWZPEnjZFKNlzfgKCZG2MIAjE" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/176367250220ed2cf4be82ba41ba5a1b50bf6cb2_2_690x368.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/176367250220ed2cf4be82ba41ba5a1b50bf6cb2_2_1035x552.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/176367250220ed2cf4be82ba41ba5a1b50bf6cb2_2_1380x736.jpeg 2x" data-dominant-color="D8DFD7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1756×937 308 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #30 by @chendong9416 (2021-06-08 15:14 UTC)

<p>radiant can transfer volume rendering into stl file</p>

---

## Post #32 by @chendong9416 (2021-06-08 15:20 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb74b0326b9a10d8073a2e7e8b9cef8ef64d2555.jpeg" data-download-href="/uploads/short-url/t1QVEMKTHYY8jol3lfwXTye3qcZ.jpeg?dl=1" title="IMG_20210608_231736" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cb74b0326b9a10d8073a2e7e8b9cef8ef64d2555_2_281x500.jpeg" alt="IMG_20210608_231736" data-base62-sha1="t1QVEMKTHYY8jol3lfwXTye3qcZ" width="281" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cb74b0326b9a10d8073a2e7e8b9cef8ef64d2555_2_281x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cb74b0326b9a10d8073a2e7e8b9cef8ef64d2555_2_421x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cb74b0326b9a10d8073a2e7e8b9cef8ef64d2555_2_562x1000.jpeg 2x" data-dominant-color="665A53"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_20210608_231736</span><span class="informations">765×1360 280 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #33 by @muratmaga (2021-06-08 15:25 UTC)

<p>I am not familiar with Radiant. A google search shows it as a DICOM viewer with limited capabilities (<a href="https://www.radiantviewer.com/">https://www.radiantviewer.com/</a>).</p>
<p>While they didn’t list segmentation as feature. But perhaps it is available as a add-on of some sorts. Yes, you can save a 3D model as STL in Slicer too (after segmenting it). However, a 3D model is not created from volume rendering.</p>

---

## Post #34 by @chendong9416 (2021-06-08 15:27 UTC)

<p>Radiant direct transfer volume rendering into stl file，so I think there must be a way in 3D slicer</p>

---

## Post #35 by @lassoan (2021-06-08 20:13 UTC)

<p>The feature that people are looking for in this topic is the ability to automatically generate a colored surface model that looks like volume rendering. It is theoretically impossible to achieve this in general and RadiANT does not do this either. I guess RadiANT exports the usual noisy, monochrome isosurface to STL file, which is nowhere near what you can visualize with volume rendering. Maybe you could post a few links to example models or at least screenshots of those models.</p>
<p>If you use a surface mesh file format that can store full-color meshes (OBJ, PLY, …) then you could assemble nicer-looking surface models from many transparent layers, but it would not be usable for 3D-printing; and rendering of such semi-transparent models would be probably much more complicated and less efficient than direct volume rendering using raycasting. So, there is no incentive to implement generation of such models.</p>

---

## Post #36 by @lassoan (2021-10-21 04:22 UTC)

<p>A post was split to a new topic: <a href="/t/dropping-point-on-a-rendered-model/20279">Dropping point on a rendered model</a></p>

---

## Post #37 by @Yihao_Liu (2021-10-20 19:37 UTC)

<p>I am working on something that involves dropping a markup point on a rendered model. From the previous discussion in this thread, I realized volume model have to be segmented to obtain a surface model. So, a question I have is that, what algorithm is used in the markup extension when we drop a markup point on a rendered model? It seems to me the markup is automatically on the surface.</p>
<p>I assume a way to obtain a surface can be: first obtain a sufficient number of markups (maybe in background), then do Delaunay triangulation. I wonder if this is a valid assumption, or I am missing something important.</p>

---

## Post #38 by @lassoan (2021-10-21 04:23 UTC)

<p>You can drop points on both volume rendering and and models. In both cases the first intersection of the view ray and the object is used as 3D position.</p>

---

## Post #39 by @Yihao_Liu (2021-10-21 04:35 UTC)

<p>If we can drop a markup by obtaining the intersection of the view ray and the object, I suppose obtaining the surface of the rendered volume is also possible. Does this imply that the “object” has certain boundary? I am a little confused from the discussion in this thread <a href="https://discourse.slicer.org/t/save-volume-rendering-as-stl-file/524/4">stl vs rendered volume</a> where you answered:</p>
<blockquote>
<p>Volume rendering displays a semi-transparent cloud, but for 3D printing you need hard boundaries that exactly define what is inside/outside</p>
</blockquote>
<p>I think I am missing some background regarding this, so I appologize if this was a dumb question.</p>

---

## Post #40 by @lassoan (2021-10-21 05:02 UTC)

<p>Appearance of a “surface” point in a volume rendering depends on what is behind, inside the volume. Therefore, position of the point that the volume raycaster picks depends on the view ray angle orientation. So, <strong>you can extract a nice colored surface patch from a single orientation</strong>.</p>
<p>However, if you then rotate the volume a little bit and extract another surface patch then you cannot assemble those two surface patches into a single mesh. The surface patches will intersect and/or not touch each other.</p>
<p>Maybe another example would help understanding the difference between surface rendering and volume rendering. Here is a jellyfish:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dca00ad54811b11856d623eb1968c55f2e938ddd.jpeg" data-download-href="/uploads/short-url/vtJVOQg7oxTIWY0TJLqNzndjD6R.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dca00ad54811b11856d623eb1968c55f2e938ddd_2_332x499.jpeg" alt="image" data-base62-sha1="vtJVOQg7oxTIWY0TJLqNzndjD6R" width="332" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dca00ad54811b11856d623eb1968c55f2e938ddd_2_332x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dca00ad54811b11856d623eb1968c55f2e938ddd_2_498x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dca00ad54811b11856d623eb1968c55f2e938ddd_2_664x998.jpeg 2x" data-dominant-color="22293C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1200×1802 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>If you acquire an RGB volume of this jellyfish then you can generate an image exactly like this using volume rendering, from any angles.</p>
<p>However, using surface rendering what you could display would be equivalent to a solid plastic model of the jellyfish with some color pattern painted on the surface. You could paint it so that from one side it looks exactly as the semitransparent real colorful jellyfish, but there is no pattern that you can paint on the surface that would reproduce the appearance from all viewing angles.</p>

---

## Post #41 by @slicer365 (2021-10-21 07:13 UTC)

<p>Model from Radiant,  the model is from the Radiant’s Volume Rendering<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b5dd0a7d99e955c9f4f9694471ee1bd62849fb38.jpeg" data-download-href="/uploads/short-url/pWQ0115wsDu2uMI5W9eCOm3sZ4Y.jpeg?dl=1" title="1634800055(1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b5dd0a7d99e955c9f4f9694471ee1bd62849fb38_2_294x250.jpeg" alt="1634800055(1)" data-base62-sha1="pWQ0115wsDu2uMI5W9eCOm3sZ4Y" width="294" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b5dd0a7d99e955c9f4f9694471ee1bd62849fb38_2_294x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b5dd0a7d99e955c9f4f9694471ee1bd62849fb38_2_441x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b5dd0a7d99e955c9f4f9694471ee1bd62849fb38_2_588x500.jpeg 2x" data-dominant-color="695C4B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1634800055(1)</span><span class="informations">705×599 27.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/176e2991b9f4b9cff57925f5cc764b97128327fa.jpeg" data-download-href="/uploads/short-url/3lh0dXhKYG7EUrW6DWzXfmp6RGq.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/176e2991b9f4b9cff57925f5cc764b97128327fa_2_304x250.jpeg" alt="image" data-base62-sha1="3lh0dXhKYG7EUrW6DWzXfmp6RGq" width="304" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/176e2991b9f4b9cff57925f5cc764b97128327fa_2_304x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/176e2991b9f4b9cff57925f5cc764b97128327fa_2_456x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/176e2991b9f4b9cff57925f5cc764b97128327fa_2_608x500.jpeg 2x" data-dominant-color="8A9198"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">634×521 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aabb5feff7d53fc80051f2c5472dacf96fd0fe20.jpeg" data-download-href="/uploads/short-url/ommClEZdmndGZgxajHZOxFTGK8U.jpeg?dl=1" title="1634800100(1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aabb5feff7d53fc80051f2c5472dacf96fd0fe20_2_292x250.jpeg" alt="1634800100(1)" data-base62-sha1="ommClEZdmndGZgxajHZOxFTGK8U" width="292" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aabb5feff7d53fc80051f2c5472dacf96fd0fe20_2_292x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aabb5feff7d53fc80051f2c5472dacf96fd0fe20_2_438x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aabb5feff7d53fc80051f2c5472dacf96fd0fe20_2_584x500.jpeg 2x" data-dominant-color="8E98A0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1634800100(1)</span><span class="informations">650×555 78.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c53ae13fd4ee3d4fed1532056117f0342f9565d.jpeg" data-download-href="/uploads/short-url/fsiQINW329AyDmrKhK8VmHlpv77.jpeg?dl=1" title="1634800314(1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6c53ae13fd4ee3d4fed1532056117f0342f9565d_2_314x250.jpeg" alt="1634800314(1)" data-base62-sha1="fsiQINW329AyDmrKhK8VmHlpv77" width="314" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6c53ae13fd4ee3d4fed1532056117f0342f9565d_2_314x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6c53ae13fd4ee3d4fed1532056117f0342f9565d_2_471x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6c53ae13fd4ee3d4fed1532056117f0342f9565d_2_628x500.jpeg 2x" data-dominant-color="7E5D3A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1634800314(1)</span><span class="informations">689×548 32.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f0d76b7bec5bb484116ecf37cefdbfe77c15235.jpeg" alt="1634800365(1)" data-base62-sha1="6IfhNoxsZANueEY2a1gIPnUYdet" width="291" height="242"></p>

---

## Post #42 by @lassoan (2021-10-21 14:52 UTC)

<aside class="quote no-group" data-username="slicer365" data-post="41" data-topic="524">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/slicer365/48/67549_2.png" class="avatar"> slicer365:</div>
<blockquote>
<p>Model from Radiant, the model is from the Radiant’s Volume Rendering</p>
</blockquote>
</aside>
<p>The images above with black background use volume rendering (raycasting) and those with blue background use surface rendering (rendering of polygonal meshes obtained using segmentation). You can see the difference between quality and level of detail.</p>
<p>Even though the skin and bone surface have very strong boundaries (so volume rendering is quite surface-rendering-like), surface rendering limitations are visible near the sutures and near the orbital bone, and for the skin rendering near the small wedges near the eyes and ears. Since the depth of the features are quite shallow, you could capture them as texture using “Probe volume with model” module - see how it is done <a href="https://discourse.slicer.org/t/retain-image-color-in-volume-rendering/12294/24">here</a>:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/2X/4/43242f476836a72628642f4fbd41a544539749c1.jpeg" data-download-href="/uploads/short-url/9zXvYUGxwsRvMn2XLlzW1udlYBP.jpeg?dl=1" title=""><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43242f476836a72628642f4fbd41a544539749c1.jpeg" alt="" role="presentation" width="644" height="500" data-dominant-color="81778A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename"></span><span class="informations">691×536 70.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But surface rendering, even with textures, would never be able to come near to rendering structures that have more transparency, such as this:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="o5I_XWkm1nk" data-video-title="Color volume rendering" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=o5I_XWkm1nk" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/o5I_XWkm1nk/maxresdefault.jpg" title="Color volume rendering" width="" height="">
  </a>
</div>


---
