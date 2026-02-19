---
topic_id: 9310
title: "New Free Video Tutorials Vtk Js And Ohif Web Apps"
date: 2019-11-27
url: https://discourse.slicer.org/t/9310
---

# New free video tutorials! VTK.js and OHIF web apps

**Topic ID**: 9310
**Date**: 2019-11-27
**URL**: https://discourse.slicer.org/t/new-free-video-tutorials-vtk-js-and-ohif-web-apps/9310

---

## Post #1 by @pieper (2019-11-27 14:41 UTC)

<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://discourse.vtk.org/uploads/default/optimized/1X/6c8eb860cf266ca35755a0f95e95251fbe63514d_2_32x32.png" class="site-icon" width="16" height="16">
      <a href="https://discourse.vtk.org/t/new-free-video-tutorials-vtk-js-and-ohif-web-apps/2164" target="_blank" title="02:39PM - 27 November 2019">VTK – 27 Nov 19</a>
  </header>
  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:120/37;"><img src="https://discourse.vtk.org/uploads/default/original/2X/7/7a669abaef771a66f7d0807ddb00089f8d9a5c6c.png" class="thumbnail"></div>

<h3><a href="https://discourse.vtk.org/t/new-free-video-tutorials-vtk-js-and-ohif-web-apps/2164" target="_blank">New free video tutorials! VTK.js and OHIF web apps</a></h3>

<p>What: The Open Health Imaging Foundation (OHIF) and Kitware have teamed up to help you create amazing 3D zero-footprint medical imaging web applications using state-of-the-art open- source software. Did we mention it’s totally free and commercially...</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #2 by @tbillah (2019-11-27 15:06 UTC)

<p>Hi Steve, can you provide adress of “HIF exhibit in the Learning Center (IN019-EC-TUA)”?</p>

---

## Post #3 by @pieper (2019-11-27 16:08 UTC)

<p>Hi Tashrif - that refers to a booth at <a href="https://rsna2019.rsna.org/">RSNA in Chicago</a> next week, in case anyone is in town for that and wants to meet face to face.</p>

---

## Post #4 by @Umesh_Persad (2019-11-30 13:54 UTC)

<p>Thanks Steve, this looks very useful. Say I wanted to build a custom 3D reconstruction web app using medical images for 3D printing etc., would OHIF and VTK.js be the best options for the front end or are there other good contenders? What about good options for back end processing?</p>

---

## Post #5 by @pieper (2019-11-30 15:17 UTC)

<p>There are some other very good options to consider, and there are always new developments to keep any eye on, but at least for the projects I’m working on we have settled on the OHIF and VTK.js approach described in the tutorials.  OHIF itself is modular, so the viewports can be rendered by other frameworks, like Cornerstone and OpenLayers.  We may also end up using threejs/aframe.  There’s also XTK and AMI and no doubt others I’m not thinking of right now.</p>
<p>For the medical imaging back end there are several good DICOMweb servers in various languages, and Google offers DICOMweb as a service, so for the data side of things that’s a logical choice.</p>
<p>For server-side processing I personally use Slicer on cloud VMs so that we can leverage the same codebase for desktop and cloud/web scenarios.</p>
<p>These are all works in progress of course.  Hope to have some more concrete worked out examples soon.</p>

---

## Post #6 by @lassoan (2019-11-30 15:28 UTC)

<p>We are also exploring using Slicer as front-end (launched from OHIF viewer) for more sophisticated visualization and processing, such as segmentation, and processing large data sets without transferring to the user’s computer. See this topic for some more information and updates about the progress: <a href="https://discourse.slicer.org/t/can-3d-slicer-be-hosted-on-a-rendering-server/9256/8" class="inline-onebox">Can 3D Slicer be hosted on a rendering server?</a></p>

---

## Post #7 by @Umesh_Persad (2019-11-30 19:35 UTC)

<p>Great, thanks for the pointers. Where do you see the future of 3D medical imaging going - more toward the cloud and software as a service or there will always be a place for desktop software like 3D Slicer? This is specifically for automated medical image processing.</p>

---

## Post #8 by @Umesh_Persad (2019-11-30 19:37 UTC)

<p>Looks interesting and I will follow it closely.</p>

---

## Post #9 by @lassoan (2019-11-30 21:25 UTC)

<aside class="quote no-group" data-username="Umesh_Persad" data-post="7" data-topic="9310">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/umesh_persad/48/4719_2.png" class="avatar"> Umesh_Persad:</div>
<blockquote>
<p>or there will always be a place for desktop software like 3D Slicer?</p>
</blockquote>
</aside>
<p>Most resource-intensive professional software are running as native applications (desktop and mobile) and this will not likely to go away.</p>
<p>Most simple, non-resource-intensive applications can be implemented as web apps with their frontend running completely in the browser. This does not seem to go away either.</p>
<p>These approaches are already mixing with each other and various interfaces are being built between them - desktop applications often embed web browsers, web applications rely on remote rendering by native applications (even for latency-critical applications, such as games - see Google Stadia), app stores make installations easier and may allow running native applications downloaded directly from a website (without users permanently installing it).</p>
<p>If any application wants to remain relevant then it has to make sure it can be used in various environments and connected to a wide range of services and applications.</p>
<p>There are a few more tricks that Slicer needs to learn but its current state is already not too bad: it runs in docker, can be streamed to a browser using VNC, runs as Jupyter kernel, has embedded web browser, there are experimental projects that make Slicer provide web services, there is coordination with web GUI (OHIF/Cornerstone) and server (Girder, XNAT) folks, etc. - and it’s just keep getting better.</p>

