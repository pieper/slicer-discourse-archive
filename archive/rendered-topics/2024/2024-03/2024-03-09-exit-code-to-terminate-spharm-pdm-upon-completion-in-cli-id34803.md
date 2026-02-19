---
topic_id: 34803
title: "Exit Code To Terminate Spharm Pdm Upon Completion In Cli"
date: 2024-03-09
url: https://discourse.slicer.org/t/34803
---

# Exit code to terminate SPHARM-PDM upon completion in CLI?

**Topic ID**: 34803
**Date**: 2024-03-09
**URL**: https://discourse.slicer.org/t/exit-code-to-terminate-spharm-pdm-upon-completion-in-cli/34803

---

## Post #1 by @kmadi (2024-03-09 17:20 UTC)

<p>Hello! I’ve spoken to a couple of the developers in person but I figured I’d ask here for a wider reach.</p>
<p>I’m currently using a python script to execute the SPHARM-PDM module in a command line interface (CLI) via python’s <code>subprocess.run()</code> function. However, my script never fully completes as the SPHARM process never actually exits upon completion (I have to terminate the script via <code>ctrl + c</code> to actually end it). I know I can manually exit my python script using a timeout function, but there’s no way of knowing that all of my meshes (&gt;100) were generated successfully.</p>
<p>I notice that when I run SPHARM via CLI through a bash shell by itself, the process doesn’t have an exit code to automatically end it after the output is printed, and I have to click enter or <code>ctrl + c</code> to get to the next input line/command prompt. I’m guessing this is causing my python script to never complete, as it’s still waiting for the exit code from SPHARM.</p>
<p>Is there a workaround for this, or is this something that can be implemented in a future version of SALT?</p>
<p>Thanks in advance and I appreciate any input!<br>
-KVM</p>

---
