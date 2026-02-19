---
topic_id: 22088
title: "Details Inside A Bone For Dental Implant Planning"
date: 2022-02-21
url: https://discourse.slicer.org/t/22088
---

# Details inside a bone for dental implant planning

**Topic ID**: 22088
**Date**: 2022-02-21
**URL**: https://discourse.slicer.org/t/details-inside-a-bone-for-dental-implant-planning/22088

---

## Post #1 by @CaetanoPM (2022-02-21 17:15 UTC)

<p>Hi,</p>
<p>I’m dentist, and i’m having some trouble with my stl file.</p>
<p>I followed all the steps, and export the stl file of the jaw bones. OK<br>
I put in Meshmixer to edit, and wen i look inside, have no details, only a empty space.<br>
What i have to do, to show or to export all details from DICOM?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2022-02-23 06:10 UTC)

<p>Segmentation is typically represented as a binary labelmap or a closed surface mesh (see more details here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html" class="inline-onebox">Image Segmentation — 3D Slicer documentation</a>). If you cut into a surface mesh then there is nothing inside, it is just a surface.</p>
<p>What is your end goal? What kind of details would you like to export for what purpose?</p>

---

## Post #3 by @CaetanoPM (2022-02-23 12:42 UTC)

<p>Hi Andras.</p>
<p>I’m trying to do a Cirurgical guide for myself.<br>
And i neet to see the interior of the bone to put the virtual implant correctly on Meshmixer to fabricate the guide. Without the interior mesh, i can’t see the important structures that i need to avoid.</p>
<p>Thanks for the reply.</p>

---

## Post #4 by @lassoan (2022-02-24 05:14 UTC)

<p>I would recommend to make the surgical guide in Slicer. You can then see both the full anatomy and in slice and 3D views and the guide that you are designing.</p>
<p>We can give more specific advice if you can tell a bit more about what body part and procedure you creating the surgical guide for.</p>
<p>Just an example of how you can create surgical guides in Slicer: <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner" class="inline-onebox">GitHub - SlicerIGT/SlicerBoneReconstructionPlanner: 3D Slicer module for planning mandible reconstruction surgery using fibula flap</a></p>

---

## Post #5 by @CaetanoPM (2022-02-25 11:15 UTC)

<p>Hi Andras.</p>
<p>Thanks one more time for the reply!</p>
<p>I want to create a cirurgical guide for Mandible and Jaw, for implantology.<br>
I have the 3D Printer (Phrozen 4k mini), and i want to do the guides by myself. I know that have on the internet several programs to do the guide, but all of them is paid to do… Anyway!</p>
<p>Thanks for the link, but i think this module is for segmentation of bone, to larger reconstruction</p>

---

## Post #6 by @lassoan (2022-02-25 14:56 UTC)

<p>Bone reconstruction planner can plan drill guides for implants as well. I think it is not yet in the main branch. <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> give more details</p>
<p>If you only need the implant planning then a separate simplified module might be added.</p>
<p>Note that in Slicer you can create implant plan and create a surgical guide without a dedicated module. For example, you can load implant models as STL, position them using transforms, then apply the same transform to position a cylinder model, import the positioned cylinder model into Segment Editor, and create the surgical guide by thresholding the bone and combining it with the cylinders. A dedicated module would make things more convenient, could automate all the complicated steps.</p>
<p><a class="mention" href="/u/manjula">@manjula</a> works in related field and <a class="mention" href="/u/cpinter">@cpinter</a> was interested in some dental applications. They might be able to give some more suggestions.</p>

---

## Post #7 by @mau_igna_06 (2022-02-25 16:16 UTC)

<p>Hi <a class="mention" href="/u/caetanopm">@CaetanoPM</a></p>
<p><a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner#readme" rel="noopener nofollow ugc">BoneReconstructionPlanner</a> can plan dental implants for a mandible reconstruction and a patient-specific fibula surgical guide with drill guides for implants on the <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/tree/DentalImplantsBranch" rel="noopener nofollow ugc">DentalImplantsBranch</a>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d05455a88cf192da728870f1f3f92e8ee15b452.png" data-download-href="/uploads/short-url/mp4fR3Jsr5DmT9qF6JiuR3pSANA.png?dl=1" title="124329758-686a3180-db62-11eb-8184-e8a685e8282b" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d05455a88cf192da728870f1f3f92e8ee15b452_2_690x353.png" alt="124329758-686a3180-db62-11eb-8184-e8a685e8282b" data-base62-sha1="mp4fR3Jsr5DmT9qF6JiuR3pSANA" width="690" height="353" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d05455a88cf192da728870f1f3f92e8ee15b452_2_690x353.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d05455a88cf192da728870f1f3f92e8ee15b452_2_1035x529.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d05455a88cf192da728870f1f3f92e8ee15b452.png 2x" data-dominant-color="BAB7C7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">124329758-686a3180-db62-11eb-8184-e8a685e8282b</span><span class="informations">1366×700 173 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>See an example of surgical guides for a case <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/issues/49#issuecomment-1027800475" rel="noopener nofollow ugc">here</a>.</p>
<p>I don’t have yet a robust workflow for dental implant planning for a healthy mandible or maxilla on Slicer.<br>
Dental implants can be planned virtually with the CBCT (one could copy the way it is done on BRP although this way has disadvantages), to make the patient-specific surgical guide you need a registered intra-oral scan. This rigid registration is the most difficult part of the workflow and I haven’t been able to solve that on Slicer yet.</p>
<p>In addition,for the planning part, reslicing would be needed have good visualization of the cortical bone and avoid damaging with the drill important internal structures like nerves. With this considerations the implant is better placed</p>
<p>Hope my comments are helpful</p>
<p>Mauro</p>

---

## Post #8 by @CaetanoPM (2022-02-25 17:44 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a></p>
<p>Thanks for the reply.</p>
<p>For <a class="mention" href="/u/lassoan">@lassoan</a> Were i find some guide or some tutorial about create this guide and plan without a module? Just to understand this method.</p>
<p>For <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> I see in the image you sent, a Dental Implant Planning. How can i integrate this on the Bone Reconstruction Planner? I install on 3D slicer, but i can’t find on the module on 3d slicer.</p>
<p>I have the Scan to do a intraoral scan and have the 3D printer too hahhahaha I’m trying to to by myself!! Thanks for the support.</p>

---

## Post #9 by @mau_igna_06 (2022-02-25 17:56 UTC)

<p>I don’t know if BoneReconstructionPlanner would be useful for you because it is optimized for mandible reconstruction workflows but you can install it by searching its name on the ExtensionManager. Here is a <a href="https://www.youtube.com/watch?v=g9Vql5h6uHM">videotutorial</a>. Also see the link I sent earlier for the DentalImplantsBranch tutorial.</p>
<p>It will be challeging to get the patient-specific dental implants surgical guides but with patience (and maybe manual registration) you could achieve it. Please post pictures here if you are successful.</p>
<p>Mauro</p>

---

## Post #10 by @manjula (2022-02-27 10:51 UTC)

<p>Hi sorry for the late reply, You can create a dental implant surgical guide within 3D Slicer with some not so convenient workflow.</p>
<ol>
<li>Import the CBCT data and the IOS scans.</li>
</ol>
<ul>
<li>Optionally, you can use the curve planar reformat tool to reformat the CBCT so that you can get a nice perpendicular view like in most commercial softwares.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a196b05972333b1752bc0cf61f826ac1b111e094.jpeg" data-download-href="/uploads/short-url/n3tILVFCVpll6nsbySH6UrB62fG.jpeg?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a196b05972333b1752bc0cf61f826ac1b111e094_2_344x250.jpeg" alt="Screenshot" data-base62-sha1="n3tILVFCVpll6nsbySH6UrB62fG" width="344" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a196b05972333b1752bc0cf61f826ac1b111e094_2_344x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a196b05972333b1752bc0cf61f826ac1b111e094_2_516x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a196b05972333b1752bc0cf61f826ac1b111e094_2_688x500.jpeg 2x" data-dominant-color="353535"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1243×903 63.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>
</li>
</ul>
<ol start="2">
<li>
<p>Register the IOS with the CBCT<br>
You have many choices in Slicer but i find the Fiducial Registration wizard to work best in this case.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df130ebafb56f4ec54e71cb726c3a3059d17bdca.jpeg" data-download-href="/uploads/short-url/vPpj0c9oq9LIB8Zy72P88I1h4fg.jpeg?dl=1" title="Screenshot_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/df130ebafb56f4ec54e71cb726c3a3059d17bdca_2_337x250.jpeg" alt="Screenshot_1" data-base62-sha1="vPpj0c9oq9LIB8Zy72P88I1h4fg" width="337" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/df130ebafb56f4ec54e71cb726c3a3059d17bdca_2_337x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/df130ebafb56f4ec54e71cb726c3a3059d17bdca_2_505x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/df130ebafb56f4ec54e71cb726c3a3059d17bdca_2_674x500.jpeg 2x" data-dominant-color="756B79"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_1</span><span class="informations">1243×920 62.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
</li>
<li>
<p>Import the Implant and the prosthetic components to the Slicer in stl format</p>
</li>
<li>
<p>You can manipulate them using the transform module or much more conveniently using the <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> script.</p>
</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/0530617817b5caa4481f183da38ea6b6c48b8e85.jpeg" data-download-href="/uploads/short-url/JU2DMpNQeLRPryzelexscsf90p.jpeg?dl=1" title="Screenshot_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0530617817b5caa4481f183da38ea6b6c48b8e85_2_345x207.jpeg" alt="Screenshot_2" data-base62-sha1="JU2DMpNQeLRPryzelexscsf90p" width="345" height="207" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0530617817b5caa4481f183da38ea6b6c48b8e85_2_345x207.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0530617817b5caa4481f183da38ea6b6c48b8e85_2_517x310.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0530617817b5caa4481f183da38ea6b6c48b8e85_2_690x414.jpeg 2x" data-dominant-color="74727C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_2</span><span class="informations">1530×920 98.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45cfa1cdd2723ecc119c8338e8a09397b70200e9.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45cfa1cdd2723ecc119c8338e8a09397b70200e9.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45cfa1cdd2723ecc119c8338e8a09397b70200e9.mp4</a>
    </source></video>
  </div><p></p>
<ol start="5">
<li>Create a surgical guide base.</li>
</ol>
<p>Many options here,</p>
<p>Segment editor can be used -  Threshold Segmentation → adjust with the scissors tool → hollow tool (inside surface and define the thickness of the guide base in mm (shell thickness) )</p>
<p>Then use the implant cylinder to cut the holes in a slicer or in a blender or you can convert cylinder to segmentation node and subtract in the segment editor.</p>
<ul>
<li>Also you can use dynamic modeler and surface toolbox to create the guide base.</li>
</ul>
<p>Curve cut → compute surface normals (auto orient normals) (in surface toolbox) → back in dynamic modeller use “Hollow” tool.</p>
<p>There may be other methods of creating the guide base but i find the dynamic modeler and the surface toolbox easier.</p>
<p>PS: if you harden the transforms and save them in stl format you can use Blender to do the final boolean operations and final finish since the objects will be exported maintaining the relative positions.</p>

---

## Post #11 by @Yusif (2024-05-23 20:09 UTC)

<p>Hello. I also need to planning orthodontic palatinal expander with mini screw. I can import cbct and stl files . But I ould not register cbct and stl file with fiducial registration. Can you help me in this case plase? My whatsapp number is +994558633713 . Thanks in advance. I tried many times but I can not do it.</p>

---

## Post #12 by @cpinter (2024-05-24 11:07 UTC)

<p>Fiducial registration is really simple using Fiducial registration wizard (in SlicerIGT). Check out this video:</p><div class="youtube-onebox lazy-video-container" data-video-id="zs-0mZQLB48" data-video-title="Dent.AI 3D Guide product presentation - October 2023" data-video-start-time="30" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=zs-0mZQLB48&amp;t=30" target="_blank" class="video-thumbnail" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/zs-0mZQLB48/hqdefault.jpg" title="Dent.AI 3D Guide product presentation - October 2023" width="480" height="360">
  </a>
</div>

<p>This is a Slicer-based application so you can do the same thing in Slicer, just need to click around more.</p>

---
