# Vic.ai API Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

### Changed
- Expand `#/components/schemas/Account` to use less inheritance.
- Expand `#/components/schemas/AccountUpsert` to use less inheritance.
- Expand `#/components/schemas/Dimension` to use less inheritance.
- Expand `#/components/schemas/DimensionUpsert` to use less inheritance.
- Expand `#/components/schemas/Invoice` to use less inheritance.
- Expand `#/components/schemas/TrainingInvoice` to use less inheritance.
- Expand `#/components/schemas/VatCode` to use less inheritance.
- Expand `#/components/schemas/VatCodeUpsert` to use less inheritance.
- Expand `#/components/schemas/Vendor` definition to use less inheritance.
- Expand `#/components/schemas/VendorUpsert` definition to use less inheritance.
- Expand `#/components/schemas/VendorConfirm` definition to use less inheritance.


## v0.3.10

### Added
- Added `DELETE /v0/invoice/{id}` to delete an invoice.


## v0.3.9
### Added
- Added `bban` to `#/components/schemas/PaymentInfoSE`
- Added `bban` to `#/components/schemas/PaymentInfoNO`
- Added `BBAN` to the allowed enum for `defaultMethod` on `#/components/schemas/PaymentInfoSE`
- Added `BBAN` to the allowed enum for `defaultMethod` on `#/components/schemas/PaymentInfoNO`


## v0.3.8
### Added
- Added `source` to `#/components/schemas/Invoice`.
- Added `vendor` to `#/components/schemas/Invoice`.
- Added `paymentRef` to `#/components/schemas/Invoice`.
- Added `paymentTerm` to `#/components/schemas/Invoice`.
- Added `dimensions` to `#/components/schemas/InvoiceLineItem`.
- Added `costAccount` to `#/components/schemas/InvoiceLineItem`.
- Added `vat` to `#/components/schemas/InvoiceLineItem`.
- Added `GET /v0/invoice/{id}/lineItems` to fetch ungrouped line items.

### Changed
- Marked `kid` as deprecated in `#/components/schemas/InvoiceInfoNO`. The `paymentRef` field on `#/components/schemas/Invoice` should be used instead.
- Marked `dimensionsInternalIds` as deprecated in `#/components/schemas/InvoiceLineItem`. Use `dimensions` instead.
- Marked `dimensionsExternalIds` as deprecated in `#/components/schemas/InvoiceLineItem`. Use `dimensions` instead.
- Marked `costAccountInternalId` as deprecated in `#/components/schemas/InvoiceLineItem`. Use `costAccount` instead.
- Marked `costAccountExternalId` as deprecated in `#/components/schemas/InvoiceLineItem`. Use `costAccount` instead.


## v0.3.7
### Changed
- Make `vendorExternalId` not required for `#/components/schemas/Invoice`.


## v0.3.6
### Changed
- Allow `createInvoice` to have `lineItems` specified.


## v0.3.5
### Added
- `useSystem` directive to `startProcessingInvoice`
- `useSystem` directive to `uploadDocumentInvoice`

### Changed
- `externalId` is no longer required for `createInvoice`.


## v0.3.4
### Added
- Added ability to filter vendors by `state` for `GET /v0/vendors`.


## v0.3.3
### Added
- Added `POST /v0/invoices` to begin the creation of an invoice.
- Added `POST /v0/invoice/{id}/document` to attach a document to an invoice.
- Added `POST /v0/invoice/{id}/process` to notify Vic that the invoice may now start being processed.

### Removed
- Removed `application/json` request body from `PUT /v0/trainingInvoice/{id}`. All requests should just be `multipart/form-data`.


## v0.3.0
## Changed
- Simplified `Vendor.confirmedAt` field.

## Removed
- Removed `NullableInternalId`. Replaced with `allOf: ["#/components/schemas/InternalId"]`; followed by a `nullable: true`.
- Removed `NullableExternalId`. Replaced with `allOf: ["#/components/schemas/ExternalId"]`; followed by a `nullable: true`.
- Removed `NullableObject`. Replaced with `allOf: ["#/components/schemas/ExternalData"]`; followed by a `nullable: true`.
- Removed `NullableString`. Replaced with `type: string`; followed by a `nullable: true`.
- Removed `InvoiceInfoUS`. No replacement added.
- Removed `InvoiceInfoSE`. No replacement added.


## v0.2.14
### Changed
- Simplified `InvoiceCommon.invoiceInfo` to reference `InvoiceInfoNO`

### Removed
- Removed extra `VendorState` definition.


## v0.2.13
### Added
- `GET /v0/costAccounts` - Ability to get all the `CostAccount` for a company.
- Added `200` response to `PUT /v0/vendor/{id}` definition when the vendor has
  been updated, and `201` when the vendor has been created.


## v0.2.12
### Added
- Added `errors` to `#/components/schemas/Vendor` to convey errors that occurred in the ERP system.
- `POST /v0/vendor/{id}/errors` - Ability to set `errors` on a vendor.
- `DELETE /v0/vendor/{id}/errors` - Ability to clear `errors` on a vendor.

### Changed
- `confirmedAt` on `#/components/schemas/Vendor` are allowed to be null.
