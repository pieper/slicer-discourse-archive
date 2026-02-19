---
topic_id: 30562
title: "Adding An Icon To Identify An Extension"
date: 2023-07-12
url: https://discourse.slicer.org/t/30562
---

# Adding an icon to identify an extension

**Topic ID**: 30562
**Date**: 2023-07-12
**URL**: https://discourse.slicer.org/t/adding-an-icon-to-identify-an-extension/30562

---

## Post #1 by @jhlegarreta (2023-07-12 19:06 UTC)

<p>Hi,<br>
when having adding some of the diffusion-related extension to the favorites toolbar I see that all have the same default icon used for extensions, which makes it difficult to recognize them.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/7788e4633a1bffc9bb09fc6bac47c20318ee8c77.png" data-download-href="/uploads/short-url/h3s6L8ZIOIy5DhABkeySkyEC1Xp.png?dl=1" title="slicer_favourite_toolbar" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/7788e4633a1bffc9bb09fc6bac47c20318ee8c77_2_690x31.png" alt="slicer_favourite_toolbar" data-base62-sha1="h3s6L8ZIOIy5DhABkeySkyEC1Xp" width="690" height="31" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/7788e4633a1bffc9bb09fc6bac47c20318ee8c77_2_690x31.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/7788e4633a1bffc9bb09fc6bac47c20318ee8c77_2_1035x46.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/7788e4633a1bffc9bb09fc6bac47c20318ee8c77.png 2x" data-dominant-color="D6D8DF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_favourite_toolbar</span><span class="informations">1066×48 13.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>What is the appropriate way to add an icon to each in the corresponding repository (<code>SlicerDMRI</code> I assume in this case)?</p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2023-07-12 19:14 UTC)

<p>They may be CLI modules. A CLI module is a simple executable that does not provide an icon, therefore only a generic icon is used. Since these modules are usually low-level data processing modules, lack of a recognizable icon is generally not a problem.</p>
<p>What are those diffusion-related modules that you are adding to the toolbar?</p>

---

## Post #3 by @jhlegarreta (2023-07-12 19:28 UTC)

<blockquote>
<p>What are those diffusion-related modules that you are adding to the toolbar?</p>
</blockquote>
<p><code>DiffusionTensorScalarMaps</code>, <code>TractographyDisplay</code>, which both have a user interface, to name two of them.</p>

---

## Post #4 by @lassoan (2023-07-13 01:18 UTC)

<p>These are the CLI modules (which right now cannot provide their module icon): <a href="https://github.com/SlicerDMRI/SlicerDMRI/tree/master/Modules/CLI">https://github.com/SlicerDMRI/SlicerDMRI/tree/master/Modules/CLI</a></p>
<p>It would be very easy to add an icon for any other modules, someone would just need to design those icons.</p>

---

## Post #5 by @jhlegarreta (2023-07-13 12:30 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="30562">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It would be very easy to add an icon for any other modules, someone would just need to design those icons.</p>
</blockquote>
</aside>
<p>I am interested in these CLI modules; designing or adding a self-created image would not be a problem, but if they cannot provide their own module icon, then there is nothing I can do.</p>

---

## Post #6 by @lassoan (2023-07-16 13:56 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a> what do you think about adding a new field to the CLI module description that would specify relative path of an extension icon in he (such as <code>&lt;icon&gt;ACPCTransform.png&lt;/icon&gt;</code>) in the <code>executable</code> element?</p>
<p>For example:</p>
<pre><code class="lang-xml">&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;executable&gt;
  &lt;category&gt;Registration.Specialized&lt;/category&gt;
  &lt;title&gt;ACPC Transform&lt;/title&gt;
  &lt;icon&gt;ACPCTransform.png&lt;/icon&gt;
  &lt;index&gt;1&lt;/index&gt;
  &lt;description&gt;&lt;![CDATA[&lt;p&gt;Calculate a transformation that aligns brain images to &lt;a href="https://en.wikipedia.org/wiki/Talairach_coordinates"&gt;Talairach coordinate system&lt;/a&gt; (also known as stereotaxic or ACPC coordinate system) based on anatomical landmarks.&lt;/p&gt;&lt;p&gt;The ACPC line extends between two points, one at the anterior commissure and one at the posterior commissure. The resulting transform will bring the line connecting the two points horizontal to the AP axis.&lt;/p&gt;&lt;p&gt;The midline is a series of points (at least 3) defining the division between the hemispheres of the brain (the mid sagittal plane). The resulting transform will result in the output volume having the mid sagittal plane lined up with the AS plane.&lt;/p&gt;&lt;p&gt;Use &lt;b&gt;Resample Scalar/Vector/DWI Volume&lt;/b&gt; to apply the transformation to a volume.&lt;/p&gt;]]&gt;&lt;/description&gt;
  &lt;version&gt;1.0&lt;/version&gt;
  &lt;documentation-url&gt;https://slicer.readthedocs.io/en/latest/user_guide/modules/acpctransform.html&lt;/documentation-url&gt;
  &lt;license&gt;slicer3&lt;/license&gt;
  &lt;contributor&gt;Nicole Aucoin (SPL, BWH), Ron Kikinis (SPL, BWH)&lt;/contributor&gt;
  &lt;acknowledgements&gt;&lt;![CDATA[This work is part of the National Alliance for Medical Image Computing (NAMIC), funded by the National Institutes of Health through the NIH Roadmap for Medical Research, Grant U54 EB005149.]]&gt;&lt;/acknowledgements&gt;
  &lt;parameters&gt;
