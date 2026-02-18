# SlicerPACSConnector available for testing

**Topic ID**: 19013
**Date**: 2021-08-01
**URL**: https://discourse.slicer.org/t/slicerpacsconnector-available-for-testing/19013

---

## Post #1 by @rbumm (2021-08-01 13:04 UTC)

<p>Hi,</p>
<p>I wrote a PACS connector extension during the last days from scripts I used during the last weeks. This improves the usability of 3D Slicer together with a local (hospital) or remote PACS.</p>
<p>The PACS Connector allows querying for AccessionNumber and SeriesDescription (new possibilities), the latter greatly reduces the size of datasets that need to be transferred into Slicers´ DICOM database because it gets/moves only the series that you really want.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/rbumm/SlicerPACSConnector">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/rbumm/SlicerPACSConnector" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/c9a57b0c73f765236a088f7bf59da4cf48addca768a60057e0da8f76a1a326e8/rbumm/SlicerPACSConnector" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/rbumm/SlicerPACSConnector" target="_blank" rel="noopener nofollow ugc">GitHub - rbumm/SlicerPACSConnector: The PACS Connector extension enables...</a></h3>

  <p>The PACS Connector extension enables querying your local or remote PACS from a clear and easily accessible interface within 3D Slicer and offers new filter parameters.     - GitHub - rbumm/SlicerPA...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/8425b744b8e4a1a816f1cb2218cefacd76b64946.png" data-download-href="/uploads/short-url/iR1PAj5KoSF8NPSs56fVuNWhCzY.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/8425b744b8e4a1a816f1cb2218cefacd76b64946.png" alt="image" data-base62-sha1="iR1PAj5KoSF8NPSs56fVuNWhCzY" width="400" height="500" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">495×618 9.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any comments are welcome, after your adaptations I would be glad to have the project considered to be included in the extension manager.</p>
<p>Best regards<br>
Rudolf</p>

---

## Post #2 by @slicer365 (2021-08-01 13:37 UTC)

<p>It can‘t support Slicer 4.11 ?</p>

---

## Post #3 by @rbumm (2021-08-01 14:21 UTC)

<p>No, it needs 4.13, I suggest using the nightly build</p>

---

## Post #4 by @rbumm (2021-08-02 13:12 UTC)

<p>Reconfirm this, just tested with Slicer 4.13.0-2021-07-29.</p>

---
