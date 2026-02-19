---
topic_id: 19646
title: "Export Segmentation To Osirix"
date: 2021-09-13
url: https://discourse.slicer.org/t/19646
---

# Export segmentation to Osirix

**Topic ID**: 19646
**Date**: 2021-09-13
**URL**: https://discourse.slicer.org/t/export-segmentation-to-osirix/19646

---

## Post #1 by @melindamareesmith (2021-09-13 13:10 UTC)

<p>Hello,<br>
I am trying to combine datasets that measure muscle size from MRI with a colleague. I have segmented muscles in 3D Slicer, my colleague has segmented muscles in Osirix.<br>
Osirix seems limited in ability to export ROIs - I have tried the import Osirix ROI in 3D Slicer, but am unable as I can only import .xml or .json files, but Osirix ROI only saves it as .roi_series. I have also tried to export my 3D Slicer segmentations to DICOM, but not successfully to import into Osirix.<br>
Has anyone experience in working between Osirix &amp; 3D Slicer?</p>

---

## Post #2 by @lassoan (2021-09-13 13:26 UTC)

<p>Do you use a very old or very new OsiriX version? Is there an OsiriX forum where you can ask about how to save your segmentation as a single ROI json or xml file (or even better, as a standard NRRD/Nifti/STL/OBJ/PLY/… file)? Maybe you need to convert to a list of 2D ROIs to a 3D ROI?</p>
<p>If you upload a sample <code>.roi_series</code> file somewhere and post the link here then I can have a look if there is a fundamental difference compared to what Slicer can import now. Maybe it is just a different file extension or other trivial difference that could be easily accommodated in the importer.</p>

---

## Post #3 by @melindamareesmith (2021-09-13 22:57 UTC)

<p>Thank you for your reply. The Osirix version is 11.0.1 (3 years old). I will investigate with Osirix support about exporting the ROIs to file formats you suggested (and post any reply/solution here too).<br>
An example .roi_series file is in link below:<br>
<a href="https://www.dropbox.com/s/x4j9wqqf0xgiwmq/PHP_01_transverse_trial%20ROIs.rois_series?dl=0" rel="noopener nofollow ugc">https://www.dropbox.com/s/x4j9wqqf0xgiwmq/PHP_01_transverse_trial%20ROIs.rois_series?dl=0</a></p>
<p>Thank you for any further information you are able to provide.</p>

---

## Post #4 by @lassoan (2021-09-14 04:58 UTC)

<aside class="quote no-group" data-username="melindamareesmith" data-post="3" data-topic="19646">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/5f8ce5/48.png" class="avatar"> melindamareesmith:</div>
<blockquote>
<p>An example .roi_series file is in link below:</p>
</blockquote>
</aside>
<p>Thank you for the sample file. This <code>.rois_series</code> file is some internal object state serialized into a binary file, so it cannot be used outside of of OsiriX.</p>

---

## Post #5 by @melindamareesmith (2021-09-14 09:01 UTC)

<p>Thank you for inspecting the file. I’ve not had reply yet from Osirix as to any solutions from that end.<br>
Are there options for exporting my 3D slicer segmentations to then be imported to Osirix? I’m not sure on this process- Osirix seem to only import ROI allowing that same ROI series file. I can enquire other options. Other import file functions include DICOM format but when I do that I haven’t been successful at importing  my 3D slicer as DICOM containing segmentations (or there is transfer issue as Segmentations don’t import to Osirix).</p>

---

## Post #6 by @lassoan (2021-09-15 03:17 UTC)

<p>I’ve found that there is an “Export ROIs” plugin available in OsiriX Lite that allows you to export the ROIs in JSON format. I’ve updated the OsiriX ROI importer module in the Sandbox extension so that it can load this JSON file.</p>
<p>Alternatively, you can also export a reconstructed surface from OsiriX Lite by choosing in menu: ROI → ROI Volume → Compute Volume…, and you can then use the icon in the lower-left corner to save in .stl format. The quality of the reconstructed surface seems pretty bad, but might be still usable. The .stl file can be loaded into Slicer as a segmentation (in “Add data” window choose “Segmentation” in the “Description” column to make the surface loaded as segmentation).</p>

