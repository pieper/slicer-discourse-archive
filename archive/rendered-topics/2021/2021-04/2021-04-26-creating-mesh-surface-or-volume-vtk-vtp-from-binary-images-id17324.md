---
topic_id: 17324
title: "Creating Mesh Surface Or Volume Vtk Vtp From Binary Images"
date: 2021-04-26
url: https://discourse.slicer.org/t/17324
---

# creating mesh surface or volume (vtk, vtp) from binary images 

**Topic ID**: 17324
**Date**: 2021-04-26
**URL**: https://discourse.slicer.org/t/creating-mesh-surface-or-volume-vtk-vtp-from-binary-images/17324

---

## Post #1 by @parvaneh.a (2021-04-26 06:27 UTC)

<p>Operating system: macos<br>
Slicer version:4.13<br>
Expected behavior: change nii segmentation to .vtk<br>
Actual behavior: the vtk format is not available for export mesh<br>
I have a binary 3d nii image and I am trying to make a mesh of it and save it in .vtk directly using slicer software preferably.<br>
the procedure I tried based on the tutorial of slicer, I opened my image as segmentation, then I went to segmentation modules and made the closed surface by clicking on the closed surface representations. Then in the export part I chose operation: export, output type: model. In the export to file section I chose a directory to save but there is no vtk format there for save it in vtk. I would be very grateful if you could help in that.</p>

---

## Post #2 by @pieper (2021-04-26 14:25 UTC)

<p>Make sure you do the export to model to a model folder and you can save to vtk from the main save dialog.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84eb5c98b52f892c6ac073023211e7da31f73866.jpeg" data-download-href="/uploads/short-url/iXRhKfSUZW3u6rmhAnpDTno7dzg.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/84eb5c98b52f892c6ac073023211e7da31f73866_2_690x333.jpeg" alt="image" data-base62-sha1="iXRhKfSUZW3u6rmhAnpDTno7dzg" width="690" height="333" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/84eb5c98b52f892c6ac073023211e7da31f73866_2_690x333.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/84eb5c98b52f892c6ac073023211e7da31f73866_2_1035x499.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84eb5c98b52f892c6ac073023211e7da31f73866.jpeg 2x" data-dominant-color="C3C4C4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1261×609 140 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @parvaneh.a (2021-04-26 15:26 UTC)

<p>Thanks for your reply. I am not sure which part I am making a mistake that when I use save button at the top it does not bring the vtk option for me?<br>
In the destination folder I am choosing the folder that my nii binary segment image is there. here are my slicer view:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd30e0e83eb6bc1ae1d024ab769d415cb91d087b.jpeg" data-download-href="/uploads/short-url/qZEXKvxsmh17opezLvxoOk1KzlV.jpeg?dl=1" title="Screen Shot 2021-04-26 at 11.21.16 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bd30e0e83eb6bc1ae1d024ab769d415cb91d087b_2_690x360.jpeg" alt="Screen Shot 2021-04-26 at 11.21.16 AM" data-base62-sha1="qZEXKvxsmh17opezLvxoOk1KzlV" width="690" height="360" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bd30e0e83eb6bc1ae1d024ab769d415cb91d087b_2_690x360.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bd30e0e83eb6bc1ae1d024ab769d415cb91d087b_2_1035x540.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bd30e0e83eb6bc1ae1d024ab769d415cb91d087b_2_1380x720.jpeg 2x" data-dominant-color="C8C8C9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-04-26 at 11.21.16 AM</span><span class="informations">2870×1500 393 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/3823467feade23f7d73c0e9d5b50564d1f2e2c87.png" data-download-href="/uploads/short-url/80CjyQQtyXo8vb4bF5SyXs7scHt.png?dl=1" title="Screen Shot 2021-04-26 at 11.20.42 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3823467feade23f7d73c0e9d5b50564d1f2e2c87_2_690x338.png" alt="Screen Shot 2021-04-26 at 11.20.42 AM" data-base62-sha1="80CjyQQtyXo8vb4bF5SyXs7scHt" width="690" height="338" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3823467feade23f7d73c0e9d5b50564d1f2e2c87_2_690x338.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3823467feade23f7d73c0e9d5b50564d1f2e2c87_2_1035x507.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3823467feade23f7d73c0e9d5b50564d1f2e2c87_2_1380x676.png 2x" data-dominant-color="C5C7C9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-04-26 at 11.20.42 AM</span><span class="informations">2880×1414 398 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34ae8e425ef3e4af0e4b74fc170c1cc82d66beec.png" data-download-href="/uploads/short-url/7w2OmA6DlZjcF83DSKLOGFa2TJW.png?dl=1" title="Screen Shot 2021-04-26 at 11.20.57 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/34ae8e425ef3e4af0e4b74fc170c1cc82d66beec_2_690x346.png" alt="Screen Shot 2021-04-26 at 11.20.57 AM" data-base62-sha1="7w2OmA6DlZjcF83DSKLOGFa2TJW" width="690" height="346" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/34ae8e425ef3e4af0e4b74fc170c1cc82d66beec_2_690x346.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/34ae8e425ef3e4af0e4b74fc170c1cc82d66beec_2_1035x519.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/34ae8e425ef3e4af0e4b74fc170c1cc82d66beec_2_1380x692.png 2x" data-dominant-color="C5C6C7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-04-26 at 11.20.57 AM</span><span class="informations">2880×1448 408 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @parvaneh.a (2021-04-26 16:03 UTC)

