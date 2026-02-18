# Shortcuts on mac os

**Topic ID**: 28094
**Date**: 2023-02-28
**URL**: https://discourse.slicer.org/t/shortcuts-on-mac-os/28094

---

## Post #1 by @mohammed_alshakhas (2023-02-28 15:35 UTC)

<p>i noticed over a long time that shortcuts occasionally stop working then return again. other times it doesn’t work again until I restart slicer</p>
<p>this happens occasionally over many versions of slicer</p>

---

## Post #2 by @hherhold (2023-02-28 15:53 UTC)

<p>I have noticed this as well, and I’ve wondered if it’s a keyboard focus issue (maybe with Qt). Sometimes if I click in a certain window or pane, shortcuts start working again.</p>

---

## Post #3 by @jamesobutler (2023-02-28 17:49 UTC)

<p>Yes keyboard shortcuts often depend on a current focus. For example if you have a shortcut for say the letter “z” to do some action on the main window, that shortcut won’t trigger if you are in a typing field writing out “zoo” for example.</p>
<p>Can you provide details about the shortcut that seems to not work at times? Then hopefully we can narrow down whether it is an issue with the key sequence and how it is triggered when using various widgets.</p>

---

## Post #4 by @mohammed_alshakhas (2023-03-01 08:01 UTC)

<p>in my experience, the shortcuts are related to segmentation like the space bar, numbers, Cmd+Z.</p>
<p>the times I remember it, it starts whenever I open a file starting working on it. closing it and restarting slicer helps sometimes and sometimes I noticed it returning without doing anything</p>

---

## Post #5 by @jamesobutler (2023-03-01 15:05 UTC)

<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#keyboard-shortcuts" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#keyboard-shortcuts</a></p>
<p>Yes so for case of pressing “space” to toggle between segment editor effects that is only enabled when the active module is SegmentEditor and the focus isn’t elsewhere such as in the python console. If the focus is the python console, then the space will trigger in the console field as adding a space. However if you click back into the module panel or slice views, it will know that pressing space means to toggle between segment editor effects.</p>

---

## Post #6 by @mohammed_alshakhas (2023-03-01 17:06 UTC)

<p>actually when it happens, it continues regardless of where the focus on.<br>
you are describing normal software behavior , but the one I’m reporting is different</p>

---

## Post #7 by @lassoan (2023-03-01 18:33 UTC)

<p>It would be great if you could figure out a minimum set of steps to reliably reproduce it. We could then investigate and fix the issue.</p>

---

## Post #8 by @mohammed_alshakhas (2023-03-02 04:56 UTC)

<p>last time it happened . opened a dcm then started segmenting . no shortcut was working . i kept working for 10 minutes or so then shortcuts started working again .</p>
<p>same exact scenario happened few times before §</p>

---

## Post #9 by @lassoan (2023-03-03 05:57 UTC)

<p>You need to be more specific. For example, describe what data you loaded and then every clicks you made.</p>

---

## Post #10 by @mohammed_alshakhas (2023-03-28 13:33 UTC)

<p>it happens when I load dicom, then start segmentation. Shortcuts to editing effects like number 2 or 4 won’t work.  in these instances, all shortcuts won’t work</p>

---

## Post #11 by @lassoan (2023-03-28 13:41 UTC)

<p>Please provide a list of every click you make after you start the application. If repeating those clicks results in incorrect behavior on a developer’s computer then the problem will be fixed. If we cannot reproduce a problem then we cannot fix it.</p>

---
