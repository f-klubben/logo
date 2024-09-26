# Manifest logos

This is the Fklub logo optimized for use in websites and webapps. To add the logo to your website, you must add the following to the `<head>` element in your HTML:

```html
<link rel="icon" sizes="any" type="image/svg+xml" href="/link/to/logo.svg">
<link rel="manifest" href="/link/to/manifest.json">
```

You can also add other fields to [manifest.json](manifest.json), such as `name` and `short_name`. Check out this article for more info: [https://developer.mozilla.org/en-US/docs/Web/Manifest](https://developer.mozilla.org/en-US/docs/Web/Manifest).

## Technical details

The `<link rel="icon"..` element defines the icon that is shown next to the page's title in the navigation bar.

The [manifest.json](manifest.json) file provides the browser with different versions of the logo that are useful in different situations. The logos are all based on [the SVG logo](../logo.svg), with some minor changes:

| Name | Display | Purpose | Changes from the default logo |
|---|---|---|---|
| [logo.svg](logo.svg) | ![logo.svg](logo.svg) | Default logo, most commonly used in the navigation bar.  | Enables support for dark mode, allowing the browser to set the foreground color to white when it is rendered on a dark background. |
| [logo-monochrome.svg](logo-monochrome.svg) | ![logo-monochrome.svg](logo-monochrome.svg) | Used when the browser wants to control the appearance of the logo. Only the shadow of the image is used, then the browser paints the shadow in whatever color it wants. | Hard coded to use a black foreground color on a transparent background. |
| [logo-maskable.svg](logo-maskable.svg) | ![logo-maskable.svg](logo-maskable.svg) | Used when the logo is rendered over an unknown/busy background. The browser can cut the edges of the logo into any shape it wants, e.g. a circle. | Enables support for dark mode, sets a solid background color that is white or dark depending on dark mode, pads the image to make sure the logo is not cut into. |

## Legacy support

There are lots of browsers out there that do not support SVG icons, and thus won't work with this setup. Unfortunately, it is almost impossible to support all of them and their weird quirks, and it is even more impossible to do that while also providing a nice and modern experience in browsers that do support SVG.

My recommendation is: don't open this Pandora's box. There is no need to ruin your day, and your users probably won't even notice if the logo is missing in their preferred browser.

If you are still here and you have decied that you want to suffer, be aware that whatever seems to work in your browser might not work in the same browser on a different operating system. You also cannot expect that forks of your browser will support it. To properly test this, you need to try it on at least 20 different browsers, all on both Windows, MacOs, and a few different Linux distros. Then remember to go back and redo the testing every 6 months because browses change their logic all the time. Good luck!
