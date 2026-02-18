# Open Anatomy Export and 3dviewer.net with URL

**Topic ID**: 26726
**Date**: 2022-12-14
**URL**: https://discourse.slicer.org/t/open-anatomy-export-and-3dviewer-net-with-url/26726

---

## Post #1 by @rbumm (2022-12-14 13:30 UTC)

<p>Open Anatomy Export of a 3D Slicer segmentation (gltf file) and drop the file in the browser window of <a href="https://3dviewer.net/">3Dviewer.net</a> is a cool feature for sharing results in a working group.</p>
<p>Has somebody made 3dviewer work with an URL to a file in a shared Google Drive folder yet?</p>

---

## Post #2 by @Eserval (2022-12-14 15:03 UTC)

<p>I use this functionality as a routine. It’s really good to share the 3D models with the surgical team and even open in the operating room.<br>
I use Dropbox to store the .gltf and generate the link. Never used G drive.<br>
There is some dificulties in hiding parts by the cell phone. We need to use desktop mode in the browser. Also the 3D model is somewhat undefined, without texture.</p>

---

## Post #3 by @lassoan (2022-12-14 15:35 UTC)

<aside class="quote no-group" data-username="Eserval" data-post="2" data-topic="26726">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/eserval/48/14650_2.png" class="avatar"> Eserval:</div>
<blockquote>
<p>Also the 3D model is somewhat undefined, without texture.</p>
</blockquote>
</aside>
<p>I’m not sure if texture are needed to make the shapes a bit better defined. It would be nice if you could check if you can get the desired result by switching to PBR interpolation and tuning the shading parameters:</p>
<ul>
<li>Export the segmentation to models</li>
<li>Go to <code>Models</code> module</li>
<li>Choose a model that you want to improve the appearance of</li>
<li>Open <code>Display</code> / <code>3D Display</code> / <code>Advanced</code> section</li>
<li>Set <code>Interpolation</code> → <code>PBR</code> and adjust <code>Diffuse</code>, <code>Metallic</code>, <code>Roughness</code> parameters</li>
<li>Export the model folder (not the original segmentation) using OpenAnatomy export</li>
</ul>
<p>If we find that this results in significant improvement in appearance then we can expose some more shading settings in OpenAnatomy export (e.g., slider to make the models more or less shiny).</p>

---

## Post #4 by @Eserval (2022-12-14 15:59 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> ! I will try this later and post a feedback.</p>
<p>Just for illustrate, that is the actual result:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b5712f9ae42b8fc4971eb7dc76ba2489305c6ea.jpeg" data-download-href="/uploads/short-url/jSEVheJbkjeNnmrLMcnhaXWtYaS.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b5712f9ae42b8fc4971eb7dc76ba2489305c6ea_2_485x500.jpeg" alt="image" data-base62-sha1="jSEVheJbkjeNnmrLMcnhaXWtYaS" width="485" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b5712f9ae42b8fc4971eb7dc76ba2489305c6ea_2_485x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b5712f9ae42b8fc4971eb7dc76ba2489305c6ea.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b5712f9ae42b8fc4971eb7dc76ba2489305c6ea.jpeg 2x" data-dominant-color="D5C6C4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">552×568 69.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11bf29408f24a4406989bd33a517b6c60771314e.jpeg" data-download-href="/uploads/short-url/2wZG1FBNebPlHhyArbVVG02PEh8.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/11bf29408f24a4406989bd33a517b6c60771314e_2_355x500.jpeg" alt="image" data-base62-sha1="2wZG1FBNebPlHhyArbVVG02PEh8" width="355" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/11bf29408f24a4406989bd33a517b6c60771314e_2_355x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11bf29408f24a4406989bd33a517b6c60771314e.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11bf29408f24a4406989bd33a517b6c60771314e.jpeg 2x" data-dominant-color="CBA7A6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">393×553 50.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c279fa42411be6cac2097667494101615812944.jpeg" data-download-href="/uploads/short-url/8A9xz7ys7pXY3bIGvAKtTrMU5JG.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c279fa42411be6cac2097667494101615812944_2_279x500.jpeg" alt="image" data-base62-sha1="8A9xz7ys7pXY3bIGvAKtTrMU5JG" width="279" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c279fa42411be6cac2097667494101615812944_2_279x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c279fa42411be6cac2097667494101615812944.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c279fa42411be6cac2097667494101615812944.jpeg 2x" data-dominant-color="A0847C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">319×571 62.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>A patient with pulmonary sequestration that was operated last week.<br>
It’s not a bad result but in the 3D Slicer itself we have a better image quality.</p>

