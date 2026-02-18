# Heart: 3D Printing/ 3D PDF view

**Topic ID**: 5012
**Date**: 2018-12-07
**URL**: https://discourse.slicer.org/t/heart-3d-printing-3d-pdf-view/5012

---

## Post #1 by @sarvpriya1985 (2018-12-07 19:53 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11<br>
Expected behavior:<br>
Actual behavior:<br>
I got two requests today from one of the cardiologists.</p>
<ol>
<li>One was if  I can cut the heart into two halves and then keep them both into display monitor as on top of each other. This way when we print those models we can have two halves. Question: When i cut using scissor, that part is gone and i am left with remaining part. How to fix that.</li>
<li>Second question was if I can export 3D files to be viewed in PDF (it’s a kind of 3d PDF viewer, where you can zoom, rotate and pan models: He showed me an example from 3D matic PDF: I think it’s MIMICS software.</li>
</ol>
<p>Would appreciate thoughts on these two.</p>
<p>Thanks,<br>
Sarv</p>

---

## Post #2 by @lassoan (2018-12-08 01:00 UTC)

<aside class="quote no-group" data-username="sarvpriya1985" data-post="1" data-topic="5012">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sarvpriya1985/48/4094_2.png" class="avatar"> sarvpriya1985:</div>
<blockquote>
<p>if I can cut the heart into two halves and then keep them both</p>
</blockquote>
</aside>
<p>You can use Scissors effect to move the cutout part to another segment as shown in this recipe: <a href="https://lassoan.github.io/SlicerSegmentationRecipes/Craniotomy/" class="inline-onebox">Overview | 3D Slicer segmentation recipes</a></p>
<aside class="quote no-group" data-username="sarvpriya1985" data-post="1" data-topic="5012">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sarvpriya1985/48/4094_2.png" class="avatar"> sarvpriya1985:</div>
<blockquote>
<p>Second question was if I can export 3D files to be viewed in PDF</p>
</blockquote>
</aside>
<p>There are so many alternatives to view 3D models that I’m not sure if PDF3D is worth the trouble (PDF3D is not easy to create and it is not usable for anything else than viewing in a PDF viewer - no 3D printable, not editable, not importable to any software).</p>
<ol>
<li>
<p>Several online file storage service can show 3D files in your web browser. For example, you can upload the STL file that Slicer exported to GitHub and view there: <a href="https://github.com/PlusToolkit/PlusModelCatalog/blob/master/Anatomy/HumanSimple.stl" class="inline-onebox">PlusModelCatalog/Anatomy/HumanSimple.stl at master · PlusToolkit/PlusModelCatalog · GitHub</a></p>
</li>
<li>
<p>There are many STL and OBJ viewers on all platforms.</p>
</li>
<li>
<p>You can save STL and OBJ files in Word documents and Powerpoint slides and you can view/rotate them around.</p>
</li>
<li>
<p>If sometimes you do need PDF3D then you can use a converter such as <a href="https://www.pdf3d.com/">https://www.pdf3d.com/</a></p>
</li>
</ol>
<p>If many users requested direct 3D PDF export then we could add <a href="https://en.wikipedia.org/wiki/Universal_3D">u3d file</a> export to Slicer, which can be embedded into PDF documents (for developers: <a href="https://github.com/ningfei/u3d">u3d library</a>, <a href="http://vtk.1045678.n5.nabble.com/exporter-to-u3d-3D-PDF-td1246440.html">more info</a>).</p>

---

## Post #3 by @sarvpriya1985 (2018-12-08 05:05 UTC)

<p>Thanks Andras</p>
<p>I will try those platforms to view 3D models. I haven’t tried importing Obj files in word or power point but if they work that will be good too.</p>
<p>Thanks again</p>
<p>Sarv</p>

---

## Post #4 by @sarvpriya1985 (2018-12-09 22:29 UTC)

<p>Thanks Andras.<br>
Also when I export files as OBJ or STL, they lose their colour as well as all the labels. Is their way the label remains as then it is easy to view by others.</p>
<p>Thanks,</p>
<p>Sarv</p>

---

## Post #5 by @lassoan (2018-12-09 23:51 UTC)

<p>If you save as OBJ then colors are preserved.</p>
<p>There is no standard way of storing color in STL (some software use some workarounds that we could easily adopt, but this has not been a commonly requested feature).</p>
<p>We are working with <a href="https://www.openanatomy.org" rel="nofollow noopener">OpenAnatomy</a> people to define an open, standard format for storing annotated models and add support for that in Slicer. We expect to have exporter/importer in Slicer in a couple of months. There is already an OpenAnatomy web viewer (see their website).</p>

---

## Post #6 by @apparrilla (2020-09-25 20:42 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="5012">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If many users requested direct 3D PDF export then we could add <a href="https://en.wikipedia.org/wiki/Universal_3D" rel="noopener nofollow ugc">u3d file </a> export to Slicer</p>
</blockquote>
</aside>
<p>It should be really usefull, at least for me…</p>

---

## Post #7 by @lassoan (2020-09-25 21:11 UTC)

<p>I still don’t understand the need for PDF3D. It is an old format that essentially failed (did not become popular). It is not easy to create and it is not usable for anything else than viewing in a PDF viewer - not 3D printable, not editable, not importable into any software. Is there any platform or environment or application where PDF3D is better than other widely used mesh formats?</p>

---

## Post #8 by @apparrilla (2020-09-25 21:51 UTC)

<p>In my particular case, it´s to generate reports to share. PDF viewer is something almost everyone have in every digital device under any OS. That´s the only porpose, but if you say PDF 3D view doesn´t work properly…<br>
Thanks.</p>

---

## Post #9 by @lassoan (2020-09-26 04:29 UTC)

<p>PDF3D works, it has just become largely irrrelevant.</p>
<ol>
<li>
<p>You can drop 3D models in standard file format (STL, OBJ, …) into Word or PowerPoint. Anybody can open the file and rotate the model around.</p>
</li>
<li>
<p>Web browsers on your PC, tablet, phone, etc. have become so powerful that you don’t need apps for displaying objects in standard 3D file formats. There are lots of online viewers that just needs a URL of your model file and they can show it in your browser.</p>
</li>
</ol>
<p>How to export a model from Slicer and create a link for viewing it in a web browser:</p>
<ul>
<li>Export segmentation to OBJ format using OpenAnatomy Exporter module (provided by SlicerOpenAnatomy extension)</li>
<li>put them in a folder that has the same name as the .obj file and zip it</li>
<li>open this URL in your web browser (on your desktop, table, or phone) and open the zip file in it: <a href="https://kitware.github.io/vtk-js/examples/OBJViewer/OBJViewer.html">https://kitware.github.io/vtk-js/examples/OBJViewer/OBJViewer.html</a>
</li>
</ul>
<p>You can also create a direct “view in browser” link that you can send to anyone:</p>
<ul>
<li>get a direct download link
<ul>
<li>for example, upload to Dropbox and replace the beginning of your default download URL by <code>https://dl.dropboxusercontent.com/</code>
</li>
</ul>
</li>
<li>create a viewer URL by adding this before your download URL: <code>https://kitware.github.io/vtk-js/examples/OBJViewer/OBJViewer.html?fileURL=</code>
</li>
</ul>
<p>Example URL for the SPL knee atlas: <a href="https://kitware.github.io/vtk-js/examples/OBJViewer/OBJViewer.html?fileURL=https://dl.dropboxusercontent.com/s/1ymrrdpy563w6jv/knee.zip">https://kitware.github.io/vtk-js/examples/OBJViewer/OBJViewer.html?fileURL=https://dl.dropboxusercontent.com/s/1ymrrdpy563w6jv/knee.zip</a></p>
<p>There are lots of other web viewers based on vtk.js, babylon.js, three.js that you can use instead of a proprietary PDF3D viewer.</p>
<p>Check out these examples just to see what’s possible:</p>
<ul>
<li><a href="https://www.openanatomy.org/atlases/nac/brain-2017-01/viewer/">https://www.openanatomy.org/atlases/nac/brain-2017-01/viewer/</a></li>
<li><a href="https://kitware.github.io/vtk-js/examples/">https://kitware.github.io/vtk-js/examples/</a></li>
<li><a href="https://threejs.org/examples/#webgl_loader_gltf">https://threejs.org/examples/#webgl_loader_gltf</a></li>
<li><a href="https://threejs.org/examples/#webgl_loader_nrrd">https://threejs.org/examples/#webgl_loader_nrrd</a></li>
</ul>
<p>3D object web viewers:</p>
<ul>
<li><a href="https://sandbox.babylonjs.com/">https://sandbox.babylonjs.com/</a></li>
<li><a href="https://kitware.github.io/vtk-js/examples/OBJViewer.html">https://kitware.github.io/vtk-js/examples/OBJViewer.html</a></li>
<li><a href="https://www.creators3d.com/online-viewer">https://www.creators3d.com/online-viewer</a></li>
<li><a href="https://3dviewer.net/">https://3dviewer.net/</a></li>
</ul>

---

## Post #10 by @lassoan (2020-09-26 04:32 UTC)

<p>I’ve figured that you can even embed these 3D viewers here. This might be useful for quickly sharing models or volumes here in the forum.</p>
<p>For example:</p>
<iframe width="480" height="373" frameborder="0" marginheight="0" marginwidth="0" src="https://kitware.github.io/vtk-js/examples/OBJViewer/OBJViewer.html?fileURL=https://dl.dropboxusercontent.com/s/1ymrrdpy563w6jv/knee.zip">
</iframe>
<details>
<summary>
Click here to see the text to write in your post to show this viewer</summary>
<pre><code class="lang-auto">&lt;iframe width="480" height="373" frameborder="0" scrolling="no" marginheight="0"
 marginwidth="0" id="kitware-obj-viewer"
 title="Object viewer"
 src="https://kitware.github.io/vtk-js/examples/OBJViewer/OBJViewer.html?fileURL=https://dl.dropboxusercontent.com/s/1ymrrdpy563w6jv/knee.zip"&gt;
&lt;/iframe&gt;
</code></pre>
</details>
<iframe width="480" height="373" frameborder="0" marginheight="0" marginwidth="0" src="https://kitware.github.io/vtk-js/examples/VolumeViewer/VolumeViewer.html?fileURL=https://data.kitware.com/api/v1/item/59e12e988d777f31ac6455c5/download">
</iframe>
<details>
<summary>
Click here to see the text to write in your post to show this viewer</summary>
<pre><code class="lang-auto">&lt;iframe width="480" height="373" frameborder="0" scrolling="no" marginheight="0"
 marginwidth="0" id="kitware-vol-viewer"
 title="Volume viewer"
 src="https://kitware.github.io/vtk-js/examples/VolumeViewer/VolumeViewer.html?fileURL=https://data.kitware.com/api/v1/item/59e12e988d777f31ac6455c5/download"&gt;
&lt;/iframe&gt;
</code></pre>
</details>

---

## Post #11 by @apparrilla (2020-09-26 09:56 UTC)

<p>Woderfull!!! Nice way to share segmentataions and models with colleagues. Thanks a lot.</p>

---

## Post #12 by @apparrilla (2020-09-26 12:33 UTC)

<p>Just one question… How can I export my volumes in vti format?</p>

---

## Post #13 by @lassoan (2020-09-26 15:03 UTC)

<p>I’ve added an “Image export” section in OpenAnatomy Exporter module (in SlicerOpenAnatomy). It’ll be available in tomorrow’s Slicer Preview Release.</p>
<p>Until then, you can export by typing this into the Python interactor (replace node name and output location):</p>
<pre><code class="lang-python">volumeNode = getNode('CTACardio')
writer=vtk.vtkXMLImageDataWriter()
writer.SetFileName("c:/Users/andra/Dropbox/models/ctacardio.vti")
writer.SetInputData(volumeNode.GetImageData())
writer.SetCompressorTypeToZLib()
writer.Write()
</code></pre>

---

## Post #14 by @mangotee (2020-09-26 16:56 UTC)

<p>Wow… Amazing <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"> Thanks for sharing this tip!</p>

---

## Post #15 by @RayCui (2020-10-19 10:00 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="5012">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If many users requested direct 3D PDF export then we could add <a href="https://en.wikipedia.org/wiki/Universal_3D" rel="noopener nofollow ugc">u3d file </a> export to Slicer,</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a> Hi, Andras. Is there a way to convert many segmentationNode to a u3d file? Does it can implemented by python vtk lib?</p>
<p>Look forward to your reply.</p>

---

## Post #16 by @lassoan (2020-10-19 13:12 UTC)

<p>PDF3D and the almost-never-heard-of u3d file format are so obsolete technology that you cannot expect any free, open-source developers to care about them. <a href="https://aecmag.com/technology-mainmenu-35/444-the-future-of-3d-pdf">Adobe dissolved its PDF3D development team more than a decade ago</a>, there have not been any improvement in the format since then, and there are many <a href="https://boxshot.com/3d-pdf/alternatives/">modern, more capable alternatives</a>.</p>
<p>Development and licensing cost of a custom software implementation would cost several thousands of dollars, so if you really must create PDF3D files then it is much less expensive and less risky to buy a converter that can create PDF3D file from common <a href="https://slicer.readthedocs.io/en/latest/user_guide/supported_data_formats.html#models">mesh file formats that Slicer can write</a>.</p>

---

## Post #17 by @RayCui (2020-10-20 01:37 UTC)

<p>I see. Thank you for your enthusiastic answer.</p>

---

## Post #18 by @Eserval (2021-11-25 05:45 UTC)

<p>Hello friends,</p>
<p>Thanks for the answers. The great part of 3D PDF is the file size. 5MB is enough to share a complete exam. We can send it from whatsapp and open on the cellphone. Does anyone have a similar simple tool?</p>

---

## Post #19 by @lassoan (2021-11-25 13:36 UTC)

<p>The whole topic is about describing various alternatives. They are all slightly different than the workflow that you described but they have many advantages over 3D pdf. For example: the pdf viewer cannot display 3D volumes as your browser can do - see <a href="https://discourse.slicer.org/t/heart-3d-printing-3d-pdf-view/5012/10">above</a>. The PDF viewer can display meshes, but how would you go about 3D printing or editing that mesh?</p>
<p>If you describe your overall goal, what kind of data to share (image, mesh, segmentation, etc), for what purpose (e.g., quality check before 3D printing, verification of implant size and placement, etc.) then we can think about a much better solution than the dead end 3D PDF.</p>

---

## Post #20 by @rbumm (2021-11-25 14:41 UTC)

<aside class="quote quote-modified" data-post="9" data-topic="5012">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/heart-3d-printing-3d-pdf-view/5012/9">Heart: 3D Printing/ 3D PDF view</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    PDF3D works, it has just become largely irrrelevant. 


You can drop 3D models in standard file format (STL, OBJ, …) into Word or PowerPoint. Anybody can open the file and rotate the model around. 


Web browsers on your PC, tablet, phone, etc. have become so powerful that you don’t need apps for displaying objects in standard 3D file formats. There are lots of online viewers that just needs a URL of your model file and they can show it in your browser. 


How to export a model from Slicer and c…
  </blockquote>
</aside>

<p>This should be starred/upvoted/documented somewhere.</p>

---

## Post #21 by @lassoan (2021-12-17 20:39 UTC)

<p>There are better web viewers now! See for example the <a href="http://3dviewer.net">3dviewer.net</a> and some example segmentation visualizations here:</p>
<aside class="quote quote-modified" data-post="7" data-topic="21082">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/is-there-any-way-to-export-the-model-by-fbx-format/21082/7">Is there any way to export the model by FBX format?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I’ve updated the OpenAnatomy Exporter module to export model names and all the hierarchy folders, which displayed well in <a href="http://3dviewer.net">3dviewer.net</a> and other gltTF viewers. 
See a model loaded into the interactive 3D viewer GUI by <a href="https://3dviewer.net/#model=https://raw.githubusercontent.com/lassoan/Test/master/SPL-Abdominal-Atlas.gltf">clicking here</a>. You can click on the volume to find the clicked object’s name, show/hide individual objects or group of objects, etc. 
<a href="https://3dviewer.net/#model=https://raw.githubusercontent.com/lassoan/Test/master/SPL-Abdominal-Atlas.gltf">[image]</a> 
The viewer can be embedded in any site, for example here is the SPL abdominal atlas exported using OpenAnatomy Exporter module (it is an in…
  </blockquote>
</aside>


---

## Post #22 by @slicer365 (2021-12-20 15:41 UTC)

<p>Today I find this topic, it is very useful! <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=10" title=":smiley:" class="emoji" alt=":smiley:"></p>
<p>Is there any way to play DICOM data(dcm or nrrd ) through web？</p>

---

## Post #23 by @lassoan (2021-12-20 15:48 UTC)

<p>If you want to see both surface mesh and image then the <a href="https://www.openanatomy.org/atlases/nac/head-neck-2016-09/viewer/">OpenAnatomy viewer</a> could be a good option.</p>
<p>For a traditional radiology viewer (2D oriented, image-only), you can use the OHIF viewer, for example in <a href="https://kheops.online/">Kheops</a>.</p>

---

## Post #25 by @Eserval (2022-03-02 21:39 UTC)

<p>Hello everyone,</p>
<p>I’m having some trouble exporting my models as OBJ. file and trying to open in platforms like Online 3D viewer. The first problem is related to opacity. The segments that are solid (100% opaque) are invisible and when I make them transparent (before creating the OBJ.) they appear opaque in the Online 3D Viewer (image). Another problem is related to the colors, everything very dark and lackluster when I invert the opacities of segments. The name of the segments also does not appear, only a code (image)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1d6e248bead620d08d3cc61b7807e0d7a3a534a.jpeg" data-download-href="/uploads/short-url/rEMxnUe5hTtEa7xFUf4ELwuYgSS.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1d6e248bead620d08d3cc61b7807e0d7a3a534a_2_690x336.jpeg" alt="image" data-base62-sha1="rEMxnUe5hTtEa7xFUf4ELwuYgSS" width="690" height="336" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1d6e248bead620d08d3cc61b7807e0d7a3a534a_2_690x336.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1d6e248bead620d08d3cc61b7807e0d7a3a534a_2_1035x504.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1d6e248bead620d08d3cc61b7807e0d7a3a534a_2_1380x672.jpeg 2x" data-dominant-color="F8F7F5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1864×908 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #26 by @lassoan (2022-03-13 14:06 UTC)

<p>You need to use the latest Slicer Preview Release. Why have implemented name, hierarchy, opacity improvements there. Colors look differs by because glTF using PBR lighting model and Slicer uses Gouraud by default. In the short term you can get more lively color by choosing lighter and more saturated colors in Slicer. Improving PBR support in the OpenAnatomy exporter is a work in progress, I’ll drop a note here when it is ready for testing.</p>

---

## Post #27 by @lassoan (2022-03-17 15:17 UTC)

<p>I’ve updated SlicerOpenAnatomy extension to use PBR colors directly for models that use PBR interpolation. For segmentation or models that use Gouraud interpolation the color saturation is now boosted when exported to glTF, so the colors should look better.</p>

---

## Post #28 by @mvergnat (2024-03-04 08:16 UTC)

<p>Dear Dr. Lasso and 3dslicer community,</p>
<p>I wanted to share with a friend a segmentation that I performed.<br>
Problem is: my friend is not nerd…therefore I checked on forum the 3d pdf solution.<br>
I carefully read the topic und fully understand the problem with 3dpdf.<br>
Therefore I tried the recommendations of the topic:<br>
I followed the post of september 2020:<br>
" How to export a model from Slicer and create a link for viewing it in a web browser:</p>
<ul>
<li>Export segmentation to OBJ format using OpenAnatomy Exporter module (provided by SlicerOpenAnatomy extension)</li>
<li>put them in a folder that has the same name as the .obj file and zip it</li>
<li>open this URL in your web browser (on your desktop, table, or phone) and open the zip file in it: <a href="https://kitware.github.io/vtk-js/examples/OBJViewer/OBJViewer.html" rel="noopener nofollow ugc">https://kitware.github.io/vtk-js/examples/OBJViewer/OBJViewer.html </a>"</li>
</ul>
<p>this is my segments:<br>
</p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7cf105540253faca09ef65c57a1ae7a2bf2ab4c1.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/903d5c3bafed41de804a80de6604b4b07047d7a0.jpeg">
  </div><p></p>
<p>I did the OBJ using the openAnatomy Exporter module. I did a zip.</p>
<p>then, when I use the <a href="http://kitware.github.io/vtk-js" class="inline-onebox" rel="noopener nofollow ugc">vtk.js</a><br>
it worked, BUT unfortunately without colors:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/28b6b0d38650879f1661dabaa051ff6b2bc732c5.jpeg" data-download-href="/uploads/short-url/5OavJJjtIi0qyVRVSpusPlXKPiZ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/28b6b0d38650879f1661dabaa051ff6b2bc732c5_2_690x388.jpeg" alt="image" data-base62-sha1="5OavJJjtIi0qyVRVSpusPlXKPiZ" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/28b6b0d38650879f1661dabaa051ff6b2bc732c5_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/28b6b0d38650879f1661dabaa051ff6b2bc732c5_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/28b6b0d38650879f1661dabaa051ff6b2bc732c5_2_1380x776.jpeg 2x" data-dominant-color="262626"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 165 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I read on the rest of topic about these colors…but I could not find a very good guidance</p>
<p>What did I do wrong…?</p>
<p>of course, I need something very simple for my colleague to share this volume, because he does not have the Programme. I need something very very basic for him.</p>
<p>thanks for help!!!<br>
mathieu</p>

---

## Post #29 by @muratmaga (2024-03-04 16:59 UTC)

<p>I would suggest exporting to glTF, instead of OBJ.</p>
<p>Also give your export OBJ a try with another viewer like: <a href="http://3dviewer.net/">http://3dviewer.net/</a></p>

---

## Post #30 by @mvergnat (2024-03-27 12:45 UTC)

<p>many Thx!!!<br>
it worked very well withgITF<br>
but with OBJ in <a href="http://3dviewer.net" rel="noopener nofollow ugc">3dviewer.net</a>, the problem remained.</p>
<p>So the good option is gITF</p>
<p>cheers!</p>

---
