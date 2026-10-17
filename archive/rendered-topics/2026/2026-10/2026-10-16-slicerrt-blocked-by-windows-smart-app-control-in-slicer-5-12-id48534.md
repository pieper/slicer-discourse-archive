---
topic_id: 48534
title: "SlicerRT blocked by Windows Smart App Control in Slicer 5.12.4"
date: 2026-10-16
url: https://discourse.slicer.org/t/48534
last_bumped: 2026-10-16T20:20:59.000Z
---

# SlicerRT blocked by Windows Smart App Control in Slicer 5.12.4

**Topic ID**: 48534
**Date**: 2026-10-16
**URL**: https://discourse.slicer.org/t/slicerrt-blocked-by-windows-smart-app-control-in-slicer-5-12-4/48534

---

## Post #1 by @hipresearch_jp (2026-10-16 13:56 UTC)

<p>Hello SlicerRT team,</p>
<p>I’m setting up SlicerRT to generate DRRs for orthopedic CT research. On a fresh installation of Slicer 5.12.4 (revision 34645), with SlicerRT installed through the Extensions Manager, Windows Smart App Control blocks vtkSlicerIsodoseModuleLogicPython.pyd because its publisher could not be verified.</p>
<p>The logs also report application-control blocks for qSlicerBeamsModule.dll and qSlicerPlmProtonDoseEngineModule.dll, followed by Python import failures.</p>
<p>The files plastimatch_slicer_drr.exe and plastimatch_slicer_drrLib.dll are present, but both show an Authenticode status of NotSigned. I have not executed them, so I have not confirmed whether DRR generation works.</p>
<p>Is this a known issue? Is a signed SlicerRT build compatible with this Slicer version available, or is there a supported solution that keeps Smart App Control enabled?</p>
<p>Thank you.</p>
<p>This post was written with AI assistance.</p>

---

## Post #2 by @Rei_Kurosawa (2026-10-16 17:00 UTC)

<p>Two things I could verify from official sources. Microsoft’s Smart App Control FAQ states there is no way to bypass it for individual apps - the only options are turning Smart App Control off entirely or the developer signing the app with a valid signature. On the signing side, the unsigned state is a known, still-open issue for 3D Slicer itself (Slicer GitHub issue 4724, “Unsigned Slicer application is hard to install and runs slower”), and your NotSigned findings for the SlicerRT binaries match that pattern; I could not find any separately signed SlicerRT build. So to your questions: no signed build seems to be available, and there is no supported way to keep Smart App Control fully enabled while running those binaries. Whether disabling it is acceptable is a security call only you or your IT can make.</p>

---

## Post #3 by @jamesobutler (2026-10-16 18:56 UTC)

<p>The above summary is correct. Slicer 5.12 stable is signed because the core code is trusted per the Slicer core developers. However Slicer extensions fall in the category of open source community provided that have no guarantee of trust by the core Slicer team even though some may be getting conveniently built by the Slicer factory build machine and made available in the extensions manager. All the extensions aren’t however developed by Slicer core developers.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> Would you agree that extensions accepted into the Slicer extensions manager are not trusted in a way that the Slicer org would otherwise sign the binaries of extensions?</p>

---

## Post #4 by @pieper (2026-10-16 20:13 UTC)

<blockquote>
<p>Would you agree that extensions accepted into the Slicer extensions manager are not trusted in a way that the Slicer org would otherwise sign the binaries of extensions?</p>
</blockquote>
<p>That is correct, we wouldn’t be able to check extension code carefully so it’s appropriate that systems that insist on signed code should alert users and make the perform explicit changes if they want to run the code.</p>
<p>We don’t know of any reason to distrust extensions, and we do run some superficial scans to avoid malware.  But one suggestion would be to run virtual machines, so that any unsigned code is in a sandbox with limited access to any confidential data or security keys.</p>
<p>By signing the core application releases, the core developer team is helping you know you have the real binaries that we believe are safe to use, but of course as open source free software we make no assurances, so everyone should assess the risks in their personal circumstances.</p>

---

## Post #5 by @hipresearch_jp (2026-10-16 20:20 UTC)

<p>Thank you all for your prompt and helpful replies.</p>
<p>I now understand the distinction between signing the Slicer core and<br>
signing community extensions. Thank you also for suggesting an<br>
isolated virtual machine as an option.</p>
<p>For now, I will keep Smart App Control enabled on my main PC and<br>
consider how best to proceed with my research setup.</p>
<p>I appreciate your time and support.</p>

---
