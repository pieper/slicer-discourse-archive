# DataStore: data not showing for uploaded dataset

**Topic ID**: 175
**Date**: 2017-04-22
**URL**: https://discourse.slicer.org/t/datastore-data-not-showing-for-uploaded-dataset/175

---

## Post #1 by @Lorensen (2017-04-22 17:26 UTC)

<p>I uploaded an .mrb file to the Slicer datastore rep at: <a href="http://slicer.kitware.com/midas3/community/23" rel="nofollow noopener">http://slicer.kitware.com/midas3/community/23</a><br>
And here is the info for the dataset: <a href="http://slicer.kitware.com/midas3/item/285338" rel="nofollow noopener">http://slicer.kitware.com/midas3/item/285338</a></p>
<p>The data is called Swiss Skull Stripper Atlas. It does not show up in the DataStore module in Slicer.</p>
<p>Bill</p>

---

## Post #2 by @lassoan (2017-04-22 19:54 UTC)

<p>Have you uploaded through the DataStore module? For data sets that show up in the DataStore module (for example <a href="http://slicer.kitware.com/midas3/item/121588">http://slicer.kitware.com/midas3/item/121588</a>), “slicerdatastore” attribute is set to “true”. This attribute is missing for your data set.</p>

---

## Post #3 by @Lorensen (2017-04-22 20:26 UTC)

<p>Yes, I  uploaded through the slicer module.</p>

---

## Post #4 by @Lorensen (2017-04-22 21:52 UTC)

<p>I just uploaded a test data set and it does not have the slicerdatastore attribute…</p>

---

## Post #5 by @lassoan (2017-04-22 22:04 UTC)

<p>The Swiss skull stripper data set has the slicerdatastore attribute now: <a href="http://slicer.kitware.com/midas3/item/285338">http://slicer.kitware.com/midas3/item/285338</a></p>
<p>But it still does not show up in the Data store:<br>
<a href="http://slicer.kitware.com/midas3/slicerdatastore" class="onebox" target="_blank">http://slicer.kitware.com/midas3/slicerdatastore</a></p>
<p>You can have a look at the MRB parser and Slicer data store source code to see what could go wrong:<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">
      <a href="https://github.com/midasplatform/mrbextractor" target="_blank">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars3.githubusercontent.com/u/1188892?s=400&amp;v=4" class="thumbnail onebox-avatar" width="378" height="378">

<h3><a href="https://github.com/midasplatform/mrbextractor" target="_blank">midasplatform/mrbextractor</a></h3>

<p>Midas Server module to extract MRB metadata. Contribute to midasplatform/mrbextractor development by creating an account on GitHub.</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">
      <a href="https://github.com/midasplatform/slicerdatastore" target="_blank">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars3.githubusercontent.com/u/1188892?s=400&amp;v=4" class="thumbnail onebox-avatar" width="378" height="378">

<h3><a href="https://github.com/midasplatform/slicerdatastore" target="_blank">midasplatform/slicerdatastore</a></h3>

<p>Midas Server module for uploading and downloading data from 3D Slicer - midasplatform/slicerdatastore</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>For example, the mrbextractor depends on scheduler, so maybe the uploaded files are not parsed immediately but according to some schedule. Maybe we just have to wait some more.</p>

---

## Post #6 by @lassoan (2017-04-22 22:12 UTC)

<p>In the meantime, the Swiss skull stripper data has appeared in the data store (listed and can be downloaded), but unfortunately there is some error in viewing its properties:<br>
<a href="http://slicer.kitware.com/midas3/slicerdatastore/view?itemId=285338&amp;layout=layout" class="onebox" target="_blank">http://slicer.kitware.com/midas3/slicerdatastore/view?itemId=285338&amp;layout=layout</a></p>
<p>There is still a chance that we have to just wait a bit more.</p>
<p>If you uploaded the data set so that the Swiss Skull Stripper extension can automatically download it, then probably it’s better to upload them on Midas as simple files (not as scenes) and download them as the SampleData module does it. Or, even simpler, you can just include the volume files in the extension package (4MB data is really small; there are much larger extension packages).</p>

---

## Post #7 by @Lorensen (2017-04-22 23:17 UTC)

<p>I manually added the proper meta data.</p>
<p>BTW the meta data contributor is misspelled. It is spelled mrbextrator. Probaby should have been mrbextractor. I realize that can’t be fixed. Also, even though the value is true, the type is text, not boolean. It took me a few times to get it right.</p>
<p>Can you try to upload an mrb and see if the slicerdatastoRE atribute is set?</p>

---

## Post #8 by @brhoom (2018-09-07 10:49 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="175">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>but unfortunately there is some error in viewing</p>
</blockquote>
</aside>
<p>I have the same problem.</p>
<pre><code>An error occurred
The system has encountered the following error:
Unable to find metadata.
In /projects/src/Midas3/modules/slicerdatastore/controllers/ViewController.php, line: 54 At 06:53:07 2018-09-07
</code></pre>

---
