# Slicer crash when launch mutiviews

**Topic ID**: 32940
**Date**: 2023-11-22
**URL**: https://discourse.slicer.org/t/slicer-crash-when-launch-mutiviews/32940

---

## Post #1 by @Young_Wang (2023-11-22 00:13 UTC)

<hr>
<h2><a name="p-103574-translated-report-full-report-below-1" class="anchor" href="#p-103574-translated-report-full-report-below-1" aria-label="Heading link"></a>Translated Report (Full Report Below)</h2>
<p>Process:               Slicer [6267]<br>
Path:                  /Applications/Slicer.app/Contents/MacOS/Slicer<br>
Identifier:            org.slicer.slicer<br>
Version:                (5.3.0-2023-08-02)<br>
Code Type:             X86-64 (Translated)<br>
Parent Process:        launchd [1]<br>
User ID:               501</p>
<p>Date/Time:             2023-11-21 20:08:22.4262 -0400<br>
OS Version:            macOS 14.1.1 (23B81)<br>
Report Version:        12<br>
Anonymous UUID:        B624F4FD-D95A-5096-DE94-F54B8E365129</p>
<p>Sleep/Wake UUID:       1C467CA6-412C-4BA1-9900-54C19B68FEB4</p>
<p>Time Awake Since Boot: 9400 seconds<br>
Time Since Wake:       298 seconds</p>
<p>System Integrity Protection: enabled</p>
<p>Notes:<br>
PC register does not match crashing frame (0x0 vs 0x14071145F)</p>
<p>Crashed Thread:        35</p>
<p>Exception Type:        EXC_BAD_ACCESS (SIGSEGV)<br>
Exception Codes:       KERN_INVALID_ADDRESS at 0x0000000000000000<br>
Exception Codes:       0x0000000000000001, 0x0000000000000000</p>
<p>Termination Reason:    Namespace SIGNAL, Code 11 Segmentation fault: 11<br>
Terminating Process:   exc handler [6267]</p>
<p>VM Region Info: 0 is not in any region.  Bytes before following region: 4333887488<br>
REGION TYPE                    START - END         [ VSIZE] PRT/MAX SHRMOD  REGION DETAIL<br>
UNUSED SPACE AT START<br>
—&gt;<br>
__TEXT                      10251e000-102562000    [  272K] r-x/r-x SM=COW  …/MacOS/Slicer</p>
<p>Error Formulating Crash Report:<br>
PC register does not match crashing frame (0x0 vs 0x14071145F)</p>

---

## Post #2 by @pieper (2023-11-22 00:36 UTC)

<p>Hi - can you clarify what steps lead to this crash?</p>

---

## Post #3 by @Young_Wang (2023-11-22 00:46 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> thank you for the quick reply. I added a scene file. The system just crashed after I switched from one window view to 3x3.</p>

---

## Post #4 by @pieper (2023-11-22 02:00 UTC)

<p>Thanks for the extra info, but I think we need more specific info to investigate.  Can you say how to recreate the issue on another machine using either public data or data you provide?</p>

---

## Post #5 by @lassoan (2023-11-22 03:50 UTC)

<p>Most likely the issue has been already fixed in a more recent Slicer version. If you can still reproduce the issue in the latest Slicer Preview Release then give us step-by-step instructions (share the scene file that can reproduce the issue if loading a scene file seems necessary; describe exactly what layouts you are switching between, etc.).</p>

---

## Post #6 by @Young_Wang (2023-11-22 17:41 UTC)

<p>Thank you <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a>, I upgraded to the latest version and the problem persists. I haven’t tried to load the same dataset on different computer. I will give this a try. I can attach the error log if that helps.</p>

---

## Post #7 by @lassoan (2023-11-22 17:47 UTC)

<p>Thanks for testing. What we would need now is a screen capture video or step-by-step instructions (literally every click you make) for reproducing the crash.</p>

---

## Post #8 by @Young_Wang (2023-12-02 03:55 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I tried to reinstall slicer and the error went away.</p>

---
