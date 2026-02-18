# Web application based on vtk.js

**Topic ID**: 15725
**Date**: 2021-01-28
**URL**: https://discourse.slicer.org/t/web-application-based-on-vtk-js/15725

---

## Post #1 by @spycolyf (2021-01-28 22:00 UTC)

<p>This is really cool…</p>
<div class="youtube-onebox lazy-video-container" data-video-id="8ZIxNuMIj9g" data-video-title="Web application - Medical image (CT) 3D visualization" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=8ZIxNuMIj9g" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/8ZIxNuMIj9g/maxresdefault.jpg" title="Web application - Medical image (CT) 3D visualization" width="" height="">
  </a>
</div>


---

## Post #2 by @jcfr (2021-01-28 22:10 UTC)

<p>The application illustrated on the video was developed by integrating <a href="https://kitware.github.io/vtk-js/index.html">vtk.js</a>  like it was done in the <a href="https://kitware.github.io/paraview-glance/app/" class="inline-onebox">ParaView Glance</a> application.</p>
<p>cc: <a class="mention" href="/u/forrest.li">@forrest.li</a></p>

---

## Post #3 by @lassoan (2021-01-29 01:15 UTC)

<p>Yes, although web viewers are still extremely limited compared to what you can do on desktop, there are many applications for that they are sufficient. They can be also used for patient browsing, quick preview, and launch desktop app on the selected data set. We work together with OHIF, dcmjs, etc. communities to make sure there is good synergy between desktop/web/server backend.</p>

---

## Post #4 by @chir.set (2021-01-29 07:41 UTC)

<p>Just one remark.</p>
<p>The application in the video runs on localhost and everything is smooth.</p>
<p>In the health center here, there’s one such web based application (Zero FootPrint) that allows to list patient exams, view slices , see volume rendered views and much more. It’s on a 1Gb/s LAN and despite that, it’s not as useful as running a desktop application. The bottleneck is network lag, and there’s not much to do about it.</p>
<p>How much work should developers be doing in this direction ?</p>
<p>Regards.</p>

---

## Post #5 by @lassoan (2021-01-29 15:43 UTC)

<p>There is clearly a trend to run more and more software in the browser. The more complicated question is where to do the processing.</p>
<p>For simple visualization of small data sets (patient browser, smaller images, etc.) local rendering/processing is easily doable and since it runs locally it is smooth and fast.</p>
<p>For larger data sets, network transfer time becomes a major hurdle, and complex visualizations and processing are still much harder to achieve using web technologies. For these cases, server-side processing and remote desktop access (or at least remote rendering) makes more sense. An example is the zero-foot-print viewer mentioned above, which is a desktop application (similar to Slicer) accessed via remote desktop. Network latency plays a somewhat different role in this case - it just makes everything a bit laggy.</p>
<p>Work is being done in both aspects:</p>
<ol>
<li>We collaborate with web developers on playing nicely with their tools (e.g., run Slicer on the cloud, integrating it with OHIF viewer, Kheops, ePad, etc. via DICOMweb, docker containers, etc.).</li>
<li>We make Slicer available in the browser - there are multiple docker containers that can be started on a server and allow you to run Slicer in the web browser. See this <a href="https://mybinder.org/v2/gh/Slicer/SlicerNotebooks/master?filepath=SlicerWeb.ipynb">example</a> of a Slicer instance that you can run in your web browser right now. It uses the free “binder” service, so it may take 1-2 minutes to start up and processing speed mediocre, but if you pay to a cloud service provider then you can get instantaneous startup and supercomputer performance.</li>
</ol>

---
