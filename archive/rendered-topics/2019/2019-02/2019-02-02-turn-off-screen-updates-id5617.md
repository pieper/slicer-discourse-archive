# Turn off screen updates

**Topic ID**: 5617
**Date**: 2019-02-02
**URL**: https://discourse.slicer.org/t/turn-off-screen-updates/5617

---

## Post #1 by @holmesrb (2019-02-02 12:47 UTC)

<p>Is there a python command to turn off screen updating whilst a large number of operations (mainly file loading) takes place please?</p>

---

## Post #2 by @lassoan (2019-02-02 14:00 UTC)

<p>You can start batch processing state in the scene, load all data, then end batch processing. It will prevent most view updates during loading, but there may be progress bars or other GUI updates that may be prevented using different approaches.</p>

---