<p>Thanks, That works ! I am actually making the mesh and save it to vtk in order to open it in paraview and resample the p-value surface on it but it seems that after saving in vtk, some specifications is changed since it does not overlay my other surface when opening the vtk image in paraview. How can I save .vtk in the same origin or change the origin of it after saving?</p>

---

## Post #5 by @pieper (2021-04-26 17:01 UTC)

<p>It’s probably an RAS/LPS issue (you can find lots of discussion by searching here).  The file will be saved in LPS, and probably if you force it to read as RAS and then save again it’ll be flipped correctly.  Or you could harden it through a transform before you save.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e7245a76760532ea1e106445d1f5906ffa8686e.png" data-download-href="/uploads/short-url/4ll9majW8mQHutSrJPOf5n8pBtY.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e7245a76760532ea1e106445d1f5906ffa8686e_2_690x418.png" alt="image" data-base62-sha1="4ll9majW8mQHutSrJPOf5n8pBtY" width="690" height="418" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e7245a76760532ea1e106445d1f5906ffa8686e_2_690x418.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e7245a76760532ea1e106445d1f5906ffa8686e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e7245a76760532ea1e106445d1f5906ffa8686e.png 2x" data-dominant-color="EBEBED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">785×476 57.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @parvaneh.a (2021-04-26 17:26 UTC)

<p>Thank you, based on the image in the previous reply, I opened it as RAS and then saved it in vtk (poly data) and then again opened it in paraviwe but it did not change and still is exactly similar to one before:<br>
i have attached a photo here when I opened it in paraview , my mesh is the blue one but it should be in the place of the white one and flipped as the white (correct) one is.<br>
Could you please explain a bit more about how to harden it through a transform before I save?<br>
the segment image actually is aligned correctly before I save as vtk but the vtk file is not correctly placed and aligned with my probability surface map after conversion.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/1506c42cffee7cfc4a345296be888e0e8a87b984.jpeg" data-download-href="/uploads/short-url/300wsQWAVZpeRfDGgmq25hbzMxe.jpeg?dl=1" title="Screen Shot 2021-04-26 at 1.23.51 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1506c42cffee7cfc4a345296be888e0e8a87b984_2_690x347.jpeg" alt="Screen Shot 2021-04-26 at 1.23.51 PM" data-base62-sha1="300wsQWAVZpeRfDGgmq25hbzMxe" width="690" height="347" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1506c42cffee7cfc4a345296be888e0e8a87b984_2_690x347.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1506c42cffee7cfc4a345296be888e0e8a87b984_2_1035x520.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1506c42cffee7cfc4a345296be888e0e8a87b984_2_1380x694.jpeg 2x" data-dominant-color="888B99"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-04-26 at 1.23.51 PM</span><span class="informations">2202×1110 314 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @pieper (2021-04-26 19:25 UTC)

<aside class="quote no-group" data-username="parvaneh.a" data-post="6" data-topic="17324">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/parvaneh.a/48/14462_2.png" class="avatar"> parvaneh.a:</div>
<blockquote>
<p>Could you please explain a bit more about how to harden it through a transform before I save?</p>
</blockquote>
</aside>
<p>You need to create a linear transform in the Transforms module and change the first two 1s on the main diagonal to be -1.  Then you apply that transform to the model (select the model click the green arrow at the bottom of the Transforms module).   Then click the harden transform button.  HTH</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6ea3d7494d17a2e032b20e393995c66e39d79f8b.png" alt="image" data-base62-sha1="fMLy3RvL4zlPss5g9YniPvDvU5t" width="170" height="108"></p>

