# Simplify Slicer or Remove some modules from Slicer

**Topic ID**: 7545
**Date**: 2019-07-12
**URL**: https://discourse.slicer.org/t/simplify-slicer-or-remove-some-modules-from-slicer/7545

---

## Post #1 by @mikecsu (2019-07-12 06:13 UTC)

<p>Operating system:win10<br>
Slicer version:4.10.0<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hi,everyone. I am studying on the source code of slicer 4.10.0 and i am wondering<br>
if it is possible to cut off some modules (that i may never use) from slicer,<br>
cause now there are too many of them, which sometimes make it difficult and<br>
time-consuming to find the module that i really want .</p>
<p>and also i tend to simplify some specific  modules by only maintaining some<br>
functionalities that i want. So i would like to know if it is possible to do that?<br>
And are there any suggestions can be offered to me to help me to do this task ?</p>
<p>Thanks in advance !</p>

---

## Post #2 by @jcfr (2019-07-12 08:06 UTC)

<p>If you would like to disable some modules you could do it:</p>
<ul>
<li>directly from Slicer by disabling specific modules in the application settings (or using the <code>--disable-modules</code> command line option)</li>
<li>or you could at build time setting these options: <a href="https://discourse.slicer.org/t/can-you-explain-the-cmake-variables-slicer-moduletype-modules-disabled-enabled/7494/2" class="inline-onebox">Can you explain the CMake variables Slicer_&lt;moduleType&gt;MODULES_DISABLED|ENABLED? - #2 by jcfr</a></li>
</ul>
<blockquote>
<p>tend to simplify some specific modules by only maintaining some functionalities that i want.</p>
</blockquote>
<p>Modules are composed integrating widgets. This means you could easily create your own module re-using widgets provided by other module.</p>
<p>Here are example of re-usable module widgets and associated Qt designer plugins: <a href="https://github.com/Slicer/Slicer/tree/master/Modules/Loadable/Markups/Widgets" class="inline-onebox">Slicer/Modules/Loadable/Markups/Widgets at main · Slicer/Slicer · GitHub</a></p>
<p>If an existing module doesn’t provide re-usable components, let us know and we can provide guidance to refactor the code.</p>
<p>It is also possible to improve existing widgets to give you the required flexibility to craft your own module.</p>

---

## Post #3 by @cpinter (2019-07-12 12:48 UTC)

<p>I think what would be ideal for you is a slicelet or a Slicer custom app<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets</a></p>
<p>Let us know if you need help.</p>

---

## Post #4 by @mikecsu (2019-07-15 06:41 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/jcfr">@jcfr</a>  Thanks for the extremely helpful reply. I tried and it works very well .<br>
But for the widget part, i still have problems which comes from the combination of<br>
C++ and Python, i assume.</p>
<p>More specific, in segment editor module, the main frame is achieved in C++ and Qt.<br>
But when it comes to the “Effects”(see pic 1 below, red rectangle), all of them are<br>
achieved with Python, so i am confused and don’t know how to do,  cause i only<br>
want part of them and delete/hide others.  For example, i only want to keep some<br>
functionalities in yellow circle(see pic 2 ). Any advice ?</p>
<p><strong>pic 1</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/cee3b9727b2f358f69e0baa08947d8e38acea36d.png" data-download-href="/uploads/short-url/twefSOFPlH6vpRGXczYNsiKfBpz.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/cee3b9727b2f358f69e0baa08947d8e38acea36d.png" alt="image" data-base62-sha1="twefSOFPlH6vpRGXczYNsiKfBpz" width="549" height="500" data-dominant-color="F9F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">615×560 14.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>pic 2</strong><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27a9a713919695d63f853101cec8cf448440ff8f.png" alt="image" data-base62-sha1="5ES6e9O8fR0XCyMyWG6bSYpCwG3" width="613" height="478"></p>

---
