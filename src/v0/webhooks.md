# Webhooks

## Event

The newer webhook endpoints will be sent to the `/events` path.

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

## Payment Batch Processed

This event is emitted from the Vic system when a batch of payments has been sent
to the payment processor and a successful response has been obtained. For more
information about the structure of what is in the `data` envelope, see
[the payments](./payments.md) documentation.

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
      // credit object
    ]
  }
}
```
