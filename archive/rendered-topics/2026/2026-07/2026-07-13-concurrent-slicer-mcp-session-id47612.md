---
topic_id: 47612
title: "Concurrent slicer mcp session"
date: 2026-07-13
url: https://discourse.slicer.org/t/47612
last_bumped: 2026-07-15T05:18:12.670Z
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

## Post #2 by @pieper (2026-07-14 07:51 UTC)

<p>Yes, I do that often.  I start the two servers on different ports in different instances or Slicer (look at the port it reports at startup or specify the port manually).  You can tell the Claude which port to use via the .mcp.json (restart the window in vscode) or just tell Claude to use that port and it figures out to use curl to do it.</p>

---

## Post #3 by @muratmaga (2026-07-14 16:05 UTC)

<p>Do you think it is possible to check whether there is an mcp server already running and if so, bump up to the port number programmatically for the new slicer session? Or do you always manually adjust inside the slicer?</p>

---

## Post #4 by @pieper (2026-07-15 04:38 UTC)

<p>This happens automatically already.</p>
<p>The first Slicer instance uses port 2026:</p>
<pre><code class="lang-auto">  MCP server: http://localhost:2026/mcp
  Log file:   /var/folders/yk/qm79wxyd1x38xpn3n046gykh0000gn/T/slicer-mcp-44515.log

  Configure your MCP client with:
    {"mcpServers": {"slicer": {"url": "http://localhost:2026/mcp"}}}

  To stop: mcpLogic.stop()
</code></pre>
<p>The second uses 2027:</p>
<pre><code class="lang-auto">
  MCP server: http://localhost:2027/mcp
  Log file:   /var/folders/yk/qm79wxyd1x38xpn3n046gykh0000gn/T/slicer-mcp-44711.log

  Configure your MCP client with:
    {"mcpServers": {"slicer": {"url": "http://localhost:2027/mcp"}}}

  To stop: mcpLogic.stop()
</code></pre>
<p>It should be enough to paste the second blob into Claude and tell it it should be using this port info.</p>

---

## Post #5 by @muratmaga (2026-07-15 05:18 UTC)

<p>Great I didn’t notice that it automatically incremented the ports.</p>

---
