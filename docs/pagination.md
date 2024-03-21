The Vic.ai API leverages cursor-based pagination for traversing through data.

To fetch the next page of information, include the `cursor` parameter to the request. This value can be obtained from the `X-next` field in a previous response. 

Example:

```bash
curl https://api.us.vic.ai/v0/accounts?cursor=foobar \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
```