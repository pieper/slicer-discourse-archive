# Sudden slowing in slicer

**Topic ID**: 16257
**Date**: 2021-02-27
**URL**: https://discourse.slicer.org/t/sudden-slowing-in-slicer/16257

---

## Post #1 by @mohammed_alshakhas (2021-02-27 11:38 UTC)

<p>after a long process of segementation i face significant slowing in any thing i do even scrolling through slices .</p>
<p>any suggestion ?</p>
<p>thanks</p>

---

## Post #2 by @mohammed_alshakhas (2021-02-27 11:40 UTC)

<p>i have the log but could not post it , too many characters</p>

---

## Post #3 by @lassoan (2021-02-27 13:04 UTC)

<p>You can upload the log file somewhere (Dropbox, OneDrive, Google drive) and post the link here.</p>
<p>Does the performance improve if you save the scene, restart your computer, start Slicer and load the scene?</p>

---

## Post #4 by @mohammed_alshakhas (2021-02-27 13:32 UTC)

<p>it doesn’t get better , i actually now realize that issue occurred before , however i though the file has an  issue itself .</p>
<p>once this occurs , working on the same file becomes extremely slow</p>
<p><a href="https://app.box.com/s/ju2eqobtha98pwclzy17bzmdl82t2mww" class="onebox" target="_blank" rel="noopener nofollow ugc">https://app.box.com/s/ju2eqobtha98pwclzy17bzmdl82t2mww</a></p>

---

## Post #5 by @lassoan (2021-02-27 14:13 UTC)

<p>The log file indicates that “Grow from seeds” effect is in progress and auto-update is enabled. This means that after each segment change, the auto-update is executed, which may be time-consuming. Go to Grow from seeds effect and click <code>Cancel</code> to cancel region growing and edit segments normally.</p>

---
