# New Python package for Slicer interoperability

**Topic ID**: 17850
**Date**: 2021-05-29
**URL**: https://discourse.slicer.org/t/new-python-package-for-slicer-interoperability/17850

---

## Post #1 by @lassoan (2021-05-29 05:21 UTC)

<p>We often find that Slicer-generated data sets needs to be accessed or created outside of Slicer’s Python environment. While we try to use standard file formats, there are often small customizations and additional metadata that requires a little effort to manage. To make this a bit easier for users, I’ve created <a href="https://github.com/lassoan/slicerio">slicerio</a>, a standalone Python package for reading/writing Slicer data files:</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://pypi.org/static/images/favicon.6a76275d.ico" class="site-icon" width="15" height="15">

      <a href="https://pypi.org/project/slicerio/" target="_blank" rel="noopener">PyPI</a>
  </header>

  <article class="onebox-body">
    <img src="https://pypi.org/static/images/twitter.90915068.jpg" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://pypi.org/project/slicerio/" target="_blank" rel="noopener">slicerio</a></h3>

  <p>Utilities for 3D Slicer</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>For now, I have only added .seg.nrrd file reading and basic writing. For example, segment metadata can be accessed like this (in any Python environment, after <code>pip install slicerio</code>):</p>
<pre><code class="lang-auto">&gt;&gt;&gt; import slicerio
&gt;&gt;&gt; segmentation_info = slicerio.read_segmentation_info("Segmentation.seg.nrrd")
&gt;&gt;&gt; segment_names
['ribs', 'cervical vertebral column', 'thoracic vertebral column', 'lumbar vertebral column', 'right lung', 'left lung', 'tissue']
&gt;&gt;&gt; segment = slicerio.segment_from_name(segmentation_info, segment_names[3])
&gt;&gt;&gt; segment["labelValue"]
4
&gt;&gt;&gt; segment["color"]
[0.831373, 0.737255, 0.4]
</code></pre>
<p>In the future we could add utilities for managing markups files (convert json to/from csv and numpy arrays), tables (read/write schema.csv files), etc.</p>
<p>Any comments and suggestions are welcome. If you have Python code snippets that could be useful in this context then feel free to send pull requests.</p>

---

## Post #2 by @Francesca_Lo_Iacono (2022-11-22 09:35 UTC)

<p>Hi! I am developing an automatic segmentation algorithm in python but the obtained segmentation do not overlap in Slicer with the original images, how can I use this package to make it happens?</p>
<p>thank you</p>

---

## Post #3 by @pieper (2022-11-22 18:24 UTC)

<p>Probably this is an RAS-LPS issue or other <a href="https://www.slicer.org/wiki/Coordinate_systems">coordinate system</a> issue.  Post data or screenshots if you need further advise.</p>

---

## Post #4 by @lassoan (2022-11-22 20:48 UTC)

<p>Have you set the origin, spacing, axis directions for the segmentation that you created?</p>

---
