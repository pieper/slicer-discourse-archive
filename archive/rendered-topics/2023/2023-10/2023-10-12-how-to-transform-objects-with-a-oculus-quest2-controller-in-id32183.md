---
topic_id: 32183
title: "How To Transform Objects With A Oculus Quest2 Controller In"
date: 2023-10-12
url: https://discourse.slicer.org/t/32183
---

# How to transform objects with a Oculus Quest2 controller in Virtual Reality module

**Topic ID**: 32183
**Date**: 2023-10-12
**URL**: https://discourse.slicer.org/t/how-to-transform-objects-with-a-oculus-quest2-controller-in-virtual-reality-module/32183

---

## Post #1 by @ally7113 (2023-10-12 11:23 UTC)

<p>I’m using Slicer 5.3.0, and I’ve successfully set up the VR module with SteamVR to display it on the Oculus Quest. However, after that, I’m limited to just using the trigger action, and I want to be able to rotate objects, resize them, and adjust the overall camera view with the controller. How can I achieve this?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c171026601f605248243fd346620bc44cdfc3eb.png" data-download-href="/uploads/short-url/40uMsutz0UgdeeRUaaSZL6Lc3Ev.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c171026601f605248243fd346620bc44cdfc3eb.png" alt="image" data-base62-sha1="40uMsutz0UgdeeRUaaSZL6Lc3Ev" width="586" height="500" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">735×627 20.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’ve followed all the steps in the picture, including applying VTK, but it’s not working. I’m not very familiar with Python or Qt, so I would really appreciate it if you could provide detailed instructions.</p>

---

## Post #2 by @cpinter (2023-10-13 12:20 UTC)

<p>People have been reprting this for Oculus Quest 2 for a while, but since I don’t have such a device I cannot test or try to fix this. Does anyone at Kitware have a Quest 2? We have been receiving these reports and I cannot tell them anything. Thank you!</p>
<p>Also there is this issue, not sure if related</p><aside class="onebox githubissue" data-onebox-src="https://github.com/KitwareMedical/SlicerVirtualReality/issues/124">
  <header class="source">

      <a href="https://github.com/KitwareMedical/SlicerVirtualReality/issues/124" target="_blank" rel="noopener">github.com/KitwareMedical/SlicerVirtualReality</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/KitwareMedical/SlicerVirtualReality/issues/124" target="_blank" rel="noopener">3D pinch function is unreliable</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-09-14" data-time="09:54:38" data-timezone="UTC">09:54AM - 14 Sep 23 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/cpinter" target="_blank" rel="noopener">
          <img alt="cpinter" src="https://avatars.githubusercontent.com/u/1325980?v=4" class="onebox-avatar-inline" width="20" height="20">
          cpinter
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">The two-handed gesture that allows to rotate/scale the world only works around h<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">alf the time. See video here
https://discourse.slicer.org/t/5-4-vr-testride/31252/3?u=cpinter

Is it possible that the `RecognizeComplexGesture` function has changed again? Or some other change in VTK causes this?

It used to work perfectly with [Slicer 98c092edb8f5a274277d2e486a4f7e584f58605e](https://github.com/Slicer/Slicer/commit/98c092edb8f5a274277d2e486a4f7e584f58605e)  (5.3.0 nightly 2023.06.19.)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
