# Fiducials configuration for spatial calibration with no streaming of 'StylusToProbe' transform

**Topic ID**: 13326
**Date**: 2020-09-03
**URL**: https://discourse.slicer.org/t/fiducials-configuration-for-spatial-calibration-with-no-streaming-of-stylustoprobe-transform/13326

---

## Post #1 by @AurelieS (2020-09-03 15:57 UTC)

<p>Hi (again…),</p>
<p>I am sorry for all the topics, 3D ultrasound is quite new for me and some aspects are still blurry…</p>
<p>I followed your tutorial U31 for spatial calibration of my ultrasound probe.<br>
The problem is that the internally computing of the ‘StylusToProbe’ transform from ‘StylusToTracker’ and ‘ProbeToTracker’ by Plus is using too much RAM of our computer and the tracking lags.</p>
<p>I am therefore trying to perform this calibration by streaming only ‘StylusToTracker’ and ‘ProbeToTracker’ to Slicer3D. Is it possible ?<br>
My hierarchy is the following :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53f655539f5843a253889e8c028119161ade326c.png" data-download-href="/uploads/short-url/bYLoB0qHPS7RlfcEpyjoqihTApS.png?dl=1" title="Image1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53f655539f5843a253889e8c028119161ade326c_2_536x500.png" alt="Image1" data-base62-sha1="bYLoB0qHPS7RlfcEpyjoqihTApS" width="536" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53f655539f5843a253889e8c028119161ade326c_2_536x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53f655539f5843a253889e8c028119161ade326c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53f655539f5843a253889e8c028119161ade326c.png 2x" data-dominant-color="F2F5F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Image1</span><span class="informations">610×569 64 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I want to create ‘ImageToProbe’ transform to insert it to ‘ProbeToTracker’ and then be able to follow my ultrasound image in the 3D view.</p>
<p>So if I follow exactly the tutorial U31, the ‘ImageToProbe’ will not be the right one since my StylusTipToStylus is not in the Probe Reference ? The Fiducial Registration Wizard configuration in the U31 is the following :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d29906eca91f4d8da5a81c2c3975b76791c3ba02.png" data-download-href="/uploads/short-url/u327V0A7RYzCR3k7m08VZkc2qjg.png?dl=1" title="Image2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d29906eca91f4d8da5a81c2c3975b76791c3ba02_2_315x500.png" alt="Image2" data-base62-sha1="u327V0A7RYzCR3k7m08VZkc2qjg" width="315" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d29906eca91f4d8da5a81c2c3975b76791c3ba02_2_315x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d29906eca91f4d8da5a81c2c3975b76791c3ba02_2_472x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d29906eca91f4d8da5a81c2c3975b76791c3ba02_2_630x1000.png 2x" data-dominant-color="F2F5F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Image2</span><span class="informations">697×1105 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Doing that I feel that the transform I am creating is the ImageToTracker transform (since StylusTip is in the Stylus reference which is in the Tracker reference) ? am I right ?<br>
I do not know how to configure the Fiducial Registration Wizard to be able to create the ‘ImageToProbe’ with my configuration…</p>
<p>Thanks in advance for all of your help, your software and libraries are very powerful and we are very glad in our biomechanics lab to set it up, even if it takes some time …</p>

---

## Post #2 by @lassoan (2020-09-03 16:32 UTC)

<aside class="quote no-group" data-username="AurelieS" data-post="1" data-topic="13326">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/87869e/48.png" class="avatar"> AurelieS:</div>
<blockquote>
<p>The problem is that the internally computing of the ‘StylusToProbe’ transform from ‘StylusToTracker’ and ‘ProbeToTracker’ by Plus is using too much RAM of our computer and the tracking lags</p>
</blockquote>
</aside>
<p>Pivot calibration computation is trivial and does not require any extra RAM. Can you describe what configuration change you make exactly that slows things down?</p>
<aside class="quote no-group" data-username="AurelieS" data-post="1" data-topic="13326">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/87869e/48.png" class="avatar"> AurelieS:</div>
<blockquote>
<p>I am therefore trying to perform this calibration by streaming only ‘StylusToTracker’ and ‘ProbeToTracker’ to Slicer3D. Is it possible ?</p>
</blockquote>
</aside>
<p>If you don’t move the stylus tip relative to the tracker then you only need a single transformation stream for pivot calibration: StylusToTracker.</p>
<p>I would recommend to start with following the calibration tutorial exactly. If you have trouble completing any of the steps then let us know.</p>

---

## Post #3 by @AurelieS (2020-09-04 11:28 UTC)

