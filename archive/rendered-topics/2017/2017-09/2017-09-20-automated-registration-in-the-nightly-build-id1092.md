# Automated registration in the Nightly Build

**Topic ID**: 1092
**Date**: 2017-09-20
**URL**: https://discourse.slicer.org/t/automated-registration-in-the-nightly-build/1092

---

## Post #1 by @stevenagl12 (2017-09-20 17:04 UTC)

<p>I am trying to automatically register some volumes together but when I looked at the modules listed for the nightly build online, none of them show an automated registration module, yet the FAQ on Registration site hints that there are automated methods out there. The modules I have all seem to be semi-automated and most of them say BRAINS on them, which I am trying to register kidney regions together. Any advice or ideas?</p>

---

## Post #2 by @lassoan (2017-09-20 19:35 UTC)

<p>A post was split to a new topic: <a href="/t/get-image-slice-voxel-plane-from-position/1093">Get image slice/voxel plane from position</a></p>

---

## Post #3 by @lassoan (2017-09-20 19:11 UTC)

<p>All intensity-based registration methods in Slicer are fully automatic.</p>
<p>I like SlicerElastix (in SlicerElastix extension) the most, because it is very robust and usually does not require any parameter tuning.</p>
<p>BRAINS is just a brand name. It contains a number of general registration methods, basically all thin wrappers over standard ITK registration algorithms. It’s been successfully used on many organs and imaging modalities, but it usually requires parameter tuning. The <a href="https://www.slicer.org/wiki/Documentation/Nightly/Registration/RegistrationLibrary">Registration case library</a> is a good starting point.</p>

---

## Post #4 by @lassoan (2017-09-20 19:35 UTC)

<p>A post was merged into an existing topic: <a href="/t/get-image-slice-voxel-plane-from-position/1093">Get image slice/voxel plane from position</a></p>

---

## Post #5 by @stevenagl12 (2017-09-25 14:12 UTC)

<p>I have volumes that I have segmented. I then registered them, is there a way to transfer the segmentations to the new registered volume matrices?</p>

---

## Post #6 by @lassoan (2017-09-25 14:21 UTC)

<p>Yes. Apply the same transform to the segmentation node that was used to transform the volume.</p>

---

## Post #7 by @stevenagl12 (2017-09-26 17:12 UTC)

<p>Alright thank you very much.</p>

---

## Post #8 by @stevenagl12 (2017-10-03 18:47 UTC)

<p>Is there a method by which to use the Elastix registration module to batch process multiple volume registrations? With regards to this, when registering 2 volumes, the fixed volume does not appear to be zero-padded if the registration transformation ends up pulling the volume image outside of the dimensions of the fixed volume so that all image dimensions can be equalized in the end. Is there a way to do this in Elastix or some other registration module?</p>

---

## Post #9 by @stevenagl12 (2017-10-03 19:00 UTC)

<p>What I mean by this is that I am essentially trying to register multiple images to each other at the same time so that if image A is smaller than image C, but not B, then A is zero-padded and image B is re-registered after image C automatically so that in the end all images have the same dimensions?</p>

---

## Post #10 by @lassoan (2017-10-03 19:22 UTC)

<p>You can have a look at how <a href="https://github.com/moselhy/SlicerSequenceRegistration">Sequence registration extension</a> is implemented. It registers a sequence of images to each other.</p>

---

## Post #11 by @stevenagl12 (2017-10-04 14:29 UTC)

<p>How would I go about converting a series of cropped volumes into a sequence without exporting all the volumes to dicom files and reloading them in? Also, according to the documentation for this extension, you are still registering the sequence to a single volume. Is that going to allow that volume to be changed as well as the 4D sequence of dicoms? Finally, judging by the description, this method of registration uses 4D data where the 4th dimension is time, so intra-patient registration. Will this still work if it is inter-patient and the registration methods have to be robust enough to handle the vast variation?</p>

---

## Post #12 by @stevenagl12 (2017-10-04 15:50 UTC)

<p>So I figured out how to create a sequence, but I don’t know how to visualize it to determine if the registration has worked or not, or how to split that sequence apart again as the sequences module only has add or delete options for the sequences. I’ve tried the sequence browser but it doesn’t visualize my sequence and it doesn’t give me the option of going through the slices like normal between each volume in the sequence. The sequences don’t show up in the data subject hierarchy either.</p>

---

## Post #13 by @lassoan (2017-10-04 16:06 UTC)

