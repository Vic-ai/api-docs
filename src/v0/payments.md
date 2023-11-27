# Payments

## List Payment Batches

```
GET /v0/paymentBatches
```

[Open API](../vic.api.v0.html#/Payments/listPaymentBatches)

List all of the payment batches in the system.

All payments and credits are returned in these calls. Special attention should
be paid attention to the `status`, `rejectedAt`, `voidedAt`, and `approvedAt`.

### Example

```bash
curl --location --request GET 'https://api.us.dev.vic.ai/v0/paymentBatches' \
    --header 'Accept: application/json' \
    --header 'Authorization: Bearer <Bearer Token>'
```

```json
[
  {
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
      {
        "id": "091f257a-9b6e-4797-bcb6-ccd36dda260f",
        "amount": "20.00",
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
]
```

## Get Payment Batch

```
GET /v0/paymentBatches/{id}
```

[Open API](../vic.api.v0.html#/Payments/getPaymentBatch)

All payments and credits are returned in these calls. Special attention should
be paid attention to the `status`, `rejectedAt`, `voidedAt`, and `approvedAt`.

### Example

```bash
curl --location --request GET 'https://api.us.dev.vic.ai/v0/paymentBatches/1f9c36dc-4be4-488b-bead-b3f73e0313c9' \
    --header 'Accept: application/json' \
    --header 'Authorization: Bearer <Bearer Token>'
```

```json
{
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
    {
      "id": "091f257a-9b6e-4797-bcb6-ccd36dda260f",
      "amount": "20.00",
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
```
## Webhook Events

See [webhooks](./webhooks.md#payment-batch-processed) for more information.
