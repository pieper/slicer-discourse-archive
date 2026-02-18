# Packaged, distributable custom application with a slicelet

**Topic ID**: 3627
**Date**: 2018-08-01
**URL**: https://discourse.slicer.org/t/packaged-distributable-custom-application-with-a-slicelet/3627

---

## Post #1 by @mschumaker (2018-08-01 15:53 UTC)

<p>I’d like to create a packaged, distributable application using my slicelet and scripted modules. I’ve looked at the <a href="https://github.com/pieper/CustomSlicerGenerator" rel="noopener nofollow ugc">CustomSlicerGenerator</a>, and I know about the work on the <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate" rel="noopener nofollow ugc">SlicerCustomAppTemplate</a>, but with that still in progress, what’s the current procedure to create a custom, packaged application, starting with a slicelet?</p>
<p>So far, I understand that the icons and images that are used when compiling are in the Slicer/Applications/SlicerApp/Resources directory, and the qrc file needs to set the aliases for it, and I have seen the list of CMake variables to add. What I still don’t know is how to invoke a slicelet at startup, when the application has been packaged.</p>
<aside class="quote quote-modified" data-post="8" data-topic="564">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/customized-application-launchers/564/8">Customized application launchers</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Currently we customize these in our custom application packages: 

All application options defined <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Customizing_application_build" rel="noopener nofollow ugc">here</a>.
These resource files:

Applications\SlicerApp\Resources\Icons\Large(appname)-DesktopIcon.png
Applications\SlicerApp\Resources\Icons\Medium(appname)-DesktopIcon.png
Applications\SlicerApp\Resources\Icons\Small(appname)-DesktopIcon.png
Applications\SlicerApp\Resources\Icons\XLarge(appname)-DesktopIcon.png
Applications\SlicerApp\Resources\Icons\XXLarge(appname)-DesktopIcon.png
Applications\Slic…
  </blockquote>
</aside>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Customizing_application_build" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Customizing_application_build</a></p>

---

## Post #2 by @jcfr (2018-08-01 18:28 UTC)

<aside class="quote no-group" data-username="mschumaker" data-post="1" data-topic="3627">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mschumaker/48/1395_2.png" class="avatar"> mschumaker:</div>
<blockquote>
<p>with that still in progress, what’s the current procedure to create a custom, packaged application, starting with a slicelet?</p>
</blockquote>
</aside>
<p>The <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate">SlicerCustomAppTemplate</a> already allow to create fully functional Slicer based application.</p>
<p>I am currently working supporting the cast of “you main application is a Slicelet”, I will follow up when I have an update.</p>

---