---

## Post #7 by @melindamareesmith (2021-09-15 10:20 UTC)

<p>Thank-you, great I see this now in the export ROI function. I have sandbox extension install but do i need to update/reinstall it now? When I tried importing a json file I got error “import failed: string indices must be integers”.</p>
<p>I also tried the export as stl and import to 3D slicer as segmentation. This seems promising but some issues: using the “power crust” render in Osirix produces holes/gaps in the segmentations when they import to 3D slicer (which affects segment statistics), but it is anatomically placed correctly on the MRI scan. Trying “iso contour” for the Osirix render seemed to work better as it imported as a solid object, but it was not placed correctly on the MRI scan. I’m not sure whether this is something I can change in 3D slicer (the placement issue). The below figure illustrates each issue i.e. red box &amp; 3D see the “holes” in segmentation; in 3D can see same segmentation placed differently when imported.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d83e2dbd4d7b411496ab2e982c61cd15183d8653.jpeg" data-download-href="/uploads/short-url/uQYlKu5bxs68xhsJxbREvTPnBuz.jpeg?dl=1" title="Screen Shot 2021-09-15 at 8.18.24 pm.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d83e2dbd4d7b411496ab2e982c61cd15183d8653_2_392x412.jpeg" alt="Screen Shot 2021-09-15 at 8.18.24 pm.jpg" data-base62-sha1="uQYlKu5bxs68xhsJxbREvTPnBuz" width="392" height="412" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d83e2dbd4d7b411496ab2e982c61cd15183d8653_2_392x412.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d83e2dbd4d7b411496ab2e982c61cd15183d8653_2_588x618.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d83e2dbd4d7b411496ab2e982c61cd15183d8653_2_784x824.jpeg 2x" data-dominant-color="40414C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-09-15 at 8.18.24 pm.jpg</span><span class="informations">1321×1390 362 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @lassoan (2021-09-15 16:11 UTC)

<aside class="quote no-group" data-username="melindamareesmith" data-post="7" data-topic="19646">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/5f8ce5/48.png" class="avatar"> melindamareesmith:</div>
<blockquote>
<p>I have sandbox extension install but do i need to update/reinstall it now?</p>
</blockquote>
</aside>
<p>Extensions are not updated for Slicer Preview Releases, but you need to install the latest Slicer Preview Release and install the extension again.</p>
<aside class="quote no-group" data-username="melindamareesmith" data-post="7" data-topic="19646">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/5f8ce5/48.png" class="avatar"> melindamareesmith:</div>
<blockquote>
<p>tried the export as stl and import to 3D slicer as segmentation. This seems promising but some issues</p>
</blockquote>
</aside>
<p>I agree. Osirix does a very poor job in reconstructing a surface from the ROIs.</p>

---

## Post #9 by @melindamareesmith (2022-01-14 03:27 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="19646">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>you need to install the latest Slicer Preview Release and install the extension again.</p>
</blockquote>
</aside>
<p>Thank you. I have now installed the latest preview release and the sandbox extension. When I try ImportOsirixROI file I get an error to say that SlicerRT is not installed. But if I try to install that from extension manager I receive an error message “failed to retrieve metadata for application”.</p>

---

## Post #10 by @melindamareesmith (2022-01-17 05:07 UTC)

<p>To add to previous post - when I tried again today to install SlicerRT it worked file. I could now use the OsirixImportROI function, but unfortunately the result was not great - the 16 different ROIs all get imported as 1 segmentation and as attempts using other methods, although it is correctly placed on the MRI images, the segmentations have gaps/holes.</p>

---

## Post #11 by @lassoan (2022-01-17 15:47 UTC)

<p>Could you please share and example file that has issues and a screenshot of how it is rendered in OsiriX?</p>

---

