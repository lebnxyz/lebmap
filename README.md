# [leb](https://supposedly.github.io/leb)
An interactive map charting dialectal features of Lebanese Arabic. Based on the results of
[this survey](https://forms.gle/U4h1xtSJZ5nnv5Ku7) posted to /r/Lebanon on 8/13/19.

This project is a WIP. The end goal is to have an interactive map of Lebanon in the browser, complete with
clickable response locations and easily accessible statistical analysis. Timeline depends on my procrastination ;)

## Build info
I want to love [Parcel](https://parceljs.org), but it just isn't mature enough yet, as of release 1.12.3, to be reliable.
The issues at [parcel-bundler#501](https://github.com/parcel-bundler/parcel/issues/501),
[parcel-bundler#1294](https://github.com/parcel-bundler/parcel/issues/1294), and
[parcel-bundler#2262](https://github.com/parcel-bundler/parcel/issues/2262) slowly added to my mounting distaste, with the
third being the absolute last straw, so I switched to Webpack... everything about the build process is ickier as a result,
but I'll gladly (if reulctantly) take icky over broken.

So if you'd like to tinker with the project yourself, the following NPM scripts are relevant:

- `dev`: Build for development.
- `prod`: Build for production.
- `serve`: Serve whatever's in `docs/`, the output directory. (I can't currently get Webpack's dev server to work, so this is important.)
- `sdev`: `dev` -> `serve`.
- `sprod`: `prod` -> `serve.`

(But don't look too hard at the remaining scripts. Please. It's for your own good.)

Of note is my *patent* abuse of Pages' "build from `docs/`" feature, allowing for local debugging from the project
root without requiring maintenance of a separate `gh-pages` branch to deploy from. If it works...!
