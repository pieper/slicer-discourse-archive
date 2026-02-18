# Viewer to share medical models from URL / website integration

**Topic ID**: 36568
**Date**: 2024-06-03
**URL**: https://discourse.slicer.org/t/viewer-to-share-medical-models-from-url-website-integration/36568

---

## Post #1 by @ILB (2024-06-03 12:09 UTC)

<p>Hi!</p>
<p>Do you know if there is a way to share medical segmentations with other team members without an installed software? Like, how can I share some kind of link, so they can access the model and interact with it easily? It would be posible to create a simple website on Squarespace and integrate the model?</p>
<p>Something like <a href="http://3dviewer.net" rel="noopener nofollow ugc">3dviewer.net</a> would be great, but i’m kind of worried about the confidenciatity of the files.</p>
<p>Any idea is welcomed.</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2024-06-03 14:08 UTC)

<p>Slicer does not need installation, just a computer. So, if you put Slicer and some data sets in a dropbox folder and share it with others then they can start Slicer from that folder without installing. You can also give users access to a Slicer computer that has some data preloaded using remote desktop sharing. The advantage of these solutions that you have access to all Slicer visualization, processing, and analysis features.</p>
<p>If you want to open the files from a phone or Android/iOS tablet and simple viewing is enough then you have many options:</p>
<p>A. If you don’t need your users to make measurements then often 3D rotation video (exported by Screen Capture module) is sufficient.</p>
<p>B. If you want to send a file in an email:</p>
<ul>
<li>B1. Use any 3D web viewer that supports glTF. For example, you can open <a href="http://3dviewer.net">3dviewer.net</a> in the browser on your phone/tablet and open the file that you downloaded (e.g., from an email). This viewer is very nice in that you can see the model hierarchy and turn on/off visibility of each segment.</li>
<li>B2. Install a glTF viewer app, such as <a href="https://play.google.com/store/apps/details?id=org.opencascade.cadassistant&amp;hl=en_US">CAD Assistant</a>. When you open the attachment in the email app, it will offer to open the 3D model in the installed viewer app. This is convenient, but unfortunately I could not find any 3D viewer that would work as well as <a href="http://3dviewer.net">3dviewer.net</a>.</li>
</ul>
<p>C. If you don’t want to send a file in email then you can upload to anywhere (such as dropbox, or any other server that you trust, it can be a computer within your hospital, too) and generate a direct link that opens the file in a web viewer in your browser. Only the viewer is downloaded from the viewer’s server, your model is not uploaded there. See more details <a href="https://discourse.slicer.org/t/open-anatomy-export-and-3dviewer-net-with-url/26726/18">here</a> about how to create viewer link.</p>

---

## Post #3 by @tsehrhardt (2024-06-03 16:08 UTC)

<p>You can look at Sketchfab. It has options for private models–downloadable or not, password protection if needed. I use it often to share models privately.</p>

---

## Post #4 by @lassoan (2024-06-05 13:03 UTC)

<p>I don’t think that sketchfab is certified to handle patient data. Some hospitals have agreements with certain cloud providers for HIPAA compliant data handling (dropbox, box,  google, aws, azure, …) so you may upload patient data to those services.</p>
<p>Also, <a href="http://3dviewer.net">3dviewer.net</a> has several essential features that Sketchfab surprisingly lacks, such as:</p>
<ul>
<li>show a hierarchy of objects and allow highlighting it, showing/hiding, or zooming to each: this is very important when sharing more complex models (you may want to show/hide skin or hide internal organs to make it easier to see bones)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18d6aa6c8d6a064f9f122af2460239ec617b76d1.jpeg" data-download-href="/uploads/short-url/3xJnsQyB7UA6nrTlnyPaeaOFFFD.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18d6aa6c8d6a064f9f122af2460239ec617b76d1_2_690x440.jpeg" alt="image" data-base62-sha1="3xJnsQyB7UA6nrTlnyPaeaOFFFD" width="690" height="440" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18d6aa6c8d6a064f9f122af2460239ec617b76d1_2_690x440.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18d6aa6c8d6a064f9f122af2460239ec617b76d1_2_1035x660.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18d6aa6c8d6a064f9f122af2460239ec617b76d1_2_1380x880.jpeg 2x" data-dominant-color="535557"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1628×1040 90.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
<li>click on an object in 3D and show that structure in the tree (again very useful for complex models, you can click on a small structure and you can see the name and its location in the anatomy tree; or you can easily hide the structure that you clicked on)</li>
<li>make simple distance and angle measurements</li>
<li>free, open-source</li>
<li>works with any hosting solution (you don’t have to upload your model to thingiverse, you can use any computer or cloud service provider), you can privately share leveraging services that you already use (e.g., dropbox, github, …)</li>
</ul>
<p>You can embed content into third-party sites, like in this forum (this model is directly exported from a segmentation in Slicer using SlicerOpenAnatomy extension):</p>
<iframe width="640" height="480" src="https://3dviewer.net/embed.html#model=https://raw.githubusercontent.com/lassoan/Test/master/SPL-Abdominal-Atlas.gltf"></iframe>
<p>You can click on the icon in the lower-right corner to get all the viewer features.</p>
<p>It can render any glTF models:</p>
<iframe width="640" height="480" src="https://3dviewer.net/embed.html#model=assets/models/DamagedHelmet.glb"></iframe>
<p>If you want to show images as well then Kitware has some nice web viewers, too. They are quite hard to use for me, so I cannot really recommend them for most people, but I don’t know other web viewers that can show meshes and images (slices and volume rendering) all combined in a single 3D scene.</p>

