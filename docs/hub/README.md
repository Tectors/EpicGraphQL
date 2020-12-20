# Party Hub (Fortnite)
An documentation about the *Fortnite Party Hub* app.

## Kairos
Information about kairos.

## API
Past or new GraphQL url and methods.

| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

## Avatars
A list of avatars is located at [here](https://cdn2.unrealengine.com/Kairos/data/avatars.json), but it is very outdated but the app seems to still use it to this day.
The url for these characters is in this format, just replace CID with the id.
```
https://cdn2.unrealengine.com/Kairos/portraits/{CID}.png
```
There is a **preview** param, see below as how they show.

| SIZE | INFO |
| - | - |
| 1 | Small |
| 2 | Large |

## Gifs
The only known gifs, also some ones that I've found are the dancing emotes.

| EMOTE |
| - |
| [Dab](https://cdn2.unrealengine.com/Kairos/gifs/Dab_opt.gif) |
| [Wiggle](https://cdn2.unrealengine.com/Kairos/gifs/Wiggle_opt.gif) |
| [Llama Bell](https://cdn2.unrealengine.com/Kairos/gifs/LlamaBell_opt.gif) |

## Andriod Events
For some reason they send requests to the appsfyler website.

| URL |
| - |
| [FN_Live (6.0.1)](https://launches.appsflyer.com/api/v6.0/androidevent?app_id=com.epicgames.fortnite&buildnumber=6.0.1&channel=FN_Live) |

## Launch Images
There is currently one image behind the *PLAY* button, but if there is more, I'll add them.

| Image |
| - |
| [Chapter 1, Season 1 (background)](https://cdn2.unrealengine.com/Kairos/launcher/fortnite/fortnite_image.jpg)

## Sentry
They have a sentry endpoint that stores all the information about your device.

| URL |
| - |
| https://sentry.io/api/1776306/store/ |