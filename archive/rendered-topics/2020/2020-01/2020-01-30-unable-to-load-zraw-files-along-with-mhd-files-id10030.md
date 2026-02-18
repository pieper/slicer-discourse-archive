# Unable to load .zraw files along with .mhd files

**Topic ID**: 10030
**Date**: 2020-01-30
**URL**: https://discourse.slicer.org/t/unable-to-load-zraw-files-along-with-mhd-files/10030

---

## Post #1 by @matt-warkentin (2020-01-30 16:22 UTC)

<p>Hi all,</p>
<p>I have been provided <code>.zraw</code> files and corresponding <code>.mhd</code> files (segmentation masks). I can load the <code>.mhd</code> masks into Slicer without issue.</p>
<p>However, I am having trouble loading a <code>.zraw</code> file into Slicer. Based on <a href="https://discourse.slicer.org/t/change-display-range-of-raw-file/6320/4">this</a> previous post, I had assumed I could load the data via <em>drag-and-drop</em> or through the <code>data</code> module, but neither seems to work. When trying either approach, nothing happens.</p>
<p>For context, I have tried <code>Slicer 4.10.1</code> and also the preview version (<code>4.11.0</code>), downloaded a few months back (not the most recent nightly build).</p>
<p>Any advice?</p>

---

## Post #2 by @muratmaga (2020-01-30 16:52 UTC)

<p>From the file name .zraw sounds like zstack in raw format. Since you can read the segmentation map already, you know the image dimensions. Use the preview version, and install the SandBox extension and try the RawImageGuess module entering the XYZ extends from your segmentation. The only unknown that will be left would be data type, but that should only take a few iterations.</p>
<p>Here is the thread on the RawImageGuess and a video tutorial.</p><aside class="quote quote-modified" data-post="1" data-topic="9219">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-extension-rawimageguess-for-loading-of-images-from-unrecognized-file-format/9219">New extension: RawImageGuess - for loading of images from unrecognized file format</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    There are proprietary image file formats the 3D Slicer does not recognize and so refuses to load. <a class="mention" href="/u/nagy.attila">@nagy.attila</a> in collaboration with Slicer core developers created an extension that can be used to load data from files that use an unknown format. 
<a href="https://github.com/acetylsalicyl/SlicerRawImageGuess">RawImageGuess extension</a> offers a number of parameters (image header size, dimensions, pixel type, etc.) that users can adjust and see the resulting image in real-time. This makes it possible to guess the image format in a couple of minutes. 
See a demo …
  </blockquote>
</aside>


---

## Post #3 by @jamesobutler (2020-01-30 17:12 UTC)

<p>If you have a MHD (header file) + zraw (compressed image data), you just need to drag and drop the MHD file into Slicer for loading. One of the header keys in the MHD would be something like <code>ElementDataFile = FileName.zraw</code>. As part of reading and loading the header information it will automatically load the specified data file. You don’t need to manually load the header and also load the zraw. It’s one action of drag-dropping the MHD.</p>

---

## Post #4 by @matt-warkentin (2020-01-30 17:22 UTC)

<p>Thanks <a class="mention" href="/u/jamesobutler">@jamesobutler</a>. So the MHD file is just the header information with a file pointer to the actual image (mask) data? Is this a correct mental model of what is going on here? So by loading the MHD file, Slicer knows where to find the actual image data in ZRAW format.</p>

---

## Post #5 by @jamesobutler (2020-01-30 19:13 UTC)

<p><a class="mention" href="/u/matt-warkentin">@matt-warkentin</a> Yes, that is correct.  As long as your MHD header file has the ElementDataFile pointing to a image data file that exists, then dragging dropping the header only file will load the full data.  If it is confusing to have the image data separate from the header, there is MHA which is the combined file (header + data).</p>

---
