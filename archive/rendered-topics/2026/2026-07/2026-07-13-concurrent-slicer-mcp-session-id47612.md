---
topic_id: 47612
title: "Concurrent slicer mcp session"
date: 2026-07-13
url: https://discourse.slicer.org/t/47612
last_bumped: 2026-07-13T23:49:36.075Z
---

# Concurrent slicer mcp session

**Topic ID**: 47612
**Date**: 2026-07-13
**URL**: https://discourse.slicer.org/t/concurrent-slicer-mcp-session/47612

---

## Post #1 by @muratmaga (2026-07-13 23:49 UTC)

<p>Sometimes I run two agents simultaneously for different tasks. these tasks are often executed in different Slicer sessions also running concurrently (e.g., stable vs a preview version, or different code branches being tested simultaneously).</p>
<p>The issue is my slicerrc.py calls the <a href="https://github.com/pieper/slicer-skill/blob/main/slicer-mcp-server.py" class="inline-onebox" rel="noopener nofollow ugc">slicer-skill/slicer-mcp-server.py at main · pieper/slicer-skill · GitHub</a> to auto start the mcp session. If I start two slicer sessions concurrently these mcp servers collide.</p>
<p>Did anyone have a robust solution on how to handle concurrency?</p>

---
