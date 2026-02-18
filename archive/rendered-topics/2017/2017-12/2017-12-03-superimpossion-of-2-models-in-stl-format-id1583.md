# Superimpossion of 2 models in STL format

**Topic ID**: 1583
**Date**: 2017-12-03
**URL**: https://discourse.slicer.org/t/superimpossion-of-2-models-in-stl-format/1583

---

## Post #1 by @poopool (2017-12-03 21:51 UTC)

<p>Hello!</p>
<p>For a research project, I am trying to superimpose (AUTOMATIC supperimposition) the STL formats of the files and then do the color mapping and measure the gaps and distance between these models.</p>
<p>What is the best way to have a consistent results? (I have one master model and 40 samples that should be superimposed on it and measure the gaps on some certain fixed points on the master model).<br>
I want to eliminate the human error during manual superimposition.</p>
<p>I really appreciate to help me out.</p>
<p>Best</p>

---

## Post #2 by @cpinter (2017-12-03 22:10 UTC)

<p>This can be a start:</p>
<ul>
<li>Create a segmentation from each STL using the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Segmentations#How_to">Segmentations module</a>
</li>
<li>Register the models using the Segment Registration extension (download and install from Extension Manager)</li>
<li>Measure distances using Segment Comparison module in SlicerRT extension</li>
</ul>

---

## Post #3 by @poopool (2017-12-03 22:29 UTC)

<p>Hi,</p>
<p>ok. Thank you. I am so new to this software and almost know nothing. I work on it. Hopefully I get it done.</p>
<p>Again, thank you for your response</p>

---
