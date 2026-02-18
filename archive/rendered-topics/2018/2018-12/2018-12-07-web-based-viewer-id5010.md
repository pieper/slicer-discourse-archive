# Web based viewer

**Topic ID**: 5010
**Date**: 2018-12-07
**URL**: https://discourse.slicer.org/t/web-based-viewer/5010

---

## Post #1 by @kayarre (2018-12-07 18:25 UTC)

<p>Hi I really think Slicer is great and use it a ton, it continues to get better and better.</p>
<p>I work with clinicians (often remotely) and as I am not a clinician I would like to provide them a way  to review a segmentation or model without editing stuff and have them login to a web portal remotely and view the information. From my experience with clinicians it needs to be very simple and not cluttered (distracting). Paraview has a nice client-server approach but it still requires downloading client, I guess there is paraviewWeb? which I haven’t tried.</p>
<p>The main thing would be able to have the traditional four up view with image data and the segmentation or model shown together on the image slices and  in 3D view. Markups would be a nice to have to record comments but not required.</p>
<p>Does something like this exist? Does anyone have a suggestion about how this might be done.</p>

---

## Post #2 by @jcfr (2018-12-08 07:22 UTC)

<h2><a name="p-18679-paraviewglance-1" class="anchor" href="#p-18679-paraviewglance-1" aria-label="Heading link"></a>ParaviewGlance</h2>
<aside class="quote no-group" data-username="kayarre" data-post="1" data-topic="5010">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/kayarre/48/3606_2.png" class="avatar"> kayarre:</div>
<blockquote>
<p>I guess there is paraviewWeb? which I haven’t tried.</p>
</blockquote>
</aside>
<p>There is now what we called <code>ParaviewGlance</code>,  you can give a try here: <a href="https://kitware.github.io/paraview-glance/">https://kitware.github.io/paraview-glance/</a></p>
<h3><a name="p-18679-what-is-paraviewglance-2" class="anchor" href="#p-18679-what-is-paraviewglance-2" aria-label="Heading link"></a>What is ParaviewGlance</h3>
<p>In  a nutshell, it is an example of client side web application built on top of <a href="https://kitware.github.io/vtk-js/">vtk.js</a> and <a href="https://insightsoftwareconsortium.github.io/itk-js/docs/index.html">itk.js</a> allowing to load and visualize datasets.  Both open-source under a permissive license.</p>
<p>Note that vtk.js has been built from the ground up to associated direction cosines with its image datastructure.</p>
<aside class="quote no-group" data-username="kayarre" data-post="1" data-topic="5010">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/kayarre/48/3606_2.png" class="avatar"> kayarre:</div>
<blockquote>
<p>Markups would be a nice to have to record comments but not required.</p>
</blockquote>
</aside>
<p>There is also a support for creating custom widget or annotation here is an example of <a href="https://kitware.github.io/vtk-js/examples/Box.html">box widget</a>.</p>
<h3><a name="p-18679-web-portal-integration-3" class="anchor" href="#p-18679-web-portal-integration-3" aria-label="Heading link"></a>web portal integration</h3>
<aside class="quote no-group" data-username="kayarre" data-post="1" data-topic="5010">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/kayarre/48/3606_2.png" class="avatar"> kayarre:</div>
<blockquote>
<p>would like to provide them a way to review a segmentation or model without editing stuff and have them login to a web portal remotely</p>
</blockquote>
</aside>
<p>Building on these components and integrating them with a data management system providing authentication/user management as well as REST API allows to implement  tailored  workflow.</p>
<p>An example of such data-management system supporting this would be Girder, see <a href="https://girder.readthedocs.io/en/stable/" class="inline-onebox">Girder: a data management platform — Girder 3.2.8 documentation</a>, but vtk.js and itk.js are agnostic to this particular system and could be integrated anywhere.</p>
<h3><a name="p-18679-out-of-box-integration-4" class="anchor" href="#p-18679-out-of-box-integration-4" aria-label="Heading link"></a>Out-of-box integration ?</h3>
<aside class="quote no-group" data-username="kayarre" data-post="1" data-topic="5010">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/kayarre/48/3606_2.png" class="avatar"> kayarre:</div>
<blockquote>
<p>Does something like this exist? Does anyone have a suggestion about how this might be done.</p>
</blockquote>
</aside>
<p>All components enabling this exists. That said, some work is required to create a tailored application as well as its associated maintenance and deployment strategy.</p>
<p>Such solution could either be hosted within an institution, or deployed on cloud services ilke Amazon or Google depending on the requirement of each institution.</p>
<h3><a name="p-18679-what-about-server-side-processing-and-jupyter-integration-5" class="anchor" href="#p-18679-what-about-server-side-processing-and-jupyter-integration-5" aria-label="Heading link"></a>What about server side processing and Jupyter integration ?</h3>
<p>If this is of interest, consider posting an other question on the forum.</p>

---

## Post #3 by @lassoan (2018-12-08 13:44 UTC)

<p>Using JavaScript web viewer is nice and probably good choice if you want to share data with unlimited number of users independently.</p>
<p>However, for the use case that you describe, running Slicer in a docker container and allowing remote access through a web browser may be more suitable You can hide all user interface elements that you would not like the user to interact with. You can try an example here:</p>
<p><em><a href="https://tinyurl.com/y82y5fk8">https://tinyurl.com/y82y5fk8</a> (link expired)</em> – similar demo is available using Binder <a href="https://mybinder.org/v2/gh/Slicer/SlicerNotebooks/master?filepath=SlicerWeb.ipynb">here</a></p>
<p>Multiple people can see and interact with the same Slicer instance and they all see the same view, which is great for collaboration/shared viewing (you can test it by opening the link in multiple browser windows). Also, viewing is immediate, no data need to be downloaded to the viewer’s computer.</p>
<p>Another obvious choice is to save image and segmentation data in DICOM format and push it to the clinical PACS system that clinicians can nowadays access remotely.</p>

---
