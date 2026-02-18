# Apple to deprecate OpenGL in OSX 10.14 Mojave

**Topic ID**: 3075
**Date**: 2018-06-05
**URL**: https://discourse.slicer.org/t/apple-to-deprecate-opengl-in-osx-10-14-mojave/3075

---

## Post #1 by @jdx-john (2018-06-05 09:48 UTC)

<p>Saw this from yesterday’s Apple conference. Obviously they are not removing GL from OSX anytime soon but that said, does Slicer (or maybe VTK?) already have support, or planned support, for Metal to replace GL?</p>
<p><a href="https://twitter.com/EvilBachus/status/1003722391627976705/photo/1?ref_src=twsrc%5Etfw&amp;ref_url=https%3A%2F%2Fwww.theregister.co.uk%2F2018%2F06%2F04%2Fapple_wwdc%2F" class="onebox" target="_blank" rel="noopener nofollow ugc">https://twitter.com/EvilBachus/status/1003722391627976705/photo/1?ref_src=twsrc^tfw&amp;ref_url=https%3A%2F%2Fwww.theregister.co.uk%2F2018%2F06%2F04%2Fapple_wwdc%2F</a></p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://developer.apple.com/whats-new/">
  <header class="source">
      <img src="https://developer.apple.com/favicon.ico" class="site-icon" width="" height="">

      <a href="https://developer.apple.com/whats-new/" target="_blank" rel="noopener nofollow ugc">Apple Developer</a>
  </header>

  <article class="onebox-body">
    <img width="" height="" src="https://developer.apple.com/news/images/og/sdk-17-og.jpg" class="thumbnail">

<h3><a href="https://developer.apple.com/whats-new/" target="_blank" rel="noopener nofollow ugc">What’s new for Apple developers</a></h3>

  <p>Learn about the key technologies and exciting capabilities available for Apple platforms, and download the tools you need to build incredible apps.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<blockquote>
<p>Deprecation of OpenGL and OpenCL<br>
Apps built using OpenGL and OpenCL will continue to run in macOS 10.14, but these legacy technologies are deprecated in macOS 10.14. Games and graphics-intensive apps that use OpenGL should now adopt Metal. Similarly, apps that use OpenCL for computational tasks should now adopt Metal and Metal Performance Shaders.</p>
<p>Metal is designed from the ground up to provide the best access to the modern GPUs on iOS, macOS, and tvOS devices. Metal avoids the overhead inherent in legacy technologies and exposes the latest graphics processing functionality. Unified support for graphics and compute in Metal lets your apps efficiently utilize the latest rendering techniques. For information about developing apps and games using Metal, see the developer documentation for Metal, Metal Performance Shaders, and MetalKit. For information about migrating OpenGL code to Metal, see Mixing Metal and OpenGL Rendering in a View.</p>
</blockquote>

---

## Post #2 by @pieper (2018-06-05 12:57 UTC)

<p>That’s a shame (as in shame on Apple for pushing their proprietary solution instead of open standards).  Microsoft does basically the same thing with DirectX.</p>
<p>I suspect it will be a long time (several years) before this has an impact on Slicer.  VTK serves as an abstraction of OpenGL for Slicer, so there’s little or no OpenGL code in Slicer itself.  In practice VTK only supports OpenGL currently, so porting VTK to Metal would be a big job.  Maybe an adaptor layer like <a href="https://github.com/google/angle">Angle</a> would be used.  I’m curious to hear what the VTK developers think about this.</p>

---

## Post #3 by @lassoan (2018-06-05 14:01 UTC)

<p>Apple’s statement of <em>“Games and graphics-intensive apps that use OpenGL should now adopt Metal.”</em> is ridiculous. As if they don’t know how much work it can be for applications to switch graphics backends…</p>
<p>Instead of switching to Metal, it is much more likely that multi-platform application developers will use adaptor libraries, so application performance may get slightly worse on Apple compared to other platforms; and Apple will have less control over the graphics stack on macOS.</p>
<p>This is not happening yet and Slicer is not impacted directly anyway but it is still sad to see Apple behaving like this instead of collaborating on improving open standards.</p>

---

## Post #4 by @chir.set (2018-06-05 15:33 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="3075">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>In practice VTK only supports OpenGL currently</p>
</blockquote>
</aside>
<p>Do you bundle OpenGL on Windows ? If so, can it be done for OSX ?</p>

---

## Post #5 by @jcfr (2018-06-05 15:36 UTC)

<p>There are few approaches to mitigate this. One of them could be to use <a href="https://moltengl.com/">https://moltengl.com/</a></p>

---

## Post #6 by @mhalle (2018-06-05 15:57 UTC)

<p>I would point out that X is still supported on macOS (via a community project, but still).  OpenGL isn’t going to disappear.</p>
<p>macOS’s OpenGL has always lagged behind the latest versions of the standard anyway: the latest versions on Apple hardware are 3.3 and 4.1, released eight years ago.  I think Apple made this decision a couple of years ago and just didn’t tell anyone.</p>
<p>It’s an unfortunate decision, and one that Kitware should open up with Apple as a vendor-to-vendor discussion,  but this isn’t going to have a perceivable impact on our community for a while.</p>
<p>Would I start an OpenCL-dependent project right now? No, but that was an iffy gamble anyway.</p>
<p>—Mike</p>

---

## Post #7 by @jcfr (2018-06-05 15:59 UTC)

