# Title: Slow and unstable performance

**Topic ID**: 4988
**Date**: 2018-12-06
**URL**: https://discourse.slicer.org/t/title-slow-and-unstable-performance/4988

---

## Post #1 by @Lucas_Formighieri (2018-12-06 14:58 UTC)

<p>Operating system: Win10-Pro (Portuguese), Intel 5820k, 32gig ram, nvidia 970gtx, nvme ssd.<br>
Slicer version: 4.10 and nightly builds<br>
Expected behavior: fluid workflow<br>
Actual behavior: interruptions and delays in the workflow</p>
<p>Hello,</p>
<p>I am a radiologist working with angiotomography exams (up to 2k slices each). I have experience with dicom programs such as Carestream Vue, Vitrea, GE-ADW, Osirix and Radiant. My focus now is segmentation and 3D printing.</p>
<p>During tasks such as loading exams and segmentation there are such sings as the “not responding” on the title bars on the “whitening” of the program´s window. Loading exams my take up to one minute. Sometimes the program “hangs” during a task and then just quits. Watching the resources usage CPU and GPU are always below 20%. Memory may reach peaks of 50 or 60% but usually hovers around 30%.</p>
<p>Even in systems more powerful than my own (Xeon 5118 Gold, 32 gig ram, nvdia Quadro) it is slow and unstable, although a little bit less so.</p>
<p>Is there anything I can do to improve this?</p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2018-12-06 15:22 UTC)

<p>Typically on a regular desktop computer (few ten GB of RAM, few-year-old i7 CPU) can handle typical images - size of up to 512^3, 16 bits per pixel. If you have a 2000^3 image (about 60x larger) then you’ll need 60x more memory space (about 150GB, preferably physical RAM) and 60x faster CPU to get similar experience as with typical images.</p>
<p>DICOM image review workstations that load and display only a few slices of the image at a time, so for them it does not matter how large the entire image is. 3D workstations either refuse to load extremely large images or downscale them when loaded and may load full-resolution representations for smaller regions when needed.</p>
<p>In Slicer, you can crop&amp;downscale the images using “Crop volume” module. Increase “Spacing scale” parameter or decrease the cropping region size until every component of the cropped volume dimensions (shown in Volume information section) gets below 512. After that, click “Apply” to generate the image and delete the original image from the scene. With this new image, all Slicer functions should work reliably. Before you start, configure at least 150GB virtual memory in your Windows system settings to make sure you don’t run out of memory.</p>

---

## Post #3 by @kayarre (2020-06-12 00:44 UTC)

<p>What could be done to handle large out of memory images. I know there is development with things like  neuroglancer, but what would have to change to handle large out of memory tiled image volumes. Essentially being able to test on a small volume but then generate an offline pipeline for the larger image and subsequently view the results in a tiled or crumbled manner?</p>

---

## Post #4 by @lassoan (2020-06-12 01:19 UTC)

<p>Multiresolution techniques are reworked/redeveloped in VTK every couple of years but since very few people actually uses them and difficult to keep these up-to-date with all the changes that are going on in VTK, they always fall behind and become unstable or just remain too limited (see <a href="https://blog.kitware.com/nsf-awards-kitware-phase-i-sbir-for-volume-rendering-of-amr-datasets/">1</a>, <a href="https://blog.kitware.com/multi-resolution-streaming-in-vtk-and-paraview/">2</a>, <a href="https://blog.kitware.com/msvtk-the-multiscale-visualisation-toolkit/">3</a>). Probably it is just too hard to implement and maintain a general solution at the level of VTK.</p>
<p>However, there are dedicated efforts where out-of-core data management is not just a distraction but a main goal. It could be interesting to investigate if these could be leveraged in Slicer. See for example how ITK and Dask is used to process a 188GB image.</p>
<p>Another potential approach could be to focus on specific problems, instead of trying to build and integrate large generic frameworks. These could be much easier to implement and maintain.</p>
<p>Can you tell more about what exactly you would like to achieve? Would you like to just visualize or also process data? What kind of data? Is it already available in multi-resolution/tiled format?</p>

---
