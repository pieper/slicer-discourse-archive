# Modify additional DICOM tags in export

**Topic ID**: 13830
**Date**: 2020-10-02
**URL**: https://discourse.slicer.org/t/modify-additional-dicom-tags-in-export/13830

---

## Post #1 by @mikebind (2020-10-02 20:17 UTC)

<p>Hello, I use the “DICOM Export” feature from right clicking on a volume in the Data module frequently to output modified volumes in a format readable by other medical devices. It is very helpful that several fields are filled in with correct values (patient name, id, date) and that I can modify others (modality, descriptions).  However, for one use case, the device is rejecting my exported volumes because they do not specify a “WindowCenter” and “WindowWidth”.  I would like to add a value for these tags (preferably just drawn automatically from the Slicer display settings for the volume).</p>
<p>What is the easiest way to do this?</p>
<p>I see that I can use the “Create a DICOM series” module, but this requires specifying every single field I want filled in, which is unwieldy and potentially error prone (and actually I don’t see that WindowCenter and WindowWidth are options there anyway).  I also see the example in the Script Repository of exporting a DICOM volume via python script, but aside from customizing the output directory, I don’t see how to change any of the DICOM tags in that process (i.e. change the series description, window settings, etc while keeping the automatically extracted patient info).</p>

---

## Post #2 by @pieper (2020-10-02 20:53 UTC)

<p>That’s an interesting question; someone would need to change the code to expose more fields (maybe in general all the fields).</p>
<p>As a workaround you could easily write a pydicom script (it is bundled with Slicer’s python) or maybe use a shell script and a command like [dcmodify].(<a href="https://support.dcmtk.org/docs/dcmodify.html">https://support.dcmtk.org/docs/dcmodify.html</a>)</p>

---

## Post #3 by @mikebind (2020-10-03 00:47 UTC)

<p>OK, I agree, it probably won’t be too hard to write a pydicom script that does what I want.  Thanks for your help.</p>

---

## Post #4 by @lassoan (2020-10-03 02:32 UTC)

<p>It would be great if you could add the missing fields to CreateDICOMSeries module (it is a very simple CLI module) and update DICOMScalarVolumePlugin.py and DICOMExportScalarVolume.py to set these fields. This should not be harder than adding a pydicom post-processing step just for your project, and all Slicer users would benefit from it.</p>

---

## Post #5 by @mikebind (2020-10-03 02:37 UTC)

<p>OK, I’ll give this a try.  I haven’t done any CLI programming yet, only scripted modules, so this will be a good chance to try.</p>

---

## Post #6 by @lassoan (2020-10-03 02:45 UTC)

<p>If you have not built Slicer yet then and don’t want to do it just for this then we can help you with that.</p>
<p>I had a closer look at CreateDICOMSeries.cxx and it actually saves window center and width fields (although it sets is to the cover the full intensity range of the image, which is not ideal):</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/3e0e44f7620253feaa23a58df33d3abe2be1fdb9/Modules/CLI/CreateDICOMSeries/CreateDICOMSeries.cxx#L325-L333" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/3e0e44f7620253feaa23a58df33d3abe2be1fdb9/Modules/CLI/CreateDICOMSeries/CreateDICOMSeries.cxx#L325-L333" target="_blank" rel="noopener">Slicer/Slicer/blob/3e0e44f7620253feaa23a58df33d3abe2be1fdb9/Modules/CLI/CreateDICOMSeries/CreateDICOMSeries.cxx#L325-L333</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="325" style="counter-reset: li-counter 324 ;">
<li>typename Image2DType::PixelType windowCenter = (minValue + maxValue) / 2;</li>
<li>typename Image2DType::PixelType windowWidth = (maxValue - minValue);</li>
<li>
</li><li>value.str("");</li>
<li>value &lt;&lt; windowCenter;</li>
<li>itk::EncapsulateMetaData&lt;std::string&gt;(dictionary, "0028|1050", value.str() );</li>
<li>value.str("");</li>
<li>value &lt;&lt; windowWidth;</li>
<li>itk::EncapsulateMetaData&lt;std::string&gt;(dictionary, "0028|1051", value.str() );</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Could you check why that particular device may reject the image? Maybe the field is there but the data type or value is incorrect?</p>

---

## Post #7 by @mikebind (2020-10-21 21:19 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, I have returned to this problem and, despite the code you link to, the exported volumes seem to be missing the WindowCenter and WindowWidth fields.  Can you test on a sample volume and see if you get the same behavior (i.e. no “0028|1050” field in exported DICOM volume)?</p>

---

## Post #8 by @lassoan (2020-10-22 02:43 UTC)

<p>A tricky bug prevented writing of the window center&amp;width fields. I’ve fixed the bug and also improved the exporter so that the current display window center&amp;width values are used for export. The fix will be available in the Slicer Preview Release on Friday.</p>

---
