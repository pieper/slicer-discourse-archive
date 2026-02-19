---
topic_id: 25572
title: "Image Processing In Matlab"
date: 2022-10-06
url: https://discourse.slicer.org/t/25572
---

# Image processing in Matlab

**Topic ID**: 25572
**Date**: 2022-10-06
**URL**: https://discourse.slicer.org/t/image-processing-in-matlab/25572

---

## Post #1 by @PaoloZaffino (2022-10-06 13:40 UTC)

<p>Hi all,<br>
I have a matlab script that processes an image.<br>
I would like to load a volume in slicer, run the matlab script from slicer, and get the results back in matlab.<br>
Any example/idea of how to do this?</p>
<p>Thanks a lot,<br>
Paolo</p>

---

## Post #2 by @ebrahim (2022-10-06 14:05 UTC)

<p>You could use <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.launchConsoleProcess" rel="noopener nofollow ugc">launchConsoleProcess</a> to run your matlab script, but it will be a separate process and not have direct access to the volume you loaded into slicer. You would have to write out the volume in a format that can be ingested by your script, and then separately read in whatever the script wrote to disk.</p>
<p>There appears to be an extension <a href="https://github.com/PerkLab/SlicerMatlabBridge" rel="noopener nofollow ugc">SlicerMatlabBridge</a> but IDK how up to date it is given that its <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/MatlabBridge" rel="noopener nofollow ugc">documentation</a> is on the old wiki. It seems like this does what you want though</p>

---

## Post #3 by @PaoloZaffino (2022-10-10 10:23 UTC)

<p>Thanks <a class="mention" href="/u/ebrahim">@ebrahim</a></p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> do you have any suggestions?</p>

---

## Post #4 by @lassoan (2022-10-10 11:38 UTC)

<p>The MatlabBridge extension sites exactly what you describe. It should still work. There are examples in its documentation.</p>

---
