---
topic_id: 28191
title: "Turn 2D Image Slices Into 3D Model"
date: 2023-03-06
url: https://discourse.slicer.org/t/28191
---

# Turn 2d image slices into 3d model

**Topic ID**: 28191
**Date**: 2023-03-06
**URL**: https://discourse.slicer.org/t/turn-2d-image-slices-into-3d-model/28191

---

## Post #1 by @ayman_bali (2023-03-06 11:48 UTC)

<p>Dear community,</p>
<p>i am new to 3d slicer and i have a set of image slices (2D), which are from a probe cut in 100 um steps, and i want to put these images together and do a 3d model. What steps do I need to follow to create a 3D reconstruction from 2D image slices using 3D Slicer, and how can I ensure that the final model retains the colors of the original images so that I can view it in 3D?</p>
<p>I saw a lot of tutorials but im still getting a wrong 3d model when im doing volume rendering. I can upload the images</p>
<p>I uploaded the images in case anyone wants to take a look on them</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/scl/fo/yk5cisai7atz7ukqhu0vt/h?dl=0&amp;rlkey=c5abce19vs1o2cfi58175813m">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon-vfl8lUR9B.ico" class="site-icon" width="32" height="32">

      <a href="https://www.dropbox.com/scl/fo/yk5cisai7atz7ukqhu0vt/h?dl=0&amp;rlkey=c5abce19vs1o2cfi58175813m" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/metaserver/static/images/spectrum-icons/generated/content/content-folder_dropbox-large.png" class="thumbnail onebox-avatar" width="160" height="160">

<h3><a href="https://www.dropbox.com/scl/fo/yk5cisai7atz7ukqhu0vt/h?dl=0&amp;rlkey=c5abce19vs1o2cfi58175813m" target="_blank" rel="noopener nofollow ugc">Neuer Ordner (12)</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Thank you so much!!</p>
<p>Best regards,<br>
Ayman</p>

---

## Post #2 by @muratmaga (2023-03-06 18:27 UTC)

<aside class="quote no-group" data-username="ayman_bali" data-post="1" data-topic="28191">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ayman_bali/48/18648_2.png" class="avatar"> ayman_bali:</div>
<blockquote>
<p>What steps do I need to follow to create a 3D reconstruction from 2D image slices using 3D Slicer, and how can I ensure that the final model retains the colors of the original images so that I can view it in 3D?</p>
</blockquote>
</aside>
<p>These are histology slides (I think), so if you simply uncheck the “grayscale” option in the <code>ImageStacks</code> module of SlicerMorph, you will get color (RGB) images. However, slides are not co-registered; i.e., the orientation of the tissue is different from one slide to the next. Hence, you will not get a good volume rendering out of these, because when stacked together they do not constitute a proper 3D ‘volume’. (see the jagged edges in green and yellow slice. If you move up and down in the red slice view, you will see the tissue rotating from one slide to the next).</p>
<p>You can try to register one slide to the next one and keep moving in the stack. I think ImageJ has a specific function to do that. I am not sure if there is anything in the Slicer to help you in aligning the slides (there a lots of registration tools, but they are usually for registering one 3D volume to another). Others on the forum that are more familiar with histology data can chime in.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/50972aec4d59179e51d0b93c1cc91a61e6240bbc.jpeg" data-download-href="/uploads/short-url/buW4w7h0m6CJHPFhaRsoaPyrEba.jpeg?dl=1" title="Screen Shot 2023-03-06 at 10.19.31 AM"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/50972aec4d59179e51d0b93c1cc91a61e6240bbc_2_690x431.jpeg" alt="Screen Shot 2023-03-06 at 10.19.31 AM" data-base62-sha1="buW4w7h0m6CJHPFhaRsoaPyrEba" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/50972aec4d59179e51d0b93c1cc91a61e6240bbc_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/50972aec4d59179e51d0b93c1cc91a61e6240bbc_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/50972aec4d59179e51d0b93c1cc91a61e6240bbc_2_1380x862.jpeg 2x" data-dominant-color="A3A0B2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2023-03-06 at 10.19.31 AM</span><span class="informations">2576×1610 686 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @ayman_bali (2023-03-06 21:14 UTC)

<p>Hey Murat,</p>
<p>thank you so much for your answer! I have been trying to reach the same result in your screenshot, but im still getting the sharp edges of the images in my model.</p>
<p>Can i ask you, did you do anything else than uploading the images and choose 0.1 mm? Did you register the images before doing the 3d model in your screenshot?</p>
<p>Thank you for your help, im trying to reach the same result as yours.</p>
<p>Best regards<br>
Ayman</p>

