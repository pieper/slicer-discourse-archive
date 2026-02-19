---
topic_id: 32825
title: "Print Output Does Not Immediately Appear In Python Console"
date: 2023-11-14
url: https://discourse.slicer.org/t/32825
---

# Print output does not immediately appear in Python console

**Topic ID**: 32825
**Date**: 2023-11-14
**URL**: https://discourse.slicer.org/t/print-output-does-not-immediately-appear-in-python-console/32825

---

## Post #1 by @MLDawn (2023-11-14 21:23 UTC)

<p>May I ask a basic question. In my python script I keep printing messages using Python’s print() commant. However, these messasges will not appear instantly! For example, if the user pushes a button in my Python plugin, a long script is executed and in the mittle I have inserted print commands. However, none of them appear, until the entire function of the button is executed! Is there an easy way to fix this? Thanks.</p>

---

## Post #2 by @lassoan (2023-11-15 05:14 UTC)

<p>You need to give a chance for the application to paint the messages into the console. The easiest way to do it is to call <code>slicer.app.processEvents()</code> after the <code>print</code> command.</p>

---

## Post #3 by @MLDawn (2023-11-15 10:47 UTC)

<p>Thanks a lot! It worked like a charm!!!</p>

---
