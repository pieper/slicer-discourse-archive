# Simple Filters module do not have any filters in latest nightly version

**Topic ID**: 6787
**Date**: 2019-05-14
**URL**: https://discourse.slicer.org/t/simple-filters-module-do-not-have-any-filters-in-latest-nightly-version/6787

---

## Post #1 by @juday (2019-05-14 16:21 UTC)

<p>I have similar issue. Slicer starts fine but unable to see any simple filters.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/3880f1cff52e51ce9fdb8a4c26fed764e86e5a95.png" data-download-href="/uploads/short-url/83R03coUzRSwnLHzDASvqy9Kqq1.png?dl=1" title="SimpleFilters%20error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/3880f1cff52e51ce9fdb8a4c26fed764e86e5a95_2_690x385.png" alt="SimpleFilters%20error" data-base62-sha1="83R03coUzRSwnLHzDASvqy9Kqq1" width="690" height="385" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/3880f1cff52e51ce9fdb8a4c26fed764e86e5a95_2_690x385.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/3880f1cff52e51ce9fdb8a4c26fed764e86e5a95_2_1035x577.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/3880f1cff52e51ce9fdb8a4c26fed764e86e5a95.png 2x" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SimpleFilters%20error</span><span class="informations">1153×645 71.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The dropdow menu under filters does not work and also the search field.</p>

---

## Post #2 by @jamesobutler (2019-05-14 16:41 UTC)

<p>Confirmed. SimpleFilters module needs to update the <a href="https://github.com/SimpleITK/SlicerSimpleFilters/blob/12efaabb0151c270e61bc7a3b3d08ad4c8db8095/SimpleFilters/SimpleFilters.py#L105" rel="nofollow noopener">following line</a> to support Python3 which is now used in Slicer.</p>

---

## Post #3 by @jamesobutler (2019-05-14 16:51 UTC)

<p>Issued has been created which you can follow the status</p><aside class="onebox githubissue" data-onebox-src="https://github.com/SimpleITK/SlicerSimpleFilters/issues/17">
  <header class="source">

      <a href="https://github.com/SimpleITK/SlicerSimpleFilters/issues/17" target="_blank" rel="noopener nofollow ugc">github.com/SimpleITK/SlicerSimpleFilters</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/SimpleITK/SlicerSimpleFilters/issues/17" target="_blank" rel="noopener nofollow ugc">Python3 compatibility issues</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2019-05-14" data-time="16:50:46" data-timezone="UTC">04:50PM - 14 May 19 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2019-06-02" data-time="18:07:44" data-timezone="UTC">06:07PM - 02 Jun 19 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">There are some compatibilities issues that were found by a user using the recent<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> Slicer nightly which uses Python3. 

https://discourse.slicer.org/t/simple-filters-module-do-not-have-any-filters-in-latest-nightly-version/6787
- On loading module
```log
Error while reading "C:\Program Files\Slicer 4.11.0-2019-05-13\lib\Slicer-4.11\qt-scripted-modules/Resources/json\AbsImageFilter.json". Exception: name 'file' is not defined
Error while reading "C:\Program Files\Slicer 4.11.0-2019-05-13\lib\Slicer-4.11\qt-scripted-modules/Resources/json\AbsoluteValueDifferenceImageFilter.json". Exception: name 'file' is not defined
Error while reading "C:\Program Files\Slicer 4.11.0-2019-05-13\lib\Slicer-4.11\qt-scripted-modules/Resources/json\AcosImageFilter.json". Exception: name 'file' is not defined
.
.
.
```


- Upon selecting one of the filters after changing `file()` usage to `open()`, there were more errors:  
```log
Traceback (most recent call last):
  File "C:/Program Files/Slicer 4.11.0-2019-05-13/bin/../lib/Slicer-4.11/qt-scripted-modules/SimpleFilters.py", line 268, in onFilterSelect
    self.filterParameters.create(json)
  File "C:/Program Files/Slicer 4.11.0-2019-05-13/bin/../lib/Slicer-4.11/qt-scripted-modules/SimpleFilters.py", line 817, in create
    w = self.createIntWidget(member["name"],t)
  File "C:/Program Files/Slicer 4.11.0-2019-05-13/bin/../lib/Slicer-4.11/qt-scripted-modules/SimpleFilters.py", line 963, in createIntWidget
    w.setValue(int(default))
NameError: name 'default' is not defined
```

More issues might be present, but these were the first I have noticed.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @jcfr (2019-05-15 04:22 UTC)

<p>Thanks for the report, these issues should now be fixed in <a href="https://github.com/SimpleITK/SlicerSimpleFilters/issues/17" rel="nofollow noopener">https://github.com/SimpleITK/SlicerSimpleFilters/issues/17</a></p>

---

## Post #5 by @jcfr (2019-05-21 05:08 UTC)

<p>Corresponding pull request has been integrated. You should expect the changes to be available <s>today or</s> tomorrow. Changes integrated in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=28261" rel="nofollow noopener">r28261</a></p>

---
