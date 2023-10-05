# Vic.ai API Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

- Added `listPurchaseOrders` operation.
- Added `refNumber` to `TrainingInvoiceUpsert` required fields.
- Changed `issuedOn` to be non nullable for `#/components/schemas/CreateInvoiceLineItem`.
- Removed `costAccountExternalId` from `TrainingInvoiceUpsert` required fields.
- Renamed `#/components/schemas/VendorRef` to `#/components/schemas/VendorLookup`.
- Added new `#/components/schemas/InvoiceRef`.

## v0.17.1

- Added `paymentTermId` to `#/components/schemas/Vendor`.
- Added `paymentTermId` to `#/components/schemas/VendorUpsert`.
- Added `paymentTermId` to `#/components/schemas/VendorCallback`.

## v0.17.0

- Allow nullable `productNumber` for `#/components/schemas/CreatePurchaseOrderItem`.
- Allow nullable `productNumber` for `#/components/schemas/CreatePurchaseOrderLineItem`.
- Allow nullable `productNumber` for `#/components/schemas/UpdatePurchaseOrderLineItem`.
- Allow nullable `productNumber` for `#/components/schemas/PurchaseOrderLineItem`.
- Fix definition of `requestor` for  `#/compnents/schemas/CreatePurchaseOrder` to be a `PurchaseOrderRequestor` object.
- Added `selfAssessedUseTaxAmount` to `#/components/schemas/Invoice`.
- Added `selfAssessedUseTaxAccount` to `#/components/schemas/Invoice`.
- Added `createTaxCode` operation.
- Added `getTaxCodes` operation.

## v0.16.0

- Replaced `bolNumber` with `bolNumbers` for `#/components/schemas/Invoice`.
- Replaced `bolNumber` with `bolNumbers` for `#/components/schemas/TrainingInvoice`.
- Replaced `bolNumber` with `bolNumbers` for `#/components/schemas/CreateInvoice`.
- Replaced `bolNumber` with `bolNumbers` for `#/components/schemas/TrainingInvoiceUpsert`.
- Added `typeName` to `#/components/schemas/Dimension`.
- Added `typeName` to `#/components/schemas/DimensionUpsert`.
- Added support for managing payment terms.

## v0.14.1

- Removed pattern constraint from `#/components/schemas/Account`.
- Removed pattern constraint from `#/components/schemas/AccountUpsert`.
- Removed pattern constraint from `#/components/schemas/CostAccountInfo`.
- Added `#/components/schemas/VendorManager`.
- Allow passing `managers` (`#/components/schemas/VendorManager`) to `#/components/schemas/VendorUpsert`.

## v0.14.0

- Added new schema `#/components/schemas/MatchItem`.
- Added `poItemsMatched` to `#/components/schemas/` which is an array of `MatchItem`s.
- Added `invoiceItemsMatched` to `#/components/schemas/PurchaseOrderLineItem` which is an array of `MatchItem`s.

## v0.13.0

For managing tags:

- Added `GET /v0/tags` to get all tags.
- Added `POST /v0/tag` to create new tags.
- Added `PUT /v0/tag/{id}` to update tags.
- Added `DELETE /v0/tag/{id}` to delete tags.

For managing vendor tags:

- Added `GET /v0/vendorTags` to get all vendor tags.
- Added `POST /v0/vendorTag` to create new vendor tags.
- Added `DELETE /v0/vendorTag/{id}` to delete vendor tags.

## v0.12.2
### V0
- Allow passing `bolNumber` (bill of lading number) to `#/components/schemas/CreateInvoice`, `#/components/schemas/TrainingInvoice` and `#/components/schemas/TrainingInvoiceUpsert`
- Allow passing `requestor` (`#/components/schemas/PurchaseOrderRequestor`) to `#/components/schemas/CreatePurchaseOrder` and `#/components/schemas/UpdatePurchaseOrder`

## v0.12.1
### V0
- Allow negative values for `quantityRequested`, `quantityReceived`, `quantityInvoiced`, `unitAmount`, and `lineItemTotal`.


