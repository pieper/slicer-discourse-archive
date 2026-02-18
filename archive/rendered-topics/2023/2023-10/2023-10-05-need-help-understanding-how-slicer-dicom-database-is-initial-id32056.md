# Need help understanding how Slicer DICOM database is initialized

**Topic ID**: 32056
**Date**: 2023-10-05
**URL**: https://discourse.slicer.org/t/need-help-understanding-how-slicer-dicom-database-is-initialized/32056

---

## Post #1 by @fedorov (2023-10-05 20:00 UTC)

<p>I am trying to make an extension I am developing robust when launched right after Slicer install, where DICOM database is not initialized. I would like to understand 1) how to detect this; 2) how to address this.</p>
<p>What is confusing is that when I start Slicer for the first time, and open DICOM browser, I see the below:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68ad61234afdf1f4b8beb6252f78e9cc9c818354.png" data-download-href="/uploads/short-url/eW17tRZ3a8LvAbu31eL5EvLdYWM.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68ad61234afdf1f4b8beb6252f78e9cc9c818354_2_690x111.png" alt="image" data-base62-sha1="eW17tRZ3a8LvAbu31eL5EvLdYWM" width="690" height="111" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68ad61234afdf1f4b8beb6252f78e9cc9c818354_2_690x111.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68ad61234afdf1f4b8beb6252f78e9cc9c818354_2_1035x166.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68ad61234afdf1f4b8beb6252f78e9cc9c818354.png 2x" data-dominant-color="E3E3D0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1252×202 36.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But if I check the presence of DICOM database programmatically, I see this, which seems to indicate that the database exists:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b880898bb31a6969928c296a7c7fcd36f710b41.png" data-download-href="/uploads/short-url/8uDCwv8EhrKftMflvFrqnKdsOzf.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b880898bb31a6969928c296a7c7fcd36f710b41_2_690x220.png" alt="image" data-base62-sha1="8uDCwv8EhrKftMflvFrqnKdsOzf" width="690" height="220" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b880898bb31a6969928c296a7c7fcd36f710b41_2_690x220.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b880898bb31a6969928c296a7c7fcd36f710b41.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b880898bb31a6969928c296a7c7fcd36f710b41.png 2x" data-dominant-color="F4F4F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">708×226 34.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Can someone explain what this means, and how I can make sure that DICOM database “completely exists”?</p>

---

## Post #2 by @pieper (2023-10-05 20:19 UTC)

<p>This should work:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; slicer.util.selectModule('DICOM')
&gt;&gt;&gt; slicer.modules.DICOMWidget.browserWidget.dicomBrowser.createNewDatabaseDirectory()
</code></pre>
<p>From a script you might need to do a processEvents in between, not sure.</p>

---

## Post #3 by @fedorov (2023-10-05 21:51 UTC)

<p>Thanks to <a class="mention" href="/u/pieper">@pieper</a>, this has been solved!</p>
<p>I have to say this was not intuitive at all to me. The problem is that those database variables are initialized even though the database itself is not. So instead of checking that database is non-null, one needs to check if <code>databaseFilename</code> corresponds to an existing file. It is also super confusing that one needs to know where the pre-determined DICOM DB folder is located if one needs to delete it to reset Slicer installation to pristine state.</p>
<p>In any case, this is the solution:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/ImagingDataCommons/SlicerIDCBrowser/blob/45dfe14b3680bdf36186a11b94ee0ab27df87383/IDCBrowser/IDCBrowser.py#L102-L109">
  <header class="source">

      <a href="https://github.com/ImagingDataCommons/SlicerIDCBrowser/blob/45dfe14b3680bdf36186a11b94ee0ab27df87383/IDCBrowser/IDCBrowser.py#L102-L109" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/ImagingDataCommons/SlicerIDCBrowser/blob/45dfe14b3680bdf36186a11b94ee0ab27df87383/IDCBrowser/IDCBrowser.py#L102-L109" target="_blank" rel="noopener">ImagingDataCommons/SlicerIDCBrowser/blob/45dfe14b3680bdf36186a11b94ee0ab27df87383/IDCBrowser/IDCBrowser.py#L102-L109</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="102" style="counter-reset: li-counter 101 ;">
          <li>if not os.path.isfile(slicer.dicomDatabase.databaseFilename):</li>
          <li>  dicomBrowser = ctk.ctkDICOMBrowser()</li>
          <li>  dicomBrowser.databaseDirectory = slicer.dicomDatabase.databaseDirectory</li>
          <li>  dicomBrowser.createNewDatabaseDirectory()</li>
          <li>  slicer.dicomDatabase.openDatabase(slicer.dicomDatabase.databaseFilename)</li>
          <li>  logging.info("DICOM database created")</li>
          <li>else:</li>
          <li>  logging.info('DICOM database is available at '+slicer.dicomDatabase.databaseFilename)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I spent couple of hours earlier today trying to figure this out. Hope this will help someone else avoid my fate!</p>

---
