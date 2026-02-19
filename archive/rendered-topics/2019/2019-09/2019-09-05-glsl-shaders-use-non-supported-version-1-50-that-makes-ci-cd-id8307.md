---
topic_id: 8307
title: "Glsl Shaders Use Non Supported Version 1 50 That Makes Ci Cd"
date: 2019-09-05
url: https://discourse.slicer.org/t/8307
---

# GLSL shaders use non supported version 1.50 that makes CI/CD to fail in a docker container

**Topic ID**: 8307
**Date**: 2019-09-05
**URL**: https://discourse.slicer.org/t/glsl-shaders-use-non-supported-version-1-50-that-makes-ci-cd-to-fail-in-a-docker-container/8307

---

## Post #1 by @Alex_Vergara (2019-09-05 10:35 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/cpinter">@cpinter</a>, we are trying to test our extension in a docker container as described by <a class="mention" href="/u/unnmdnwb3">@unnmdnwb3</a> in <a href="https://discourse.slicer.org/t/docker-image-for-nightly-master/">this</a> thread.</p>
<p>However, the test fails when executing slicer with <a href="https://gitlab.com/BishopWolf/dosimetry4d/-/jobs/288261429" rel="nofollow noopener">these</a> errors.</p>
<p>Basically the VTK version that is used enforces the use of GLSL version 1.50 which is unsopported by the opengl libraries. Is there any way to change VTK version while creating the slicer container? Which is the recommended version of VTK that does not have this problem? I can’t see this enforcement in VTK 8.2 for instance.</p>

---

## Post #2 by @Alex_Vergara (2019-09-05 12:34 UTC)

<p>This is a quick view of the error for those interested but with no access to the project yet<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3a27ecabe5967d659d48ee579495151c7338f17.png" data-download-href="/uploads/short-url/pD7BVxR7uRufneNqok5RRTBw6s7.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3a27ecabe5967d659d48ee579495151c7338f17.png" alt="image" data-base62-sha1="pD7BVxR7uRufneNqok5RRTBw6s7" width="654" height="500" data-dominant-color="0A0A0A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">749×572 23.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @lassoan (2019-09-05 12:47 UTC)

<p>There are several docker container examples where appropriate OpenGL version is configured. See for example this topic:</p>
<aside class="quote quote-modified" data-post="1" data-topic="4091">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/e5b9ba/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/workflow-with-docker-and-slicer/4091">Workflow with Docker and Slicer</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi, 
I’am a scientist and working with Slicer build inside a docker image but I want make some upgrade in a workflow and add SlicerJupyter extension. I have a dream that I am preparing a docker image for my friends in team. In last few days I did some research about your solution with docker but I got lost in this topic. What need I to create a dream workflow: 

Create docker image with build version Slicer Qt5 (always need builded version because I working with own extensions
Build and install …
  </blockquote>
</aside>


---
