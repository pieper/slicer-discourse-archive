# Create a Draw tube and move it

**Topic ID**: 13856
**Date**: 2020-10-04
**URL**: https://discourse.slicer.org/t/create-a-draw-tube-and-move-it/13856

---

## Post #1 by @Hamid (2020-10-04 21:29 UTC)

<p>I created a tube using Draw tube, I want to move it to connect to another part.How can I move it?</p>

---

## Post #2 by @lassoan (2020-10-04 23:26 UTC)

<p>You can click Edit button in Draw tube effect options to edit the control points, then you can repaint the tube into the selected segment.</p>

---

## Post #3 by @Hamid (2020-10-26 15:28 UTC)

<p>What is the difference between labelmap and Model?!</p>

---

## Post #4 by @Hamid (2020-10-27 16:28 UTC)

<p>I gave a  5mm thickness to my model, but when I measure it by using ruler it says 3 mm!!! which one should I rely on?</p>

---

## Post #5 by @jamesobutler (2020-10-27 16:35 UTC)

<p><a class="mention" href="/u/hamid">@hamid</a> Can you provide screenshots of what you are measuring? The model is used to generate the labelmap. The model is in continuous space while the labelmap is in discrete space so what the model shows is not going to generate a labelmap that is exactly the same.</p>

---

## Post #6 by @Hamid (2020-10-27 16:44 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/220290a322137a051952e8e1b062d2e2da0fd35e.jpeg" data-download-href="/uploads/short-url/4QRJe2zUzVFBnsFw6WnMDwesLka.jpeg?dl=1" title="Aorta thickness" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/220290a322137a051952e8e1b062d2e2da0fd35e_2_534x500.jpeg" alt="Aorta thickness" data-base62-sha1="4QRJe2zUzVFBnsFw6WnMDwesLka" width="534" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/220290a322137a051952e8e1b062d2e2da0fd35e_2_534x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/220290a322137a051952e8e1b062d2e2da0fd35e.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/220290a322137a051952e8e1b062d2e2da0fd35e.jpeg 2x" data-dominant-color="8485A3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Aorta thickness</span><span class="informations">765×716 55.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @lassoan (2020-10-27 16:45 UTC)

<p>The model and labelmap should be very close (you can reduce surface smoothing to make them more similar).</p>
<p>You may see significant differences between the size that you request for brush size, tube radius, shell thickness, etc. and the actual size that can be represented in the labelmap at the current resolution. If you find that this difference is too large then you can increase the resolution of the segmentation (at the cost of increased memory usage and computation time).</p>

---

## Post #8 by @Hamid (2020-10-27 16:45 UTC)

<p>This is the thickness that I set for 5mm but it says around 2mm for descending Aorta</p>

---

## Post #9 by @lassoan (2020-10-27 16:47 UTC)

<p>Are you using latest stable release (Slicer-4.11.20200930)?</p>

---

## Post #10 by @Hamid (2020-10-27 17:31 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e7fa022e6fda99ab90ed1a39658a37eb483b10f.jpeg" data-download-href="/uploads/short-url/fLvXphWEIVsh9Auy0HMYfpIsm0T.jpeg?dl=1" title="2020" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6e7fa022e6fda99ab90ed1a39658a37eb483b10f_2_690x388.jpeg" alt="2020" data-base62-sha1="fLvXphWEIVsh9Auy0HMYfpIsm0T" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6e7fa022e6fda99ab90ed1a39658a37eb483b10f_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6e7fa022e6fda99ab90ed1a39658a37eb483b10f_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6e7fa022e6fda99ab90ed1a39658a37eb483b10f_2_1380x776.jpeg 2x" data-dominant-color="C6C9D7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2020</span><span class="informations">1920×1080 235 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I am using this version!</p>

---

## Post #11 by @Hamid (2020-10-27 17:32 UTC)

<p>Many thanks to you James!</p>

---

## Post #13 by @lassoan (2020-11-05 21:02 UTC)

<p>A post was split to a new topic: <a href="/t/dicom-browser-hangs/14452">DICOM browser hangs</a></p>

---

## Post #14 by @Hamid (2020-10-28 01:11 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a>, How can I increase the resolution of the segmentation?</p>

---

## Post #15 by @Hamid (2020-11-05 17:58 UTC)