## v0.12.0
### V0
- Added `lineNumber` to `#/components/schemas/CreatePurchaseOrderItem`
- Added `lineNumber` to `#/components/schemas/PurchaseOrderItem`
- Renamed `quantity` to `quantityRequested` in `#/components/schemas/CreatePurchaseOrderItem`
- Renamed `quantity` to `quantityRequested` in `#/components/schemas/PurchaseOrderItem`
- Added `quantityReceived` to `#/components/schemas/CreatePurchaseOrderItem`
- Added `quantityReceived` to `#/components/schemas/PurchaseOrderItem`
- Added `quantityInvoiced` to `#/components/schemas/InvoiceLineItem`
- Added `quantityInvoiced` to `#/components/schemas/CreateInvoiceLineItem`
- Added `quantityInvoiced` to `#/components/schemas/TrainingInvoiceLineItemUpsert`
- Added `lineItemTotal` to `#/components/schemas/InvoiceLineItem`
- Added `poLineNumber` to `#/components/schemas/InvoiceLineItem`
- Added `poNumber` to `#/components/schemas/InvoiceLineItem`
- Renamed `#/components/schemas/PurchaseOrderItem` to `#/components/schemas/PurchaseOrderLineItem`
- Changed `vendor` is now required for `#/components/schemas/CreatePurchaseOrder`
- Changed `vendor` is now required for `#/components/schemas/UpdatePurchaseOrder`
- Fixed missing `externalId` by adding it to `#/components/schemas/Invoice`


## v0.11.0
### V0
- Added `accountNumber` to `#/components/schemas/CreateInvoice`
- Added `servicePeriodStart` to `#/components/schemas/CreateInvoice`
- Added `servicePeriodEnd` to `#/components/schemas/CreateInvoice`
- Added `accountNumber` to `#/components/schemas/TrainingInvoiceUpsert`
- Added `servicePeriodStart` to `#/components/schemas/TrainingInvoiceUpsert`
- Added `servicePeriodEnd` to `#/components/schemas/TrainingInvoiceUpsert`


## v0.10.0
### V0
- Added `createDimension` operation.
- `invoiceTransfer` callback will now receive the same payload as the `invoicePost` callback.

## v0.9.0
### V0
- Added `typeExternalId` to `#/components/schemas/DimensionRef`.
- Expanded documentation for `#/components/schemas/DimensionRef`.
- Deprecated `dimensionsExternalIds` in `#/components/schemas/TrainingInvoiceLineItemUpsert`. Instead please use the `dimensions` field which has the same functionality as the `createInvoice` operation.

### V1
- Dropped all support for V1. We have not offered it in production since it was documented. In the future we will bring it back.


## v0.8.0
### V0
- Deprecate singular resource path names in favor of pluralized paths. Old paths will be supported for at least 6 months. We recommend changing to the newer paths as soon as possible.
- Changed `/v0/account/{id}` to `/v0/accounts/{id}`
- Changed `/v0/dimension/{id}` to `/v0/dimensions/{id}`
- Changed `/v0/invoice/{id}/confirm` to `/v0/invoices/{id}/confirm`
- Changed `/v0/invoice/{id}/document` to `/v0/invoices/{id}/document`
- Changed `/v0/invoice/{id}/lineItems` to `/v0/invoices/{id}/lineItems`
- Changed `/v0/invoice/{id}/process` to `/v0/invoices/{id}/process`
- Changed `/v0/invoice/{id}/reject` to `/v0/invoices/{id}/reject`
- Changed `/v0/invoice/{id}` to `/v0/invoices/{id}`
- Changed `/v0/trainingInvoice/{id}/document` to `/v0/trainingInvoices/{id}/document`
- Changed `/v0/trainingInvoice/{id}` to `/v0/trainingInvoices/{id}`
- Changed `/v0/vatCode/{id}` to `/v0/vatCodes/{id}`
- Changed `/v0/vendor/{id}/errors` to `/v0/vendors/{id}/errors`
- Changed `/v0/vendor/{id}` to `/v0/vendors/{id}`
- Add `typeExternalId` to `#/components/schemas/Dimension`.
- Add `typeExternalId` to `#/components/schemas/DimensionUpsert`.
- Changed set max length for `type` on `#/components/schemas/Dimension`.
- Changed set max length for `type` on `#/components/schemas/DimensionUpsert`.
- Changed set max length for `name` on `#/components/schemas/Dimension`.
- Changed set max length for `name` on `#/components/schemas/DimensionUpsert`.
- Changed `name` to be required for `#/components/schemas/DimensionUpsert`.


