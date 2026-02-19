---
topic_id: 8532
title: "Newmat C Matrix Library"
date: 2019-09-23
url: https://discourse.slicer.org/t/8532
---

# Newmat C++ matrix library

**Topic ID**: 8532
**Date**: 2019-09-23
**URL**: https://discourse.slicer.org/t/newmat-c-matrix-library/8532

---

## Post #1 by @danial (2019-09-23 07:43 UTC)

<p>Operating system: MacOS-10.14<br>
Slicer version: 4.10.2</p>
<p>Hello,</p>
<p>I’m trying to use newmat11 (<a href="http://www.robertnz.net/nm_intro.htm" rel="noopener nofollow ugc">Newmat C++ matrix library</a>) library in my module, but a syntax error is found <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<blockquote>
<p>controlw.h:49:4: error: unknown type name ‘FREE_CHECK’</p>
</blockquote>
<pre><code>/// \ingroup newmat
///@{

/// \file controlw.h
/// Control word class.
/// Manipulate bits used for setting options.


#ifndef CONTROL_WORD_LIB
#define CONTROL_WORD_LIB 0

/// Organise an int as a series of bits to set options.
/// \internal
class ControlWord
{
protected:
   int cw;                                      // the control word
public:
   ControlWord() : cw(0) {}                     // do nothing
   ControlWord(int i) : cw(i) {}                // load an integer

      // select specific bits (for testing at least one set)
   ControlWord operator*(ControlWord i) const
      { return ControlWord(cw &amp; i.cw); }
   void operator*=(ControlWord i)  { cw &amp;= i.cw; }

      // set bits
   ControlWord operator+(ControlWord i) const
      { return ControlWord(cw | i.cw); }
   void operator+=(ControlWord i)  { cw |= i.cw; }

      // reset bits
   ControlWord operator-(ControlWord i) const
      { return ControlWord(cw - (cw &amp; i.cw)); }
   void operator-=(ControlWord i) { cw -= (cw &amp; i.cw); }

      // check if all of selected bits set or reset
   bool operator&gt;=(ControlWord i) const { return (cw &amp; i.cw) == i.cw; }
   bool operator&lt;=(ControlWord i) const { return (cw &amp; i.cw) == cw; }

      // flip selected bits
   ControlWord operator^(ControlWord i) const
      { return ControlWord(cw ^ i.cw); }
   ControlWord operator~() const { return ControlWord(~cw); }

      // convert to integer
   int operator+() const { return cw; }
   int operator!() const { return cw==0; }
   FREE_CHECK(ControlWord)
};


#endif

///@}
</code></pre>
<p>Any ideas on what’s going on and how to fix it?</p>
<p>Thanks for your help.</p>

---

## Post #2 by @pieper (2019-09-23 11:17 UTC)

<p>I don’t know much about the newmat library, but from a quick look at the homepage it looks pretty old and could be hard to support.  Can’t you do what you need with numpy or <a href="https://vxl.github.io/" rel="nofollow noopener">vnl</a> in itk?  Those are already compiled on all platforms.</p>

---

## Post #3 by @danial (2019-09-25 04:48 UTC)

<p>Thank you for your answer. I will try replace it with bumpy or vnl.</p>

---
