# Loading DICOM volume got significantly slower

**Topic ID**: 9605
**Date**: 2019-12-24
**URL**: https://discourse.slicer.org/t/loading-dicom-volume-got-significantly-slower/9605

---

## Post #1 by @chir.set (2019-12-24 10:39 UTC)

<p>Here are the logs when loading the same DICOM volume with the ‘Add data’ menu on Linux :</p>
<p>On 2019-11-11 (don’t know the revision tag) :</p>
<pre><code> There is more than one file, use the vtkITKArchetypeImageSeriesReader instead
Loaded volume from file: /home/user/tmp/mscans/fsg_2019-10-23/images/pat00000/st000000/se000000/ct000027. Dimensions: 512x512x2167. Number of components: 1. Pixel type: int.
"Volume" Reader has successfully read the file "/home/user/tmp/mscans/fsg_2019-10-23/images/pat00000/st000000/se000000/ct000027" "[89.89s]"
</code></pre>
<p>Today 2019-12-24 (6e48df6) :</p>
<pre><code>There is more than one file, use the vtkITKArchetypeImageSeriesReader instead
Loaded volume from file: /home/user/tmp/mscans/fsg_2019-10-23/images/pat00000/st000000/se000000/ct000027. Dimensions: 512x512x2167. Number of components: 1. Pixel type: int.
"Volume" Reader has successfully read the file "/home/user/tmp/mscans/fsg_2019-10-23/images/pat00000/st000000/se000000/ct000027" "[389.11s]"
</code></pre>
<p>That’s 5 minutes more, and 4.4 times slower.</p>
<p>Loaded the same volume with the DICOM module : time parameter is not logged, I would say about 5 minutes.</p>
<pre><code>Switch to module:  "DICOM"
QXcbConnection: XCB error: 3 (BadWindow), sequence: 8822, resource id: 42099390, major code: 40 (TranslateCoords), minor code: 0
"DICOM indexer has successfully inserted 2167 files [2.38s]"
"DICOM indexer has successfully processed 2167 files [6.13s]"
"DICOM indexer has updated display fields for 2167 files [0.66s]"
Imported a DICOM directory, checking for extensions
Loading with imageIOName: GDCM
Window/level found in DICOM tags (center=40.0, width=400.0) has been applied to volume 2: Aorte Membre Inf
</code></pre>
<p>Can it be improved ?</p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2019-12-24 14:01 UTC)

<p>I don’t see any difference between DICOM loading speed between Slicer-2019-11-03 and Slicer-2019-12-19 versions on Windows when using Add data module (a CT consisting of 2600 files, 340MB in total in 22-23sec). I don’t see any code change in this time period that could affect DICOM loading speed.</p>
<ul>
<li>Have you repeated the measurements several times? First loading of a file after may be much slower than loading the file again.</li>
<li>What kind of series you are reading? What device generated it (manufacturer, model, year)? What is the total size of the series?</li>
<li>Did you build Slicer with the same optimization options?</li>
<li>Could you try the official build Slicer builds (you can download them by specifying “offset” value for the download page, for example <a href="https://download.slicer.org/?offset=-30">https://download.slicer.org/?offset=-30</a>).</li>
<li>Can you try more Slicer versions to find the exact version number between 2019-11-11 and 2019-12-24 to check where exactly you start to see the difference?</li>
</ul>

---

## Post #3 by @chir.set (2019-12-24 18:09 UTC)

<p>After a few tests, I think the problem is related to fuse on that particular machine.</p>
<p>I tried a 512x512x1935 volume on another machine, my laptop. I usually copy the image of CT angioscan DVDs as an ISO file, then mount these with fuseiso. The load time is ‘normal’ on my laptop :</p>
<p>ISO mounted with fuseiso : 68 secs (evaluated twice)<br>
ISO mounted as root : 9 seconds<br>
DICOM files copied in a directory on disk from the ISO : 8 seconds</p>
<p>During the loading, fuseiso consumes about 70% of 1 CPU core, while on my work PC where loading got slow, fuseiso consumes about 95% of 1 CPU core.</p>
<p>Using 6e48df6 here.</p>
<p>I’ll perform further tests on the problematic PC ASAP.</p>
<p>Thanks.</p>

---
