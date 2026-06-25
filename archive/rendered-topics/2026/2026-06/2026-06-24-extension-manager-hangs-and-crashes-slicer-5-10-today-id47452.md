---
topic_id: 47452
title: "Extension manager hangs and crashes Slicer 5.10 today"
date: 2026-06-24
url: https://discourse.slicer.org/t/47452
last_bumped: 2026-06-25T03:11:07.601Z
---

# Extension manager hangs and crashes Slicer 5.10 today

**Topic ID**: 47452
**Date**: 2026-06-24
**URL**: https://discourse.slicer.org/t/extension-manager-hangs-and-crashes-slicer-5-10-today/47452

---

## Post #1 by @mikebind (2026-06-24 23:56 UTC)

<p>I am using Slicer 5.10 on Windows, and wanted to add the model to model distance extension today.  However, when I open the Extension Manager, I get a blank window and spinning waiting cursor for an indefinite period, apparently hanging.  If I try to close the window, Windows asks if I want to close end the process because it is not responding, and if I do that, it closes Slicer as well.  I don’t know if this could be related to <a href="https://discourse.slicer.org/t/release-of-slicer-5-12-in-progress/47440" class="inline-onebox">Release of Slicer 5.12 in progress</a> ?  In any case, it is disruptive to not be able to try to access the extension manager in a prior stable release, and if I had not saved my work prior to trying to open the extension manager, I would have lost that work as well since there was no way to close the extension manager window without force-closing Slicer.  I have used the extension manager many times in the past, including with my current Slicer installation and network configuration without problems, so that is why I suspect it is something on the remote end which could be the issue.  Is anyone else running into this problem?  Is it known that the extension manager is down temporarily due to the 5.12 release?  Thanks for any insight you can provide.</p>

---

## Post #2 by @lassoan (2026-06-25 02:32 UTC)

<p>The extension manager works the same way as before and there is no difference in how it displays extensions for various Slicer versions. Due to the extension builds for Slicer-5.12 were completed and uploaded to the extension server during the day, it is possible that the server was slower, but it should have recovered over time (or timed out). Maybe stopping network connections (e.g., by unplugging the network cable or turning off WiFi for a few seconds) could have forced the page loading to fail faster and allow you to close the browser faster. Let us know if the issue comes up again.</p>

---

## Post #3 by @mikebind (2026-06-25 03:11 UTC)

<p>Thanks for the response.  I will check again tomorrow and try resetting my network connections.</p>

---
