To initiate the authentication process, send a POST request to `/v0/token` with the payload as shown in the example below:

```json
{
    "client_id": "VIC_CLIENT_ID",
    "client_secret": "VIC_CLIENT_SECRET"
}
```

Here is an example of how to do this:

```bash
curl -X POST https://api.us.vic.ai/v0/token \
    -H "Content-Type: application/json" \
    -d '{"client_id": "VIC_CLIENT_ID", "client_secret": "VIC_CLIENT_SECRET"}'
```

Upon providing a valid client ID and client secret, you should receive a response similar to the following:

```json
{
    "access_token": "YOUR_ACCESS_TOKEN",
    "token_type": "Bearer",
    "expires_in": 3600
}
```

For subsequent calls, use the value in `access_token` in the `Authorization` field. 

Here is an example:

```bash
curl https://api.us.vic.ai/v0/healthCheck \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

The response should resemble the following:

```bash
{"company":"Your Company Name","status":"PASS","version":"0.19.0"}
```
