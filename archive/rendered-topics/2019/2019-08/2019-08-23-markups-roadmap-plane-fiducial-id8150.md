# Markups roadmap - Plane fiducial

**Topic ID**: 8150
**Date**: 2019-08-23
**URL**: https://discourse.slicer.org/t/markups-roadmap-plane-fiducial/8150

---

## Post #1 by @Sam_Horvath (2019-08-23 21:09 UTC)

<p>Hi all:</p>
<p>per the <a href="https://www.slicer.org/wiki/Documentation/Labs/Improving_Markups" rel="nofollow noopener">roadmap</a>, we are planning to add a plane fiducial type.  Two questions:</p>
<ul>
<li>Is this intended to go into Slicer core?</li>
<li>Is anyone working on it yet?</li>
</ul>
<p>I am trying to get the <a href="https://github.com/KitwareMedical/OsteotomyPlanner" rel="nofollow noopener">Osteotomy Planner</a> updated for current Slicer, and it (currently) includes its own version of a plane widget that needs to be replaced.   If no one else is actively working on adding the plane fiducial to Slicer I will, but I wanted to make sure I wasn’t duplicating any in-progress work.</p>

---

## Post #2 by @jamesobutler (2019-08-23 23:49 UTC)

<p>I think the closest things done related to planes is <a href="https://github.com/Slicer/Slicer/pull/1010" class="inline-onebox" rel="noopener nofollow ugc">References are not preserved after imports · Issue #1010 · Slicer/Slicer · GitHub</a> which was prior to markups refactor, but includes work for a vtkMRMLMarkupsPlanesNode.cxx.</p>
<aside class="quote quote-modified" data-post="1" data-topic="3951">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/johan_andruejol/48/3639_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-annotation-for-slicer-splines-and-planes/3951">New Annotation for Slicer - Splines and Planes</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Hi everyone, 
We have developed new annotation support for Slicer in the form of Splines and Planes. Here is a preview: 
Planes: 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb2e3c2dcf929723d021bb7f003afd46b0250453.png" data-download-href="/uploads/short-url/sZpZ39i35hYxnY6eXqMFMD34hGP.png?dl=1" title="image" rel="noopener nofollow ugc">[image]</a> 
Note: Planes annotation are only available in the 3D view 
Splines: 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be66bd06ebf017f0ac49c1a03abe7a22f081eaeb.jpeg" data-download-href="/uploads/short-url/ramPN8DnBuoNaUWSHc63qh8Oyr9.jpeg?dl=1" title="image" rel="noopener nofollow ugc">[image]</a> 
These fulfill the needs we have for them, but I don’t think they could be considered “feature complete”. They don’t have a GUI to interact with them for example. Where do you think would be a good idea to share these so the community can have access to it ? As an extension ? 
Each…
  </blockquote>
</aside>


---

## Post #3 by @lassoan (2019-08-24 03:44 UTC)

<p>The plane widget could be implemented as a markups widget, as most of the infrastructure that would be needed for this feature is already available for markups.</p>
<aside class="quote no-group" data-username="Sam_Horvath" data-post="1" data-topic="8150">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sam_horvath/48/3092_2.png" class="avatar"> Sam_Horvath:</div>
<blockquote>
<p>Is this intended to go into Slicer core?</p>
</blockquote>
</aside>
<p>Yes, it should definitely go into the Slicer core.</p>
<aside class="quote no-group" data-username="Sam_Horvath" data-post="1" data-topic="8150">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sam_horvath/48/3092_2.png" class="avatar"> Sam_Horvath:</div>
<blockquote>
<p>Is anyone working on it yet?</p>
</blockquote>
</aside>
<p>I don’t think anyone is working on a plane widget right now.</p>

---

## Post #4 by @Sam_Horvath (2019-08-26 15:59 UTC)

<p>Great!  I hope to get to this in the next week or so.</p>
<p>Sam</p>

---
