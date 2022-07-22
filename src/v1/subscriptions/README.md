# Subscriptions

Subscriptions are how Vic is able to notify third party integrations about
events and updates within the system.

The functionality of subscriptions in the V1 system are very different than how
they operate in the V0 system.

All subscriptions must have a `callback_url`, `access_token`, `expires_at`, and
a `version` specified.

## Callback Consumption

The callback url specified is where all events will be sent to via an HTTP
`POST` call. The Vic system does not care about the response from the
`callback_url` specified. The only response the Vic system cares about is the
status code not being a `5XX`.

## Callback Retries

The callback will be attempted 5 times if the response from the callback system
if the response status code is a `5XX`. We will back off exponentially when this
occurs.

## Callback Event Ordering

The callback events have no guaranteed ordering at the moment.

## Callback Payload Shape

The following is an example of a callback event that can be received.

```json
{
  "event": "purchase_order_updated",
  "occurred_at": "2022-06-01T12:00:00Z",
  "data": {
    "external_id": null,
    "internal_id": "51721bc8-6263-464b-babd-ba754f7fd94b",
    "internal_updated_at": "2022-05-02T12:34:56Z",
    "issued_on": "2022-05-01",
    "po_number": "1234567890",
    "deliver_on": "2022-06-01",
    "amount": "100.00",
    "currency_id": "USD",
    "status": "open",
    "description": "The purchase order description",
    "items": [
        {
          "internal_id": "e6097517-548d-448f-a7f5-bfb656be228f",
          "product_number": "theproductnumber",
          "product_description": "The product description",
          "unit_of_measure": "kg",
          "quantity": "12.3",
          "unit_amount": "1.99",
          "line_item_total": "24.48",
          "dimensions": [
            {"internal_id": "12345", "external_id": "abc123"}
          ]
        }
    ]
  }
}
```