---

## Post #5 by @rbumm (2022-12-14 16:28 UTC)

<p>Nice. But do you have Dropbox access enabled in your hospital intranet? The other users must have Dropbox accounts?</p>

---

## Post #6 by @Eserval (2022-12-14 16:59 UTC)

<p>It’s not necessary that others users have any software instaled or dropbox account. I just send the link like that:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://3dviewer.net#model=https://dl.dropbox.com/s/zf2blp2kviil9iw/Caso%20S6%20-%20Preceptorship.gltf">
  <header class="source">
      <img src="https://3dviewer.net/assets/images/3dviewer_net_favicon.ico" class="site-icon" width="128" height="128">

      <a href="https://3dviewer.net#model=https://dl.dropbox.com/s/zf2blp2kviil9iw/Caso%20S6%20-%20Preceptorship.gltf" target="_blank" rel="noopener nofollow ugc">3dviewer.net</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://3dviewer.net/assets/images/3dviewer_net_logo_social.png" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://3dviewer.net#model=https://dl.dropbox.com/s/zf2blp2kviil9iw/Caso%20S6%20-%20Preceptorship.gltf" target="_blank" rel="noopener nofollow ugc">Online 3D Viewer</a></h3>

  <p>A free and open source web solution to visualize and explore 3D models right in your browser. Supported file formats: obj, 3ds, stl, ply, gltf, glb, off, 3dm, fbx, dae, wrl, 3mf, brep, step, iges, fcstd, ifc, bim.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>And they are able to open.</p>
<p>Most of time I open in my laptop because I need to connect in the robot console to use the Tilepro. Using the hospital wi-fi I never had any problems. However most of time I use the hospital open web (for guest and patients)… maybe if your hospital have some firewall block to Dropbox it’s possible that you have some difficulty.</p>

---

