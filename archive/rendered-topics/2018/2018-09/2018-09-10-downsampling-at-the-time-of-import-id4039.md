# Downsampling at the time of import

**Topic ID**: 4039
**Date**: 2018-09-10
**URL**: https://discourse.slicer.org/t/downsampling-at-the-time-of-import/4039

---

## Post #1 by @muratmaga (2018-09-10 05:18 UTC)

<p>I am working on a high-resolution dataset, which is 16GB in size (2000x2000x2000, short data type). It is a tiff sequence. I need to write a set of instructions for people to process such large data in Slicer.</p>
<p>While I have enough memory on my laptop to load the full-resolution image, and then downsample it using the ResampleScalarVolume module, I thought it might be a good option to downsample at time of import. But I don’t think that’s possible through the load data UI. Is the recommended solution to use unu utility for this?</p>
<p>Thanks for the input.</p>

---

## Post #2 by @pieper (2018-09-10 12:59 UTC)

<p>unu is a very handy utility.  There are other scripting options too, such as just reading the tif files a slice at a time with vtk and forming a volume from downsampled slices.  Probably this should be a custom importer module, at least at first.  That would allow you to examine the input and provide options about how you want to downsample it, and maybe crop.</p>
<p>If there’s a common use case then a similar feature could be added to the core load data UI.</p>
<p>Also, <a class="mention" href="/u/blowekamp">@blowekamp</a> had a neat solution for operating on high-res ROIs within downsampled volumes for working with large electron microscopy volumes.  You could have a look at the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/IASEM">ion abrasion scanning EM</a> extension and see if it’s possible to build on or generalize that.</p>

---

## Post #3 by @blowekamp (2018-09-10 13:19 UTC)

<p><span class="mention">@Steve</span> Thanks for the mention of the module.</p>
<p>I believe the IASEM-&gt;<strong>Import Image</strong> module will do what you want. There is actually nothing specific in this plugin for microscopy data. The import module works with any file format which ITK support for streaming, including RGB images. For TIFF files I believe that ITK will read in a whole slice at a time. I have used it on the Visible Human Data set, when it was a MHA file.</p>
<p>With this module you can specify an ROI, and/or specify shrinking or binning factors to reduce the resolution.</p>

---

## Post #4 by @muratmaga (2018-09-10 18:23 UTC)

<p>Thanks Steve. So my Slicer 4.8.1 or any of the recent nightlies, no longer has unu.exe. Did you guys stop distributing with Slicer?</p>

---

## Post #5 by @muratmaga (2018-09-10 18:23 UTC)

<p><a class="mention" href="/u/blowekamp">@blowekamp</a>. I will give it a try…</p>

---

## Post #6 by @muratmaga (2018-09-10 18:58 UTC)

<p>I installed the extension (for stable 4.8.1), when I navigate to Input File, the listed compatible file extensions are mha, hdf5, vtk and mrc. I don’t see any other formats for image sequences…</p>

---

## Post #7 by @blowekamp (2018-09-10 19:14 UTC)

<p>I looks like that limitation is coming from the CLI xml here:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/blowekamp/Slicer-IASEM/blob/master/IASEMImport/IASEMImport.xml.in#L38" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/blowekamp/Slicer-IASEM/blob/master/IASEMImport/IASEMImport.xml.in#L38" target="_blank" rel="nofollow noopener">blowekamp/Slicer-IASEM/blob/master/IASEMImport/IASEMImport.xml.in#L38</a></h4>
<pre class="onebox"><code class="lang-in"><ol class="start lines" start="28" style="counter-reset: li-counter 27 ;">
<li>  &lt;name&gt;imageROI&lt;/name&gt;</li>
<li>  &lt;label&gt;Image ROI&lt;/label&gt;</li>
<li>  &lt;channel&gt;input&lt;/channel&gt;</li>
<li>  &lt;longflag&gt;imageROI&lt;/longflag&gt;</li>
<li>  &lt;description&gt;&lt;![CDATA[Label image which defines a ROI of interest to import from the volume.]]&gt;&lt;/description&gt;</li>
<li>  &lt;default/&gt;</li>
<li>&lt;/region&gt;</li>
<li>&lt;label&gt;IO&lt;/label&gt;</li>
<li>&lt;description&gt;&lt;![CDATA[Input/output parameters]]&gt;&lt;/description&gt;</li>
<li>
</li>
<li class="selected">&lt;file fileExtensions=".hdf5,.mrc,.mha.,.vtk"&gt;</li>
<li>  &lt;name&gt;input&lt;/name&gt;</li>
<li>  &lt;longflag&gt;--input&lt;/longflag&gt;</li>
<li>  &lt;label&gt;Input File&lt;/label&gt;</li>
<li>  &lt;description&gt;&lt;![CDATA[Input file containing a large 3D volume in a streamable format.]]&gt;&lt;/description&gt;</li>
<li>&lt;/file&gt;</li>
<li>&lt;image&gt;</li>
<li>  &lt;name&gt;outputVolume&lt;/name&gt;</li>
<li>  &lt;label&gt;IASEM Volume&lt;/label&gt;</li>
<li>  &lt;channel&gt;output&lt;/channel&gt;</li>
<li>  &lt;index&gt;1&lt;/index&gt;</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>The ITK support for streaming IOs has improved since I wrote that module. I believe that it could be updated to support at least TIFF files, others may work now too. It has been a while since I have had a working Slicer development environment so I can’t quickly experiment to see if the change would work.</p>
<p>Alternatively, could you convert the file to MHA?</p>

---

## Post #8 by @muratmaga (2018-09-10 19:50 UTC)

<p>We are just getting setup for Slicer development, we might try to tackle this along the way. Thanks.<br>
M</p>

---

## Post #9 by @pieper (2018-09-10 20:39 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="4039" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Thanks Steve. So my Slicer 4.8.1 or any of the recent nightlies, no longer has unu.exe. Did you guys stop distributing with Slicer?</p>
</blockquote>
</aside>
<p>Probably better to do some python scripting instead of using unu - although it’s a handy utility it can be a bit “cryptic” at times and there’s more long-term utility in learning more python scripting.</p>

---
