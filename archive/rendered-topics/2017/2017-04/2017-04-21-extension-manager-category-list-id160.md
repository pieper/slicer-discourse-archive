---
topic_id: 160
title: "Extension Manager Category List"
date: 2017-04-21
url: https://discourse.slicer.org/t/160
---

# Extension manager category list

**Topic ID**: 160
**Date**: 2017-04-21
**URL**: https://discourse.slicer.org/t/extension-manager-category-list/160

---

## Post #1 by @lassoan (2017-04-21 03:21 UTC)

<p>Only the first 14 category names show up in the extension manager (Windows, latest nightly):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6de2042f77cf616431ca9cd6d8e95965d76051ea.png" data-download-href="/uploads/short-url/fG4hui8WKftLdF3AsvqAxpnRZgK.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6de2042f77cf616431ca9cd6d8e95965d76051ea_2_459x499.png" alt="image" data-base62-sha1="fG4hui8WKftLdF3AsvqAxpnRZgK" width="459" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6de2042f77cf616431ca9cd6d8e95965d76051ea_2_459x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6de2042f77cf616431ca9cd6d8e95965d76051ea_2_688x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6de2042f77cf616431ca9cd6d8e95965d76051ea.png 2x" data-dominant-color="D3D9DD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">913×994 284 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>For example, Registration category is not shown.</p>
<p>How should we fix this?</p>
<ul>
<li>Option A: fix category in all s4ext files to have meaningful categories(current categories are quite useless now, as there are only 1-2 extensions in most of them)</li>
<li>Option B: Fix Midas3 slicerappstore to show all categories</li>
</ul>

---

## Post #2 by @jcfr (2017-04-21 20:27 UTC)

<h3><a name="p-460-option-a-1" class="anchor" href="#p-460-option-a-1" aria-label="Heading link"></a>Option A</h3>
<aside class="quote no-group" data-username="lassoan" data-post="1" data-topic="160">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Option A: fix category in all s4ext files to have meaningful categories(current categories are quite useless now, as there are only 1-2 extensions in most of them)</p>
</blockquote>
</aside>
<p>Given the current infrastructure, we would have to submit an update to the project itself since it used to generate the description file.</p>
<h3><a name="p-460-option-b-2" class="anchor" href="#p-460-option-b-2" aria-label="Heading link"></a>Option B</h3>
<aside class="quote no-group" data-username="lassoan" data-post="1" data-topic="160">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Option B: Fix Midas3 slicerappstore to show all categories</p>
</blockquote>
</aside>
<p>Note that all categories (and sub-categories) are expected to be visible if they have at least one extension.</p>
<p>On the frontend, generation of the current category list happen here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/midasplatform/slicerappstore/blob/4b6c4ddfc4bff11a7137c88e24631741152301c6/public/js/index/index.index.js#L273-L277">
  <header class="source">

      <a href="https://github.com/midasplatform/slicerappstore/blob/4b6c4ddfc4bff11a7137c88e24631741152301c6/public/js/index/index.index.js#L273-L277" target="_blank" rel="noopener">github.com/midasplatform/slicerappstore</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/midasplatform/slicerappstore/blob/4b6c4ddfc4bff11a7137c88e24631741152301c6/public/js/index/index.index.js#L273-L277" target="_blank" rel="noopener">public/js/index/index.index.js</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/midasplatform/slicerappstore/blob/4b6c4ddfc4bff11a7137c88e24631741152301c6/public/js/index/index.index.js#L273-L277" rel="noopener"><code>4b6c4ddfc</code></a>
</div>



    <pre class="onebox"><code class="lang-js">
      <ol class="start lines" start="273" style="counter-reset: li-counter 272 ;">
          <li>$.each(midas.slicerappstore.categories, function(category, count) {</li>
          <li>    if(count &gt; 0) {</li>
          <li>        midas.slicerappstore.showCategory(category, count);</li>
          <li>    }</li>
          <li>});</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>and the corresponding data are gathered using a call like this one:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="http://slicer.kitware.com/midas3/slicerappstore/index/categories?os=win&amp;arch=amd64&amp;revision=25939">
  <header class="source">
      <img src="http://slicer.kitware.com/favicon.ico" class="site-icon" alt="" width="32" height="32">

      <a href="http://slicer.kitware.com/midas3/slicerappstore/index/categories?os=win&amp;arch=amd64&amp;revision=25939" target="_blank" rel="noopener">slicer.kitware.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="http://slicer.kitware.com/midas3/slicerappstore/index/categories?os=win&amp;arch=amd64&amp;revision=25939" target="_blank" rel="noopener">@KitwareMedical/slicer-extensions-webapp</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>returning</p>
