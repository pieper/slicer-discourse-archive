# Increase Width of segments after TotalSegmentor autosegmentation

**Topic ID**: 37018
**Date**: 2024-06-25
**URL**: https://discourse.slicer.org/t/increase-width-of-segments-after-totalsegmentor-autosegmentation/37018

---

## Post #1 by @waterbottle (2024-06-25 21:12 UTC)

<p>Hi all,</p>
<p>I am brand new to 3D Slicer and am using it on MRIs. I have just started learning to use totalsegmentor to automatically segment muscles, its going okay but so far there are segments I need to increase or decrease the width of across all of the slices.</p>
<p>From what I gather I can use the scissors tool to handle decreasing width across all slices at once but I am confused on how I can <strong>increase the width of certain segments</strong>. I tried to use the paint tool but it only does one slice at a time, can anyone point me in the right direction?</p>
<p>Much appreciated, complete rookie here.</p>

---

## Post #2 by @mikebind (2024-06-25 21:17 UTC)

<p>The Margin tool would allow you to grow a segment uniformly in all directions (in 3D).  If that isn’t what you want, some screen shots and some more description of what you are trying to accomplish would be helpful.</p>

---

## Post #3 by @waterbottle (2024-06-25 21:46 UTC)

<p>Hello, thank you for your answer! I tried the margin tool on the MRI I have open and it says “Not feasible at current resolution,” any tips or am I using it wrong?</p>
<p>Re: picture—this is an example, inside the red outline is what I am getting right now and I want to expand the boundries to the blue outline.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85d9de290302041389baaf44a70d426108e1ef77.jpeg" data-download-href="/uploads/short-url/j66hyE8N6pzjcs3VLWN57c36Y7l.jpeg?dl=1" title="Mriexample" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85d9de290302041389baaf44a70d426108e1ef77_2_644x500.jpeg" alt="Mriexample" data-base62-sha1="j66hyE8N6pzjcs3VLWN57c36Y7l" width="644" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85d9de290302041389baaf44a70d426108e1ef77_2_644x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85d9de290302041389baaf44a70d426108e1ef77.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85d9de290302041389baaf44a70d426108e1ef77.jpeg 2x" data-dominant-color="6D6D6D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Mriexample</span><span class="informations">701×544 65 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @waterbottle (2024-06-26 00:46 UTC)

<p>Margin does the trick, for anyone wondering how to resolve “not feasible” problem, check this out:</p>
<aside class="quote" data-post="1" data-topic="19068">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alberto_paredes/48/9629_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-do-i-set-segmentation-resolution/19068">How do I set segmentation resolution</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Operating system: Windows 10 
Slicer version: Slicer 4.11.20210226 
Question: I am completely new to 3D Slicer. I was working on a segmentation and when trying to make it hollow, I was not able to with my desired shell thickness because it is not feasible at the current resolution. I believe I have to adjust the “master volume”, but I do not know how. Can you please tell me how I can adjust the resolution of my segmentation, and can you explain to me more about this “master volume”
  </blockquote>
</aside>


---