<aside class="quote no-group" data-username="stevenagl12" data-post="11" data-topic="1092" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stevenagl12/48/3391_2.png" class="avatar"> stevenagl12:</div>
<blockquote>
<p>Also, according to the documentation for this extension, you are still registering the sequence to a single volume. Is that going to allow that volume to be changed as well as the 4D sequence of dicoms?</p>
</blockquote>
</aside>
<p>Yes.</p>
<aside class="quote no-group" data-username="stevenagl12" data-post="11" data-topic="1092" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stevenagl12/48/3391_2.png" class="avatar"> stevenagl12:</div>
<blockquote>
<p>this method of registration uses 4D data where the 4th dimension is time, so intra-patient registration. Will this still work if it is inter-patient and the registration methods have to be robust enough to handle the vast variation?</p>
</blockquote>
</aside>
<p>The less variation between the images, the higher the success rate and accuracy is, but - thanks to the robustness of Elastix, it should not be a problem to register images of different patients, even if different imaging modality is used. If registration is not successful then you have to tune the registration parameters.</p>

---

## Post #14 by @lassoan (2017-10-04 16:12 UTC)

<aside class="quote no-group" data-username="stevenagl12" data-post="12" data-topic="1092" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stevenagl12/48/3391_2.png" class="avatar"> stevenagl12:</div>
<blockquote>
<p>I don’t know how to visualize it to determine if the registration has worked or not, or how to split that sequence apart again as the sequences module only has add or delete options for the sequences.</p>
</blockquote>
</aside>
<p>If you use Sequence registration, it puts the result in a volume sequence that you can review using the existing browser node. Just choose to show the registration result volume in the slice views. You can show original volume in the foreground and registered volume in the background and fade between them.</p>
<aside class="quote no-group" data-username="stevenagl12" data-post="12" data-topic="1092" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stevenagl12/48/3391_2.png" class="avatar"> stevenagl12:</div>
<blockquote>
<p>I’ve tried the sequence browser but it doesn’t visualize my sequence and it doesn’t give me the option of going through the slices like normal between each volume in the sequence. The sequences don’t show up in the data subject hierarchy either.</p>
</blockquote>
</aside>
<p>Volume sequence nodes don’t show up in the <code>Subject hierarchy</code> tab (they only show up in the <code>All nodes</code> tab). You need to add the volume sequence node to a browser node; it will create a proxy node (that makes the selected item of the sequence appear in the scene). Note that you can create multiple browser nodes, each exposing one item of the sequence in the scene.</p>

---

## Post #15 by @stevenagl12 (2017-10-04 16:22 UTC)

<p>And how do you split up a sequence once it’s created?</p>

---

## Post #16 by @stevenagl12 (2017-10-04 16:25 UTC)

<p>Also, this error keeps appearing every time I run the sequence registration: AttributeError: ‘NoneType’ object has no attribute ‘SetOverwriteProxyName’</p>

---

## Post #17 by @stevenagl12 (2017-10-04 16:28 UTC)

<p>This is what I meant by the sequence isn’t playing on the sequence browser:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b0ae52ad16d314ddcea868140686ba3eb1e47f5.png" data-download-href="/uploads/short-url/3ReexwsOHYSSRACxiui4zdFatSd.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b0ae52ad16d314ddcea868140686ba3eb1e47f5_2_690x373.png" alt="image" data-base62-sha1="3ReexwsOHYSSRACxiui4zdFatSd" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b0ae52ad16d314ddcea868140686ba3eb1e47f5_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b0ae52ad16d314ddcea868140686ba3eb1e47f5_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b0ae52ad16d314ddcea868140686ba3eb1e47f5_2_1380x746.png 2x" data-dominant-color="232223"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 60.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #18 by @lassoan (2017-10-04 18:31 UTC)

<aside class="quote no-group" data-username="stevenagl12" data-post="15" data-topic="1092" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stevenagl12/48/3391_2.png" class="avatar"> stevenagl12:</div>
<blockquote>
<p>And how do you split up a sequence once it’s created?</p>
</blockquote>
</aside>
<p>You can retrieve any item from the sequence node and create a clone of that in the scene. However, typically you don’t need to do this, as this is exactly what the browser node does. You just create as many browser nodes as many items of the sequence you want to see in the scene at the same time. Usually it is enough to add two sequence nodes, which allows you to compare any two items of the sequence.</p>

---

## Post #19 by @lassoan (2017-10-04 18:33 UTC)

