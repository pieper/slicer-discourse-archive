---
topic_id: 19615
title: "Import Position Data Tracking For Images"
date: 2021-09-10
url: https://discourse.slicer.org/t/19615
---

# Import position data (tracking) for images

**Topic ID**: 19615
**Date**: 2021-09-10
**URL**: https://discourse.slicer.org/t/import-position-data-tracking-for-images/19615

---

## Post #1 by @megt (2021-09-10 18:54 UTC)

<p>Hi everybody,</p>
<p>I am Matthieu working on a 3D free-hand project involving ultrasound imaging and electromagnetic device.  I am interested to use 3D Slicer for volume visualization instead of Matlab. I am also thinking that the toolbox SlicerIGT can be the solution to generate a volume of my acquisition data without using Matlab however I do not know/did not find the way to do it.</p>
<p>I am using a research scanner (Verasonics Vantage system) acquiring at a high frame rate (100 Hz) where we save all the frames and later on generate a dataset, see above an image of our dataset:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/949d3ab606d005a80cd5e4d4ea67c0d2c4c6a41d.jpeg" data-download-href="/uploads/short-url/lcHwJnpEuRUpgMW99oL4QcfSTPD.jpeg?dl=1" title="3D_Slicer_Question_V02" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/949d3ab606d005a80cd5e4d4ea67c0d2c4c6a41d_2_690x388.jpeg" alt="3D_Slicer_Question_V02" data-base62-sha1="lcHwJnpEuRUpgMW99oL4QcfSTPD" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/949d3ab606d005a80cd5e4d4ea67c0d2c4c6a41d_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/949d3ab606d005a80cd5e4d4ea67c0d2c4c6a41d_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/949d3ab606d005a80cd5e4d4ea67c0d2c4c6a41d.jpeg 2x" data-dominant-color="C8C8C8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3D_Slicer_Question_V02</span><span class="informations">1280×720 77.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>During the acquisition, we also save the position of the probe using a Polhemus electromagnetic device at 240 Hz. All positions are saved in a text file (see above) with [Source number / Tracker number / Frame number / 00 / Time Stamp / X / Y / Z / Azimuthal / Elevation / Rho] :<br>
1   1  000000004  00  1625573624860503     15.113   -6.832     7.757      10.525  -49.260   65.391<br>
1   2  000000004  00  1625573624860503     12.144    10.723    8.686     -50.461  -0.218    30.956<br>
1   1  000000005  00  1625573624864646     15.113   -6.832     7.757      10.524  -49.260   65.392<br>
1   2  000000005  00  1625573624864646     12.144    10.723    8.686     -50.461  -0.218    30.956</p>
<p>We use Matlab and some of our script to register all the frames with the tracking position and generate a volume:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c43e6e991c98164a25bed9d23a5c5e58d1331211.jpeg" data-download-href="/uploads/short-url/s03ll701fPOmIIjRRAB1sDbhRip.jpeg?dl=1" title="3D_Slicer_Question_V01" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c43e6e991c98164a25bed9d23a5c5e58d1331211_2_690x372.jpeg" alt="3D_Slicer_Question_V01" data-base62-sha1="s03ll701fPOmIIjRRAB1sDbhRip" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c43e6e991c98164a25bed9d23a5c5e58d1331211_2_690x372.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c43e6e991c98164a25bed9d23a5c5e58d1331211_2_1035x558.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c43e6e991c98164a25bed9d23a5c5e58d1331211_2_1380x744.jpeg 2x" data-dominant-color="A2CCBB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3D_Slicer_Question_V01</span><span class="informations">1920×1036 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>But Matlab is not really great for 3D Visualization, so we export our volume from Matlab as a lot of images and import them in 3D Slicer where we also do some segmentation<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a4c2193ba2dd213e02a21b95b20e3c356cd8206c.jpeg" data-download-href="/uploads/short-url/nvw9SMN7yfGHN0mvZvTo8t7S7da.jpeg?dl=1" title="3D_Slicer_Question_V03" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a4c2193ba2dd213e02a21b95b20e3c356cd8206c_2_597x500.jpeg" alt="3D_Slicer_Question_V03" data-base62-sha1="nvw9SMN7yfGHN0mvZvTo8t7S7da" width="597" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a4c2193ba2dd213e02a21b95b20e3c356cd8206c_2_597x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a4c2193ba2dd213e02a21b95b20e3c356cd8206c_2_895x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a4c2193ba2dd213e02a21b95b20e3c356cd8206c_2_1194x1000.jpeg 2x" data-dominant-color="5B5B73"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3D_Slicer_Question_V03</span><span class="informations">1312×1098 71.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>It works well but I would like to avoid passing by Matlab to generate the volume and directly generate it using Slicer3D.</p>
<p>I saw that SlicerIGT allow the streaming of video and trackers position in real time of certain equipment. However, in our case we do not want to do it in real-time but only as post-process. Is it possible to do it? I have checked about it but did not find anything.<br>
I have also checked in 3DSlicer if it is possible to import our tracking position but either, I did not find anything.<br>
If there is no such solution, do you know which format file I can use to provide a tracking position for each of our images and then provide them to 3DSlicer? I am also happy to do this way in order to generate a volume.</p>
<p>Thank you for your advice.</p>

---

## Post #2 by @lassoan (2021-09-10 23:54 UTC)

<p>If you want to keep Matlab for data acquisition then all you need to do is to <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/FileSequenceFile.html">save the image and tracking data in sequence nrrd/mha file format</a>. You can then load that into Slicer and reconstruct the volume using the Volume Reconstructor module, similarly to this:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="l0BcW8c9CnI" data-video-title="Tracked ultrasound AI segmentation and 3D reconstruction tutorial" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=l0BcW8c9CnI" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/l0BcW8c9CnI/maxresdefault.jpg" title="Tracked ultrasound AI segmentation and 3D reconstruction tutorial" width="" height="">
  </a>
</div>

<p>If you want to do real-time acquisition in Slicer then you need to set up an OpenIGTLink connection. We usually use Plus toolkit for this, but that does not support Verasonics ultrasound and Polhemus tracker, so instead you can keep using your Matlab code for acquiring the tracked image data and send the tracked image data to Slicer using by using <a href="https://pypi.org/project/pyigtl/">pyigtl</a>.</p>

---

## Post #3 by @megt (2021-09-12 15:56 UTC)

<p>Hi Andras,</p>
<p>Thank you for your reply.</p>
<p>I will have a look to save my dataset to the nrrd/mha file format. It was what I was thinking to do however I did not know which file format to use. Thanks !</p>
<p>I am not interested in the Real-Time display, we have to do further processing to combine several acquisitions together.</p>
<p>I will update the post when I succeed in everything and share how I did it.</p>

---

## Post #4 by @Anjalimukundan (2023-01-23 06:59 UTC)

<p>As mentioned above can Matlab get us real time data from the tracker and ultrasound machine, Iam  pretty new at this so your help will be highly appreciated.</p>

---
