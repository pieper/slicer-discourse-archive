# Can we use the 3D slicer software only to model the implant?

**Topic ID**: 15865
**Date**: 2021-02-05
**URL**: https://discourse.slicer.org/t/can-we-use-the-3d-slicer-software-only-to-model-the-implant/15865

---

## Post #1 by @Focus (2021-02-05 14:54 UTC)

<p>Can we us the 3d slicer in design of customized implants?</p>

---

## Post #2 by @lassoan (2021-02-05 14:55 UTC)

<p>Most probably yes. Can you tell a bit more about what you would like to achieve?</p>

---

## Post #3 by @Focus (2021-02-22 08:06 UTC)

<p>Oh sorry for I lately reply your comment. My project is to make Craniofacial Implants. First of all, I make the model from DICOM File using the grayscale modelmaker. So how can I get the mirror model and locate the defecting skull? Actually, how can I get implants from the healthy side of Craniofacial by using 3d Slicer. Sorry again if it makes you confuse.</p>

---

## Post #4 by @lassoan (2021-02-22 12:51 UTC)

<p>There are many tools in Slicer that you can use for surgical planning. For model mirroring you can try Dynamic modeler module:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="F6fNMQTxD-4" data-video-title="3D Slicer: Dynamic Modeler - Parametric Surface Editing for Biomedical Applications" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=F6fNMQTxD-4" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/F6fNMQTxD-4/maxresdefault.jpg" title="3D Slicer: Dynamic Modeler - Parametric Surface Editing for Biomedical Applications" width="" height="">
  </a>
</div>


---

## Post #5 by @Focus (2021-02-23 18:30 UTC)

<p>How can I get the model implant on the red area? How can I subtract it?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7dbd0fe1d27c985215ff6196f24cc86161e561d.png" data-download-href="/uploads/short-url/uNzBR0jQwTVr1S32jGMRc6Aiwpv.png?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7dbd0fe1d27c985215ff6196f24cc86161e561d_2_690x236.png" alt="Screenshot" data-base62-sha1="uNzBR0jQwTVr1S32jGMRc6Aiwpv" width="690" height="236" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7dbd0fe1d27c985215ff6196f24cc86161e561d_2_690x236.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7dbd0fe1d27c985215ff6196f24cc86161e561d_2_1035x354.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7dbd0fe1d27c985215ff6196f24cc86161e561d.png 2x" data-dominant-color="9D98BB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1260×431 68.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2021-02-23 19:25 UTC)

<p>What do you mean by getting the model implant on the red area?<br>
What would you like to subtract from what?<br>
What would you like to achieve overall?</p>

---

## Post #7 by @Focus (2021-02-24 08:13 UTC)

<p>Sorry for make you confuse.  I want to fill hole the skull and i want only red area in the hole in 3D model. How can i do ?  My goal is create a model that is in the hole (red area) in 3D object.</p>

---

## Post #8 by @manjula (2021-02-24 12:02 UTC)

<p>I would make a curve cut with a closed curve in the dynamic modeler on the red model.</p>
<p>Then it can be used as the template to generate the implant you want. There maybe other ways of doing it but i would convert the cut model into segmentation and use the segment editor effects to create/model the implant the way I want.</p>
<p>Once you have the final implant with desired thickness and shape you can use a boolean subtraction (red-yellow) to make the fitting surface to exactly match the defect edges and the skull surface.</p>

---

## Post #9 by @Focus (2021-02-28 09:05 UTC)

<p>Thank you, you help me a lot. Could you tell more detail about convert the model to segmentation? Now, I have a surface implant but it doesn’t have thickness. how can I make a model thickness? could you guide me or any video tutorial? <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a0ed58b7809620ce33d7960916e587600dcf7df5.png" alt="image" data-base62-sha1="mXCUi0nLsWCsqLP6oAF243XTqNn" width="485" height="302"></p>

---

## Post #10 by @lassoan (2021-02-28 13:28 UTC)

<p>Segmentation node stores a 3D volume. There are many ways to convert a surface patch to 3D volume.</p>
<p>If you want to extrude the model (to have a thickness) then you do the followings:</p>
<ul>
<li>make sure the surface has normals (you can compute normals by using Surface Toolbox, enabling “Normals” option)</li>
<li>extrude the surface along the normal direction using “Hollow” tool in Dynamic modeler (you can specify negative shell thickness to extrude the surface to the opposite side of surface normals) - this tool is available in recent Slicer Preview Releases</li>
</ul>

---

## Post #11 by @pll_llq (2021-03-01 07:34 UTC)

<p>Hey <img src="https://emoji.discourse-cdn.com/twitter/wave.png?v=9" title=":wave:" class="emoji" alt=":wave:">, here’s a post that might help <a href="https://discourse.slicer.org/t/3d-model-to-segmentation">https://discourse.slicer.org/t/3d-model-to-segmentation</a></p>
<p>Your workflow with substracting the defect shape from the mirrored side of the scull seems logical because not only you will get the shape with the necessary thickness, but also you can get the shape of the defect edges on the implant.</p>

---

## Post #12 by @manjula (2021-03-01 10:48 UTC)

<p>cannot find the  “Hollow” tool in the Surface toolbox in the latest preview release (2021.02.28)</p>

---

## Post #13 by @lassoan (2021-03-01 12:45 UTC)

<aside class="quote no-group" data-username="manjula" data-post="12" data-topic="15865">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>cannot find the “Hollow” tool in the Surface toolbox in the latest preview release</p>
</blockquote>
</aside>
<p>My mistake, sorry, it is in “Dynamic modeler” module.</p>

---

## Post #14 by @Focus (2021-03-16 08:17 UTC)

<p>Right now, I can create the implant model. By use this following method.</p>
<ol>
<li>generate model by using grayscale model maker and create the 2 model. First model is a defect the skull. and the second model is mirror model.</li>
<li>Import the two models in to segmentation module(drag file) as segmentation format.</li>
<li>use logical operation to subtract model.</li>
<li>then, using a scissor to cut the model, get the model implants.</li>
<li>using smoothing opening operation to erase the error object.</li>
</ol>
<p>Thank you for all your support.<br>
The next project, I would like to develop for the extension in 3d-slicer.</p>

---

## Post #15 by @yousra (2022-11-10 12:56 UTC)

<p>Hello i’m interested by how create an implant or how to fill a Holl so can you show as a video thant explain differents steps to do this please .<br>
thank you</p>

---
