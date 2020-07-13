#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : svg.path
Version  : 4.0.2
Release  : 11
URL      : https://files.pythonhosted.org/packages/63/f9/56781c02bb69f96f0af1644aaabf065bea6cb0e67ffe2b3ca100847f3f82/svg.path-4.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/63/f9/56781c02bb69f96f0af1644aaabf065bea6cb0e67ffe2b3ca100847f3f82/svg.path-4.0.2.tar.gz
Summary  : SVG path objects and parser
Group    : Development/Tools
License  : MIT
Requires: svg.path-license = %{version}-%{release}
Requires: svg.path-python = %{version}-%{release}
Requires: svg.path-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : util-linux

%description
svg.path
========

svg.path is a collection of objects that implement the different path
commands in SVG, and a parser for SVG path definitions.


Usage
-----

There are four path segment objects, ``Line``, ``Arc``, ``CubicBezier`` and
``QuadraticBezier``.`There is also a ``Path`` object that acts as a
collection of the path segment objects.

All coordinate values for these classes are given as ``complex`` values,
where the ``.real`` part represents the X coordinate, and the ``.imag`` part
representes the Y coordinate::

    >>> from svg.path import Path, Line, Arc, CubicBezier, QuadraticBezier, Close

All of these objects have a ``.point()`` function which will return the
coordinates of a point on the path, where the point is given as a floating
point value where ``0.0`` is the start of the path and ``1.0`` is end end.

You can calculate the length of a Path or it's segments with the
``.length()`` function. For CubicBezier and Arc segments this is done by
geometric approximation and for this reason **may be very slow**. You can
make it faster by passing in an ``error`` option to the method. If you
don't pass in error, it defaults to ``1e-12``::

    >>> CubicBezier(300+100j, 100+100j, 200+200j, 200+300j).length(error=1e-5)
    297.2208145656899

CubicBezier and Arc also has a ``min_depth`` option that specifies the
minimum recursion depth. This is set to 5 by default, resulting in using a
minimum of 32 segments for the calculation. Setting it to 0 is a bad idea for
CubicBeziers, as they may become approximated to a straight line.

``Line.length()`` and ``QuadraticBezier.length()`` also takes these
parameters, but they are ignored.

CubicBezier and QuadraticBezier also has ``is_smooth_from(previous)``
methods, that check if the segment is a "smooth" segment compared to the
given segment.

There is also a ``parse_path()`` function that will take an SVG path definition
and return a ``Path`` object::

    >>> from svg.path import parse_path
    >>> parse_path('M 100 100 L 300 100')
    Path(Move(to=(100+100j)), Line(start=(100+100j), end=(300+100j)))


Classes
.......

These are the SVG path segment classes. See the `SVG specifications
<http://www.w3.org/TR/SVG/paths.html>`_ for more information on what each
parameter means.

* ``Line(start, end)``

* ``Arc(start, radius, rotation, arc, sweep, end)``

* ``QuadraticBezier(start, control, end)``

* ``CubicBezier(start, control1, control2, end)``

In addition to that, there is the ``Path`` class, which is instantiated
with a sequence of path segments:

* ``Path(*segments)``

The ``Path`` class is a mutable sequence, so it behaves like a list.
You can add to it and replace path segments etc::

    >>> path = Path(Line(100+100j,300+100j), Line(100+100j,300+100j))
    >>> path.append(QuadraticBezier(300+100j, 200+200j, 200+300j))
    >>> path[0] = Line(200+100j,300+100j)
    >>> del path[1]

The path object also has a ``d()`` method that will return the
SVG representation of the Path segments::

    >>> path.d()
    'M 200,100 L 300,100 Q 200,200 200,300'


Examples
........

This SVG path example draws a triangle::


    >>> path1 = parse_path('M 100 100 L 300 100 L 200 300 z')

You can format SVG paths in many different ways, all valid paths should be
accepted::

    >>> path2 = parse_path('M100,100L300,100L200,300z')

And these paths should be equal::

    >>> path1 == path2
    True

You can also build a path from objects::

    >>> path3 = Path(Line(100+100j,300+100j), Line(300+100j, 200+300j), Line(200+300j, 100+100j))

And it should again be equal to the first path::

    >>> path1 == path2
    True

Paths are mutable sequences, you can slice and append::

    >>> path1.append(QuadraticBezier(300+100j, 200+200j, 200+300j))
    >>> len(path1[2:]) == 3
    True

Note that there is no protection against you creating paths that are invalid.
You can for example have a Close command that doesn't end at the path start::

    >>> wrong = Path(Line(100+100j,200+100j), Close(200+300j, 0))


Future features
---------------

* Reversing paths. They should then reasonably be drawn "backwards" meaning each
  path segment also needs to be reversed.

* Mathematical transformations might make sense.

* Verifying that paths are correct, or protection against creating incorrect paths.


License
-------

This module is under a MIT License.

Contributors
============

Lennart Regebro <regebro@gmail.com>, Original Author

