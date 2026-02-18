# Piece of C++ programming in ITK examples

**Topic ID**: 10648
**Date**: 2020-03-11
**URL**: https://discourse.slicer.org/t/piece-of-c-programming-in-itk-examples/10648

---

## Post #1 by @MachadoL (2020-03-11 17:44 UTC)

<p>Hey guys,</p>
<p>very basic question here. What does the operator <code>&lt;&lt;</code> do in the following line of the example <code>DeformableRegistration6.cxx</code>?</p>
<pre><code>TransformType::MeshSizeType requiredMeshSize;
for( unsigned int d = 0; d &lt; ImageDimension; d++ )   
 {
   requiredMeshSize[d] = meshSize[d] &lt;&lt; level;
 }
</code></pre>
<p><code>Level</code> is an integer number; <code>requiredMeshSize</code> is an integer vector of <code>imageDimension</code> size;</p>
<p>The example is explained at page 758 of the (PDF) ITK Software Guide.</p>
<p>Thanks in advance.</p>

---

## Post #2 by @dave3d (2020-03-11 17:51 UTC)

<p>That’s doing bit shifting.  So ‘meshSize[d]’ is getting bit shifted ‘level’ times.  Essentially it’s double ‘meshSize[d]’ ‘level’ times.</p>

---

## Post #3 by @MachadoL (2020-03-11 18:01 UTC)

<p>Still, hard to grasp. Is it doing binary operations? Where can I learn such association bitshifting with multiplication.<br>
Thanks anyway! <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=9" title=":wink:" class="emoji" alt=":wink:"></p>

---

## Post #4 by @dave3d (2020-03-11 18:08 UTC)

<p>Here’s the Wikipedia entry for C’s bit operations:<br>
<aside class="onebox wikipedia">
  <header class="source">
      <a href="https://en.wikipedia.org/wiki/Bitwise_operations_in_C" target="_blank" rel="nofollow noopener">en.wikipedia.org</a>
  </header>
  <article class="onebox-body">
    

<h3><a href="https://en.wikipedia.org/wiki/Bitwise_operations_in_C" target="_blank" rel="nofollow noopener">Bitwise operations in C</a></h3>

<p>
 In the C programming language, operations can be performed on a bit level using bitwise operators.
 Bitwise operations are contrasted by byte-level operations which characterize the bitwise operators' logical counterparts, the AND, OR and NOT operators. Instead of performing on individual bits, byte-level operators perform on strings of eight bits (known as bytes) at a time. The reason for this is that a byte is normally the smallest unit of addressable memory (i.e. data with a unique memory ad...</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>Half way down they talk about bit shifting.</p>
<p>Here’s a simple example:</p>
<pre><code>unsigned char x=1;

unsigned char y = x &lt;&lt; 1;
</code></pre>
<p>The binary representation of x is 0000 0001.  Doing 1 bit shift to the left gets you 0000 0010.  So y==2.</p>
<p>For every bit shift operation, all the binary digits get shifted one position to the left.  In effect, you are multiplying by 2, until you run out of bits.  Any bit at the top gets lost in the bit shift.</p>

---

## Post #5 by @MachadoL (2020-03-11 19:27 UTC)

<p>Great!!! Thank you so much for your patience.<br>
I guess I got it!<br>
Thanks again.</p>

---

## Post #6 by @dave3d (2020-03-11 19:47 UTC)

<p>It’s one of those old-school C optimizations.  Back in the day shift operations where much faster (1 cycle) than multiple operations (O(# bits), I think).</p>
<p>But these days, who the heck cares?  And it makes the code harder to understand if you’re not familiar with these things.</p>

---
