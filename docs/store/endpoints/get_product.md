# Get Product
Get a product from the epic games store.

*This is used on the main Epic Games store page, and possibly also used inside of the launcher.*

## Request
| URL | Method |
| - | - |
| https://store-content-ipv4.ak.epicgames.com/api/en-US/content/products/:name | `GET` |

## Query
- `name`: The name of the game

## Response Information
It gives you information about the game such as the namespace (eg. fn for fortnite), requirements (eg. Windows 10 64-bit), the image of the game, main logo, and more.