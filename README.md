# [leb](https://supposedly.github.io/leb)
An interactive map charting dialectal features of Lebanese Arabic. Based on the results of
[this survey](https://forms.gle/U4h1xtSJZ5nnv5Ku7) posted to /r/Lebanon on 8/13/19.

This project is a WIP still in the early stages of its "actually finish the thing" phase. The end goal is to have
an interactive map of Lebanon in the browser, complete with clickable response locations and easily accessible
statistical analysis. Hopefully, I can figure out d3.js in a timely fashion :)

## Build info
I use [Parcel](https://parceljs.org/) for bundling, and the site is run client-side via GitHub Pages. If you'd like
to follow the same process and build the project yourself, clone and run `npm install` in the directory root, then
run `parcel build index.html --out-dir docs/ --public-url ./`.

And don't look at my NPM scripts. Please. It's for your own good.

Of note is my *patent* abuse of Pages' "build from `docs/`" feature, allowing for local debugging from the project
root without requiring maintenance of a separate `gh-pages` branch to deploy from. If it works...!
