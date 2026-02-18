# Reload CLI module

**Topic ID**: 8309
**Date**: 2019-09-05
**URL**: https://discourse.slicer.org/t/reload-cli-module/8309

---

## Post #1 by @fpsiddiqui91 (2019-09-05 14:20 UTC)

<p>Hello Developers,</p>
<p>I am developing a slicer based application using CLI and scripted module. I am passing my arguments from scripted modules, doing the computations on CLI and returning back the output.</p>
<p>The problem which I am having might be very simple I guess, I just want to reload my cli module without restarting Slicer application. When I make some changes in my cpp file for cli module I need to restart the whole slicer application to see the change.</p>
<p>However, on the other hand, when I make changes on my scripted module I just have to use “Relaod” button to see the changes. Is there any functionality lie “Reload” for CLI moduels as well.</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2019-09-05 15:51 UTC)

<p>If you enable “Prefer executable CLIs” in application settings then C++ CLI modules will not be loaded into the application but the CLI executable will be used. You can then replace the CLI executable anytime and use the new version without restarting Slicer.</p>
<p>Module GUI is constructed at Slicer start, so if you change the module descriptor XML then you need to restart Slicer. You need to restart Slicer after <em>any</em> module change if you provide your module as a shared library and “Prefer executable CLIs” is disabled.</p>

---

## Post #3 by @fpsiddiqui91 (2019-09-05 16:01 UTC)

<p>Thank you for your response <a class="mention" href="/u/lassoan">@lassoan</a>. Yes, My Preferer executable option is enabled. But I was actually making changes in XML. So I guess, I need to restart the slicer after every update.</p>
<p>Thanks for the information</p>

---
