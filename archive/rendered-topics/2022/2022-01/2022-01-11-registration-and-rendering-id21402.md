# Registration and rendering

**Topic ID**: 21402
**Date**: 2022-01-11
**URL**: https://discourse.slicer.org/t/registration-and-rendering/21402

---

## Post #1 by @sandigeeup (2022-01-11 05:01 UTC)

<p>Data registration do I do the direct rendering and segmentations of MRI, CT and PET scans, prior to registration or after?</p>
<div class="youtube-onebox lazy-video-container" data-video-id="9iiOBmaP8bA" data-video-title='Airway segmentation in 3D Slicer with "Grow from Seeds"' data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=9iiOBmaP8bA" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/9iiOBmaP8bA/maxresdefault.jpg" title='Airway segmentation in 3D Slicer with "Grow from Seeds"' width="" height="">
  </a>
</div>


---

## Post #2 by @mikebind (2022-01-11 16:11 UTC)

<p>Rendering is a visualization method.  Depending on how you are doing the segmentations, it may or may not matter whether you do registrations before or after segmentation. The simplest and most foolproof method would likely be to do registrations first and then segment and visualize the registered images.</p>

---

## Post #3 by @sandigeeup (2022-01-11 16:43 UTC)

<p>Thanks, Mike, I appreciate your advice :). Also which method of registration do you recommend is best for these data sets? I am doing this for an MSc project, so want them to align as good as is possible. Thank you so much, Sandie</p>

---

## Post #4 by @mikebind (2022-01-11 17:22 UTC)

<p>Are the PET and CT images already aligned (e.g. from a PET/CT scanner)?  If so, then all you need to establish is registration with the MRI.  I would try the Elastix registration module (which you may need to install first using the Extensions manager, find the extension named “SlicerElastix”) with the “generic rigid (all)” preset, with the CT image as the “fixed” volume and the MRI as the “moving” volume.  You can evaluate how well this worked by setting one volume as the foreground image and another as the background image and fade between them to see whether they are well aligned. If so, great!  If not, then you will either need to try other automated or manual registration approaches or try changing parameters for the Elastix registration.</p>
<p>If your PET is not aligned to the CT, then you will also need to register it. I don’t have experience doing that (all our PET imaging has associated CT’s for attenuation correction), but I have seen examples so I know it is sometimes done.</p>

---

## Post #5 by @sandigeeup (2022-01-11 21:14 UTC)

<p>Hi Mike, So I used landmark registration to register the CT and MRI data, onto the CT scans used transformation matrix to align the CT scan data with the MRI (MRI as the fixed point) and it worked ok. I tried to use a checkerboard to check the alignment but 50% of the boxes were black so could not see both sets of scans, so I guess I’ll hope for the best, I may go back and try the MITK, but not at this point. now I need to add the Pet so fingers crossed. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"> Sandie</p>

---

## Post #6 by @mikebind (2022-01-11 21:25 UTC)

<p>Landmark registration is a reasonable approach.</p>
<p>I find fading between the two volumes which should be registered to be the most effective way to evaluate registration quality (better than checkerboard, see discussion <a href="https://discourse.slicer.org/t/checkerboard-for-registered-mri-and-ct-of-hip-bone/18768">here</a> for another alternative approach).  You can achieve this in Slicer by selecting one volume as the background volume and the other as the foreground volume, and then use the foreground opacity slider to fade the foreground volume in and out.  See <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view" class="inline-onebox">User Interface — 3D Slicer documentation</a> for the controls.  If you link the slice views (the linked/unlinked rings), then the foreground and background selections and foreground opacity will all be linked across the slice views, and you can view the fading in the other slices without the slice controls getting in the way.</p>

---

## Post #7 by @sandigeeup (2022-01-12 21:38 UTC)

<p>Hi Mike, I have finally registered the CT with the MRI (Land Mark reg) and the Pet scan and MRI (Expert automatic reg, with a preset transformation matrix) I now need to combine them all together…eek! I didn’t know they could be done, do I need to register them together is this something you have done? I need to have this done by tomorrow and then render them (individually to then put together). I hope this all makes sense!!!</p>

---

## Post #8 by @mikebind (2022-01-13 19:30 UTC)

<p><a class="mention" href="/u/sandigeeup">@sandigeeup</a>, if you have registered the CT (moving) to the MRI (fixed) and the PET scan (moving) to the same MRI (fixed), then all three images should be registered in the same 3D space (the space the MRI is defined in), and volume rendering should show them there.  Are you having problems with that visualization?</p>

---

## Post #9 by @sandigeeup (2022-01-13 20:27 UTC)

<p>Right now I feel like I don’t know my arse from my elbow. Does this look right, the joined data sets are in the top left?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da497e58640108680c344607e717cc16b7d11b00.jpeg" alt="Picture1" data-base62-sha1="v93xXu82Ud8Fi0R4hVjpwlUueGI" width="602" height="359"></p>

---

## Post #10 by @mikebind (2022-01-14 20:31 UTC)

<p>I’m not sure what the goal is, what do you mean by “joined data sets”?  Are you trying to combine all three image volumes into a single image volume?  If so, why?  A common goal might be to segment some structure (a tumor perhaps) on one type of imaging where it is conspicuous, and then view that segmentation over a different image type to see exactly where that structure is in that other image.  Does that correspond to what you are trying to do?</p>

---

## Post #11 by @sandigeeup (2022-01-15 11:37 UTC)

<p>Yes, that’s exactly it. I think I was overthinking it. As this is for a Master project and the direction was a bit confusing, I have worked it out and it is all good from that point now. Thanks so much for your help!! Sandie</p>

---