...
  &lt;/parameters&gt;
&lt;/executable&gt;
</code></pre>

---

## Post #7 by @pieper (2023-07-16 16:34 UTC)

<p>I think that’s a great idea, no reason not to that I can see.</p>

---

## Post #8 by @jhlegarreta (2023-07-17 22:52 UTC)

<p>Thanks Andras. Let me know when things are ready to support this, and I will add an icon for the diffusion/tractography CLIs that are of interest to me.</p>

---

## Post #9 by @lassoan (2023-07-25 02:36 UTC)

<p>I had a closer look and CLI modules actually can already store icons, but they provide it on their standard output when the CLI module is launched with the <code>--logo</code> argument. It would be very inefficient to simply start using this feature, as it would mean running 50 executables at each Slicer startup to just get the CLI module icons. We would need to do something like that is done for the module description .xml files cache the icon files in the module folder so that the application can load them directly. Even then, loading 50 icon files may have add some perceivable delay at application startup. Maybe adding the icon to the .xml file would be faster (as we already load the .xml files at startup)? Another complication is that it is not trivial to bundle the icon file into the executable file (embedding binary resources into an executable is different on each compiler).</p>
<p>Exploring all the options and implement something that does not slow down application startup and remains compatible with the existing CLI module infrastructure would be quite significant work. Since the benefits are quite small, I don’t think this will be worked on soon. Anyway, this issue tracks this task:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/4145">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/4145" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/4145" target="_blank" rel="noopener">Allow adding logos and icon to a CLI module</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-13" data-time="00:56:39" data-timezone="UTC">12:56AM - 13 Mar 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/slicerbot" target="_blank" rel="noopener">
          <img alt="slicerbot" src="https://avatars.githubusercontent.com/u/10277015?v=4" class="onebox-avatar-inline" width="20" height="20">
          slicerbot
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:enhancement
        </span>
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          priority:low
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">_This issue was created automatically from an original [Mantis Issue](https://ma<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ntisarchive.slicer.org/view.php?id=4145). Further discussion may take place here._</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #10 by @jcfr (2023-07-25 03:12 UTC)

<p>As you outlined, we already have a mechanism to associate icons with CLIs.</p>
<p>To move forward, we could expand the XML description file with the <code>&lt;logo&gt;</code> element<sup class="footnote-ref"><a href="#footnote-98134-1" id="footnote-ref-98134-1">[1]</a></sup>.</p>
<p>It could accept the following:</p>
<pre><code class="lang-auto">data:image/png;base64,iVBORw0KG....
qrc:///path/to/image.png
file://relative/path/to/image.png
</code></pre>
<p>where:</p>
<ul>
<li>the <code>data</code>  URI scheme may be used to specify a base64 encoded image. See <a href="https://en.wikipedia.org/wiki/Data_URI_scheme">here</a></li>
<li>the <code>qrc</code> URI scheme may be used to specify an icon expected to be provided through the <a href="https://doc.qt.io/qt-5/resources.html">Qt resource system</a></li>
<li>the <code>file</code> URI scheme allows to specify a (relative) path for looking up the icon. To support the build and installed case, the path should be relative and the same in both cases.</li>
</ul>
<hr class="footnotes-sep">

<ol class="footnotes-list">
<li id="footnote-98134-1" class="footnote-item"><p>Using <code>logo</code> would be consistent with the current CLI parameter <code>--logo</code> and associated CMake macro argument <code>LOGO_HEADER</code>. <a href="#footnote-ref-98134-1" class="footnote-backref">↩︎</a></p>
</li>
</ol>

---

## Post #11 by @jhlegarreta (2023-07-25 13:12 UTC)

<p>Not sure if I follow the rationale of the icon resources needing to be loaded being prohibitive in terms of time; there are other modules (CLIs or not; I am still not that familiar with these in the context of Slicer) that have a non-negligible number of icons in their panels. But my knowledge about the underlying mechanisms is very limited, so my reasoning may not be accurate enough.</p>
<p>To me, being able to identify a tool is essential in an application, and as a user, I expect any application to offer this capability for the sake of usability.</p>
<p>I grant that if an application is too slow to start, this can bother some users in some contexts or deter them from using an application; but being slow at start is a one-time event, whereas being unable to identify an icon or needing to constantly navigate through a hierarchy of menus is a recurrent event within one session.</p>
<p>Maybe the feature is not straightforward to implement given the current constraints, but I do believe that it can make a difference in usability.</p>
<p>Thanks for your work Andras, JC.</p>

---

## Post #12 by @lassoan (2023-07-25 16:03 UTC)

<p>Loadable modules use the Qt resource system to efficiently load icons. It is a very much optimized system for both minimizing storage requirements and loading time. Since CLI modules are just standalone console applications that don’t depend on Qt, they cannot use the Qt resource system.</p>
<p>The cross-platform resource embedding mechanism that is currently implemented for CLI modules is quite slow and complicated to use, so we would need to revamp that before we can use it to load all CLI module icons at each startup.</p>
<p>Lack of icons for CLI modules is usually not a problem because CLI modules implement computational algorithms that users typically do not interact with directly, but via more convenient higher-level interactive “loadable” modules (which all have icons and nicer GUI).</p>

---