## Post #12 by @melindamareesmith (2022-01-18 07:23 UTC)

<p>Yes, please find attached files and screenshot. I was not able to attach the .json file (Osirix export of ROIs)  as I received a message saying it was an unauthorised file type. I’ve tried a link to the file on dropbox:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/s/wsyuoxkw2crzn0c/ROI_64%20image%20set.json?dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon-vfl8lUR9B.ico" class="site-icon" width="" height="">

      <a href="https://www.dropbox.com/s/wsyuoxkw2crzn0c/ROI_64%20image%20set.json?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/metaserver/static/images/spectrum-icons/generated/content/content-code-large.png" class="thumbnail" width="" height="">

<h3><a href="https://www.dropbox.com/s/wsyuoxkw2crzn0c/ROI_64%20image%20set.json?dl=0" target="_blank" rel="noopener nofollow ugc">ROI_64 image set.json</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f3cb81b8f1e6ce2dcbb6da7757eedb6ee11335b.jpeg" data-download-href="/uploads/short-url/kr8mQvaEVlmFaRThVvnqdRKX4Qb.jpeg?dl=1" title="3D slicer screenshot Osirix import" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8f3cb81b8f1e6ce2dcbb6da7757eedb6ee11335b_2_690x444.jpeg" alt="3D slicer screenshot Osirix import" data-base62-sha1="kr8mQvaEVlmFaRThVvnqdRKX4Qb" width="690" height="444" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8f3cb81b8f1e6ce2dcbb6da7757eedb6ee11335b_2_690x444.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8f3cb81b8f1e6ce2dcbb6da7757eedb6ee11335b_2_1035x666.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8f3cb81b8f1e6ce2dcbb6da7757eedb6ee11335b_2_1380x888.jpeg 2x" data-dominant-color="B4ADB9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3D slicer screenshot Osirix import</span><span class="informations">1920×1236 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b82ed2767344057ab8c93d5be9887f1078d9749f.jpeg" data-download-href="/uploads/short-url/qhmazmZeE5j8YeyyrFezc8uKtWL.jpeg?dl=1" title="Osirix ROI screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b82ed2767344057ab8c93d5be9887f1078d9749f_2_442x500.jpeg" alt="Osirix ROI screenshot" data-base62-sha1="qhmazmZeE5j8YeyyrFezc8uKtWL" width="442" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b82ed2767344057ab8c93d5be9887f1078d9749f_2_442x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b82ed2767344057ab8c93d5be9887f1078d9749f_2_663x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b82ed2767344057ab8c93d5be9887f1078d9749f_2_884x1000.jpeg 2x" data-dominant-color="2B2B2B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Osirix ROI screenshot</span><span class="informations">1920×2168 205 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c300c86d0dbf0e70ab90905dec5eb604d37f6996.jpeg" data-download-href="/uploads/short-url/rP4MCauSn1po3FGDAxBu9WMxlGu.jpeg?dl=1" title="Osirix render" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c300c86d0dbf0e70ab90905dec5eb604d37f6996_2_690x335.jpeg" alt="Osirix render" data-base62-sha1="rP4MCauSn1po3FGDAxBu9WMxlGu" width="690" height="335" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c300c86d0dbf0e70ab90905dec5eb604d37f6996_2_690x335.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c300c86d0dbf0e70ab90905dec5eb604d37f6996_2_1035x502.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c300c86d0dbf0e70ab90905dec5eb604d37f6996_2_1380x670.jpeg 2x" data-dominant-color="060505"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Osirix render</span><span class="informations">1920×933 27.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #13 by @lassoan (2022-01-19 15:34 UTC)

