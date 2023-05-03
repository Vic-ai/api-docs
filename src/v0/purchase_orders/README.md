# Purchase Orders

## Create Purchase Order

```
POST /v0/purchaseOrders
```

[Open API][createPurchaseOrder]

Creates a purchase order in the Vic.ai system.

You are responsible for setting the `amount` on the purchase order which is the
summation of all the purchase order line items.

Once the purchase order has been created and all manipulations are finished, you
must call [Process Purchase Order](#process-purchase-order).

### Example

```bash
curl --location --request POST 'https://api.us.dev.vic.ai/v0/purchaseOrders' \
    --header 'Content-Type: application/json' \
    --header 'Accept: application/json' \
    --header 'Authorization: Bearer <Bearer Token>' \
    --data-raw '{
      "amount": "1.00",
      "createdOn": "2022-06-01",
      "deliverOn": "2022-07-01",
      "issuedOn": "2022-06-01",
      "currencyId": "USD",
      "poNumber": "abc123",
      "requestor": "Bob From Marketing",
      "description": "A purchase order",
      "externalId": "po-1",
      "vendor": {
          "externalId": "the-vendor-external-id"
      },
      "lineItems": [
          {
              "productNumber": "11111",
              "productDescription": "Some widget",
              "unitOfMeasure": null,
              "quantityReceived": "13.0",
              "quantityRequested": "13.0",
              "unitAmount": "3.50",
              "lineItemTotal": "45.50",
              "lineNumber": 0,
              "dimensions": [
                  {"externalId": "dimenstion-external-id"}
              ]
          },
          {
              "productNumber": "22222",
              "productDescription": "A different widget",
              "unitOfMeasure": null,
              "quantityReceived": "1.0",
              "quantityRequested": "1.0",
              "unitAmount": "3.50",
              "lineItemTotal": "3.50",
              "lineNumber": 1,
              "dimensions": [
                  {"externalId": "dimenstion-external-id"}
              ]
          }
      ]
    }'
```

## Get Purchase Order

```
GET /v0/purchaseOrders/{purchaseOrderId}
```

[Open API][getPurchaseOrder]

Fetch a purchase order in the Vic.ai system.

Only the `internalId` of the purchase order is supported.

### Example

```bash
curl --location --request GET 'https://api.us.dev.vic.ai/v0/purchaseOrders/ffb64be6-5e80-47d1-90bd-316663c52c8' \
    --header 'Accept: application/json' \
    --header 'Authorization: Bearer <Bearer Token>'
```

## Delete Purchase Order

```
DELETE /v0/purchaseOrders/{purchaseOrderId}
```

[Open API][deletePurchaseOrder]

Deletes a purchase order from the Vic.ai system.

Only the `internalId` of the purchase order is supported.

### Example

```bash
curl --location --request DELETE 'https://api.us.dev.vic.ai/v0/purchaseOrders/ffb64be6-5e80-47d1-90bd-316663c52c8' \
    --header 'Accept: application/json' \
    --header 'Authorization: Bearer <Bearer Token>'
```

## Update Purchase Order

```
PUT /v0/purchaseOrders/{purchaseOrderId}
```

[Open API][updatePurchaseOrder]

Updates a purchase order.

To alter a purchase order's set of line items you will need to call one of the
following operations.

* [Create Purchase Order Item](#create-purchase-order-item)
* [Update Purchase Order Item](#update-purchase-order-item)
* [Delete Purchase Order Item](#delete-purchase-order-item)

Once you are finished manipulating the purchase order you will need to call
[Process Purchase Order](#process-purchase-order) to kick off the matching
process based on the updated information.

### Example

```bash
curl --location --request PUT 'https://api.us.dev.vic.ai/v0/purchaseOrders/56dae9cc-8726-4082-9622-1111d1a61da5' \
    --header 'Content-Type: application/json' \
    --header 'Accept: application/json' \
    --header 'Authorization: Bearer <Bearer Token>' \
    --data-raw '{
      "amount": "100.00",
      "createdOn": "2022-06-01",
      "deliverOn": "2022-07-01",
      "issuedOn": "2022-06-01",
      "currencyId": "USD",
      "poNumber": "abc123",
      "requestor": "Bob From Marketing",
      "description": "A purchase order",
      "externalId": "po-1",
      "vendor": {
          "externalId": "the-vendor-external-id"
      }
    }'
```

## Process Purchase Order

```
POST /v0/purchaseOrders/{purchaseOrderId}/process
```

[Open API][processPurchaseOrder]

Starts the matching process for the purchase order.

Only the `internalId` of the purchase order is supported.

### Example

```bash
curl --location --request POST 'https://api.us.dev.vic.ai/v0/purchaseOrders/ffb64be6-5e80-47d1-90bd-316663c52c8/process' \
    --header 'Accept: application/json' \
    --header 'Authorization: Bearer <Bearer Token>'
```

## Create Purchase Order Line Item

```
POST /v0/purchaseOrderLineItems
```

[Open API][createPurchaseOrderLineItem]

Create a purchase order's line item.

Caution should be taken when creating a new line item in a purchase order. Each
purchase order line item must have a line number and it must be unique among the
other line items. It should be a non negative value.

After creating the new purchase order line item, you **must** update the the
purchase order's `amount` field. This should be done once you are finished
manipulating all of the line items.

Once you are finished manipulating the purchase order you will need to call
[Process Purchase Order](#process-purchase-order) to kick off the matching
process based on the updated information.

### Example

```bash
curl --location --request POST 'https://api.us.dev.vic.ai/v0/purchaseOrdersLineItems' \
    --header 'Content-Type: application/json' \
    --header 'Accept: application/json' \
    --header 'Authorization: Bearer <Bearer Token>' \
    --data-raw '{
      "purchaseOrderId": "0dfeb8db-7eae-4207-9557-b365062d5877",
      "productNumber": "11111",
      "productDescription": "Some widget",
      "unitOfMeasure": null,
      "quantityReceived": "13.0",
      "unitAmount": "3.50",
      "lineItemTotal": "45.50",
      "lineNumber": 0,
      "dimensions": [
          {"externalId": "dimenstion-external-id"}
      ]
    }'
```

## Update Purchase Order Line Item

```
PUT /v0/purchaseOrderLineItems/{purchaseOrderLineItemId}
```

[Open API][updatePurchaseOrderLineItem]

Updates a purchase order's line item.

If there are existing matches made to an invoice that has been posted, you will
not be able to update the purchase order line item.

If you update `lineItemTotal` you **must** update the purchase order's `amount`
field which is the summation of all the line items. This should be done once you
are finished manipulating all of the line items.

Once you are finished manipulating the purchase order you will need to call
[Process Purchase Order](#process-purchase-order) to kick off the matching
process based on the updated information.

### Example

```bash
curl --location --request PUT 'https://api.us.dev.vic.ai/v0/purchaseOrdersLineItems/9b4810da-5959-47b6-91db-4b7d76a67232' \
    --header 'Content-Type: application/json' \
    --header 'Accept: application/json' \
    --header 'Authorization: Bearer <Bearer Token>' \
    --data-raw '{
      "productNumber": "11111-r12",
      "productDescription": "Change widget description",
      "unitOfMeasure": null,
      "quantityReceived": "20.0",
      "quantityRequested": "13.0",
      "unitAmount": "3.50",
      "lineItemTotal": "70.00",
      "lineNumber": 0,
      "dimensions": [
          {"externalId": "dimenstion-external-id"}
      ]
    }'
```


## Delete Purchase Order Line Item

```
DELETE /v0/purchaseOrderLineItems/{purchaseOrderLineItemId}
```

[Open API][deletePurchaseOrderLineItem]

Delete a purchase order's line item.

If there are existing matches made to an invoice that has been posted, you will
not be able to delete the purchase order line item.

After deleting the purchase order line item, you **must** update the the
purchase order's `amount` field. This should be done once you are finished
manipulating all of the line items.

Once you are finished manipulating the purchase order you will need to call
[Process Purchase Order](#process-purchase-order) to kick off the matching
process based on the updated information.

### Example

```bash
curl --location --request DELETE 'https://api.us.dev.vic.ai/v0/purchaseOrdersLineItems/9b4810da-5959-47b6-91db-4b7d76a67232' \
    --header 'Accept: application/json' \
    --header 'Authorization: Bearer <Bearer Token>'
```

[createPurchaseOrder]: <../../vic.api.v0.html#/PurchaseOrders/createPurchaseOrder>
[getPurchaseOrder]: <../../vic.api.v0.html#/PurchaseOrders/getPurchaseOrder>
[deletePurchaseOrder]: <../../vic.api.v0.html#/PurchaseOrders/deletePurchaseOrder>
[updatePurchaseOrder]: <../../vic.api.v0.html#/PurchaseOrders/updatePurchaseOrder>
[processPurchaseOrder]: <../../vic.api.v0.html#/PurchaseOrders/processPurchaseOrder>
[createPurchaseOrderLineItem]: <../../vic.api.v0.html#/PurchaseOrders/createPurchaseOrderLineItem>
[updatePurchaseOrderLineItem]: <../../vic.api.v0.html#/PurchaseOrders/updatePurchaseOrderLineItem>
[deletePurchaseOrderLineItem]: <../../vic.api.v0.html#/PurchaseOrders/deletePurchaseOrderLineItem>
