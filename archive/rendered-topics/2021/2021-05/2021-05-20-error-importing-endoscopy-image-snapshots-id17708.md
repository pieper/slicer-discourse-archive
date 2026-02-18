# Error importing endoscopy image snapshots

**Topic ID**: 17708
**Date**: 2021-05-20
**URL**: https://discourse.slicer.org/t/error-importing-endoscopy-image-snapshots/17708

---

## Post #1 by @caesarsalad (2021-05-20 12:03 UTC)

<p>Hi everyone,</p>
<p>I’m very new to 3d Slicer, started using it just two days ago.<br>
I have an issue that I don’t know why is going on.</p>
<p>When I try loading my set of .dcm files, it gives me the error message:</p>
<p>“[Scalar Volume]: Multi-frame image. If slice orientation or spacing is non-uniform then the image may be displayed incorrectly. Use with caution.<br>
Reference image in series does not contain geometry information. Please use caution.”</p>
<p>Which, if I disregard, follows up with the error:</p>
<p>“Could not load: 1: Image file as a Scalar Volume”</p>
<p>I’m quite lost as to why this is, and further if I somehow get the file to load it appears as such:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd40244ea37bf02eb15d6e8867c4bb88f9c03199.jpeg" data-download-href="/uploads/short-url/thJiT8XnNdvd7pAAz55mMOVGSjD.jpeg?dl=1" title="Screen Shot 2021-05-20 at 3.45.21 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cd40244ea37bf02eb15d6e8867c4bb88f9c03199_2_690x431.jpeg" alt="Screen Shot 2021-05-20 at 3.45.21 PM" data-base62-sha1="thJiT8XnNdvd7pAAz55mMOVGSjD" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cd40244ea37bf02eb15d6e8867c4bb88f9c03199_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cd40244ea37bf02eb15d6e8867c4bb88f9c03199_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cd40244ea37bf02eb15d6e8867c4bb88f9c03199_2_1380x862.jpeg 2x" data-dominant-color="989498"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-05-20 at 3.45.21 PM</span><span class="informations">2880×1800 720 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Compared to other sample data it does seem like it’s a bit off because the frequency at which the photos were taken is wasn’t quick enough (?)<br>
What I want to do is go through the .dcm images and if identify any signs of malignant tumours as I go, more leaning towards 2D. Would I need to fix my file format?</p>
<p>Sorry if it’s a dumb question, I’m just trying to learn how to use it and see if it can be any help.</p>

---

## Post #2 by @lassoan (2021-05-20 12:27 UTC)

<p>It would be probably more appropriate to load these images as a sequence of single-slice image volumes (and replay it using Sequences module) - similarly to how we segment ultrasound images. We have developed a couple of modules for such image sequence labeling, training data generation, and real-time segmentation with a trained model. <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> could you help <a class="mention" href="/u/caesarsalad">@caesarsalad</a> with relevant SlicerAIGT modules?</p>
<p>Could you share an example data set with us so that we can make sure it can be imported as an image sequence (instead of a single 3D image volume)?</p>

---

## Post #3 by @caesarsalad (2021-05-20 12:40 UTC)

<p>Hello,</p>
<p>Thanks a lot for your reply, I really appreciate your time.<br>
I’d like to share a data set, I’ve tried compressing the image set into a zip file but the platform doesn’t support the extension – is there an alternative to share the image set?</p>
<p>Again thanks a lot for your time.</p>

---

## Post #4 by @lassoan (2021-05-20 12:44 UTC)

<p>You can upload it anywhere (dropbox, onedrive, googledrive, …) and post the link here.</p>

---

## Post #5 by @caesarsalad (2021-05-20 12:50 UTC)

<p><em>(link removed as it might contain patient information)</em></p>
<p>Here’s the link to the sample data zip file’s google drive. I’ve double checked that it’s public but if you can’t access it please let me know.</p>
<p>Thanks!!</p>

---

## Post #6 by @lassoan (2021-05-20 17:04 UTC)

<p>I’ve updated the DICOM image sequence importer to allow loading endoscopy secondary capture images. DICOM module of Slicer Preview Release that you download tomorrow (or later) will be able to load the endoscopy images. Since each image comes with a different instance number, each image will show up as a separate volume in Slicer. If you want to put them into one sequence then you can do that using the Sequences module.</p>

---
