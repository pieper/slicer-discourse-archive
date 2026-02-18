# Unable to load slicer extension website

**Topic ID**: 17554
**Date**: 2021-05-10
**URL**: https://discourse.slicer.org/t/unable-to-load-slicer-extension-website/17554

---

## Post #1 by @banderies (2021-05-10 22:26 UTC)

<p>I have been trying to load the slicer extension website via the extension manager and manually via <a href="https://slicer.kitware.com/midas3/slicerappstore" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>. Initially, it would only load on my Mac and not on my Linux installation, but now I can’t get it to load anywhere on multiple networks. Is this a known problem? I have attached a screenshot of the error.</p>
<p>Thanks,<br>
Barrett</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab586114a083a2d0f563762332e00b9627f98c08.png" data-download-href="/uploads/short-url/orMZWmELhjcJkrqWdad8jc4RoEw.png?dl=1" title="Screen Shot 2021-05-10 at 5.24.16 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab586114a083a2d0f563762332e00b9627f98c08_2_690x440.png" alt="Screen Shot 2021-05-10 at 5.24.16 PM" data-base62-sha1="orMZWmELhjcJkrqWdad8jc4RoEw" width="690" height="440" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab586114a083a2d0f563762332e00b9627f98c08_2_690x440.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab586114a083a2d0f563762332e00b9627f98c08_2_1035x660.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab586114a083a2d0f563762332e00b9627f98c08_2_1380x880.png 2x" data-dominant-color="E0E0E0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-05-10 at 5.24.16 PM</span><span class="informations">1392×889 173 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2021-05-10 22:47 UTC)

<p>Thanks for the report.  Probably this is expected and due to the server upgrades:</p>
<aside class="quote quote-modified" data-post="1" data-topic="17444">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sam_horvath/48/3092_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/upcoming-downtime-for-download-slicer-org-and-extension-manager-due-to-package-server-transition/17444">Upcoming downtime for download.slicer.org and extension manager due to package server transition</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi all: 
Over the next two weeks, the Slicer development team at Kitware will be transitioning to new backend servers for hosting the Slicer installer packages and extensions.  We are moving to a server built on the newer Girder platform for the backend and a vue.js based web application for the frontend.  This will address EOL issues with the infrastructure, and significantly improve the download / extension manager experience for users. 
As a result of this ongoing upgrade, during the next two…
  </blockquote>
</aside>


---