---

## Post #8 by @lassoan (2021-04-26 20:28 UTC)

<p>Paraview’s volume support is very limited. For example, it completely ignores image axis directions. Slicer display, volume rendering GUI is very poor, there is barely any support transforms, etc. For this reason, it is very inconvenient to use it in any serious medical image computing projects. Image orientation support has been recently added to VTK, so at some point Paraview might implement support for oriented images.</p>
<p>I would recommend to copy p values from the volume to the segmented surface using “Probe volumes with model” module in Slicer.</p>

---

## Post #9 by @parvaneh.a (2021-04-27 00:11 UTC)

<p>thanks for your reply but it actually when i save it  after transformation it does not change the orientation or anything else it is exactly the same as the image before. As you said I loaded the previously saved vtk image as RAS and in the transformation module I changed the two 1s to -1 and  then select the image (segment_1_main) on the left as shown below and click on the first arrow to bring it to the right and clicked on the hard transform then from the save option above I saved it as .vtk again. are all process correct?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21d3233eb7ac3b10682655bdd10d71119e8398a0.jpeg" data-download-href="/uploads/short-url/4Pe7foEcV3jxwSJa0h1wY8dGhsk.jpeg?dl=1" title="Screen Shot 2021-04-26 at 8.04.19 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21d3233eb7ac3b10682655bdd10d71119e8398a0_2_441x499.jpeg" alt="Screen Shot 2021-04-26 at 8.04.19 PM" data-base62-sha1="4Pe7foEcV3jxwSJa0h1wY8dGhsk" width="441" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21d3233eb7ac3b10682655bdd10d71119e8398a0_2_441x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21d3233eb7ac3b10682655bdd10d71119e8398a0_2_661x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21d3233eb7ac3b10682655bdd10d71119e8398a0_2_882x998.jpeg 2x" data-dominant-color="ECEDED"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-04-26 at 8.04.19 PM</span><span class="informations">1024×1160 107 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #10 by @lassoan (2021-04-27 01:17 UTC)

<p>VTK format cannot save the image orientation. We generally recommend nrrd format for saving 3D volumes. For simple things metaimage works well, too. For neuroimaging you may choose nifti.</p>

---

## Post #11 by @parvaneh.a (2021-04-27 01:25 UTC)

<p>Thanks for your reply. Actually I am using vtk or vtp because I am going to use that in paraview which accepts the vtk and vtp formats. There should be a way since the white mesh image in the few images before I took screenshot from paraview shows the correct mesh which has been made from the same segment binary image so I think there is a way to make that correction in the mesh i have saved with slicer. Actually I have been informed that the white mesh has also been made with slicer. So, I am trying slicer. So, I hope I could make my blue mesh correct as the white one is.</p>

---

## Post #12 by @lassoan (2021-04-27 01:33 UTC)

<p>Paraview can read uncompressed metaimage and nrrd formats, too. But it does not help much, because Paraview ignores the image orientation information.</p>
<aside class="quote no-group" data-username="parvaneh.a" data-post="11" data-topic="17324">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/parvaneh.a/48/14462_2.png" class="avatar"> parvaneh.a:</div>
<blockquote>
<p>Actually I am using vtk or vtp because I am going to use that in paraview which accepts the vtk and vtp formats. There</p>
</blockquote>
</aside>
<p>I see that you are referring to VTP. Maybe you mean you want to save meshes and not images? Meshes can be saved in any orientation and Paraview will load them correctly.</p>
<p>Paraview may still show misaligned image and mesh because it cannot load the image correctly. The only way you can work around the Paraview’s non-oriented image issue is that if you transform everything (the image, segmentation, all meshes) with a transformation that makes the image’s direction matrix become identity (diagonal of 1.0), because it does not matter if you ignore an identity orientation matrix. You need to harden this transform on all nodes before saving. I’m not sure if you need to save the meshes in LPS and RAS coordinate system in this case, so try both.</p>
<p>Paraview is great for working with meshes, but if you work with image volumes then you are much better off using Slicer. Let us know if there is anything that you know how to do in Paraview but not sure how to do in Slicer. Slicer is built on top of VTK the same way as Paraview, so Slicer has the same low-level features, just not all have been made available via graphical user interface or not the same way as in Paraview.</p>

---
