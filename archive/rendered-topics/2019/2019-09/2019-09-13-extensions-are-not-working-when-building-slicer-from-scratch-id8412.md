# Extensions are not working when building Slicer from scratch

**Topic ID**: 8412
**Date**: 2019-09-13
**URL**: https://discourse.slicer.org/t/extensions-are-not-working-when-building-slicer-from-scratch/8412

---

## Post #1 by @fpsiddiqui91 (2019-09-13 12:41 UTC)

<p>Hello Developers,</p>
<p>I have built the Nightly version of slicer from scratch. The reason fro that is I want make my own CLI modules and Loadable modules.<br>
Everything seemed to be working until I had to download the extension packages.</p>
<p>When I was trying to install the extension pacakges from extension manager, It was showing " No extensions found for linux:64-bit"</p>
<p>After reading several solution in this forum I manually install the packages as explained here<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ#How_to_manually_install_an_extension_package.3F" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ#How_to_manually_install_an_extension_package.3F</a></p>
<p>But when I am trying to run the DWItoDTI Estimation module it gives me this error:</p>
<p><strong>path/to/cli-modules/DWIToDTIEstimation: error while loading shared libraries: libvtkDMRI.so: cannot open shared object file: No such file or directory</strong></p>
<p>And with Brain masking module it is giving me this error:</p>
<p><strong>path/to/cli-modules/DiffusionWeightedVolumeMasking: error while loading shared libraries: libITKIOJPEG-4.12.so.1: cannot open shared object file: No such file or directory</strong></p>
<p>Am I missing something?</p>

---

## Post #2 by @cpinter (2019-09-13 13:03 UTC)

<aside class="quote no-group" data-username="fpsiddiqui91" data-post="1" data-topic="8412">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/53a042/48.png" class="avatar"> fpsiddiqui91:</div>
<blockquote>
<p>download the extension packages</p>
</blockquote>
</aside>
<p>You cannot use factory-built extensions with your locally built Slicer. In that case you’ll need to clone and build the extensions you want to use.</p>
<p>See also for example</p><aside class="quote quote-modified" data-post="1" data-topic="1900">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kanderle/48/1100_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/loadable-module-crashing-binary-slicer/1900">Loadable module crashing binary Slicer</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    I have an error with my loadable module. I’ve built the Slicer stable version (revision 26489) and I’ve built my module against it without errors. The module works as intended when I launch the built Slicer version. However, if I try to launch module with the binary Slicer release (downloaded from the website, the 4.8.0 version - same as the built revision) the Slicer crashes before opening and I get the following error: 
“terminate called after throwing an instance of ‘H5::DataSpaceIException’” …
  </blockquote>
</aside>
<p>
or</p><aside class="quote quote-modified" data-post="1" data-topic="6750">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/b2d939/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/compiled-app-whichs-source-pulled-from-git-cannot-download-extension-due-to-reversion-not-match/6750">Compiled App whichs source pulled from git cannot download extension due to reversion not match.</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Problem report for Slicer 4.11.0-2019-05-01 win-amd64: [please describe expected and actual behavior] 
I compiled the Slicer reversion of “28202” which was pulled from github, and it’s reversion became “aae6a8c”, so that I can’t download extension from Extensions Manager online. The message from Extensions Manager says as below: 
“No extensions found for win:64-bit, revision: ‘aae6a8c’. Please try a different combination” 
After that I installed a SlicerVR extension, and it works well. 
Then I m…
  </blockquote>
</aside>


---

## Post #3 by @fpsiddiqui91 (2019-09-13 13:45 UTC)

<p>thanks, I have cloned the extensions and built it. It worked.<br>
Thanks alot</p>

---
