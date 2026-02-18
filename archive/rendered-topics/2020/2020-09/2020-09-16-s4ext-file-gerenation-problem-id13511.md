# .s4ext File gerenation problem

**Topic ID**: 13511
**Date**: 2020-09-16
**URL**: https://discourse.slicer.org/t/s4ext-file-gerenation-problem/13511

---

## Post #1 by @Viniciuscob (2020-09-16 21:15 UTC)

<p>Hello,</p>
<p>My extension has already been submitted on github. Now, we just need to update the .s4ext file on Slicer github. However, we are having a hard time in this .s4ext file step. Searching the discussion forum, i found this:</p>
<aside class="quote quote-modified" data-post="15" data-topic="829">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/extensionwizard-not-uploading-my-extension/829/15">ExtensionWizard not uploading my extension</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    <a class="mention" href="/u/moselhy">@moselhy</a> You can find it in the build tree. For example: 
$ git clone https://github.com/moselhy/SequenceRegistration
$ mkdir SequenceRegistration-build
$ cd SequenceRegistration-build/
$ cmake -DCMAKE_BUILD_TYPE:STRING=Release -DSlicer_DIR:PATH=/home/jcfr/Projects/Slicer-2-build/Slicer-build/ ../SequenceRegistration

$ make -j6
[...]
-- Configuring Scripted module: Elastix4D
-- Extension description has been written to: /tmp/SequenceRegistration-build/SequenceRegistration.s4ext   &lt;------------…
  </blockquote>
</aside>

<p>The s4ext file is already generated, but is it not shown in the directory and this code will “find” it and provide me the file, or will this code generated the s4ext file from the CMakeLists?</p>
<p>Either way, i was able to run until the third command line of this code but something went wrong with the “cmake” command (fourth line). The GitBash is accessing the right folder but it is not finding the CMakeLists file or it is just accessing the wrong folder for some reason.</p>
<p>We don’t have much experience with GitHub, so it is being complicated to solve this…</p>

---

## Post #2 by @lassoan (2020-09-17 01:58 UTC)

<p>Automatic generation of s4ext file requires you to build Slicer. If you just created Python scripted modules then it is easier to create a .s4ext file using a text editor. You can use <a href="https://github.com/Slicer/ExtensionsIndex/">.s4ext files of existing extensions</a> as examples.</p>

---
