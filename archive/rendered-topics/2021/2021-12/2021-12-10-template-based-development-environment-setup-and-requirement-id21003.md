---
topic_id: 21003
title: "Template Based Development Environment Setup And Requirement"
date: 2021-12-10
url: https://discourse.slicer.org/t/21003
---

# Template based development environment setup and requirements of FDA approval

**Topic ID**: 21003
**Date**: 2021-12-10
**URL**: https://discourse.slicer.org/t/template-based-development-environment-setup-and-requirements-of-fda-approval/21003

---

## Post #1 by @Dwij_Mistry (2021-12-10 13:45 UTC)

<h3><a name="p-70983-how-we-can-setup-a-clean-development-environment-1" class="anchor" href="#p-70983-how-we-can-setup-a-clean-development-environment-1" aria-label="Heading link"></a>How we can setup a clean development environment?</h3>
<p>What we are doing is as follow.</p>
<ol>
<li>We created Template in which we had<br>
GIT_REPOSITORY git://github.com/Slicer/Slicer<br>
GIT_TAG 62e4d8544f2a6f30b707a87288a5e1b9fc5a5a86<br>
(this is a latest commit on 3/12/2021  which is a based on 4.11.20210226 stable patch)</li>
<li>build it.</li>
<li>we pushed slicersource-src to our GitHub repo.</li>
<li>in template we modified<br>
GIT_REPOSITORY <em>our repo</em><br>
GIT_TAG        <em>tag id</em><br>
So from next time when we are setting up an environment it is taking source code from our GitHub repo.</li>
<li>once development environment is set, we are doing required modification in <strong>slicersource-src</strong> folder which is linked with our GitHub repo. by this we are pushing and pulling changes (So, multiple developers can contribute).</li>
</ol>
<h3><a name="p-70983-does-we-are-following-correct-method-for-clean-development-2" class="anchor" href="#p-70983-does-we-are-following-correct-method-for-clean-development-2" aria-label="Heading link"></a>Does we are following correct method for clean development?</h3>
<p>Or Is there any way to do<br>
Please tell me your suggestions.</p>
<p>In addition to this, We are planning for FDA approval.</p>
<ul>
<li>
<h3><a name="p-70983-does-we-will-get-fda-approval-by-using-slicer-template-based-software-development-or-any-other-way-to-achieve-3" class="anchor" href="#p-70983-does-we-will-get-fda-approval-by-using-slicer-template-based-software-development-or-any-other-way-to-achieve-3" aria-label="Heading link"></a>Does we will get FDA approval by using slicer template based software development? or any other way to achieve?</h3>
</li>
<li>
<h3><a name="p-70983-what-are-the-requirements-to-get-full-fda-approval-for-the-software-4" class="anchor" href="#p-70983-what-are-the-requirements-to-get-full-fda-approval-for-the-software-4" aria-label="Heading link"></a>What are the requirements to get full FDA approval for the software?</h3>
</li>
</ul>

---

## Post #2 by @Sam_Horvath (2021-12-10 14:03 UTC)

<p>Forking Slicer to your GitHub organization and then creating a branch in that fork based on your desired Slicer commit would have been a more straightforward method, but achieves the same thing in the end.</p>
<p>With regards to FDA approval, FDA submission is a complicated process that will depend heavily on the intended use of the software.  You will need to engage with a regulatory consultant in order to determine the requirements for FDA approval.</p>

---

## Post #3 by @Dwij_Mistry (2021-12-10 14:15 UTC)

<aside class="quote no-group" data-username="Sam_Horvath" data-post="2" data-topic="21003">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sam_horvath/48/3092_2.png" class="avatar"> Sam_Horvath:</div>
<blockquote>
<p>Forking Slicer to your GitHub organization and then creating a branch in that fork based on your desired Slicer commit would have been a more straightforward method</p>
</blockquote>
</aside>
<p>We are using private repo for the development.</p>
<aside class="quote no-group" data-username="Sam_Horvath" data-post="2" data-topic="21003">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sam_horvath/48/3092_2.png" class="avatar"> Sam_Horvath:</div>
<blockquote>
<p>FDA submission is a complicated process</p>
</blockquote>
</aside>
<p>Is there any hardware specification for the development?</p>
<p>Dese we will get FDA approval for full slicer based software or we need to create software from a scratch like ITK, VTK, Qt lib (start from zero)</p>

---

## Post #4 by @pieper (2021-12-10 14:47 UTC)

<p>I’ll just reiterate Sam’s point that there is a lot to consider if you plan to bring a medical device to market so there’s no simple answer.</p>
<p>A good place to start learning is to take this course and read the accompanying textbook:</p>
<aside class="quote" data-post="1" data-topic="20149">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/yale-course-about-medical-software-development/20149">Yale course about medical software development</a> <a class="badge-category__wrapper " href="/c/announcements/7"><span data-category-id="7" style="--category-badge-color: #ED207B; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="Low-traffic category for 3D Slicer, extension, and community news and announcements."><span class="badge-category__name">Announcements</span></span></a>
  </div>
  <blockquote>
    Our friend and colleague Xenios has put together a great set of material about developing medical software.  The course is free, or $50 if you want a certificate.  There’s a textbook with additional  material.  I read an earlier draft and there’s a lot of very practical information for anyone working in the field.
  </blockquote>
</aside>


---
