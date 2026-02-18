# Remove circular dependency between CompareVolumes and LandmarkRegistration

**Topic ID**: 44221
**Date**: 2025-08-27
**URL**: https://discourse.slicer.org/t/remove-circular-dependency-between-comparevolumes-and-landmarkregistration/44221

---

## Post #1 by @koeglfryderyk (2025-08-27 12:15 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> mentioned <a href="https://github.com/pieper/CompareVolumes/pull/16#pullrequestreview-3157455960" rel="noopener nofollow ugc">here</a> that it would be a good idea to remove the circular dependencies.</p>
<p>The simplest approach for me seemed to be just to move common functionality into <code>qt-scripted-modules/RegistrationLib/Visualization.py</code>.</p>
<p>Now CompareVolumes simply does <code>import RegistrationLib</code>and <code>LandmarkRegistration.py</code> and <code>Visualization.py</code> don’t import <code>CompareVolumes</code> any more.</p>
<p>You can take a look at the changes here:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/pieper/CompareVolumes/compare/master...koegl:CompareVolumes:removeCircularDependency">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" alt="" width="32" height="32">

      <a href="https://github.com/pieper/CompareVolumes/compare/master...koegl:CompareVolumes:removeCircularDependency" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/551f56ffa95e00f069d6855ae78596144fcdaf8842326ddc8308a386a63baec4/pieper/CompareVolumes" class="thumbnail" alt="" width="690" height="345"></div>

<h3><a href="https://github.com/pieper/CompareVolumes/compare/master...koegl:CompareVolumes:removeCircularDependency" target="_blank" rel="noopener nofollow ugc">Comparing pieper:master...koegl:removeCircularDependency · pieper/CompareVolumes</a></h3>

  <p>Slicer module providing high level layout and visualization options - Comparing pieper:master...koegl:removeCircularDependency · pieper/CompareVolumes</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/Slicer/LandmarkRegistration/compare/master...koegl:LandmarkRegistration:removeCircularDependency">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" alt="" width="32" height="32">

      <a href="https://github.com/Slicer/LandmarkRegistration/compare/master...koegl:LandmarkRegistration:removeCircularDependency" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/8e44f783f418efd3b874d145bf686452bef1156bbb953d9c60a4238c0e658ca6/Slicer/LandmarkRegistration" class="thumbnail" alt="" width="690" height="345"></div>

<h3><a href="https://github.com/Slicer/LandmarkRegistration/compare/master...koegl:LandmarkRegistration:removeCircularDependency" target="_blank" rel="noopener nofollow ugc">Comparing Slicer:master...koegl:removeCircularDependency ·...</a></h3>

  <p>An interactive registration tool that manages viewing and manipulating of sets of fiducials - Comparing Slicer:master...koegl:removeCircularDependency · Slicer/LandmarkRegistration</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @pieper (2025-08-27 15:43 UTC)

<p>Thanks <a class="mention" href="/u/koeglfryderyk">@koeglfryderyk</a> - I haven’t worked with the code in a while, so maybe what you are proposing is the most expeditious way to remove the circular dependency.  My thought though had been that the CompareVolumes code is more of the helper library and that LandmarkRegistration is the specific application so to me, putting the visualization and widgets in CompareVolumes would feel more natural.  I don’t know if you had looked into that and prefer this organization?</p>

---

## Post #3 by @koeglfryderyk (2025-08-28 11:12 UTC)

<p>My thinking was: <code>CompareVolumes.py</code> and <code>LandmarkRegistration.py</code> are scripted modules, so any code that they share (or that could be reused) should be moved to a helper library, e.g., to <code>RegistrationLib/Visualization.py</code></p>
<p>This way, any scripted module that wants to use this code can just import RegistrationLib</p>
<p>Does that make sense?</p>

---

## Post #4 by @pieper (2025-08-28 15:04 UTC)

<p>If you think it’s a lot of work to change we can leave it in RegistrationLib, but to me the visualization features and the corresponding widgets are proper to CompareVolumes.  The other RegistrationLib code is to support the different kinds of transforms that plug into LandmarkRegistration.  Since CompareVolumes is the more general module it makes more sense to me that other modules would only want to import the lower level code.  But your point is true that since they are both available in the app it doesn’t make any real practical difference.</p>

---