## v0.7.0
### V0
- Remove unused `#/components/schemas/QueryCommon`.
- Remove unused `#/components/schemas/UpsertCommon`.
- Rename `#/components/schemas/CreateInvoiceVendor` to `#/components/schemas/VendorRef`.
- Add `#/components/schemas/Currency` to represent ISO-4217 codes.
- Add `POST /v0/purchaseOrders` to create purchase orders.
- Add `GET /v0/purchaseOrders/{purchaseOrderId}` to get a purchase order.
- Add `POST /v0/purchaseOrders/{purchaseOrderId}/process` to start the matching process.
- Add `DELETE /v0/purchaseOrders/{purchaseOrderId}` to delete purchase orders.


## v0.6.1
### V0
- Add `#/components/schemas/PaymentInfoMethod` enum.
- Add `#/components/schemas/InternationalBankAccount` object.
- Allow `bic` and `iban` to be nullable on `#/components/schemas/InternationalBankAccount`.
- Fold `#/components/schemas/PaymentInfoUS`, `#/components/schemas/PaymentInfoNO`, and `#/components/schemas/PaymentInfoSE` into a single `#/components/schemas/PaymentInfo` definition.
- Allow most `#/components/schemas/PaymentInfo` fields to be nullable.
- Fold `#/components/schemas/InvoiceLineItemInfoUS`, `#/components/schemas/InvoiceLineItemInfoSE`, and `#/components/schemas/InvoiceLineItemInfoNO` into `#/components/schemas/InvoiceLineItemInfo`.
- Allow `#/components/schemas/InvoiceLineItemInfo` fields to be nullable.
- Allow `invoiceLineItemInfo` on `#/components/schemas/TrainingInvoiceLineItemUpsert` to be nullable.
- Allow `invoiceLineItemInfo` on `#/components/schemas/InvoiceLineItem` to be nullable.
- Remove required fields from `#/components/schemas/Dimension`.