---

## Post #4 by @muratmaga (2023-03-06 21:19 UTC)

<aside class="quote no-group" data-username="ayman_bali" data-post="3" data-topic="28191">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ayman_bali/48/18648_2.png" class="avatar"> ayman_bali:</div>
<blockquote>
<p>Can i ask you, did you do anything else than uploading the images and choose 0.1 mm? Did you register the images before doing the 3d model in your screenshot?</p>
</blockquote>
</aside>
<p>I didn’t do anything. I simply dragged one of your files into Slicer and asked it to open with ImageStacks. However, your files are not named conventionally. Normally slice sequences go something like 0001, 0002, 0003, and yours are missing leading zeros. Your operating systems may sort those files differently then mine (MacOS).  Please expand the files list and see that the sequence of files is correst (ie., it goes 1,2,3,…,10,11,12,…100,101).</p>
<p>Imagestack relies on the ordering OS provides and we expect the files to have properly formated sequences.</p>

---

## Post #5 by @ayman_bali (2023-03-06 22:00 UTC)

<p>Hey Murat,</p>
<p>thank you again, i tried now to rename the files as you said, and im still not getting the same 3d Model, it seems that the software is still taking the images in a different order because i did exactly the same as you said, do you have any other ideas why this is happening? (Screenshot)</p>
<p>Thank you so much!</p>
<p>Best regards<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de0ff2fb67164254cecaf0d6929b4010a205f3c0.png" data-download-href="/uploads/short-url/vGsauUMT4quUPqhsC4MeOGUryCs.png?dl=1" title="Screenshot 2023-03-06 225853" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de0ff2fb67164254cecaf0d6929b4010a205f3c0_2_690x361.png" alt="Screenshot 2023-03-06 225853" data-base62-sha1="vGsauUMT4quUPqhsC4MeOGUryCs" width="690" height="361" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de0ff2fb67164254cecaf0d6929b4010a205f3c0_2_690x361.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de0ff2fb67164254cecaf0d6929b4010a205f3c0_2_1035x541.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de0ff2fb67164254cecaf0d6929b4010a205f3c0_2_1380x722.png 2x" data-dominant-color="7B7C8C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-03-06 225853</span><span class="informations">1896×992 253 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @muratmaga (2023-03-06 22:08 UTC)

<aside class="quote no-group" data-username="ayman_bali" data-post="5" data-topic="28191">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ayman_bali/48/18648_2.png" class="avatar"> ayman_bali:</div>
<blockquote>
<p>ideas why this is happening?</p>
</blockquote>
</aside>
<p>It is because you do not have the files named in a consistent manner (i.e your slice ordinals are sometimes 1, sometimes 2 and sometimes 3 digits), so parsing is also inconsistent.</p>
<p>the proper way of fixing this is adding the leading zeros so 1.tif becomes 001.</p>
<p>You can also try dragging one of the three digit ones into Slicer scene and see if that helps to import all 120 slices (your screenshot shows only 48 slices).</p>
<p>You can also click the select files button and try to select the files manually.</p>
<p>Also uncheck the grayscale button if you want RGB images.</p>

---

## Post #7 by @ayman_bali (2023-03-06 22:24 UTC)

<p>Okay i added leading zeros and i chose the files manually and checked that they are in the right order and still not getting it. Do you think it is a windows issue?</p>
<p>Best regards<br>
Ayman<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/5209ead29ee902d92d7f93d15cb365e38475f257.jpeg" data-download-href="/uploads/short-url/bHKoOxc3Z46F9F9H8DaXAnageur.jpeg?dl=1" title="Screenshot2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/5209ead29ee902d92d7f93d15cb365e38475f257_2_690x367.jpeg" alt="Screenshot2" data-base62-sha1="bHKoOxc3Z46F9F9H8DaXAnageur" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/5209ead29ee902d92d7f93d15cb365e38475f257_2_690x367.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/5209ead29ee902d92d7f93d15cb365e38475f257_2_1035x550.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/5209ead29ee902d92d7f93d15cb365e38475f257_2_1380x734.jpeg 2x" data-dominant-color="8B899D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot2</span><span class="informations">1917×1021 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @ayman_bali (2023-03-06 22:37 UTC)

