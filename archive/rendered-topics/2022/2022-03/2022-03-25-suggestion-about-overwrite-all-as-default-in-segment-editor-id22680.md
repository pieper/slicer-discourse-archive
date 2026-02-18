# Suggestion about overwrite all as default in segment editor

**Topic ID**: 22680
**Date**: 2022-03-25
**URL**: https://discourse.slicer.org/t/suggestion-about-overwrite-all-as-default-in-segment-editor/22680

---

## Post #1 by @Hannnonk (2022-03-25 12:58 UTC)

<p>Just a thought…why is “overwrite all” the default with logical operators, and threshold, etc? It seems that “allow overlap” would be a better default as you can always go back and subtract?<br>
Maybe I am missing some logic here, but here was my recent path-</p>
<ol>
<li>work on segment 1</li>
<li>create new segment, do a threshold etc, which erases my segment 1 unbeknownst to me…then I save and lose segment 1…</li>
</ol>
<p>I know I should save files at every step…and I am a veteran of your program and I huge fan…I just forgot about the overwrite all default…</p>
<p>Anyway just thought I would share this thought.</p>

---

## Post #2 by @lassoan (2022-03-25 14:31 UTC)

<p>The current default setting is chosen because the most common reason for segmentation is to partition the 3D volume into non-overlapping regions. Risk of losing information is limited because undo is available.</p>
<p>If you find that usually you need to allow overlap then you can change the default setting by editing the Slicer startup file as described <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#set-default-segmentation-options">here</a>.</p>
<p>It would not be hard to make this adjustable more conveniently in the application settings, but the question has not come up too many times and changing the startup file seems to be an acceptable solution. But if you think that it would be important to have an application settings for this then you can submit a feature request to the <a href="https://github.com/Slicer/Slicer/issues">issue tracker</a>. If many people votes on the issue then we’ll implement the feature.</p>

---
