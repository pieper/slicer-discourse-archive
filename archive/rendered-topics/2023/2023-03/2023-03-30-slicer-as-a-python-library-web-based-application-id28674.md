# Slicer as a python library / web based application?

**Topic ID**: 28674
**Date**: 2023-03-30
**URL**: https://discourse.slicer.org/t/slicer-as-a-python-library-web-based-application/28674

---

## Post #1 by @NaglisR (2023-03-30 08:02 UTC)

<p>Hello,</p>
<p>I want to ask if there are any plans at any point to create Slicer as a full python package or a web based application, which would not require/reference a separate slicer executable application.</p>
<p>Currently to my knowledge the closest match is slicerio/slicer web server which allows to execute commands from python, howere it requires the slicer executable app.<br>
Are there any plans to make Slicer as a web based app/viewer, similar to <a href="https://github.com/niivue/niivue" class="inline-onebox" rel="noopener nofollow ugc">GitHub - niivue/niivue: a WebGL2 based medical image viewer. Supports over 30 formats of volumes and meshes.</a> for example? Such functionality would allow to implement slicer UI window viewing in external UIs in which different windows would display different studies for multiple parallel users.</p>
<p>Basically to have multiple subsequent interactive windows like this in a single page.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/2176bab0459e4247ea38b27b3caca9577d5b382b.png" data-download-href="/uploads/short-url/4M28enSjpV41wy3ZrzzLJn2ykAP.png?dl=1" title="Screenshot from 2023-03-30 10-43-52" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/2176bab0459e4247ea38b27b3caca9577d5b382b_2_625x500.png" alt="Screenshot from 2023-03-30 10-43-52" data-base62-sha1="4M28enSjpV41wy3ZrzzLJn2ykAP" width="625" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/2176bab0459e4247ea38b27b3caca9577d5b382b_2_625x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/2176bab0459e4247ea38b27b3caca9577d5b382b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/2176bab0459e4247ea38b27b3caca9577d5b382b.png 2x" data-dominant-color="1D1B1A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2023-03-30 10-43-52</span><span class="informations">750×600 110 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2023-03-30 14:33 UTC)

<p>Slicer is focused on being a workstation or server application.  For web app use cases we tend to use OHIF, and some of us work on both projects so interoperability should be pretty good via dicom objects.</p>
<p>Separately we are thinking of factoring out some of Slicer into python packages that could be used in other ways, but it’s a complex process that will take time.</p>

---

## Post #3 by @NaglisR (2023-03-31 12:19 UTC)

<p>Understood, that makes sense.<br>
What I currently find lacking is a good web app for nifti file display/manipulation. There are some lightweight DICOM viewers such as OHIF, but they only load DICOMS, not nifti files.<br>
Then there are some nifti file viewers (such as niivue and a few others), but as far as I’ve seen all are either no longer maintained or lack some important features or efficiency/optimization.<br>
Slicer user interface for nifti file display/manipulation is the best that I know of and if it was available as a web app that would be optimal. However I fully understand that these are two very different use cases and tracks, so it makes sense to focus on server application.</p>
<p>Thanks!</p>

---

## Post #4 by @pieper (2023-03-31 13:50 UTC)

<p>I know nifti support comes up in the OHIF world from time to time and probably a solution is forthcoming.  Right now I suppose anything is possible with enough coding effort but it’s not clear there’s something out of the box that does exactly what you have in mind.</p>

---

## Post #5 by @muratmaga (2023-03-31 14:29 UTC)

<p>Did you try the glance viewer from kitware?</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://kitware.github.io/glance/index.html">
  <header class="source">
      <img src="https://kitware.github.io/glance/icon/favicon-196x196.png" class="site-icon" width="" height="">

      <a href="https://kitware.github.io/glance/index.html" target="_blank" rel="noopener" title="08:36PM - 23 January 2023">Glance – 23 Jan 23</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://kitware.github.io/glance/index.html" target="_blank" rel="noopener">Glance</a></h3>

  <p>Kitware Glance - your data viewer for the Web</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @Sam_Horvath (2023-03-31 14:33 UTC)

<p>Also, <a href="https://volview.netlify.app/">VolView</a> should work with non-DICOM (just tested)</p>

---

## Post #7 by @Sam_Horvath (2023-03-31 14:36 UTC)

<p>CTChest from the Slicer sample data in <a href="https://volview.netlify.app/">VolView</a>:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/9633b421699826c1fef3cd4e14a55d7330c7ef51.jpeg" data-download-href="/uploads/short-url/lqKouJZdwmbBzprwPpw5vHUYOkN.jpeg?dl=1" title="Screenshot 2023-03-31 10.35.12"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/9633b421699826c1fef3cd4e14a55d7330c7ef51_2_690x283.jpeg" alt="Screenshot 2023-03-31 10.35.12" data-base62-sha1="lqKouJZdwmbBzprwPpw5vHUYOkN" width="690" height="283" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/9633b421699826c1fef3cd4e14a55d7330c7ef51_2_690x283.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/9633b421699826c1fef3cd4e14a55d7330c7ef51_2_1035x424.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/9633b421699826c1fef3cd4e14a55d7330c7ef51_2_1380x566.jpeg 2x" data-dominant-color="2A292A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-03-31 10.35.12</span><span class="informations">1920×788 48.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @NaglisR (2023-04-03 10:58 UTC)