## Post #7 by @muratmaga (2022-12-14 17:25 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="5" data-topic="26726" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>Nice. But do you have Dropbox access enabled in your hospital intranet? The other users must have Dropbox accounts?</p>
</blockquote>
</aside>
<p>You don’t need to have a dropbox account (as the receiving user). The data poster should be able to put in a place where the full URL of the model is visible. So that leaves out google drive and box. E.g., <a href="https://drive.google.com/file/d/1mNiq3OMDU3q9Iab2UYdQ9jsyzQC_diap/view?usp=sharing" class="inline-onebox">Gor_template_low_res.ply - Google Drive</a> you can see the ply file, but if you paste this URL to 3D viewer like this</p>
<p><code>http://3dviewer.net/#model=https://drive.google.com/file/d/1mNiq3OMDU3q9Iab2UYdQ9jsyzQC_diap/view?usp=sharing</code></p>
<p>then 3Dviewer doesn’t display.</p>
<p>I don’t have dropbox subscription, but I find github to be sufficient. Eg:<br>
<a href="http://3dviewer.net/#model=https://github.com/SlicerMorph/SampleData/blob/master/baboon.gltf">`http://3dviewer.net/#model=https://github.com/SlicerMorph/SampleData/blob/master/baboon.gltf’</a></p>
<p>as long as you can live with 50MB file size restriction from the UI upload.</p>

---

## Post #8 by @muratmaga (2022-12-14 17:34 UTC)

<p>Also I would encourage people to suggest Kitware to add load data from URL option to their <a href="https://kitware.github.io/glance/app/">Glance viewer</a>.</p>
<p>Compared to 3Dviewer, you can embed volumes and other things in. Currently it works only with local data, or data posted to their cloud infrastructure.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc47a8ce872cd9f28a52a2ad427b2da52b5dd022.jpeg" data-download-href="/uploads/short-url/t98VSuzdNBmWTMfr4fWcLAbE2To.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc47a8ce872cd9f28a52a2ad427b2da52b5dd022_2_690x395.jpeg" alt="image" data-base62-sha1="t98VSuzdNBmWTMfr4fWcLAbE2To" width="690" height="395" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc47a8ce872cd9f28a52a2ad427b2da52b5dd022_2_690x395.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc47a8ce872cd9f28a52a2ad427b2da52b5dd022_2_1035x592.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc47a8ce872cd9f28a52a2ad427b2da52b5dd022.jpeg 2x" data-dominant-color="65636A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1326×760 74.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #9 by @rbumm (2022-12-14 19:03 UTC)

<p>GitHub would have been my next try, thanks. I can confirm your example works well. Where exactly do you upload your &gt; 25 MB files in which UI? I get error messages in the GitHub Web interface if I drop files  &gt; 25 MB.</p>

---

## Post #10 by @muratmaga (2022-12-14 19:23 UTC)

<p>Looks like I was mistaken, the UI limits is indeed 25MB.<br>
<a href="https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github#file-size-limits" class="onebox" target="_blank" rel="noopener">https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github#file-size-limits</a></p>
<p>But you can push more from command line…</p>

---

## Post #11 by @lassoan (2022-12-14 19:51 UTC)

<p>For sharing within a hospital VPN, you may use any file server in the hospital that can serve files via HTTP. You don’t need to use the hosted <a href="http://3dviewer.net/">http://3dviewer.net/</a> viewer but it should be easy to set up <a href="https://github.com/kovacsv/Online3DViewer" class="inline-onebox">GitHub - kovacsv/Online3DViewer: A solution to visualize and explore 3D models in your browser.</a> on the same file server.</p>

---

## Post #12 by @Eserval (2022-12-15 22:05 UTC)

<p>We can have a great improve performing that adjusts. Thanks for the advice <a class="mention" href="/u/lassoan">@lassoan</a> .<br>
There still is a loose in quality. However its a better option.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b232fb34d186fc339c876af4066b630be15ee38b.jpeg" data-download-href="/uploads/short-url/pqqdqFWNDxljWjqbW4BC0WfQucr.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b232fb34d186fc339c876af4066b630be15ee38b_2_517x500.jpeg" alt="image" data-base62-sha1="pqqdqFWNDxljWjqbW4BC0WfQucr" width="517" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b232fb34d186fc339c876af4066b630be15ee38b_2_517x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b232fb34d186fc339c876af4066b630be15ee38b_2_775x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b232fb34d186fc339c876af4066b630be15ee38b.jpeg 2x" data-dominant-color="A5A8AC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">859×830 77 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Slicer</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/58f5ad836d47cd3bfe9e4021deaacc7c7226e6dd.jpeg" data-download-href="/uploads/short-url/cGYnxiqO5FUuy0PrpMju8SaSRsh.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/58f5ad836d47cd3bfe9e4021deaacc7c7226e6dd_2_488x500.jpeg" alt="image" data-base62-sha1="cGYnxiqO5FUuy0PrpMju8SaSRsh" width="488" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/58f5ad836d47cd3bfe9e4021deaacc7c7226e6dd_2_488x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/58f5ad836d47cd3bfe9e4021deaacc7c7226e6dd.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/58f5ad836d47cd3bfe9e4021deaacc7c7226e6dd.jpeg 2x" data-dominant-color="BFCFD6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">596×610 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Online 3D Viewer</p>

---

## Post #13 by @Eserval (2022-12-15 22:26 UTC)

<p>Is there any tutorial for final users ? Tks</p>

---

## Post #14 by @lassoan (2022-12-16 05:33 UTC)

<aside class="quote no-group" data-username="Eserval" data-post="12" data-topic="26726">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/eserval/48/14650_2.png" class="avatar"> Eserval:</div>
<blockquote>
<p>We can have a great improve performing that adjusts. Thanks for the advice <a class="mention" href="/u/lassoan">@lassoan</a> .<br>
There still is a loose in quality. However its a better option.</p>
</blockquote>
</aside>
<p>Probably the issue is just that the default image-based lighting in <code>3dviewer.net</code> is a too bright. I’ve created an issue in the SlicerOpenAnatomy extension and described a few tips that may solve your remaining lighting issues:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/PerkLab/SlicerOpenAnatomy/issues/8">
  <header class="source">

      <a href="https://github.com/PerkLab/SlicerOpenAnatomy/issues/8" target="_blank" rel="noopener">github.com/PerkLab/SlicerOpenAnatomy</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/PerkLab/SlicerOpenAnatomy/issues/8" target="_blank" rel="noopener">Colors or lighting are not exactly the same in Slicer and glTF viewer</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-12-15" data-time="22:50:55" data-timezone="UTC">10:50PM - 15 Dec 22 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Colors appear to be lighter, somewhat washed out in glTF viewers - see

https:<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">//discourse.slicer.org/t/open-anatomy-export-and-3dviewer-net-with-url/26726/12?u=lassoan</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #15 by @forrest.li (2022-12-19 16:35 UTC)

<p>Hi there, Glance does actually support loading remote files from the URL: <a href="https://kitware.github.io/glance/doc/loading_files.html" class="inline-onebox" rel="noopener nofollow ugc">Loading Files | Glance</a></p>
<p>You can see a demonstration of this here: <a href="https://kitware.github.io/glance/app/?name=diskout.vtp&amp;url=https://data.kitware.com/api/v1/item/59de9de58d777f31ac641dc5/download" rel="noopener nofollow ugc">diskout.vtp</a></p>

---

## Post #16 by @muratmaga (2022-12-20 16:14 UTC)

<p>Doesn’t seem to work for me, at least for github. On 3D viewer:<br>
<code>https://kovacsv.hu/3dviewer.net/#model=https://github.com/SlicerMorph/SampleData/blob/master/Gor_template_low_res.ply</code></p>
<p>vs on glance</p>
<p><code>https://kitware.github.io/glance/app/?name=Gor_template_low_res.ply?url=https://github.com/SlicerMorph/SampleData/blob/master/Gor_template_low_res.ply</code></p>
<p>it would be also simpler if they construct a open URL button like 3D viewer does.</p>

---

## Post #17 by @jamesobutler (2022-12-20 18:39 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> The following seems to work for me after giving it a URL download link for GitHub rather than the regular link to the file page.</p>
<p><a href="https://kitware.github.io/glance/app/?name=Gor_template_low_res.ply&amp;url=https://raw.githubusercontent.com/SlicerMorph/SampleData/master/Gor_template_low_res.ply" rel="noopener nofollow ugc">Link</a>:<br>
<code>https://kitware.github.io/glance/app/?name=Gor_template_low_res.ply&amp;url=https://raw.githubusercontent.com/SlicerMorph/SampleData/master/Gor_template_low_res.ply</code></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/25d6d462c0ef9de194d519cf82642b260aff6bcb.png" data-download-href="/uploads/short-url/5oJW4WyfiJhJCFqWnom41OeNCR5.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/25d6d462c0ef9de194d519cf82642b260aff6bcb_2_690x370.png" alt="image" data-base62-sha1="5oJW4WyfiJhJCFqWnom41OeNCR5" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/25d6d462c0ef9de194d519cf82642b260aff6bcb_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/25d6d462c0ef9de194d519cf82642b260aff6bcb_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/25d6d462c0ef9de194d519cf82642b260aff6bcb_2_1380x740.png 2x" data-dominant-color="8D8D8D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1030 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #18 by @lassoan (2022-12-20 21:17 UTC)

<p><a href="http://3dviewer.net">3dviewer.net</a> has two very important features that I cannot seem to find in Kitware Glance:</p>
<ul>
<li>object hierarchy (select, expand/collapse, show/hide group of objects)</li>
<li>3D picking (click in the 3D view to see its name, see where is it in the hierarchy, and adjust properties)</li>
</ul>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3654f4a975b4329784e57051c04dad0b2ca065e.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3654f4a975b4329784e57051c04dad0b2ca065e.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3654f4a975b4329784e57051c04dad0b2ca065e.mp4</a>
    </source></video>
  </div><p></p>
<p>If these features could be added to Glance then it could become a useful web viewer for segmentations and atlases.</p>
<p>3D image volume/slice view rendering is a nice feature in Glance and although the 2D image slice viewer is very limited (there are no slice intersections, crosshair, etc.), this viewer is still better than most 3D web viewers, as they usually cannot display 3D image data at all.</p>

---

## Post #19 by @muratmaga (2022-12-20 22:55 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="17" data-topic="26726">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>The following seems to work for me after giving it a URL</p>
</blockquote>
</aside>
<p>Thanks for me as well. I still think they should do a open URL button and just simply parse the input URL on their end to construct it correctly.</p>

---

## Post #20 by @rbumm (2023-01-07 16:40 UTC)

<p>Found a way to use <a href="http://3Dviewer.net">3Dviewer.net</a> with data from an AWS S3 bucket and avoid the CORS error.</p>
<p>In “Permissions” of the S3 bucket</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8eceb0cfde5385357f40982ebc0017d61b579988.png" data-download-href="/uploads/short-url/knkDhgWn6ciEHI0Pbs96oJNTmHe.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8eceb0cfde5385357f40982ebc0017d61b579988_2_690x230.png" alt="image" data-base62-sha1="knkDhgWn6ciEHI0Pbs96oJNTmHe" width="690" height="230" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8eceb0cfde5385357f40982ebc0017d61b579988_2_690x230.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8eceb0cfde5385357f40982ebc0017d61b579988.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8eceb0cfde5385357f40982ebc0017d61b579988.png 2x" data-dominant-color="D2D4D6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1027×343 28.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>is a section</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1bc701e2a9d70e48f98c7336a2aa17fda9ec99ef.png" data-download-href="/uploads/short-url/3XJgj1P19e1yfMGgP1mzZU8u9af.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1bc701e2a9d70e48f98c7336a2aa17fda9ec99ef_2_690x119.png" alt="image" data-base62-sha1="3XJgj1P19e1yfMGgP1mzZU8u9af" width="690" height="119" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1bc701e2a9d70e48f98c7336a2aa17fda9ec99ef_2_690x119.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1bc701e2a9d70e48f98c7336a2aa17fda9ec99ef_2_1035x178.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1bc701e2a9d70e48f98c7336a2aa17fda9ec99ef_2_1380x238.png 2x" data-dominant-color="F8FAFB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1522×264 16.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>in which you can put</p>
<pre><code class="lang-auto">[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "PUT",
            "POST",
            "DELETE"
        ],
        "AllowedOrigins": [
            "https://kovacsv.hu/3dviewer.net"
        ],
        "ExposeHeaders": []
    },
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "PUT",
            "POST",
            "DELETE"
        ],
        "AllowedOrigins": [
            "https://kovacsv.hu/3dviewer.net"
        ],
        "ExposeHeaders": []
    },
    {
        "AllowedHeaders": [],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
]
</code></pre>
<p>so an URL like</p>
<pre><code class="lang-auto">https://kovacsv.hu/3dviewer.net/#model=https://rbummawsbucket.s3.eu-west-1.amazonaws.com/CTChest%20segmentation.gltf?response-content-disposition=inline&amp;X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDGV1LWNlbnRyYWwtMSJHMEUCIHkVcGi9QPtpow169oj6XyHlrKNTYsyqmF3Xi%2B0Eio%2BrAiEAghSOFXKeQprUoZQDpAHTVBWGYMZOFpgzB7jFw7%2BHPTkq5AIISRAAGgw4ODUzNDIxNDY2NTYiDB3%2FoAIGeYTBiVOhyyrBAq0j5FZzH1HE7Qi%2BCsXY1G6a0AvjXc0uoMT692NXeB%2FjJotVs2%2Fi1fWsaMkNYM0OUb9XppZKv3c4F1xurJoqpkR6x1ndliwSa9vvZXeEOHoV259Xb5MFPp6TU85qZSFJ4HAyEdkQu7NtQnSe%2F9exDA9aAB36GRUUfiA%2BYa8eztOZ%2Fdn5JItSiJIBF7Uq7VVmpBaiui5Fw3hoOFhB1c6qUpmgQ4QLAjDDmqC2Ja5TGmmrGSBIapxNaxZL8IpCe2JdV3sPmbyEt3b3%2F0VR9AR2dl4U6F4DsThJr5DUqKp1hPWBYbVkCEUykAq2X5I9p4woNMeS%2FWO6qso7mb07Q34PZXDXfqbt26%2FNyfudouAFsKwWhtWZ4Mx67qNZg5dI1QVXlyxTDqjMZtEJu5a4TT2eZIjTR8Ury9Rz2zSzElHrygeu5TDFquadBjqzAk9yE6c1kihDHtzs1s9QaUcRRENStAvw09fPfKFvzrAc5R3ZpoPWqmL2iQFIPz6efhcLfI%2F2%2FNhBtNYm6pvz9zLQt1Y2xRw2C8HLb%2Bmof9stS2jTzrIQ7VNcDATCsQ%2BitML2wncolYArIpgQlQAk7oinSUMx5iCB%2B55Ra36pyrDFwSFbnZpT8B9EZWywVUWHzcoN3Lq9epDAzRa%2BhlRtkwHIH%2Bi0rNhLLF0VK3D%2F%2FEeEXrxFtqiBOAwx5%2FPJSqNbpx34MHhcz%2FqMCMvZLGwTS9%2BucUwzSB9Jp6%2BV2lBqd4M7W5ja4PRXASUdwjbvQJFDMeYOznJ6BGvMCr7Ho544hnBdzROMCW%2Fk0dPN2FaRgYYJP6CpkMDHdNtFnvs3y60lK1DIGm1kYSfkCLkGnD%2FQQyv4K44%3D&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Date=20230107T163256Z&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Expires=43200&amp;X-Amz-Credential=ASIA44IUBCBQAXFWWLMS%2F20230107%2Feu-west-1%2Fs3%2Faws4_request&amp;X-Amz-Signature=eb9693d9d5519b71b61a35fea20b36344d47157fcf7f01eeda0bbf07525d172a
</code></pre>
<p>would work.</p>
<p>The above demo link one of a 10 MB gltf file is only active for 12 h per definition on a non-public S3 bucket from now, which is great because afterward, it expires in case you would use half sensitive data. And it saves access costs.</p>

---
