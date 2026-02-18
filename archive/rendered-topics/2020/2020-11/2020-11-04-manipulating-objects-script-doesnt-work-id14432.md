# Manipulating objects script doesn't work

**Topic ID**: 14432
**Date**: 2020-11-04
**URL**: https://discourse.slicer.org/t/manipulating-objects-script-doesnt-work/14432

---

## Post #1 by @mau_igna_06 (2020-11-04 17:28 UTC)

<p>The script is <a href="https://www.slicer.org/wiki/Documentation/4.10/ScriptRepository#Manipulating_objects_in_the_slice_viewer" rel="noopener nofollow ugc">this one</a>. The drawn circle should be updated in relation to the two fiducials position but after is created it doesn’t update with a modification to the position of the fiducials. I added this line logging.debug(‘function executes’) to UpdateSphere definition and it never executes</p>

---

## Post #2 by @lassoan (2020-11-04 17:31 UTC)

<p>You need to use the script repository examples that match the Slicer version. Your link points to 4.10 version and that works with Slicer-4.11. For the latest version, you need to use this link: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Manipulating_objects_in_the_slice_viewer">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Manipulating_objects_in_the_slice_viewer</a></p>

---
