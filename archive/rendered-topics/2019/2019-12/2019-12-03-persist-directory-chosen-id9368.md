---
topic_id: 9368
title: "Persist Directory Chosen"
date: 2019-12-03
url: https://discourse.slicer.org/t/9368
---

# Persist directory chosen

**Topic ID**: 9368
**Date**: 2019-12-03
**URL**: https://discourse.slicer.org/t/persist-directory-chosen/9368

---

## Post #1 by @giovform (2019-12-03 14:55 UTC)

<p>Hi! I was wondering, what is the best way to persist (after closing Slicer) the directory a user has chosen in a module I am creating. I initially thought about saving this information in .slicerrc.py and ended asking here because maybe there is some utility function to do this kind of thing.</p>
<p>Thanks!</p>

---

## Post #2 by @adamrankin (2019-12-03 15:11 UTC)

<p>I believe you have access to QSettings. You could use that with a well chosen prefix to save intersession values.</p>
<p>This is for users who don’t save their scenes. If you have users who save scenes, the module data should be baked into a MRML node of your creation (not as bad as you think).</p>

---

## Post #3 by @giovform (2019-12-03 16:48 UTC)

<p>Thanks Adam, the first solution is what I wanted.</p>

---