<p>I checked now through the 3d Model and the images are actually in the right order inside the 3d Model, but its still not looking like the one you had in your screenshot <img src="https://emoji.discourse-cdn.com/twitter/confused.png?v=12" title=":confused:" class="emoji" alt=":confused:" loading="lazy" width="20" height="20"></p>

---

## Post #9 by @muratmaga (2023-03-07 00:01 UTC)

<aside class="quote no-group" data-username="ayman_bali" data-post="8" data-topic="28191">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ayman_bali/48/18648_2.png" class="avatar"> ayman_bali:</div>
<blockquote>
<p>ts still not looking like the one you had in your screenshot</p>
</blockquote>
</aside>
<p>What do you mean, apart from the arrangement of the windows, they look pretty similar to me.</p>

---

## Post #10 by @ayman_bali (2023-03-07 08:41 UTC)

<p>Hey Murat,</p>
<p>im sorry from the first look, i thought that your 3d model was different and didnt have this rough transitions between the layers, my goal is to make these transitions between the layers as smooth as possible.</p>
<p>Thank you so much for your help!!</p>
<p>Best regards,<br>
Ayman</p>

---

## Post #11 by @ayman_bali (2023-03-07 10:22 UTC)

<p>UPDATE:</p>
<p>I have applied a registration algorithm to the images in the hope of obtaining a better 3D view.</p>
<p>My problem is that the transitions between the layers don’t look smooth. My goal is to reconstruct the shape of the sample with curved edges, but what I am seeing are sharp edges between each layer.</p>
<p>First question: Is what I am thinking feasible? Can I reconstruct the sample with curved edges?</p>
<p>Second question: What am I doing wrong? Would the sharp edges go away if I increase the number of slices, for example?</p>
<p>Best regards,<br>
Ayman<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd9374e4b9ea0ba696b84deafe0c3bc53aa24629.jpeg" data-download-href="/uploads/short-url/AbeIUsjO1GS3hAOeU2WOGQTLz2F.jpeg?dl=1" title="Unbenannt.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd9374e4b9ea0ba696b84deafe0c3bc53aa24629_2_690x411.jpeg" alt="Unbenannt.PNG" data-base62-sha1="AbeIUsjO1GS3hAOeU2WOGQTLz2F" width="690" height="411" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd9374e4b9ea0ba696b84deafe0c3bc53aa24629_2_690x411.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd9374e4b9ea0ba696b84deafe0c3bc53aa24629_2_1035x616.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd9374e4b9ea0ba696b84deafe0c3bc53aa24629_2_1380x822.jpeg 2x" data-dominant-color="6D6D70"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Unbenannt.PNG</span><span class="informations">1677×999 153 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #12 by @muratmaga (2023-03-07 17:31 UTC)

<aside class="quote no-group" data-username="ayman_bali" data-post="11" data-topic="28191">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ayman_bali/48/18648_2.png" class="avatar"> ayman_bali:</div>
<blockquote>
<p>First question: Is what I am thinking feasible?</p>
</blockquote>
</aside>
<p>This is feasible to the extend that these slides do not have large gaps between them, i.e., the sections are sufficiently sampled. Are you sure the spacing between slides is the same as the in-plane spacing (0.1 mm). In my experience they are usually least an order of magnitude larger. Yes, jagged edges will probably be less jagged if you include more slides (but they also need to be correctly registered) and used the correct spacing.</p>
<aside class="quote no-group" data-username="ayman_bali" data-post="11" data-topic="28191">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ayman_bali/48/18648_2.png" class="avatar"> ayman_bali:</div>
<blockquote>
<p>Second question: What am I doing wrong? Would the sharp edges go away if I increase the number of slices, for example?</p>
</blockquote>
</aside>
<p>I don’t think you are doing anything wrong. You just need to find a registration algorithm that will do a better slice-to-slice registration. I highlighted one slide that’s obviously quite offset with respect to the others. The others are like that, but not as obvious.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f30ec1c7bb0ad1cda783e55d47a616514c42ae7.png" data-download-href="/uploads/short-url/biyxdlyOX4lEtn6UH6xJpyZtCET.png?dl=1" title="Screen Shot 2023-03-07 at 9.28.32 AM"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f30ec1c7bb0ad1cda783e55d47a616514c42ae7_2_690x484.png" alt="Screen Shot 2023-03-07 at 9.28.32 AM" data-base62-sha1="biyxdlyOX4lEtn6UH6xJpyZtCET" width="690" height="484" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f30ec1c7bb0ad1cda783e55d47a616514c42ae7_2_690x484.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f30ec1c7bb0ad1cda783e55d47a616514c42ae7_2_1035x726.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f30ec1c7bb0ad1cda783e55d47a616514c42ae7.png 2x" data-dominant-color="414040"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2023-03-07 at 9.28.32 AM</span><span class="informations">1074×754 216 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @Shiyang_Tian (2023-06-20 22:48 UTC)

