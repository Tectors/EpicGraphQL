# BlogQuery

[This is gotten from Terbau's gist, parsed to look good, check him out!](https://gist.github.com/Terbau/f36990a1d608f65645206835e708d488)

## Request
| URL | METHOD |
| - | - |
| https://graphql.epicgames.com/graphql | POST |

## Query
```graphql
query BlogQuery($locale: String!, $rootPageSlug: String!, $category: String!, $postsPerPage: Int!, $offset: Int!, $slug: String!) {
    Blog {
        getPosts(locale: $locale, rootPageSlug: $rootPageSlug, category: $category, postsPerPage: $postsPerPage, offset: $offset) {
            articlesToLoad
            blogList {
                _id
                _script
                _type
                author
                category
                title
                content
                short_
                featured
                trending
                date
                image
                shareImage
                shareDescription
                trendingImage
                link
                externalLink
                locale
                slug
                urlPattern
                url
                nextSlug
                prevSlug
                noTopImage
                sticky
                pageMapping
            }
            blogTotal
            incrementCount
            postCount
            categoryTotals {
                name
                count
            }
            _meta
            config {
                hideAuthor
                hideCategoryLink
                blogList {
                    _id
                    _script
                    _type
                    author
                    category
                    title
                    content
                    short_
                    featured
                    trending
                    date
                    image
                    shareImage
                    shareDescription
                    trendingImage
                    link
                    externalLink
                    locale
                    slug
                    urlPattern
                    url
                    nextSlug
                    prevSlug
                    noTopImage
                    sticky
                    pageMapping
                }
                blogTotal
                shareConfigs {
                    type
                }
                shareOptions {
                    name
                    enabled
                }
                useTitleCase
            }
        }
        getPost(locale: $locale, slug: $slug, rootPageSlug: $rootPageSlug) {
            _id
            _script
            _type
            author
            category
            title
            content
            short_
            featured
            trending
            date
            image
            shareImage
            shareDescription
            trendingImage
            link
            externalLink
            locale
            slug
            urlPattern
            url
            nextSlug
            prevSlug
            noTopImage
            sticky
            pageMapping
        }
    }
}
```

## Variables
```json
{
    "locale": "",
    "rootPageSlug": "",
    "category": "",
    "postsPerPage": 0,
    "offset": 0,
    "slug": ""
}
```