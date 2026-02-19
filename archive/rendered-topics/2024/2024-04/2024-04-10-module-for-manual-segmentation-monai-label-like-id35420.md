---
topic_id: 35420
title: "Module For Manual Segmentation Monai Label Like"
date: 2024-04-10
url: https://discourse.slicer.org/t/35420
---

# Module for manual segmentation (MONAI Label-like)

**Topic ID**: 35420
**Date**: 2024-04-10
**URL**: https://discourse.slicer.org/t/module-for-manual-segmentation-monai-label-like/35420

---

## Post #1 by @nicola-dallosto (2024-04-10 20:27 UTC)

<p>I need to create a module to segment nifti images. My idea was to recreate the settings panel of MONAI Label (see screenshot) because it consent to connect to a server and there is a button to save the annotation and a button to upload another image from the dataset. I don’t need all the other stuff for automatic segmentation, but Segment Editor to manually segment images.<br>
The main problem is that when you start a MONAILabel server, it also upload pretrained models for automatic segmentation. So, the function present in MONAI Label module does not simply retrieve data from a server, but it imports also the pretrained models and other information. However, I only need a section in my module that has the function to connect to the database’s URL. The module then upload the first image of the dataset, the user segments it, save the segmentation, click “next sample”, another image is uploaded, and so on.<br>
Is there anyone that can help me?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/8097e9c75bf1e804d1767938b0eef62dd0dad5a7.png" data-download-href="/uploads/short-url/ilAAv85zKEpj4ICnasQEry9VpFd.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/8097e9c75bf1e804d1767938b0eef62dd0dad5a7_2_214x500.png" alt="image" data-base62-sha1="ilAAv85zKEpj4ICnasQEry9VpFd" width="214" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/8097e9c75bf1e804d1767938b0eef62dd0dad5a7_2_214x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/8097e9c75bf1e804d1767938b0eef62dd0dad5a7_2_321x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/8097e9c75bf1e804d1767938b0eef62dd0dad5a7_2_428x1000.png 2x" data-dominant-color="373738"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">449×1047 40.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @rfenioux (2024-04-11 09:20 UTC)

<p>One thing you can do is first have a look at the code of the MONAILabel Module. It is available on the <a href="https://github.com/Project-MONAI/MONAILabel/tree/main/plugins/slicer/MONAILabel" rel="noopener nofollow ugc">github repository</a>. Alternatively you can use the “Edit” button in the reload &amp; test panel to open the main python file of the module.</p>
<p>From there you could have a look at the logic used for the communication with the server for uploading and retrieving images.</p>
<p>However, I don’t know how generic the code is, it might be only specific for communication with the monailabel server application. Maybe someone else can comment on the feasibility of your approach.</p>

---

## Post #3 by @nicola-dallosto (2024-04-11 16:30 UTC)

<p>There is a big obstacle that I’m facing. To simplify, I found a module, called <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ImportFromURL" rel="noopener nofollow ugc">ImportFromURL</a>, in the <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master" rel="noopener nofollow ugc">SlicerMorph</a> extension that allows the retrieval of images from URLs and I created a new extension using Extension Wizard in 3D Slicer. I’ve tried to simply copy and paste the Python code of ImportFromURL in my new module, but it is not clear to me how and if I need to modify also the UI of the widget using Qt Designer. By copying and pasting the code from one module to my module, my module interface appears empty. Is there a step I am missing or am I doing something wrong?</p>

---
