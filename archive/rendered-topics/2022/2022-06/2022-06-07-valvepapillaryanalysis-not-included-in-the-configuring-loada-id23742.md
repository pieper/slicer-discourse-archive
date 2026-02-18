# ValvePapillaryAnalysis not included in the Configuring Loadable module:

**Topic ID**: 23742
**Date**: 2022-06-07
**URL**: https://discourse.slicer.org/t/valvepapillaryanalysis-not-included-in-the-configuring-loadable-module/23742

---

## Post #1 by @whu (2022-06-07 03:10 UTC)

<p>Hello, the newly ValvePapillaryAnalysis in the directory as the TCAVValveSimulator and the others. But<br>
ValvePapillaryAnalysis  in not in the Configuring Loadable module:</p>
<p>– Configuring Scripted module: ValveView<br>
7&gt;-- Configuring Scripted module: Philips4dUsDicomPatcher<br>
7&gt;-- Configuring Loadable module: KretzFileReader [qSlicerKretzFileReaderModuleExport.h]<br>
7&gt;-- Configuring Loadable module: GeUsMovieReader [qSlicerGeUsMovieReaderModuleExport.h]<br>
7&gt;-- Configuring Scripted module: CardiacDeviceSimulator<br>
7&gt;-- Configuring Scripted module: AsdVsdDeviceSimulator<br>
7&gt;-- Configuring Scripted module: TCAVValveSimulator<br>
7&gt;-- Configuring Scripted module: ValveAnnulusAnalysis<br>
7&gt;-- Configuring Scripted module: ValveClipDeviceSimulator<br>
7&gt;-- Configuring Scripted module: ValveQuantification<br>
7&gt;-- Configuring Scripted module: TomTecUcdPlugin<br>
7&gt;-- Configuring Scripted module: CartoExport<br>
7&gt;-- Configuring Scripted module: BafflePlanner<br>
7&gt;-- Configuring Scripted module: UltrasoundImage3dReader<br>
7&gt;-- Configuring Scripted module: Reconstruct4DCineMRI</p>
<p>exactly without ValvePapillaryAnalysis .</p>
<p>need some help…</p>

---

## Post #2 by @mau_igna_06 (2022-06-07 08:55 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> may know about this</p>

---

## Post #3 by @whu (2022-06-08 03:21 UTC)

<p>Thanks.<br>
This have been solved by adding add_subdirectory(ValvePapillaryAnalysis) in the CMakeLists manually.</p>

---

## Post #4 by @lassoan (2022-06-09 15:54 UTC)

<p>Thanks for the information. I’ve <a href="https://github.com/SlicerHeart/SlicerHeart/commit/743fcc43d4377b093fbf19ca7d7b1d8565127693">fixed</a> the CMakeLists.txt file now.</p>

---
