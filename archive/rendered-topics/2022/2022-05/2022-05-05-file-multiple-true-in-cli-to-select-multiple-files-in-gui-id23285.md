---
topic_id: 23285
title: "File Multiple True In Cli To Select Multiple Files In Gui"
date: 2022-05-05
url: https://discourse.slicer.org/t/23285
---

# <file multiple="true"> in CLI to select multiple files in GUI

**Topic ID**: 23285
**Date**: 2022-05-05
**URL**: https://discourse.slicer.org/t/file-multiple-true-in-cli-to-select-multiple-files-in-gui/23285

---

## Post #1 by @gaoyi.cn (2022-05-05 07:34 UTC)

<p>Dear all,</p>
<p>In CLI xml file, although the tag  support multiple files in the command line calling of the CLI module, in the GUI, the file selection dialog box does not allow selection of multiple files (using, say, shift or ctrl keys). I read this notice on wiki:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/SlicerExecutionModel" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/Developers/SlicerExecutionModel</a></p>
<p>Limitation: the automatically built GUI will not support selecting multiple volumes for the <strong>image</strong> and <strong>pointfile</strong> argument, but they can be passed on the command line.</p>
<p>Could I know if there is a solution to do multiple file selection in GUI?</p>
<p>Thanks!<br>
yi</p>

---

## Post #2 by @pieper (2022-05-05 13:07 UTC)

<p>Hi Yi -</p>
<p>Thanks for the report - I don’t think anyone has looked at that code in a while.  I’m sure you remember the old days when Jim and Bill were adding this functionality to slicer3 and there was a lot of activity (ahh, the old days…).  It’s possible that when this feature was ported to Qt for slicer4 this feature was missed.  If it’s in your critical path it should be possible to track down and add this option to the dialog.  The limitation you cite is for the mrml node combo boxes, but the file dialogs should be workable.</p>
<p>-Steve</p>

---

## Post #3 by @lassoan (2022-05-06 01:11 UTC)

<p>The feature could be added for both node and file selectors. For file selectors it would be probably pretty easy (just enable multi-select in a standard file dialog). For node selectors we could use <code>qMRMLCheckableNodeComboBox</code> or <code>qMRMLSubjectHierarchyTreeView</code> - they both support multi-select.</p>

---

## Post #4 by @gaoyi.cn (2022-06-24 13:47 UTC)

<p>Hi Steve, Hi Andras,</p>
<p>The CLI “file multiple” corresponds to a ctkPathLineEdit. In the ctkPathLineEdit.cpp line 651, it opens a QFileDialog through a static function getOpenFileName(), which returns a QString.</p>
<p>However, the static function version getOpenFileNames() (with an “s” at the end) opens multiple files returns a QStringList.</p>
<p>According to</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/000162ec909c569c9e18b38a0e741b6199afffc7.png" data-download-href="/uploads/short-url/2Yacv8P66NWBR5viy5aWAPmBh.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/000162ec909c569c9e18b38a0e741b6199afffc7.png" alt="image" data-base62-sha1="2Yacv8P66NWBR5viy5aWAPmBh" width="690" height="215" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2411×754 12.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The same CLI xml tag  may return a std::string or a std::vector<a>std::string</a>, depending on the “multiple” switch.</p>
<p>I guess changing this may affect several places that uses this CLI mechanism.</p>
<p>Please advice a direction and i can try work on this.</p>
<p>Best,<br>
yi</p>

---

## Post #5 by @pieper (2022-06-24 13:56 UTC)

<p>Hi <a class="mention" href="/u/gaoyi.cn">@gaoyi.cn</a>  - I think it’s worth getting this fixed, but I agree there may be some side effects.  We could spot-check the CLIs in the core and some extensions to see if this would be a breaking change.  At first thought I don’t think it’s likely to be a big problem.</p>

---

## Post #6 by @lassoan (2022-06-25 05:04 UTC)

<p>File input and output is rarely used (as inputs and outputs are usually nodes or simple parameter values). Where files were used as input/output it was always just a single file (there is no CLI in Slicer that uses <code>file multiple="true"</code>). So, it is unlikely that adding support for multiple input/output files would cause a problem anywhere.</p>

---
