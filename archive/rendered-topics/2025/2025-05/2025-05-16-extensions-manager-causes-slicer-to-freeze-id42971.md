# Extensions manager causes Slicer to freeze

**Topic ID**: 42971
**Date**: 2025-05-16
**URL**: https://discourse.slicer.org/t/extensions-manager-causes-slicer-to-freeze/42971

---

## Post #1 by @ramenegaz (2025-05-16 18:26 UTC)

<p>Hello -</p>
<p>When I try to open the Extensions Manager, it’s causing 3D Slicer to freeze. I don’t get the “Extensions manager is starting, please wait…” message, just a spinning wheel.</p>
<p>I’ve tried both stable build 5.8.1 and preview version 5.9.0. I’ve also tried uninstalling and reinstalling, <a href="https://discourse.slicer.org/t/windows-not-responding-error-remains-after-reinstallation/42933">including the troubleshooting steps here.</a></p>
<p>This issue is only on one computer, so I don’t think it’s a server issue?</p>
<p>Thanks!<br>
RM</p>

---

## Post #2 by @muratmaga (2025-05-16 18:35 UTC)

<p>Go to <strong>/slicer.org/Extensions-XXXX/</strong> subfolder under your Slicer install tree, and delete <strong>ExtensionsMetadataFromServer.json</strong></p>
<p>and retry launching and extension manager.</p>
<p>If it keeps failing, it might be a network/firewall issue on that specific computer.</p>

---

## Post #3 by @ramenegaz (2025-05-29 20:15 UTC)

<p>Thanks, Murat!</p>
<p>Deleted the extensions .json file was unsuccessful. Our IT insists it can’t be the firewall because it works on most of our computers, just not the two most recently setup ones. Here was our workaround:</p>
<ul>
<li>
<p>One one computer, installing and running as adminstrator allowed us to use the Extension Manager.</p>
</li>
<li>
<p>On the other computer, admin didn’t work. We had to roll back the install to build 5.7 to use the Extension Manager.</p>
</li>
</ul>

---

## Post #4 by @lassoan (2025-06-01 12:13 UTC)

<p>Slicer is fully portable. You can copy all the files in the Slicer install folder to a USB stick and run from there. You can install it on any computer by simply copying the Slicer folder.</p>

---

## Post #5 by @PiasTanmoy (2025-11-19 00:00 UTC)

<p>The solution worked for me!</p>
<p>Thank you!</p>

---
