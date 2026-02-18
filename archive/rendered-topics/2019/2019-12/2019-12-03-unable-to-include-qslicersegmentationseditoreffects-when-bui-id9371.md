# Unable to include qSlicerSegmentationsEditorEffects when building extension

**Topic ID**: 9371
**Date**: 2019-12-03
**URL**: https://discourse.slicer.org/t/unable-to-include-qslicersegmentationseditoreffects-when-building-extension/9371

---

## Post #1 by @Netta_Z (2019-12-03 18:55 UTC)

<p>Hi, I’m trying to implement an editor effect as part of an extension. I’m having issues with accessing files from the qSlicerSegmentationsEditorEffects directory by declaring it in MODULE_INCLUDE_DIRECTORIES like so: <code>${qSlicerSegmentationsEditorEffects_INCLUDE_DIRS}</code> which I have seen this done in the segmentations module. However the directory was not accessible after cmake has configured and generated successfully. I tried declaring <code>${qSlicerSegmentationsModules_INCLUDE_DIRS}\EditorEffects</code> instead, but this only allowed me to access files in Slicer’s build directory not the source directory. What can I do to fix that?</p>
<p>Thanks in advance.</p>

---

## Post #2 by @Netta_Z (2019-12-04 17:28 UTC)

<p>I managed to include \EditorEffects of the Slicer’s source directory in my build by doing this:</p>
<pre><code>list(GET qSlicerSegmentationsModule_INCLUDE_DIRS 0 qSegmentationSource_DIR)
set(MODULE_INCLUDE_DIRECTORIES
  ${qSegmentationSource_DIR}/EditorEffects
}
</code></pre>
<p>However is there a preferred way to achieve this? Should I be referencing the EditorEffects API when I create a loadable editor effect?</p>

---

## Post #3 by @lassoan (2019-12-04 17:58 UTC)

<p>You can <a href="https://stackoverflow.com/questions/9298278/cmake-print-out-all-accessible-variables-in-a-script">print all CMake variables</a> to see what variables you can use to specify the include directory.</p>

---

## Post #4 by @Netta_Z (2019-12-04 18:50 UTC)

<p>Thanks for the reply. Following the instructions from your link I didn’t see a variable available for the editor effect directory specifically, which is why I was unsure if the qSlicerSegmentationsEditorEffects API was made “private” by design. Could you please confirm that it’s ok to reference the API the way I described in my previous post?</p>

---

## Post #5 by @lassoan (2019-12-04 19:07 UTC)

<p>The API is not private, you can make your effects based on existing C++ classes. If you can send a link to your source code then we can have a look at it and suggest how to make CMake work (and maybe expose more directories as CMake variables from Slicer).</p>

---

## Post #6 by @Netta_Z (2019-12-04 20:28 UTC)

<p>Sounds good! Here’s the CMakeList of the effect module(WIP):<br>
<a href="https://bitbucket.org/OrthopaedicBiomechanicsLab/slicersegmenteditorfastlogicaleffect/src/master/SegmentEditorFastLogical/CMakeLists.txt" class="onebox" target="_blank" rel="nofollow noopener">https://bitbucket.org/OrthopaedicBiomechanicsLab/slicersegmenteditorfastlogicaleffect/src/master/SegmentEditorFastLogical/CMakeLists.txt</a></p>

---

## Post #7 by @lassoan (2019-12-05 02:24 UTC)

<p>Thank you, this helped. I have a <a href="https://github.com/Slicer/Slicer/pull/1277">potential fix</a>, but <a class="mention" href="/u/jcfr">@jcfr</a> has to review first.</p>

---
