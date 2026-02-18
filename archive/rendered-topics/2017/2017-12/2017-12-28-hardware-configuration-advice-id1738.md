# Hardware Configuration advice

**Topic ID**: 1738
**Date**: 2017-12-28
**URL**: https://discourse.slicer.org/t/hardware-configuration-advice/1738

---

## Post #1 by @gsfoco (2017-12-28 20:05 UTC)

<p>Operating system: Windows 10 pro<br>
Slicer version: 4.8<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Would you be able to help recommend a configuration?<br>
I will be doping volume regeneration from 3 dicom images, each ~0.8GB large. I have a lot of them to process, so I am looking at what will provide me with the best performance for the momeny (between RAM, processor, graphic card).</p>
<p>Thank you.</p>

---

## Post #2 by @dzenanz (2017-12-28 20:42 UTC)

<p>Depending on what you processing will entail, memory requirements will differ. What you could do, is load the largest images you intend to work with into Slicer and examine SlicerApp-real.exe’s Memory(private working set). Then start your processing, and observe what is the peak of memory usage. For best results, you will want to have about twice the peak (so OS and other apps can live too). If you can’t bother yourself with the measurement, get 8GB.</p>
<p>Graphics card does not participate in processing, only in visualization. Get a decent dedicated one only if you intend to do volume rendering and/or polygonal surface visualization.</p>
<p>For general speed nowdays, solid state drive is quite important, at least for the OS and applications (C:).</p>
<p>Any remaining money you will want to spend on processor with more cores. AMD Ryzen seems to offer best price/value ratio right now.</p>

---
