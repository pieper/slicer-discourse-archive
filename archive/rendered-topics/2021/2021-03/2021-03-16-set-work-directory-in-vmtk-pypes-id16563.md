# set work directory in VMTK/Pypes?

**Topic ID**: 16563
**Date**: 2021-03-16
**URL**: https://discourse.slicer.org/t/set-work-directory-in-vmtk-pypes/16563

---

## Post #1 by @MPP (2021-03-16 04:34 UTC)

<p>Hi all,</p>
<p>Is it possible to set a work directory and switch to this directory at the start of a text file containing a list of VMTK commands?</p>
<p>I developed a vmtk for an older version of VMTK that I could still easily launch from the command line on ubuntu, but with the new version forcing me to switch I don’t see how I can tell VMTK to look for the input files in the correct directory, and to save the output files in the correct directory.</p>
<p>Or is there a way on windows to launch vmtk in a specific working directory already?</p>
<p>I don’t want to explicitly program the full directory path in each -ifile or -ofile command, because I need to execute this script in multiple directories, so I dont want to have to change each line of my script every time I execute it.</p>
<p>Thanks in advance,<br>
MPP</p>

---

## Post #2 by @lassoan (2021-03-26 03:30 UTC)

<p>On Windows, you can use %cd% as a placeholder for the current directory, for example <code>... -ifile %cd%/something.vtp ...</code>.</p>

---