## v0.6.0
### V0
- Lift all error responses to the `#/components/responses` section.
- Replace `obtainToken` response with `#/components/responses/TokenCreatedResponse`
- Replace `healthCheck` response with `#/components/responses/HealthyResponse`
- Replace `listAccounts` response with `#/components/responses/AccountsResponse`
- Replace `getAccount` response with `#/components/responses/AccountResponse`
- Replace `upsertAccount` response with `#/components/responses/AccountUpsertedResponse`
- Replace `deleteAccount` response with `#/components/responses/AccountDeletedResponse`
- Replace `listDimensions` response with `#/components/responses/DimensionsResponse`
- Replace `getDimension` response with `#/components/responses/DimensionResponse`
- Replace `upsertDimension` response with `#/components/responses/DimensionCreatedResponse` and `#/components/responses/DimensionUpdatedResponse`
- Replace `deleteDimension` response with `#/components/responses/DimensionDeletedResponse`
- Replace `listVendors` response with `#/components/responses/VendorsResponse`
- Replace `getVendor` response with `#/components/responses/VendorResponse`
- Replace `upsertVendor` response with `#/components/responses/VendorCreatedResponse` and `#/components/responses/VendorUpdatedResponse`
- Replace `deleteVendor` response with `#/components/responses/VendorDeletedResponse`
- Replace `setVendorRemoteErrors` response with `#/components/responses/VendorRemoteErrorsUpdatedResponse`
- Replace `clearVendorRemoteErrors` response with `#/components/responses/VendorRemoteErrorsClearedResponse`
- Replace `listInvoices` response with `#/components/responses/InvoicesResponse`
- Replace `createInvoice` response with `#/components/responses/InvoiceCreatedResponse`
- Replace `getInvoice` response with `#/components/responses/InvoiceResponse`
- Replace `ackInvoice` response with `#/components/responses/InvoiceResponse`
- Replace `deleteInvoice` response with `#/components/responses/InvoiceDeletedResponse`
- Replace `startProcessingInvoice` response with `#/components/responses/InvoiceResponse`
- Replace `getInvoiceDocument` response with `#/components/responses/InvoiceDocumentResponse`
- Replace `confirmInvoice` response with `#/components/responses/InvoiceConfirmedResponse`
- Replace `rejectInvoice` response with `#/components/responses/InvoiceRejectedResponse`
- Replace `getInvoicelineItems` response with `#/components/responses/InvoiceLineItemsResponse`
- Replace `listTrainingInvoices` response with `#/components/responses/TrainingInvoicesResponse`
- Replace `upsertTrainingInvoice` response with `#/components/responses/TrainingInvoiceUpsertedResponse`
- Replace `deleteTrainingInvoice` response with `#/components/responses/TrainingInvoiceDeletedResponse`
- Replace `getTrainingInvoiceDocument` response with `#/components/responses/TrainingInvoiceDocumentResponse`
- Replace `listVatCodes` response with `#/components/responses/VatCodesResponse`
- Replace `getVatCode` response with `#/components/responses/VatCodeResponse`
- Replace `upsertVatCode` response with `#/components/responses/VatCodeUpsertedResponse`
- Replace `deleteVatCode` response with `#/components/responses/VatCodeDeletedResponse`
- Replace `getSubscription` response with `#/components/responses/SubscriptionResponse`
- Replace `subscribe` response with `#/components/responses/SubscriptionUpsertedResponse`
- Replace `unsubscribe` response with `#/components/responses/SubscriptionDeletedResponse`
- Replace `getCostAccounts` response with `#/components/responses/CostAccountsResponse`


## v0.5.0
### V0
- Replace `dimensions` ref to `#/components/schemas/Dimension`.


## v0.4.0
### V0
- Removed `requiredDimensionsExternal` from `#/components/schemas/Account`. This field was never supported.
- Removed `parentAccountExternalId` from `#/components/schemas/Account`. This field was never supported.
- Removed `requiredDimensionsInternal` from `#/components/schemas/Account`. This field was never supported.
- Removed `parentAccountInternalId` from `#/components/schemas/Account`. This field was never supported.
- Removed `requiredDimensionsExternal` from `#/components/schemas/AccountUpsert`. This field was never supported.
- Removed `parentAccountExternalId` from `#/components/schemas/AccountUpsert`. This field was never supported.
- Removed `parentDimensionExternalId` from `#/components/schemas/Dimension`. This field was never supported.
- Removed `parentDimensionInternalId` from `#/components/schemas/Dimension`. This field was never supported.
- Removed `parentDimensionExternalId` from `#/components/schemas/DimensionUpsert`. This field was never supported.


## v0.3.19
### V0
- Changed `Account` `number` to only permit the pattern `^\d+$`.


## v0.3.18
### V0
- Added `name` to `#/components/schemas/DimensionRef`


## v0.3.17
### V0
- Added `POST /v0/invoice/{id}/reject`.
- Added `GET /v0/subscription` to fetch the currently configued V0 subscription.
- Added `customFields` to `#/components/schemas/Invoice`.


## v0.3.16
### V1
- Added `POST /v1/purchase_orders` to create a purchase order.
- Added `GET /v1/purchase_orders/:id` to get a specific purchase order.