<p>And here are some more details from the VTK core team:</p>
<aside class="onebox twitterstatus" data-onebox-src="https://twitter.com/Kitware/status/1004005222757404674">
  <header class="source">

      <a href="https://twitter.com/Kitware/status/1004005222757404674" target="_blank" rel="noopener">twitter.com</a>
  </header>

  <article class="onebox-body">
    <img src="https://pbs.twimg.com/profile_images/1471171969613803523/C2CCqi87_400x400.jpg" class="thumbnail onebox-avatar" width="" height="">
<h4><a href="https://twitter.com/Kitware/status/1004005222757404674" target="_blank" rel="noopener">Kitware</a></h4>
<div class="twitter-screen-name"><a href="https://twitter.com/Kitware/status/1004005222757404674" target="_blank" rel="noopener">@Kitware</a></div>

<div class="tweet">
  <span class="tweet-description"><a href="https://twitter.com/EngNadeau" target="_blank" rel="noopener">@EngNadeau</a> Early VTK supported multiple backends, and recent experience with modern OpenGL, WebGL, OSPRay and OptiX ports has given us confidence that we can maintain <a href="https://twitter.com/Apple" target="_blank" rel="noopener">@Apple</a> support. We are already talking about prototypes.</span>
</div>

<div class="date">
  <a href="https://twitter.com/Kitware/status/1004005222757404674" class="timestamp" target="_blank" rel="noopener">2:21 PM - 5 Jun 2018</a>

    <span class="like">
      <svg viewbox="0 0 512 512" width="14px" height="16px" aria-hidden="true">
        <path d="M462.3 62.6C407.5 15.9 326 24.3 275.7 76.2L256 96.5l-19.7-20.3C186.1 24.3 104.5 15.9 49.7 62.6c-62.8 53.6-66.1 149.8-9.9 207.9l193.5 199.8c12.5 12.9 32.8 12.9 45.3 0l193.5-199.8c56.3-58.1 53-154.3-9.8-207.9z"></path>
      </svg>
      1
    </span>

    <span class="retweet">
      <svg viewbox="0 0 640 512" width="14px" height="16px" aria-hidden="true">
        <path d="M629.657 343.598L528.971 444.284c-9.373 9.372-24.568 9.372-33.941 0L394.343 343.598c-9.373-9.373-9.373-24.569 0-33.941l10.823-10.823c9.562-9.562 25.133-9.34 34.419.492L480 342.118V160H292.451a24.005 24.005 0 0 1-16.971-7.029l-16-16C244.361 121.851 255.069 96 276.451 96H520c13.255 0 24 10.745 24 24v222.118l40.416-42.792c9.285-9.831 24.856-10.054 34.419-.492l10.823 10.823c9.372 9.372 9.372 24.569-.001 33.941zm-265.138 15.431A23.999 23.999 0 0 0 347.548 352H160V169.881l40.416 42.792c9.286 9.831 24.856 10.054 34.419.491l10.822-10.822c9.373-9.373 9.373-24.569 0-33.941L144.971 67.716c-9.373-9.373-24.569-9.373-33.941 0L10.343 168.402c-9.373 9.373-9.373 24.569 0 33.941l10.822 10.822c9.562 9.562 25.133 9.34 34.419-.491L96 169.881V392c0 13.255 10.745 24 24 24h243.549c21.382 0 32.09-25.851 16.971-40.971l-16.001-16z"></path>
      </svg>
      2
    </span>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox twitterstatus" data-onebox-src="https://twitter.com/Kitware/status/1004005538471055361">
  <header class="source">

      <a href="https://twitter.com/Kitware/status/1004005538471055361" target="_blank" rel="noopener">twitter.com</a>
  </header>

  <article class="onebox-body">
    <img src="https://pbs.twimg.com/profile_images/1471171969613803523/C2CCqi87_400x400.jpg" class="thumbnail onebox-avatar" width="" height="">
<h4><a href="https://twitter.com/Kitware/status/1004005538471055361" target="_blank" rel="noopener">Kitware</a></h4>
<div class="twitter-screen-name"><a href="https://twitter.com/Kitware/status/1004005538471055361" target="_blank" rel="noopener">@Kitware</a></div>

<div class="tweet">
  <span class="tweet-description"><a href="https://twitter.com/EngNadeau" target="_blank" rel="noopener">@EngNadeau</a> <a href="https://twitter.com/Apple" target="_blank" rel="noopener">@Apple</a> We expect the maintenance cost to grow, however. Even with one backend, it takes effort to ensure compliance across multiple operating systems and drivers. Dropping OpenGL increases that burden.</span>
</div>

<div class="date">
  <a href="https://twitter.com/Kitware/status/1004005538471055361" class="timestamp" target="_blank" rel="noopener">2:22 PM - 5 Jun 2018</a>

    <span class="like">
      <svg viewbox="0 0 512 512" width="14px" height="16px" aria-hidden="true">
        <path d="M462.3 62.6C407.5 15.9 326 24.3 275.7 76.2L256 96.5l-19.7-20.3C186.1 24.3 104.5 15.9 49.7 62.6c-62.8 53.6-66.1 149.8-9.9 207.9l193.5 199.8c12.5 12.9 32.8 12.9 45.3 0l193.5-199.8c56.3-58.1 53-154.3-9.8-207.9z"></path>
      </svg>
      1
    </span>

</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