<p>I need to extend the three  arch branches to some extent.But the Slicer dose NOT allowed me to draw tube or … outside the magenta cubic from the top side ‘S’!<br>
Is there any way to do this?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc5c8d628a2ae71c2c53040a827b8ccfe61e39d6.png" data-download-href="/uploads/short-url/vrpkP1xQmyOLzrHOKiXBsWyWJeK.png?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc5c8d628a2ae71c2c53040a827b8ccfe61e39d6_2_584x500.png" alt="Screenshot" data-base62-sha1="vrpkP1xQmyOLzrHOKiXBsWyWJeK" width="584" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc5c8d628a2ae71c2c53040a827b8ccfe61e39d6_2_584x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc5c8d628a2ae71c2c53040a827b8ccfe61e39d6.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc5c8d628a2ae71c2c53040a827b8ccfe61e39d6.png 2x" data-dominant-color="989BCC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">590×505 28 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #16 by @manjula (2020-11-05 18:45 UTC)

<p>You need to create an empty volume above that space as it is the limit of your volume.</p>
<p>There may be other more elegant ways of doing this but one that comes to my mind is to draw a ROI  box to include your current volume and extend it up to the excess space you want and then crop it using the crop module. (you can specify the fill value for this newly created space in the crop volume)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/006b54a3f006af986d21680cb634ae32df82e26a.png" data-download-href="/uploads/short-url/3HXchaO62XMtIFpoEDzWXuYvOO.png?dl=1" title="Screenshot from 2020-11-05 19-48-56" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/006b54a3f006af986d21680cb634ae32df82e26a_2_690x388.png" alt="Screenshot from 2020-11-05 19-48-56" data-base62-sha1="3HXchaO62XMtIFpoEDzWXuYvOO" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/006b54a3f006af986d21680cb634ae32df82e26a_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/006b54a3f006af986d21680cb634ae32df82e26a_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/006b54a3f006af986d21680cb634ae32df82e26a_2_1380x776.png 2x" data-dominant-color="BCC1D4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-11-05 19-48-56</span><span class="informations">1920×1080 281 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/581ef79ffd20e95f2e04804e686a991485e2e864.png" data-download-href="/uploads/short-url/czymB8We6GItpydo2cuoq76ieQA.png?dl=1" title="Screenshot from 2020-11-05 19-52-16" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/581ef79ffd20e95f2e04804e686a991485e2e864_2_690x388.png" alt="Screenshot from 2020-11-05 19-52-16" data-base62-sha1="czymB8We6GItpydo2cuoq76ieQA" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/581ef79ffd20e95f2e04804e686a991485e2e864_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/581ef79ffd20e95f2e04804e686a991485e2e864_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/581ef79ffd20e95f2e04804e686a991485e2e864_2_1380x776.png 2x" data-dominant-color="BEC2D8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-11-05 19-52-16</span><span class="informations">1920×1080 217 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #17 by @Hamid (2020-11-06 21:12 UTC)

<p>Thank you so much manjula,<br>
I tried to make ROI volume and then extend the three branches to some extent but the extended parts (inside the new volume and outside of the origin volume) do NOT show up.Would you please help me to make a ROI volume?Mabe I have not made the ROI correctly.<br>
Should I go to the volume rendering to make the ROI and then using segment editor to lengthen 3 branches?</p>

---

## Post #18 by @manjula (2020-11-06 22:57 UTC)

<p>I believe you must have not selected the newly cropped volume in the segment editor?</p>

---

## Post #19 by @Hamid (2020-11-07 01:51 UTC)

<p>I choose the cropped volume in segment editor and when I reload the .mrml file(the previous lumen) and new cropped volume(.nrrd file) together the extended branches (using Draw Tube) do not show up in cropped volume!!!<br>
But when I reload just the .nrrd file , the Draw Tube works on it.</p>

---

## Post #20 by @Hamid (2020-11-07 02:16 UTC)

<p>Moreover I need to merge these two together and make a thick shell</p>

---

## Post #21 by @manjula (2020-11-07 12:27 UTC)

<p>I still think you are working in different segments with different volumes.</p>
<p>You can combine the two segments with the logical operators in the segment editor.</p>

---

## Post #22 by @Hamid (2020-11-07 20:22 UTC)

