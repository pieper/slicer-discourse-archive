---
topic_id: 19165
title: "Is It Possible To Segment Image Data In The View Of Volume R"
date: 2021-08-12
url: https://discourse.slicer.org/t/19165
---

# Is it possible to segment image data in the view of volume rendering?

**Topic ID**: 19165
**Date**: 2021-08-12
**URL**: https://discourse.slicer.org/t/is-it-possible-to-segment-image-data-in-the-view-of-volume-rendering/19165

---

## Post #1 by @WilliamDaniel (2021-08-12 02:12 UTC)

<p>Hello,<br>
I am new to 3D Slicer, and currently, I am learning how to develop a new module in 3D Slicer to implement new features.<br>
The basic idea of the module I am going to achieve is:</p>
<p>To enable users to specify and extract image data from a specific region by placing widgets like ROI boxes in the volume rendering view for subsequent statistical calculations. For example, first, the user places an ROI box in the 3D view of volume rendering and then clicks a button on the GUI panel implemented by this module to get the count of pixels in the region enclosed by the ROI box, which is somewhat similar to the segmentation operation.</p>
<p>I learned that the ‘segment editor’ module in 3D Slicer could be used to perform segmentation, but it is done by iterating all the medical image slices and drawing contour lines on three orthogonal planes. The user cannot directly extract the ROI in the 3D view of the volume rendering through widgets (in my case, I would like to extract the information such as pixel count in a box-shaped region by placing a box in the 3D view directly.)</p>
<p>Therefore, is it possible to implement this feature in 3D Slicer? Could you please elaborate on the feasibility of developing this feature? What do I need to learn to develop this module?</p>
<p>I appreciate any help and suggestions in advance!</p>
<p>The figure below is similar to the effect I’m going to achieve, FYI:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c046dbca5033cc58e066b757a28070425ad22d03.jpeg" alt="BOX segmentation" data-base62-sha1="rqXugbzM1mtZtnavNgViFJ4RXk7" width="345" height="306"></p>

---

## Post #2 by @lassoan (2021-08-12 03:47 UTC)

<aside class="quote no-group" data-username="WilliamDaniel" data-post="1" data-topic="19165">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/williamdaniel/48/13425_2.png" class="avatar"> WilliamDaniel:</div>
<blockquote>
<p>but it is done by iterating all the medical image slices and drawing contour lines on three orthogonal planes</p>
</blockquote>
</aside>
<p>You can segment by iterating through slices but there are many other tools.</p>
<p>If you just need a rectangular region then you can draw an annotation or markups ROI and crop the volume using Crop volume module.</p>
<p>If you need free-form cutouts then I would recommend to try Scissors or Surface cut effects to specify region of interest and then add or remove the selected region using Volume clip effect. Install SegmentEditorExtraEffects extension, as it provides a number of additional effects.</p>

---

## Post #4 by @WilliamDaniel (2021-08-13 00:45 UTC)

<p>Hello Dr.Lassoan,<br>
Thank you for your kind and quick response!<br>
Cool, I see that combine ‘Scissors’ and ‘Mask volume’ can help users to segment image data in the 3D view of volume rendering.<br>
Although I know that both segmentation operations and volume calculations can be done by tools and modules that already exist in 3D Slicer (Scissors, Mask volume, Segmentation statistics).<br>
My purpose is to integrate above functions into one plug-in. Therefore, the form of operation and the workflow will be different with the tools you mentioned.<br>
Is it feasible to develop this module?<br>
Now that these tools of 3D Slicer have implemented similar functions, does this mean that it will be more convenient to implement my own modules and workflows?<br>
Could you please give more suggestions?<br>
Thank you very much!</p>

---

## Post #5 by @lassoan (2021-08-13 04:09 UTC)

<aside class="quote no-group" data-username="WilliamDaniel" data-post="4" data-topic="19165">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/williamdaniel/48/13425_2.png" class="avatar"> WilliamDaniel:</div>
<blockquote>
<p>My purpose is to integrate above functions into one plug-in. Therefore, the form of operation and the workflow will be different with the tools you mentioned.<br>
Is it feasible to develop this module?</p>
</blockquote>
</aside>
<p>You need to set up a number of things in multiple modules, so if you want cutting in volume rendering conveniently available (because you need to process hundreds of cases or you are time-constrained or the software will be operated by clinicians) then it make sense to add a scripted module that sets up everything automatically on a single click. It should be fairly straightforward to do this, there are lots of examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#segmentations">script repository</a>.</p>

---

## Post #6 by @WilliamDaniel (2021-08-13 14:10 UTC)

<p>Hello Dr.Lassoan,<br>
Thank you so much for your reply, I will try to learn how to implement my own workflow from these examples you provided. <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=10" title=":+1:" class="emoji" alt=":+1:"></p>

---

## Post #7 by @WilliamDaniel (2022-01-15 00:56 UTC)

<p>Hello lassoan,<br>
Thank you so much for your previous guidance, I have learned how to create an extension from the tutorial you provided and the development process has been relatively smooth so far.<br>
And you’ve mentioned:</p>
<blockquote>
<p>You need to set up a number of things in multiple modules, so if you want cutting in volume rendering conveniently available (because you need to process hundreds of cases or you are time-constrained or the software will be operated by clinicians) then it make sense to add a scripted module that sets up everything automatically on a single click.</p>
</blockquote>
<p>That’s exactly how my extension working(Sets up some useful functionalities of existing modules automatically on a single click.)</p>
<p>My question is: After I finish developing this extension, may I distribute and publish it to the Slicer Extensions Index so that users can download it from slicer directly?</p>
<p>Thank you!</p>

---

## Post #8 by @lassoan (2022-01-15 13:17 UTC)

<p>It would be great if you could submit your extension to the extensions index so that users can install it by a few clicks. See details here: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#distribute-an-extension" class="inline-onebox">Extensions — 3D Slicer documentation</a></p>

---
