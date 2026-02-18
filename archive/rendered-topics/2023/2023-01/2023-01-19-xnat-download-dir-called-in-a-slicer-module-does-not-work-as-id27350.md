# XNAT download_dir called in a slicer module does not work as expected on fetching some of images, while exactly the same code works fine when run outside slicer

**Topic ID**: 27350
**Date**: 2023-01-19
**URL**: https://discourse.slicer.org/t/xnat-download-dir-called-in-a-slicer-module-does-not-work-as-expected-on-fetching-some-of-images-while-exactly-the-same-code-works-fine-when-run-outside-slicer/27350

---

## Post #1 by @S_Arbabi (2023-01-19 12:55 UTC)

<p>Hello,</p>
<p>In one module I’d developed functionality to connect to RIA database through XNAT api and download specific images to local. Unfortunately I learned that for some unknown reason to me it drops on download_dir. I tried a lot to find the issue and after a lot investigations I know that the same exact code that I’m running in slicer works perfectly if I run it outside slicer.<br>
the code is as simple as:</p>
<pre><code class="lang-auto">import xnat
username=#username
password=#password
ria = xnat.connect('http://ria.ds.umcutrecht.nl/', user=username, password=password)
...
try:
   scan.resources["DICOM"].download_dir(temp_download_dir+"\\")
except:
   print("could not download!")
</code></pre>
<p>basically the error is something that I never get running the code outside slicer, something like this:</p>
<pre><code class="lang-auto">    scan.resources["DICOM"].download_dir(
  File "C:\Users\saeed\AppData\Local\NA-MIC\Slicer 5.0.2\lib\Python\Lib\site-packages\xnat\mixin.py", line 591, in download_dir
    zip_file.extractall(target_dir)
  File "C:\Users\saeed\AppData\Local\NA-MIC\Slicer 5.0.2\lib\Python\Lib\zipfile.py", line 1633, in extractall
    self._extract_member(zipinfo, path, pwd)
  File "C:\Users\saeed\AppData\Local\NA-MIC\Slicer 5.0.2\lib\Python\Lib\zipfile.py", line 1687, in _extract_member
    open(targetpath, "wb") as target:
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\saeed\\Desktop\\tmp2\\00-ria\\02-026\\02-026_212596038910566_662398200_20210301\\302\\DICOM\\temp\\02-026_212596038910566_662398200_20210301\\scans\\302-MPR_SAG_3D_PD_SPAIR\\resources\\DICOM\\files\\1.3.46.670589.50.2.15757877403410526784.31298281802920234632-302-43-687f92.dcm'
</code></pre>
<p>I was wondering is there any thoughts why this is happening?</p>
<p>Best,<br>
Saeed</p>

---
