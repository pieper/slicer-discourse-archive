---
topic_id: 47346
title: "download fails/freezes on both direct connection and VPN (with academic license activated)"
date: 2026-06-15
url: https://discourse.slicer.org/t/47346
last_bumped: 2026-09-29T06:38:13.352Z
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

## Post #3 by @Jingtao_Chen (2026-07-13 17:17 UTC)

<p>Hi <a class="mention" href="/u/tomy_roster">@Tomy_Roster</a>,</p>
<p>I saw your post about the <code>tissue_4_types</code> download issue. I’m experiencing exactly the same problem — the download stalls at around 86% (202MB/233MB) with <code>IncompleteRead</code> / <code>ChunkedEncodingError</code>.</p>
<p>I’ve also tried using a VPN but it didn’t help.</p>
<p>Were you able to resolve this issue? Did you find a way to get the weights or a direct download link?</p>
<p>Any advice would be greatly appreciated!</p>
<p>Thanks!</p>

---

## Post #4 by @bjmufffff (2026-09-29 06:38 UTC)

<p>Encountered the same issue: the weights could not be downloaded and kept reporting errors.Here is my solution just for reference (as everyone’s network environment is different):</p>
<p>Referring to the official documentation ( <a href="https://github.com/wasserth/TotalSegmentator/blob/master/README.md" class="inline-onebox" rel="noopener nofollow ugc">TotalSegmentator/README.md at master · wasserth/TotalSegmentator · GitHub</a> ),<br>
Set up  Python environment on my computer (separate from 3D Slicer’s Python), install TotalSegmentator with <code>pip install TotalSegmentator</code>,</p>
<p>set the license with <code>totalseg_set_license -l aca_12345678910</code>,</p>
<p>successfully downloaded the weights with <code>totalseg_download_weights -t &lt;task_name&gt;</code> (with VPN  global mode).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/742fe231c13f40dad26aed2759cd3248af7270d2.png" data-download-href="/uploads/short-url/gzPYyflZ8OorPJxBakc5hdOepj4.png?dl=1" title="1790663722167" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/742fe231c13f40dad26aed2759cd3248af7270d2.png" alt="1790663722167" data-base62-sha1="gzPYyflZ8OorPJxBakc5hdOepj4" width="690" height="56" data-dominant-color="1D1D1D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1790663722167</span><span class="informations">1252×102 1.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b38db599f64a794e9784452306c61c0cd60ba0b8.png" data-download-href="/uploads/short-url/pCp4QrdD72phaax9SWvblV7hsEg.png?dl=1" title="1790663755330" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b38db599f64a794e9784452306c61c0cd60ba0b8_2_649x500.png" alt="1790663755330" data-base62-sha1="pCp4QrdD72phaax9SWvblV7hsEg" width="649" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b38db599f64a794e9784452306c61c0cd60ba0b8_2_649x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b38db599f64a794e9784452306c61c0cd60ba0b8_2_973x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b38db599f64a794e9784452306c61c0cd60ba0b8.png 2x" data-dominant-color="ABAAAF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1790663755330</span><span class="informations">1288×992 221 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