<pre data-code-wrap="json"><code class="lang-json">{
  "Applications":"1",
  "Astronomy":"0",
  "CARMA":"0",
  "Cardiac":"2",
  "Cardiac MRI toolkit":"0",
  "Chest Imaging Platform":"1",
  "Converters":"1",
  "DICOM":"1",
  "Developer Tools":"3",
  "Diffusion":"2",
  "Diffusion.Tractography":"1",
  "Editor Effects":"1",
  "Editor Effects New":"0",
  "Epilepsy":"0",
  "Examples":"1",
  "Exporter":"1",
  "FiberViewer":"0",
  "Filtering":"2",
  "Filtering.Anomalous Filters":"0",
  "Filtering.Morphology":"0",
  "Heart":"0",
  "IGT":"9",
  "Informatics":"4",
  "Informatics Utilities 'Developer Tools'":"1",
  "Libraries":"1",
  "MARGIN CALCULATOR":"0",
  "Machine Learning":"1",
  "Mesh Generation":"1",
  "Microscopy":"0",
  "MultiDimension":"0",
  "Multidimensional data":"0",
  "Nuclear Medicine":"1",
  "Pathology":"0",
  "Port Placement":"0",
  "Quantification":"7",
  "Radiotherapy":"3",
  "Registration":"2",
  "Remote":"0",
  "Scoliosis":"0",
  "Segmentation":"11",
  "Sequences":"1",
  "Shape Analysis":"5",
  "Shape AnalysisRegistration":"0",
  "Surface Models":"0",
  "Thingiverse":"0",
  "Tractography":"0",
  "Training":"1",
  "Transforms":"1",
  "Utilities":"0",
  "Vascular Modeling Toolkit":"1",
  "Volume Rendering":"0",
  "Web System Tools":"1",
  "Wizards":"1",
  "\u201cIGT\u201d":"0",
  "\u201cRadiotherapy\u201d":"0"
}
</code></pre>
<p>Json formatted using <a href="https://jsonformatter.curiousconcept.com/">https://jsonformatter.curiousconcept.com/</a></p>
<h3><a name="p-460-alternative-idea-3" class="anchor" href="#p-460-alternative-idea-3" aria-label="Heading link"></a>Alternative idea</h3>
<p>Categorization could be done one our side without expecting extension maintainer to assign a category.</p>

---

## Post #3 by @lassoan (2017-04-21 20:40 UTC)

<p>We control the ExtensionsIndex, so we can change the categories.</p>
<p>The category list is cut off at about 14 elements. For example, you don’t see Registration category until you remove some modules by filtering, for example:</p>
<p>All modules are shown - Registration category not visible:<br>
<a href="http://slicer.kitware.com/midas3/slicerappstore/?os=win&amp;arch=amd64&amp;revision=25939&amp;category=&amp;search=&amp;layout=layout" class="onebox" target="_blank">http://slicer.kitware.com/midas3/slicerappstore/?os=win&amp;arch=amd64&amp;revision=25939&amp;category=&amp;search=&amp;layout=layout</a></p>
<p>Only a few modules are shown, Registration category shows up:<br>
<a href="http://slicer.kitware.com/midas3/slicerappstore/?os=win&amp;arch=amd64&amp;revision=25939&amp;category=&amp;search=ela&amp;layout=layout" class="onebox" target="_blank">http://slicer.kitware.com/midas3/slicerappstore/?os=win&amp;arch=amd64&amp;revision=25939&amp;category=&amp;search=ela&amp;layout=layout</a></p>
<p>If we cannot fix Midas then we should probably override category submissions in the ExtensionsIndex.</p>

---

## Post #4 by @jcfr (2017-04-21 21:33 UTC)

<p>I suspect the category with quote is causing trouble. <code>Informatics Utilities 'Developer Tools'</code> … looking at the code now.</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="160">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If we cannot fix Midas then we should probably override category submissions in the ExtensionsIndex</p>
</blockquote>
</aside>
<p>I think that will prove to be a lot of work with the current process in place. This means that every PR would have to be manually tweaked or fixed after integration.</p>

---

## Post #5 by @lassoan (2017-04-21 21:52 UTC)

<p>Not many extensions use git hashes and updates are not that frequent anyway. When we get an updated s4ext with a mismatched category name, we would ask developers to update their extension with the new category name and regenerate the s4ext.</p>
<p>Fixing Midas would be useful regardless.</p>

---

