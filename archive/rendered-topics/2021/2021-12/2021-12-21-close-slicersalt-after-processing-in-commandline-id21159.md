---
topic_id: 21159
title: "Close Slicersalt After Processing In Commandline"
date: 2021-12-21
url: https://discourse.slicer.org/t/21159
---

# Close slicersalt after processing in commandline

**Topic ID**: 21159
**Date**: 2021-12-21
**URL**: https://discourse.slicer.org/t/close-slicersalt-after-processing-in-commandline/21159

---

## Post #1 by @iPsych (2021-12-21 02:47 UTC)

<p>Running slicersalt via commandline seems very useful, but seems not-loop friendly.<br>
Is it possible to stop slicersalt, after<br>
./slicersalt --no-main-window --python-script SOME COMMAND?<br>
after successful run, the cmd stops with ‘all pipeline took ~~~’.</p>
<p>Because this, it’s not loop-able for bash script. Is it possible to kill slicersalt and make commandline script loopable?</p>

---

## Post #2 by @lassoan (2021-12-22 03:52 UTC)

<p>You can add <code>exit()</code> as the last command or you can use the <code>--testing</code> command-line argument (which exits the application when all the commands are executed).</p>

---
