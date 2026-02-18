# Loading of GE/Kretz ultrasound volumes (.vol file)

**Topic ID**: 808
**Date**: 2017-08-02
**URL**: https://discourse.slicer.org/t/loading-of-ge-kretz-ultrasound-volumes-vol-file/808

---

## Post #1 by @Martin_Ceschin (2017-08-02 15:06 UTC)

<p>Good morning, I have a doubt as to the extensions that the program can upload. In my case I need to load a cartesian volume file with .vol extension to edit it and convert it into a 3D STL model. Is it possible to do this with 3D Slicer?</p>

---

## Post #2 by @lassoan (2017-08-02 15:22 UTC)

<p>There are a couple of different file formats that use .vol extension. Where does this file come from?</p>
<p>If it’s from an old GE ultrasound system then most likely it is a Kretz volume file, which has no known free converter, although you might find some free viewers (<a href="https://groups.google.com/forum/#!topic/comp.protocols.dicom/PMMnxcTh6nw">https://groups.google.com/forum/#!topic/comp.protocols.dicom/PMMnxcTh6nw</a>). For example, free viewer that might work is <a href="http://www.tomovision.com/download/download_tomo.html">TomoVision</a>. The cheapest available converter is <a href="http://www.tomovision.com/download/download_dicomatic.html">DICOMatic</a>, costs $1000.</p>
<p>Kretzfile loading has come up a couple of times, so I would implement a reader for it in Slicer, but for reverse-engineering the file format I would need 3-4 sample images of phantoms (preferably with different sizes, acquired with different imaging settings).</p>

---

## Post #3 by @Martin_Ceschin (2017-08-02 15:51 UTC)

<p>Thanks for your answer<br>
This file is originated by the ultrasound, I need to make a 3D impression of a 4d-5d ultrasound. The equipment that manages this extension are those of General Electric.</p>
<p>Thanks</p>

---

## Post #4 by @lassoan (2017-08-03 04:51 UTC)

<p>OK, so most likely the files are in Kretzfile format. You can confirm that by opening them with the free TomoVision viewer. If you want to 3D print it then you have to convert to a usable format by either buying DICOMatic ($1000), Mimics (around $15000), or share a few data sets that we can use to implement support for it in Slicer (for free).</p>

---

## Post #5 by @bobby_hill (2017-08-29 23:29 UTC)

<p>I have a GE Voluson I 730 and would be able to send any data you need to get these to work in slicer. I send to the slicer listener via dicom but get an error trying to load the file no geometry data</p>

---

## Post #6 by @lassoan (2017-08-30 00:09 UTC)

<p>OK. For this, please acquire a few scans with varying depth, zoom, etc. settings, of an object with known dimensions (preferably use an ultrasound quality assurance phantom, but if you don’t have access to one then you can put a cube or sphere shaped object in water). Upload these scans to Dropbox or OneDrive and post the link here.</p>

---

## Post #7 by @bobby_hill (2017-08-30 01:26 UTC)

<p>I will get with the tech and have her do some scans.</p>

---

## Post #8 by @bobby_hill (2017-09-01 03:13 UTC)

<p>Here is a link to 3 files. I have loaded these in the GE 4d viewer software and it has volumes…</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vflUeLeeY.ico" class="site-icon" width="32" height="32">
      <a href="https://www.dropbox.com/sh/jlswufzcuo8kmdw/AAA9jMkAmqz6_YKOUBhXkVu_a?dl=0" target="_blank" rel="nofollow noopener">Dropbox</a>
  </header>
  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/images/spectrum-icons/generated/content/content-folder_dropbox-large.png" class="thumbnail onebox-avatar" width="160" height="160">

<h3><a href="https://www.dropbox.com/sh/jlswufzcuo8kmdw/AAA9jMkAmqz6_YKOUBhXkVu_a?dl=0" target="_blank" rel="nofollow noopener">DICOM</a></h3>

<p>Shared with Dropbox</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #9 by @lassoan (2017-09-01 04:32 UTC)

<p>Thank you fro the sample files. I was able to load the files manually but still need to figure out how to get some metadata from the files automatically.</p>
<p>Getting some more files, some of them showing objects with known size would help.</p>

---

## Post #10 by @bobby_hill (2017-09-02 01:07 UTC)

<p>I can do… We will do a a study and supply measurements on them… But how did you get them to load manually?</p>

---

## Post #11 by @lassoan (2017-09-02 11:25 UTC)

<p>I’ve compared the content of each file and from the differences determined where voxels and image size information is stored. Now the challenge is that voxels are stored in a rectangular grid but the image is acquired with a convex probe, so I need to figure out where the spherical projection parameters are stored. For this, it would help if you could also acquire a scan of a flat surface, such as a bottom of a water-filled plastic box, at a few different depths.</p>

---

## Post #12 by @bobby_hill (2017-09-03 16:17 UTC)

<p>At what levels do you need the measurements?..</p>
<p>Basically the tech wants to know what you need and she will scan it for<br>
you…</p>
<p>Thanks</p>

---

## Post #13 by @lassoan (2017-09-03 19:34 UTC)

<p>Something like these:</p>
<ul>
<li>probe imaging depth set to 5cm, have the water tank bottom at 3cm</li>
<li>imaging depth set to 10cm, have the water tank  bottom at 5cm</li>
<li>imaging depth set to 10.5cm, have the water tank  bottom at 5cm</li>
<li>imaging depth set to 11cm, have the water tank  bottom at 5cm</li>
<li>imaging depth set to 15cm, have the water tank  bottom at 10cm</li>
</ul>
<p>Always have an object of known size in the image (such as a dice or coin).</p>
<p>In the meantime, I’ve found out how data fields are stored in the image header, I can retrieve angular resolution, image size, field of view, etc. The only information that I could not decode yet is the imaging depth start/end. That’s why the above described set of images with different imaging depth would help.</p>

---

## Post #14 by @lassoan (2017-09-08 19:18 UTC)

<p>Importing is now available in latest Slicer nightly version, in SlicerHeart extension. See a demo here:</p>
<div class="lazyYT" data-youtube-id="UHq0uyDvhaA" data-youtube-title="View your baby ultrasound and create 3D printable model using free software" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>Conversion of spherical coordinates to Cartesian is not perfect yet, there are distortions in the images. If you send me those additional images that I’ve asked then there is a good chance I can fix all remaining issues.</p>

---

## Post #15 by @Amir_Zolal (2017-09-16 05:58 UTC)

<p>Andras, did you already get the data you need?</p>
<p>Amir</p>

---

## Post #16 by @lassoan (2017-09-18 02:46 UTC)

<p>I would still need some more data to finalize scan conversion (from spherical to Cartesian). Put a small object of known dimensions (such as a dice or thick coin) into water container with flat bottom and acquire images like these:</p>
<ul>
<li>start imaging depth set to 0cm, imaging depth set to about 10cm. This setting will serve as baseline, keep all parameters that are not mentioned unchanged compared to these settings.</li>
<li>imaging depth set very slightly (by 5-10mm) less</li>
<li>imaging depth set very slightly (by 5-10mm) more</li>
<li>imaging depth set to much more (by 3-5cm)</li>
<li>imaging depth set to much less (by 3-5cm)</li>
<li>field of view decreased a bit (by a few degrees)</li>
<li>field of view decreased significantly (by at least 15-20 degrees)</li>
<li>start imaging depth set to a small value (1-2cm?)</li>
<li>start imaging depth set to a larger value (3-5cm?)</li>
</ul>

---

## Post #17 by @Amir_Zolal (2017-09-18 11:18 UTC)

<p>I will try to obtain the scans till the end of the week. If it helps I will also try take the object to the angio suite or CT so that you have an exact 3D representation for comparison.</p>
<p>Moreover, there was a plugin for Amira written at our institution years ago to import the kretz files. Unfortunately the developer left and I cannot find the source code. All I have now is the dll, that you could disassemble to get to the algorithm. But I don’t think thats helpful. I will try to search for the source code though.</p>
<p>Amir</p>

---

## Post #18 by @lassoan (2017-09-18 19:45 UTC)

<p>Thanks in advance.</p>
<p>If the Amira reader implemented scan conversion then it’s source code would be very useful.</p>

---

## Post #19 by @Amir_Zolal (2017-09-19 17:27 UTC)

<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vflUeLeeY.ico" class="site-icon" width="32" height="32">
      <a href="https://www.dropbox.com/s/t3ekv0u98emi2q4/BrainlabKugel.zip?dl=0" target="_blank" rel="nofollow noopener">Dropbox</a>
  </header>
  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/images/spectrum-icons/generated/content/content-zip-large.png" class="thumbnail onebox-avatar" width="160" height="160">

<h3><a href="https://www.dropbox.com/s/t3ekv0u98emi2q4/BrainlabKugel.zip?dl=0" target="_blank" rel="nofollow noopener">BrainlabKugel.zip</a></h3>

<p>Shared with Dropbox</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>This is a “brainlab disposable reflective marker sphere” in a cylinder container with water. The bottom of the container is not perfectly flat. I didnt find any better Phantom. There Voluson E8 exports also DICOM, DICOM with DICOMDIR, 4dv (i took uncompressed, proprietary format again I think).</p>
<p>For the vol files, it exports vol (nicht cartesian), vol with wavelet (compression I guess, can be lossy or not lossy, so I took the not lossy) and most imortantly, VOL Karthesisch=cartesian.</p>
<p>So I think maybe modifying your algorithm so that the volumes of carthesian and not carthesian match could help.</p>
<p>I have given up the search for the source code of our amira plugin, because its long lost and as far as I know, it only imports the “cartesian” volumes.</p>
<p>What I want to say is that there are also cartesian volumes around, that could be imported with more ease. However, I don’t know since what version the export of cartesian is supported on the machines.</p>
<p>Let me know if this helps or is completely useless and I should search for another phantom.</p>
<p>Amir</p>

---

## Post #20 by @lassoan (2017-09-19 23:06 UTC)

<p>Thank you these images are very useful. I’ll try to update the code to handle Cartesian volumes and improve scan conversion of spherical volumes.</p>

---

## Post #21 by @Wilber_Lopez_T (2017-10-19 21:09 UTC)

<p>hi guys, any progress?</p>

---

## Post #22 by @FabianR (2017-11-10 20:24 UTC)

<p>hey <a class="mention" href="/u/lassoan">@lassoan</a>  , i am a student (Computer Science) from an university from Chile (Universidad Austral de Chile , UACH), and i am part of a group that is trying  to read Kertz ultrasound to make a 3D impression.<br>
We are thinking if you need help with more data sets or even development, to improve the scan conversion, because we might be able to help you if you want, we have a Voluson i if you are interested.</p>

---

## Post #23 by @lassoan (2017-11-11 15:27 UTC)

<p>It would be great if you could help with improving the importer. There are two main limitations:</p>
<ul>
<li>import from simple rectilinear volumes is not implemented yet (we would just need to figure out which fields store image spacing and use that and disable scan conversion)</li>
<li>it is not clear how to determine start/end radius for spherical acquisitions (I’ve got some more data that should help in finding out which fields to use and how, but I did not have time to analyze it yet)</li>
</ul>

---

## Post #24 by @miquelin (2018-01-24 15:06 UTC)

<p>I followed the instruction that you suggest but have no success to load .vol imagens in 3D Slicer. This .vol imagens opens in TomoVision but not in 3D Slicer. Any advice?</p>

---

## Post #25 by @lassoan (2018-01-24 15:23 UTC)

<p>I have only implemented importing of images acquired with a spherical probe, your might have been acquired with a cylindrical, or there could have been other differences. I’ll improve the importer in the following weeks and post an update here.</p>

---

## Post #26 by @Jake (2018-01-31 19:29 UTC)

<p>I am having the same problem as Charlie and the probe for the GE machine is a rab6-4d convex probe.  I’m pretty sure you are correct Andras, and this is a cylindrical probe.  From my research it seems the most popular type for that machine. I don’t have direct access to the machine, but I might be able to get some data for you if that would be of help.  Thank you for all you do.</p>

---

## Post #27 by @lassoan (2018-02-01 04:21 UTC)

<p>OK, thanks for the note. I’ll find some time to work on this soon.</p>

---

## Post #28 by @oscarvalz (2018-02-01 17:12 UTC)

<p>Hi! thanks for your awesome work!! do you need anymore data??? i have a Voluson P8, if you need some volumetric data tell me</p>

---

## Post #29 by @oscarvalz (2018-02-01 17:15 UTC)

<p>You have to save the file as a compressed volume format, and then search for a file with the extension .4dv</p>

---

## Post #31 by @shenziheng (2018-03-22 04:32 UTC)

<p>hi guys, any progress? I met this problem too.</p>

---

## Post #32 by @Ian_Kiel (2018-03-23 14:47 UTC)

<p>Hola Fabian! Trabajo en la Universidad de Concepción y estamos en un proyecto relacionado a lo que comentas, como puedo contactarte? mi correo es ian.kiel@crai.cl.</p>
<p>Saludos!</p>

---

## Post #33 by @lassoan (2018-03-23 17:35 UTC)

<p>Please keep the conversation in English.</p>
<p>I haven’t had time recently to work on this, but if somebody could spend some time with improving the importer then I could give pointers where to start.</p>

---

## Post #34 by @albert_buwono (2018-05-18 00:55 UTC)

<p>i try different extension to save image in volume in voluson s8 dicom, uncompressed 4dv, cartesian volume, (vol, raw). could you tell me where is extension for nightly 3d slicer?? thank you</p>

---

## Post #35 by @lassoan (2018-05-19 15:28 UTC)

<p>The importer is provided by SlicerHeart extension.</p>

---

## Post #36 by @kopachini (2018-05-28 09:37 UTC)

<p>Hi everybody.<br>
I have also problems as mentioned above. I have several studies performed with GE Voluson S8 and S10, and Siemens acuson x300. All three US have convex probe.</p>
<p>I have nightly version od Slicer and have installed SlicerHeart extension but still can’t do anything. When I try to upload .vol file directly (drag and drop) nothing appears, and when I try to open the whole folder of study, a usual message appears … could not upload… scalar volume.</p>
<p>Desperately need help, thank you!!</p>
<p>Vjekoslav.</p>

---

## Post #37 by @albert_buwono (2018-06-03 23:42 UTC)

<p>hi kopachini. same problem. i instaled slice heart also, import vol, dicom, and other format doesnt appear anything. could someone help more detailed how to load.  thank you so much</p>

---

## Post #38 by @lassoan (2018-06-04 00:13 UTC)

<p>Anybody who has GE/Kretz ultrasound volumes that fails to load after installing SlicerHeart extension: please upload anonymized or phantom datasets to a file sharing service and send me the link in private message so that I can investigate.</p>

---

## Post #39 by @RobertS (2018-06-20 20:12 UTC)

<p>Couldn’t find out how to send a private message. here is some data that I couldn’t get to import. Came up with ‘Voxel data not found’</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/sh/4x10xieahr67i9v/AABvrIaVDG8gHeORYyIM1iPda?dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon-vfl8lUR9B.ico" class="site-icon" width="" height="">

      <a href="https://www.dropbox.com/sh/4x10xieahr67i9v/AABvrIaVDG8gHeORYyIM1iPda?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/metaserver/static/images/spectrum-icons/generated/content/content-folder_dropbox-large.png" class="thumbnail" width="" height="">

<h3><a href="https://www.dropbox.com/sh/4x10xieahr67i9v/AABvrIaVDG8gHeORYyIM1iPda?dl=0" target="_blank" rel="noopener nofollow ugc">4D Ultrasound</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #40 by @lassoan (2018-06-22 06:27 UTC)

<p>The files that you have uploaded were compressed. Loading of compressed files are not supported. However, I was able to load it into GE’s 4D-View software and from there save it as “3D Cart. vol.” (3D Cartesian volume). I was able to load this Cartesian volume file into Slicer successfully. I just had to make a small tweak, which will be available in nightly releases downloaded June 24 or later.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78f51472adc1444f929138698675b9c86157e577.jpeg" alt="image" data-base62-sha1="hg2npJVXR71fXac9ZxYRnAFWpHF" width="481" height="467"></p>

---

## Post #41 by @florian (2018-10-20 17:45 UTC)

<p>Hi Andras,</p>
<p>sorry, I haven’t been able to find how I can send private messages.</p>
<p>I’ve been trying to load a GE Kretz ultrasound volume (.vol) given to me by a sonographer.<br>
After installing the SlicerHeart Extension I was able to load a few of the supplied files, but I wasn’t able to visualise the volumes correctly following the steps shown in your demonstration video.</p>
<p>Would you be so kind and test the following files?</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/sh/x8erab0mtksmqfm/AABdfV-E3Fo9v-4Q0Otda1CVa?dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon-vfl8lUR9B.ico" class="site-icon" width="" height="">

      <a href="https://www.dropbox.com/sh/x8erab0mtksmqfm/AABdfV-E3Fo9v-4Q0Otda1CVa?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/metaserver/static/images/spectrum-icons/generated/content/content-folder_dropbox-large.png" class="thumbnail" width="" height="">

<h3><a href="https://www.dropbox.com/sh/x8erab0mtksmqfm/AABdfV-E3Fo9v-4Q0Otda1CVa?dl=0" target="_blank" rel="noopener nofollow ugc">3D_ultrasound</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The file version 6_2 seemed to be the “closest” but it seems to be a wrong projection somehow.</p>
<p>Any tips would be very much appreciated!</p>
<p>Thank you</p>

---

## Post #42 by @lassoan (2018-10-20 18:40 UTC)

<p>Image 6_2 looked good for me. I’ve used Segment Editor module’s Threshold effect to create surface and then Scissors effect to remove irrelevant parts and got this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6dd5a68f3278f2277ca69fd4db0f4ba520113ad2.jpeg" data-download-href="/uploads/short-url/fFDMTtNuxbNPpB3N8i9IIa1eLYK.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6dd5a68f3278f2277ca69fd4db0f4ba520113ad2_2_488x500.jpeg" alt="image" data-base62-sha1="fFDMTtNuxbNPpB3N8i9IIa1eLYK" width="488" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6dd5a68f3278f2277ca69fd4db0f4ba520113ad2_2_488x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6dd5a68f3278f2277ca69fd4db0f4ba520113ad2_2_732x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6dd5a68f3278f2277ca69fd4db0f4ba520113ad2_2_976x1000.jpeg 2x" data-dominant-color="676B7C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1206×1234 280 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Scene file: <a href="https://1drv.ms/u/s!Arm_AFxB9yqHte8wjhWIUamIsj-Chg">download</a>. This segmentation is usable for 3D printing.</p>
<p>After that, I’ve used Margin effect to grow the segmentation a bit and used it as mask in Mask Volume effect (this effect shows up if you install SegmentEditorExtraEffects extension) to blank out parts of the input volume that are outside the segmented region, and visualized result using Volume rendering module:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c81dcd639bd3636b787d3584ab553b0de4c770f.jpeg" data-download-href="/uploads/short-url/ftTNmKdrwVYjFXDHkEagJyBs9D9.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6c81dcd639bd3636b787d3584ab553b0de4c770f_2_600x500.jpeg" alt="image" data-base62-sha1="ftTNmKdrwVYjFXDHkEagJyBs9D9" width="600" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6c81dcd639bd3636b787d3584ab553b0de4c770f_2_600x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c81dcd639bd3636b787d3584ab553b0de4c770f.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c81dcd639bd3636b787d3584ab553b0de4c770f.jpeg 2x" data-dominant-color="9C91B6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">698×581 124 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Scene file: <a href="https://1drv.ms/u/s!Arm_AFxB9yqHte8xnR8axgq6uXR86A">download</a></p>

---

## Post #43 by @florian (2018-10-20 18:55 UTC)

<p>thanks so much for all these valuable tips and getting back so quickly! I’m going to try and replicate your workflow.</p>
<p>I’m wondering about why the other files aren’t working.</p>
<p>If I asked the sonographer to re-supply some data, how would I need to describe the type of data that’s supported by Slicer? Would it be an “uncompressed 3D Cartesian volume file”?</p>

---

## Post #44 by @lassoan (2018-10-20 19:20 UTC)

<p>All the other volumes are imported correctly, too, but the default brightness/contrast of the image is off (the image is too dark because there is a very bright spot and the automatic contrast adjustment method optimizes the visibility of that spot). You can make the image brighter by click-and-drag mouse left button over the slice view in down/right direction.</p>

---

## Post #45 by @florian (2018-10-20 19:24 UTC)

<p>That’s it! fantastic, thank you!!</p>

---

## Post #46 by @lassoan (2018-10-21 02:04 UTC)

<aside class="quote no-group" data-username="florian" data-post="43" data-topic="808">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/898d66/48.png" class="avatar"> florian:</div>
<blockquote>
<p>how would I need to describe the type of data that’s supported by Slicer? Would it be an “uncompressed 3D Cartesian volume file”?</p>
</blockquote>
</aside>
<p>For GE Kretzfile format, it does not have to be Cartesian (actually, you may get more accurate images if saved as native, non-Cartesian volume), but it must be uncompressed.</p>

---

## Post #47 by @dlovett (2018-10-22 10:13 UTC)

<p>Hi Andras,</p>
<p>I am trying to load some .vol files from a GE machine (GE Voluson S8) that I have been sent by a sonographer. is it possible I could email you a private link to the files and ask if you can open them as I am struggling to. I have the latest nightly build with the heart slice extension installed, but nothing happens when I open the files. I have downloaded a copy of the GE 4d view app (10.5bt12 ext1) and with this I can open the file sample files ok.</p>
<p>Many thanks</p>
<p>Duncan</p>

---

## Post #48 by @lassoan (2018-10-22 17:49 UTC)

<p>Feel free to send me the link in a private message (click on my name and then on the message button).</p>

---

## Post #50 by @xVVx (2018-10-26 11:09 UTC)

<p>Hi,<br>
I am jewelry designer and i would like to implement my wife USG to 3d software, and then make probably some jewelry. I tried to open .vol file from the Voluson S10(probably) machine in 3D Slicer, but i see nothing. I can’t write to you in priv now.  If you have any suggestion what can i do with it, i will be very grateful <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=6" title=":slight_smile:" class="emoji" alt=":slight_smile:"> I can of course share a file…</p>

---

## Post #51 by @lassoan (2018-10-26 13:51 UTC)

<p>Install SlicerHeart extension and follow these instructions to load .vol files into Slicer: <a href="https://github.com/SlicerHeart/SlicerHeart#ge">https://github.com/SlicerHeart/SlicerHeart#ge</a></p>

---

## Post #52 by @xVVx (2018-10-26 14:48 UTC)

<p>It works! Thanks a lot <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
Is there any possibility to export model smoother like that?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52d08670f8726d9300f84cb49478ffee1b9a1bb1.jpeg" alt="image" data-base62-sha1="bOBULQReRyiIdqdSq3VKNzoCqJP" width="520" height="389"><br>
When i export it looks like this<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f2094a0bc5db4400cccfb908f924153ff3d91ed.jpeg" alt="image" data-base62-sha1="29OXRQQOF7qINrpwqF1jWWp8Pp3" width="564" height="499"><br>
Any suggestions?</p>

---

## Post #53 by @xVVx (2018-11-07 12:17 UTC)

<p>Anyone have some suggestions?</p>

---

## Post #54 by @avarghes23 (2018-11-09 15:27 UTC)

<p>While in the Segment Editor module, if you click the dropdown arrow next to “Show 3D”, you can set surface smoothing. By default, I believe it is at 0.5.</p>

---

## Post #55 by @lassoan (2018-11-09 15:49 UTC)

<p>If the goal is nice model to look at on screen then I would recommend volume rendering, as you make boundaries semi-transparent, which naturally smoothes out any surface errors.</p>
<p>If the goal is 3D printing of the model with a common plastic/PLA printer using non-transparent materials then you need to generate a surface mesh (that is the input format for these printers). You can apply smoothing during 3D model generation as <a class="mention" href="/u/avarghes23">@avarghes23</a> recommended above. If that’s not enough then you can use Smoothing effect in the Segment Editor.</p>
<p>You can print volume rendering using <a href="https://github.com/SlicerFab/SlicerFab">pixel printing</a> technique, but such printers are very scarcely available.</p>

---

## Post #56 by @xVVx (2018-11-09 16:18 UTC)

<p>Thank you all for the suggestions. I will try this method.<br>
I usually use printers with high accuracy like SLA, so the accurancy is up to 10 microns.</p>
<p>Have a nice weekend.</p>

---

## Post #58 by @schmidhuber (2019-02-20 00:52 UTC)

<p>Hello, I have a GE Voluson E6. I wan’t to open .vol files on Slicer but I haven’t be able to do it.<br>
I have been using the 4.11 nigtly version, I couldn’t find the extension “SlicerHeart”, Or, is there another way to import these files and get an image suitable for 3d printing?</p>

---

## Post #59 by @lassoan (2019-02-20 04:42 UTC)

<aside class="quote no-group" data-username="schmidhuber" data-post="58" data-topic="808">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/ecae2f/48.png" class="avatar"> schmidhuber:</div>
<blockquote>
<p>using the 4.11 nigtly version, I couldn’t find the extension “SlicerHeart”</p>
</blockquote>
</aside>
<p>There are some build errors preventing SlicerHeart extension to show up in latest nightly build. Until the error is fixed, you can use the latest stable Slicer version.</p>

---

## Post #61 by @Kwstas_Papas (2019-03-04 19:19 UTC)

<p>Hello I have a GE Voluson E8 ultrasound system and I want to extract an ultrasound file for 3D editing in 3D Slicer program. However, I know neither what exactly to extract nor how to do it. I have read some of your comments about inserting data in 3D Slicer program. Could you give me some instructions what to do?</p>
<p>Thank you in advance, Kostas.</p>

---

## Post #62 by @lassoan (2019-03-05 16:40 UTC)

<p>Slicer can only import certain 3D ultrasound files, yours may or may not be among those that are supported. You need to install SlicerHeart extension and follow instructions described here: <a href="https://github.com/SlicerHeart/SlicerHeart" rel="nofollow noopener">https://github.com/SlicerHeart/SlicerHeart</a>.</p>

---

## Post #63 by @kataru_sreenath (2019-05-18 19:16 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d15c7356e34d0ccc32447e750743f6608976ea3.png" data-download-href="/uploads/short-url/49ivnzNAph9DPjo3BnPAHBPJt5h.png?dl=1" title="2019-05-19%2000_44_19-sirisha%20ultrasound" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d15c7356e34d0ccc32447e750743f6608976ea3.png" alt="2019-05-19%2000_44_19-sirisha%20ultrasound" data-base62-sha1="49ivnzNAph9DPjo3BnPAHBPJt5h" width="690" height="404" data-dominant-color="F1F4F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2019-05-19%2000_44_19-sirisha%20ultrasound</span><span class="informations">779×457 34.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>How to open .vol file.</p>

---

## Post #64 by @lassoan (2019-05-19 13:20 UTC)

<p>Install SlicerHeart extension and follow <a href="https://github.com/SlicerHeart/SlicerHeart#ge" rel="nofollow noopener">these instructions</a> to load .vol files into Slicer.</p>

---

## Post #65 by @Coloradoultrasound (2019-05-21 23:55 UTC)

<p>Hello, we own both an E8 and BT.16 E10 And are planning to 3-D print to PLA for our customers. We have both types of volume formats,.VOL and .VOL Cartesian. We have read through these posts and have slicer set up with slicer heart. From what I can gather, we should be exporting.VOL Cartesian format, was that correct? We plan to then export as an .STL file or .OBJ file. What are the steps for the export of those file types? We would also be happy to send you any types of files from this equipment to help streamline the process</p>

---

## Post #66 by @lassoan (2019-05-22 02:52 UTC)

<aside class="quote no-group" data-username="Coloradoultrasound" data-post="65" data-topic="808">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/coloradoultrasound/48/3835_2.png" class="avatar"> Coloradoultrasound:</div>
<blockquote>
<p>VOL Cartesian format, was that correct?</p>
</blockquote>
</aside>
<p>Yes.</p>
<aside class="quote no-group" data-username="Coloradoultrasound" data-post="65" data-topic="808">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/coloradoultrasound/48/3835_2.png" class="avatar"> Coloradoultrasound:</div>
<blockquote>
<p>We plan to then export as an .STL file or .OBJ file. What are the steps for the export of those file types?</p>
</blockquote>
</aside>
<p>You need to segment the volume using Segment editor module. See tutorials <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation">here</a>. If you have any questions then post them as new topics.</p>
<p>Once you are done with segmentation, use “Segmentations…” button’s drop-down menu and choose “Export to files…”.</p>

---

## Post #67 by @Coloradoultrasound (2019-05-22 15:30 UTC)

<p>Thank you, that was helpful. I am referencing this video walkthrough but am running into some issues which are most likely user error, <a href="https://www.youtube.com/watch?v=UHq0uyDvhaA&amp;feature=youtu.be" class="inline-onebox" rel="noopener nofollow ugc">View your baby ultrasound and create 3D printable model using free software - YouTube</a></p>
<p>When I move from Volume Rendering to to Segment Editor, the segments I create are not shown in the 3d rendering box 1. Not sure what I am doing wrong.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c67417ea1bf66b03f8d8900b2ae2118f8e8e0400.jpeg" data-download-href="/uploads/short-url/sjBgCKA91Ojvg6Kze7YnOgAOsN2.jpeg?dl=1" title="SEGMENTATION" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c67417ea1bf66b03f8d8900b2ae2118f8e8e0400_2_690x386.jpeg" alt="SEGMENTATION" data-base62-sha1="sjBgCKA91Ojvg6Kze7YnOgAOsN2" width="690" height="386" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c67417ea1bf66b03f8d8900b2ae2118f8e8e0400_2_690x386.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c67417ea1bf66b03f8d8900b2ae2118f8e8e0400.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c67417ea1bf66b03f8d8900b2ae2118f8e8e0400.jpeg 2x" data-dominant-color="969597"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SEGMENTATION</span><span class="informations">974×545 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #68 by @Coloradoultrasound (2019-05-22 15:32 UTC)

<p>This means of course that any edits I try to make will not take effect (such as scissors/magic cut)</p>

---

## Post #69 by @lassoan (2019-05-22 18:09 UTC)

<p>You need to paint the mask (using threshold, paint, scissors, etc. effects) and use Mask Volume effect to apply the mask to the volume (blank out regions). Install SegmentEditorExtraEffects extension to get Mask volume effect in Segment Editor.</p>

---

## Post #70 by @Coloradoultrasound (2019-05-22 20:20 UTC)

<p>Really appreciate the help, that worked. How do you clear the 3D box when going from say Filtering/Volume Rendering/ ETC then to Segment Editor, I know I must be missing something simple? <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/355aab53df2c108fe25e4f0e491ba6c156da2129.png" data-download-href="/uploads/short-url/7BZyXDQhNXWkHZMQAzBGgruB773.png?dl=1" title="Segment%20Editor" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/355aab53df2c108fe25e4f0e491ba6c156da2129_2_690x318.png" alt="Segment%20Editor" data-base62-sha1="7BZyXDQhNXWkHZMQAzBGgruB773" width="690" height="318" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/355aab53df2c108fe25e4f0e491ba6c156da2129_2_690x318.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/355aab53df2c108fe25e4f0e491ba6c156da2129.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/355aab53df2c108fe25e4f0e491ba6c156da2129.png 2x" data-dominant-color="98989D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Segment%20Editor</span><span class="informations">974×449 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #71 by @lassoan (2019-05-22 22:06 UTC)

<p>You can show/hide the cropping ROI box in volume rendering module. You can show/hide any node in the Data module (subject hierarchy tab) by clicking on the eye icon.</p>

---

## Post #72 by @kopachini (2019-05-27 19:49 UTC)

<p>If you have E10 you should be able to export STL directly from ultrasound.</p>

---

## Post #73 by @Coloradoultrasound (2019-05-27 20:18 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e457ea94ee1710b1527d51fcde083562c941b3ff.jpeg" data-download-href="/uploads/short-url/wA1dPKQgYkRq9iG4n81WZDA33mn.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e457ea94ee1710b1527d51fcde083562c941b3ff_2_375x500.jpeg" alt="image" data-base62-sha1="wA1dPKQgYkRq9iG4n81WZDA33mn" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e457ea94ee1710b1527d51fcde083562c941b3ff_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e457ea94ee1710b1527d51fcde083562c941b3ff_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e457ea94ee1710b1527d51fcde083562c941b3ff_2_750x1000.jpeg 2x" data-dominant-color="7B7469"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3024×4032 3.09 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> Unfortunately, this is not the case. We have a BT.16 and only a BT.18 has the .STL .OBJ file export option. Appreciate the recommendation though.</p>
<p>I’ve actually had some success now after some deliberation to get this to work. I’m still having some issues getting the same resolution or quality that our E10 is getting. I am using the smoothing feature. If anyone else has any suggestions as far as improving the facial images for a later 3D print I’d love to hear it as I’m getting more familiar with this software.</p>

---

## Post #74 by @Rodrigo_Visconti (2019-06-02 05:15 UTC)

<p>I’m trying to print cardiac 3D volumes from TEE into slicer but i can’t load these files. I use GE Vivid E95 and E9. Any clue on how to load these files? Phillips cardio images load with no problems.</p>

---

## Post #75 by @lassoan (2019-06-02 19:20 UTC)

<p>SlicerHeart can only read images exported in KretzFile format (or its DICOM-ized variant), which are mostly used by obstetrics and not cardiac systems. Last time we asked, GE would require us to sign a non-disclosure agreement to get specification of private DICOM fields that are required to read their TEE ultrasound volumes. However, such an agreement would prevent us from continuing our research and platform development work completely openly.</p>
<p>It would be great if GE changed their ultrasound systems to store image data in standard DICOM fields; or published how to retrieve image data from their private DICOM fields; or provided an export tool similar to Philips QLab (which creates DICOM files that store image data in standard fields). Make GE and your hospital administration aware of this issue and these potential solutions. Until GE does something about this, you may need to switch to Philips systems for research studies that require image data access.</p>

---

## Post #76 by @Rodrigo_Visconti (2019-06-08 18:04 UTC)

<p>I asked GE engineers about this issue and they don’t have an answer yet. How can I put the images of Philips platform in scale? The stl files became too small.</p>

---

## Post #77 by @lassoan (2019-06-08 19:25 UTC)

<p>Philips systems store some essential information in private DICOM fields, therefore you need to follow these instructions to load them correctly: <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/README.md#philips" rel="nofollow noopener">https://github.com/SlicerHeart/SlicerHeart/blob/master/README.md#philips</a></p>

---

## Post #78 by @Rodrigo_Visconti (2019-07-07 11:48 UTC)

<p>DICOMatic software claims to transform GE dicom into conventional dicom… Do you know if this archive can be loaded into slicer?</p>

---

## Post #79 by @HirofumiSeo (2019-07-24 15:25 UTC)

<p>lassoan,</p>
<p>Thank you so much for your code. This really helps a lot.<br>
I tried visualizing the beam animation referencing your code. Here is the result.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/327ccebba0e2b1126e536188ec1fa9cae79d41b5.gif" data-download-href="/uploads/short-url/7cDgTmj75a7DEarYuQnpVL4VxEF.gif?dl=1" title="KretzReadEchoAnim03" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/327ccebba0e2b1126e536188ec1fa9cae79d41b5_2_690x388.gif" alt="KretzReadEchoAnim03" data-base62-sha1="7cDgTmj75a7DEarYuQnpVL4VxEF" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/327ccebba0e2b1126e536188ec1fa9cae79d41b5_2_690x388.gif, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/327ccebba0e2b1126e536188ec1fa9cae79d41b5.gif 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/327ccebba0e2b1126e536188ec1fa9cae79d41b5.gif 2x" data-dominant-color="16070A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">KretzReadEchoAnim03</span><span class="informations">960×540 1.52 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This might be a question about the transducer’s mechanism rather than the code, but does the beam from 3D echo move like the above instead of like the following?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0cc8867560433476d123115d3e910ad459948228.gif" data-download-href="/uploads/short-url/1P5lSNHqWExIVhMWHVWSOZbh9VK.gif?dl=1" title="KretzReadEchoAnim02" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0cc8867560433476d123115d3e910ad459948228_2_690x388.gif" alt="KretzReadEchoAnim02" data-base62-sha1="1P5lSNHqWExIVhMWHVWSOZbh9VK" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0cc8867560433476d123115d3e910ad459948228_2_690x388.gif, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0cc8867560433476d123115d3e910ad459948228.gif 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0cc8867560433476d123115d3e910ad459948228.gif 2x" data-dominant-color="17090D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">KretzReadEchoAnim02</span><span class="informations">960×540 1.59 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Or like the following?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/dfdd5d8a50351367f6d3c3436c5d0f7ce9e9322a.gif" data-download-href="/uploads/short-url/vWoKrrslHwVEuF00KiP9oeXC2AG.gif?dl=1" title="KretzReadEchoAnim01" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dfdd5d8a50351367f6d3c3436c5d0f7ce9e9322a_2_690x388.gif" alt="KretzReadEchoAnim01" data-base62-sha1="vWoKrrslHwVEuF00KiP9oeXC2AG" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dfdd5d8a50351367f6d3c3436c5d0f7ce9e9322a_2_690x388.gif, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/dfdd5d8a50351367f6d3c3436c5d0f7ce9e9322a.gif 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/dfdd5d8a50351367f6d3c3436c5d0f7ce9e9322a.gif 2x" data-dominant-color="16080B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">KretzReadEchoAnim01</span><span class="informations">960×540 1.54 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I tried measuring some distances in the 3D space and of course the first one seems correct, but I didn’t know that the beam intersects during 3D echo. I looked for some technical document about the beam but I couldn’t find any materials…</p>

---

## Post #80 by @lassoan (2019-07-24 16:46 UTC)

<p>Nice visualization!</p>
<p>Beamforming is partly mechanical (acoustic lens on the transducer) partly electronic (by adjustment of signal time delays), which allows a lot of design freedom. It is not necessary to use a single focal point (what would be the advantage? simpler reconstruction computations?). Instead, focusing is optimized for maximizing signal-to-noise ratio, penetration, geometrical accuracy, etc.</p>
<p>Note that these ultrasound files store a single spherical or cylindrical volume. In reality, the transducer probably generates many more beams, optimized for various depths and smartly integrates them. So, you won’t get too much insight into the inner workings of a transducer by inspecting these volumes.</p>

---

## Post #81 by @HirofumiSeo (2019-07-26 15:32 UTC)

<p>Thank you so much for your reply.<br>
If you do not mind, I would like to know how you formularized the most important part of your vtkSlicerKretzFileReaderLogic.cxx, from the line 280 to 282,<br>
x =  r * sin(theta)<br>
y = -r * cos(theta) * sin(phi) + bModeRadius * sin(phi)<br>
z =  r * cos(theta) * cos(phi) + bModeRadius*(1-cos(phi))<br>
espacially the latter part (bModeRadius * something at y, and z).<br>
I could easily check that x and y was correct by measuring some length via the GE ultrasound apparatus, but I have no idea how you guessed the bModeRadius part.<br>
The three animation gifs I made have been made by changing the bModeRadius part a little bit.<br>
(The first gif is using your original formula.)<br>
And I wonder if (C200, 0004), and (C200, 0005) values are unnecessary for reconstruct the volumes in 3D space.</p>
<p>Thank you.</p>

---

## Post #82 by @lassoan (2019-07-26 21:11 UTC)

<p>I inspected many images and tried to find a logical explanation of how various inputs contributed to the reconstructed output. It was quite fun, like solving a riddle.</p>

---

## Post #83 by @Mate_Toth (2019-08-04 06:50 UTC)

<p>Hi András, would you be able to share the transferred files used for this model?</p>

---

## Post #84 by @lassoan (2019-08-04 23:58 UTC)

<p>See download link in <a href="https://discourse.slicer.org/t/loading-of-ge-kretz-ultrasound-volumes-vol-file/808/42">this post above</a>.</p>

---

## Post #85 by @shaeshaenee (2019-08-13 22:23 UTC)

<p>Continuing the discussion from <a href="https://discourse.slicer.org/t/loading-of-ge-kretz-ultrasound-volumes-vol-file/808/39">Loading of GE/Kretz ultrasound volumes (.vol file)</a>:</p>
<p>HI,<br>
i have a problem <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=9" title=":frowning:" class="emoji" alt=":frowning:"><br>
-i tried importing sample data(s) shared in this discussion,<br>
-i was able to load DICOME samples.<br>
-i am not able to import 4DUltrasound sample, (even after re-saving as 3d Cart volume using 4dviewv.10) … it doesn’t load in slicer …actually it doesn’t load any data! there’s an ERROR in 3dsclier (“vtkSlicerKretzFileReaderLogic::LoadKretzFile failed: file ‘F:/Radiology sample data/Ultrasound/4D Ultrasound/IMG_20180620_2_1_cart.vol’ phi angle array is invalid (expected 260 elements, found 0”)<br>
-the same goes for 3d ultrasound data sample , even after re-saving as non compressed using 4dview v.10)</p>
<ul>
<li>i am using 3dslicer 4.8.0 and slicerhear is installed.<br>
what am i doing wrong?<br>
thanks in advance</li>
</ul>

---

## Post #86 by @lassoan (2019-08-15 15:13 UTC)

<aside class="quote no-group" data-username="shaeshaenee" data-post="85" data-topic="808">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/7bcc69/48.png" class="avatar"> shaeshaenee:</div>
<blockquote>
<p>i am using 3dslicer 4.8.0</p>
</blockquote>
</aside>
<p>Slicer-4.8 only supported spherical volumes. As far as I remember, current Slicer version supports rectilinear volumes, too.</p>
<p>Slicer-4.8 is more than 2 years old. Slicer is constantly being improved with new features and fixes, so if you use such ancient version then you miss out on many things. Always use at least the latest stable release.</p>

---

## Post #87 by @lassoan (2020-01-30 20:02 UTC)

<p>2 posts were merged into an existing topic: <a href="/t/adding-body-to-a-fetus/10031/2">Adding body to a Fetus</a></p>

---

## Post #88 by @samsonaie (2020-04-11 16:24 UTC)

<p>Hi Andras,</p>
<p>Thanks a lot for your sharing. I had learned a lot from you post.<br>
As you had mentioned in many post that GE may have private fileds in their DICOM ( dcm file ) , indeed!, I had followed your instruction to upload to GE’s 4D view v 10.5  ( per link in your Gitbub post ) , I successfully convert it to 3D Cart , and also set wavelet-compression to " none"<br>
see the link below:<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vflUeLeeY.ico" class="site-icon" width="16" height="16">
      <a href="https://www.dropbox.com/s/t8mghjgkn66yj5r/IMG_20200410_1_58-3DCart%20vol%20none-wave.dcm?dl=0" target="_blank" rel="nofollow noopener">Dropbox</a>
  </header>
  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/images/spectrum-icons/generated/content/content-unknown-large.png" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://www.dropbox.com/s/t8mghjgkn66yj5r/IMG_20200410_1_58-3DCart%20vol%20none-wave.dcm?dl=0" target="_blank" rel="nofollow noopener">IMG_20200410_1_58-3DCart vol none-wave.dcm</a></h3>

<p>Shared with Dropbox</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>however I still fail to upload to Slicer v4.10 in which I had already included SlicerHeart extension<br>
would you check the file for me and let me know if I had done anything wrong ?</p>
<p>the original dcm is in here:<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vflUeLeeY.ico" class="site-icon" width="16" height="16">
      <a href="https://www.dropbox.com/s/bcvoskxd291kkzp/IMG_20200410_1_58.dcm?dl=0" target="_blank" rel="nofollow noopener">Dropbox</a>
  </header>
  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/images/spectrum-icons/generated/content/content-unknown-large.png" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://www.dropbox.com/s/bcvoskxd291kkzp/IMG_20200410_1_58.dcm?dl=0" target="_blank" rel="nofollow noopener">IMG_20200410_1_58.dcm</a></h3>

<p>Shared with Dropbox</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>thank you very much, it will certainly be great if you can guide me on how to load it to slicer successfully.</p>

---

## Post #89 by @lassoan (2020-04-26 01:04 UTC)

<p>I remember answering this question somewhere (maybe in another topic or forum) but cannot find it. Anyway, I could load both images without any problems by installing latest Slicer Preview Release (4.11, rev 29009) and SlicerHeart extension, then importing and loading them in DICOM module.</p>

---

## Post #90 by @samsonaie (2020-04-30 03:18 UTC)

<p>Yes, you had helped me. with the latest verison 4.11.-4-19 works fine.<br>
Thanks again.</p>

---

## Post #91 by @Guangxu_Li (2020-05-31 15:53 UTC)

<p>A very good ITK based example: <a href="https://github.com/plooney/kretz" rel="nofollow noopener">https://github.com/plooney/kretz</a>.<br>
If you use 4D images, the ‘number of frames’ could be obtained in tag (0xd400, 0x0001).</p>

---

## Post #92 by @lassoan (2020-10-10 02:28 UTC)

<p>A post was split to a new topic: <a href="/t/segmenting-ge-voluson-ultrasound-image/13971">Segmenting GE Voluson ultrasound image</a></p>

---

## Post #93 by @lassoan (2020-12-23 14:57 UTC)

<p>2 posts were split to a new topic: <a href="/t/how-to-import-ultrasound-images-from-samsung-accuvix/15201">How to import ultrasound images from Samsung accuvix</a></p>

---

## Post #94 by @Gregory_Van (2020-12-23 19:12 UTC)

<p>Hi,</p>
<p>Thank you Andras for putting all the work into this! Exactly what I was looking for! One question, is the github link for GE’s API files ( <a href="https://github.com/GEUltrasound/GE_CVUS_Loader/releases/" rel="noopener nofollow ugc">https://github.com/GEUltrasound/GE_CVUS_Loader/releases/</a> ) still in working order? I get a 404 error message but is that due to the fact that GE hasnt accepted me into the Edison Developer Program yet? I havent heard back from GE and just getting a little anxious.</p>

---

## Post #95 by @Mich (2021-01-17 18:43 UTC)

<p>Hello! I have the Cartesian Vol format of a Voluson S8, How can I import it to the 3D Slicer ?because I have not achieved it, I hope you can help me.</p>

---

## Post #96 by @lassoan (2021-01-17 18:49 UTC)

<p>Most probably you can use Image3dAPI to load that file. See detailed information here: <a href="https://github.com/SlicerHeart/SlicerHeart#ge" class="inline-onebox">GitHub - SlicerHeart/SlicerHeart: 3D Slicer extension for cardiac analysis</a>.</p>
<p>If you share an example file then I can verify that SlicerHeart can indeed load it.</p>

---

## Post #97 by @Mich (2021-01-17 19:01 UTC)

<p>Hello, thanks for the answer, I already downloaded the SliceHeart and I still can’t, I share the file for you to verify it, is it necessary to register in the Edison program to be able to achieve it?<br>
<a href="https://www.dropbox.com/sh/63ujg7yl1o0pwcq/AADAcYlHdDpFb91CSbYbfnK5a?dl=0" rel="noopener nofollow ugc">https://www.dropbox.com/sh/63ujg7yl1o0pwcq/AADAcYlHdDpFb91CSbYbfnK5a?dl=0</a></p>

---

## Post #98 by @lassoan (2021-01-17 19:38 UTC)

<p>These images can be loaded without Image3dAPI (without joining GE’s developer program), just using SlicerHeart.</p>
<p>After you installed SlicerHeart extension and restarted the application, drag-and-drop the .vol files to the application window and click OK to load them.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14a191b799e7f6142fe463da5e6129029b796cbc.jpeg" data-download-href="/uploads/short-url/2WvI0CMZumgSM6sU0VtzLCJmtje.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/14a191b799e7f6142fe463da5e6129029b796cbc_2_690x420.jpeg" alt="image" data-base62-sha1="2WvI0CMZumgSM6sU0VtzLCJmtje" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/14a191b799e7f6142fe463da5e6129029b796cbc_2_690x420.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/14a191b799e7f6142fe463da5e6129029b796cbc_2_1035x630.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/14a191b799e7f6142fe463da5e6129029b796cbc_2_1380x840.jpeg 2x" data-dominant-color="4C4C4D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1373 447 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>After median filtering and adjusting volume rendering transfer functions:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c30d6dc4108a83a56f448418fe17c162e234e9d.jpeg" data-download-href="/uploads/short-url/mhJ7Dd9vgsuiZW2zZSbHhhcIsK9.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9c30d6dc4108a83a56f448418fe17c162e234e9d_2_548x500.jpeg" alt="image" data-base62-sha1="mhJ7Dd9vgsuiZW2zZSbHhhcIsK9" width="548" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9c30d6dc4108a83a56f448418fe17c162e234e9d_2_548x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c30d6dc4108a83a56f448418fe17c162e234e9d.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c30d6dc4108a83a56f448418fe17c162e234e9d.jpeg 2x" data-dominant-color="6C3F28"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">662×604 73.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #99 by @Mich (2021-01-17 22:41 UTC)

<p>Thanks! It´s beutiful</p>

---

## Post #100 by @Coloradoultrasound (2021-01-18 06:02 UTC)

<p>Of course; <a href="https://youtu.be/UHq0uyDvhaA" rel="noopener nofollow ugc">https://youtu.be/UHq0uyDvhaA</a></p>

---

## Post #101 by @simongeek (2021-01-20 07:57 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>,<br>
I added the above file into my Slicer 3D, but volume rendering doesn’t work. Do you know what happened?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/685e96159a5c242b09785a0e2b21dbbc25bfafeb.jpeg" data-download-href="/uploads/short-url/eTij2nf0Xn8i1MVrpOnFcY2vB91.jpeg?dl=1" title="Zrzut ekranu 2021-01-20 o 08.57.19" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/685e96159a5c242b09785a0e2b21dbbc25bfafeb_2_690x366.jpeg" alt="Zrzut ekranu 2021-01-20 o 08.57.19" data-base62-sha1="eTij2nf0Xn8i1MVrpOnFcY2vB91" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/685e96159a5c242b09785a0e2b21dbbc25bfafeb_2_690x366.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/685e96159a5c242b09785a0e2b21dbbc25bfafeb_2_1035x549.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/685e96159a5c242b09785a0e2b21dbbc25bfafeb_2_1380x732.jpeg 2x" data-dominant-color="636377"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Zrzut ekranu 2021-01-20 o 08.57.19</span><span class="informations">1916×1019 222 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #102 by @lassoan (2021-01-20 16:54 UTC)

<p>The <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumerendering.html">volume rendering module documentation</a> should help. Drag-and-drop of volumes from the data tree into views requires recent Slicer Preview Release.</p>

---

## Post #103 by @simongeek (2021-01-20 17:24 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>! It works!</p>
<p>Now, I would like to convert .vol files into .STL, it’s possible using Slicer 3D? Then, I am going to do segmentation on mesh data.</p>

---

## Post #104 by @lassoan (2021-01-20 18:37 UTC)

<p>For 3D printing, you need to segment the image. See video tutorial here: <a href="https://youtu.be/UHq0uyDvhaA">https://youtu.be/UHq0uyDvhaA</a></p>
<p>In addition to the segmentation tools shown in the video, in recent Slicer Preview Releases you can also do local smoothing using a <a href="https://discourse.slicer.org/t/new-segment-editing-feature-smoothing-brush/14577">smoothing brush</a>.</p>

---

## Post #105 by @simongeek (2021-02-11 21:10 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thank you. I have a problem with this file. It is the right format to load into Slicer 3D? I can load this file into Slicer3D, but I don’t see a baby.</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vflUeLeeY.ico" class="site-icon" width="16" height="16">
      <a href="https://www.dropbox.com/sh/lwijz3j6mz2yo34/AACR4QLrQj4e45t1v3ctIwTha?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>
  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/images/spectrum-icons/generated/content/content-folder_dropbox-large.png" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://www.dropbox.com/sh/lwijz3j6mz2yo34/AACR4QLrQj4e45t1v3ctIwTha?dl=0" target="_blank" rel="noopener nofollow ugc">GE</a></h3>

<p>Shared with Dropbox</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #106 by @bahram_jafrasteh (2021-03-08 13:03 UTC)

<p>Can you please let me know how can I open kretz files using python. I tried the following command:<br>
slicer.util.loadVolume(’/IMG_201_1.vol’)<br>
It does not work.<br>
I also tried to open it using the following script and I could not do that.</p>
<pre><code>  plugin = slicer.modules.dicomPlugins['DicomUltrasoundPlugin']()
  loadables = plugin.examine([['/IMG_201_1.vol']])
  node = plugin.load(loadable)
</code></pre>
<p>I got the following error:<br>
E: DcmElement: Unknown Tag &amp; Data (…) larger (…) than remaining bytes in file<br>
Could not load  “/IMG_201_1.vol”<br>
Thank you in advance</p>

---

## Post #107 by @lassoan (2021-03-08 15:23 UTC)

<p>You can follow <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_load_DICOM_files_into_the_scene_from_a_folder">this example</a>.</p>
<p>If you are OK with duplicating some loading logic and you are sure that you will only get .vol files then you can copy-paste code from the DICOM ultrasound plugin:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerHeart/SlicerHeart/blob/715a3eb0c086dfa1e110453ceebd6c750d3989f2/DicomUltrasoundPlugin/DicomUltrasoundPlugin.py#L564-L585" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerHeart/SlicerHeart/blob/715a3eb0c086dfa1e110453ceebd6c750d3989f2/DicomUltrasoundPlugin/DicomUltrasoundPlugin.py#L564-L585" target="_blank" rel="noopener">SlicerHeart/SlicerHeart/blob/715a3eb0c086dfa1e110453ceebd6c750d3989f2/DicomUltrasoundPlugin/DicomUltrasoundPlugin.py#L564-L585</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="564" style="counter-reset: li-counter 563 ;">
<li>import vtkSlicerKretzFileReaderLogicPython</li>
<li>logic = slicer.modules.kretzfilereader.logic()</li>
<li>nodeName = slicer.mrmlScene.GenerateUniqueName(loadable.name)</li>
<li>
<li>ds = dicom.read_file(loadable.files[0], defer_size=30)  # use defer_size to not load large fields</li>
<li>kretzUsDataTag = dicom.tag.Tag('0x7fe1', '0x1101')</li>
<li>kretzUsDataItem = ds.get(kretzUsDataTag)</li>
<li>volFileOffset = kretzUsDataItem.file_tell # add 12 bytes for tag, VR, and length,</li>
<li>
<li># This can be a long operation - indicate it to the user</li>
<li>qt.QApplication.setOverrideCursor(qt.Qt.WaitCursor)</li>
<li>
<li>
<li>outputSpacing = [0.667, 0.667, 0.667]</li>
<li>if "(low-resolution)" in loadable.tooltip:</li>
<li>  outputSpacing = [1.0, 1.0, 1.0]</li>
<li>elif "(high-resolution)" in loadable.tooltip:</li>
<li>  outputSpacing = [0.333, 0.333, 0.333]</li>
<li>
<li>outputVolume = logic.LoadKretzFile(loadable.files[0], nodeName, True, outputSpacing, volFileOffset)</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/SlicerHeart/SlicerHeart/blob/715a3eb0c086dfa1e110453ceebd6c750d3989f2/DicomUltrasoundPlugin/DicomUltrasoundPlugin.py#L564-L585" target="_blank" rel="noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>If you just need to work with .vol files that do not embed the volume in a DICOM file then you can load it with a single line of code (set <code>volFileOffset</code> to 0):</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerHeart/SlicerHeart/blob/715a3eb0c086dfa1e110453ceebd6c750d3989f2/DicomUltrasoundPlugin/DicomUltrasoundPlugin.py#L583" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerHeart/SlicerHeart/blob/715a3eb0c086dfa1e110453ceebd6c750d3989f2/DicomUltrasoundPlugin/DicomUltrasoundPlugin.py#L583" target="_blank" rel="noopener">SlicerHeart/SlicerHeart/blob/715a3eb0c086dfa1e110453ceebd6c750d3989f2/DicomUltrasoundPlugin/DicomUltrasoundPlugin.py#L583</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="573" style="counter-reset: li-counter 572 ;">
<li># This can be a long operation - indicate it to the user</li>
<li>qt.QApplication.setOverrideCursor(qt.Qt.WaitCursor)</li>
<li>
<li>
<li>outputSpacing = [0.667, 0.667, 0.667]</li>
<li>if "(low-resolution)" in loadable.tooltip:</li>
<li>  outputSpacing = [1.0, 1.0, 1.0]</li>
<li>elif "(high-resolution)" in loadable.tooltip:</li>
<li>  outputSpacing = [0.333, 0.333, 0.333]</li>
<li>
<li class="selected">outputVolume = logic.LoadKretzFile(loadable.files[0], nodeName, True, outputSpacing, volFileOffset)</li>
<li>
<li>qt.QApplication.restoreOverrideCursor()</li>
<li>
<li># Show in slice views</li>
<li>selectionNode = slicer.app.applicationLogic().GetSelectionNode()</li>
<li>selectionNode.SetReferenceActiveVolumeID(outputVolume.GetID())</li>
<li>slicer.app.applicationLogic().PropagateVolumeSelection(1)</li>
<li>
<li>return outputVolume</li>
<li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #108 by @bahram_jafrasteh (2021-03-08 17:02 UTC)

<p>Thanks. However, I have some problems.<br>
I am sure that my file is a Kretz file.<br>
I have this error:<br>
File is missing DICOM File Meta Information header or the ‘DICM’ prefix is missing from the header. Use force=True to force reading.<br>
I checked that the output of the fp.read(4) in filereader.py is : b’\x00\x00&amp;\x02’ which is not equal to b"DICM". If I use force=True I should set <code>volFileOffset</code> to 0 .</p>

---

## Post #109 by @lassoan (2021-03-08 17:12 UTC)

<p>There are two Kretz file formats circulating. One of them is just the proprietary data structure in a file. The other one is a DICOM file that contains the proprietary data structure in a private DICOM tag.</p>
<p>DICOM files start with a preamble of 128 bytes that should be ignored. If you want to determine if a file is DICOM or not then parse it using pydicom (already bundled with Slicer) instead of trying to analyze the file on your own.</p>

---

## Post #110 by @bahram_jafrasteh (2021-03-08 19:05 UTC)

<p>So my file is the proprietary data structure in a file. How can I open it using python?<br>
I can easily open it in the Slicer GUI.</p>

---

## Post #111 by @lassoan (2021-03-08 20:24 UTC)

<p>This should work on a non-DICOM-embedded Kretzfile:</p>
<pre><code class="lang-python">volumeNode = slicer.modules.kretzfilereader.logic().LoadKretzFile(
  volFilePath, 'my node name', True, [0.3,0.3,0.3])
slicer.util.setSliceViewerLayers(background=volumeNode, fit=True)
</code></pre>

---

## Post #112 by @bahram_jafrasteh (2021-03-10 14:54 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> . It is working.</p>

---

## Post #113 by @Goli (2021-03-10 22:01 UTC)

<p>Hi Andras <a class="mention" href="/u/lassoan">@lassoan</a>, I hope you’re doing well!</p>
<p>I can successfully load .vol image volumes (from Voluson E10) in Slicer using the SlicerHeart module, which is great. However, the voxel sizes (image spacing) seem to be too large (0.5x0.5x0.5 mm) and the multiplication of the voxel dimensions by the image dimensions don’t match the image depth and width (but the image depth measured using the ruler is correct!). Is there a way to get the correct voxel size from the .vol files? Thank you.</p>

---

## Post #114 by @lassoan (2021-03-10 22:25 UTC)

<p>What probe did you use? Can you share an image of a ultrasound phantom (or an object of known size, for example a Lego brick)?</p>
<p>Note that you can also <a href="https://github.com/SlicerHeart/SlicerHeart#loading-various-3d4d-ultrasound-images-using-image3dapi">get Image3dAPI from GE</a> and read the files using the official GE reader instead of the open implementation.</p>

---

## Post #115 by @Goli (2021-03-11 00:18 UTC)

<p>We used a RAB6-D probe. Unfortunately, I only have patient and volunteer images now (we’re using a hospital’s scanner). I’ll try to get a phantom image next time I’m there. I signed up for the GE Edison Developer Program earlier today.</p>

---

## Post #116 by @klemo4 (2021-05-04 10:24 UTC)

<p>Hi. I am trying to open .vol files from voluson E6 that doctor export for me so i can 3d print them. i have try to open them with slicer but no luck. i get a error every time. i have follow the instruction for [Edison Developer Program], i have install Image3dLoaderGe.dll but still i cant open them,(i just install Image3dLoaderGe.dll from cmd with “regsvr32 Image3dLoaderGe.dll” and then try to open with slicer. Maybe i had to do something else? ). Can someone help plz. i will share my vol file if anyone can open them and tell me how. i think i am doing something wrong.</p>
<p><a href="https://drive.google.com/drive/folders/1MlpSsZKHUDT21OtGGMDc3_F5QO5NmYxn?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1MlpSsZKHUDT21OtGGMDc3_F5QO5NmYxn?usp=sharing</a></p>

---

## Post #117 by @issakomi (2021-05-04 16:40 UTC)

<aside class="quote no-group" data-username="klemo4" data-post="116" data-topic="808">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/c67d28/48.png" class="avatar"> klemo4:</div>
<blockquote>
<p>I am trying to open .vol files from voluson E6 that doctor export for me</p>
</blockquote>
</aside>
<p>The files are in <em>Kretzfile</em> format, but unfortunately they are compressed, not supported by most programs (i don’t ever know a program with support for compressed <em>Kretzfile</em>, except closed from manufacturer).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb5c24049a90d42cc5f6edd6fb1fe44f62794677.png" alt="tv" data-base62-sha1="zRDfQzskUWeBKzh44a3XF3wcU2r" width="375" height="121"></p>

---

## Post #118 by @klemo4 (2021-05-04 16:48 UTC)

<p>Tnx man for the help. I have try it too and i saw the same error but i didn’t know that they are not support to be compressed. so what is why i cant open them. So where is no way i can open them?</p>

---

## Post #119 by @issakomi (2021-05-04 17:38 UTC)

<p>May be the doctor could re-export images without compression. Also, there is GE’s program <em>4DView</em>, but it is not downloadable without registration (it requires device serial number). Files are compressed with wavelet transform<br>
<code>0xD100,0x0001 compression? WTCompression</code><br>
difficult, a lot of work were required to solve the puzzle, not impossible, there are many experiments with wavelets, but  probably there is no working solution…</p>

---

## Post #120 by @issakomi (2021-05-04 18:05 UTC)

<blockquote>
<p>Also, there is GE’s program <em>4DView</em></p>
</blockquote>
<p>There is a link to <em>4DView</em> installer (1drv) in description of <a href="https://github.com/SlicerHeart/SlicerHeart" rel="noopener nofollow ugc">SlicerHeart</a></p>
<p>Edit:<br>
It seems to be possible to archive a file in 4DView without compression, here is one re-exported <a href="https://drive.google.com/file/d/1jbv2YQ4zO4LvEHRgeRtd8IqNKUOmU6Ky/view?usp=sharing" rel="noopener nofollow ugc">file</a></p>

---

## Post #121 by @klemo4 (2021-05-04 19:09 UTC)

<p>THENK you man you have make my day. you have save me. i have no words to tell you. i have install and open the files with <em>4DView</em> and i have archive them and decompress them. now i can fix the so i can print them. tnx again man</p>

---

## Post #122 by @Goli (2021-05-14 16:09 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a>, I used a Lego phantom to confirm the voxel sizes and everything was correct.<br>
On a different note, I have issues opening sample data (.vol) that a collaborator sent us from Hon Kong using an older GE scanner, with a RAB 4-8 probe. Would you know what the problem could be? Is it possible that .vol files from some scanners can’t be opened in Slicer?</p>

---

## Post #123 by @lassoan (2021-05-14 18:12 UTC)

<p>SlicerHeart’s Kretzfile reader and Image3dAPI reader (with Ge’s plugin) can read most GE .vol files. If you can send an anonymized/phantom example image then I can have a look.</p>

---

## Post #124 by @Goli (2021-05-14 22:25 UTC)

<p>Thank you, here’s an example volume: <a href="https://drive.google.com/drive/folders/1pLmKvSodtOm8HNOHrraCAnqLsL0pkIV6?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">VOL Sample - Google Drive</a></p>

---

## Post #125 by @lassoan (2021-05-15 00:13 UTC)

<p>I’ve checked the data set and unfortunately it is a compressed Kretzfile. You can open it with GE 4D View but even (at least my version) can only save it compressed. You may be able to open it using Image3dAPI, if you get <code>KretzLoader.KretzImage3dFileLoader</code> plugin from GE (you need to sign up for the Edison developer program as described <a href="https://github.com/SlicerHeart/SlicerHeart#loading-various-3d4d-ultrasound-images-using-image3dapi">here</a>).</p>

---

## Post #126 by @Goli (2021-05-15 22:03 UTC)

<p>Thank you for looking into this Andras!</p>

---

## Post #127 by @lassoan (2021-10-04 14:06 UTC)

<p>A post was merged into an existing topic: <a href="/t/anyone-know-how-can-i-export-a-3d-volumen-from-mindray-m6-ultrasound-in-dicom-format-to-use-in-slicer/19992/2">Anyone know how can i export a 3D volumen from Mindray M6 ultrasound in DICOM format to use in Slicer?</a></p>

---

## Post #128 by @OliveiraDulce (2022-02-23 23:53 UTC)

<p>I have .V00 files and I would like to extract Cartesian volumes. Using 4D View I cannot open the file, it begs the following information “Cannot decompress file”. Any suggestions?</p>

---

## Post #129 by @lassoan (2022-02-24 05:10 UTC)

<p>If 4D View cannot open the file then the file may be corrupted. You can still try to load it using SlicerHeart extension: install the extension and follow <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/ImageImportExport.md#loading-ge-kretz-ultrasound-images">these instructions</a>.</p>

---

## Post #130 by @OliveiraDulce (2022-02-25 14:13 UTC)

<p>Well, I am using the 4D View Free 60-day demo version and I don’t have an ultrasound machine. That may be why I cannot import the files.<br>
I received the anonymized data from a doctor and what I want is to extract Cartesian volumes to do finite element analysis.</p>

---

## Post #131 by @lassoan (2022-02-25 14:47 UTC)

<p>Unfortunately, ultrasound imaging vendors generally don’t want to make it easy for users to access to 3D/4D ultrasound images because they don’t want to make an effort to support this and/or they want to lock you into using their proprietary software. Therefore, usually you need to spend some time with experimenting with various options to figure out a way to get to the data.</p>
<p>You may ask the doctor to try to save or export the data in all possible formats that the image acquisition software supports.</p>
<p>Are you trying to load cardiovascular or ob/gyn images?</p>

---

## Post #132 by @OliveiraDulce (2022-02-26 11:57 UTC)

<p>I am trying to load ob/gyn imagens.</p>

---

## Post #133 by @lassoan (2022-03-12 18:35 UTC)

<p>A post was merged into an existing topic: <a href="/t/dcmfiletype-140-to-stl-or-obj/22458/2">Dcmfiletype.140 to stl or obj</a></p>

---

## Post #134 by @lassoan (2022-03-21 18:08 UTC)

<aside class="quote no-group" data-username="OliveiraDulce" data-post="130" data-topic="808">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/oliveiradulce/48/14431_2.png" class="avatar"> OliveiraDulce:</div>
<blockquote>
<p>Well, I am using the 4D View Free 60-day demo version and I don’t have an ultrasound machine. That may be why I cannot import the files</p>
</blockquote>
</aside>
<p>Slicer can import Cartesian volumes but it needs to be in one of the supported formats (e.g., non-compressed KretzFile DICOM).</p>
<aside class="quote no-group" data-username="OliveiraDulce" data-post="132" data-topic="808" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/oliveiradulce/48/14431_2.png" class="avatar"> OliveiraDulce:</div>
<blockquote>
<p>I am trying to load ob/gyn imagens.</p>
</blockquote>
</aside>
<p>Then Image3dAPI will probably not help. If GE’s 4DView cannot load the image then you might be able to manually extract some data using <a href="https://github.com/acetylsalicyl/SlicerRawImageGuess">RawImageGuess</a> extension.</p>

---

## Post #135 by @casvane (2022-05-04 18:04 UTC)

<p>Hi</p>
<p>I have tried and read alot about 3D slicer. I have some issue opening a file. I have tried with sliceheart aswel, so I was hoping that you could help me to investigate the issue?<br>
I cannot upload the file here.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77420d2a872a054642a3f2eb78c828f12339efcb.jpeg" data-download-href="/uploads/short-url/h10kG38yl1YDNphz3jXaunrWDMf.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/77420d2a872a054642a3f2eb78c828f12339efcb_2_345x151.jpeg" alt="image" data-base62-sha1="h10kG38yl1YDNphz3jXaunrWDMf" width="345" height="151" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/77420d2a872a054642a3f2eb78c828f12339efcb_2_345x151.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/77420d2a872a054642a3f2eb78c828f12339efcb_2_517x226.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/77420d2a872a054642a3f2eb78c828f12339efcb_2_690x302.jpeg 2x" data-dominant-color="F4F2F1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2178×954 204 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I hope you have some time to help me with.</p>
<p>Best regards<br>
Camilla</p>

---

## Post #136 by @whu (2022-05-30 12:08 UTC)

<p>what is the difference with or without <span class="hashtag">#ge</span> ?   where are the instructions ?<br>
I have the same GE data, after loading througth “Add DICOM Data” button, I can not using the volume rendering.<br>
Need help. thanks</p>

---

## Post #137 by @lassoan (2022-05-30 18:56 UTC)

<aside class="quote no-group" data-username="casvane" data-post="135" data-topic="808">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/67e7ee/48.png" class="avatar"> casvane:</div>
<blockquote>
<p>I have tried and read alot about 3D slicer. I have some issue opening a file. I have tried with sliceheart aswel, so I was hoping that you could help me to investigate the issue?</p>
</blockquote>
</aside>
<p>You can check the application log for more information. It may give some hints about what’s wrong.</p>
<p>The instructions for loading .vol files are available <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/ImageImportExport.md#loading-ge-kretz-ultrasound-images">here</a>.</p>
<aside class="quote no-group" data-username="whu" data-post="136" data-topic="808">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/7ab992/48.png" class="avatar"> whu:</div>
<blockquote>
<p>I have the same GE data, after loading througth “Add DICOM Data” button, I can not using the volume rendering.</p>
</blockquote>
</aside>
<p>You need to first successfully import the image. Follow <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/ImageImportExport.md#loading-ge-kretz-ultrasound-images">these instructions</a> for loading .vol files files and if it fails then check the application log for details.</p>

---

## Post #138 by @Rodolfo (2022-09-23 20:50 UTC)

<p>Hello, I’m starting the fetal ultrasound part, and I have some doubts, following the youtube video tutorial, I installed SlicerHeart and it doesn’t stay, Desciption the “GE Kretz ultrasound volume”, only the “Volume”, what to do? Thanks</p>

---

## Post #139 by @moulibrata_sarkar (2022-10-01 18:56 UTC)

<p>I have a set of 3d volume data obtained from GE logiq p9 ultrasound machine. The scans were performed using curvilinear 3d probes. I want to calculate the volume of certain structures in them… like VOCAL. How do I go about this using 3d slicer?</p>

---

## Post #140 by @newsblue1983 (2023-01-05 22:31 UTC)

<p>I am a student studying the 3d ultrasound volume file. You said .vol is from old GE ultrasound system, may I ask what file extension (.xxx) the newer GE machine use? And how to read in Windows?</p>

---

## Post #141 by @newsblue1983 (2023-01-05 22:58 UTC)

<p>I can read your dcm files in dicom viwer, it is a baby. But it is already reconstruction, I want to see a raw data from machine. Old type GE730 could export dicom file?</p>

---

## Post #142 by @newsblue1983 (2023-01-05 23:10 UTC)

<p>Can you share these 3d volume raw data files?</p>

---

## Post #143 by @lassoan (2023-01-07 16:37 UTC)

<p>Unfortunately, most 3D ultrasound systems save images into proprietary file formats. 3D Slicer can read some of them but not all. See instructions <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/ImageImportExport.md#importing-dicom-files">here</a>.</p>
<aside class="quote no-group" data-username="moulibrata_sarkar" data-post="139" data-topic="808" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/moulibrata_sarkar/48/16672_2.png" class="avatar"> moulibrata_sarkar:</div>
<blockquote>
<p>I have a set of 3d volume data obtained from GE logiq p9 ultrasound machine. The scans were performed using curvilinear 3d probes. I want to calculate the volume of certain structures in them… like VOCAL. How do I go about this using 3d slicer?</p>
</blockquote>
</aside>
<p>First step is to import the image. If you don’t manage to load the data into 3D Slicer using the instructions at the link above then contact your ultrasound sales rep/application specialist for export options.</p>
<p>Then you can use Segment Editor module in Slicer for segmenting any structures.</p>
<aside class="quote no-group" data-username="newsblue1983" data-post="140" data-topic="808" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/newsblue1983/48/17908_2.png" class="avatar"> newsblue1983:</div>
<blockquote>
<p>I am a student studying the 3d ultrasound volume file. You said .vol is from old GE ultrasound system, may I ask what file extension (.xxx) the newer GE machine use? And how to read in Windows?</p>
</blockquote>
</aside>
<p>There are many GE ultrasound systems and they use very different software, so there is no simple answer for these questions.</p>
<aside class="quote no-group" data-username="newsblue1983" data-post="141" data-topic="808">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/newsblue1983/48/17908_2.png" class="avatar"> newsblue1983:</div>
<blockquote>
<p>But it is already reconstruction, I want to see a raw data from machine.</p>
</blockquote>
</aside>
<p>Raw data from the machine is easily accessible - this is usually all you get. The difficulty is that there is no information about how to interpret the raw data. This is not public information, so you either need to sign a research contract with the vendor to get access or reverse-engineer the files.</p>

---

## Post #144 by @newsblue1983 (2023-01-08 11:22 UTC)

<p>So you mean different GE ultrasound machine generate different type of raw data. Unlike dicom   file with a similar meta head info?</p>

---

## Post #145 by @lassoan (2023-01-08 14:32 UTC)

<p>Yes, systems for different clinical segments (cardiovascular, ob-gyn, point-of-care, etc) and different generations of these systems are developed independently by different groups in different countries and generate completely different data sets. Even though they may all use DICOM fields, most data are stored in various private tags.</p>

---

## Post #146 by @Roxxx (2023-02-08 15:30 UTC)

<p>I just read all your suggestions on this thread and tried out some things, but could not get it to work.</p>
<p>Using SlicerHeart it does find the data, but only one slice, so I only see a line in two of the three planes and can’t scroll through the transverse plane.</p>
<p>When I open the data in 4D View all 3D data is there, but I can’t save it in any way that is not only a screenshot of the three planes.<br>
Also the files don’t have an extension.</p>
<p>Do you have any suggestion what could be the problem here?</p>

---

## Post #147 by @Mate_Toth (2023-02-12 16:27 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Hi András, first thank you for your help here in this thread, it is very useful for many of us.</p>
<p>I would have a question, because I have read the topic and the others you used to link for this type of questions ( <a href="https://github.com/SlicerHeart/SlicerHeart#ge" rel="noopener nofollow ugc">SlicerHeart</a>, <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/ImageImportExport.md#importing-dicom-files" rel="noopener nofollow ugc">import export</a> ) but I’m still unable to import my .vol files from a GE ultrasound.<br>
They are not compressed and I use the Heart extension, and I saved the files with the GE 4D view tool as well (Wavelet compression" set to None).<br>
Could you please <a href="https://drive.google.com/file/d/1aahFqPFmLWfUKPlYfagHcNvEbxXQ9fkz/view?usp=share_link" rel="noopener nofollow ugc">take a look on it?</a></p>
<p>thank you!</p>
<p>Máté</p>

---

## Post #148 by @Jordi_Ysard (2023-03-07 14:51 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> . Thanks for all the help provided in this thread. It’s really been an awesome source of information to try to visualize .vol data in slicer3D.</p>
<p>However, I haven’t ben able to find an answer to the question I still have.</p>
<p>GE Voluson S8 (the machine I’m working with) allows me to export in 2 types of .vol format, cartesian and non-cartessian. When I download the cartesian file, I only find 1 of the 56 volumes recorded in that 4D ultrasound session. I don’t know for sure which of the 56 “frames” it corresponds, to, but in any case, it is not the “frame” I’d like.</p>
<p>I’ve been exporting data in any format possible, and I only managed to find that non-cartesian .vol files seem to have different sizes for different 4D “videos”. Would my guess be right in assuming that the non-cartesian .vol file contains every frame? in that case, how can I save the file so that it is not compressed?</p>
<p>Trying to delve into the code for reading .vols, I found that for polar .vol files, you still expect the data to be in tag xD000, but I find my data on xD700 instead, and not in an easy to read/interpret format.</p>
<p>Would you have any hints (coding or not coding) that could help me read frame  <span class="hashtag">#30</span>? Can I do anything to export a cartesian .vol with a specific frame that I care about?</p>
<p>Thanks!</p>

---

## Post #149 by @MartinNA (2023-06-17 00:04 UTC)

<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/scl/fo/amkkyaavt3jmpcrbavf67/h?dl=0&amp;rlkey=h64e5zgxtjq65xptwihvdxtqc">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon-vfl8lUR9B.ico" class="site-icon" width="32" height="32">

      <a href="https://www.dropbox.com/scl/fo/amkkyaavt3jmpcrbavf67/h?dl=0&amp;rlkey=h64e5zgxtjq65xptwihvdxtqc" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/362;"><img src="https://www.dropbox.com/static/metaserver/static/images/opengraph/opengraph-content-icon-folder-dropbox-landscape.png" class="thumbnail" width="690" height="362"></div>

<h3><a href="https://www.dropbox.com/scl/fo/amkkyaavt3jmpcrbavf67/h?dl=0&amp;rlkey=h64e5zgxtjq65xptwihvdxtqc" target="_blank" rel="noopener nofollow ugc">Doctor_Retana</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Hi<br>
I have a similar problem, I have .vol files from a voluson S8 ultrasound, the doctor gave me the files via USB, when I pass them to slicer an error appears and that it cannot load them. I don’t know if anyone has had the same problem and how do I solve it.</p>

---

## Post #150 by @AldairPadilla (2023-11-29 02:45 UTC)

<p>Hi everyone. Let me tell you my problem and i wish someone could help me, i appreciate a lot. <img src="https://emoji.discourse-cdn.com/twitter/smiling_face_with_tear.png?v=12" title=":smiling_face_with_tear:" class="emoji" alt=":smiling_face_with_tear:" loading="lazy" width="20" height="20"></p>
<p>I’m Aldair Padilla and a few months ago my couple and I received the news that we will be parents. We are so happy because of that. <img src="https://emoji.discourse-cdn.com/twitter/smiling_face.png?v=12" title=":smiling_face:" class="emoji" alt=":smiling_face:" loading="lazy" width="20" height="20"> Well i’m an engineer and i know about 3d printers because i have a two of this machines, and i really want to print the face fof my baby. <img src="https://emoji.discourse-cdn.com/twitter/heart_eyes.png?v=12" title=":heart_eyes:" class="emoji" alt=":heart_eyes:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/heart_eyes.png?v=12" title=":heart_eyes:" class="emoji" alt=":heart_eyes:" loading="lazy" width="20" height="20"></p>
<p>A few days ago we receive the .Vol file from the doctor, i download a lot of softwares like rhinoceros, babyslice, 3dslicer, etc… but I couldn’t open the file to modify it and later print it in 3D.  <img src="https://emoji.discourse-cdn.com/twitter/sneezing_face.png?v=12" title=":sneezing_face:" class="emoji" alt=":sneezing_face:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/disappointed_relieved.png?v=12" title=":disappointed_relieved:" class="emoji" alt=":disappointed_relieved:" loading="lazy" width="20" height="20"></p>
<p>I was hoping to surprise my couple with 3D printing of the face from our baby. i add the files and i really wish someone could help me to convert the file in some format that i could edit. But if someone could convert them in .STL, .OBJ, or any format that i can use to print I would really apreciate it, and if you need a pay for that job i’m pay it i just want to print my baby face. I add the link to get the .vol files <img src="https://emoji.discourse-cdn.com/twitter/heart_eyes.png?v=12" title=":heart_eyes:" class="emoji" alt=":heart_eyes:" loading="lazy" width="20" height="20"></p>
<p><a href="https://www.dropbox.com/scl/fo/l01c88d6le9v00g2q3y9e/h?rlkey=ic3s6xsggfsfu1dbv3a4dl24l&amp;dl=0" rel="noopener nofollow ugc">UltraSound baby</a></p>

---
