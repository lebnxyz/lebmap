"""
Very, very quick-n-dirty solution to formatting questions.json the way
I want it to be formatted. Everything below the JSONEncoder class
definition is my own, but the rest is janked and hastily modified from
various parts of PyPy's source, and the license for all of it follows:

License
=======

Except when otherwise stated (look for LICENSE files in directories or
information at the beginning of each file) all software and documentation in
the 'rpython', 'pypy', 'ctype_configure', 'dotviewer', 'demo', 'lib_pypy',
'py', and '_pytest' directories is licensed as follows:

    The MIT License

    Permission is hereby granted, free of charge, to any person
    obtaining a copy of this software and associated documentation
    files (the "Software"), to deal in the Software without
    restriction, including without limitation the rights to use,
    copy, modify, merge, publish, distribute, sublicense, and/or
    sell copies of the Software, and to permit persons to whom the
    Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included
    in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
    OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
    THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
    DEALINGS IN THE SOFTWARE.


PyPy Copyright holders 2003-2019
--------------------------------

Except when otherwise stated (look for LICENSE files or information at
the beginning of each file) the files in the 'pypy' directory are each
copyrighted by one or more of the following people and organizations:

  Armin Rigo
  Maciej Fijalkowski
  Carl Friedrich Bolz-Tereick
  Antonio Cuni
  Amaury Forgeot d'Arc
  Matti Picus
  Samuele Pedroni
  Ronan Lamy
  Alex Gaynor
  Philip Jenvey
  Richard Plangger
  Brian Kearns
  Michael Hudson-Doyle
  Manuel Jacob
  David Schneider
  Holger Krekel
  Christian Tismer
  Hakan Ardo
  Benjamin Peterson
  Anders Chrigstrom
  Wim Lavrijsen
  Eric van Riet Paap
  Remi Meier
  Richard Emslie
  Alexander Schremmer
  Dan Villiom Podlaski Christiansen
  Lukas Diekmann
  Sven Hager
  Anders Lehmann
  Aurelien Campeas
  Niklaus Haldimann
  Camillo Bruni
  Laura Creighton
  Toon Verwaest
  Leonardo Santagada
  Seo Sanghyeon
  Romain Guillebert
  Ronny Pfannschmidt
  Justin Peel
  Raffael Tfirst
  David Edelsohn
  Anders Hammarquist
  Jakub Gustak
  Gregor Wegberg
  Guido Wesdorp
  Lawrence Oluyede
  Bartosz Skowron
  Daniel Roberts
  Adrien Di Mascio
  Niko Matsakis
  Alexander Hesse
  Ludovic Aubry
  stian
  Jacob Hallen
  Jason Creighton
  Mark Young
  Alex Martelli
  Spenser Bauman
  Michal Bendowski
  Jan de Mooij
  Tyler Wade
  Vincent Legoll
  Michael Foord
  Stephan Diehl
  Stefano Rivera
  Jean-Paul Calderone
  Stefan Schwarzer
  Tomek Meka
  Valentino Volonghi
  Patrick Maupin
  Devin Jeanpierre
  Bob Ippolito
  Bruno Gola
  Andrew Lawrence
  David Malcolm
  Squeaky
  Edd Barrett
  Timo Paulssen
  Laurence Tratt
  Marius Gedminas
  Nicolas Truessel
  Alexandre Fayolle
  Simon Burton
  Martin Matusiak
  Wenzhu Man
  Konstantin Lopuhin
  John Witulski
  Stefan Beyer
  Jeremy Thurgood
  Greg Price
  Ivan Sichmann Freitas
  Dario Bertini
  Mark Pearse
  Simon Cross
  Tobias Pape
  Andreas StÃ¼hrk
  Jean-Philippe St. Pierre
  Guido van Rossum
  Pavel Vinogradov
  William Leslie
  PaweÅ‚ Piotr Przeradowski
  marky1991
  Ilya Osadchiy
  Tobias Oberstein
  Paul deGrandis
  Boris Feigin
  Taavi Burns
  Adrian Kuhn
  tav
  Stian Andreassen
  Georg Brandl
  Joannah Nanjekye
  Bert Freudenberg
  Wanja Saatkamp
  Mike Blume
  Gerald Klix
  Julian Berman
  Oscar Nierstrasz
  Rami Chowdhury
  Stefan H. Muller
  Dodan Mihai
  Tim Felgentreff
  Eugene Oden
  Colin Valliant
  Jeff Terrace
  Henry Mason
  Vasily Kuznetsov
  Preston Timmons
  David Ripton
  Pieter Zieschang
  Dusty Phillips
  Lukas Renggli
  Guenter Jantzen
  Jasper Schulz
  Ned Batchelder
  Amit Regmi
  Anton Gulenko
  Sergey Matyunin
  Andrew Chambers
  Åukasz Langa
  Nicolas Chauvat
  Andrew Durdin
  Ben Young
  Michael Schneider
  Yusuke Tsutsumi
  Nicholas Riley
  Jason Chu
  Igor Trindade Oliveira
  Yichao Yu
  Michael Twomey
  Rocco Moretti
  Gintautas Miliauskas
  Lucian Branescu Mihaila
  Mariano Anaya
  anatoly techtonik
  Karl Bartel
  Gabriel Lavoie
  Jared Grubb
  Alecsandru Patrascu
  Olivier Dormond
  Wouter van Heyst
  Sebastian PawluÅ›
  Brian Dorsey
  Victor Stinner
  Andrews Medina
  Aaron Iles
  Toby Watson
  Daniel Patrick
  Stuart Williams
  Antoine Pitrou
  Christian Hudon
  Justas Sadzevicius
  Neil Shepperd
  Michael Cheng
  Mikael SchÃ¶nenberg
  Stanislaw Halik
  Mihnea Saracin
  Matt Jackson
  Berkin Ilbeyi
  Gasper Zejn
  Faye Zhao
  Elmo MÃ¤ntynen
  Anders Qvist
  Corbin Simpson
  Chirag Jadwani
  Pauli Virtanen
  Jonathan David Riehl
  Beatrice During
  Alex Perry
  Robert Zaremba
  Alan McIntyre
  Alexander Sedov
  David C Ellis
  Vaibhav Sood
  Reuben Cummings
  Attila Gobi
  Floris Bruynooghe
  Christopher Pope
  Tristan Arthur
  Christian Tismer 
  Dan Stromberg
  Carl Meyer
  Florin Papa
  Arianna Avanzini
  Jens-Uwe Mager
  Valentina Mukhamedzhanova
  Stefano Parmesan
  touilleMan
  Marc Abramowitz
  Arjun Naik
  Aaron Gallagher
  Alexis Daboville
  Karl Ramm
  Lukas Vacek
  Omer Katz
  Jacek Generowicz
  Tomasz Dziopa
  Lin Cheng
  Sylvain Thenault
  Jakub Stasiak
  Andrew Dalke
  Alejandro J. Cura
  Vladimir Kryachko
  Gabriel
  Thomas Hisch
  Mark Williams
  Kunal Grover
  Nathan Taylor
  Barry Hart
  Travis Francis Athougies
  Yasir Suhail
  Sergey Kishchenko
  Martin Blais
  Lutz Paelike
  Ian Foote
  Philipp Rustemeuer
  Logan Chien
  Catalin Gabriel Manciu
  Jacob Oscarson
  Ryan Gonzalez
  Antoine Dupre
  Kristjan Valur Jonsson
  Lucio Torre
  Richard Lancaster
  Dan Buch
  Lene Wagner
  Tomo Cocoa
  Miro HronÄok
  Anthony Sottile
  David Lievens
  Neil Blakey-Milner
  Henrik Vendelbo
  Lars Wassermann
  Ignas Mikalajunas
  Christoph Gerum
  Miguel de Val Borro
  Artur Lisiecki
  afteryu
  Toni Mattis
  Laurens Van Houtven
  Bobby Impollonia
  Roberto De Ioris
  Jeong YunWon
  Christopher Armstrong
  Aaron Tubbs
  Vasantha Ganesh K
  Jason Michalski
  Radu Ciorba
  Markus Holtermann
  Andrew Thompson
  Yusei Tahara
  Ruochen Huang
  Fabio Niephaus
  Akira Li
  Gustavo Niemeyer
  Nate Bragg
  Lucas Stadler
  roberto@goyle
  Carl Bordum Hansen
  Matt Bogosian
  Yury V. Zaytsev
  florinpapa
  Anders Sigfridsson
  Nikolay Zinov
  rafalgalczynski@gmail.com
  Joshua Gilbert
  Anna Katrina Dominguez
  Kim Jin Su
  Amber Brown
  Andrew Stepanov
  RafaÅ‚ GaÅ‚czyÅ„ski
  Ben Darnell
  Juan Francisco Cantero Hurtado
  Godefroid Chappelle
  Stephan Busemann
  Dan Colish
  timo
  Volodymyr Vladymyrov
  Daniel NeuhÃ¤user
  Flavio Percoco
  halgari
  Jim Baker
  Chris Lambacher
  John Aldis
  coolbutuseless@gmail.com
  Mike Bayer
  Rodrigo AraÃºjo
  Daniil Yarancev
  Min RK
  OlivierBlanvillain
  Jonas Pfannschmidt
  Zearin
  Johan Forsberg
  Andrey Churin
  Dan Crosta
  reubano@gmail.com
  StanisÅ‚aw Halik
  Julien Phalip
  Roman Podoliaka
  Steve Papanik
  Eli Stevens
  Boglarka Vezer
  gabrielg@ec2-54-146-239-158.compute-1.amazonaws.com
  PavloKapyshin
  HervÃ© Beraud
  Tomer Chachamu
  Christopher Groskopf
  Asmo Soinio
  Antony Lee
  Jim Hunziker
  shoma hosaka
  Buck Golemon
  Iraklis D.
  JohnDoe
  yrttyr
  Michael Chermside
  Anna Ravencroft
  remarkablerocket
  Petre Vijiac
  Berker Peksag
  Christian Muirhead
  soareschen
  Matthew Miller
  Konrad Delong
  Dinu Gherman
  pizi
  TomÃ¡Å¡ PruÅ¾ina
  James Robert
  Armin Ronacher
  Diana Popa
  Mads Kiilerich
  Brett Cannon
  Caleb Hattingh
  aliceinwire
  Zooko Wilcox-O Hearn
  James Lan
  jiaaro
  Evgenii Gorinov
  Markus Unterwaditzer
  Kristoffer Kleine
  Graham Markall
  Dan Loewenherz
  werat
  Filip Salomonsson
  Niclas Olofsson
  Chris Pressey
  Tobias Diaz
  Paul Graydon
  Nikolaos-Digenis Karagiannis
  Kurt Griffiths
  Ben Mather
  Donald Stufft
  Dan Sanders
  Jason Madden
  Yaroslav Fedevych
  Even Wiik Thomassen
  m@funkyhat.org
  Stefan Marr

  Heinrich-Heine University, Germany
  Open End AB (formerly AB Strakt), Sweden
  merlinux GmbH, Germany
  tismerysoft GmbH, Germany
  Logilab Paris, France
  DFKI GmbH, Germany
  Impara, Germany
  Change Maker, Sweden
  University of California Berkeley, USA
  Google Inc.
  King's College London

The PyPy Logo as used by http://speed.pypy.org and others was created
by Samuel Reis and is distributed on terms of Creative Commons Share Alike
License.

License for 'lib-python/2.7, lib-python/3'
==========================================

Except when otherwise stated (look for LICENSE files or copyright/license
information at the beginning of each file) the files in the 'lib-python'
directory are all copyrighted by the Python Software Foundation and licensed
under the terms that you can find here: https://docs.python.org/3/license.html

License for 'pypy/module/unicodedata/'
======================================

The following files are from the website of The Unicode Consortium
at http://www.unicode.org/.  For the terms of use of these files, see
http://www.unicode.org/terms_of_use.html .  Or they are derived from
files from the above website, and the same terms of use apply.

    CompositionExclusions-*.txt
    EastAsianWidth-*.txt
    LineBreak-*.txt
    UnicodeData-*.txt
    UnihanNumeric-*.txt

License for 'dotviewer/font/'
=============================

Copyright (C) 2008 The Android Open Source Project

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Detailed license information is contained in the NOTICE file in the
directory.


Licenses and Acknowledgements for Incorporated Software
=======================================================

This section is an incomplete, but growing list of licenses and
acknowledgements for third-party software incorporated in the PyPy
distribution.

License for 'Tcl/Tk'
--------------------

This copy of PyPy contains library code that may, when used, result in
the Tcl/Tk library to be loaded.  PyPy also includes code that may be
regarded as being a copy of some parts of the Tcl/Tk header files.
You may see a copy of the License for Tcl/Tk in the file
`lib_pypy/_tkinter/license.terms` included here.

License for 'bzip2'
-------------------

This copy of PyPy may be linked (dynamically or statically) with the
bzip2 library.  You may see a copy of the License for bzip2/libbzip2 at

    http://www.bzip.org/1.0.5/bzip2-manual-1.0.5.html

License for 'openssl'
---------------------

This copy of PyPy may be linked (dynamically or statically) with the
openssl library.  You may see a copy of the License for OpenSSL at

    https://www.openssl.org/source/license.html

License for 'gdbm'
------------------

The gdbm module includes code from gdbm.h, which is distributed under
the terms of the GPL license version 2 or any later version.  Thus the
gdbm module, provided in the file lib_pypy/gdbm.py, is redistributed
under the terms of the GPL license as well.

License for 'rpython/rlib/rvmprof/src'
--------------------------------------

The code is based on gperftools. You may see a copy of the License for it at

    https://github.com/gperftools/gperftools/blob/master/COPYING
"""

