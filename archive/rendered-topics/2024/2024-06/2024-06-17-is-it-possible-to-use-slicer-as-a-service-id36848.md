# Is it possible to use slicer as a service?

**Topic ID**: 36848
**Date**: 2024-06-17
**URL**: https://discourse.slicer.org/t/is-it-possible-to-use-slicer-as-a-service/36848

---

## Post #1 by @youngishcord (2024-06-17 19:24 UTC)

<p>There is a plan to use a slicer to extract some data from the CT scan. The rest of the program architecture is deployed in Docker.<br>
The best option would be to connect celery and assign tasks through it, but it didn’t work out for me.<br>
Is it possible to implement celery into a slicer or at least set up a server with its own API.</p>

---

## Post #2 by @lassoan (2024-06-17 19:27 UTC)

<p>Slicer has a web API - see documentation <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/webserver.html">here</a>. It exposes only a small fraction of things that Slicer can do, but any module can customize and extend the API, so it should not be a problem to make available any features you need.</p>

---

## Post #3 by @youngishcord (2024-06-18 09:39 UTC)

<p>I think that “GET /exec” is partially suitable for solving my problems. I’ll see what I can come up with.<br>
Perhaps later I’ll add the solution I came to.<br>
Thank you!</p>

---

## Post #4 by @pieper (2024-06-19 16:40 UTC)

<p>Just FYI <a class="mention" href="/u/youngishcord">@youngishcord</a> - the <code>exec</code> endpoint is great for prototyping but it may be cleaner and a bit safer to define a few specific endpoints to do the jobs you have in mind.</p>

---
