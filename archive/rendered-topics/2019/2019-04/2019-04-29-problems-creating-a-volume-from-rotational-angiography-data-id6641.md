---
topic_id: 6641
title: "Problems Creating A Volume From Rotational Angiography Data"
date: 2019-04-29
url: https://discourse.slicer.org/t/6641
---

# Problems creating a volume from rotational angiography data

**Topic ID**: 6641
**Date**: 2019-04-29
**URL**: https://discourse.slicer.org/t/problems-creating-a-volume-from-rotational-angiography-data/6641

---

## Post #1 by @Deyline (2019-04-29 13:55 UTC)

<p>Hello Slicer wizards,</p>
<p>I’ve been trying to generate a volume from DICOM data that I’ve obtained from a rotational angiography scan. To help me explain the problem I’m encountering, I’ve attached 2 images. The first image shows the problem I’m getting, apparently the rotational angiography does not provide me 3D data, but sort of a “2D data over a time”, not sure how I could classify it. This can be easily seen when analysing the top right of the image, where only one view is actually correct. Is it possible to generate volume from this type of data or a CT scan is what I should be looking for?<br>
For the second image, a 3D model was generated in the machine that does the angiography. Is it possible to generate volumes from these already pre-made volumes from the machine’s software? Because if I try to import it, slicer only treats it as being a 2D image, as seen from the Y and G views.</p>
<p>Thanks in advance!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/9892a891893ba53110bf8bfa1aa09fe3b4a9f26e.jpeg" data-download-href="/uploads/short-url/lLIMY7dRudDb0UI1DeaQxqAYzLw.jpeg?dl=1" title="slicer3d_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9892a891893ba53110bf8bfa1aa09fe3b4a9f26e_2_690x369.jpeg" alt="slicer3d_1" data-base62-sha1="lLIMY7dRudDb0UI1DeaQxqAYzLw" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9892a891893ba53110bf8bfa1aa09fe3b4a9f26e_2_690x369.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9892a891893ba53110bf8bfa1aa09fe3b4a9f26e_2_1035x553.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/9892a891893ba53110bf8bfa1aa09fe3b4a9f26e.jpeg 2x" data-dominant-color="C3C3C4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer3d_1</span><span class="informations">1361×728 234 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2019-04-29 14:09 UTC)

<p>This looks like a sinogram (projection images acquired during the rotation), which needs to be reconstructed to a 3D Cartesian volume. See more information in these topics:</p>
<aside class="quote" data-post="15" data-topic="4272">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/volume-rendering-shows-solid-black-cube-only/4272/15">Volume rendering shows solid black cube only</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    It looks like the image is not a Cartesian 3D volume but a <a href="https://en.wikipedia.org/wiki/Tomographic_reconstruction">sinogram</a>. You need to run these images through filtered backprojection or similar reconstruction method to get a 3D volume that you can load into Slicer.
  </blockquote>
</aside>

<aside class="quote" data-post="2" data-topic="2768">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gcsharp/48/863_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/issues-viewing-dicom-files-after-import/2768/2">issues viewing DICOM files after import</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi Freya, 
Based on the image in the lower right, it looks like you have projection data (aka sinogram data).  When you scroll through the upper left, does it look like a sequence of images taken at different angles?  If so, you need to ask the scanner technician for “reconstructed” data. 
Greg
  </blockquote>
</aside>

<aside class="quote no-group" data-username="Deyline" data-post="1" data-topic="6641">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/278dde/48.png" class="avatar"> Deyline:</div>
<blockquote>
<p>For the second image, a 3D model was generated in the machine that does the angiography. Is it possible to generate volumes from these already pre-made volumes from the machine’s software?</p>
</blockquote>
</aside>
<p>That is just a screenshot. If there is any 3D information in that image, it is stored in private fields.</p>
<p>What devices (manufacturer, model, number) did you use to acquire and visualize/reconstruct the images?</p>

---

## Post #3 by @pieper (2019-04-29 14:29 UTC)

<p><a class="mention" href="/u/gcsharp">@gcsharp</a> would it make sense to consider an <a href="http://www.openrtk.org" rel="nofollow noopener">openrtk</a> extension?</p>

---

## Post #4 by @gcsharp (2019-04-29 14:55 UTC)