## Post #6 by @jcfr (2017-04-22 00:37 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="160">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Not many extensions use git hashes and updates are not that frequent anyway. When we get an updated s4ext with a mismatched category name, we would ask developers to update their extension with the new category name and regenerate the s4ext.</p>
</blockquote>
</aside>
<p>It means we should document the current valid and accepted category. That would help both “maintainer of” and “contributor to” the extension index.</p>
<p>Inclusion of new category would then be discussed and agreed within the community.</p>
<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="160">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Fixing Midas would be useful regardless.</p>
</blockquote>
</aside>
<p>Look like the culprit is indeed the category with quote, it should be easy to fix by having a robust sanitize function …</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0571c6be4cc5a2e5aed7430acf104e3f5b9754f.png" data-download-href="/uploads/short-url/yi9e6adNybW7bzbjEmjOCyLkVfV.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0571c6be4cc5a2e5aed7430acf104e3f5b9754f.png" alt="image" data-base62-sha1="yi9e6adNybW7bzbjEmjOCyLkVfV" width="690" height="69" data-dominant-color="E6E0E1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">878×88 13.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @jcfr (2017-04-22 00:39 UTC)

<p>The problem is here:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/midasplatform/slicerappstore/blob/4b6c4ddfc4bff11a7137c88e24631741152301c6/public/js/index/index.index.js#L240" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/midasplatform/slicerappstore/blob/4b6c4ddfc4bff11a7137c88e24631741152301c6/public/js/index/index.index.js#L240" target="_blank" rel="nofollow noopener">midasplatform/slicerappstore/blob/4b6c4ddfc4bff11a7137c88e24631741152301c6/public/js/index/index.index.js#L240</a></h4>
<pre class="onebox"><code class="lang-js"><ol class="start lines" start="230" style="counter-reset: li-counter 229 ;">
<li>}</li>
<li>
</li>
<li>/**</li>
<li>* Render the category tree based on tokens separated by . character</li>
<li>*/</li>
<li>midas.slicerappstore.showCategory = function(category, count) {</li>
<li>   var tokens = category.split('.');</li>
<li>   var lastToken = '';</li>
<li>   var name = '';</li>
<li>   $.each(tokens, function(k, token) {</li>
<li class="selected">       var tokenId = token.replace(/ /g, '_');</li>
<li>       var parentId = lastToken == '' ? 'categoriesList' : 'category_'+lastToken;</li>
<li>
</li>
<li>       name += token;</li>
<li>       if(lastToken != '') { //subcategory</li>
<li>           lastToken += '_';</li>
<li>           var id = 'category_'+lastToken+tokenId;</li>
<li>           if($('#'+id).length == 0) {</li>
<li>               var html = '&lt;li class="categoryControl" name="'+name+'" id="'+id+'"&gt;'+token+' ('+count+')&lt;/li&gt;';</li>
<li>               html = '&lt;ul class="categoriesSubList"&gt;'+html+'&lt;/ul&gt;';</li>
<li>               var el = $('#'+parentId);</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #8 by @jcfr (2017-04-22 01:03 UTC)

<p>Issue has been fixed in <a href="https://github.com/midasplatform/slicerappstore/commit/68db48e7b0f74f15752b4dfdbc26eab5f537224f">midasplatform/slicerappstore@68db48e</a> and deployed on the server.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61b58aee1da575081e5957b5acc63acb9246ee6b.png" data-download-href="/uploads/short-url/dWngCrxoTbDXl0bWnmRn5D4V2kP.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61b58aee1da575081e5957b5acc63acb9246ee6b_2_690x479.png" alt="image" data-base62-sha1="dWngCrxoTbDXl0bWnmRn5D4V2kP" width="690" height="479" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61b58aee1da575081e5957b5acc63acb9246ee6b_2_690x479.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61b58aee1da575081e5957b5acc63acb9246ee6b_2_1035x718.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61b58aee1da575081e5957b5acc63acb9246ee6b_2_1380x958.png 2x" data-dominant-color="F0F0EF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1385×962 124 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @lassoan (2017-04-22 01:42 UTC)

<p>This is great, thank you. Some more tuning may be needed, as clicking on the category with ’ in the name does not bring up any extension:</p>
<p><a href="http://slicer.kitware.com/midas3/slicerappstore/?os=win&amp;arch=amd64&amp;revision=25939&amp;category=Informatics%20Utilities%20'Developer%20Tools'&amp;search=&amp;layout=layout" class="onebox" target="_blank">http://slicer.kitware.com/midas3/slicerappstore/?os=win&amp;arch=amd64&amp;revision=25939&amp;category=Informatics%20Utilities%20’Developer%20Tools’&amp;search=&amp;layout=layout</a></p>
<p>I’ll start a new topic on defining good extension category names.</p>

---
