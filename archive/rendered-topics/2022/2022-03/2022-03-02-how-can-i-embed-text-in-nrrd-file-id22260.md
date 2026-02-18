# How can I embed text in nrrd file?

**Topic ID**: 22260
**Date**: 2022-03-02
**URL**: https://discourse.slicer.org/t/how-can-i-embed-text-in-nrrd-file/22260

---

## Post #1 by @Sukhe (2022-03-02 13:04 UTC)

<p>I want to embed text in the MRI nrrd file. Is there any method?<br>
Many thanks!</p>

---

## Post #2 by @mikebind (2022-03-04 21:39 UTC)

<p>You can add custom fields to NRRD files.  <a href="https://pynrrd.readthedocs.io/en/latest/examples.html" class="inline-onebox">Examples — pynrrd 0.4.2 documentation</a></p>
<p>You could save your MRI to a .nrrd file in Slicer, and then load using pynrrd, then do something like this</p>
<pre><code class="lang-auto">import nrrd   # load pynnrd package
img_data, img_header = nrrd.read('my_saved_mri.nrrd')
# Add the text you want to save to the header
img_header["my_custom_field1"] =  "the text I want to save goes here"
my_custom_field_map = {"my_custom_field1": "str"} # python dict of custom field names and data types
nrrd.write('output_including_text.nrrd', img_data, img_header, custom_field_map=my_custom_field_map)
</code></pre>

---
