---
topic_id: 38231
title: "How To Set Proxy Node For A Sequence Node And Save"
date: 2024-09-05
url: https://discourse.slicer.org/t/38231
---

# How to set proxy node for a sequence node and save

**Topic ID**: 38231
**Date**: 2024-09-05
**URL**: https://discourse.slicer.org/t/how-to-set-proxy-node-for-a-sequence-node-and-save/38231

---

## Post #1 by @maniron (2024-09-05 09:43 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/9100ae8398faa4b56de05a93c9ccdf9ec54e1a36.png" data-download-href="/uploads/short-url/kGKH0JUwhYsWPuohQ6tkSbNAVlI.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/9100ae8398faa4b56de05a93c9ccdf9ec54e1a36.png" alt="image" data-base62-sha1="kGKH0JUwhYsWPuohQ6tkSbNAVlI" width="690" height="159" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">873×202 5.57 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I want to handle setting a proxy node for a sequence node and save it through python how can I do this Kindly help me out</p>
<p>I added a sequence through python which is getting listed in the sequences module</p>

---

## Post #2 by @maniron (2024-09-05 13:45 UTC)

<p>I want to access a combo box which is present in the sequence module widget through python Kindly help me out</p>

---

## Post #3 by @ssv (2024-09-06 05:09 UTC)

<p>Hello <a class="mention" href="/u/maniron">@maniron</a> ,</p>
<p>you can access sequence module any widget by using getModuleWidget in python console<br>
Here’s example:<br>
slicer.util.getModuleWidget(“Sequences”).findChild(“ctkComboBox”,“ComboBox_IndexType”)</p>

---

## Post #4 by @maniron (2024-09-06 05:37 UTC)

<p>Hi <a class="mention" href="/u/ssv">@ssv</a> thanks for replying it was useful but now I want to access the proxy node combo box, do you have any suggestion for that</p>

---

## Post #5 by @lassoan (2024-09-12 03:30 UTC)

<p>There is no need to access module GUI widgets. You can set up a proxy node by calling <a href="https://apidocs.slicer.org/master/classvtkMRMLSequenceBrowserNode.html#aba16a856688831e670c26c9f4cd7fc34">AddProxyNode method of the sequence browser node</a>.</p>

---