<p>Maybe for people who are uncomfortable with command line programs it could be good.  Currently, a (potential, proposed) workflow within Slicer does not seem easier (IMO) than to run RTK separately.</p>
<p>If an RTK extension were available would people make add-on programs to do image processing on projection data, thereby proving the value of the extension?  Who knows!</p>
<p>[Edited for clarity.]</p>

---

## Post #5 by @lassoan (2019-04-29 15:29 UTC)

<aside class="quote no-group" data-username="gcsharp" data-post="4" data-topic="6641">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gcsharp/48/863_2.png" class="avatar"> gcsharp:</div>
<blockquote>
<p>Currently, a (potential, proposed) workflow within Slicer does not seem easier (IMO) than to run RTK separately.</p>
</blockquote>
</aside>
<p>Oh yes, I would find it much easier if it was distributed as a Slicer extension and could be installed and executed by a couple of clicks!</p>
<p>The problem with RTK starts with a note on download page: “The current release is version 1.3.0 from September 2016”. For me, it means that the project is dead and I should probably not waste any time with it.</p>
<p>OK, I go past this, but then I find that there is <a href="http://www.openrtk.org/RTK/resources/software.html">no binary download</a>. I give up at this point. Since the project is dead, I will not spend time with trying to build it, running into issues, and then having difficulties with trying to get help. Github repository seems to be linked to a single GitHub user, not an organization - another red flag.</p>
<p>I also glanced at the documentation section. There was no mention of any command-line tools, just <a href="http://www.openrtk.org/Doxygen/index.html">API reference</a>. After this, I’m certain that this toolkit will not work for me.</p>
<p>Maybe the actual situation is better, maybe the toolkit is not dead, there are pre-built binaries and documentation available somewhere… but then toolkit’s website is extremely poor and misleading.</p>

---

## Post #6 by @pieper (2019-04-29 16:11 UTC)

<p>I hadn’t looked at openrtk in detail and not recently, but I noticed <a href="http://www.openrtk.org/RTK/news/201902_release2.0.php" rel="nofollow noopener">that version 2.0</a> was released very recently and that gives me hope the project is still very viable.  I agree with <a class="mention" href="/u/lassoan">@lassoan</a> that easy to install and use binaries could be a boost.</p>

---

## Post #7 by @gcsharp (2019-04-29 16:14 UTC)

<p>Typical use cases for reconstruction software are: (1) algorithm R&amp;D, and (2) equipment development.  As such, RTK has a more narrowly focused set of users than Slicer, and I don’t know how an extension would improve their workflow.</p>
<p>If an RTK extension were made, it should include the python API.</p>
<p>Thank you for spotting the error on the web site about the current release.  I’ll post a message to let them know.</p>

---

## Post #8 by @pieper (2019-04-29 16:29 UTC)

<p>True, if users with a sinogram could just as easily request a reconstruction from their scanner then there’s no point in making an extension.</p>

---

## Post #9 by @Deyline (2019-04-29 17:06 UTC)

<p>Thanks for the help <a class="mention" href="/u/lassoan">@lassoan</a><br>
Let me see if I got the right idea after reading the 2 topics you have sent me.<br>
I can reconstruct a volume from the software that acquired the sinogram and from that I would export as .dcm to slicer? Because the screenshot that I showed in the second image was the reconstruction made by the machine’s software, but I probably exported it wrong.<br>
As for the device, I’ll contact the physician responsible for the images, since all I know is that the device/software are from Philips (I don’t think that this is enough info).</p>
<p>Edit: Just got in contact with the physician and the device model is “Allura FD10” with the “3D RA” software. Both the device and software are from Philips.</p>

---

## Post #10 by @lassoan (2019-04-29 17:31 UTC)

<p>Thanks for the update. I agree that the best would be to export the reconstructed 3D volume as a CT image from the Philips software.</p>

---

## Post #11 by @kopachini (2019-04-30 06:12 UTC)

<p>Try to import that fluoroscopy study in Philips IntelliSpace Portal (you should ask someone at your radiology department) and if you can open it maybe it is possible to make VRT reconstructions. If you are able to do so than you could export that VRT as. stl file simply by clicking right mouse button on VRT and choose save as stl.<br>
Please let me know the results because my department got Philips Azurion <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #12 by @Deyline (2019-04-30 12:29 UTC)

