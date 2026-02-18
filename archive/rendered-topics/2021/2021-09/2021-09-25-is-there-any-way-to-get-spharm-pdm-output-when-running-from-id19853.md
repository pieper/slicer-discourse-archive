# Is there any way to get SPHARM-PDM output when running from cmd?

**Topic ID**: 19853
**Date**: 2021-09-25
**URL**: https://discourse.slicer.org/t/is-there-any-way-to-get-spharm-pdm-output-when-running-from-cmd/19853

---

## Post #1 by @Robert_Michael_Sharp (2021-09-25 17:00 UTC)

<p>I’m having a problem where I have created a mac application that calls SPHARM-PDM and informs the user as files are created by reading the terminal output and searching for “CASE completed”, however, when trying to port to Windows this method no longer works.</p>
<p>When running SPHARM-PDM SlicerSALT from terminal using SPHARM-PDM.py on mac there is a number of lines generated such as:</p>
<p><strong>"Model" Reader has successfully read the file CASE 0 took 0 sec to run All pipelines took 0 sec to run</strong></p>
<p>However no such lines are generated when running from cmd prompt on Windows.</p>
<p>Is there any way to turn those lines on for Windows?</p>
<p>If not, what’s the best way to capture when a file has processed (so that an application that is calling SPHARM-PDM can inform the user as files are generated)?</p>
<p>Thanks for your help!</p>

---

## Post #2 by @lassoan (2021-09-25 17:01 UTC)

<p>See how to get the console output on Windows for recent Slicer Preview Releases: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/debugging/overview.html#console-output-on-windows">https://slicer.readthedocs.io/en/latest/developer_guide/debugging/overview.html#console-output-on-windows</a></p>

---
