# Broken link for uploaded file on Slicer wiki

**Topic ID**: 9237
**Date**: 2019-11-20
**URL**: https://discourse.slicer.org/t/broken-link-for-uploaded-file-on-slicer-wiki/9237

---

## Post #1 by @fedorov (2019-11-20 20:44 UTC)

<p>Today I discovered that a PDF linked from a documentation wiki page disappeared (wiki page: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/MultiVolumeExplorer">https://www.slicer.org/wiki/Documentation/Nightly/Modules/MultiVolumeExplorer</a>, broken link: <a href="https://www.slicer.org/slicerWiki/images/8/8d/MultiVolumeExplorer_Meysam_SNR-April2013-v4.pdf">https://www.slicer.org/slicerWiki/images/8/8d/MultiVolumeExplorer_Meysam_SNR-April2013-v4.pdf</a>).</p>
<p><a class="mention" href="/u/freephile">@freephile</a> can you help with this issue?</p>
<p>I was instructed by <a class="mention" href="/u/mhalle">@mhalle</a> to post this issue on the forum.</p>

---

## Post #2 by @fedorov (2019-11-21 16:27 UTC)

<p><a class="mention" href="/u/freephile">@freephile</a> can you confirm you have seen this post? Do you think it is possible to recover the file missing?</p>

---

## Post #3 by @freephile (2019-11-21 17:20 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a></p>
<p>The file itself is at<br>
<aside class="onebox pdf">
  <header class="source">
      <a href="https://www.slicer.org/w/img_auth.php/8/8d/MultiVolumeExplorer_Meysam_SNR-April2013-v4.pdf" target="_blank" rel="nofollow noopener">slicer.org</a>
  </header>
  <article class="onebox-body">
    <a href="https://www.slicer.org/w/img_auth.php/8/8d/MultiVolumeExplorer_Meysam_SNR-April2013-v4.pdf" target="_blank" rel="nofollow noopener"><span class="pdf-onebox-logo"></span></a>
<h3><a href="https://www.slicer.org/w/img_auth.php/8/8d/MultiVolumeExplorer_Meysam_SNR-April2013-v4.pdf" target="_blank" rel="nofollow noopener">MultiVolumeExplorer_Meysam_SNR-April2013-v4.pdf</a></h3>

<p class="filesize">1984.43 KB</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>The wiki page for the file is<br>
<aside class="onebox pdf">
  <header class="source">
      <a href="https://www.slicer.org/wiki/File:MultiVolumeExplorer_Meysam_SNR-April2013-v4.pdf" target="_blank" rel="nofollow noopener">slicer.org</a>
  </header>
  <article class="onebox-body">
    <a href="https://www.slicer.org/wiki/File:MultiVolumeExplorer_Meysam_SNR-April2013-v4.pdf" target="_blank" rel="nofollow noopener"><span class="pdf-onebox-logo"></span></a>
<h3><a href="https://www.slicer.org/wiki/File:MultiVolumeExplorer_Meysam_SNR-April2013-v4.pdf" target="_blank" rel="nofollow noopener">File:MultiVolumeExplorer_Meysam_SNR-April2013-v4.pdf</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>The problem is simply that the very <strong>old</strong> ‘slicerWiki’ path is used in the wiki content you cited.</p>
<p>Using the <a href="https://www.slicer.org/wiki/Special:ReplaceText" rel="nofollow noopener">‘Replace Text’ extension</a> (a new admin feature of the Slicer wiki), I’m fixing hundreds of pages of content.  This will fix the problem ‘on wiki’.  For ‘off wiki’ content (e.g. bookmarks, publications), I’m currently working on implementing the rewrite rule which will a) serve the file at the correct location while b) sending a ‘moved permanently’ status code so old URLs are not indexed by search engines.</p>
<p>Aside: please post wiki issues to the eQuality Technology <a href="https://discourse.equality-tech.com" rel="nofollow noopener">Customer Support forum</a>.</p>

---

## Post #4 by @fedorov (2019-11-21 17:33 UTC)

<p>Greg, thank you for recovering the file!</p>
<aside class="quote no-group" data-username="freephile" data-post="3" data-topic="9237">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/freephile/48/248_2.png" class="avatar"> freephile:</div>
<blockquote>
<p>please post wiki issues to the eQuality Technology <a href="https://discourse.equality-tech.com">Customer Support forum</a></p>
</blockquote>
</aside>
<p>Indeed. I misunderstood instructions from <a class="mention" href="/u/mhalle">@mhalle</a>. Sorry.</p>

---

## Post #5 by @fedorov (2019-11-21 17:49 UTC)

<p>Greg, to make sure I understand correctly - it is not possible to make sure that the original link (<a href="https://www.slicer.org/slicerWiki/images/8/8d/MultiVolumeExplorer_Meysam_SNR-April2013-v4.pdf">https://www.slicer.org/slicerWiki/images/8/8d/MultiVolumeExplorer_Meysam_SNR-April2013-v4.pdf</a>) is functional, correct?</p>
<p>The issue is that this link is referenced from external sources, such as this post: <a href="https://discourse.slicer.org/t/how-to-analyze-dce-mri-data/622" class="inline-onebox">How to analyze DCE-MRI data</a>. I can fix the link in that post manually, but there may be other places I am not aware of. Overall, it is rather important that the original links don’t die. Is redirecting an option?</p>

---

## Post #6 by @freephile (2019-11-22 15:23 UTC)

<p>I’m working on the redirect rules now.</p>
<p>All “old” URLs will work – without appearing to search engines as if duplicate content is being served.  The correct URLs will become canonical, improving SEO.</p>

---

## Post #7 by @freephile (2019-11-26 15:03 UTC)

<p>This has been fixed, tested, and moved into production.<br>
<a href="https://discourse.equality-tech.com/t/add-rewrite-rules-to-nginx-to-replace-apache-rules/991/3" class="onebox" target="_blank" rel="nofollow noopener">https://discourse.equality-tech.com/t/add-rewrite-rules-to-nginx-to-replace-apache-rules/991/3</a></p>

---