<p>I’ve updated the “Import OsiriX ROI” module to import multiple ROIs:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/7170c1cefefd46eaa48c435ea93de2f6799e3903.png" data-download-href="/uploads/short-url/gbxxaLghglFjyxAV7j5XMvjgwpB.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7170c1cefefd46eaa48c435ea93de2f6799e3903_2_624x500.png" alt="image" data-base62-sha1="gbxxaLghglFjyxAV7j5XMvjgwpB" width="624" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7170c1cefefd46eaa48c435ea93de2f6799e3903_2_624x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7170c1cefefd46eaa48c435ea93de2f6799e3903_2_936x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7170c1cefefd46eaa48c435ea93de2f6799e3903_2_1248x1000.png 2x" data-dominant-color="BFBEC4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1505×1205 233 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can download the updated <a href="https://github.com/PerkLab/SlicerSandbox/blob/master/ImportOsirixROI/ImportOsirixROI.py">ImportOsirixROI.py</a> file manually or get it in the Slicer Preview Release tomorrow.</p>

---

## Post #14 by @melindamareesmith (2022-01-21 09:53 UTC)

<p>Thank you! I have downloaded the new Slicer preview today and installed the sandbox extension. But I couldn’t find a SlicerRT extension in the extension manager and when I use “import Osirix ROI” I get a message that it needs to be installed to generate a solid object. Here is the result. The individual segmentations per muscle have come through this time, but they are not a solid form (which means volumes aren’t computed).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f47e31da19ea253e10a4f19953371d741d53101.jpeg" data-download-href="/uploads/short-url/mJ3VZvdpHuZdtft1BwKYrQNNKmJ.jpeg?dl=1" title="Screen Shot 2022-01-21 at 7.50.23 pm" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9f47e31da19ea253e10a4f19953371d741d53101_2_690x445.jpeg" alt="Screen Shot 2022-01-21 at 7.50.23 pm" data-base62-sha1="mJ3VZvdpHuZdtft1BwKYrQNNKmJ" width="690" height="445" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9f47e31da19ea253e10a4f19953371d741d53101_2_690x445.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9f47e31da19ea253e10a4f19953371d741d53101_2_1035x667.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9f47e31da19ea253e10a4f19953371d741d53101_2_1380x890.jpeg 2x" data-dominant-color="A6A7B4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-01-21 at 7.50.23 pm</span><span class="informations">1920×1241 174 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #15 by @lassoan (2022-01-25 14:37 UTC)

<p>SlicerRT is require for creating surface from contours. For the Slicer Preview Release there is a few-hour time period each day when you can already download the Slicer installer but building of extensions is still in progress and they arrive on the extensions server one by one (see more details <a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html#extension-is-not-found-for-current-slicer-version">here</a>). If you go to the Extensions Manager now then you should be able to download SlicerRT for the release that you installed a few days ago.</p>

---

## Post #16 by @melindamareesmith (2022-01-27 01:04 UTC)

<p>Perfect- yes I have gone back in and that is all working now. Thank you for the help!</p>

---

## Post #17 by @John_Muschelli (2025-12-17 22:08 UTC)

<p>We have a working solution for taking <code>rois_series</code> files and the associated DICOM series and exporting the ROIs to either DICOM or a table of points to create a polygon outside of OsiriX.  Please drop me a line if anyone would use this (e.g. license or service).</p>
<p>For example, the first ROI in the dropbox file from above has points of:</p>
<pre><code class="lang-auto">{213.30005433638254, 212.07240137719543}, {222.35368516523997, 206.16816553735168}, {230.74033143599192, 200.48469385766418}, {237.3608720548884, 192.5489676918927}, {237.84936883528391, 181.94529947900207}, {245.70289495070139, 183.73958811425598}, {250.45869329054514, 185.70766672753723}, {252.79079558928171, 190.63020929955871}, {251.10219361860911, 197.46916422509582}, {249.62261226256052, 202.49739489221008}, {242.73433759291331, 210.0103820290509}, {237.90103700239817, 219.70516428613098}, {231.65156533796946, 227.05375370644958}, {223.14514710982004, 222.98138126992615}, {219.09156205732981, 220.15608439111145}
</code></pre>
<p>is called INTEROSSEI and starts on slide 78.  This can be extracted straight from the <code>rois_series</code> file.</p>

---
