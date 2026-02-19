---
topic_id: 13480
title: "Ukf Tractography Output Issues"
date: 2020-09-14
url: https://discourse.slicer.org/t/13480
---

# UKF Tractography Output Issues 

**Topic ID**: 13480
**Date**: 2020-09-14
**URL**: https://discourse.slicer.org/t/ukf-tractography-output-issues/13480

---

## Post #1 by @cnot (2020-09-14 12:06 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10.2<br>
Expected behavior: UKF Tractography<br>
Actual behavior: Empty output file from UKF Tractography</p>
<p>Hi all,</p>
<p>I am trying to run a UKF Tractography on Windows 10, and am having problems. Namely, the program will run for somewhere between 4-20 hours, tell me ‘Status Completed’, but then output a completely empty bundle file.</p>
<p>It has worked once correctly, whereby after about 2 hours I had a complete output. The other times it never worked, despite me keeping all settings and parameters the same…</p>
<p>Here is the log file output from one of the times it did not work:</p>
<p>——————————————————————————————————</p>
<p>[DEBUG][Qt] 14.09.2020 13:12:55 [] (unknown:0) - UKF Tractography standard output:</p>
<p>Using the 2T simple model. Setting the default parameters accordingly:</p>
<p>“*”: set by user</p>
<p>“-”: default setting</p>
<ul>
<li>
<p>stoppingFA: 0.12</p>
</li>
<li>
<p>seedingThreshold: 0.18</p>
</li>
</ul>
<ul>
<li>
<p>Qm: 0.001</p>
</li>
<li>
<p>Ql: 50</p>
</li>
<li>
<p>Rs: 0.02</p>
</li>
</ul>
<ul>
<li>
<p>stepLength: 0.3</p>
</li>
<li>
<p>recordLength: 2</p>
</li>
<li>
<p>stoppingThreshold: 0.1</p>
</li>
</ul>
<ul>
<li>seedsPerVoxel: 1</li>
</ul>
<p>Found 28 cores on your system.</p>
<p>Running tractography with 28 thread(s).</p>
<p>Number of non-zero gradients: 64</p>
<p>Number of zero gradients: 1</p>
<p>Permuting the axis order to: 0 1 2 3</p>
<p>Resizing the data to: 64 220 220 144</p>
<p>Computing the baseline image</p>
<p>Dividing the signal by baseline image</p>
<p>Data normalization finished!</p>
<p>Using 2-tensor simple model.</p>
<p>Branching disabled</p>
<p>Using unconstrained filter</p>
<p>nmse_avg=0</p>
<p>[DEBUG][Qt] 14.09.2020 13:12:55 [] (unknown:0) - UKF Tractography completed without errors</p>
<p>[ERROR][VTK] 14.09.2020 13:12:55 [vtkCompositeDataPipeline (0000014846A160B0)] (D:\D\S\Slicer-4102-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:709) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(00000148AEB3D000) has 0 connections but is not optional.</p>
<p>[ERROR][VTK] 14.09.2020 13:12:55 [vtkCompositeDataPipeline (0000014846A160B0)] (D:\D\S\Slicer-4102-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:709) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(00000148AEB3D000) has 0 connections but is not optional.</p>
<p>[ERROR][VTK] 14.09.2020 13:12:55 [vtkCompositeDataPipeline (0000014846A160B0)] (D:\D\S\Slicer-4102-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:709) - Input port 0 of algorithm vtkExtractSelectedPolyDataIds(00000148AEB3D000) has 0 connections but is not optional.</p>
<p>[ERROR][VTK] 14.09.2020 13:13:33 [vtkXMLDataParser (00000148B0221620)] (D:\D\S\Slicer-4102-build\VTK\IO\XMLParser\vtkXMLDataParser.cxx:495) - Error reading beginning of compression header. Read 0 of 12 bytes.</p>
<p>[ERROR][VTK] 14.09.2020 13:13:33 [vtkXMLDataParser (00000148B0221620)] (D:\D\S\Slicer-4102-build\VTK\IO\XMLParser\vtkXMLDataParser.cxx:847) - ReadCompressionHeader failed. Aborting read.</p>
<p>[ERROR][VTK] 14.09.2020 13:13:33 [vtkXMLPolyDataReader (00000148ADD18430)] (D:\D\S\Slicer-4102-build\VTK\IO\XML\vtkXMLDataReader.cxx:415) - Cannot read point data array “FA1” from PointData in piece 0. The data array in the element may be too short.</p>
<p>———————————————————————————————————</p>
<p>Could someone tell me what is going wrong?</p>
<p>I really appreciate your help, thanks!</p>

---

## Post #2 by @pieper (2020-09-23 15:52 UTC)

<p>Not sure if anyone got back to you on this.  A couple suggestions: use the latest preview version of 4.11.  If you are still having trouble can you try reproducing this with one of the datasets in the sample data.  Let us know how it goes.</p>

---

## Post #3 by @cnot (2020-10-05 09:09 UTC)

<p>Thank you for your response! I did the update, and tried to run it on the sample data, which worked well.</p>
<p>Comparing the files from the sample and my data, I noticed the issue was coming from the brain mask I had created, which was not of data type short. This must have been the problem, as now that I have changed it things seem to be running fine.</p>
<p>Thanks for everything!</p>

---
