# How to load a .vol file of 4D ultrasound file

**Topic ID**: 11367
**Date**: 2020-04-30
**URL**: https://discourse.slicer.org/t/how-to-load-a-vol-file-of-4d-ultrasound-file/11367

---

## Post #1 by @samsonaie (2020-04-30 16:28 UTC)

<p>I like to upload a vol file of 4D ultrasound file within the file there are also blood flow. Wondering what should I do . thanks</p>

---

## Post #2 by @samsonaie (2020-04-30 16:37 UTC)

<p>Hi There,<br>
Attached is the file I try to load into slicer.<br>
would need someone to provide the process to load it in Slicer<br>
Thanks a lot.<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vflUeLeeY.ico" class="site-icon" width="16" height="16">
      <a href="https://www.dropbox.com/s/pyijsisj8ts70u6/heartHD%20Flow.vol?dl=0" target="_blank" rel="nofollow noopener">Dropbox</a>
  </header>
  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/images/spectrum-icons/generated/content/content-unknown-large.png" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://www.dropbox.com/s/pyijsisj8ts70u6/heartHD%20Flow.vol?dl=0" target="_blank" rel="nofollow noopener">heartHD Flow.vol</a></h3>

<p>Shared with Dropbox</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>I had successful loaded it in GE 4D view, however, It is static , not a 4D moving heart that I was told the heart volume was caught as 4D with blood flow. below is the video I caught as screenshoot of 4D view.<br>
          </p><div class="onebox video-onebox">
            <video width="100%" height="100%" controls="">
              <source src="https://dl.dropboxusercontent.com/s/397lj0niirbu7gz/heartHD-flow%20in%20GE%204D%20view.mp4?dl=0">
              <a href="https://dl.dropboxusercontent.com/s/397lj0niirbu7gz/heartHD-flow%20in%20GE%204D%20view.mp4?dl=0" rel="nofollow noopener">https://dl.dropboxusercontent.com/s/397lj0niirbu7gz/heartHD-flow%20in%20GE%204D%20view.mp4?dl=0</a>
            </source></video>
          </div>

<p>I would like to load it in Slicer !! thanks,</p>

---

## Post #3 by @lassoan (2020-04-30 19:27 UTC)

<p>You can load the ultrasound image without any problems (I’ve tested it with installing latest Slicer Preview Release and then SlicerHeart extension, then drag-and-dropping the .vol file to the application window; then setting up volume rendering for 3D view):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89bd672caca2bdac7f4c1821a190a2b6739256c2.jpeg" data-download-href="/uploads/short-url/jEvcRRPLK5QDii7Flcqd3ZdXrjA.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/89bd672caca2bdac7f4c1821a190a2b6739256c2_2_690x441.jpeg" alt="image" data-base62-sha1="jEvcRRPLK5QDii7Flcqd3ZdXrjA" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/89bd672caca2bdac7f4c1821a190a2b6739256c2_2_690x441.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/89bd672caca2bdac7f4c1821a190a2b6739256c2_2_1035x661.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/89bd672caca2bdac7f4c1821a190a2b6739256c2_2_1380x882.jpeg 2x" data-dominant-color="948D90"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2256×1444 591 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Currently, the importer currently does not load Doppler data, as I did not have such images when I implemented this. Maybe it would take just 1-2 days to add it, but right now there is no project that would fund this development.</p>

---

## Post #4 by @samsonaie (2020-05-01 03:09 UTC)

<p>thanks alot for your quick reponse.<br>
It is unfortuante that slicer can not illustrate Doppler data,yet.  Hope we can have it in the near future. <img src="https://emoji.discourse-cdn.com/twitter/love_you_gesture.png?v=12" title=":love_you_gesture:" class="emoji" alt=":love_you_gesture:" loading="lazy" width="20" height="20"></p>
<p>I have a following question : I am wondering  that the .vol file I sent is a 4D file.<br>
I went a bit further in GE 4D view, and found the .vol can be export to "4D img cine sequence " also see attached print screen.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/58eb790ebdef539236daeb29c5b0224a6d28d712.jpeg" data-download-href="/uploads/short-url/cGCvYqH8wCv9AUMlEwRguM7dKZc.jpeg?dl=1" title="3244607e673c2019009a9124519f7f2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/58eb790ebdef539236daeb29c5b0224a6d28d712_2_690x370.jpeg" alt="3244607e673c2019009a9124519f7f2" data-base62-sha1="cGCvYqH8wCv9AUMlEwRguM7dKZc" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/58eb790ebdef539236daeb29c5b0224a6d28d712_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/58eb790ebdef539236daeb29c5b0224a6d28d712_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/58eb790ebdef539236daeb29c5b0224a6d28d712_2_1380x740.jpeg 2x" data-dominant-color="3E3E3E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3244607e673c2019009a9124519f7f2</span><span class="informations">1486×797 224 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>and I export it to a AVI file, ( then convert to mp4 due to less file size). see below.</p>          <div class="onebox video-onebox">
            <video width="100%" height="100%" controls="">
              <source src="https://dl.dropboxusercontent.com/s/7hfysf92ulqlj1f/heartHD%20Flow.mp4?dl=0">
              <a href="https://dl.dropboxusercontent.com/s/7hfysf92ulqlj1f/heartHD%20Flow.mp4?dl=0" rel="noopener nofollow ugc">https://dl.dropboxusercontent.com/s/7hfysf92ulqlj1f/heartHD%20Flow.mp4?dl=0</a>
            </source></video>
          </div>

<p>It looks to me it is a volume rendering 4D ultrasound image,  am I right ?<br>
Can I also see 4D ultrasound image sequence in slicer ? how to do it</p>
<p>again， thanks a lot.</p>

---

## Post #5 by @lassoan (2020-05-01 05:13 UTC)

<aside class="quote no-group" data-username="samsonaie" data-post="4" data-topic="11367">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/d07c76/48.png" class="avatar"> samsonaie:</div>
<blockquote>
<p>Can I also see 4D ultrasound image sequence in slicer ? how to do it</p>
</blockquote>
</aside>
<p>Yes, but not from GE ultrasound systems. Unfortunately, most ultrasound imaging vendors prevent researchers to openly access 4D ultrasound data and none of them gives access to anything more than that (such as Doppler measurements or ECG signals). Some but not all vendors may let you access your data if you sign non-disclosure and/or research agreements with them. It is a shame, really, and hopefully vendors will eventually realize how much their behavior harms research. Tell your GE representatives that you need open access to your data - maybe they will listen if they hear this from many places.</p>

---

## Post #6 by @samsonaie (2020-05-01 10:10 UTC)

<p>Got it , I will pass the message to the GE rep.  I fully support the openness for research !</p>
<p>so, which ultrasound system can Slicer read their 4D ultrasound data ?<br>
I may be able to access. please advice , thanks a lot.</p>

---

## Post #7 by @lassoan (2020-05-01 13:39 UTC)

<p>Only Philips and Eigen Artemis support export of 4D images. See detailed description of what can be loaded from what vendor <a href="https://github.com/SlicerHeart/SlicerHeart#importing-dicom-files">here</a>.</p>

---
