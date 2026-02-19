---
topic_id: 17906
title: "Connect 3D Slicer With Python Pynetdicom Library"
date: 2021-06-01
url: https://discourse.slicer.org/t/17906
---

# Connect 3D Slicer with python PYNETDICOM library

**Topic ID**: 17906
**Date**: 2021-06-01
**URL**: https://discourse.slicer.org/t/connect-3d-slicer-with-python-pynetdicom-library/17906

---

## Post #1 by @klm-1992 (2021-06-01 15:15 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>We are trying to connect to 3D slicer with a python script using PYNETDICOM library. We’re able to establish communication but we’re getting an error of connection timeout.</p>
<p>Please find code below:-<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/564353010045c7d3e04bd8537028f0c3dc2c45a7.png" data-download-href="/uploads/short-url/cj7iQrjL19O9tFSH37dHbGmSBmf.png?dl=1" title="ss4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/564353010045c7d3e04bd8537028f0c3dc2c45a7_2_690x463.png" alt="ss4" data-base62-sha1="cj7iQrjL19O9tFSH37dHbGmSBmf" width="690" height="463" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/564353010045c7d3e04bd8537028f0c3dc2c45a7_2_690x463.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/564353010045c7d3e04bd8537028f0c3dc2c45a7_2_1035x694.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/564353010045c7d3e04bd8537028f0c3dc2c45a7.png 2x" data-dominant-color="2E2F2E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ss4</span><span class="informations">1272×855 92.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Please find the output in order below (connection error)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/4887efdfdfcb82a852350ef9a728335b86b9f252.png" data-download-href="/uploads/short-url/alDCxk9XfCFIqcPqZlhFIK2QBz4.png?dl=1" title="ss1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4887efdfdfcb82a852350ef9a728335b86b9f252_2_579x499.png" alt="ss1" data-base62-sha1="alDCxk9XfCFIqcPqZlhFIK2QBz4" width="579" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4887efdfdfcb82a852350ef9a728335b86b9f252_2_579x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4887efdfdfcb82a852350ef9a728335b86b9f252_2_868x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/4887efdfdfcb82a852350ef9a728335b86b9f252.png 2x" data-dominant-color="332D2D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ss1</span><span class="informations">936×807 77.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/3331bb536a6e1bb59d9fea309e8509a1ff34926d.png" data-download-href="/uploads/short-url/7iSTQvOcEFrGye2cItyUek6LjOt.png?dl=1" title="ss2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3331bb536a6e1bb59d9fea309e8509a1ff34926d_2_568x500.png" alt="ss2" data-base62-sha1="7iSTQvOcEFrGye2cItyUek6LjOt" width="568" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3331bb536a6e1bb59d9fea309e8509a1ff34926d_2_568x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3331bb536a6e1bb59d9fea309e8509a1ff34926d_2_852x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/3331bb536a6e1bb59d9fea309e8509a1ff34926d.png 2x" data-dominant-color="342E2E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ss2</span><span class="informations">919×808 79.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7741809d04bca28c48381f15f6937d21b98be00.png" data-download-href="/uploads/short-url/zj4Ff9SVraRujqElYAJgKNe12UM.png?dl=1" title="ss3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f7741809d04bca28c48381f15f6937d21b98be00_2_518x500.png" alt="ss3" data-base62-sha1="zj4Ff9SVraRujqElYAJgKNe12UM" width="518" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f7741809d04bca28c48381f15f6937d21b98be00_2_518x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f7741809d04bca28c48381f15f6937d21b98be00_2_777x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7741809d04bca28c48381f15f6937d21b98be00.png 2x" data-dominant-color="342E2E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ss3</span><span class="informations">853×822 71 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Please let us know if you have any idea. Any help will be appreciated. Thanks!</p>

---

## Post #2 by @lassoan (2021-06-01 16:15 UTC)

<p>You can already do DICOM networking with existing Slicer modules and extensions.</p>
<p>Classic DIMSE networking:</p>
<ul>
<li>C-STORE SCP: see DICOM module / DICOM networking / Storage listener</li>
<li>C-STORE SCU: right-click on a patient/study/series and choose Send to DICOM server</li>
<li>QUERY/RETRIEVE: see DICOM module / DICOM networking / Query and retrieve</li>
</ul>
<p>DICOMweb networking:</p>
<ul>
<li>query and retrieve using DICOMwebBrowser module</li>
<li>DICOMweb upload using DICOM module: right-click on a patient/study/series and choose Send to DICOM server</li>
</ul>
<p>While there is certainly room for usability and performance improvements, all these features generally work well in Slicer. All these features are available from both the GUI and using Python scripting.</p>
<p>If you don’t want to use this infrastructure but prefer PYNETDICOM then you can do that, too. Since Python is essentially single-threaded, you may achieve better user experience if you run all the network jobs in a separate Python processes. You can debug these communication processes completely independently from Slicer and get network troubleshooting help from PYNETDICOM community.</p>

---
