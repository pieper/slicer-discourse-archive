---
topic_id: 8879
title: "Cannot Install Latest Preview On Macos"
date: 2019-10-23
url: https://discourse.slicer.org/t/8879
---

# Cannot install latest Preview on macOS

**Topic ID**: 8879
**Date**: 2019-10-23
**URL**: https://discourse.slicer.org/t/cannot-install-latest-preview-on-macos/8879

---

## Post #1 by @Fernando (2019-10-23 17:22 UTC)

<p>Hi all,</p>
<p>I get this on Finder:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a2e4708291b59793d627e60fd681ad214ef40fb.png" data-download-href="/uploads/short-url/1s3VgN3gug38ArWogrHQ0l72goH.png?dl=1" title="09" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a2e4708291b59793d627e60fd681ad214ef40fb_2_345x228.png" alt="09" data-base62-sha1="1s3VgN3gug38ArWogrHQ0l72goH" width="345" height="228" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a2e4708291b59793d627e60fd681ad214ef40fb_2_345x228.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a2e4708291b59793d627e60fd681ad214ef40fb_2_517x342.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a2e4708291b59793d627e60fd681ad214ef40fb_2_690x456.png 2x" data-dominant-color="EBECED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">09</span><span class="informations">734×486 17.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And this within the error lines of <code>brew</code>:</p>
<pre><code class="lang-auto"> (miniconda3)  ~/git  brew cask reinstall slicer-nightly                                                                                ✓  62% (1:38) 🔋  3.49 Dur  17:40:53
==&gt; Satisfying dependencies
==&gt; Downloading https://download.slicer.org/bitstream/1123751
==&gt; Downloading from http://slicer.kitware.com/midas3/download?bitstream=1123751
######################################################################## 100.0%
==&gt; No SHA-256 checksum defined for Cask 'slicer-nightly', skipping verification.
==&gt; Uninstalling Cask slicer-nightly
==&gt; Purging files for version latest of Cask slicer-nightly
==&gt; Installing Cask slicer-nightly
hdiutil: attach failed - no mountable file systems
==&gt; Purging files for version latest of Cask slicer-nightly
Error: Failure while executing; `hdiutil attach -plist -nobrowse -readonly -noidme -mountrandom /var/folders/rp/779zzrds13q7z93s151_mv440000gn/T/d20191023-73477-prsgh9 /var/folders/rp/779zzrds13q7z93s151_mv440000gn/T/d20191023-73477-prsgh9/cfd4a367e042671e5575fac3c657ab36d5aafb8af133df11bef20a4b9e9459c3--Slicer-4.11.0-2019-10-21-macosx-amd64.cdr` exited with 1. Here's the output:
hdiutil: attach failed - no mountable file systems
</code></pre>

---

## Post #2 by @pieper (2019-10-23 17:37 UTC)

<p>I can confirm I get the same dialog when trying to open today’s preview from <a href="http://download.slicer.org" rel="nofollow noopener">download.slicer.org</a>.</p>

---

## Post #3 by @Sam_Horvath (2019-10-23 17:38 UTC)

<p>Hi Fernando:</p>
<p>This appears to be caused by an upload error on the Midas server.  See: <a href="http://slicer.cdash.org/viewBuildError.php?buildid=1728377" rel="nofollow noopener">http://slicer.cdash.org/viewBuildError.php?buildid=1728377</a><br>
I frequently see this error (i.e. upload failed), but it is generally a false positive, and the package is uploaded and functional.  No idea why it corrupted the file this time.  Anyway, i have grabbed the package off the build factory and posted it here: <a href="https://data.kitware.com/#item/5db08f85e3566bda4b0a88c5" rel="nofollow noopener">https://data.kitware.com/#item/5db08f85e3566bda4b0a88c5</a></p>

---

## Post #4 by @Fernando (2019-10-24 10:59 UTC)

<p>Thanks <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a>!</p>

---

## Post #5 by @Fernando (2019-10-25 09:30 UTC)

<p>Today’s preview works fine.</p>

---
