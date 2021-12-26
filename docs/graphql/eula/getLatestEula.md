query EulaQuery($id: String!, $locale: String!, $accountId: String!) {
    Eula {
        getLatestEula(id: $id, locale: $locale) {
            key
            version
            revision
            title
            body
            locale
            createdTimestamp
            lastModifiedTimestamp
            agentUserName
            status
            custom
            accepted
        }
    }
}
