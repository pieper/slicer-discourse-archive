---
topic_id: 10693
title: "Using Reflective Sphere Center To Register Bone Model With O"
date: 2020-03-15
url: https://discourse.slicer.org/t/10693
---

# Using reflective sphere center to register bone model with Optitrack pre-recorded data

**Topic ID**: 10693
**Date**: 2020-03-15
**URL**: https://discourse.slicer.org/t/using-reflective-sphere-center-to-register-bone-model-with-optitrack-pre-recorded-data/10693

---

## Post #1 by @GL1984 (2020-03-15 13:36 UTC)

<p>Hello,<br>
I have gathered 3D tracking data a while back on anatomical samples using optitrack. Essentially, we tracked the motions of Skull, C1, C2 using reflecting spheres attached to plastic poles fixed to the bone. CT images of the samples including bone + spheres were collected.<br>
I have used the neuronavigation modules in 3D slicer and my understanding is that registration of bones is done by using a pointer on pre-established landmarks. My question is the following:<br>
Could I use the coordinates of the spheres (provided by Optitrack) to register each bone in 3D slicer?<br>
I can easily locate the center of each sphere in 3D slicer so I don’t see a theoretical problem to do that but I can’t figure out how to in the available modules. I can provide models and optitrack raw data if that helps…<br>
The goal would be to generate 3D animation of the bones moving with respect to each other ideally using C2 as reference coordinate system.<br>
Any help much appreciated,<br>
Guillaume</p>

---

## Post #2 by @pieper (2020-03-15 17:24 UTC)

<p>Sounds quite doable - these were just bones, right (not a living person?).  Did you have three or more spheres per bone?  Probably some screenshots would help clarify.</p>
<p>In any case as long as you have the tracked position and orientation you can convert that into a sequence to transforms (use the Sequences extension).  Then segment the CT with the markers and figure out the transform from tracker space to CT space, e.g. using the centroids of the segmented spheres.</p>

---

## Post #3 by @ungi (2020-03-15 21:53 UTC)

<p>If there is any chance to repeat the motion experiment (you still have the bone with markers and the OptiTrack available), then it would be much easier to use PLUS (<a href="http://www.PlusToolkit.org" rel="nofollow noopener">www.PlusToolkit.org</a>) and OpenIGTLink to make a real time connection between the tracker and Slicer. That way, you could pre-register the bones, so you would see motions accurately in real time in Slicer as they move in the physical world. And you could use Slicer’s Sequences extension to record/replay time series motion data. There are lots of useful tutorials on <a href="http://www.SlicerIGT.org" rel="nofollow noopener">www.SlicerIGT.org</a> for such experiments.</p>
<p>If this is not possible for some reason, then as Steve said, you can probably write code to convert OptiTrack recorded trajectories to sequence metafiles and import them in Slicer as sequences.</p>

---

## Post #4 by @GL1984 (2020-03-15 22:17 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b885ff90da86c454b22cd2a10ff9740d38270932.jpeg" data-download-href="/uploads/short-url/qkmWz3OGSjyJFpFEmuimvkzV6ee.jpeg?dl=1" title="Screen Shot 2020-03-15 at 18.24.36" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b885ff90da86c454b22cd2a10ff9740d38270932_2_690x387.jpeg" alt="Screen Shot 2020-03-15 at 18.24.36" data-base62-sha1="qkmWz3OGSjyJFpFEmuimvkzV6ee" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b885ff90da86c454b22cd2a10ff9740d38270932_2_690x387.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b885ff90da86c454b22cd2a10ff9740d38270932_2_1035x580.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b885ff90da86c454b22cd2a10ff9740d38270932_2_1380x774.jpeg 2x" data-dominant-color="413F38"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-03-15 at 18.24.36</span><span class="informations">4088×2296 752 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Hi,<br>
Thanks you both for the quick reply.</p>
<p>Steve,<br>
Yes, these were bones from dog cadavers actually. I had 4 spheres per bone (see screenshot of the scene attached, the plastic poles are not showing because I cut them out of the segments for animation purposes).<br>
I think I have only used the sequence module for the online tutorials… I am not sure what a sequence to transform is? How would I go about figuring out the transform? And if I figure it out at one point in time, will it be then tracking the rest of the data over time?</p>
<p>Tamas,<br>
I realise your method would have been the best one. I was not familiar with 3D Slicer IGT capacity at the time that data was collected unfortunately. The samples are long gone I am afraid.<br>
However, I would have thought I should be able to replay the raw data from Optitrack no? If I replayed it on Optitrack, could I then use PLUS toolkit to stream that data to Slicer? Or does it only work on live data?<br>
Assuming that part works, I am back to my problem of registering the models based on sphere location because that would be the only points I have knowledge about in the “physical world” using the tracker coordinate system… Any ideas if these points could be used within the registration modules somehow?</p>
<p>It would actually be nice to be able to do the same thing for neuronavigation. If we could use spheres directly as registration points, we could potentially skip registration step using pointer and landmarks for some applications.</p>
<p>Thanks again…<br>
3D Slicer is a great piece of software, I wish I had known more about it a few years back.</p>

---

## Post #5 by @lassoan (2020-03-15 23:15 UTC)

<p>Have you recorded just individual sphere positions, or you created a marker from the set of spheres that were attached to each rigid body?</p>
<p>If you created markers and recorded marker positions then you can convert the recorded file to <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/FileSequenceFile.html">sequence file format</a> the Slicer can directly load and replay (it is a simple text file format, so it should be straightforward to create it).</p>
<p>You can determine transformation between two coordinate systems from a set of matching landmark positions using Fiducial registration wizard module (see <a href="http://www.slicerigt.org/wp/user-tutorial/">SlicerIGT Landmark registration tutorial</a>). One set of points you can obtain from the image (marking points in the image), you may get the other set of point positions from the Optitrack recording.</p>

---

## Post #6 by @GL1984 (2020-03-16 19:27 UTC)

<p>Thanks,<br>
I will have to go back to my data. I am having issues with the computer running motive at the moment so I will do when that issue s fixed.<br>
The files have been saved in .c3d but I am not sure what is within them. I presume I would have to convert to something else to use the data.<br>
Will need to do some reading and testing… Will let you all know once I understand a bit better the suggested options.</p>

---