Justin Gruenberg implemented the Quadradic Bezier calculations and
provided suggestions and feedback about the d() function.

Michiel Schallig suggested calculating length by recursive straight-line
approximations, which enables you to choose between accuracy or speed.
Steve Schwarz added an error argument to make that choice an argument.

ClayJarCom speeded up `point()` calculations for paths.

Thanks also to bug fixers Martin R, abcjjy, Daniel Stender, MTician,
blokhin and jaraco, and thanks to tatarize for help with investigating
the subpath issues.

Changelog
=========


4.0.2 (2019-11-04)
------------------

- A solution for the setup.cfg [Alex Grönholm]


4.0.1 (2019-11-03)
------------------

- The pure setup.cfg config didn't work. All the tests pass fine,
  but when installing the package somewhere else, nothing gets installed.
  So I'm reverting that change for now.


4.0 (2019-11-02)
----------------

- Moved all the information from setup.py into setup.cfg.

- Added a Close() command which is different from a Line() command in
  no way at all, to simplify the handling of closepath commands and subpaths.

- Path()'s no longer have a `closed` attribute.

- Now fully supports the SVG 1.1 "F.6.2 Out-of-range parameters" list.

- Uses circular maths to calculate the length of circular arcs,
  more accurate and much faster.


3.1 (2019-10-25)
----------------

- The Move null command was not imported into ``__init__.py`` [blokhin]
- #41: Switched from ``pkg_resource``-style namespace
  package for ``svg`` to a `pkgutil style
  <https://packaging.python.org/guides/packaging-namespace-packages/#pkgutil-style-namespace-packages>`_
  namespace package.
- A faster ``point()`` implementation for paths. [ClayJarCom]
- Dropped support for Python 2.6 and Python 3.3.
- Added support for Python 3.7 and 3.8.


3.0 (2018-08-14)
----------------

- Dropped support for Python 3.1 and 3.2. It still works, but it may stop.
  Added support for Python 3.6. Dropped support for Jython, it's not
  supported by Travis, and hasn't seen  a release in over a year.

- #33: Move commands are now preserved when parsed.

- Subpaths are no longer merged even if they are joined.

- #30: Arcs where the endpoint is the same as the start point caused a crash.
  The SVG specs say that it instead should be the equavalent of skipping
  that section, which now is the case.


2.2 (2016-10-15)
----------------

- Don't add a line when closing a path if it's not needed.


2.1.1 (2016-02-28)
------------------

- #18: QuadraticBeziers could get a DivideByZero error under certain
  circumstances. [MTician]

- Accept an error parameter to Path.point() to be able to
  control error vs performance setting. [saschwarz]

- #25: Arc's could create a MathDomain error under certain circumstances.

- #17: Set last_command always.


2.0.1 (2015-10-17)
------------------

- #20: The doctext for the closed() setter was incorrect.

- #19: Fixed so tests didn't use relative paths. [danstender]


2.0 (2015-05-15)
----------------

- Nothing changed yet.


2.0b1 (2014-11-06)
------------------

- Added a Path.d() function to generate the Path's d attribute.

- Added is_smooth_from() on QubicBezier and QuadradicBezier.

- Path()'s now have a .closed property.

- Fixed the representation so it's parseable.

- The calculations for CubicBezier and Arc segments are now recursive,
  and will end when a specific accuracy has been achieved.
  This is somewhat faster for Arcs and somewhat slower for CubicBezier.
  However, you can now specify an accuracy, so if you want faster but
  looser calculations, you can have that.

- 't' segments (smooth, relative QuadraticBeziers) whose previous segment was
  not a QuadraticBezier would get an incorrect control point.


1.2 (2014-11-01)
----------------

- New Quadradic Bezier implementation. [Justin Gruenberg]

- Solved issue #6: Z close path behavior. [abcjjy]


1.1 (2013-10-19)
----------------

- Floats with negative exponents work again.

- New tokenizer that is around 20 times faster.


1.0 (2013-05-28)
----------------

- Solved issue #2: Paths with negative values and no spaces didn't work.
  [regebro]


1.0b1 (2013-02-03)
------------------

- Original release.

%package license
Summary: license components for the svg.path package.
Group: Default

%description license
license components for the svg.path package.


%package python
Summary: python components for the svg.path package.
Group: Default
Requires: svg.path-python3 = %{version}-%{release}

%description python
python components for the svg.path package.


%package python3
Summary: python3 components for the svg.path package.
Group: Default
Requires: python3-core
Provides: pypi(svg.path)

%description python3
python3 components for the svg.path package.


%prep
%setup -q -n svg.path-4.0.2
cd %{_builddir}/svg.path-4.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582914106
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/svg.path
cp %{_builddir}/svg.path-4.0.2/LICENSE.txt %{buildroot}/usr/share/package-licenses/svg.path/d14a2577da362843bb255e84ec3c2dd4bfd47f50
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/svg.path/d14a2577da362843bb255e84ec3c2dd4bfd47f50

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
