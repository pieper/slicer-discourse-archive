---
topic_id: 19084
title: "Girder Integration"
date: 2021-08-05
url: https://discourse.slicer.org/t/19084
---

# Girder Integration

**Topic ID**: 19084
**Date**: 2021-08-05
**URL**: https://discourse.slicer.org/t/girder-integration/19084

---

## Post #1 by @vickyapril02 (2021-08-05 14:25 UTC)

<p>Hi,</p>
<p>We are a newbie  to 3D Slicer , and we are using Girder as a Data Management Tool for our project.<br>
We are planning to integrate Girder with 3D Slicer.</p>
<p>Any leads would be a great help for our team</p>
<p>Thanks and Regards<br>
Vicky</p>

---

## Post #2 by @lassoan (2021-08-05 14:28 UTC)

<p>We use Girder’s Python client in Slicer in a generic way (download data and then load it into Slicer). Maybe <a class="mention" href="/u/ungi">@ungi</a> can provide more details.</p>
<p>You can also just download data from a URL of data hosted on girder. See example <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#load-volume-from-a-remote-server">here</a>.</p>

---

## Post #3 by @ungi (2021-08-05 15:54 UTC)

<p>I’m not very experienced in girder. I use the girder-client Python package to download files from girder. I don’t use it in a Slicer module but it should work the same way. E.g. this function downloads a list of files from girder (for training ai): <a href="https://github.com/SlicerIGT/aigt/blob/eb2c007dbfed66cf7a59996e6b5f368b52a8ba91/utils.py#L45" class="inline-onebox" rel="noopener nofollow ugc">aigt/utils.py at eb2c007dbfed66cf7a59996e6b5f368b52a8ba91 · SlicerIGT/aigt · GitHub</a></p>

---

## Post #4 by @vickyapril02 (2021-08-06 07:57 UTC)

<p>Thanks for the lead ,let us try the method as you stated.</p>

---

## Post #5 by @vickyapril02 (2021-08-06 08:08 UTC)

<p>Thanks for the quick response and the tips.</p>

---
