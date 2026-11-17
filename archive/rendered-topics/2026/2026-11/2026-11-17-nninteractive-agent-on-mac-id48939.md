---
topic_id: 48939
title: "Nninteractive_agent on mac"
date: 2026-11-17
url: https://discourse.slicer.org/t/48939
last_bumped: 2026-11-17T03:59:50.620Z
---

# Nninteractive_agent on mac

**Topic ID**: 48939
**Date**: 2026-11-17
**URL**: https://discourse.slicer.org/t/nninteractive-agent-on-mac/48939

---

## Post #1 by @Jean_Pinson (2026-11-17 03:59 UTC)

<p>Hi everyone, and thanks <a class="mention" href="/u/lassoan">@lassoan</a>  for the new <strong>nnInteractive_agent</strong> integration in Slicer, it’s a great addition.</p>
<p>I’m trying it on macOS (Slicer 5.12.4) with nnInteractive running remotely: an <code>nninteractive-server</code> v2.6 on a Windows PC (RTX 5080), exposed through an ngrok tunnel, started with <code>--api-key</code>.</p>
<p>In the Server panel I use “Internal server” with “nnInteractive runs on: nnInteractive server” and the tunnel URL. The connection fails with <code>401 Unauthorized</code> on <code>/claim</code>, so the server is reachable but the key is not sent.</p>
<p>I couldn’t find a field for the nnInteractive server API key in the panel. The “API key file” field seems to be for the LLM only. From the nninteractive-agent README, I understand the client reads <code>NN_INTERACTIVE_API_KEY</code> from the environment, but Slicer launched from the Dock doesn’t inherit my shell variables.</p>
<p>Questions:</p>
<ol>
<li>Is there a way to provide the nnInteractive server key from the GUI that I missed? I’m using nninteractive from my mac a lot and it works well.</li>
<li>Would a key field next to the server URL be possible in a future version? It would help anyone using a shared GPU server.</li>
</ol>
<p>Happy to share logs or test anything. Thanks!</p>

---
