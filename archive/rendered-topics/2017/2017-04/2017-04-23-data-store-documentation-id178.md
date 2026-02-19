---
topic_id: 178
title: "Data Store Documentation"
date: 2017-04-23
url: https://discourse.slicer.org/t/178
---

# Data Store documentation

**Topic ID**: 178
**Date**: 2017-04-23
**URL**: https://discourse.slicer.org/t/data-store-documentation/178

---

## Post #1 by @Lorensen (2017-04-23 15:21 UTC)

<p>I have been trying to upload an mrb to the DataStore using the Slice module, I notice that uploaded data set does not have an index,json file that somehow describes the .png file that holds my scene view. Also, the metadata is missing the slicerdatastore metadata. If I add that metadata manually through the midas interface, my dataset shows up in the slicer datastore datasets.</p>
<p>Where is the upload process documented that describes the index.json file and how to get the meta data properly documented?</p>

---

## Post #2 by @jcfr (2017-04-24 12:41 UTC)

<p>Hi Bill,</p>
<p>Thanks for the note.</p>
<aside class="quote no-group" data-username="Lorensen" data-post="1" data-topic="178">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lorensen/48/31_2.png" class="avatar"> Lorensen:</div>
<blockquote>
<p>Where is the upload process documented that describes the index.json file and how to get the meta data properly documented?</p>
</blockquote>
</aside>
<p>Current documentation is available here:</p>
<ul>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DataStore" class="inline-onebox">Documentation/Nightly/Modules/DataStore - Slicer Wiki</a></li>
<li><a href="https://www.slicer.org/wiki/Documentation/4.6/Modules/DataStore" class="inline-onebox">Documentation/4.6/Modules/DataStore - Slicer Wiki</a></li>
</ul>
<p>Could you could add a note on the wiki pages ?</p>

---

## Post #3 by @Lorensen (2017-04-24 20:27 UTC)

<p><span class="mention">@jc</span> ,can you upload an mrb to the datastore and see if it appears in the Slicer DataStore. I have a feeling that the mechanism is broken. When I upload (using the Slicer Datastore module), the meta data is nor properly populated. I have tried this with my own mrb’s and mrb’s I have downloaded from the DataStore.</p>
<p>Bill</p>

---

## Post #4 by @Lorensen (2017-04-26 14:47 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a> Is the datastore broken? Can you upload a dataset and see if it shows up in the Slicer DataStore listing?</p>

---

## Post #5 by @jcfr (2017-04-26 14:59 UTC)

<p>Hi Bill,</p>
<p>I didn’t have a chance to look into this yet. I will let you know as soon as I have an update.</p>
<p>Thanks for your patience,<br>
Jc</p>

---

## Post #6 by @jcfr (2017-05-02 19:49 UTC)

<aside class="quote no-group" data-username="Lorensen" data-post="1" data-topic="178">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lorensen/48/31_2.png" class="avatar"> Lorensen:</div>
<blockquote>
<p>Where is the upload process documented that describes the index.json file and how to get the meta data properly documented?</p>
</blockquote>
</aside>
<p>I would recommend to look at:</p>
<ul>
<li>the following Midas plugin: <a href="https://github.com/midasplatform/slicerdatastore" class="inline-onebox">GitHub - midasplatform/slicerdatastore: Midas Server module for uploading and downloading data from 3D Slicer</a></li>
<li><a href="https://github.com/Slicer/Slicer-DataStore" class="inline-onebox">GitHub - Slicer/Slicer-DataStore: Slicer module to Download, Upload and Browse MRB datasets stored in a Midas database</a></li>
</ul>

---

## Post #7 by @Lorensen (2017-05-02 20:03 UTC)

<p>Sorry I can’t help. My php skills are 0.</p>

---

## Post #8 by @jcfr (2017-05-02 20:14 UTC)

<p>Having an other look, the following module is responsible for the extraction of metadata associated with a MRB file is this one:</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">
      <a href="https://github.com/midasplatform/mrbextractor/tree/9a9e26f9a7d47ca5e7ab1a14908a1be851374307" target="_blank">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars3.githubusercontent.com/u/1188892?s=400&amp;v=4" class="thumbnail onebox-avatar" width="378" height="378">

<h3><a href="https://github.com/midasplatform/mrbextractor/tree/9a9e26f9a7d47ca5e7ab1a14908a1be851374307" target="_blank">midasplatform/mrbextractor</a></h3>

<p>Midas Server module to extract MRB metadata. Contribute to midasplatform/mrbextractor development by creating an account on GitHub.</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Note that revision <code>9a9e26f9</code> is used on the slicer server.</p>
<p>More specifically, the script in charge of extract the metadata is this one: <a href="https://github.com/midasplatform/mrbextractor/blob/9a9e26f9a7d47ca5e7ab1a14908a1be851374307/controllers/components/scripts/mrb-extract-views.py">https://github.com/midasplatform/mrbextractor/blob/9a9e26f9a7d47ca5e7ab1a14908a1be851374307/controllers/components/scripts/mrb-extract-views.py</a></p>
<p>Generation of <code>index.json</code> happens here:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/midasplatform/mrbextractor/blob/9a9e26f9a7d47ca5e7ab1a14908a1be851374307/controllers/components/scripts/mrb-extract-views.py#L77" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/midasplatform/mrbextractor/blob/9a9e26f9a7d47ca5e7ab1a14908a1be851374307/controllers/components/scripts/mrb-extract-views.py#L77" target="_blank">midasplatform/mrbextractor/blob/9a9e26f9a7d47ca5e7ab1a14908a1be851374307/controllers/components/scripts/mrb-extract-views.py#L77</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="67" style="counter-reset: li-counter 66 ;">
<li>for viewInfo in sceneViewInfo:
</li>
<li>    for z in zipfileSrc.namelist():
</li>
<li>        mrmlFilename = viewInfo['mrmlFilename']
</li>
<li>        if z.endswith(mrmlFilename):
</li>
<li>            newFilename = mrmlFilename.replace('/', '_').replace(' ', '_')
</li>
<li>            viewInfo['filename'] = newFilename
</li>
<li>            
</li>
<li>toc = json.dumps(sceneViewInfo, sort_keys=True,indent=4, separators=(',', ': '))
</li>
<li>
</li>
<li>try:
</li>
<li class="selected">  f = open(outputFolder+"/index.json", "w")
</li>
<li>  try:
</li>
<li>    f.write(toc)
</li>
<li>  finally:
</li>
<li>    f.close()
</li>
<li>except IOError:
</li>
<li>    pass
</li>
<li>  
</li>
<li>zipinfos = zipfileSrc.infolist()
</li>
<li>for zipinfo in zipinfos:
</li>
<li>    for viewInfo in sceneViewInfo:
</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
