# Party Hub (Fortnite)
An documentation about the *Fortnite Party Hub* app.

## Assets
A lot of the assets are loacted below
| DIRECTORY |
| - |
| res\drawable-xxxhdpi |
| res\drawable-xxhdpi |
| res\drawable-xhdpi |
| res\drawable-ldrtl-xxxhdpi |
| res\drawable-ldrtl-xxhdpi |
| res\drawable-ldrtl-xhdpi |
| res\drawable-ldrtl-mdpi |
| res\drawable-ldrtl-hdpi |
| res\drawable-hdpi |

## Trusted Subdomains
These subdomains may also include more subdomains that are also trusted no mather what.

| SUBDOMAIN |
| - |
| ol.epicgames.com |

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

## ID CODES
Here's some codes that represent the platform as.
| NAME |
| - |
| FortniteMobileAndroid |

## Gifs
The only known gifs, also some ones that I've found are the dancing emotes.

| EMOTE |
| - |
| [Dab](https://cdn2.unrealengine.com/Kairos/gifs/Dab_opt.gif) |
| [Wiggle](https://cdn2.unrealengine.com/Kairos/gifs/Wiggle_opt.gif) |
| [Llama Bell](https://cdn2.unrealengine.com/Kairos/gifs/LlamaBell_opt.gif) |

We actually created a bunch of gifs our selfs, check below. (Some of these are helped/created by [@InTheShadeYT](https://twitter.com/InTheShadeYT))

| EMOTE |
| - |
| [Boom Box](https://github.com/Tectors/EpicGraphQL/blob/main/docs/hub/gifs/BoomBox.gif) |
| [Dance Moves](https://github.com/Tectors/EpicGraphQL/blob/main/docs/hub/gifs/DanceMoves.gif) |
| [Deep End](https://github.com/Tectors/EpicGraphQL/blob/main/docs/hub/gifs/DeepEnd.gif) |
| [Floss](https://github.com/Tectors/EpicGraphQL/blob/main/docs/hub/gifs/Floss.gif) |
| [Tidy](https://github.com/Tectors/EpicGraphQL/blob/main/docs/hub/gifs/Tidy.gif) |
| [True Heart](https://github.com/Tectors/EpicGraphQL/blob/main/docs/hub/gifs/TrueHeart.gif) |
| [Wizard](https://github.com/Tectors/EpicGraphQL/blob/main/docs/hub/gifs/Wizard.gif) |
| [Smooth Moves](https://github.com/Tectors/EpicGraphQL/blob/main/docs/hub/gifs/SmoothMoves.gif) |
| [Victory Von Doom](https://github.com/Tectors/EpicGraphQL/blob/main/docs/hub/gifs/VictoryVonDoom.gif) |
| [Scenario](https://github.com/Tectors/EpicGraphQL/blob/main/docs/hub/gifs/Scenario.gif) |
| [Planetary Vibe](https://github.com/Tectors/EpicGraphQL/blob/main/docs/hub/gifs/PlanetaryVibe.gif) |

## App Identifiers
This list will be updated if there is any more.
| IDENTIFIER |
| - |
| com.epicgames.fortnite |

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
| https://sentry.io/api/1776306/store |

The data they store is below.

| NAME | PROPERTY NAME |
| - | - |
| Arch | arch |
| Battery Level | contexts.device.battery_level |
| Brand Of Phone | contexts.device.brand |
| Is Charging | contexts.device.charging |
| Amount Of External Free Storage | contexts.device.external_free_storage |
| Amount Of External Storage Left | contexts.device.external_storage_size |
| Brand Version | contexts.device.family |
| Free Memory Amount | contexts.device.free_memory |
| Free Storage Amount | contexts.device.free_storage |
| Is Low Memory | contexts.device.low_memory |
| Manufacturer | contexts.device.manufacturer |
| Memory Size | contexts.device.memory_size |
| Model Of Phone | contexts.device.model |
| Model ID Of Phone | contexts.device.model_id |
| Online | contexts.device.online |
| Orientation | contexts.device.orientation |
| Screen Density | contexts.device.screen_density |
| Screen DPI | contexts.device.screen_dpi |
| Screen Resolution | contexts.device.screen_resolution |
| Simulator | contexts.device.simulator |
| Storage Size | contexts.device.storage_size |
| Build | contexts.os.build |
| Kernel Version | contexts.os.kernel_version |
| Name Of OS | contexts.os.name |
| Rooted | contexts.os.rooted |
| Version | contexts.os.version |

## Supported Devices
Here is a list of supported devices you can use partyhub on.
| OS | DEVICE |
| - | - |
| android | Razer Phone 2 |
| android | Razer Phone |
| android | Essential PH-1 |
| android | Asus V |
| android | Asus 5Z |
| android | Asus Zenfone 4 Pro |
| android | Asus ROG Phone |
| android | OnePlus 6 |
| android | OnePlus 5T |
| android | OnePlus 5 |
| android | Nokia 8 |
| android | LG V30+ |
| android | LG V30 |
| android | LG V20 |
| android | LG ThinQ |
| android | LG G7 |
| android | LG G6 |
| android | LG G5 |
| android | Honor 20 |
| android | Honor View 20 |
| android | Honor Play |
| android | Honor 10 |
| android | Huawei V10 |
| android | Huawei P20 Pro |
| android | Huawei P20h |
| android | Huawei Nova 3 |
| android | Huawei Mate RS |
| android | Huawei Mate 10 Pro |
| android | Huawei Mate 10 |
| android | Google Pixel 2 XL |
| android | Google Pixel 2 |
| android | Google Pixel XL |
| android | Google Pixel |
| android | Samsung Tab S4 |
| android | Samsung Tab S3 |
| android | Samsung Note 9 |
| android | Samsung Note 8 |
| android | Samsung Galaxy S9+ |
| android | Samsung Galaxy S9 |
| android | Samsung Galaxy S8+ |
| android | Samsung Galaxy S8 |
| android | Samsung Galaxy S7 Edge |
| android | Samsung Galaxy S7 |

## Modules
Here's some modules they use. (gotten from the sentry request)

*The main package name is com.epicgames.fortnite*

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

## Permissions
These are the permissions that the app uses.
| TYPE | PERMISSION |
| - | - |
| android | android.permission.INTERNET |
| android | android.permission.ACCESS_NETWORK_STATE |
| android | android.permission.WAKE_LOCK |
| com.android | com.android.vending.CHECK_LICENSE |
| android | android.permission.ACCESS_WIFI_STATE |
| android | android.permission.RECEIVE_BOOT_COMPLETED |
| android | android.permission.MODIFY_AUDIO_SETTINGS |
| android | android.permission.VIBRATE |
| com.android | com.android.vending.BILLING |
| android | android.permission.BLUETOOTH |
| android | android.permission.FOREGROUND_SERVICE |
| com.samsung | com.samsung.android.iap.permission.BILLING |
| android | android.permission.GET_ACCOUNTS |
| com.google | com.google.android.c2dm.permission.RECEIVE |
| com.epicgames | com.epicgames.fortnite.permission.C2D_MESSAGE |
| android | android.permission.REQUEST_INSTALL_PACKAGES |
| android | android.permission.DOWNLOAD_WITHOUT_NOTIFICATION |
| android | android.permission.RECORD_AUDIO |