import re

class StringBuilder:
    def __init__(self, init_size=100):
        self._l = []
        self._size = 0

    def _grow(self, size):
        self._size += size

    def append(self, s):
        assert isinstance(s, str)
        self._l.append(s)
        self._grow(len(s))

    def append_slice(self, s, start, end):
        assert isinstance(s, str)
        assert 0 <= start <= end <= len(s)
        s = s[start:end]
        self._l.append(s)
        self._grow(len(s))

    def append_multiple_char(self, c, times):
        assert isinstance(c, str)
        self._l.append(c * times)
        self._grow(times)

    def append_charpsize(self, s, size):
        assert size >= 0
        l = []
        for i in range(size):
            l.append(s[i])
        self._l.append("".join(l))
        self._grow(size)

    def build(self):
        result = "".join(self._l)
        assert len(result) == self._size
        self._l = [result]
        return result

    def getlength(self):
        return self._size



INFINITY = float('inf')

ESCAPE = re.compile(r'[\x00-\x1f\\"\b\f\n\r\t]')
ESCAPE_ASCII = re.compile(r'([\\"]|[^\ -~])')
HAS_UTF8 = re.compile(b'[\x80-\xff]')
ESCAPE_DCT = {
    '\\': '\\\\',
    '"': '\\"',
    '\b': '\\b',
    '\f': '\\f',
    '\n': '\\n',
    '\r': '\\r',
    '\t': '\\t',
}
for i in range(0x20):
    ESCAPE_DCT.setdefault(chr(i), '\\u{0:04x}'.format(i))
    #ESCAPE_DCT.setdefault(chr(i), '\\u%04x' % (i,))

