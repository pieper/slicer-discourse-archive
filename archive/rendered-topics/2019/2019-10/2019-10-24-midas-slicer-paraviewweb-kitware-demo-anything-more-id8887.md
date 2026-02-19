---
topic_id: 8887
title: "Midas Slicer Paraviewweb Kitware Demo Anything More"
date: 2019-10-24
url: https://discourse.slicer.org/t/8887
---

# Midas + Slicer + ParaviewWeb Kitware Demo - Anything more?

**Topic ID**: 8887
**Date**: 2019-10-24
**URL**: https://discourse.slicer.org/t/midas-slicer-paraviewweb-kitware-demo-anything-more/8887

---

## Post #1 by @Morasta (2019-10-24 02:07 UTC)

<p>While working on a paraviewweb/vtk project, I came across this old kitware video: <a href="https://www.youtube.com/watch?v=jbq26vWdNdE&amp;feature=youtu.be" rel="nofollow noopener">https://www.youtube.com/watch?v=jbq26vWdNdE&amp;feature=youtu.be</a>.</p>
<p>Curious if anyone here knows anything more about it as the notes in the video’s description are confusing and I can’t seem to find any further concrete info about it. Anyone know anything about it?</p>

---

## Post #2 by @lassoan (2019-10-24 02:33 UTC)

<p>Midas is replaced Girder. It has plugins for browsing DICOM image slices and run Slicer CLI modules, so you can probably set up the same thing as in the demo video. ParaViewWeb is now VTK.js and ParaView Glance.</p>
<p>You can access Girder from Slicer using Girder’s Python API and it should be possible to set up Girder to launch Slicer in your web browser (running in a docker container).</p>
<p>For DICOM-oriented workflows you may also consider using XNAT and OHIF viewer. There are some Slicer integration options for these, too.</p>

---

## Post #3 by @Morasta (2019-10-28 19:41 UTC)

<p>Thanks, Andras! I currently have a custom ParaView Web/VTK.js FE with paraview/vtk backend server side rendering app up and running, so I’m somewhat familiar with that end of things. New to Slicer though, so a couple of follow-up questions on how I might get started here.</p>
<ul>
<li>Is paraview (the server version, and my current backend for server-side rendering) calling the Slicer CLI modules, or would that be handled by Girder?</li>
<li>Is Girder necessary given that Paraview has methods for loading dicom/pns series data? How exactly does this fit into the equation?</li>
<li>Basically I’m wondering if I could proceed with Paraview Server --&gt; Slicer CLI modules on the backend pushing data across to paraviewweb/vtk.js on the frontend and if there are any docs anywhere for that type of thing and how to start connecting the pieces.</li>
</ul>

---

## Post #4 by @lassoan (2019-10-28 21:25 UTC)

<p>Paraview is extremely limited when it comes to dealing with medical images. It can load only a very small subset of DICOM images (if any) and some of then may just load with incorrect geometry. So, unless you know in advance what images exactly you will receive and test with those, I would not rely on Paraview for DICOM loading.</p>
<p>I don’t think Paraview supports CLI modules, but Girder does, at least I remember seeing some demos showing it.</p>
<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> <a class="mention" href="/u/jcfr">@jcfr</a> could you ask Kitware girder developers to comment on this?</p>

---

## Post #5 by @Morasta (2019-10-30 17:04 UTC)

<p>Thanks again, Andras. Wrapping my head about the specific libs I should be digging deeper into and how they relate. My primary need is the server side rendering component which vtk.js supports out of the box and I was able to put together.</p>
<p>Currently I have a vtk.js/react page that’s communicating to a paraview backend. Are you saying I should be looking at using Girder and Slicer together on my server/BE to do the vis, then continue using VTK.js to AS the FE? If so, is girder necessary in this type of approach, or would data loading be something I could tackle via python modules or the like. Once again, thanks for your help. Lot of confusion about the different pieces here and how they fit together.</p>

---

## Post #6 by @Morasta (2019-10-30 23:02 UTC)

<p>Clarifying I’m exploring using Slicer and writing modules for it to extend it as needed to replace my current BE/FE design described above. The tech stack is still confusing.</p>
<p>Our current approach:<br>
Backend of python (pvpython) using</p>
<ul>
<li>paraview.web</li>
<li>paraview.simple</li>
<li>wslink</li>
</ul>
<p>FE using</p>
<ul>
<li>paraviewweb</li>
<li>VTKRenderer</li>
<li>paraview/io/websocket/ParaViewWebClient w/SmartConnect</li>
</ul>
<p>To make sure I understand, an approach to incorporate Slicer with server-side rendering could be:</p>
<ul>
<li>A <em>Frontend</em> webpage written using VTK.js/paraviewweb (along what we have now, above)<br>
** What would it use to connect? (e.g. as with SmartConnect currently)</li>
<li>A <em>Backend</em> of Slicer to handle the vis heavy lifting, replacing paraview.simple? What about paraview.web?</li>
<li>Girder (if necessary, could we do this ourselves with locally stored files?) for file management</li>
</ul>

---

## Post #7 by @lassoan (2019-10-31 03:59 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a> could you help out here? I’m not familiar enough with these web technologies to give good advice.</p>

---

## Post #8 by @pieper (2019-10-31 20:13 UTC)

<p>Hi <a class="mention" href="/u/morasta">@Morasta</a> -</p>
<p>Sounds like you are exploring all the good options, but probably there isn’t yet a really complete end-to-end implementation that’s in production.</p>
<p>I’m not personally too familiar with the paraview approaches.  Maybe you could describe a bit about what you want to achieve and why your current approach isn’t working for you and why you want to change direction?</p>
<p>For myself, we’ve been working mostly lately with this formulation (all should be easy to find by searching but let me know if you want more info):</p>
<ul>
<li>DICOMweb serving all the data (can come from Google Healthcare or self-hosted open source server)</li>
<li>OHIF client for dicom study browser, layout, app context</li>
<li>vtk.js plugin for MPR rendering</li>
</ul>
<p>For server-side rendering with Slicer, I’ve been playing for a while with <a href="https://github.com/pieper/SlicerWeb">embedding a web server</a> in Slicer.  This actually works quite nicely, but it means you have to maintain a server with the user’s data loaded or create one on the fly.  That’s why the client-side rendering is preferred in general, although there will be limits on how much data can be downloaded efficiently and how much can be loaded into the browser.</p>
<p>Hope that helps - I’m curious to hear what works best for your use case.</p>
<p>-Steve</p>

---

## Post #9 by @BadCookie (2021-06-09 05:58 UTC)

<p>Hi, <a class="mention" href="/u/morasta">@Morasta</a>.<br>
I wanted to know some information on your approach to solve this problem. Cause I have the exact same F.E and B.E setup. I wanted to utilize slicers segmentation algorithms, along with the current setup. So, any guidance or links or approaches is appreciated. Thanks</p>

---