<p>I am talking about ‘Spatial calibration’, not ‘pivot calibration’ (which I succeeded in doing and verified the transform matrix was OK).</p>
<p>The problem is that when I stream from PlusServer: ‘ProbeToTracker’ + ‘StylusToTracker’ + ‘StylusToProbe’, the tracking is lagging. I wanted to have the three of them to be able to visualize my Stylus and Probe independently moving in the Tracker frame.<br>
However if I stream only ‘StylusToProbe’ for the spatial calibration, as explained in the tutorial, then it worked fine, and the tracking was not lagging. So for spatial calibration I will use a config file that is only streaming ‘StylusToProbe’.</p>
<p>I now would like to visualise my tracked ultrasound and verify that all is OK with my transform ImageToProbe.</p>
<p>So this time I use a config file which is streaming ‘ProbeToTracker’ and ‘StylusToTracker’ (I want to stream the stylus tracking, to use it to verify the location of my ultrasound image in the 3D view, see below). Then, I uploaded the previously calculated ‘StylusTipToStylus’ and ‘ImageToProbe’ transforms.</p>
<p>If I follow the tutorial U32, which is a bit different from my case since I stream ‘Image_image’ and not ‘image_reference’ (according to recommendations from your team in a previous post), I tried using the following hierarchy :<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75859e9c71f6f863c21f3af9ded031b2298596c2.png" alt="Capture" data-base62-sha1="gLE8Qo6bDorx8OBHWuAxeAG5azE" width="346" height="200"><br>
Do you confirm my hierarchy is correct ?</p>
<p>Then I followed the tutorial to display the ultrasound image in the 3D view :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/79842cf7991531038f9edf875e69e3afbd1386f5.png" data-download-href="/uploads/short-url/hkYXsdOxPjVhlzvRtlDXJXbypr7.png?dl=1" title="Capture2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79842cf7991531038f9edf875e69e3afbd1386f5_2_673x500.png" alt="Capture2" data-base62-sha1="hkYXsdOxPjVhlzvRtlDXJXbypr7" width="673" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79842cf7991531038f9edf875e69e3afbd1386f5_2_673x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/79842cf7991531038f9edf875e69e3afbd1386f5.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/79842cf7991531038f9edf875e69e3afbd1386f5.png 2x" data-dominant-color="9295CC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture2</span><span class="informations">708×526 6.93 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The ultrasound image is displayed but if I put the StylusTip (represented by the needle model) in the plane of the ultrasound image, you can see that it is not at all in the image displayed, and even quite far …<br>
Is it an ‘ImageToProbe’ transform problem ?</p>

---

## Post #4 by @AurelieS (2020-09-22 16:29 UTC)

<p>I found the problem, my Stylus geometry was not correct (3D printed in the office, I attached the marker plane not in the stylus plane) and therefore the StylusTipToStylus transform was incorrect (not taking into account the rotations) and therefore also my ImageToProbe transform…<br>
All is good now, with a correct Stylus I succeeded in scanning an object both live and with a recorded sequence !</p>

---

## Post #5 by @LoganWade (2020-10-23 11:07 UTC)

<p>I am having the same issues now. What stylus did you end up using? I am not sure why this would cause an issue as i thought the pivot calibration would account for differences between one stylus to the next?</p>

---

## Post #6 by @AurelieS (2020-10-23 13:06 UTC)

<p>Hi Logan,</p>
<p>Here is the stylus I am now using :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43e241bf60c9c67ed486cd56256587393e036604.jpeg" data-download-href="/uploads/short-url/9GwK69engIL1YUdn3DJOaKBr1UU.jpeg?dl=1" title="Stylus_MIPLab" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/43e241bf60c9c67ed486cd56256587393e036604_2_375x500.jpeg" alt="Stylus_MIPLab" data-base62-sha1="9GwK69engIL1YUdn3DJOaKBr1UU" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/43e241bf60c9c67ed486cd56256587393e036604_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/43e241bf60c9c67ed486cd56256587393e036604_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/43e241bf60c9c67ed486cd56256587393e036604_2_750x1000.jpeg 2x" data-dominant-color="C2BCB2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Stylus_MIPLab</span><span class="informations">3024×4032 1.9 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I uploaded my STL file here if you want to print a similar one :<br>
<a href="https://we.tl/t-kNYOXBvkIR" class="onebox" target="_blank" rel="noopener nofollow ugc">https://we.tl/t-kNYOXBvkIR</a></p>
<p>That way I made sure the plan of the markers was the same as the one from the needle tip. However I don’t know exactly why there was a problem with my first version, this one is working nicely !</p>
<p>Cheers,<br>
Aurélie</p>

---

## Post #7 by @jonortegav (2024-11-04 07:58 UTC)

<p>Hi <a class="mention" href="/u/aurelies">@AurelieS</a>,</p>
<p>Could you upload the STL file to somewhere else except wetransfer? I have no access to it and I think that using a similar stylus as yours would help me performing my ultrasound calibration.</p>
<p>Thank you !!</p>

---

## Post #8 by @AurelieS (2024-11-04 11:06 UTC)

<p>Hi,<br>
You can find all the 3DUS tutorials and the STL files on my github :</p><aside class="onebox githubrepo" data-onebox-src="https://github.com/AurelieSar/3Dultrasound">
  <header class="source">

      <a href="https://github.com/AurelieSar/3Dultrasound" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/fe7e295209cd006265c41c3c4084e11d/AurelieSar/3Dultrasound" class="thumbnail">

  <h3><a href="https://github.com/AurelieSar/3Dultrasound" target="_blank" rel="noopener nofollow ugc">GitHub - AurelieSar/3Dultrasound: Tutorial and resources for our 3D ultrasound...</a></h3>

    <p><span class="github-repo-description">Tutorial and resources for our 3D ultrasound system using 3D Slicer</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
Best regards,<br>
Aurélie</p>

---

## Post #9 by @jonortegav (2024-11-04 13:52 UTC)

<p>Thank you very much for your reply !</p>
<p>Jon</p>

---