---

## Post #5 by @muratmaga (2024-06-05 16:36 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="36568">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can embed content into third-party sites, like in this forum (this model is directly exported from a segmentation in Slicer using SlicerOpenAnatomy extension):</p>
</blockquote>
</aside>
<p>This is great. I did not know about the embedding…</p>

---

## Post #6 by @tsehrhardt (2024-06-06 01:09 UTC)

<p>It is not but it is being used by “commercial” entities to privately host models for clients, including medical clients. The API gives you access to model hierarchy of gltf or fbx files, so it’s definitely not as easy as 3Dviewer. It’s a nice option if you want to control privacy and prevent download, and a customizable viewer can be embedded on websites as well. As far as I can tell with 3Dviewer, generated links allow the viewer to download and share your model.</p>
<p>Anatomage also offers a viewer called InVivo that can support 3d models and dicom.</p>

---

## Post #7 by @ILB (2024-06-06 07:55 UTC)

<p>Thank you so much for your answer!<br>
I have tried <a href="http://3dviewer.net" rel="noopener nofollow ugc">3dviewer.net</a>, but when i try to upload several stl files, i get this message:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/329849de0d579dd734a5beb2e7c6a20dc2b49e5c.png" data-download-href="/uploads/short-url/7dA9jsEcDLBjUb2t85tennLPtnu.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/329849de0d579dd734a5beb2e7c6a20dc2b49e5c_2_690x372.png" alt="image" data-base62-sha1="7dA9jsEcDLBjUb2t85tennLPtnu" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/329849de0d579dd734a5beb2e7c6a20dc2b49e5c_2_690x372.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/329849de0d579dd734a5beb2e7c6a20dc2b49e5c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/329849de0d579dd734a5beb2e7c6a20dc2b49e5c.png 2x" data-dominant-color="FCFDFD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">778×420 14 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>How can i upload all?<br>
Thank you!</p>

---

## Post #8 by @lassoan (2024-06-06 11:39 UTC)

<aside class="quote no-group" data-username="ILB" data-post="7" data-topic="36568">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/i/e9c0ed/48.png" class="avatar"> ILB:</div>
<blockquote>
<p>I have tried <a href="http://3dviewer.net">3dviewer.net</a>, but when i try to upload several stl files, i get this message:</p>
</blockquote>
</aside>
<p>You can use OpenAnatomy Export module (provided by SlicerOpenAnatomy extension) to export your segmentation into a single glTF file.</p>
<aside class="quote no-group" data-username="tsehrhardt" data-post="6" data-topic="36568">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tsehrhardt/48/18470_2.png" class="avatar"> tsehrhardt:</div>
<blockquote>
<p>It’s a nice option if you want to control privacy and prevent download</p>
</blockquote>
</aside>
<p>For your information, when somebody views a 3D model in his browser, he can also save that 3D model to file, regardless of what website is used and if the website provides a convenient download option or not.</p>
<p>The reason is that - unlike videos - 3D models do not have standard for end-to-end digital rights management solution: 3D models are stored in your graphics hardware without any encryption and can be retrieved by using tools such as NVIDIA Nsight or GPU model rippers.</p>

---

## Post #9 by @ILB (2024-06-06 12:27 UTC)

<p>Do you know how can i solve this error? I am not able to export my segmentations.<br>
Thanks!<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85a946436293978037b2da5487dff26c06a2cb71.png" alt="image" data-base62-sha1="j4qaGRfZPLhDEo2Fn3luDwp83dL" width="452" height="374"></p>

---

## Post #10 by @lassoan (2024-06-06 12:31 UTC)

<p>You need to rename the node that has <code>:</code> in the name. I’ll update the exporter to remove the <code>:</code> automatically but for now you have to do it manually.</p>

---

## Post #11 by @ILB (2024-06-06 12:36 UTC)

<p>Thank you so much! Everything works just fine now.<br>
Have a nice day!</p>

---