<p>Thanks for the suggestion <a class="mention" href="/u/kopachini">@kopachini</a>.<br>
However, I do not think our radiology department has this software at our disposal, unfortunately. I had a check on this software, and it would probably solve our problem, but I need to work with what we have, which is the Allura - 3DRA software. Has your department used or has any idea if this specific software is able to do something similar or at least export volumetric data as .dcm so I can generate a 3D model in blender?</p>

---

## Post #13 by @kopachini (2019-04-30 12:52 UTC)

<p>Hi, unfortunately I don’t know what softwer we will have with Azurion.<br>
What I ment is that if you have Philips fluoroscopy, maybe the department have Philips CT machine wich comes with Intellispace Portal so you could import it there.</p>
<p>uto, 30. tra 2019. 14:39 Deyline via 3D Slicer Forum <a href="mailto:slicer@discoursemail.com">slicer@discoursemail.com</a> je napisao:</p>

---

## Post #14 by @lassoan (2019-05-01 03:04 UTC)

<p>It would be extremely limiting if you could only export STL files from your 3DRA acquisitions. The 3D reconstructed volumetric image contains much more information. You can use volume rendering for visualization or segmentation structures to save them as STL files, etc.</p>
<p>Your Philips representative should be able to tell you what options you have to access reconstructed 3D volume in DICOM format.</p>

---

## Post #15 by @kopachini (2019-05-10 16:06 UTC)

<p>Hello everybody, a few days ago educator from Philips came at angio suite regarding Azurion machine. Under rotational angiography, you mean CBCT? If that is so than it is possible to export that study into Philips IntelliSpace portal and export stl file from VRT</p>

---

## Post #16 by @VincentYu (2019-10-23 08:53 UTC)

<p>Is there any module in 3D Slicer related to “filtered backprojection”?<br>
I have similar problem, creating volume from a rotational angiography data, and noticed Lasso’s reply in <a href="https://discourse.slicer.org/t/volume-rendering-shows-solid-black-cube-only/4272/15" class="inline-onebox">Volume rendering shows solid black cube only</a>, which mentioned the technique to reconstruct 3D volume from sinogram. If necessary, I can share the DICOM (anonymous) link here.</p>

---

## Post #17 by @lassoan (2019-10-23 13:28 UTC)

<p>I’m not aware of any Slicer module that can do this. The best would be to implement a GUI  for <a href="http://www.openrtk.org/" rel="nofollow noopener">RTK toolkit</a> as a Slicer module. You can submit a request on their bugtracker to implement a Slicer module, implement it yourself (we can help you to get started), or use its existing Python or command-line interface.</p>

---

## Post #18 by @luigi_m (2020-05-13 18:13 UTC)

<p>Hi everybody,<br>
i’m writing a thesis about 3D printing aplications in neurosurgery and i’m having the same trouble that has generated this topic: i haven’t found any way to obtain a <strong>3D model from a rotational angiography</strong>:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c5bb692852958aee872432168c9adfd6669c7d51.jpeg" alt="screenshot_angio" data-base62-sha1="sddApYYhn7rhjHZLxxQyTps8MuJ" width="434" height="318"></p>
<p>Since some time is passed, do you know if any solution has been created? because RTK toolkit looks really too much complicated for me…<br>
Otherwise i will follow <a class="mention" href="/u/lassoan">@lassoan</a> 's suggestion and i will submit a request to implement a Slicer module</p>
<p>Thanks in advance <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"></p>

---

## Post #19 by @lassoan (2020-05-16 19:00 UTC)

<p>You have a 2D projection image sequence, which is not a 3D volume. You can use <a href="http://www.openrtk.org/">RTK</a> to reconstruct a 3D volume.</p>

---

## Post #20 by @Anton_Fomenko (2022-08-19 15:08 UTC)

<p>Hi Deyline. I have the exact same issue as you (trying to use Slicer to reconstruct cerebral angio). Just wondering - did you ever find a solution to this issue? If so would love to hear from you ASAP</p>

---

## Post #21 by @Luxalyn (2024-01-22 10:32 UTC)

<p>Hi Anton, May I ask you, as well <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> , if you could ever find a solution to this problem?</p>

---
