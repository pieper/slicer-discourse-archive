# Incorrect DICOM import

**Topic ID**: 23029
**Date**: 2022-04-19
**URL**: https://discourse.slicer.org/t/incorrect-dicom-import/23029

---

## Post #1 by @Boris33 (2022-04-19 18:10 UTC)

<p>Hello,</p>
<p>I’m just getting started with 3D Slicer (4.11) and I have problems loading correctly my DICOM volume. The data is acquired from a Siemens CT scanner as IMA files and stacked with a pattern 1.1, 1.2, … 1.200 (1 sequence with 200 z positions).</p>
<p>Importing the folder where my DICOM files are stored does not work as each slice is imported separately and not as a volume.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/67e5f7e51e0c9de47871b20e2e605f887446b6c5.png" data-download-href="/uploads/short-url/eP7SPrPzKBFsL2mwLl2NjKCa7JP.png?dl=1" title="Skärmbild 2022-04-19 102311" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67e5f7e51e0c9de47871b20e2e605f887446b6c5_2_345x211.png" alt="Skärmbild 2022-04-19 102311" data-base62-sha1="eP7SPrPzKBFsL2mwLl2NjKCa7JP" width="345" height="211" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67e5f7e51e0c9de47871b20e2e605f887446b6c5_2_345x211.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67e5f7e51e0c9de47871b20e2e605f887446b6c5_2_517x316.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67e5f7e51e0c9de47871b20e2e605f887446b6c5_2_690x422.png 2x" data-dominant-color="F2F2F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Skärmbild 2022-04-19 102311</span><span class="informations">760×467 45 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I noticed moreover in Show DICOM database&gt;View DICOM metadata that my files are reordered by Slicer as 1.1, 1.10, 1.100, 1.101 …</p>
<p>I already tried the following corrections as proposed in other topics without success so far:</p>
<ul>
<li>DICOM patcher</li>
<li>Changing the DICOM reader approach in Edit&gt;Application Settings</li>
<li>Importing as standard data</li>
</ul>
<p>I usually have no problem to import the data in ImageJ, MatLab or Python</p>
<p>Thanks in advance for the help,</p>
<p>B</p>

---
