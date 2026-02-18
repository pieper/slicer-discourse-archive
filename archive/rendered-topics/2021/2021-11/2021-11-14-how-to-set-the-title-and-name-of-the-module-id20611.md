# How to set the title and name of the module

**Topic ID**: 20611
**Date**: 2021-11-14
**URL**: https://discourse.slicer.org/t/how-to-set-the-title-and-name-of-the-module/20611

---

## Post #1 by @LuPingChina (2021-11-14 03:23 UTC)

<p>How to set the title and name of the module when the application starts and before the module is used</p>

---

## Post #2 by @lassoan (2021-11-14 20:06 UTC)

<p>I don’t think you can change a module’s name. Changing the title that is returned by the module object could be hard, too, because usually it is hardcoded in the implementation.<br>
Why would you need to change a module’s title? To translate to a different language?</p>

---

## Post #3 by @LuPingChina (2021-11-18 08:47 UTC)

<p>I want to translate the software interface into Chinese.</p>

---

## Post #4 by @pieper (2021-11-18 13:13 UTC)

<p>Building on a lot of excellent preliminary work, a group is now funded to work on i18n for Slicer.  It would be great if you can help!</p>
<aside class="quote quote-modified" data-post="1" data-topic="19500">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/spujol/48/3498_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/czi-essential-open-source-software-for-science-eoss-award-for-3d-slicer-internationalization/19500">CZI Essential Open Source Software for Science (EOSS) Award for 3D Slicer Internationalization</a> <a class="badge-category__wrapper " href="/c/announcements/7"><span data-category-id="7" style="--category-badge-color: #ED207B; --category-badge-text-color: #000000;" data-drop-close="true" class="badge-category --style-square " title="Low-traffic category for 3D Slicer, extension, and community news and announcements."><span class="badge-category__name">Announcements</span></span></a>
    </div>
  </div>
  <blockquote>
    It is my distinct pleasure to announce that we have been awarded an Essential Open Source Software for Science (EOSS) grant from the Chan Zuckerberg Initiative (CZI), a philanthropy led by Facebook founder Mark Zuckerberg and his wife Dr. Priscilla Chan. The grant will support the new “3D Slicer in My Language” project to increase the accessibility of 3D Slicer in non-English speaking countries. We are thrilled to start developing a French version of 3D Slicer in collaboration with Cheikh Anta D…
  </blockquote>
</aside>

<aside class="quote quote-modified" data-post="1" data-topic="579">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/slicer-internationalization/579">Slicer Internationalization</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #000000;" data-drop-close="true" class="badge-category --style-square " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
    </div>
  </div>
  <blockquote>
    <a name="overview-1" class="anchor" href="#overview-1"></a>Overview
Following conversation with <a class="mention" href="/u/marilola">@marilola</a> that took place during the 25th Slicer project week, I am summarizing here the current state of the Slicer internationalization framework. 
Prior discussion and description of the I18N framework can be found here: 

<a href="https://www.slicer.org/wiki/Documentation/Labs/I18N" class="inline-onebox">Documentation/Labs/I18N - Slicer Wiki</a>
<a href="https://www.slicer.org/wiki/Slicer4:Internationalization_of_Slicer" class="inline-onebox">Slicer4:Internationalization of Slicer - Slicer Wiki</a>

<a name="technology-2" class="anchor" href="#technology-2"></a>Technology
Since most of the user facing strings to translate are associated with user interface components implemented using Qt, we standardized…
  </blockquote>
</aside>


---
