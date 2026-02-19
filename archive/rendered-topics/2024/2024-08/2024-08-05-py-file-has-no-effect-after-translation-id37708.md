---
topic_id: 37708
title: "Py File Has No Effect After Translation"
date: 2024-08-05
url: https://discourse.slicer.org/t/37708
---

# Py file has no effect after translation

**Topic ID**: 37708
**Date**: 2024-08-05
**URL**: https://discourse.slicer.org/t/py-file-has-no-effect-after-translation/37708

---

## Post #1 by @MikhayEeer (2024-08-05 16:04 UTC)

<p>Hello, I built the source code of slicer according to the instructions in the document, and used update_translation.py to generate .ts files. However, when I opened the software and used the languagetools extension, I found that <strong>some translation items did not take effect</strong>.<br>
Specifically, for example, the py files like <code>dataprobe.py</code> and under <code>Modules\Loadable\Segmentations\EditorEffects\Python\SegmentEditorEffects</code> paths, the modules corresponding to these python files have not been successfully translated.<br>
I am pretty sure I translated the strings of these files in QTLinguist. Also, to confirm that the translation is OK, I let Slicer5.7.0 direct installation use the .ts files I generated, and successfully saw the translation of DataProbe.py and SegmentEditorEffects in Slicer5.7.0.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec88f718e0e6d980f0c3e9609a8354d705d0e9f9.png" alt="This is the dataprobe translation display of slicer5.7.0" data-base62-sha1="xKu82qu3E8oTICjTbAs0QEPrk9z" width="199" height="95"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f7316f3264eb33912c303597eb66492fbe70dff.png" alt="This is the dataprobe translation display of slicer source code build version" data-base62-sha1="bkQivOmgvQdhLwVwZS4IV8xFoYf" width="243" height="99"><br>
In order to find out the reason, I pulled the latest code of Slicer (<a href="https://github.com/Slicer/Slicer" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Slicer/Slicer: Multi-platform, free open source software for visualization and image computing.</a>), and used the vscode plug-in CompareFolders to compare my code with the official code. Almost all relevant changes were synchronized, but in the end these modules were still not translated.<br>
When I was building the slicer source code, I used QT5.15.2. I vaguely remember that the developer said that the translation of the python file needs to use Qt6. So I want to know if this is the reason why I can’t translate it. Can I change all QT-related configuration items to QT6 in the CMake stage of source code building?<br>
Or, if I update the Qt used to build the source code to QT6, can it solve my problem?<br>
Looking forward to your answer, thank you very much!</p>

---

## Post #2 by @MikhayEeer (2024-08-07 07:40 UTC)

<p>I saw that the community has discussed the development of the Qt6 version of Slicer. Is there any result now? Where can I download the Qt6 version of Slicer?</p>

---

## Post #3 by @lassoan (2024-08-07 09:12 UTC)

<p>We are still working on preparing all libraries that Slicer relies on to becompatible with Qt6. Qt6 is not needed for translation and any translation related problems are unrelated to Qt5/6.</p>
<p>If you find any text that cannot be translated in the very latest Slicer Preview Release then you can file a bug report at <a href="http://issues.slicer.org">issues.slicer.org</a>.</p>

---

## Post #4 by @MikhayEeer (2024-08-07 09:35 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="37708">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We are still working on preparing all libraries that Slicer relies on to becompatible with Qt6. Qt6 is not needed for translation and any translation related problems are unrelated to Qt5/6.</p>
</blockquote>
</aside>
<p>Thank you for your reply. Since the translation problem are unrelated to Qt5/6, I will check my code changes carefully.</p>

---
