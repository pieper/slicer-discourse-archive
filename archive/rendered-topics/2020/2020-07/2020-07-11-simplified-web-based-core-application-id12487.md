---
topic_id: 12487
title: "Simplified Web Based Core Application"
date: 2020-07-11
url: https://discourse.slicer.org/t/12487
---

# Simplified web based core application

**Topic ID**: 12487
**Date**: 2020-07-11
**URL**: https://discourse.slicer.org/t/simplified-web-based-core-application/12487

---

## Post #1 by @tobiedesgreniers (2020-07-11 16:28 UTC)

<p>Hi 3DSlicer community!<br>
I’m a student in computer engineering and i’m working on a bachelor end project aiming to develop a commercial service prototype for surgeons to print biomimetic models of human parts to practice surgeries!</p>
<p>The goal of our team would be to “probably” have a segmentation module in a web browser so that surgeons can target specified regions containing tumors and then send a 3D model print request to a 3D printing service.</p>
<p>I consulted these resources :</p><aside class="quote quote-modified" data-post="1" data-topic="9729">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/5fc32e/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/remote-web-based-ui/9729">Remote web based UI</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    This is kind of a far fetched question, but I was wondering if anyone has done work on seperating the UI layer of slicer. 
My end goal is to have slicer running on a computer, but also have remote web based UI built similarly to webvtk.  I know I can do the entire slicer interface using VNC, but in my case I want different UIs for different people. 
My thought is to write a module which exports the MRML node list and subscribes to the events then either use vtk.js on the other side or render loc…
  </blockquote>
</aside>
<p><a href="https://discourse.slicer.org/t/run-slicer-in-your-web-browser-as-a-jupyter-notebook-or-as-a-full-application/11569" class="inline-onebox">Run Slicer in your web browser - as a Jupyter notebook or as a full application</a><br>
<a href="https://discourse.slicer.org/t/segmentation-via-web-browser/9270" class="inline-onebox">Segmentation via web-browser</a><br>
<a href="https://discourse.slicer.org/t/embed-3dslicer-in-a-web-gui/3167" class="inline-onebox">Embed 3DSlicer in a web GUI</a><br>
<a href="https://discourse.slicer.org/t/can-3d-slicer-be-hosted-on-a-rendering-server/9256" class="inline-onebox">Can 3D Slicer be hosted on a rendering server?</a></p>
<p>And I have so many questions concerning the software architecture, modules and how to adapt 3DSlicer for our project.<br>
Would it be better to go for common gateway interface to run 3DSlicer as a service and then make our own GUI?<br>
Would it be better to use docker images (which from what i understood is using VNC to work?)?<br>
Or maybe go for RDP and resource sharing across users?<br>
Is Jupyter Notebook GUI customizable enough for us to develop a customer ready GUI?</p>
<p>Our main requirements are reusing the great technologies that were developed for 3DSlicer, but the GUI would be, for the prototype, way to complicated for simple users who’d like to have surgery simulators within range of a few simple clicks. And we would also like many (let’s say 10 or 20) users to connect at the same time.<br>
The main features would be the segmentation module with a display in a web site, patient’s files and folder management, web authentication and data exporting for a 3D printing service.</p>
<p>Since i have so many questions and with my lack of experience as a student, i would be very open to have a Microsoft Teams conversation with some expert. It would be a great help in our project.</p>
<p>In case this topic isn’t within the scope of this forum or the community, please excuse my trespassing.</p>
<p>Best regards,<br>
Tobie</p>

---

## Post #2 by @lassoan (2020-07-11 17:09 UTC)

<p>There are many options for simplifying Slicer user interface and make it available without installation. I would recommend to focus on figuring out the workflow first: who does what and how, what steps can be automated and what requires user inputs, what visualization you need, validate robustness and accuracy of automatic processing algorithms, etc. You will need minimal software development for this, but it is mostly learning and experimenting with various existing tools. Once you have a very good idea of how everything will work and what you need to do, you can start thinking about how to achieve that (what to develop, what technologies to use, where to deploy, etc.).</p>
<p>If you are more comfortable talking about your project rather than discussing it on the forum then you can join one of the <a href="https://discourse.slicer.org/c/community/hangout/20">weekly Slicer hangouts</a>.</p>

---

## Post #3 by @tobiedesgreniers (2020-07-14 02:51 UTC)

<p>Hi Andras,<br>
Thank you very much for your answer.<br>
I will make sure to make some progress towards what you proposed about our specifications, workflow and key requirements and i will get back to you in the next weekly hangout (probably july 21 from my understanding).<br>
I just want to make sure that i’m not losing anyone’s time so would it be okay if i make a very brief presentation of a few slides for you to better understand the project?</p>
<p>Best regards,<br>
Tobie</p>

---

## Post #4 by @lassoan (2020-07-14 04:32 UTC)

<p>You can join the next meeting in 9.5 hours (<a href="https://discourse.slicer.org/t/2020-07-14-hangout/12509" class="inline-onebox">2020.07.14 Hangout</a>), but next week is fine, too.</p>

---