<p>Hello! I have some histology slices as well and they are already registered, I am trying to have them show on the 3D module as you did. But when I tried to visualize them, the 3D module on the left only gave me black spaces. If possible, could you share you steps on importing these images and how did you manage to turn them into 3D? Thanks!</p>

---

## Post #14 by @Shiyang_Tian (2023-06-20 22:57 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9ccafe9c47ef0cfad94e2b4a2965bc859bd4eb8d.jpeg" data-download-href="/uploads/short-url/mn3oKJFwn2AsnqTLFKCaphuCToh.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9ccafe9c47ef0cfad94e2b4a2965bc859bd4eb8d_2_690x427.jpeg" alt="image" data-base62-sha1="mn3oKJFwn2AsnqTLFKCaphuCToh" width="690" height="427" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9ccafe9c47ef0cfad94e2b4a2965bc859bd4eb8d_2_690x427.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9ccafe9c47ef0cfad94e2b4a2965bc859bd4eb8d_2_1035x640.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9ccafe9c47ef0cfad94e2b4a2965bc859bd4eb8d_2_1380x854.jpeg 2x" data-dominant-color="878693"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1189 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
This is what I have if you want to take a look</p>

---

## Post #15 by @muratmaga (2023-06-21 00:15 UTC)

<p>According to the screenshot you are getting an Invalid Texture Dimensions errors (i.e., the dimensions of the your dataset is larger than what your GPU driver supports). Try switching to CPU rendering, and you should be able to get something in 3D viewer (it might be slow).</p>

---

## Post #16 by @waltbobrowski (2023-06-21 01:35 UTC)

<p>For alignment of a serial stack of histology section images, I’m using ImageJ with the TrackEM plugin.<br>
Here is a link below to a complete description of the steps required. I’ve found that I’ve needed to do multiple passes, including more tedious pair-wise alignment using the landmark option with aligning (2-3 landmarks should work). However, you will not get 100% alignment due to deformations in the tissue sections and many of your sections have missing components or heavily damaged.<br>
After alignment in TrakEM, you right-click and select EXPORT then save those to a new folder. Watch all the options! Also, after alignment you can draw a rectangular marqee to capture all stack elements prior to export to remove extraneous background.</p>
<p><a href="http://stefischer.de/2019/06/01/aligning-an-image-stack-in-trackem2/#comments" rel="noopener nofollow ugc">Aligning an image stack in TrackEM2 – Electron microscopy / Image analysis / 3D reconstruction (stefischer.de)</a></p>

---

## Post #17 by @waltbobrowski (2023-06-21 17:34 UTC)

<p>414 serial sections of a ganglion. So to get it this good as shown (still not “perfect” when you examine edge misalignments in the coronal and sagittal views), after doing basic TrakEM alignment, I then performed more critical pair-wise alignment using Landmarks (up to 12 per pair). Using many landmarks helps with elasticity as histology sections look great individually but a lot of deformation occurs while the cut section relaxes prior to placement on a glass slide due to both individual protein components and the fixation rigidity for those individual components. “Optical sectioning” (aka confocal, MRI, etc) is easy for registration. Histology sections which deform and rotate as they are gathered make the downstream alignment process extremely tedious &amp; difficult.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/930cba2692e05832145eccccba3d10add937614e.jpeg" data-download-href="/uploads/short-url/kYRsgFZYruq8vf618JkdsA6ZScm.jpeg?dl=1" title="ScreenShot-FullRes-PostCriticalPairWiseSectionAlignments" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/930cba2692e05832145eccccba3d10add937614e_2_690x329.jpeg" alt="ScreenShot-FullRes-PostCriticalPairWiseSectionAlignments" data-base62-sha1="kYRsgFZYruq8vf618JkdsA6ZScm" width="690" height="329" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/930cba2692e05832145eccccba3d10add937614e_2_690x329.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/930cba2692e05832145eccccba3d10add937614e_2_1035x493.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/930cba2692e05832145eccccba3d10add937614e_2_1380x658.jpeg 2x" data-dominant-color="746A81"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ScreenShot-FullRes-PostCriticalPairWiseSectionAlignments</span><span class="informations">1918×917 382 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
