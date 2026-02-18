# Calling cli with specific python path

**Topic ID**: 32278
**Date**: 2023-10-17
**URL**: https://discourse.slicer.org/t/calling-cli-with-specific-python-path/32278

---

## Post #1 by @Gaelle_Leroux (2023-10-17 16:17 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/jcfr">@jcfr</a> !</p>
<p>We want to run a cli with specific dependencies not compatible with slicerPython, is it possible to specify the python path when we use the slicer.cli.run ?<br>
Right now it will run with python-real. Or what would be the best way to connect a subprocess run to the cli observer mechanism?</p>
<p>Thank you very much !</p>

---

## Post #2 by @lassoan (2023-10-17 16:36 UTC)

<p>Slicer will always run the Slicer CLI module script in the Slicer Python environment. However, in that Slicer CLI module script you can run any other software (e.g., another Python script, in any environment, using any interpreter, using standard <code>subprocess</code> functions). You need to pass all relevant parameters to that other process and wait for the execution to complete before your script returns.</p>

---

## Post #3 by @Gaelle_Leroux (2023-10-17 20:34 UTC)

<p>I understand, thank you <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