## v0.3.15
### V0
- Added `description` to `#/components/schemas/Vendor`.
- Added `VendorTaxInfo` to `#/components/schemas/VendorTaxInfo`.
- Removed `#/components/schemas/TaxInfoUS`. Has been combined to `#/components/schemas/VendorTaxInfo`.
- Removed `#/components/schemas/TaxInfoSE`. Has been combined to `#/components/schemas/VendorTaxInfo`.
- Removed `#/components/schemas/TaxInfoNO`. Has been combined to `#/components/schemas/VendorTaxInfo`.


## v0.3.14
### Added in V1
- Added `POST /v1/purchase_orders` to create a purchase order.
- Added `GET /v1/purchase_orders/{id}` to get a purchase order.
- Added `#/components/schemas/Monetary` to represent monetary values.
- Added `#/components/schemas/Currency` to represent currency values.
- Added `#/components/schemas/DimensionRef`.
- Added `#/components/schemas/PurchaseOrder`.
- Added `#/components/schemas/PurchaseOrderItem`.
- Added `#/components/schemas/PurchaseOrderStatus`.

### Changed in V1
- Reuse `#/components/schemas/CreateSubscription` for the `#/components/requestBodies/CreateSubscription` definition.
- Reuse `#/components/schemas/UpdateSubscription` for the `#/components/requestBodies/UpdateSubscription` definition.



## v0.3.13
### Added in V1
- Added `GET /v1/subscriptions` to list subscriptions.
- Added `POST /v1/subscriptions` to create a subscription.
- Added `GET /v1/subscriptions/{id}` to get the details of a subscription.
- Added `PUT /v1/subscriptions/{id}` to update a subscription.
- Added `DELETE /v1/subscriptions/{id}` to delete a subscription.


## v0.3.12
### Added in V0
- Added `POST /v0/invoice/{id}/confirm` to confirm invoices.


## v0.3.11
### Changed in V0
- Expand `#/components/schemas/Account` definition to use less inheritance.
- Expand `#/components/schemas/AccountUpsert` definition to use less inheritance.
- Expand `#/components/schemas/Dimension` definition to use less inheritance.
- Expand `#/components/schemas/DimensionUpsert` definition to use less inheritance.
- Expand `#/components/schemas/Invoice` definition to use less inheritance.
- Expand `#/components/schemas/InvoiceLineItem` definition to use less inheritance.
- Expand `#/components/schemas/TrainingInvoice` definition to use less inheritance.
- Expand `#/components/schemas/VatCode` definition to use less inheritance.
- Expand `#/components/schemas/VatCodeUpsert` definition to use less inheritance.
- Expand `#/components/schemas/Vendor` definition to use less inheritance.
- Expand `#/components/schemas/VendorUpsert` definition to use less inheritance.
- Expand `#/components/schemas/VendorConfirm` definition to use less inheritance.
- Expand `#/components/schemas/VendorCallback` definition to use less inheritance.

### Removed in V0
- Removed `#/components/schemas/AccountCommon`.
- Removed `#/components/schemas/DimensionCommon`.
- Removed `#/components/schemas/InvoiceCommon`.
- Removed `#/components/schemas/InvoiceFetched`.
- Removed `#/components/schemas/InvoiceRequirable`.
- Removed `#/components/schemas/InvoiceLineItemCommon`.
- Removed `#/components/schemas/VatCodeCommon`.
- Removed `#/components/schemas/VatCodeRequirable`.
- Removed `#/components/schemas/VendorRequirable`.
- Removed `#/components/schemas/VendorCommon`.


## v0.3.10
### Added in V0
- Added `DELETE /v0/invoice/{id}` to delete an invoice.


## v0.3.9
### Added in V0
- Added `bban` to `#/components/schemas/PaymentInfoSE`
- Added `bban` to `#/components/schemas/PaymentInfoNO`
- Added `BBAN` to the allowed enum for `defaultMethod` on `#/components/schemas/PaymentInfoSE`
- Added `BBAN` to the allowed enum for `defaultMethod` on `#/components/schemas/PaymentInfoNO`


