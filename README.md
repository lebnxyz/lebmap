# [leb](https://lebnxyz.github.io/lebmap)
An interactive map charting dialectal features of Lebanese Arabic. Based on the results of
[this survey](https://forms.gle/U4h1xtSJZ5nnv5Ku7) posted to /r/Lebanon on 8/13/19.

This project is a WIP. The end goal is to have an interactive map of Lebanon in the browser, complete with
clickable response locations and easily accessible statistical analysis. Timeline depends on my procrastination ;)

## Build info
I really wanted to love [Parcel](https://parceljs.org), but (as of release 1.12.3) it just isn't mature enough yet to be reliable.
The issues at [parcel-bundler#501](https://github.com/parcel-bundler/parcel/issues/501),
[parcel-bundler#1294](https://github.com/parcel-bundler/parcel/issues/1294), and
[parcel-bundler#2262](https://github.com/parcel-bundler/parcel/issues/2262) slowly added to my mounting frustration, with the
third being the absolute last straw, so I switched to Webpack... and everything about the build process is a little bit ickier
as a result, but I'll gladly take icky over broken.

So if you'd like to tinker with the project yourself, the following four NPM scripts are relevant:

- `dev`: Serves a development build. Automatically opens in default browser.
- `prodserve`: Ditto, but serves a production build (just in case).
- `build`: Builds for production.
- `devbuild`: Bulids for development (just in case).

(And don't look at the remaining scripts. Please. It's for your own good.)

Of note is my *patent* abuse of Pages' "build from `docs/`" feature, allowing for local debugging from the project
root without requiring maintenance of a separate `gh-pages` branch to deploy from. If it works...!
