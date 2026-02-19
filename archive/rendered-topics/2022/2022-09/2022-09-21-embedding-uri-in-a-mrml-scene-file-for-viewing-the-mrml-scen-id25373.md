---
topic_id: 25373
title: "Embedding Uri In A Mrml Scene File For Viewing The Mrml Scen"
date: 2022-09-21
url: https://discourse.slicer.org/t/25373
---

# Embedding URI in a mrml scene file, for viewing the mrml scene on a remote slicer application

**Topic ID**: 25373
**Date**: 2022-09-21
**URL**: https://discourse.slicer.org/t/embedding-uri-in-a-mrml-scene-file-for-viewing-the-mrml-scene-on-a-remote-slicer-application/25373

---

## Post #1 by @Rajesh_Ds (2022-09-21 10:39 UTC)

<p>This is a sample .mrml scene file.  It is having a local filepath embedded in it which points to the niftii file corresponding to a particular segmentation result shown in the mrml scene.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a26701f33bda43d93f99ae02712ad5e48dbd97ab.png" data-download-href="/uploads/short-url/naG2FlSFOKeXaW4JIhIa1NapoCv.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a26701f33bda43d93f99ae02712ad5e48dbd97ab.png" alt="image" data-base62-sha1="naG2FlSFOKeXaW4JIhIa1NapoCv" width="690" height="316" data-dominant-color="D6D6D6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1233×566 54 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is it possible to replace the path with a URI (universal resource identifier) of the “segmentation result niftii file” and sent this mrml scene file  to a remote system, so that this same .mrml scene can be viewed on a “remote system slicer application” ?  Will the slicer application of the remote system be able to download the niftii file mentioned in the URI ?</p>

---

## Post #2 by @Rajesh_Ds (2022-09-21 10:42 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/3436a1071e8b25228b95e9303b8bbbd8544adfa4.png" data-download-href="/uploads/short-url/7rTRYxtXNlbJfzvVwFivWXUdqew.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/3436a1071e8b25228b95e9303b8bbbd8544adfa4_2_690x316.png" alt="image" data-base62-sha1="7rTRYxtXNlbJfzvVwFivWXUdqew" width="690" height="316" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/3436a1071e8b25228b95e9303b8bbbd8544adfa4_2_690x316.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/3436a1071e8b25228b95e9303b8bbbd8544adfa4_2_1035x474.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/3436a1071e8b25228b95e9303b8bbbd8544adfa4.png 2x" data-dominant-color="D3D4D6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1233×566 68.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Like this</p>

---

## Post #3 by @pieper (2022-09-21 14:29 UTC)

<p>As <a class="mention" href="/u/lassoan">@lassoan</a> mentioned we used to have a feature like this in mrml, but it turned out to be messy and difficult to deal with security tokens/logins and similar issues in a generic way.  If you really need something like this I’d suggest writing a python script that accepts a mrml file as input, detects URIs <code>fileName</code> fields, and downloads them to the local filesystem and replaces the URI with a local path so the user can load from there.</p>

---

## Post #4 by @lassoan (2022-09-21 14:56 UTC)