<p>I do modifications as bellow:<br>
1- load the original .mrml file.<br>
2- from the top I choose Crop Volume and name the output volume as ‘cropped volume’ and then click Apply.<br>
3- save this new file.<br>
4- reopen the slicer and load the new file. hit the Segment Editor, click on master volume to set the ‘cropped volume’ and then go through the effect to Draw tube and do some modifications.at this point I see the new ROI in my 3d view but when draw something there, nothing shows up in new ROI!!!<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8b178381be9f873ada842577fad261b43da91e5.jpeg" data-download-href="/uploads/short-url/zu2DEqqq8gQxG7kg8qaWiNSTBhH.jpeg?dl=1" title="photo_2020-11-07_15-24-23" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f8b178381be9f873ada842577fad261b43da91e5_2_666x500.jpeg" alt="photo_2020-11-07_15-24-23" data-base62-sha1="zu2DEqqq8gQxG7kg8qaWiNSTBhH" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f8b178381be9f873ada842577fad261b43da91e5_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f8b178381be9f873ada842577fad261b43da91e5_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8b178381be9f873ada842577fad261b43da91e5.jpeg 2x" data-dominant-color="8A8997"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">photo_2020-11-07_15-24-23</span><span class="informations">1280×960 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #23 by @manjula (2020-11-07 20:33 UTC)

<p>I do not know why you need to close and re open the file.</p>
<p>I think the problem is that it does not work if you just change the master volume from the drop down list. You need to select the cropped volume from the small button on the right side of the master volume selection. It says specify geometry. From there select the new cropped volume and it should work.</p>
<p>I dont know if this is due to bug or is this the way it is intended to work.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5adefdd8c125b8ac28101e4e1b48aeb400199efd.png" data-download-href="/uploads/short-url/cXSJeDR92styA5WrCmmpTM5Wvfv.png?dl=1" title="Screenshot from 2020-11-05 19-48-56" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5adefdd8c125b8ac28101e4e1b48aeb400199efd_2_597x500.png" alt="Screenshot from 2020-11-05 19-48-56" data-base62-sha1="cXSJeDR92styA5WrCmmpTM5Wvfv" width="597" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5adefdd8c125b8ac28101e4e1b48aeb400199efd_2_597x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5adefdd8c125b8ac28101e4e1b48aeb400199efd_2_895x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5adefdd8c125b8ac28101e4e1b48aeb400199efd.png 2x" data-dominant-color="ECF0F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-11-05 19-48-56</span><span class="informations">904×757 44.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #24 by @Hamid (2020-11-07 20:43 UTC)

<p>Manjula I can not thank you enough.<br>
It works now.The problem was the way clicking on drop down menu instead of specify geometry.<br>
Many thanks to you.</p>

---

## Post #25 by @Hamid (2020-11-12 00:27 UTC)

<p>Does anybody know how to extract the ‘flow data’ from the CT-scan images?<br>
I have bunch of CT-images of the Heart and I’m looking for the flow rate of the blood.</p>

---

## Post #26 by @lassoan (2020-11-12 01:03 UTC)

<p>If all you have is the dynamic CT then you need to compute the flow information. Fortunately, Slicer already has all the necessary infrastructure to do this - you just need to write a Python script to connect all the pieces.</p>
<p>You can extract centerline using SlicerVMTK extension, estimate bolus arrival time at each centerline position by analyzing image intensity change in time, and compute all the metrics. In recent Slicer Preview releases we added the option of to store custom data arrays in markups curve nodes, which you can use to store information such as such as vessel radius, transit time, flow rate,…</p>
<p>If you need to analyze moving vessels (e.g., coronaries) then you have to detect vessels in each frame or suppress motion using SequenceRegistration extension.</p>

---

## Post #27 by @lassoan (2020-11-12 19:09 UTC)

<p>A post was split to a new topic: <a href="/t/how-to-hide-cropping-region-box-and-label-cube/14572">How to hide cropping region box and label cube</a></p>

---

## Post #28 by @lassoan (2020-12-11 14:51 UTC)

<p>2 posts were split to a new topic: <a href="/t/display-vertical-ruler/15005">Display vertical ruler</a></p>

---

## Post #29 by @lassoan (2021-04-26 21:22 UTC)

<p>A post was split to a new topic: <a href="/t/merge-cad-file-with-segmentation/17338">Merge CAD file with segmentation</a></p>

---

## Post #30 by @lassoan (2021-05-11 04:55 UTC)

<p>2 posts were split to a new topic: <a href="/t/how-to-edit-an-stl-file-using-segment-editor/17559">How to edit an STL file using Segment Editor</a></p>

---