## v0.3.8
### Added in V0
- Added `source` to `#/components/schemas/Invoice`.
- Added `vendor` to `#/components/schemas/Invoice`.
- Added `paymentRef` to `#/components/schemas/Invoice`.
- Added `paymentTerm` to `#/components/schemas/Invoice`.
- Added `dimensions` to `#/components/schemas/InvoiceLineItem`.
- Added `costAccount` to `#/components/schemas/InvoiceLineItem`.
- Added `vat` to `#/components/schemas/InvoiceLineItem`.
- Added `GET /v0/invoice/{id}/lineItems` to fetch ungrouped line items.

### Changed in V0
- Marked `kid` as deprecated in `#/components/schemas/InvoiceInfoNO`. The `paymentRef` field on `#/components/schemas/Invoice` should be used instead.
- Marked `dimensionsInternalIds` as deprecated in `#/components/schemas/InvoiceLineItem`. Use `dimensions` instead.
- Marked `dimensionsExternalIds` as deprecated in `#/components/schemas/InvoiceLineItem`. Use `dimensions` instead.
- Marked `costAccountInternalId` as deprecated in `#/components/schemas/InvoiceLineItem`. Use `costAccount` instead.
- Marked `costAccountExternalId` as deprecated in `#/components/schemas/InvoiceLineItem`. Use `costAccount` instead.


## v0.3.7
### Changed in V0
- Make `vendorExternalId` not required for `#/components/schemas/Invoice`.


## v0.3.6
### Changed in V0
- Allow `createInvoice` to have `lineItems` specified.


## v0.3.5
### Added in V0
- `useSystem` directive to `startProcessingInvoice`
- `useSystem` directive to `uploadDocumentInvoice`

### Changed in V0
- `externalId` is no longer required for `createInvoice`.


## v0.3.4
### Added in V0
- Added ability to filter vendors by `state` for `GET /v0/vendors`.


## v0.3.3
### Added in V0
- Added `POST /v0/invoices` to begin the creation of an invoice.
- Added `POST /v0/invoice/{id}/document` to attach a document to an invoice.
- Added `POST /v0/invoice/{id}/process` to notify Vic that the invoice may now start being processed.

### Removed in V0
- Removed `application/json` request body from `PUT /v0/trainingInvoice/{id}`. All requests should just be `multipart/form-data`.


## v0.3.0
## Changed in V0
- Simplified `Vendor.confirmedAt` field.

## Removed in V0
- Removed `NullableInternalId`. Replaced with `allOf: ["#/components/schemas/InternalId"]`; followed by a `nullable: true`.
- Removed `NullableExternalId`. Replaced with `allOf: ["#/components/schemas/ExternalId"]`; followed by a `nullable: true`.
- Removed `NullableObject`. Replaced with `allOf: ["#/components/schemas/ExternalData"]`; followed by a `nullable: true`.
- Removed `NullableString`. Replaced with `type: string`; followed by a `nullable: true`.
- Removed `InvoiceInfoUS`. No replacement added.
- Removed `InvoiceInfoSE`. No replacement added.


## v0.2.14
### Changed in V0
- Simplified `InvoiceCommon.invoiceInfo` to reference `InvoiceInfoNO`

### Removed in V0
- Removed extra `VendorState` definition.


## v0.2.13
### Added in V0
- `GET /v0/costAccounts` - Ability to get all the `CostAccount` for a company.
- Added `200` response to `PUT /v0/vendor/{id}` definition when the vendor has
  been updated, and `201` when the vendor has been created.


## v0.2.12
### Added in V0
- Added `errors` to `#/components/schemas/Vendor` to convey errors that occurred in the ERP system.
- `POST /v0/vendor/{id}/errors` - Ability to set `errors` on a vendor.
- `DELETE /v0/vendor/{id}/errors` - Ability to clear `errors` on a vendor.

### Changed in V0
- `confirmedAt` on `#/components/schemas/Vendor` are allowed to be null.