<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> I have tried VolView (as Osimis Orthanc plugin), it is quite nice, but still lacks some very relevant features (as far as I’ve managed to explore, let me know if there is something I have missed):</p>
<ol>
<li>Ability to display a study with overlayed 3D annotations. An equivalent in Slicer would be loading a study nifti file and a Segmentation-label.nii or Segmentation.seg.nrrd file which would contain 3d overlays/annotations and load the study with overlays. As far as I’ve seen VolView only supports 2D annotations.</li>
<li>An available executive API endpoint which would allow other applications to send commands to VolView, for example to open and display a specific study. I’ve seen there is a way to general a URL which would open a specific study from URL, however I have not found if this allows to load multiple nifti files from disk. An equivalent in Slicer is the web server with EXEC endpoint which allows not only to send commands to load but also manipulate studies via requests.</li>
</ol>

---

## Post #9 by @forrest.li (2023-04-03 14:47 UTC)

<p>Hi <a class="mention" href="/u/naglisr">@NaglisR</a>, thanks for your feedback on VolView! I can address your two points.</p>
<ol>
<li>Rendering 3D annotations is in progress! I don’t have a timeline for it, since it’s not a priority right now.</li>
<li>This is an interesting idea. The closest thing to a control endpoint in VolView is this PR that integrates a python server as a backend service: <a href="https://github.com/Kitware/VolView/pull/272" class="inline-onebox" rel="noopener nofollow ugc">Python server demo by floryst · Pull Request #272 · Kitware/VolView · GitHub</a>. Since it’s not possible to run an accessible webserver in the browser, you’d have to run a python server that acts as the control node for VolView.</li>
</ol>

---

## Post #10 by @lassoan (2023-04-03 15:08 UTC)

<p><a class="mention" href="/u/naglisr">@NaglisR</a> Note that you actually don’t need a web client for image review. You can open Slicer directly from a website where you host your data, have very fast and sophisticated viewing and editing features, and then save the results to the remote database, when the user finished processing. You need to install a local application, which may be an extra step, but if your users spend significant time with image review and annotation then the inconvenience of installing a local application may be negligible.</p>
<p>For example, a group has set up a MONAILabel server in their hospital with some added features for authenticating users and adding more metadata (ability to flag segmentations for expert review, etc.) and they used locally installed 3D Slicer as frontend. They utilized MONAILabel to continuously retrain the model and select those images for manual segmentation that MONAILabel was the most uncertain about how to segment.</p>

---

## Post #11 by @pieper (2023-04-03 15:38 UTC)

<p>And if you really don’t want to install anything on the client machine, you can run Slicer itself on a cloud instance.</p>
<p>Either on <a href="https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/SlicerCloud/">AWS</a> or <a href="https://learn.canceridc.dev/cookbook/virtual-machines/idc-desktop">GCP</a> or really anywhere that rents VMs.</p>
<p>I’ve come to like this model because you don’t have the limitations imposed by the browser.  It’s not a replacement for web applications, but it covers a lot of interesting cases (like being highly scalable) and means we don’t always need to reimplement everything in javascript if we don’t want to.</p>

---

## Post #12 by @jcfr (2023-04-18 14:29 UTC)

<aside class="quote no-group" data-username="NaglisR" data-post="8" data-topic="28674">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/naglisr/48/16280_2.png" class="avatar"> NaglisR:</div>
<blockquote>
<p>I have tried VolView (as Osimis Orthanc plugin)</p>
</blockquote>
</aside>
<p>To follow up on that specific topic, VolView has been officially integrated with Orthanc.</p>
<p>You may read more details <a href="https://www.linkedin.com/feed/update/urn:li:activity:7054043886259736576/">here</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b6311f2f7acb57a478c6f3220c28813d2604f8c.jpeg" data-download-href="/uploads/short-url/fjZlsjYXcqz3jlG4DkqcCC6SV9a.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b6311f2f7acb57a478c6f3220c28813d2604f8c_2_517x283.jpeg" alt="image" data-base62-sha1="fjZlsjYXcqz3jlG4DkqcCC6SV9a" width="517" height="283" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b6311f2f7acb57a478c6f3220c28813d2604f8c_2_517x283.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b6311f2f7acb57a478c6f3220c28813d2604f8c_2_775x424.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b6311f2f7acb57a478c6f3220c28813d2604f8c_2_1034x566.jpeg 2x" data-dominant-color="848380"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1600×877 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote no-group" data-username="forrest.li" data-post="9" data-topic="28674">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/forrest.li/48/13557_2.png" class="avatar"> forrest.li:</div>
<blockquote>
<ul>
<li>Rendering 3D annotations is in progress! I don’t have a timeline for it, since it’s not a priority right now.</li>
<li>This is an interesting idea. The closest thing to a control endpoint in VolView is this PR that integrates a python server as a backend service: <a href="https://github.com/Kitware/VolView/pull/272">Python server demo by floryst · Pull Request #272 · Kitware/VolView · GitHub </a>. Since it’s not possible to run an accessible webserver in the browser, you’d have to run a python server that acts as the control node for VolView.</li>
</ul>
</blockquote>
</aside>
<p>Exciting to see progress on that front <img src="https://emoji.discourse-cdn.com/twitter/rocket.png?v=12" title=":rocket:" class="emoji" alt=":rocket:" loading="lazy" width="20" height="20"></p>

---
