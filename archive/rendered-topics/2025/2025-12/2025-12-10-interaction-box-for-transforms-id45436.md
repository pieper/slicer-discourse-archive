---
topic_id: 45436
title: "Interaction Box For Transforms"
date: 2025-12-10
url: https://discourse.slicer.org/t/45436
---

# Interaction Box for Transforms

**Topic ID**: 45436
**Date**: 2025-12-10
**URL**: https://discourse.slicer.org/t/interaction-box-for-transforms/45436

---

## Post #1 by @Jane_Hand (2025-12-10 14:55 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84849497c15c95ed0bfc92d5f55dc2661cb596ad.jpeg" data-download-href="/uploads/short-url/iUj4RiUWYZh48HrHQfA2c44bSLb.jpeg?dl=1" title="Screenshot 2025-12-09 at 9.51.56 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84849497c15c95ed0bfc92d5f55dc2661cb596ad_2_690x267.jpeg" alt="Screenshot 2025-12-09 at 9.51.56 PM" data-base62-sha1="iUj4RiUWYZh48HrHQfA2c44bSLb" width="690" height="267" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84849497c15c95ed0bfc92d5f55dc2661cb596ad_2_690x267.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84849497c15c95ed0bfc92d5f55dc2661cb596ad_2_1035x400.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84849497c15c95ed0bfc92d5f55dc2661cb596ad_2_1380x534.jpeg 2x" data-dominant-color="70708B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-12-09 at 9.51.56 PM</span><span class="informations">1920×743 173 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I can’t figure out how to made my interaction display a box to more easily manipulate my models. I updated to 5.10. While I am able to move my models with the object on the screen, it only allows for local manipulation and it is very difficult to line up my models. Any advice on how to change my interaction display the more easily manipulated box would be appreciated.</p>

---

## Post #2 by @muratmaga (2025-12-10 16:25 UTC)

<p>Use the data module, and right-clcik on the visibility (eye) icon and enable interaction:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db92780511a11c9a5ca302cd50b5ccc623c48a0a.jpeg" data-download-href="/uploads/short-url/vkqnbP4P1LdJ3aoc3k3lFvKnVO2.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db92780511a11c9a5ca302cd50b5ccc623c48a0a_2_662x499.jpeg" alt="image" data-base62-sha1="vkqnbP4P1LdJ3aoc3k3lFvKnVO2" width="662" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db92780511a11c9a5ca302cd50b5ccc623c48a0a_2_662x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db92780511a11c9a5ca302cd50b5ccc623c48a0a_2_993x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db92780511a11c9a5ca302cd50b5ccc623c48a0a.jpeg 2x" data-dominant-color="C1C3CA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1191×899 213 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @philippepellerin (2025-12-11 13:57 UTC)

<p>Hi, I should say that your problems are about orientation. I solved them by using the vestibular orientation.</p>
<p>Here is a link to a tutorial to learn how to perform a VO.</p>
<p>If you want to go further and have your planes set as to have them displayed oriented in the 3D view</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27c5020c5afadbbc80304a64e7b68a245a60c2e3.png" data-download-href="/uploads/short-url/5FOHXyOCsSKg7eub29hnPVrRZIv.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27c5020c5afadbbc80304a64e7b68a245a60c2e3.png" alt="image" data-base62-sha1="5FOHXyOCsSKg7eub29hnPVrRZIv" width="478" height="278"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">478×278 19.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>you can perform a transform of the view and align the planes in the corresponding orientation.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="Bs4GWLrFQfA" data-video-title="Vestibular Orientation with 3DSlicer 02" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=Bs4GWLrFQfA" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/Bs4GWLrFQfA/maxresdefault.jpg" title="Vestibular Orientation with 3DSlicer 02" width="690" height="388">
  </a>
</div>


---
