# Party Hub (Fortnite)
An documentation about the *Fortnite Party Hub* app.

## API
Past or new GraphQL url and methods.

| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/partyhub/graphql | POST |

[Check the operations folder to get a list of ways to use this post request.](https://github.com/Tectors/EpicGraphql/blob/main/docs/hub/operations)

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

## Modules
Here's some modules they use. (gotten from the sentry request)

*The main package name is *com.epicgames.fortnite* *

| MODULE | FILENAME | FUNCTION |
| - | - | - |
| com.google.protobuf | null | null | null |
| android.os.HandlerThread | HandlerThread.java | run |
| android.os.Looper | Looper.java | loop |
| android.os.Handler | Handler.java | dispatchMessage |
| android.os.Handler | Handler.java | handleCallback |
| com.epicgames.kairos.core.tasks.TaskOperationQueue$performNextSynchronousTask$2 | null | run |
| com.epicgames.kairos.core.tasks.TaskOperationQueue$performNextSynchronousTask$2 | null | ᫖ࡱ᫋ |
| com.epicgames.kairos.core.tasks.BaseTask | null | start |
| com.epicgames.kairos.core.tasks.BaseTask | null | ᫅ࡦ᫋ |
| com.epicgames.kairos.utils.DataStoreTaskRunner | null | run |
| com.epicgames.kairos.utils.DataStoreTaskRunner | null | ᫋᫂᫚ |
| com.epicgames.kairos.RootNavigationControllerDelegate$DefaultImpls | null | safeWrite |
| com.epicgames.kairos.RootNavigationControllerDelegate$DefaultImpls | null | ࡳ᫕ |
| com.epicgames.kairos.utils.DataStoreTaskRunner$run$$inlined$use$lambda$1 | null | invoke |
| com.epicgames.kairos.utils.DataStoreTaskRunner$run$$inlined$use$lambda$1 | null | ᫙᫂᫚ |
| com.epicgames.kairos.core.transforms.eos.PresenceTransform$handleEOSEvent$1 | null | invoke |
| com.epicgames.kairos.core.transforms.eos.PresenceTransform$handleEOSEvent$1 | null | ᫅ࡳ᫋ |
| com.epicgames.kairos.RootNavigationControllerDelegate$DefaultImpls | null | access$getProperties |
| com.epicgames.kairos.RootNavigationControllerDelegate$DefaultImpls | null | ࡳ᫕ |
| com.epicgames.kairos.RootNavigationControllerDelegate$DefaultImpls | null | parse |
| com.epicgames.kairos.RootNavigationControllerDelegate$DefaultImpls | null | ࡳ᫕ |
| com.google.protobuf.util.JsonFormat$Parser | null | merge |
| com.google.protobuf.util.JsonFormat$Parser | null | ࡳ࡫᫊ |
| com.google.protobuf.util.JsonFormat$ParserImpl | null | merge |
| com.google.protobuf.util.JsonFormat$ParserImpl | null | ᫀ࡫᫊ |
| com.google.protobuf.util.JsonFormat$ParserImpl | null | merge |
| com.google.protobuf.util.JsonFormat$ParserImpl | null | ᫀ࡫᫊ |
| com.google.protobuf.util.JsonFormat$ParserImpl | null | mergeMessage |
| com.google.protobuf.util.JsonFormat$ParserImpl | null | ᫀ࡫᫊ |
| com.epicgames.kairos.core.models.constants.AutoUpdateDownloadOption$Companion | null | stringToEngineModelPlatform |
| com.epicgames.kairos.core.models.constants.AutoUpdateDownloadOption$Companion | null | ࡪࡠ᫋ |
| com.epicgames.kairos.utils.KLog | null | a |
| com.epicgames.kairos.utils.KLog | null | ࡲ᫂᫚ |
| com.epicgames.kairos.utils.KLog | null | e |
| com.epicgames.kairos.utils.KLog | null | ࡲ᫂᫚ |
| com.epicgames.kairos.utils.KLog | null | log$4414f3 |
| com.epicgames.kairos.utils.KLog | null | ࡨ᫂᫚ |