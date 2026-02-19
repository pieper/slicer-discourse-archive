---
topic_id: 22714
title: "Real Time Processing Of Data Retrieved From A Plus Server"
date: 2022-03-28
url: https://discourse.slicer.org/t/22714
---

# Real-time processing of data retrieved from a Plus Server

**Topic ID**: 22714
**Date**: 2022-03-28
**URL**: https://discourse.slicer.org/t/real-time-processing-of-data-retrieved-from-a-plus-server/22714

---

## Post #1 by @lb123 (2022-03-28 07:32 UTC)

<p>Hi,</p>
<p>I am trying to process in real-time the data retrieved from a Plus Server and then visualise it in Slicer.<br>
The only way I was able to handle this problem until now is the following:</p>
<ul>
<li>In an external python script I initialised a client using pyigtl that retrieve the data.</li>
<li>In the same external script the data is processed.</li>
<li>In the same external script I initialised also a server using pyigtl that streams the processed data.</li>
<li>In Slicer  using the OpenIGTLinkIF module I defined a client that retrieves the processed data from the server of the external script.</li>
</ul>
<p>This works. However this workflow is not efficient.</p>
<p>Is there any way to process the data retrieved from a Plus server in real-time directly in Slicer?</p>
<p>Thank you</p>

---