<aside class="quote no-group" data-username="stevenagl12" data-post="17" data-topic="1092">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stevenagl12/48/3391_2.png" class="avatar"> stevenagl12:</div>
<blockquote>
<p>This is what I meant by the sequence isn’t playing on the sequence browser:</p>
</blockquote>
</aside>
<p>You need to choose “OutputVolumes” as background volume in your slice view (and click FOV reset to make sure the slice view is positioned over the volume).</p>

---

## Post #20 by @lassoan (2017-10-04 18:34 UTC)

<aside class="quote no-group" data-username="stevenagl12" data-post="16" data-topic="1092" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stevenagl12/48/3391_2.png" class="avatar"> stevenagl12:</div>
<blockquote>
<p>Also, this error keeps appearing every time I run the sequence registration: AttributeError: ‘NoneType’ object has no attribute ‘SetOverwriteProxyName’</p>
</blockquote>
</aside>
<p>If you would like us to investigate this then please provide the full application log (menu: Help / Report a bug).</p>

---

## Post #21 by @stevenagl12 (2017-10-04 19:11 UTC)

<p>Just to clarify, does this mean that the browser node splits the sequence back into volumes (or transforms as in the case of the registration) so that I can do things like export those volumes or apply the individual transforms to other segmentations and volumes, or would I have to clone the scene? As for cloning the scene, does that separate the volume?</p>

---

## Post #22 by @lassoan (2017-10-04 19:22 UTC)

<p>Each browser node can take one item (corresponding to one time point, one patient, …) from a sequence and copies it into the scene.</p>
<p>When you save a volume sequence to file then it may be either saved as a 4D image (if all 3D volumes in the sequence has the same size, geometry, etc) or as a .mrb file (a zip file containing individual volumes).</p>
<p>To force save a volume sequence as .mrb (so that you can unzip it to have each volume in a separate file), you can set the storage node explicitly:</p>
<pre><code># remove current storage node
slicer.mrmlScene.RemoveNode(s.GetStorageNode())
# create and set storage node that writes sequence in .mrb file
s.SetAndObserveStorageNodeID(slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSequenceStorageNode').GetID())
</code></pre>
<p>ITK, VTK can read 4D nrrd volumes natively, so there should be no need for dealing with individual 3D files (if they have the same geometry). We even created a <a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/nrrdread.m">nrrd file reader</a>/writer for Matlab that can deal with 4D volumes (used in MatlabBridge).</p>

---

## Post #23 by @stevenagl12 (2017-10-09 19:12 UTC)

<p>Here is the error log when I ran the sequence registration:</p>
<p><a href="https://drive.google.com/file/d/0B7remrTspnWab0J0eEZuM1dyZTA/view?usp=sharing" class="onebox" target="_blank" rel="nofollow noopener">https://drive.google.com/file/d/0B7remrTspnWab0J0eEZuM1dyZTA/view?usp=sharing</a></p>

---

## Post #24 by @lassoan (2017-10-11 04:33 UTC)

<p>Thanks for the logs. If you go to Volumes module and select the OutputVolumes proxy volume node as <code>Active volume</code>, in Information section, what are <code>Image Dimensions</code> values? In the slice view controller, what background and foreground volume is selected? Did you see the input volume playing before you run the registration?</p>

---

## Post #25 by @stevenagl12 (2017-10-13 17:55 UTC)

<p>As I registered two sequences, I’ll give you both dimensions: 74 X 77 X 117 and 89 X 66 X 122. The foreground by default was always None, and the Background was the registered volume when I went to the Sequence Browser. I checked the sequence input volume before I rant the registration and there was nothing wrong with it as far as I know. While I was registering the sequences (at start) I had the sequence of the input volume displayed on a particular portion. During the registration process it switched over to show particular registered volume images until the end when it stopped at the first volume in the registered sequence. The registration for the volume with the 74 X 77 X 117 is really bad though, and that was the sequence that kept giving me the error. The registered volume has extreme distortion where the image is pulled far off the registered image space. Also, by the appearance of both of my registered sequences, it looks as if the sequence registration just registered all of the volumes to the first volume in the sequence, as that is the only volume that wasn’t distorted. I’m trying to get the registration to register all of the images together so that even the first volume is zero-padded based off from whether it is or isn’t the largest volume in the sequence. Is there an easy method to do this?</p>

---

## Post #26 by @lassoan (2017-10-13 21:21 UTC)

<p>I couldn’t really follow what you described, but if registration result was incorrectly distorted then probably you need to step back and figure out how to register just two frames to each other. Once that works reliably, you can move on to register a complete sequence.</p>
<p>In sequence registration all frames are registered to one frame, which might be the first frame by default but in general the beat is to choose a frame from near the middle of the sequence.</p>

---
