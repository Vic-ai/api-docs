## Subscriptions

You can subscribe to all events in the Vic API system or a subset of the
[events](#events). At the moment, each company may only have one subscription
specified.

### Create and Update Subscription

To create or update a subscription with the Vic API, you can pass the following.

```bash
curl --request PUT \
  --url http://api.us.vic.ai/v0/subscription \
  --header 'Authorization: Bearer MYBEARERTOKEN' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --data '{
  "callbackUrl": "https://yourCallbackUrl",
  "accessToken": "unique-token-per-client",
  "expiresAt": "2024-01-01T00:00:00Z"
}'
```

If you wish to only subscribe to specific events you may pass an array of event
names.

```bash
curl --request PUT \
  --url http://api.us.vic.ai/v0/subscription \
  --header 'Authorization: Bearer MYBEARERTOKEN' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --data '{
  "callbackUrl": "https://yourCallbackUrl",
  "accessToken": "unique-token-per-client",
  "expiresAt": "2024-01-01T00:00:00Z",
  "events": ["payment_batch_processed"]
}'
```

If you need to update your subscription to receive all events after trimming it
down, you may pass `"events":["all"]`. When passing `all`, it must be set by
itself.

```bash
curl --request PUT \
  --url http://api.us.vic.ai/v0/subscription \
  --header 'Authorization: Bearer MYBEARERTOKEN' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --data '{
  "callbackUrl": "https://yourCallbackUrl",
  "accessToken": "unique-token-per-client",
  "expiresAt": "2024-01-01T00:00:00Z",
  "events": ["all"]
}'
```

### Unsubscribe

You can delete a subscription by doing the following. Once the subscription is
deleted, events will stop going to the callback url.

```bash
curl --request DELETE \
  --url http://api.us.vic.ai/v0/subscription \
  --header 'Authorization: Bearer MYBEARERTOKEN'
```

## Events

These are the `V1` events you can subscribe to. These will be sent as a `POST`
to `https://yourCallbackUrl/events`.

* `all` - This is a special form, that specifies that you want all events sent
  to your webhook.
* [`payment_batch_processed`](#payment-batch-processed)

The following `V0` events may be specified. They will be sent to the original
callback paths where the event name was in the path.

* `vendorNew` - `POST` `https://yourCallbackUrl/vendorNew`
* `invoicePost` - `POST` `https://yourCallbackUrl/invoicePost`
* `invoiceTransfer` - `POST` `https://yourCallbackUrl/invoiceTransfer`
* `syncRequest` - `POST` `https://yourCallbackUrl/syncRequest`

### Event Details

The newer webhook endpoints will be sent to `https://yourCallbackUrl/events`.
The receiver is expected to handle everything asynchronously via this method. We
do not parse parse the response body and will ignore it.

* All `2XX` responses will be treated as successful.
* `401` and `403` responses will be treated as failures and be retried with an
  exponential backoff. Once the retries have been exhausted, the event is
  discarded.
* All other `4XX` responses will be treated as successful. If something is to be
  rejected, you will need to make the appropriate calls to the Vic API to
  complete the asynchronous handshake. Example: confirming or rejecting an
  invoice post.
* All `5XX` responses will be treated as a failure and will be retried with an
  exponential backoff. Once the retries have been exhausted, the event is
  discarded.
* All events retried will be reattempted at least 5 times.

> **NOTE**: The integrating system has 15 seconds to respond. After the time has
> passed it will be considered a failure, and a retry will be sent for events
> going to `https://yourCallbackUrl/events`.

The general structure of the webhook event will be as follows.

```json
{
  "event": "the_event_name",
  "data": {
    "id": "123",
    "something": "value"
  }
}
```

There will be a top level field `event` that describes what the type of event
is. There will also be a `data` envelope that will contain the data for the
event.

### Payment Batch Processed

This event is emitted from the Vic system when a batch of payments has been sent
to the payment processor and a successful response has been obtained. The
payload for this event matches almost exactly what you will receive in the
`getPaymentBatch` operation.

Only approved credits and payments will be emitted with the event. Voided and
rejected payments will not be sent. If you need these values, you should call
`getPaymentBatch` in order to fetch them.

Here is an example of an $200 invoice being paid in full with a $20 credit note
being applied. This will bring the total batch payment to $180. The credit note
applied is not subtracted from the payment in this breakdown because ERPs
typically need entries of the payment being applied and the credit note being
used in conjunction with that credit note.

```json
{
  "event": "payment_batch_processed",
  "data": {
    "id": "f1c2384f-57d8-41fe-afa6-17caf62b2a3f",
    "name": "Batch 2023-10-01 001",
    "processedAt": "2023-10-01T19:12:00Z",
    "approvedAt": "2023-10-01T19:12:00Z",
    "rejectedAt": null,
    "voidedAt": null,
    "status": "approved",
    "companyId": "123",
    "payments": [
      {
        "id": "edb3a624-9f12-4cd8-adb8-4d9a5ec0b48b",
        "amount": "200.00",
        "settlementAmount": "200.00",
        "settlementCurrencyId": "USD",
        "exchangeRate": "1.0",
        "discountAmount": "0.00",
        "currencyId": "USD",
        "status": "approved",
        "voidedAt": null,
        "rejectedAt": null,
        "approvedAt": "2023-10-01T19:12:00Z",
        "fundedAt": null,
        "costAccount": {
          "internalId": "1",
          "externalId": "cost-account-id-in-erp",
        },
        "invoice": {
          "internalId": "876",
          "externalId": "invoice-id-in-erp"
        },
        "vendor": {
          "internalId": "409",
          "externalId": "vendor-id-in-erp"
        },
      }
    ],
    "credits": [
      {
        "id": "091f257a-9b6e-4797-bcb6-ccd36dda260f",
        "amount": "20.00",
        "settlementAmount": "20.00",
        "settlementCurrencyId": "USD",
        "exchangeRate": "1.0",
        "discountAmount": "0.00",
        "currencyId": "USD",
        "status": "approved",
        "voidedAt": null,
        "rejectedAt": null,
        "approvedAt": "2023-10-01T19:12:00Z",
        "fundedAt": null,
        "invoice": {
          "internalId": "900",
          "externalId": "credit-note-id-in-erp"
        },
        "vendor": {
          "internalId": "409",
          "externalId": "vendor-id-in-erp"
        },
      }
    ]
  }
}
```