<p>You can also use custom URLs to open a .nrrd file from a link directly Slicer using custom URL (<code>slicer://</code>). Slicer core has built-in handler for DICOMweb URIs, but you can add handlers for additional data types by adding a very short scripted module that recognizes the URL content and processes it. I provided an example for loading a .nrrd file and some description <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository/gui.html#launch-slicer-directly-from-a-web-browser">here</a>.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> What do you think about adding this module to Slicer core (changing it to allow open .mrb files and a few other common file formats; or allow it to open all supported file formats)?</p>

---

## Post #5 by @pieper (2022-09-21 15:49 UTC)

<p>If it helps solve a problem or facilitate a common use case then yes, it makes sense to have a module like that in the core.</p>
<p><a class="mention" href="/u/rajesh_ds">@Rajesh_Ds</a> for your scenario is it just the segmentation that you would like to download via URI or all the contents of the MRML scene (e.g. the background MR or CT).</p>

---

## Post #6 by @Rajesh_Ds (2022-09-22 14:13 UTC)

<aside class="quote no-group" data-username="pieper" data-post="5" data-topic="25373">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>all the contents of the MRML scene (e.g. the background MR or CT).</p>
</blockquote>
</aside>
<p>Yes Steve, I would like to all contents, not just segmentation.</p>

---

## Post #7 by @pieper (2022-09-22 14:20 UTC)

<p>A practical way for many projects is to share .mrb files via dropbox or a similar service.  There have been some problems reported when people save directly to a virtual drive, so best practice is to save to a local disk and then copy the files up to the cloud drive.</p>

---

## Post #8 by @Rajesh_Ds (2022-10-02 16:58 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="25373">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>slicer://</p>
</blockquote>
</aside>
<p>Is it possible to download a niftii file from an  URI as follows ?</p>
<p>import requests<br>
URL = “<a href="https://drive.google.com/file/d/1jnkq9TORuCRCvwWFXhUhxsgLs7bOIZeu/view?usp=sharing" rel="noopener nofollow ugc">https://drive.google.com/file/d/1jnkq9TORuCRCvwWFXhUhxsgLs7bOIZeu/view?usp=sharing</a>”<br>
response = requests.get(URL)<br>
open(“abc.nii.gz”, “wb”).write(response.content)</p>

---

## Post #9 by @muratmaga (2022-10-02 23:25 UTC)

<p>See the source of ImportFromURL module in SlicerMorph. You need to have the correct storageNode to store the downloaded data (assuming your goal is not just to download but open it in Slicer).</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph/blob/master/ImportFromURL/ImportFromURL.py#L165-L200">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/ImportFromURL/ImportFromURL.py#L165-L200" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/ImportFromURL/ImportFromURL.py#L165-L200" target="_blank" rel="noopener nofollow ugc">SlicerMorph/SlicerMorph/blob/master/ImportFromURL/ImportFromURL.py#L165-L200</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="165" style="counter-reset: li-counter 164 ;">
          <li>class ImportFromURLLogic(ScriptedLoadableModuleLogic):</li>
          <li>  """This class should implement all the actual</li>
          <li>    computation done by your module.  The interface</li>
          <li>    should be such that other python code can import</li>
          <li>    this class and make use of the functionality without</li>
          <li>    requiring an instance of the Widget.</li>
          <li>    Uses ScriptedLoadableModuleLogic base class, available at:</li>
          <li>    https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py</li>
          <li>    """</li>
          <li>  def runImport(self, url, fileNames, nodeNames):</li>
          <li>    filename, extension = os.path.splitext(fileNames)</li>
          <li>    if(extension in ['.zip']):</li>
          <li>      fileTypes = 'ZipFile'</li>
          <li>    elif(extension in ['.mrb'] ):</li>
          <li>      fileTypes = 'SceneFile'</li>
          <li>    elif(extension in ['.dcm', '.nrrd', '.nii', '.mhd', '.mha', '.hdr', '.img', '.bmp', '.jpg', '.jpeg', '.png', '.tif', '.tiff']):</li>
          <li>      fileTypes = 'VolumeFile'</li>
          <li>    elif(extension == '.gz'):</li>
          <li>      subfilename, subextension = os.path.splitext(filename)</li>
          <li>      if subextension == '.nii':</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/ImportFromURL/ImportFromURL.py#L165-L200" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #10 by @lassoan (2022-10-03 12:56 UTC)

<p><a class="mention" href="/u/rajesh_ds">@Rajesh_Ds</a> Do we understand correctly that you want to avoid popping up of the web browser and doing an extra click there? If that’s the issue then the solution I described should work well. On Windows the Slicer installer already associates the <code>slicer://</code> custom URL protocol with Slicer, so you just need to use the example file that I provided and change <code>nrrd</code> to <code>mrb</code>.</p>

---

## Post #11 by @Rajesh_Ds (2022-10-06 14:22 UTC)

<p>I have created a slicer scene  .mrml  file,  using python code. The attached image shows one of the niftii file that takes part in the scene.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a99e35e11e8c2b03efa0cbe9136d71d146c24b8e.png" data-download-href="/uploads/short-url/ocvEIZIhL7OHyjUkH3XZ4auku6y.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a99e35e11e8c2b03efa0cbe9136d71d146c24b8e.png" alt="image" data-base62-sha1="ocvEIZIhL7OHyjUkH3XZ4auku6y" width="690" height="326" data-dominant-color="EBEBEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">771×365 48.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If I transfer this scene file to a remote system, where (which folder in his system) must the recipient at the remote system store these nifii files. Is it possible to make slicer pick the niftii file from any folder that he wishes by inserting appropriate path information in the above identified location in the .mrml file (please see the attached image above)</p>

---

## Post #12 by @lassoan (2022-10-20 15:00 UTC)

<p>I’ve tested and download from an http uri works, just replace <code>filename</code> with <code>uri</code> and provide the url as value. I’ve now also <a href="https://github.com/Slicer/Slicer/pull/6604">added support for https</a> - this will be available in the Slicer Preview Release from tomorrow.</p>

---
