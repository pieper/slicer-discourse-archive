---
topic_id: 7686
title: "Running Multiple Clis At Once"
date: 2019-07-19
url: https://discourse.slicer.org/t/7686
---

# Running multiple CLIs at once

**Topic ID**: 7686
**Date**: 2019-07-19
**URL**: https://discourse.slicer.org/t/running-multiple-clis-at-once/7686

---

## Post #1 by @jamesobutler (2019-07-19 15:53 UTC)

<p>I was testing running some CLIs at the same time. I was using <code>slicer.cli.run()</code> calls back to back and it is calling a python CLI. However, the second cli run call stays in “Scheduled” status state until the first run call finishes.</p>
<p>Is it possible or some setting I’m missing to make these two run at the same time?</p>
<p>CPU processing was no where near getting maxed out during this time so I’d like to take advantage of more processing power since these two calls are processing independent data.</p>

---

## Post #2 by @jamesobutler (2019-07-19 18:18 UTC)

<p>I should’ve probably specified that I’m using a Slicer nightly build which is about 10 days old.</p>
<p>The behavior is as though I’m specifying <code>wait_for_completion=True</code> argument even though I’m using the default of “False”.</p>

---

## Post #3 by @lassoan (2019-07-19 18:46 UTC)

<p>I think there is a single processing thread in vtkSlicerApplicationLogic, which maintains a task queue and executes them one by one. It would probably not too difficult to change the application logic to run multiple tasks at once. If we wanted to make things optimal then the application logic would need to analyze dependencies between CLIs (since you can auto-run CLIs that use outputs of other CLI as inputs), but this is not essential.</p>

---

## Post #4 by @jcfr (2022-12-08 03:28 UTC)

<p>To follow up, support for running multiple CLIs in parallel is proposed in <a href="https://github.com/Slicer/Slicer/pull/6723">PR-6723</a>.</p>

---
