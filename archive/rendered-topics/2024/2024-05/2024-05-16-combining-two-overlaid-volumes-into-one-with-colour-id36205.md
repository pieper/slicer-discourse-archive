---
topic_id: 36205
title: "Combining Two Overlaid Volumes Into One With Colour"
date: 2024-05-16
url: https://discourse.slicer.org/t/36205
---

# Combining two overlaid volumes into one (with colour)

**Topic ID**: 36205
**Date**: 2024-05-16
**URL**: https://discourse.slicer.org/t/combining-two-overlaid-volumes-into-one-with-colour/36205

---

## Post #1 by @hannaho (2024-05-16 12:32 UTC)

<p>Hi all,</p>
<p>I am trying to add ‘hotspots’ from a DW MRI image over top of a CT image. The goal is to have something that looks like a classic PET-CT image, with anatomical data from CT in greyscale with ‘functional’ info from the MRI in colour on top. I have been able to get something that looks like what I want by doing manual registration and overlaying the CT and MRI images in the viewer. That looks like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/59de8b343b0780867b5f3b2f65826ba9dd32d395.png" data-download-href="/uploads/short-url/cP1i95ZXASzGPL7oelnxJDnrf7L.png?dl=1" title="Screenshot 2024-05-16 at 12.32.38" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59de8b343b0780867b5f3b2f65826ba9dd32d395_2_456x500.png" alt="Screenshot 2024-05-16 at 12.32.38" data-base62-sha1="cP1i95ZXASzGPL7oelnxJDnrf7L" width="456" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59de8b343b0780867b5f3b2f65826ba9dd32d395_2_456x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59de8b343b0780867b5f3b2f65826ba9dd32d395_2_684x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/59de8b343b0780867b5f3b2f65826ba9dd32d395.png 2x" data-dominant-color="4F4D57"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-05-16 at 12.32.38</span><span class="informations">767×840 263 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, I haven’t found a way to make this into one volume. Registration does something very weird to the image!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/463bc347508d6c0e7aa377f2f9d7b73680b10086.png" data-download-href="/uploads/short-url/a1jsMd4yU1wK0u9cyIIU3WVhUxw.png?dl=1" title="Screenshot 2024-05-16 at 12.35.59" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/463bc347508d6c0e7aa377f2f9d7b73680b10086_2_690x415.png" alt="Screenshot 2024-05-16 at 12.35.59" data-base62-sha1="a1jsMd4yU1wK0u9cyIIU3WVhUxw" width="690" height="415" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/463bc347508d6c0e7aa377f2f9d7b73680b10086_2_690x415.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/463bc347508d6c0e7aa377f2f9d7b73680b10086_2_1035x622.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/463bc347508d6c0e7aa377f2f9d7b73680b10086_2_1380x830.png 2x" data-dominant-color="3B3B3F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-05-16 at 12.35.59</span><span class="informations">1431×861 165 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And a scalar addition doesn’t preserve the colour. Plus, even with intensity filtering the MRI data isn’t coming up well.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/6571613840d9f5f15bec3efa5ce0e429e3427e52.jpeg" data-download-href="/uploads/short-url/etp8EostBsiA5lKkkz4vY0DHeiC.jpeg?dl=1" title="Screenshot 2024-05-16 at 12.36.26" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/6571613840d9f5f15bec3efa5ce0e429e3427e52_2_690x412.jpeg" alt="Screenshot 2024-05-16 at 12.36.26" data-base62-sha1="etp8EostBsiA5lKkkz4vY0DHeiC" width="690" height="412" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/6571613840d9f5f15bec3efa5ce0e429e3427e52_2_690x412.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/6571613840d9f5f15bec3efa5ce0e429e3427e52_2_1035x618.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/6571613840d9f5f15bec3efa5ce0e429e3427e52_2_1380x824.jpeg 2x" data-dominant-color="39393D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-05-16 at 12.36.26</span><span class="informations">1433×857 180 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I would like to get one volume that looks more similar to the first image, and can be exported as a DICOM file. Is this possible? Thanks in advance!</p>

---

## Post #2 by @pieper (2024-05-16 20:50 UTC)

<p>If the MRI covers the same anatomy and has good content then registration should be robust, just <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html">follow the instructions</a>.  If the DWI scan doesn’t show the anatomy well then another series from the same study that shares the geometry could be used for the registration.</p>

---

## Post #3 by @hannaho (2024-05-19 07:39 UTC)

<p>Thanks Steve,</p>
<p>I’ve been able to follow those instructions.<br>
It’s still unclear how when using manual registration I can go from having two different overlaid files in the viewer to actually being able to export that as one DICOM file. Is that possible?</p>
<p>Is there a way to get automatic registration to preserve the colour I’ve set on the DW MRI image? These are the things I’m struggling with the most, as I’m not sure how I can essentially export this file with the visual I’d like.</p>
<p>Thanks again!</p>

---

## Post #4 by @pieper (2024-05-19 14:22 UTC)

<p>We don’t typically export these visualizations to DICOM.  What is your goal for that?</p>
<p>You can use the Screen Capture module to export to movie or image files with the overlays and colors preserved.  It could make sense to export these to DICOM secondary captures but I don’t recall that ever coming up as a requirement before.</p>

---

## Post #5 by @hannaho (2024-05-19 14:28 UTC)

<p>The goal is just to be able to share the file with colleagues who don’t have or can’t work Slicer. I will have a look at exporting them as image files and see if that suits the use.</p>
<p>Thank you <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #6 by @hannaho (2024-06-24 10:48 UTC)

<p>The solution I found was to give up on preserving the different colours. Scalar addition lets you add the high intensity regions to the background image volume. Then there is a function built in to 3D Slicer to export the image volume as a DICOM file. This file works when uploading to other viewers, such as PACS.</p>

---
