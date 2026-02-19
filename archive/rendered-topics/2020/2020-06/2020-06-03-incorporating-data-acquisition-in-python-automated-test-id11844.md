---
topic_id: 11844
title: "Incorporating Data Acquisition In Python Automated Test"
date: 2020-06-03
url: https://discourse.slicer.org/t/11844
---

# Incorporating data acquisition in python automated test

**Topic ID**: 11844
**Date**: 2020-06-03
**URL**: https://discourse.slicer.org/t/incorporating-data-acquisition-in-python-automated-test/11844

---

## Post #1 by @cpinter (2020-06-03 12:38 UTC)

<p>Hi all,</p>
<p>I am writing an automated workflow test that is supposed to collect some data at times. This would mean that at certain points in the test, I “let it run” until it collects a certain seconds of replayed tracked ultrasound data.</p>
<p>The problem I’m facing is that an automated test is deemed finished when its main function returns, but I need to incorporate some idle run, which cannot be done using time.sleep because then the event queue is stopped. So I’d need to wait in some way that does not release execution from the main runTest function. I have a few ideas, but each have some problems:</p>
<ul>
<li>Wait using singleShot: Call the function that runs the continuation of the test using QTimer.singleShot. For example runTest calls testWorkflow1 that runs the first part of the test, then when it needs to collect data, then calls testWorkflow2 using singleShot, which then continues the test. In this way I can implement the whole test case, but the automated test is considered done when testWorkflow1 returns after calling singleShot. So errors are not caught during the test run.</li>
<li>Implement threading: Start a new thread from runTest that executes the workflow using the above singleShot method, and then at the end sets a variable, for which a while loop waits in runTest. The problem is that the thread needs to access and manipulate lots of things in the application, so it is not safe. I don’t have lots of threading experience, however, so I’m not sure if it could be made safe in some way.</li>
</ul>
<p>Can anyone think of a solution for this?</p>
<p>Thank you!</p>

---

## Post #2 by @pieper (2020-06-03 13:00 UTC)

<p>Hi Csaba -</p>
<p>It should work to use <code>slicer.util.delayDisplay(message,msec=1000)</code> in a loop in your test.  It uses a dialog so that the singleShot happens within the calling context.</p>
<p>-Steve</p>

---

## Post #3 by @cpinter (2020-06-03 14:12 UTC)

<p>That’s right, the dialog should do the trick. What a simple solution! I’ll try this, thanks a lot!</p>
<p>Update: Works like a charm!</p>

---
