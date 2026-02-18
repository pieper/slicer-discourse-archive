# Unhide slicer Interface

**Topic ID**: 19658
**Date**: 2021-09-14
**URL**: https://discourse.slicer.org/t/unhide-slicer-interface/19658

---

## Post #1 by @S_Arbabi (2021-09-14 09:52 UTC)

<p>Hi,</p>
<p>Once I build customAppTemplate, the user interface has just few buttons for data loading and not all other slicer toolboxes. Then by clicking on the setting-like button:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/636aecf8f3a8b9a9a188d2e37598d449b99306c5.png" alt="Capture" data-base62-sha1="ebum7rbVtM0EZnRvpHyQeQ1MTKR" width="44" height="32"><br>
I can choose the slicer interface to appear<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/141bca6369a5ac715fb9befa184b78c9ffdaec97.png" alt="Capture2" data-base62-sha1="2RT5BGX95LPEowz9ozEHgd7EGN1" width="223" height="109"></p>
<p>and then I have access to all tools again.</p>
<p>I was wondering how can I make the slicer interface the default and remove this setting-like button?</p>
<p>Best</p>

---

## Post #2 by @S_Arbabi (2021-09-14 23:21 UTC)

<p>I found the solution. In modules/scripted/home there’s a python class file with two methods hideSlicerUI and showSlicerUI.</p>

---