---

## Post #10 by @pieper (2019-11-30 22:30 UTC)

<p>I agree with everything <a class="mention" href="/u/lassoan">@lassoan</a> said, we are in a pretty interesting time, with new options to make convenient and powerful computing and visualization software.  It’s really good that there is so much open software on all these fronts.  To me, standards-based interoperability is the key, which is why I keep focusing on DICOMweb, SEG, SR, and related standards in javascript, python and c++.  That way we can keep using the hardware and software that best suits our needs (e.g. Slicer as a processing environment).</p>
<p>I do think there will be a lot of cases where cloud processing and rendering will make the most sense.  Like in <a href="https://www.youtube.com/watch?v=oHZBFm02wbM">this video</a> where the data volume is 16G.  I could barely render that data on a state of the art laptop after a long download, but it works nicely on a big cloud hosted GPU.</p>

---

## Post #11 by @Umesh_Persad (2019-12-01 09:11 UTC)

<p>Great. Slicer as a platform for research is ideal if it enables prototyping locally and deployment to both native and web services.</p>

---

## Post #12 by @Umesh_Persad (2019-12-01 09:15 UTC)

<p>Couldn’t agree more on the standards and interoperability. One area I’ve been looking at is the use of 3D reconstruction and printing via Implicit Functions. For example, nTopology is a field based CAD tool (<a href="https://ntopology.com/" rel="nofollow noopener">https://ntopology.com/</a>), and creating .stl files could be skipped entirely because the implicit models could be sliced directly for 3D printing shortening the workflow while reducing the data requirements. Seems like an interesting direction to go in.</p>

---

## Post #13 by @Gaurav_Gupta (2020-06-12 19:20 UTC)

<p>can someone help with vtk.js and react-vtkjs-components?<br>
Due to lack of API documentation, I am having trouble setting origin and direction for LabelMap in vtk.js<br>
Please see this short video:</p><div class="youtube-onebox lazy-video-container" data-video-id="jQNOye3iB0I" data-video-title="Welcome to TD" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=jQNOye3iB0I" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/jQNOye3iB0I/maxresdefault.jpg" title="Welcome to TD" width="" height="">
  </a>
</div>


---

## Post #14 by @pieper (2020-06-12 20:12 UTC)

<p>The <a href="https://github.com/OHIF/Viewers/tree/master/extensions/vtk">vtk extension in OHIF</a> has labelmap in volume-based reslicing worked out.  There’s also <a href="https://github.com/dcmjs-org/dcmjs-examples/tree/master/vtkDisplay">this example in dcmjs</a>.</p>
<p><a class="mention" href="/u/gaurav_gupta">@Gaurav_Gupta</a> is your project open source?</p>

---

## Post #15 by @Gaurav_Gupta (2020-06-12 20:34 UTC)

<p>Steve, as of now it is only exploratory project. I am trying to understand capabilities &amp; limitations of react-vtkjs-components. Would you know if HU threshold based segmentation with multiple colors is functional in react-vtkjs-components?</p>

---

## Post #16 by @pieper (2020-06-12 22:56 UTC)

<aside class="quote no-group" data-username="Gaurav_Gupta" data-post="15" data-topic="9310">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gaurav_gupta/48/5944_2.png" class="avatar"> Gaurav_Gupta:</div>
<blockquote>
<p>Would you know if HU threshold based segmentation with multiple colors is functional in react-vtkjs-components?</p>
</blockquote>
</aside>
<p>No, I don’t know about that.</p>

---

## Post #17 by @Marko_Nikovic (2021-02-03 14:25 UTC)

<p>Hello <a class="mention" href="/u/gaurav_gupta">@Gaurav_Gupta</a><br>
I am using react-vtkjs-veiwport module in my react app.<br>
I set webpack as this requirement(<a href="https://kitware.github.io/vtk-js/docs/intro_vtk_as_es6_dependency.html" class="inline-onebox" rel="noopener nofollow ugc">Using vtk.js as an ES6 dependency | vtk.js</a>)<br>
<a href="https://discourse.vtk.org/t/i-want-to-add-2-features-of-vtkjs-library-to-my-reactjs-project/5082" class="inline-onebox" rel="noopener nofollow ugc">I want to add 2 features of vtkjs library to my Reactjs project - Web - VTK</a><br>
But I have error like above url, so I am not this module now.<br>
I hope you help me.<br>
Thank you in advance</p>

---
