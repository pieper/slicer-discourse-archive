---
topic_id: 11435
title: "Connecting To A Remote Dicom Server Through Proxy"
date: 2020-05-06
url: https://discourse.slicer.org/t/11435
---

# Connecting to a remote DICOM server through proxy

**Topic ID**: 11435
**Date**: 2020-05-06
**URL**: https://discourse.slicer.org/t/connecting-to-a-remote-dicom-server-through-proxy/11435

---

## Post #1 by @kleingeo (2020-05-06 15:44 UTC)

<p>With the current state of everything I am working from home. I currently have a DICOM server at work that I require to be able to interface with. I am on Windows 10 and I am currently able to connect to the server through WinSCP, but that requires a proxy jump to work. Is it possible to connect Slicer to the DICOM server, or somehow have DICOM read the folders? At work, I have the server set-up as a Samba network drive and have Slicer read that, but I am unsure how to do this from home. Does anyone have an ideas?</p>

---

## Post #2 by @pieper (2020-05-06 16:43 UTC)

<p>I suppose some sort of VPN is the most general solution rather than doing something specific for Slicer.  When you say DICOM server at work, so you mean you use DICOM networking (CGET, CFIND, etc) or do you mean it’s a file share with DICOM files?</p>

---

## Post #4 by @kleingeo (2020-05-06 17:45 UTC)

<p>Either honestly. It is an othanc dicom server, but I could also just access the raw files.</p>

---

## Post #5 by @pieper (2020-05-06 19:10 UTC)

<p>I’m not familiar with WinSCP, but it you have access to command-line ssh to the machine in question (via a shell) you could tunnel the dicom port, like what’s <a href="https://www.ssh.com/ssh/tunneling/example">described here</a>.  You would need to know the IP and port information.</p>

---

## Post #6 by @kleingeo (2020-05-06 19:44 UTC)

<p>I do have cmd line ssh and have most of the proxy stuff saved in a OpenSSH config file. Not sure if that makes it easier or not.</p>

---

## Post #7 by @pieper (2020-05-06 20:00 UTC)

<p>If you access the pacs via dicom networking then you could do something like:</p>
<pre><code class="lang-auto">ssh ${pacshost} -L 104:localhost:104
</code></pre>
<p>then configure Slicer to do dicom networking to localhost port 104 instead of <code>pacshost</code> 104.</p>

---

## Post #8 by @kleingeo (2020-05-08 02:40 UTC)

<p>I’m not entirely sure how to use that information.</p>

---

## Post #9 by @pieper (2020-05-08 12:13 UTC)

<p>Fair enough, that’s probably not a good approach for you then.</p>
<p>If you have access to the data via a file system on a remote machine, then you really just need to investigate file sharing options.  There are many ways to do this these days and the best solution depends on the details of your setup, but dropbox, google drive, and other off the shelf solutions are options to investigate.</p>

---

## Post #10 by @lassoan (2021-05-17 13:14 UTC)

<p>You may also ask for DICOMweb enabled on the Orthanc server and use DICOMweb extensions to browse the server and download/upload data. DICOMweb can use various standard authentication methods (password, token, etc).</p>

---
