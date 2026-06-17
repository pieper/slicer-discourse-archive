---
topic_id: 47346
title: "download fails/freezes on both direct connection and VPN (with academic license activated)"
date: 2026-06-15
url: https://discourse.slicer.org/t/47346
last_bumped: 2026-06-16T12:44:05.316Z
---

# download fails/freezes on both direct connection and VPN (with academic license activated)

**Topic ID**: 47346
**Date**: 2026-06-15
**URL**: https://discourse.slicer.org/t/download-fails-freezes-on-both-direct-connection-and-vpn-with-academic-license-activated/47346

---

## Post #1 by @Tomy_Roster (2026-06-15 12:40 UTC)

<p>I am using the TotalSegmentator extension in 3D Slicer to extract muscle and fat compartments using the <code>tissue_4_types</code> subtask. I have already successfully obtained and activated my academic license key.</p>
<p>However, I am completely blocked by downloading errors when clicking “Apply” for the <code>tissue_4_types</code> task (while the default <code>total</code> task runs perfectly fine without any issues).</p>
<p><strong>To Reproduce / Network Symptoms</strong></p>
<p><strong>1.Without VPN (Direct Connection):</strong> The download process starts but is extremely slow. It consistently freezes/hangs at around 3MB and never progresses, eventually resulting in a connection timeout.</p>
<ol>
<li>
<p><strong>2.With VPN Enabled:</strong> The network completely fails to handshake with the model repository. 3D Slicer instantly throws an SSL/Connection error in the Python console and aborts the task <strong>Environment:</strong></p>
<ul>
<li>
<p><strong>OS:</strong> Windows 11;RTX 5060ti 8G</p>
</li>
<li>
<p><strong>Software:</strong> 3D Slicer (with TotalSegmentator extension)</p>
</li>
<li>
<p><strong>Task Mode:</strong> <code>tissue_4_types</code> with Academic License</p>
</li>
</ul>
<p><strong>Expected behavior</strong> Since my academic license is valid and entered, I expected the plugin to successfully download the <code>tissue_4_types</code> model weights and complete the segmentation.</p>
<p>Is there a known workaround for this network issue? Or could you please provide a <strong>direct download link</strong> (like Zenodo or Google Drive) for the <code>tissue_4_types</code> model weights so that I can manually place them into my local <code>.totalsegmentator</code> folder?</p>
<p>Thank you so much for your time and this amazing tool!.</p>
</li>
</ol>

---

## Post #2 by @Tomy_Roster (2026-06-16 12:44 UTC)

<p>​<strong>Update: License verified, but network drops mid-download (IncompleteRead error)</strong></p>
<p>​Hi again,</p>
<p>​Good news: My academic license is successfully verified now. However, I am facing a new network instability issue during the weight downloading process.</p>
<p>​The download starts successfully but always gets interrupted halfway. The Python console throws this error:</p>
<p>urllib3.exceptions.IncompleteRead: IncompleteRead(186127600 bytes read, 47091847 more expected)</p>
<p>followed by a ChunkedEncodingError. It seems my connection drops exactly at 186MB out of the 233MB file. Because the Slicer built-in downloader doesn’t support resuming broken downloads, I am completely stuck in a loop of failing mid-way.</p>
<p>​<strong>My Request:</strong></p>
<p>Due to the strict network firewall/instability in my hospital, could you please kindly provide a <strong>direct download link (e.g., a .zip file on Google Drive, Dropbox, or Zenodo)</strong> for the tissue_4_types (Task 485) model weights?</p>
<p>​If I can download it via a browser (which supports resume), I can manually extract it into my %USERPROFILE%\.totalsegmentator\nnunet\results folder.</p>
<p>​Thank you so much for your understanding and support!</p>

---
