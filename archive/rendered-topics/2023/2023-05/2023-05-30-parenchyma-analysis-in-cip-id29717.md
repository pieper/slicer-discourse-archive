---
topic_id: 29717
title: "Parenchyma Analysis In Cip"
date: 2023-05-30
url: https://discourse.slicer.org/t/29717
---

# Parenchyma Analysis in CIP

**Topic ID**: 29717
**Date**: 2023-05-30
**URL**: https://discourse.slicer.org/t/parenchyma-analysis-in-cip/29717

---

## Post #1 by @csnily (2023-05-30 02:18 UTC)

<p>Please help me to see how I can batch import dicom files from the dicom database in the python console of 3d slicer, and use CIP_ParenchymaAnalysis under the CIP_ParenchymaAnalysis library for processing and analysis, and export data. I need to process and export in batches, because I have hundreds of Patient’s dicom files</p>

---

## Post #2 by @csnily (2023-05-30 02:48 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e746e53f95935f34116b30c9508c716af9a57c1e.jpeg" data-download-href="/uploads/short-url/wZYbGV6TpT20LraqhkFPgNT4b9k.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e746e53f95935f34116b30c9508c716af9a57c1e_2_690x368.jpeg" alt="image" data-base62-sha1="wZYbGV6TpT20LraqhkFPgNT4b9k" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e746e53f95935f34116b30c9508c716af9a57c1e_2_690x368.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e746e53f95935f34116b30c9508c716af9a57c1e_2_1035x552.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e746e53f95935f34116b30c9508c716af9a57c1e_2_1380x736.jpeg 2x" data-dominant-color="BBB9C4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2600×1388 592 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I want to load my CT files(.dcm)，a large number to deal with,and using Parenchyma Analysis and finally to export this table</p>

---

## Post #3 by @csnily (2023-05-30 02:49 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/efbd1436979b2c28396ec4249de5973fb4f800d2.jpeg" data-download-href="/uploads/short-url/ycPdlmTL9pQB4STx8hP0NVl3EfU.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/efbd1436979b2c28396ec4249de5973fb4f800d2_2_690x340.jpeg" alt="image" data-base62-sha1="ycPdlmTL9pQB4STx8hP0NVl3EfU" width="690" height="340" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/efbd1436979b2c28396ec4249de5973fb4f800d2_2_690x340.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/efbd1436979b2c28396ec4249de5973fb4f800d2_2_1035x510.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/efbd1436979b2c28396ec4249de5973fb4f800d2_2_1380x680.jpeg 2x" data-dominant-color="DDE0E5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2404×1186 377 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
this is the table I want .I want to use python console to deal with a large number of CT files and use Parenchyma Analysis in Python console and export this table</p>

---

## Post #4 by @rbumm (2023-05-30 13:38 UTC)

<p>You should probably start looking at the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">Script Repository</a> and learn some Python. Alternatively, you could hire a programmer or consult ChatGPT for program snippets.</p>
<p>All your requests can be realized relatively simply.</p>

---

## Post #5 by @jamesobutler (2023-05-30 18:01 UTC)

<p>This type of batch workflow stuff would probably be a job for <a href="https://github.com/KitwareMedical/SlicerPipelines" rel="noopener nofollow ugc">SlicerPipelines</a>.</p>
<p><a class="mention" href="/u/rbumm">@rbumm</a> Do you know if Parenchyma Analysis works with SlicerPipelines or could easily be made to work with it?</p>

---

## Post #6 by @rbumm (2023-05-30 20:18 UTC)

<p>I have not worked with SlicerPiplines before, just tested it a bit but do not see how I could integrate DICOM import or Parenchyma analsis in this extension … do you ?</p>

---

## Post #7 by @rbumm (2023-05-30 20:21 UTC)

<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#load-dicom-files-into-the-scene-from-a-folder">Load DICOM files from a folder</a></p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-volume-of-each-segment">Call a module (here Segmentstatistcs)</a></p>

---

## Post #9 by @csnily (2023-05-31 01:19 UTC)

<p>Thanks a lot.I will try this tutorial.</p>

---

## Post #10 by @csnily (2023-05-31 01:21 UTC)

<p>I don’t konw it.But I think maybe I can look throught the source code and try to run it in my scene.Thanks a lot.</p>

---
