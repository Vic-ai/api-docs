# Vic.ai API Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased


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