def raw_encode_basestring(s):
    """Return a JSON representation of a Python string

    """
    def replace(match):
        return ESCAPE_DCT[match.group(0)]
    return ESCAPE.sub(replace, s)
encode_basestring = lambda s: '"' + raw_encode_basestring(s) + '"'


def raw_encode_basestring_ascii(s):
    """Return an ASCII-only JSON representation of a Python string

    """
    def replace(match):
        s = match.group(0)
        try:
            return ESCAPE_DCT[s]
        except KeyError:
            n = ord(s)
            if n < 0x10000:
                return '\\u{0:04x}'.format(n)
                #return '\\u%04x' % (n,)
            else:
                # surrogate pair
                n -= 0x10000
                s1 = 0xd800 | ((n >> 10) & 0x3ff)
                s2 = 0xdc00 | (n & 0x3ff)
                return '\\u{0:04x}\\u{1:04x}'.format(s1, s2)
    return ESCAPE_ASCII.sub(replace, s)
encode_basestring_ascii = lambda s: '"' + raw_encode_basestring_ascii(s) + '"'

class JSONEncoder(object):
    """Extensible JSON <http://json.org> encoder for Python data structures.

    Supports the following objects and types by default:

    +-------------------+---------------+
    | Python            | JSON          |
    +===================+===============+
    | dict              | object        |
    +-------------------+---------------+
    | list, tuple       | array         |
    +-------------------+---------------+
    | str               | string        |
    +-------------------+---------------+
    | int, float        | number        |
    +-------------------+---------------+
    | True              | true          |
    +-------------------+---------------+
    | False             | false         |
    +-------------------+---------------+
    | None              | null          |
    +-------------------+---------------+

    To extend this to recognize other objects, subclass and implement a
    ``.default()`` method with another method that returns a serializable
    object for ``o`` if possible, otherwise it should call the superclass
    implementation (to raise ``TypeError``).

    """
    item_separator = ', '
    key_separator = ': '
    def __init__(self, *, skipkeys=False, ensure_ascii=True,
            check_circular=True, allow_nan=True, sort_keys=False,
            indent=None, separators=None, default=None):
        """Constructor for JSONEncoder, with sensible defaults.

        If skipkeys is false, then it is a TypeError to attempt
        encoding of keys that are not str, int, float or None.  If
        skipkeys is True, such items are simply skipped.

        If ensure_ascii is true, the output is guaranteed to be str
        objects with all incoming non-ASCII characters escaped.  If
        ensure_ascii is false, the output can contain non-ASCII characters.

        If check_circular is true, then lists, dicts, and custom encoded
        objects will be checked for circular references during encoding to
        prevent an infinite recursion (which would cause an OverflowError).
        Otherwise, no such check takes place.

        If allow_nan is true, then NaN, Infinity, and -Infinity will be
        encoded as such.  This behavior is not JSON specification compliant,
        but is consistent with most JavaScript based encoders and decoders.
        Otherwise, it will be a ValueError to encode such floats.

        If sort_keys is true, then the output of dictionaries will be
        sorted by key; this is useful for regression tests to ensure
        that JSON serializations can be compared on a day-to-day basis.

        If indent is a non-negative integer, then JSON array
        elements and object members will be pretty-printed with that
        indent level.  An indent level of 0 will only insert newlines.
        None is the most compact representation.

        If specified, separators should be an (item_separator, key_separator)
        tuple.  The default is (', ', ': ') if *indent* is ``None`` and
        (',', ': ') otherwise.  To get the most compact JSON representation,
        you should specify (',', ':') to eliminate whitespace.

        If specified, default is a function that gets called for objects
        that can't otherwise be serialized.  It should return a JSON encodable
        version of the object or raise a ``TypeError``.

        """

        self.skipkeys = skipkeys
        self.ensure_ascii = ensure_ascii
        if ensure_ascii:
            self.__encoder = raw_encode_basestring_ascii
        else:
            self.__encoder = raw_encode_basestring
        self.check_circular = check_circular
        self.allow_nan = allow_nan
        self.sort_keys = sort_keys
        self.indent = indent
        if separators is not None:
            self.item_separator, self.key_separator = separators
        elif indent is not None:
            self.item_separator = ','
        if default is not None:
            self.default = default

        if indent is not None and not isinstance(indent, str):
            self.indent_str = ' ' * indent
        else:
            self.indent_str = indent
        
        self.do_not_indent = False
        self.in_dne_dict = False
        self.indent_once = False

    def default(self, o):
        """Implement this method in a subclass such that it returns
        a serializable object for ``o``, or calls the base implementation
        (to raise a ``TypeError``).

        For example, to support arbitrary iterators, you could
        implement default like this::

            def default(self, o):
                try:
                    iterable = iter(o)
                except TypeError:
                    pass
                else:
                    return list(iterable)
                # Let the base class default method raise the TypeError
                return JSONEncoder.default(self, o)

        """
        raise TypeError("Object of type '%s' is not JSON serializable" %
                        o.__class__.__name__)

    def encode(self, o):
        """Return a JSON string representation of a Python data structure.

        >>> from json.encoder import JSONEncoder
        >>> JSONEncoder().encode({"foo": ["bar", "baz"]})
        '{"foo": ["bar", "baz"]}'

        """
        if self.check_circular:
            markers = {}
        else:
            markers = None
        builder = StringBuilder()
        self.__encode(o, markers, builder, 0)
        return builder.build()

    def __emit_indent(self, builder, _current_indent_level):
        if self.indent != 'no' and (self.indent_once == 1 or self.indent is not None and not self.do_not_indent and not self.in_dne_dict):
            _current_indent_level += 1
            newline_indent = '\n' + self.indent_str * _current_indent_level
            separator = self.item_separator + newline_indent
            builder.append(newline_indent)
        else:
            separator = self.item_separator + ' '
        self.indent_once += 1
        return separator, _current_indent_level

    def __emit_unindent(self, builder, _current_indent_level):
        if self.indent != 'no' and (self.indent_once == 2 or self.indent is not None and not self.do_not_indent and not self.in_dne_dict):
            builder.append('\n')
            builder.append(self.indent_str * (_current_indent_level - 1))
        self.indent_once -= 1
        if self.indent_once == 1:
            self.indent_once = False

    def __encode(self, o, markers, builder, _current_indent_level):
        if isinstance(o, str):
            builder.append('"')
            builder.append(self.__encoder(o))
            builder.append('"')
        elif o is None:
            builder.append('null')
        elif o is True:
            builder.append('true')
        elif o is False:
            builder.append('false')
        elif isinstance(o, int):
            # Subclasses of int/float may override __str__, but we still
            # want to encode them as integers/floats in JSON. One example
            # within the standard library is IntEnum.
            builder.append(int.__str__(o))
        elif isinstance(o, float):
            builder.append(self.__floatstr(o))
        elif isinstance(o, (list, tuple)):
            if not o:
                builder.append('[]')
                return
            self.__encode_list(o, markers, builder, _current_indent_level)
        elif isinstance(o, dict):
            if not o:
                builder.append('{}')
                return
            self.__encode_dict(o, markers, builder, _current_indent_level)
        else:
            self.__mark_markers(markers, o)
            res = self.default(o)
            self.__encode(res, markers, builder, _current_indent_level)
            self.__remove_markers(markers, o)
            return res

    def __encode_list(self, l, markers, builder, _current_indent_level):
        _old_dne = self.do_not_indent
        self.do_not_indent = self.in_dne_dict or self.do_not_indent or len(l) == 1 and isinstance(l[0], list)
        self.__mark_markers(markers, l)
        builder.append('[')
        first = True
        separator, _current_indent_level = self.__emit_indent(builder,
                                                      _current_indent_level)
        _old_dne, self.do_not_indent = self.do_not_indent, _old_dne
        for elem in l:
            if first:
                first = False
            else:
                builder.append(separator)
            self.__encode(elem, markers, builder, _current_indent_level)
            del elem # XXX grumble
        _old_dne, self.do_not_indent = self.do_not_indent, _old_dne
        self.__emit_unindent(builder, _current_indent_level)
        self.do_not_indent = _old_dne
        builder.append(']')
        self.__remove_markers(markers, l)

    def __encode_dict(self, d, markers, builder, _current_indent_level):
        self.__mark_markers(markers, d)
        first = True
        builder.append('{')
        separator, _current_indent_level = self.__emit_indent(builder,
                                                         _current_indent_level)
        if self.sort_keys:
            items = sorted(d.items(), key=lambda kv: kv[0])
        else:
            items = d.items()

        for key, v in items:
            if first:
                first = False
            else:
                builder.append(separator)
            if isinstance(key, str):
                pass
            # JavaScript is weakly typed for these, so it makes sense to
            # also allow them.  Many encoders seem to do something like this.
            elif isinstance(key, float):
                key = self.__floatstr(key)
            elif key is True:
                key = 'true'
            elif key is False:
                key = 'false'
            elif key is None:
                key = 'null'
            elif isinstance(key, int):
                # see comment for int in __encode
                key = int.__str__(key)
            elif self.skipkeys:
                continue
            else:
                raise TypeError("key " + repr(key) + " is not a string")
            builder.append('"')
            builder.append(self.__encoder(key))
            builder.append('"')
            builder.append(self.key_separator)
            if key == 'templateArgs':
                _old_indent = self.indent
                self.indent = 'no'
            if key == 'options':
                _old_dne = self.do_not_indent
                self.in_dne_dict = True
                self.do_not_indent = True
                self.indent_once = True
            self.__encode(v, markers, builder, _current_indent_level)
            if key == 'templateArgs':
                self.indent = _old_indent
            if key == 'options':
                self.in_dne_dict = False
                self.do_not_indent = _old_dne
            del key
            del v # XXX grumble
        self.__emit_unindent(builder, _current_indent_level)
        builder.append('}')
        self.__remove_markers(markers, d)

    def iterencode(self, o, _one_shot=False):
        """Encode the given object and yield each string
        representation as available.

        For example::

            for chunk in JSONEncoder().iterencode(bigobject):
                mysocket.write(chunk)

        """
        raise NotImplementedError
        '''
        if self.check_circular:
            markers = {}
        else:
            markers = None
        return self.__iterencode(o, markers, 0)
        '''

    def __floatstr(self, o):
        # Check for specials.  Note that this type of test is processor
        # and/or platform-specific, so do tests which don't depend on the
        # internals.

        if o != o:
            text = 'NaN'
        elif o == INFINITY:
            text = 'Infinity'
        elif o == -INFINITY:
            text = '-Infinity'
        else:
            return float.__repr__(o)

        if not self.allow_nan:
            raise ValueError(
                "Out of range float values are not JSON compliant: " +
                repr(o))

        return text

    def __mark_markers(self, markers, o):
        if markers is not None:
            if id(o) in markers:
                raise ValueError("Circular reference detected")
            markers[id(o)] = None

    def __remove_markers(self, markers, o):
        if markers is not None:
            del markers[id(o)]

    def __iterencode_list(self, lst, markers, _current_indent_level):
        if not lst:
            yield '[]'
            return
        self.__mark_markers(markers, lst)
        buf = '['
        if self.indent is not None:
            _current_indent_level += 1
            newline_indent = '\n' + self.indent_str * _current_indent_level
            separator = self.item_separator + newline_indent
            buf += newline_indent
        else:
            newline_indent = None
            separator = self.item_separator
        first = True
        for value in lst:
            if first:
                first = False
            else:
                buf = separator
            if isinstance(value, str):
                yield buf + '"' + self.__encoder(value) + '"'
            elif value is None:
                yield buf + 'null'
            elif value is True:
                yield buf + 'true'
            elif value is False:
                yield buf + 'false'
            elif isinstance(value, int):
                # see comment for int in __encode
                yield buf + int.__str__(value)
            elif isinstance(value, float):
                yield buf + self.__floatstr(value)
            else:
                yield buf
                if isinstance(value, (list, tuple)):
                    chunks = self.__iterencode_list(value, markers,
                                                   _current_indent_level)
                elif isinstance(value, dict):
                    chunks = self.__iterencode_dict(value, markers,
                                                   _current_indent_level)
                else:
                    chunks = self.__iterencode(value, markers,
                                              _current_indent_level)
                yield from chunks
        if newline_indent is not None:
            _current_indent_level -= 1
            yield '\n' + self.indent_str * _current_indent_level
        yield ']'
        self.__remove_markers(markers, lst)

    def __iterencode_dict(self, dct, markers, _current_indent_level):
        if not dct:
            yield '{}'
            return
        self.__mark_markers(markers, dct)
        yield '{'
        if self.indent is not None:
            _current_indent_level += 1
            newline_indent = '\n' + self.indent_str * _current_indent_level
            item_separator = self.item_separator + newline_indent
            yield newline_indent
        else:
            newline_indent = None
            item_separator = self.item_separator
        first = True
        if self.sort_keys:
            items = sorted(dct.items(), key=lambda kv: kv[0])
        else:
            items = dct.items()
        for key, value in items:
            if isinstance(key, str):
                pass
            # JavaScript is weakly typed for these, so it makes sense to
            # also allow them.  Many encoders seem to do something like this.
            elif isinstance(key, float):
                key = self.__floatstr(key)
            elif key is True:
                key = 'true'
            elif key is False:
                key = 'false'
            elif key is None:
                key = 'null'
            elif isinstance(key, int):
                # see comment for int in __encode
                key = int.__str__(key)
            elif self.skipkeys:
                continue
            else:
                raise TypeError("key " + repr(key) + " is not a string")
            if first:
                first = False
            else:
                yield item_separator
            yield '"' + self.__encoder(key) + '"'
            yield self.key_separator
            if isinstance(value, str):
                yield '"' + self.__encoder(value) + '"'
            elif value is None:
                yield 'null'
            elif value is True:
                yield 'true'
            elif value is False:
                yield 'false'
            elif isinstance(value, int):
                yield int.__str__(value)
            elif isinstance(value, float):
                yield self.__floatstr(value)
            else:
                if isinstance(value, (list, tuple)):
                    chunks = self.__iterencode_list(value, markers,
                                                   _current_indent_level)
                elif isinstance(value, dict):
                    chunks = self.__iterencode_dict(value, markers,
                                                   _current_indent_level)
                else:
                    chunks = self.__iterencode(value, markers,
                                              _current_indent_level)
                yield from chunks
        if newline_indent is not None:
            _current_indent_level -= 1
            yield '\n' + self.indent_str * _current_indent_level
        yield '}'
        self.__remove_markers(markers, dct)

    def __iterencode(self, o, markers, _current_indent_level):
        if isinstance(o, str):
            yield '"' + self.__encoder(o) + '"'
        elif o is None:
            yield 'null'
        elif o is True:
            yield 'true'
        elif o is False:
            yield 'false'
        elif isinstance(o, int):
            yield int.__str__(o)
        elif isinstance(o, float):
            yield self.__floatstr(o)
        elif isinstance(o, (list, tuple)):
            yield from self.__iterencode_list(o, markers, _current_indent_level)
        elif isinstance(o, dict):
            yield from self.__iterencode_dict(o, markers, _current_indent_level)
        else:
            self.__mark_markers(markers, o)
            obj = self.default(o)
            yield from self.__iterencode(obj, markers, _current_indent_level)
            self.__remove_markers(markers, o)

encode = JSONEncoder(indent=4).encode
import json
def reformat(s):
    return encode(json.loads(s))
def write(obj, path):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(encode(obj))
